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
    ("Pyrrole-full.png", "Pyridine-full.png"),
    ("Cytosine.png", "Uracil.png"),
    ("Histamine.png", "Imidazole_numbered.png")
]

print(f"✅ Found {len(image_pairs)} images (only testing 3 for now).")

# --- Step 3: Define Prompts ---

# 1 Baseline prompt
baseline_prompt = ["Which molecule is a stronger acid or base, the first or the second? Why?"]

# 3 Improved Stepwise prompts
stepwise_prompts = [
    "Step 1: Examine the electron density of each molecule. Step 2: Identify atoms capable of donating a lone pair. Step 3: Consider resonance or inductive effects. Step 4: Compare steric hindrance. Step 5: Decide which molecule is the better nucleophile and explain why.",
    "Step-by-step: First, identify potential nucleophilic sites. Second, evaluate charge delocalization. Third, assess solvent effects if any are implied. Finally, choose the better nucleophile and explain your choice.",
    "Step 1: Identify negatively charged or lone pair-bearing atoms. Step 2: Consider how conjugation or electronegative groups affect reactivity. Step 3: Evaluate the kinetic accessibility of the site. Step 4: Conclude which is more reactive as a nucleophile."
]
# 3 Visual-first prompst
visual_first_prompst = [
    "From the image, focus on the reactive centers. Do you see bulky groups that block attack? Do you see resonance that spreads out charge? Pick the more reactive nucleophile.",
    "Check the structures: Which molecule has a more exposed, electron-rich site? Which one looks less crowded? Use visual evidence to answer which is the better nucleophile.",
    "Based on visual inspection, which molecule’s reactive site is freer to act as a nucleophile? Consider electron density and bulkiness in your answer."
]
# 3 Improved Explanation-first prompts
explanation_first_prompts = [
    "To decide which is more nucleophilic, we need to consider the atom's electron density, resonance stabilization, and any steric hindrance. Let's apply this reasoning to the two molecules.",
    "In general, nucleophilicity increases with higher electron density and lower stabilization of the nucleophilic center. Let's consider how this applies to these two molecules.",
    "Let’s first recall: nucleophiles attack electrophiles using available electrons. A good nucleophile is both electron-rich and sterically unencumbered. Which molecule better matches this?"
]

# Merge prompts
all_prompts = baseline_prompt + stepwise_prompts + visual_first_prompst + explanation_first_prompts

# Label CoT type for each prompt
cot_types = (
    ["Baseline"] + 
    ["Stepwise"] * 3 +
    ["Visual_first"] * 3 +
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
output_csv = "Task3_1V_finetune_prompts_res.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image1", "image2", "prompt_type", "prompt_number", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"\n✅ All results saved to {output_csv}")