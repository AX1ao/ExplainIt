# -*- coding: utf-8 -*-
"""
Batch Inference for Molecule Identification Tasks 
(3 Images × 16 Prompts) using Llava-OneVision
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
dataset_folder = "0_Identify"  # relative path to your dataset folder
image_filenames = [os.path.join(dataset_folder, fname) for fname in os.listdir(dataset_folder) if fname.lower().endswith(('.png', '.jpg', '.jpeg'))]
image_filenames.sort()  # sort alphabetically

# Only take first 3 images
image_filenames = image_filenames[:3]

print(f"✅ Found {len(image_filenames)} images (only testing 3 for now).")

# --- Step 3: Define Prompts ---

# 1 Baseline prompt
baseline_prompt = ["Describe what this molecule structure shows."]

# 5 Improved Stepwise prompts
stepwise_prompts = [
    "Step 1: Count the number of carbon atoms in the main structure. Step 2: Identify rings, chains, or branches. Step 3: Determine bond types (single, double, etc.). Step 4: Identify any attached groups. Step 5: Conclude what the molecule is.",
    "Let's work through this: (1) Analyze the core structure (ring/chain), (2) Analyze bond types, (3) Analyze attached groups, (4) Suggest the molecule's identity.",
    "First, describe whether the molecule is cyclic or acyclic. Then, count heavy atoms (carbon, oxygen, nitrogen). Finally, propose the molecule's name.",
    "Break down the image into parts: central structure → side groups → bond types → final conclusion about the molecule.",
    "Step by step: (a) Visual layout, (b) Type of bonds, (c) Special features like rings/double bonds, (d) Likely molecule type."
]

# 5 Improved Visual-first prompts
visual_first_prompts = [
    "Carefully describe the number and arrangement of atoms (rings, chains) you see in this structure. Based only on that, infer the molecule.",
    "Looking at the number of sides and angles in the structure, describe the shape and types of bonds you see, and suggest the most fitting molecule.",
    "Focus purely on counting the visible rings and branches. Describe their connection pattern and infer the molecule type.",
    "Describe how many rings, double bonds, and attached groups you observe visually. Then guess the molecule based on that visual layout.",
    "Observe the connectivity between atoms — are they forming a hexagon, pentagon, chain? Use that information to suggest the molecule."
]

# 5 Improved Explanation-first prompts
explanation_first_prompts = [
    "Explain the molecule's main chemical features (rings, functional groups, bond types) and based on these features, conclude its identity.",
    "This molecule shows distinct chemical properties. First, list the bonds and functional groups you observe; then infer what molecule fits them.",
    "Describe the structure by naming the types of bonds, atoms, and any patterns you see, and based on these, propose the molecule's name.",
    "Focus on explaining what the bond patterns (single/double, conjugation) imply chemically, and then identify the molecule.",
    "Analyze the functional groups, ring structures, and bonding network present in the molecule, and reason toward its most likely identity."
]

# Merge prompts
all_prompts = baseline_prompt + stepwise_prompts + visual_first_prompts + explanation_first_prompts

# Label CoT type for each prompt
cot_types = (
    ["Baseline"] + 
    ["Stepwise"] * 5 +
    ["Visual_first"] * 5 +
    ["Explanation_first"] * 5
)

# --- Step 4: Run Inference ---
results = []

generate_kwargs = {
    "max_new_tokens": 300,
    "do_sample": True,
    "top_p": 0.9
}

for img_path in image_filenames:
    image = Image.open(img_path).convert("RGB")
    
    for idx, prompt_text in enumerate(all_prompts):
        # Build conversation
        conversation = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt_text},
                    {"type": "image"},
                ],
            },
        ]
        
        # Prepare input
        prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)
        inputs = processor(images=image, text=prompt, padding=True, return_tensors="pt").to(model.device, torch.float16)
        
        # Generate
        output = model.generate(**inputs, **generate_kwargs)
        generated_text = processor.batch_decode(output, skip_special_tokens=True)[0]
        
        # Save result
        results.append({
            "image": os.path.basename(img_path),
            "prompt_type": cot_types[idx],
            "prompt_number": idx + 1,  # 1-indexed
            "prompt_text": prompt_text,
            "generated_text": generated_text
        })

# --- Step 5: Save Results to CSV ---
output_csv = "OneVisionID_outputs_3img_test.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image", "prompt_type", "prompt_number", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"\n✅ All results saved to {output_csv}")
