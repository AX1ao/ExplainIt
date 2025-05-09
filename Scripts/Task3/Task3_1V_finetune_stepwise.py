# -*- coding: utf-8 -*-
"""
Batch Inference for Functional Group Reactivity Comparison (Task 3)
10 Image Pairs × 10 Stepwise Prompts using Llava-OneVision
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

# --- Step 3: Top 10 Stepwise Prompts for Acid/Base Comparison ---
stepwise_prompts = [
    "Step 1: Examine the electron density of each molecule. Step 2: Identify atoms capable of donating a lone pair. Step 3: Consider resonance or inductive effects. Step 4: Compare steric hindrance. Step 5: Decide which molecule is the better nucleophile and explain why.",
    "Let's work through it. (1) Look at the atoms with lone pairs. (2) Check how stable the negative charge is. (3) Analyze if the molecule is bulky or accessible. (4) Use this info to decide which is more nucleophilic.",
    "Step-by-step: First, identify potential nucleophilic sites. Second, evaluate charge delocalization. Third, assess solvent effects if any are implied. Finally, choose the better nucleophile and explain your choice.",
    "Step 1: Identify negatively charged or lone pair-bearing atoms. Step 2: Consider how conjugation or electronegative groups affect reactivity. Step 3: Evaluate the kinetic accessibility of the site. Step 4: Conclude which is more reactive as a nucleophile.",
    "Let’s break it down: (1) Which molecule has more available electron density? (2) Are there any resonance structures that stabilize the charge? (3) Is one molecule bulkier than the other? (4) Summarize which one is better and why.",
    "Step 1: Identify lone pairs or π electrons. Step 2: Consider the pKa of the conjugate acid. Step 3: Assess resonance stabilization. Step 4: Judge steric hindrance. Step 5: Conclude which molecule is more nucleophilic.",
    "Step-by-step analysis: First, look at atomic charge. Then, assess resonance effects. Next, examine electron-withdrawing groups. Finally, decide which molecule acts as a better nucleophile.",
    "Let’s go in order: (1) What atom is the nucleophile center? (2) What’s its charge and electronegativity? (3) Is the site sterically accessible? (4) Make a decision based on this info.",
    "First, identify nucleophilic atoms. Then, evaluate if those atoms are hindered or stabilized. Next, consider if any delocalization reduces reactivity. Finally, conclude which molecule wins.",
    "Start by spotting lone pairs or negative charges. Then ask: Are those electrons free to attack? Consider resonance, steric bulk, and electronegativity. Use these to decide the better nucleophile."
]

cot_types = ["Stepwise"] * len(stepwise_prompts)

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
    
    for idx, prompt_text in enumerate(stepwise_prompts):
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
output_csv = "Task3_Stepwise_Res.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image1", "image2", "prompt_type", "prompt_number", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"\n✅ All results saved to {output_csv}")
