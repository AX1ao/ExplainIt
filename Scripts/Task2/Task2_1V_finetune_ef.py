# -*- coding: utf-8 -*-
"""
Batch Inference for Acid/Base Strength Comparison (Task 2)
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
    ("Benzoic_acid.png", "Phenol.png"),
    ("Formic_acid.png", "Acetic-acid.png"),
    ("Ammonia.png", "MeNH2.png"),
]

# --- Step 3: Top 10 Explanation-First Prompts for Acid/Base Comparison ---
'''
explanation_first_prompts = [
    "The key to acid or base strength lies in how stable the molecule is after gaining or losing a proton. Which one forms a more stable conjugate species?",
    "Strong acids usually have highly stable conjugate bases. Based on the structures, which molecule fits that pattern better?",
    "Electron-withdrawing or donating groups near acidic or basic sites can strongly affect reactivity. Which molecule shows a stronger effect?",
    "The ability to donate or accept a proton depends on both atom type and surrounding structure. Which molecule’s setup makes that easier?",
    "If a molecule can stabilize a negative or positive charge through resonance or electronegativity, it’s likely to be stronger. Which of these does that better?",
    "Functional groups like carboxylic acids, amines, and phenols influence acidity or basicity. Which molecule has more reactive groups?",
    "Based on the molecular structures, think about where each molecule could gain or lose a proton. Which would be more favorable?",
    "Acidity and basicity often depend on where the proton goes and what’s left behind. Which molecule creates the more stable result?",
    "One of these molecules has a structure that clearly supports stronger acid-base behavior. Identify it and explain what features make it stronger.",
    "The stability of conjugate acids and bases is everything. Which molecule supports better charge distribution after proton transfer?"
]
'''
explanation_first_prompts = [
    "When a molecule donates a proton, the stability of its conjugate base determines how strong an acid it is. Which molecule would form a more stable conjugate base, and why?",
    "Molecules with electron-withdrawing groups near acidic sites tend to be stronger acids. Which of these molecules shows that pattern more clearly?",
    "If a molecule accepts a proton, the resulting conjugate acid must be stable for it to be a strong base. Which molecule supports that better based on its structure?",
    "Charge delocalization through resonance often makes a molecule more acidic or basic. Which of the two molecules allows better charge distribution after proton transfer?",
    "Acid strength increases when the resulting conjugate base can stabilize its negative charge. Which molecule is better suited for that based on its structure?",
    "Stronger bases often have lone pairs that are both available and not overly stabilized. Which molecule fits that description more closely?",
    "The presence of highly electronegative atoms can influence acid/base behavior by shifting electron density. Which molecule shows stronger effects from electronegative atoms?",
    "Aromatic or conjugated systems can stabilize charges through delocalization. Which molecule uses this kind of stabilization more effectively?",
    "The more a molecule can distribute or hide charge after proton gain/loss, the stronger its acid or base behavior. Which one achieves that more efficiently?",
    "Substituents and local environment strongly affect proton transfer tendencies. Based on what you see, which molecule is more likely to act as a strong acid or base?"
]

cot_types = ["Visual_first"] * len(explanation_first_prompts)

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
output_csv = "Task2_ExplanationFirst_AcidBase_Results.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image1", "image2", "prompt_type", "prompt_number", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"\n✅ All results saved to {output_csv}")
