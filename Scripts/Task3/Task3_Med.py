# -*- coding: utf-8 -*-
"""
Batch Inference for Task 3 
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
image_folder = "/home/yx3493/llvm/T3/img"
output_csv = "Task3_MED_outputs.csv"

image_files = [f"{i}.png" for i in range(1, 11)]

prompt_templates = {
    "Baseline": 
    "Which molecule is a better nucleophile, the first or the second? Why?",  # Baseline
    "Stepwise": 
    "Step-by-step: First, identify potential nucleophilic sites. Second, evaluate charge delocalization. Third, assess solvent effects if any are implied. Finally, choose the better nucleophile and explain your choice.",  # Stepwise
    "Visual_first": 
    "From the image, focus on the reactive centers. Do you see bulky groups that block attack? Do you see resonance that spreads out charge? Pick the more reactive nucleophile.",  # Visual-first
    "Explanation_first": 
    "To decide which is more nucleophilic, we need to consider the atom's electron density, resonance stabilization, and any steric hindrance. Let's apply this reasoning to the two molecules." # Explanation-first
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
