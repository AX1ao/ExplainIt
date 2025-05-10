# -*- coding: utf-8 -*-
"""
Batch Inference for SN1SN2 (Task 4)
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
    ("Ibuprofen.png", "Salicylic-acid.png"),
    ("Methanol.png", "Ethanol.png"),
    ("Acetic-acid.png", "Benzoic_acid.png")
]

print(f"✅ Found {len(image_pairs)} images (only testing 3 for now).")

# --- Step 3: Define Prompts ---

# 1 Baseline prompt
baseline_prompt = ["Which molecule is more likely to undergo an SN1 reaction, and why?"]

# 3 Improved Stepwise prompts
stepwise_prompts = [
    "Let’s evaluate both molecules for SN1 reactivity: (i) Leaving group ability, (ii) Carbocation stability, (iii) Steric accessibility. Then decide which is more favorable.",
    "Let’s take it step-by-step: 1. Is the leaving group good? 2. What’s the class of carbocation (primary/secondary/tertiary)? 3. Is resonance a factor? 4. Decide SN1 reactivity.",
    "Step through the analysis: Evaluate each molecule’s leaving group, the stability of the intermediate carbocation, and the reaction conditions. Then select the more SN1-reactive one."
]
# 3 Visual-first prompst
visual_first_prompst = [
    "Identify any aromatic rings adjacent to the site of bond cleavage. Which molecule is better positioned to stabilize the resulting structure through resonance?",
    "Focus on any resonance structures you can infer visually. Which molecule seems better suited to delocalize a charge?", #8
    "Scan each molecule for ring structures or conjugated systems near the leaving group site. Which structure looks more capable of dispersing charge?",
    ]
# 3 Improved Explanation-first prompts
explanation_first_prompts = [
    "The more stable the carbocation intermediate, the more likely an SN1 mechanism will occur. Consider how the structure of each molecule affects the stability of its carbocation.",
    "Molecules that undergo SN1 easily often contain benzylic or allylic positions that stabilize carbocations. Does either molecule contain such a feature?",
    "Some molecules are stabilized by inductive effects from nearby atoms. Which of the two benefits more from this in the context of SN1?",
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
output_csv = "Task4_1V_finetune_prompts_res.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image1", "image2", "prompt_type", "prompt_number", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"\n✅ All results saved to {output_csv}")