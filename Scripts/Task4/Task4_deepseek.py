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
    ("Aniline.png", "Phenol.png"),
    ("Paracetamol.png", "Morphine.png"),
    ("Caffeine.png", "Adenine.png"),
    ("Ibuprofen.png", "Salicylic-acid.png"),
    ("Methanol.png", "Ethanol.png"),
    ("Acetic-acid.png", "Benzoic_acid.png"),
    ("Cyclohexane.png", "Benzene.png"),
    ("Formic_acid.png", "Nitrobenzene.png"),
    ("Pyridine_numbers.png", "Pyrrole-numbered.png"),
    ("Furan-full.png", "Thiophene-full.png")
]

prompts = {
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

cot_types = list(prompts.keys())

# --- Step 3: Output Setup ---
os.makedirs("outputs", exist_ok=True)
csv_file = open("outputs/Task4_deepseek_outputs.csv", "w", encoding="utf-8", newline="")
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
print("!!!! All results saved to outputs/Task4_deepseek_outputs.csv")