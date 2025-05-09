# -*- coding: utf-8 -*-
"""
Batch Inference for Acid/Base Strength Comparison (Task 2)
(3 Images × 10 Prompts) using Llava-OneVision
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
# Load model
model = LlavaOnevisionForConditionalGeneration.from_pretrained(
    "llava-hf/llava-onevision-qwen2-7b-ov-hf",
    quantization_config=quantization_config,
    device_map='auto'
)
# Load processor
processor = LlavaOnevisionProcessor.from_pretrained("llava-hf/llava-onevision-qwen2-0.5b-ov-hf")
processor.tokenizer.padding_side = "left"

# --- Step 2: Set Dataset Folder ---
dataset_folder = "images"  # your actual image folder

# List of image pairs
image_pairs = [
    ("Cytosine.png", "Adenine.png"),
    ("H2O.png", "Methanol.png"),
    ("Caffeine.png", "Morphine.png"),
]

print(f"✅ Found {len(image_pairs)} images (only testing 3 for now).")

# --- Step 3: Define Prompts ---

# 1 Baseline prompt
baseline_prompt = ["Which molecule is a stronger acid or base, the first or the second? Why?"]

# 3 Improved Stepwise prompts
'''
stepwise_prompts = [
    "Step 1: Count the polar bonds in each molecule. Step 2: Predict how they affect proton donation or acceptance. Step 3: Decide which molecule is a stronger acid or base.",
    "Step 1: Focus on the atoms that could stabilize a negative charge. Step 2: Think about conjugate base or conjugate acid stability. Step 3: Determine the stronger acid or base.",
    "Step 1: Analyze how electron-withdrawing or donating groups affect each molecule. Step 2: Use that to estimate proton affinity or loss. Step 3: Identify the stronger acid or base."
]

# Only 1 Visual-first prompt so skip
#"Without any external data, visually decide: which molecule’s structure supports stronger acid-base activity? Explain why."

# 2 Improved Explanation-first prompts
explanation_first_prompts = [
    "The stability of conjugate acids and bases is everything. Which molecule supports better charge distribution after proton transfer?",
    "Acid strength increases when the resulting conjugate base can stabilize its negative charge. Which molecule is better suited for that based on its structure?"
]
'''
stepwise_prompts = [
    "Step 1: Identify the most acidic or basic site in each molecule. Step 2: Consider how stable the molecule is after gaining or losing a proton. Step 3: Say which molecule is stronger, the first or the second, and explain why.",
    "Step 1: Look for electron-withdrawing or donating groups. Step 2: Think about how they affect proton affinity. Step 3: Decide which molecule is a stronger acid or base — the first or the second.",
    "Step-by-step: (1) Observe atoms likely to gain or lose a proton. (2) Consider charge stabilization. (3) Conclude: which molecule is more reactive in acid-base chemistry, first or second?"
]
visual_first_prompts = [
    "Look at the molecular structures and visually compare atoms and groups. Which molecule has more acidic or basic features visible in the image? Choose first or second.",
    "From what you see, which molecule has groups that would make it easier to donate or accept a proton? Justify your answer, then state: is it the first or the second?",
    "Examine the image only. Based on visible atom types and bonds, which molecule appears stronger in acid/base behavior? End by stating 'first' or 'second'."
]
explanation_first_prompts = [
    "Stronger acids form more stable conjugate bases. Based on that, explain which molecule is more acidic, and say if it’s the first or second molecule.",
    "The ability to stabilize charge after proton gain or loss determines acid/base strength. Analyze both molecules, then conclude which is stronger: first or second.",
    "If one molecule supports better charge distribution, it will be a stronger acid or base. Explain your reasoning and clearly choose first or second."
]

# Merge prompts
all_prompts = baseline_prompt + stepwise_prompts + visual_first_prompts + explanation_first_prompts

# Label CoT type for each prompt
cot_types = (
    ["Baseline"] + 
    ["Stepwise"] * 3 +
    ["visual_first_prompts"] * 3 +
    ["Explanation_first"] * 3
)

# --- Step 4: Run Inference---
results = []

generate_kwargs = {
    "max_new_tokens": 300,
    "do_sample": True,
    "top_p": 0.9
}

for img1_name, img2_name in image_pairs:
    image1 = Image.open(os.path.join(dataset_folder, img1_name)).convert("RGB")
    image2 = Image.open(os.path.join(dataset_folder, img2_name)).convert("RGB")
    
    for idx, prompt_text in enumerate(all_prompts):
        # Build conversation with 2 images
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
        
        # Prepare input
        prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)
        inputs = processor(images=[image1, image2], text=prompt, padding=True, return_tensors="pt").to(model.device, torch.float16)
        
        # Generate
        output = model.generate(**inputs, **generate_kwargs)
        generated_text = processor.batch_decode(output, skip_special_tokens=True)[0]
        
        # Save result
        results.append({
            "image1": img1_name,
            "image2": img2_name,
            "prompt_type": cot_types[idx],
            "prompt_number": idx + 1,  # 1-indexed
            "prompt_text": prompt_text,
            "generated_text": generated_text
        })

# --- Step 5: Save Results to CSV ---
output_csv = "Task2_1V_finetune_prompts_res.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image1", "image2", "prompt_type", "prompt_number", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"\n✅ All results saved to {output_csv}")