# -*- coding: utf-8 -*-
"""
Batch Inference for Acid/Base Strength Comparison (Task 2)
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
    ("Benzoic_acid.png", "Phenol.png"),
    ("Formic_acid.png", "Acetic-acid.png"),
    ("Ammonia.png", "MeNH2.png"),
]

# --- Step 3: Top 10 Visual-first Prompts for Acid/Base Comparison ---
'''
visual_first_prompts = [
    "By looking at the structure, identify which molecule has more electron-donating or withdrawing groups. Use that to decide which one is more acidic or basic.",
    "Just from the image, which molecule appears more likely to donate a proton? Which one looks better at accepting one?",
    "Visually examine the functional groups in both molecules. Which ones suggest a stronger acid or base?",
    "Check for the presence of acidic hydrogens and lone pairs. Based on what you see, which molecule is more reactive in acid-base terms?",
    "Focus on visible lone pairs and polar bonds. Which molecule looks more likely to stabilize charge after gaining or losing a proton?",
    "Purely from visual inspection, which molecule seems better equipped to act as an acid or a base? Consider groups and atom types.",
    "Look for electronegative atoms like oxygen or nitrogen. Which molecule uses them to enhance acidity or basicity?",
    "Based on what’s visible in the image, which molecule has features that suggest stronger acid/base behavior?",
    "Observe both molecules and visually compare their reactive centers. Which one looks more prone to donate or accept protons?",
    "Without any external data, visually decide: which molecule’s structure supports stronger acid-base activity? Explain why."
]
'''
visual_first_prompts = [
    "Looking at the molecular structures, which one has more electron-withdrawing groups near reactive sites? Use this to infer acid or base strength.",
    "Compare the two molecules by identifying acidic protons and lone pairs directly from the image. Which molecule is better suited for proton transfer?",
    "From the visible functional groups, decide which molecule is more likely to donate a proton. Explain how the structure supports your answer.",
    "Observe where polar bonds are located. Which molecule appears more able to stabilize charge after gaining or losing a proton?",
    "Just by examining atom types and bond patterns, determine which molecule has stronger acid-base behavior.",
    "Based on visible electronegative atoms and bonding patterns, which molecule is more likely to act as a base? Which as an acid?",
    "Focus on the regions with high electron density. Which molecule looks better prepared to stabilize a charge through resonance?",
    "Without external info, judge which molecule has structural features that suggest stronger acidity or basicity. Explain what you see.",
    "Pay attention to hydroxyl, amine, or carbonyl groups. Which molecule has groups that support stronger proton transfer behavior?",
    "From visual inspection alone, decide which molecule is more reactive in acid-base chemistry and explain what features support your decision."
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
output_csv = "Task2_VisualFirst_AcidBase_Results.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image1", "image2", "prompt_type", "prompt_number", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"\n✅ All results saved to {output_csv}")
