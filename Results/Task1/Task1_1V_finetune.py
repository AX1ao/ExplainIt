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
dataset_folder = "images"  # your actual image folder

# List of image pairs
image_pairs = [
    ("Aniline.png", "Nitrobenzene.png"),
    ("Benzene.png", "Toluene.png"),
    ("Benzaldehyde.png", "Benzoic_acid.png"),
]

print(f"✅ Found {len(image_pairs)} images (only testing 3 for now).")

# --- Step 3: Define Prompts ---

# 1 Baseline prompt
baseline_prompt = ["Which molecule is more reactive toward electrophilic aromatic substitution, the first or the second? Why?"]

# 5 Improved Stepwise prompts
stepwise_prompts = [
    "Step 1: Identify any activating groups (e.g., -OH, -NH₂, alkyl). Step 2: Identify any deactivating groups (e.g., -NO₂, carbonyls). Step 3: Decide which molecule has stronger activation toward EAS.",
    "First, note if the ring has electron-donating substituents. Then, note if it has electron-withdrawing substituents. Finally, determine which ring is more reactive toward electrophiles.",
    "Step 1: Look at functional groups. Step 2: Predict their effects on electron density. Step 3: Predict which molecule favors EAS.",
    "Step-by-step: (1) List all substituents. (2) Label them as activators or deactivators. (3) Infer which molecule reacts faster based on the substituents.",
    "Begin by assessing whether the groups attached to the aromatic rings push or pull electron density. Then infer which molecule is better suited for EAS."
]

# 5 Improved Visual-first prompts
visual_first_prompts = [
    "Looking at the structure, identify which groups could donate electrons into the ring, and which could withdraw. Based on what you see, predict EAS reactivity.",
    "Focus only on the types of groups attached to the rings: donating vs withdrawing. Based on visual inspection, which molecule is more activated for substitution?",
    "Observe visible features: are there -OH, -NH₂, or -NO₂ groups? Count and compare electron-donating versus electron-withdrawing groups for both molecules.",
    "Purely based on the visual layout of groups on the ring, which molecule appears more electron-rich and attractive to an electrophile?",
    "By examining only the visible substituents on the rings, conclude which molecule would favor electrophilic attack more easily."
]

# 5 Improved Explanation-first prompts
explanation_first_prompts = [
    "Explain how the substituents visible on the rings affect the ring's electron density, and predict which molecule undergoes EAS faster.",
    "Electron-donating groups stabilize the transition state of EAS. Describe which molecule has more activating groups, and conclude which is more reactive.",
    "Electron-withdrawing groups decrease EAS reactivity. Considering this, explain which molecule's structure favors substitution more.",
    "Relate the presence of activating vs deactivating groups to the overall reactivity of the ring in EAS. Which molecule is better suited for EAS?",
    "Consider the net electronic effect (donating vs withdrawing) of all substituents. Based on that, decide which molecule is more reactive toward EAS."]

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

# --- Step 4: Run Inference (updated for 2 images) ---
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
output_csv = "Task1_1V_finetune_prompts_res.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image1", "image2", "prompt_type", "prompt_number", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"\n✅ All results saved to {output_csv}")

'''
# 1 Baseline prompt
baseline_prompt = ["Which molecule is more reactive toward electrophilic aromatic substitution, the first or the second? Why?"]

# 10 Updated Stepwise prompts
stepwise_prompts = [
    "Step 1: Spot any -OH, -NH₂, or -OR groups on the rings. Step 2: Spot any -NO₂, carbonyl, or halide groups. Step 3: Molecule with more donating groups reacts faster. Which is it?",
    "First, count the electron-donating groups on each molecule. Then, count the electron-withdrawing groups. Conclude which molecule reacts faster toward EAS.",
    "Identify if either molecule has activating groups (like alkyl, amine). If yes, that molecule is more reactive toward EAS. Pick the molecule.",
    "List all major groups visible on each molecule. Categorize each group as activating or deactivating. Choose the molecule with more activation.",
    "Focus on whether each molecule has groups that donate lone pairs into the ring (e.g., -OH, -NH₂). The molecule with more donation is faster. Decide.",
    "Check for strongly deactivating groups (-NO₂, -SO₃H, carbonyls). If one molecule has such a group, it's less reactive. Choose the more reactive one.",
    "Look for features that stabilize carbocations (activating groups). The molecule with better carbocation stabilization is more EAS-reactive. Pick one.",
    "First, determine if there are multiple activating groups in any structure. Then, determine if there are multiple deactivating groups. Predict the faster-reacting molecule.",
    "Analyze the conjugation and resonance donation capacity of substituents. Pick the molecule where substituents enhance resonance more.",
    "Focus on ortho/para-directing groups: if a molecule has strong ortho/para activators, it favors EAS. Choose based on visible groups."
]

# 5 Improved Visual-first prompts
visual_first_prompts = [
    "Looking at the structure, identify which groups could donate electrons into the ring, and which could withdraw. Based on what you see, predict EAS reactivity.",
    "Focus only on the types of groups attached to the rings: donating vs withdrawing. Based on visual inspection, which molecule is more activated for substitution?",
    "Observe visible features: are there -OH, -NH₂, or -NO₂ groups? Count and compare electron-donating versus electron-withdrawing groups for both molecules.",
    "Purely based on the visual layout of groups on the ring, which molecule appears more electron-rich and attractive to an electrophile?",
    "By examining only the visible substituents on the rings, conclude which molecule would favor electrophilic attack more easily."
]

# 10 Updated Explanation-first prompts
explanation_first_prompts = [
    "Explain which groups on the molecules increase electron density on the ring. The molecule with more electron density reacts faster with electrophiles.",
    "Identify the groups that donate electrons to the ring system. Then conclude which molecule is more attractive to electrophiles based on those groups.",
    "Electron-withdrawing groups slow down EAS by pulling electron density away. Analyze the molecules and explain which one is less affected.",
    "Based on resonance and inductive effects, explain which molecule activates the aromatic ring more for substitution reactions.",
    "Consider the net electronic effect (donating vs withdrawing) of all substituents. Based on that, decide which molecule is more reactive toward EAS.",
    "Analyze whether the groups visible on each molecule would stabilize or destabilize the carbocation intermediate in EAS. Pick the molecule with better stabilization.",
    "Strongly activating groups (like -OH, -NH₂) increase EAS rates. Which molecule visibly benefits more from activation? Explain and conclude.",
    "Groups that can delocalize electrons into the ring enhance EAS. Which molecule shows this effect more? Reason and state your answer.",
    "Negative resonance contributors (e.g., nitro, carbonyls) decrease EAS reactivity. Identify if such groups exist, and conclude the faster-reacting molecule.",
    "Explain whether each molecule has a net activating or deactivating effect on the ring system, and conclude which one undergoes EAS more easily."
]

# Merge prompts
all_prompts = baseline_prompt + stepwise_prompts + visual_first_prompts + explanation_first_prompts

# Label CoT type for each prompt
cot_types = (
    ["Baseline"] + 
    ["Stepwise"] * 10 +
    ["Visual_first"] * 5 +
    ["Explanation_first"] * 10
)

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
output_csv = "Task1_1V_finetune_prompts_res.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image1", "image2", "prompt_type", "prompt_number", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"\n✅ All results saved to {output_csv}")
'''