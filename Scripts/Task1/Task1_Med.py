# -*- coding: utf-8 -*-
"""
Batch Inference for EAS Reactivity Tasks  
(10 Combined Images × 4 Prompts) using Llava-Med (via eval_model)
"""

import os, sys, io, csv, types, contextlib, torch, gc

# === PATHS & ENVIRONMENT ===
sys.path.insert(0, "/scratch/yx3493/LLaVA-Med")
sys.path.insert(0, "/scratch/yx3493/LLaVA")

os.environ["TRITON_CACHE_DIR"] = "/scratch/yx3493/.triton_cache"
os.environ["HF_HOME"] = "/scratch/yx3493/.hf_cache"
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

# === IMPORT CORE LLAVA INFERENCE ===
from llava.eval.run_llava import eval_model
from llava.mm_utils import get_model_name_from_path

# === SETUP ===
model_path = "microsoft/llava-med-v1.5-mistral-7b"
image_folder = "/home/yx3493/llvm/T1/img"
output_csv = "Task1_MED_outputs.csv"

image_files = [f"{i}.png" for i in range(1, 11)]

prompt_templates = {
    "Baseline": "Which molecule is more reactive toward electrophilic aromatic substitution, the first or the second? Why?",
    "Stepwise": "First, note if the ring has electron-donating substituents. Then, note if it has electron-withdrawing substituents. Finally, determine which ring is more reactive toward electrophiles.",
    "Visual_first": "Observe visible features: are there -OH, -NH₂, or -NO₂ groups? Count and compare electron-donating versus electron-withdrawing groups for both molecules.",
    "Explanation_first": "Consider the net electronic effect (donating vs withdrawing) based on the visible substituents. Then predict which molecule will react faster toward EAS."
}

# === INFERENCE LOOP ===
results = []

for idx, image_name in enumerate(image_files, start=1):
    image_path = os.path.join(image_folder, image_name)
    print(f"\n📷 Image {idx}: {image_name}")

    for prompt_type, prompt_text in prompt_templates.items():
        print(f"   ➤ Prompt Type: {prompt_type}")
        args = types.SimpleNamespace(
            model_path=model_path,
            model_base=None,
            model_name=get_model_name_from_path(model_path),
            query=prompt_text,
            conv_mode=None,
            image_file=image_path,
            sep="，",
            temperature=0,
            top_p=None,
            num_beams=1,
            max_new_tokens=512
        )

        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            eval_model(args)

        output = buffer.getvalue().strip()
        results.append({
            "image_index": idx,
            "prompt_type": prompt_type,
            "prompt_text": prompt_text,
            "generated_text": output
        })

        # === EMPTY CACHE AFTER EACH INFERENCE ===
        torch.cuda.empty_cache()
        gc.collect()

# === SAVE TO CSV ===
with open(output_csv, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["image_index", "prompt_type", "prompt_text", "generated_text"])
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print(f"\n✅ Done! All results saved to {output_csv}")

'''
"""
Batch Inference for EAS Reactivity Tasks 
(10 Pairs × 4 Prompts) using Llava-Med (Microsoft)
"""

import sys, os, csv, torch
from PIL import Image

# === Paths & Envs ===
sys.path.insert(0, '/scratch/yx3493/LLaVA-Med')
sys.path.insert(0, "/scratch/yx3493/LLaVA")
os.environ["TRITON_CACHE_DIR"] = "/scratch/yx3493/.triton_cache"
os.environ["HF_HOME"] = "/scratch/yx3493/.hf_cache"
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

import os
from PIL import Image
from llava.model.builder import load_pretrained_model
from llava.mm_utils import get_model_name_from_path
from llava.eval.run_llava import eval_model
import types
import io
import contextlib

# === 1. Load Model ===
model_path = "microsoft/llava-med-v1.5-mistral-7b"
tokenizer, model, image_processor, context_len = load_pretrained_model(
    model_path=model_path,
    model_base=None,
    model_name=get_model_name_from_path(model_path),
    device_map = "auto"
)

# === 3. Set Image Folder ===
image_folder = "/home/yx3493/llvm/T1/img"
save_folder = "/home/yx3493/llvm/T1"
os.makedirs(save_folder, exist_ok=True)

# === 3. Define 4 Prompt Templates ===
prompt_templates = {
    "Baseline": "Which molecule is more reactive toward electrophilic aromatic substitution, the first or the second? Why?",
    "Stepwise CoT": "First, note if the ring has electron-donating substituents. Then, note if it has electron-withdrawing substituents. Finally, determine which ring is more reactive toward electrophiles.",
    "Visual-First CoT":"Observe visible features: are there -OH, -NH₂, or -NO₂ groups? Count and compare electron-donating versus electron-withdrawing groups for both molecules.",
    "Explanation-First CoT": "Consider the net electronic effect (donating vs withdrawing) based on the visible substituents. Then predict which molecule will react faster toward EAS."
}

# === 6. Infer for each image and collect outputs into one file ===
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png'))]
output_file = os.path.join(save_folder, "all_outputs.txt")
with open(output_file, "w") as f:
    for img_file in image_files:
        img_path = os.path.join(image_folder, img_file)
        print(f"🔵 Processing Image: {img_file}")
        f.write(f"===== Image: {img_file} =====\n\n")

        for style, prompt in prompt_templates.items():
            print(f"  ➡️  Using Prompt Style: {style}")

            args = types.SimpleNamespace(
                model_path=model_path,
                model_base=None,
                model_name=get_model_name_from_path(model_path),
                query=prompt,
                conv_mode=None,
                image_file=img_path,
                sep="，",
                temperature=0,
                top_p=None,
                num_beams=1,
                max_new_tokens=512
            )

            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                eval_model(args)
            output = buffer.getvalue()
            f.write(f"[{style}]\n{output}\n\n")

        f.write("\n")

print("🎯 All Done! Outputs saved to:", output_file)


"""
Batch Inference for EAS Reactivity Tasks 
(10 Pairs × 4 Prompts) using Llava-Med (Microsoft)
"""

import sys, os, csv, torch
from PIL import Image

# === Paths & Envs ===
sys.path.insert(0, '/scratch/yx3493/LLaVA-Med')
sys.path.insert(0, "/scratch/yx3493/llava_libs")
os.environ["TRITON_CACHE_DIR"] = "/scratch/yx3493/.triton_cache"
os.environ["HF_HOME"] = "/scratch/yx3493/.hf_cache"
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

# === LLaVA-Med Imports ===
from llava.mm_utils import get_model_name_from_path, process_images, tokenizer_image_token
from llava.conversation import conv_templates
from llava.model.language_model.llava_mistral import LlavaMistralForCausalLM
from transformers import AutoConfig, AutoTokenizer
from accelerate import init_empty_weights, infer_auto_device_map

# Debug available keys
# print("Available conversation templates:", list(conv_templates.keys()))

# === Model Setup ===
model_path = "microsoft/llava-med-v1.5-mistral-7b"

# Step 1: Config and device map
config = AutoConfig.from_pretrained(model_path)
with init_empty_weights():
    empty_model = LlavaMistralForCausalLM(config)
device_map = infer_auto_device_map(empty_model, max_memory={0: "8GiB", "cpu": "32GiB"})

# Step 2: Load full model with offloading
model = LlavaMistralForCausalLM.from_pretrained(model_path, config=config, device_map=device_map)

# Step 3: Load tokenizer & processor manually
tokenizer = AutoTokenizer.from_pretrained(model_path)
from llava.model.builder import load_pretrained_model
_, _, image_processor, context_len = load_pretrained_model(
    model_path=model_path,
    model_base=None,
    model_name=get_model_name_from_path(model_path),
    device_map=device_map
)

# === Dataset ===
dataset_folder = "/home/yx3493/llvm/T1/images"
image_pairs = [
    ("Aniline.png", "Nitrobenzene.png"),
    ("Benzene.png", "Toluene.png"),
    ("Benzaldehyde.png", "Benzoic_acid.png"),
    ("Pyridine-full.png", "Benzene.png"),
    ("Pyrrole-full.png", "Benzene.png"),
    ("Phenol.png", "Benzene.png"),
    ("Salicylic-acid.png", "Benzoic_acid.png"),
    ("Nitrobenzene.png", "Ozone.png"),
    ("Pyrrole-numbered.png", "Pyridine-full.png"),
    ("Morphine.png", "Caffeine.png")
]

cot_labels = ["Baseline", "Stepwise", "Visual_first", "Explanation_first"]
prompts = [
    "Which molecule is more reactive toward electrophilic aromatic substitution, the first or the second? Why?",
    "First, note if the ring has electron-donating substituents. Then, note if it has electron-withdrawing substituents. Finally, determine which ring is more reactive toward electrophiles.",
    "Observe visible features: are there -OH, -NH₂, or -NO₂ groups? Count and compare electron-donating versus electron-withdrawing groups for both molecules.",
    "Consider the net electronic effect (donating vs withdrawing) based on the visible substituents. Then predict which molecule will react faster toward EAS."
]

# === Inference ===
def run_inference(prompt, image1_path, image2_path):
    images = [Image.open(image1_path).convert("RGB"), Image.open(image2_path).convert("RGB")]
    image_tensor = process_images(images, image_processor, model.config).to(model.device, dtype=model.dtype)

    conv = conv_templates["llava_v1"].copy()
    conv.append_message(conv.roles[0], prompt)
    conv.append_message(conv.roles[1], None)
    prompt_text = conv.get_prompt()

    input_ids = tokenizer_image_token(prompt_text, tokenizer, return_tensors="pt").unsqueeze(0).to(model.device)

    output_ids = model.generate(
        input_ids=input_ids,
        images=image_tensor,
        max_new_tokens=512,
        temperature=0,
        do_sample=False
    )

    return tokenizer.decode(output_ids[0][input_ids.shape[1]:], skip_special_tokens=True).strip()

# === Run Inference for All Pairs ===
results = []
for img1_name, img2_name in image_pairs:
    img1_path = os.path.join(dataset_folder, img1_name)
    img2_path = os.path.join(dataset_folder, img2_name)

    for idx, prompt in enumerate(prompts):
        print(f"🔍 {img1_name} vs {img2_name} | Prompt: {cot_labels[idx]}")
        output = run_inference(prompt, img1_path, img2_path)

        results.append({
            "image1": img1_name,
            "image2": img2_name,
            "prompt_type": cot_labels[idx],
            "prompt_text": prompt,
            "generated_text": output
        })

# === Save to CSV ===
output_csv = "Task1_MED_outputs.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image1", "image2", "prompt_type", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print(f"\n✅ Done! Results saved to {output_csv}")
'''