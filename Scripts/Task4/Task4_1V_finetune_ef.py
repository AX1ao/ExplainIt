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

# --- Step 3: Top 10 Explanation-First Prompts for Acid/Base Comparison ---
explanation_first_prompts = [
    "In SN1 reactions, the key factor is carbocation stability. Molecules that can form a stable carbocation after losing a leaving group will react faster. With that in mind, which of these two is more likely to follow the SN1 path?",
    "SN1 reactions occur in two steps, with the slow step being the formation of a carbocation. Resonance, tertiary carbons, and nearby electron-donating groups all help stabilize this. Apply this logic to decide between the two molecules.",
    "The more stable the carbocation intermediate, the more likely an SN1 mechanism will occur. Consider how the structure of each molecule affects the stability of its carbocation.",
    "SN1 favors molecules where the leaving group can depart easily and leave behind a stable intermediate. Which of these fits that description better?",
    "A good SN1 substrate must have a good leaving group and the ability to stabilize positive charge. Which molecule fits that better, and why?",
    "In polar protic environments, SN1 reactions are favored. Think about which molecule has a structure that could take advantage of such conditions.",
    "Explain how resonance or hyperconjugation might stabilize the carbocation formed during an SN1 reaction. Then decide which molecule benefits more from that.",
    "SN1 reactivity is influenced by substitution pattern — tertiary > secondary > primary. Use this idea to analyze the molecules and choose.",
    "Molecules that undergo SN1 easily often contain benzylic or allylic positions that stabilize carbocations. Does either molecule contain such a feature?",
    "A strong electron-withdrawing group near the reactive center can destabilize a carbocation, making SN1 less likely. Consider this when comparing the two.",
    "Carbocation rearrangements can also stabilize intermediates in SN1. Is either structure able to rearrange to form a more stable ion?",
    "Steric hindrance isn't a major problem for SN1, but it affects SN2 more. So, we focus mostly on how stable the resulting cation is. Analyze that here.",
    "SN1 involves bond breaking first, then nucleophilic attack. Therefore, we focus on how well the molecule handles a temporary loss of electrons.",
    "The best SN1 substrates are those where the leaving group leaves easily, and the molecule can stabilize the resulting positive charge. Based on this, which one is a better candidate?",
    "Remember, SN1 is not concerted. It relies on spontaneous leaving group departure. Which molecule is more likely to allow that, and why?",
    "Consider the molecular orbitals: delocalized π systems and lone pairs on adjacent atoms help stabilize a carbocation. Which molecule shows this feature?",
    "SN1 mechanisms are common in molecules with tertiary carbon centers or resonance stabilization. Use this knowledge to decide which one is more SN1-prone.",
    "Leaving group ability matters too. A weaker base is a better leaving group. Which molecule contains one that fits this criterion?",
    "Some molecules are stabilized by inductive effects from nearby atoms. Which of the two benefits more from this in the context of SN1?",
    "Explain how the structure of each molecule would influence its ability to form and stabilize a carbocation, and choose accordingly."
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
output_csv = "Task4_ExplanationFirst_Res0.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image1", "image2", "prompt_type", "prompt_number", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"\n✅ All results saved to {output_csv}")
