# -*- coding: utf-8 -*-
"""
Batch Inference for Functional Group Reactivity Comparison (Task 3)
10 Image Pairs × 10 Explanation-First Prompts using Llava-OneVision
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

# --- Step 3: Top 10 Explanation-First Prompts for Acid/Base Comparison ---
'''
explanation_first_prompts = [
]
'''
explanation_first_prompts = [
    "Nucleophilicity depends on electron availability, charge localization, and steric accessibility. Based on these factors, let's determine which molecule is the better nucleophile.",
    "To decide which is more nucleophilic, we need to consider the atom's electron density, resonance stabilization, and any steric hindrance. Let's apply this reasoning to the two molecules.",
    "The stronger nucleophile will have a more concentrated electron density and minimal steric obstruction. Keeping this in mind, let's compare the two molecules.",
    "We evaluate nucleophiles by their ability to donate electrons. Molecules with lone pairs on less electronegative atoms, minimal resonance delocalization, and low hindrance are more reactive.",
    "Electron-donating capacity is key to nucleophilicity. Resonance, inductive effects, and accessibility all influence this. Let’s use these ideas to evaluate the molecules.",
    "A good nucleophile has readily available electrons and isn't blocked by bulky groups. Which molecule fits this description better?",
    "In general, nucleophilicity increases with higher electron density and lower stabilization of the nucleophilic center. Let's consider how this applies to these two molecules.",
    "The more nucleophilic molecule should be less stabilized by resonance and less hindered sterically. Keep this framework in mind while comparing the two.",
    "Key ideas: electron availability, accessibility, and the absence of charge delocalization. Use this to interpret the molecular structures and pick the better nucleophile.",
    "Let’s first recall: nucleophiles attack electrophiles using available electrons. A good nucleophile is both electron-rich and sterically unencumbered. Which molecule better matches this?"
]

cot_types = ["Explanation_first"] * len(explanation_first_prompts)

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
    
    for idx, prompt_text in enumerate(explanation_first_prompts):
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
output_csv = "Task3_ExplanationFirst_Res.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image1", "image2", "prompt_type", "prompt_number", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"\n✅ All results saved to {output_csv}")
