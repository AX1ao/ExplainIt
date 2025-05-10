# -*- coding: utf-8 -*-
"""
Batch Inference for SN1SN2 (Task 4)
3 Image Pairs × 20 Stepwise Prompts using Llava-OneVision
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
'''
image_pairs = [
    ("Aniline.png", "Phenol.png"),
    ("Paracetamol.png", "Morphine.png"),
    ("Caffeine.png", "Adenine.png")
]
'''
image_pairs = [
    ("Aniline.png", "Phenol.png"),
    ("Paracetamol.png", "Morphine.png"),
    ("Caffeine.png", "Adenine.png"),
    ("Ibuprofen.png", "Salicylic-acid.png"),
    ("Methanol.png", "Ethanol.png"),
    ("Acetic-acid.png", "Benzoic_acid.png"),
    ("Cyclohexane.png", "Benzene.png"),
    ("Formic_acid.png", "Nitrobenzene.png"),
    ("Pyridine_numbers.png", "Pyrrole-numbered.png"),
    ("Furan-full.png", "Thiophene-full.png"),
]
# --- Step 3: 20 Stepwise Prompts for Acid/Base Comparison ---
stepwise_prompts = [
    "Analyze each molecule in steps. First, identify the leaving group. Then, consider how stable the carbocation would be if that group left. Finally, determine which molecule favors an SN1 mechanism.",
    "Step by step: (1) What’s the leaving group in each molecule? (2) If it leaves, how stable is the resulting carbocation? (3) Based on that, which molecule is more likely to follow SN1?",
    "Start by identifying the structure and functional group of each molecule. Then assess the stability of the carbocation intermediate. Which one leads to a more stable intermediate? That’s the better SN1 candidate.",
    "Break this down: (1) Identify the potential site of substitution. (2) Predict whether a carbocation would form. (3) Rank their stabilities. (4) Choose the molecule more reactive via SN1.",
    "Let’s evaluate both molecules for SN1 reactivity: (i) Leaving group ability, (ii) Carbocation stability, (iii) Steric accessibility. Then decide which is more favorable.",
    "Think through the SN1 pathway. First, determine how easily each molecule can form a carbocation. Then compare their stabilities (e.g., tertiary > secondary > primary). Which one is better suited?",
    "Walk through this: Does each molecule have a good leaving group? Can it form a stable carbocation (e.g., resonance-stabilized or tertiary)? Then compare and decide.",
    "Step-by-step analysis: 1. Identify if a leaving group is present. 2. Determine carbocation stability via inductive/resonance effects. 3. Choose the more SN1-favorable molecule.",
    "Examine each molecule carefully: What is the potential leaving group? How stable is the resulting carbocation? Which one follows the SN1 pathway more readily?",
    "First, identify any polar protic solvent that might assist SN1. Then consider the leaving group. Finally, compare how well each carbocation is stabilized.",
    "Go through each factor in SN1: Leaving group strength, carbocation stability, solvent type. For each molecule, determine how they rank. Then decide the more likely SN1 participant.",
    "Let’s work stepwise: 1. What’s the site of possible ionization? 2. If ionization occurs, is the intermediate carbocation stabilized by resonance or hyperconjugation? 3. Which is more reactive via SN1?",
    "Break down the SN1 mechanism into parts. Check which molecule has: (1) A better leaving group, (2) A more stable carbocation, and (3) Less steric hindrance. Use this to choose.",
    "First, isolate the group that would leave in SN1. Second, determine the carbocation that would form. Third, analyze the stability (e.g., resonance, hyperconjugation, tertiary). Then pick.",
    "Step-by-step evaluation: 1. Is there a good leaving group? 2. Is the resulting carbocation primary, secondary, or tertiary? 3. Any resonance stabilization? 4. Which is favored for SN1?",
    "Identify the substitution center on each molecule. Then ask: How stable is the carbocation that forms if that bond breaks? Use this to assess SN1 favorability.",
    "Start by checking the molecule’s structure. Then simulate carbocation formation and assess its stability (via resonance or inductive effects). Determine SN1 likelihood.",
    "Which molecule loses its leaving group more easily? Which forms a stable carbocation? Use these steps to predict which one undergoes SN1 more readily.",
    "Let’s take it step-by-step: 1. Is the leaving group good? 2. What’s the class of carbocation (primary/secondary/tertiary)? 3. Is resonance a factor? 4. Decide SN1 reactivity.",
    "Step through the analysis: Evaluate each molecule’s leaving group, the stability of the intermediate carbocation, and the reaction conditions. Then select the more SN1-reactive one."
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
output_csv = "Task4_Stepwise_Res0.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image1", "image2", "prompt_type", "prompt_number", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"\n✅ All results saved to {output_csv}")
