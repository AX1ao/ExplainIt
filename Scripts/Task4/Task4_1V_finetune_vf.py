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
# --- Step 3: Top 10 Visual-first Prompts for Acid/Base Comparison ---
'''
visual_first_prompts = [
    "Look at the structure of both molecules. Which one has a group that looks easier to break off? Use this to decide which could follow an SN1 path.",
    "Start by examining the central atoms and their connections. Which molecule appears more capable of stabilizing a positive charge if a group leaves?",
    "Observe the overall shape and groups attached to the carbon centers. Which molecule seems to support carbocation formation better?",
    "Visually compare the two molecules. Which one shows more branching or ring structures that might stabilize a leaving group?",
    "Look at the atoms near the potential reaction site. Which one appears more substituted or supported by nearby groups?",
    "Start with a visual scan: does either molecule look like it has a bulky, stable framework that could hold a positive charge well?",
    "Compare both molecules. Which has a leaving group that looks more isolated or weakly bonded? That may point to easier SN1 reactivity.",
    "Focus on any resonance structures you can infer visually. Which molecule seems better suited to delocalize a charge?",
    "From the structure alone, which molecule looks more likely to form a stable intermediate after bond cleavage?",
    "Visually inspect the substituents. Which molecule seems more tertiary-like or ring-stabilized? That’s often better for SN1.",
    "Look at the atoms directly bonded to the reactive center. Which one has more electron-donating neighbors to stabilize a positive charge?",
    "Compare both molecules side by side. Does either one show hints of conjugation or aromaticity near the reaction site?",
    "Start with visual features: Which molecule has a longer alkyl chain or more branching at the site of reaction?",
    "Look for any heteroatoms or pi systems nearby. Which structure seems more able to support charge delocalization?",
    "Focus on the immediate geometry around the reactive site. Which one looks more spacious or sterically able to lose a leaving group?",
    "Observe the molecule that has fewer rigid rings or planar groups near the reactive center. That might hint at a more flexible SN1 path.",
    "Which molecule appears to have better orbital overlap or lone pairs near the reactive site to stabilize a charge?",
    "Begin by visually checking for good leaving groups — halogens, OH, or similar. Which one stands out as easier to detach?",
    "Visually explore the molecular frameworks. Which one looks better able to form a stable ion after losing a group?",
    "Start from the overall impression of both structures. Which looks more complex, branched, or capable of forming stable intermediates?"
]
'''
visual_first_prompts = [
    "Look at the structure of both molecules. Which one has a group that looks easier to break off? Use this to decide which could follow an SN1 path.", #1
    "Observe the overall shape and groups attached to the carbon centers. Which molecule seems to support carbocation formation better?", #3
    "Focus on any resonance structures you can infer visually. Which molecule seems better suited to delocalize a charge?", #8
    "Look at the atoms directly bonded to the potential reaction site. Which molecule has more surrounding groups that could help stabilize a positive charge?",
    "Scan each molecule for ring structures or conjugated systems near the leaving group site. Which structure looks more capable of dispersing charge?",
    "Focus on the symmetry and planarity around the central atom. Which molecule looks like it could support charge delocalization better if a group left?",
    "Visually compare the number of nearby lone pair atoms or electronegative groups. Which molecule has more elements that might stabilize a charged center?",
    "Check the branching or substitution near the reaction site. Which molecule appears more substituted at the carbon attached to the leaving group?",
    "Compare the rigidity of the two molecules. Which one looks more flexible or less sterically crowded at the site of substitution?",
    "Identify any aromatic rings adjacent to the site of bond cleavage. Which molecule is better positioned to stabilize the resulting structure through resonance?",
    "Look for nearby heteroatoms (like N or O) that could interact with a developing positive charge. Which molecule has more helpful groups in the right position?",
    "Observe how isolated the leaving group appears in each structure. Which one looks more 'exposed' or weakly connected — a possible sign of easier SN1 departure?",
    "Compare both molecules: which one has more visually connected electron-rich systems (like double bonds or lone pair donors) that could stabilize an intermediate?",
    "Look for any heteroatoms or pi systems nearby. Which structure seems more able to support charge delocalization?",
    "Focus on the immediate geometry around the reactive site. Which one looks more spacious or sterically able to lose a leaving group?",
    "Observe the molecule that has fewer rigid rings or planar groups near the reactive center. That might hint at a more flexible SN1 path.",
    "Which molecule appears to have better orbital overlap or lone pairs near the reactive site to stabilize a charge?",
    "Begin by visually checking for good leaving groups — halogens, OH, or similar. Which one stands out as easier to detach?",
    "Visually explore the molecular frameworks. Which one looks better able to form a stable ion after losing a group?",
    "Start from the overall impression of both structures. Which looks more complex, branched, or capable of forming stable intermediates?"
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
output_csv = "Task4_VisualFirst_Res0.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image1", "image2", "prompt_type", "prompt_number", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"\n✅ All results saved to {output_csv}")
