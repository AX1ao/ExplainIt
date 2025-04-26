# -*- coding: utf-8 -*-
"""
Batch Inference for Molecule Identification Tasks 
(18 Images × 4 Prompts) using Llava-OneVision
"""

import os
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
dataset_folder = "dataset"  # relative path to your dataset folder
image_filenames = [os.path.join(dataset_folder, fname) for fname in os.listdir(dataset_folder) if fname.lower().endswith(('.png', '.jpg', '.jpeg'))]
image_filenames.sort()  # sort alphabetically

print(f"✅ Found {len(image_filenames)} images in '{dataset_folder}'.")
CoTs = ["Baseline", "Stepwise", "Visual_first", "Explanation_first"]

# --- Step 3: Define Prompts ---
prompts = [
    "Describe what this molecule structure shows.",
    "Let's think step by step. First, identify the key visual elements of the molecule. Then, determine the types of bonds and functional groups. Finally, explain what the overall structure represents.",
    "Looking at the molecular structure, describe the key visual patterns you notice (such as bond types, rings, or chains) and explain what this structure shows.",
    "This structure represents certain chemical features. Explain these features, focusing on bonds, functional groups, and any distinct patterns you observe."
]

# --- Step 4: Run Inference ---
results = []

generate_kwargs = {
    "max_new_tokens": 100,
    "do_sample": True,
    "top_p": 0.9
}

for img_path in image_filenames:
    image = Image.open(img_path).convert("RGB")
    
    for idx, prompt_text in enumerate(prompts):
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
            "prompt_type": CoTs[idx],
            "prompt_text": prompt_text,
            "generated_text": generated_text
        })

# --- Step 5: Save Results to CSV ---
output_csv = "OneVision_ID_outputs.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image", "prompt_number", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"\n✅ All results saved to {output_csv}")
