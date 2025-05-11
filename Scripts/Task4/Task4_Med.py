# -*- coding: utf-8 -*-
"""
Batch Inference for Task 3 
(10 Combined Images × 10 Prompts) using Llava-Med (via eval_model)
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
    "Baseline": "Which molecule is more likely to undergo an SN1 reaction, and why?",
    "Stepwise_1": "Analyze each molecule in steps. First, identify the leaving group. Then, consider how stable the carbocation would be if that group left. Finally, determine which molecule favors an SN1 mechanism.",
    "Stepwise_2": "Step by step: (1) What’s the leaving group in each molecule? (2) If it leaves, how stable is the resulting carbocation? (3) Based on that, which molecule is more likely to follow SN1?",
    "Stepwise_3": "Which molecule loses its leaving group more easily? Which forms a stable carbocation? Use these steps to predict which one undergoes SN1 more readily.",
    "Visual_1": "Look at the structure of both molecules. Which one has a group that looks easier to break off? Use this to decide which could follow an SN1 path.",
    "Visual_2": "Scan each molecule for ring structures or conjugated systems near the leaving group site. Which structure looks more capable of dispersing charge?",
    "Visual_3": "Observe how isolated the leaving group appears in each structure. Which one looks more 'exposed' or weakly connected — a possible sign of easier SN1 departure?",
    "Explanation_1": "The best SN1 substrates are those where the leaving group leaves easily, and the molecule can stabilize the resulting positive charge. Based on this, which one is a better candidate?",
    "Explanation_2": "The more stable the carbocation intermediate, the more likely an SN1 mechanism will occur. Consider how the structure of each molecule affects the stability of its carbocation.",
    "Explanation_3": "Molecules that undergo SN1 easily often contain benzylic or allylic positions that stabilize carbocations. Does either molecule contain such a feature?"
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
