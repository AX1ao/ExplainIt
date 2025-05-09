# -*- coding: utf-8 -*-
"""
Batch Inference for Acid/Base Strength Comparison (Task 2)
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
    ("Benzoic_acid.png", "Phenol.png"),
    ("Formic_acid.png", "Acetic-acid.png"),
    ("Ammonia.png", "MeNH2.png"),
]

# --- Step 3: Top 10 Stepwise Prompts for Acid/Base Comparison ---
stepwise_prompts = [
    "Step 1: Identify any atoms with acidic protons. Step 2: Examine how stable the molecule becomes after losing one. Step 3: Decide which molecule is more acidic or basic.",
    "Step 1: Look for lone pairs or negatively charged atoms. Step 2: Consider how easily they could accept or donate a proton. Step 3: Choose the stronger acid or base.",
    "Step 1: Find the most likely proton donor or acceptor in each molecule. Step 2: Compare their strength based on electronegativity or charge stability. Step 3: Pick the more reactive one.",
    "Step 1: Analyze the environment around each molecule’s functional groups. Step 2: Think about how that environment affects acidity or basicity. Step 3: Conclude which molecule is stronger.",
    "Step 1: Identify acidic hydrogens or basic sites. Step 2: Look at resonance or inductive effects nearby. Step 3: Infer which site is more reactive.",
    "Step 1: Check if there are oxygen or nitrogen atoms with lone pairs. Step 2: Evaluate how likely they are to accept or give up a proton. Step 3: Choose which molecule is stronger.",
    "Step 1: Count the polar bonds in each molecule. Step 2: Predict how they affect proton donation or acceptance. Step 3: Decide which molecule is a stronger acid or base.",
    "Step 1: Focus on the atoms that could stabilize a negative charge. Step 2: Think about conjugate base or conjugate acid stability. Step 3: Determine the stronger acid or base.",
    "Step 1: Compare the pKa trends suggested by the functional groups. Step 2: Use that to judge acidity or basicity. Step 3: Make your final decision.",
    "Step 1: Analyze how electron-withdrawing or donating groups affect each molecule. Step 2: Use that to estimate proton affinity or loss. Step 3: Identify the stronger acid or base."
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
output_csv = "Task2_Stepwise_AcidBase_Results.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image1", "image2", "prompt_type", "prompt_number", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"\n✅ All results saved to {output_csv}")
