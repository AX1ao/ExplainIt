from transformers import AutoTokenizer
from deepseek_vl.models import VLChatProcessor, MultiModalityCausalLM
from deepseek_vl.utils.io import load_pil_images
import torch
from PIL import Image
import os
import csv

# --- Step 1: Load DeepSeek Model and Processor ---
model_id = "deepseek-ai/deepseek-vl-7b-chat"
device = "cuda" if torch.cuda.is_available() else "cpu"

model = MultiModalityCausalLM.from_pretrained(model_id, trust_remote_code=True).to(torch.bfloat16).cuda().eval()
vl_chat_processor = VLChatProcessor.from_pretrained(model_id)
tokenizer = vl_chat_processor.tokenizer

# --- Step 2: Set Dataset Folder and Image Pairs ---
dataset_folder = "/content"

image_pairs = [
    ("Ammonia.png", "Methanol.png"),
    ("MeNH2.png", "Aniline.png"),
    ("Imidazole_full.png", "Pyridine-full.png"),
    ("Ethanol.png", "Phenol.png"),
    ("Pyrrole-full.png", "Pyridine-full.png"),
    ("Cytosine.png", "Uracil.png"),
    ("Histamine.png", "Imidazole_numbered.png"),
    ("Benzaldehyde.png", "Benzoic_acid.png"),
    ("Nicotinamid.png", "Purine.png"),
    ("Furan-full.png", "Thiophene-full.png")
]

cot_types = ["Baseline", "Stepwise", "Visual_first", "Explanation_first"]

prompts = {
    "Baseline": "Which molecule is a better nucleophile, the first or the second? Why?",
    "Stepwise": "Step-by-step: First, identify potential nucleophilic sites. Second, evaluate charge delocalization. Third, assess solvent effects if any are implied. Finally, choose the better nucleophile and explain your choice.",
    "Visual_first": "From the image, focus on the reactive centers. Do you see bulky groups that block attack? Do you see resonance that spreads out charge? Pick the more reactive nucleophile.",
  "Explanation_first": "To decide which is more nucleophilic, we need to consider the atom's electron density, resonance stabilization, and any steric hindrance. Let's apply this reasoning to the two molecules."
}

# --- Step 3: Output Setup ---
os.makedirs("outputs", exist_ok=True)
csv_file = open("outputs/Task3_deepseek_outputs.csv", "w", encoding="utf-8", newline="")
writer = csv.DictWriter(csv_file, fieldnames=["image1", "image2", "prompt_type", "prompt_text", "generated_text"])
writer.writeheader()

# --- Step 4: Run Inference ---
for img1, img2 in image_pairs:
    img_path1 = os.path.join(dataset_folder, img1)
    img_path2 = os.path.join(dataset_folder, img2)
    for cot in cot_types:
        prompt = prompts[cot]
        conversation = [
            {
                "role": "User",
                "content": prompt,
                "images": [img_path1, img_path2]
            },
            {
                "role": "Assistant",
                "content": ""
            }
        ]

        images = load_pil_images(conversation)
        prepare_inputs = vl_chat_processor(
            conversations=conversation,
            images=images,
            force_batchify=True
        ).to(model.device)

        with torch.no_grad():
            inputs_embeds = model.prepare_inputs_embeds(**prepare_inputs)
            outputs = model.language_model.generate(
                inputs_embeds=inputs_embeds,
                attention_mask=prepare_inputs.attention_mask,
                pad_token_id=tokenizer.eos_token_id,
                bos_token_id=tokenizer.bos_token_id,
                eos_token_id=tokenizer.eos_token_id,
                max_new_tokens=512,
                do_sample=False,
                use_cache=True
            )

        answer = tokenizer.decode(outputs[0].cpu().tolist(), skip_special_tokens=True)
        print(f"--- Finished {cot} for {img1} and {img2}")
        writer.writerow({
            "image1": img1,
            "image2": img2,
            "prompt_type": cot,
            "prompt_text": prompt,
            "generated_text": answer.strip()
        })

csv_file.close()
print("!!!! All results saved to outputs/Task3_deepseek_outputs.csv")