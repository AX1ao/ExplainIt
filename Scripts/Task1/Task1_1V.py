# -*- coding: utf-8 -*-
"""
Batch Inference for EAS Reactivity Tasks 
(10 Pairs × 4 Prompts) using Llava-OneVision
"""

import sys
sys.path.insert(0, '/scratch/yx3493/llava_libs')
import os
os.environ["TRITON_CACHE_DIR"] = "/scratch/yx3493/.triton_cache"
os.environ["HF_HOME"] = "/scratch/yx3493/.hf_cache"
import csv
from transformers import BitsAndBytesConfig, LlavaOnevisionForConditionalGeneration, LlavaOnevisionProcessor
from PIL import Image
import torch

# --- Step 1: Load Model and Processor ---
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)

model = LlavaOnevisionForConditionalGeneration.from_pretrained(
    "llava-hf/llava-onevision-qwen2-7b-ov-hf",
    quantization_config=quantization_config,
    device_map='auto'
)

processor = LlavaOnevisionProcessor.from_pretrained("llava-hf/llava-onevision-qwen2-0.5b-ov-hf")
processor.tokenizer.padding_side = "left"

# --- Step 2: Set Dataset Folder and Image Pairs ---
dataset_folder = "images"

image_pairs = [
    ("Aniline.png", "Nitrobenzene.png"),
    ("Benzene.png", "Toluene.png"),
    ("Benzaldehyde.png", "Benzoic_acid.png"),
    ("Pyridine-full.png", "Benzene.png"),
    ("Pyrrole-full.png", "Benzene.png"),
    ("Phenol.png", "Benzene.png"),
    ("Salicylic-acid.png", "Benzoic_acid.png"),
    ("Nitrobenzene.png", "Ozone.png"),
    ("Pyrrole-numbered.png", "Pyridine-full.png"),
    ("Morphine.png", "Caffeine.png")
]

CoTs = ["Baseline", "Stepwise", "Visual_first", "Explanation_first"]

# --- Step 3: Define Prompts (placeholder for now) ---
prompts = [
    "Which molecule is more reactive toward electrophilic aromatic substitution, the first or the second? Why?",  # Baseline
    "First, note if the ring has electron-donating substituents. Then, note if it has electron-withdrawing substituents. Finally, determine which ring is more reactive toward electrophiles.",  # Stepwise
    "Observe visible features: are there -OH, -NH₂, or -NO₂ groups? Count and compare electron-donating versus electron-withdrawing groups for both molecules.",  # Visual-first
    "Consider the net electronic effect (donating vs withdrawing) based on the visible substituents. Then predict which molecule will react faster toward EAS."   # Explanation-first
]

# --- Step 4: Run Inference ---
results = []

generate_kwargs = {
    "max_new_tokens": 300,
    "do_sample": True,
    "top_p": 0.9
}

for img1_name, img2_name in image_pairs:
    image1 = Image.open(os.path.join(dataset_folder, img1_name)).convert("RGB")
    image2 = Image.open(os.path.join(dataset_folder, img2_name)).convert("RGB")
    
    for idx, prompt_text in enumerate(prompts):
        # Build conversation with two images
        conversation = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt_text},
                    {"type": "image"},
                    {"type": "image"},
                ],
            },
        ]
        
        prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)
        inputs = processor(images=[image1, image2], text=prompt, padding=True, return_tensors="pt").to(model.device, torch.float16)
        
        # Generate
        output = model.generate(**inputs, **generate_kwargs)
        generated_text = processor.batch_decode(output, skip_special_tokens=True)[0]
        
        # Save result
        results.append({
            "image1": img1_name,
            "image2": img2_name,
            "prompt_type": CoTs[idx],
            "prompt_text": prompt_text,
            "generated_text": generated_text
        })

# --- Step 5: Save Results to CSV ---
output_csv = "Task1_1V_outputs.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image1", "image2", "prompt_type", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"\n✅ All results saved to {output_csv}")
