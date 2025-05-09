# -*- coding: utf-8 -*-
"""
Batch Inference for Acid-Base Strength Tasks 
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
    ("Benzoic_acid.png", "Phenol.png"),
    ("Formic_acid.png", "Acetic-acid.png"),
    ("Ammonia.png", "MeNH2.png"),
    ("Cytosine.png", "Adenine.png"),
    ("H2O.png", "Methanol.png"),
    ("Caffeine.png", "Morphine.png"),
    ("Ibuprofen.png", "Salicylic-acid.png"),
    ("Imidazole_full.png", "Pyridine-full.png"),
    ("Nicotinamid.png", "Histamine.png"),
    ("Purine.png", "Uracil.png"),
]

CoTs = ["Baseline", "Stepwise", "Visual_first", "Explanation_first"]

# --- Step 3: Define Prompts (placeholder for now) ---
prompts = [
    "Which molecule is a stronger acid or base, the first or the second? Why?",  # Baseline
    "Step 1: Identify the most acidic or basic site in each molecule. Step 2: Consider how stable the molecule is after gaining or losing a proton. Step 3: Say which molecule is stronger, the first or the second, and explain why.",  # Stepwise
    "Examine the image only. Based on visible atom types and bonds, which molecule appears stronger in acid/base behavior? End by stating 'first' or 'second'.",  # Visual-first
    "The ability to stabilize charge after proton gain or loss determines acid/base strength. Analyze both molecules, then conclude which is stronger: first or second."  # Explanation-first
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
output_csv = "Task2_1V_outputs.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image1", "image2", "prompt_type", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"\n✅ All results saved to {output_csv}")
