# -*- coding: utf-8 -*-
"""
Batch Inference for Functional Group Reactivity Comparison (Task 3)
10 Image Pairs × 10 Visual_first Prompts using Llava-OneVision
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

# --- Step 0: Check CUDA availability ---
print(f"🔍 GPU available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"🖥️  Using GPU: {torch.cuda.get_device_name(0)}")
else:
    print("⚠️  GPU not detected — inference will run on CPU (much slower).")

# --- Step 1: Load Model and Processor ---
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)

model = LlavaOnevisionForConditionalGeneration.from_pretrained(
    "llava-hf/llava-onevision-qwen2-7b-ov-hf",
    quantization_config=quantization_config,
    device_map="auto"
)

print(f"✅ Model is on: {next(model.parameters()).device}")

processor = LlavaOnevisionProcessor.from_pretrained("llava-hf/llava-onevision-qwen2-0.5b-ov-hf")
processor.tokenizer.padding_side = "left"

# --- Step 2: Correct Task 2 Image Pairs ---
dataset_folder = "images"

# 3 pairs samples
image_pairs = [
    ("Ammonia.png", "Methanol.png"),
    ("MeNH2.png", "Aniline.png"),
    ("Imidazole_full.png", "Pyridine-full.png")
]

# --- Step 3: Top 10 Visual-first Prompts for Acid/Base Comparison ---
'''
visual_first_prompts = []
'''
visual_first_prompts = [
    "Look at both molecular structures. Identify the atoms with lone pairs or negative charge. Use this to determine which one has more available electron density for nucleophilic attack.",
    "Visually analyze the molecules. Which one appears more compact or less hindered? Which atom looks more exposed for attack? Use these clues to pick the stronger nucleophile.",
    "Start by inspecting both molecules: Where are the lone pairs? Are any atoms negatively charged? Based on the visuals, which site looks more reactive?",
    "From the image, focus on the reactive centers. Do you see bulky groups that block attack? Do you see resonance that spreads out charge? Pick the more reactive nucleophile.",
    "Check the structures: Which molecule has a more exposed, electron-rich site? Which one looks less crowded? Use visual evidence to answer which is the better nucleophile.",
    "By examining the drawings, identify electron-dense regions. Are they surrounded by bulky groups or free to react? Use what you see to decide.",
    "Look at the atoms likely to act as nucleophiles. Are there delocalized electrons nearby? Are those atoms buried or exposed? Based on what you see, choose the better nucleophile.",
    "Focus on the spatial layout. Does one molecule have a more accessible lone pair? Which one has less steric hindrance? Visualize the attack route and pick the better candidate.",
    "Inspect both images for resonance patterns and groups nearby the nucleophilic center. Which one looks better suited to donate electrons?",
    "Based on visual inspection, which molecule’s reactive site is freer to act as a nucleophile? Consider electron density and bulkiness in your answer."
]


cot_types = ["Visual_first"] * len(visual_first_prompts)

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
    
    for idx, prompt_text in enumerate(visual_first_prompts):
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
        
        output = model.generate(**inputs, **generate_kwargs)
        generated_text = processor.batch_decode(output, skip_special_tokens=True)[0]
        
        results.append({
            "image1": img1_name,
            "image2": img2_name,
            "prompt_type": cot_types[idx],
            "prompt_number": idx + 1,
            "prompt_text": prompt_text,
            "generated_text": generated_text
        })

# --- Step 5: Save to CSV ---
output_csv = "Task2_VisualFirst_Res.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image1", "image2", "prompt_type", "prompt_number", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"\n✅ All results saved to {output_csv}")
