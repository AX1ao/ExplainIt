from transformers import AutoTokenizer
from deepseek_vl.models import VLChatProcessor, MultiModalityCausalLM
from deepseek_vl.utils.io import load_pil_images
import torch
from PIL import Image
import os
import csv

# ----- 1. Setup Model -----
model_id = "deepseek-ai/deepseek-vl-7b-chat"
device = "cuda" if torch.cuda.is_available() else "cpu"

model = MultiModalityCausalLM.from_pretrained(model_id, trust_remote_code=True).to(torch.bfloat16).cuda().eval()
vl_chat_processor = VLChatProcessor.from_pretrained(model_id)
tokenizer = vl_chat_processor.tokenizer

# ----- 2. Define Prompts (Baseline + 15 CoT prompts) -----
baseline_prompt = ["Which molecule is a better nucleophile, the first or the second? Why?"]

stepwise_prompts = [
    "Step-by-step: First, identify potential nucleophilic sites. Second, evaluate charge delocalization. Third, assess solvent effects if any are implied. Finally, choose the better nucleophile and explain your choice.",
    "Step 1: Examine the electron density of each molecule. Step 2: Identify atoms capable of donating a lone pair. Step 3: Consider resonance or inductive effects. Step 4: Compare steric hindrance. Step 5: Decide which molecule is the better nucleophile and explain why."
]

visual_first_prompts = [
    "From the image, focus on the reactive centers. Do you see bulky groups that block attack? Do you see resonance that spreads out charge? Pick the more reactive nucleophile.",
    "Check the structures: Which molecule has a more exposed, electron-rich site? Which one looks less crowded? Use visual evidence to answer which is the better nucleophile."
]

explanation_first_prompts = [
    "To decide which is more nucleophilic, we need to consider the atom's electron density, resonance stabilization, and any steric hindrance. Let's apply this reasoning to the two molecules.",
    "Let’s first recall: nucleophiles attack electrophiles using available electrons. A good nucleophile is both electron-rich and sterically unencumbered. Which molecule better matches this?"
]

all_prompts = baseline_prompt + stepwise_prompts + visual_first_prompts + explanation_first_prompts

cot_types = (
    ["Baseline"] +
    ["Stepwise"] * len(stepwise_prompts) +
    ["Visual_first"] * len(visual_first_prompts) +
    ["Explanation_first"] * len(explanation_first_prompts)
)

# ----- 3. Define Image Pairs -----
dataset_folder = "/content"
image_pairs = [
    ("Pyrrole-full.png", "Pyridine-full.png"),
    ("Cytosine.png", "Uracil.png"),
    ("Histamine.png", "Imidazole_numbered.png")
]

# ----- 4. Output Setup -----
os.makedirs("outputs", exist_ok=True)
csv_file = open("outputs/Task2_deepseek_finetune-res.csv", "w", encoding="utf-8", newline="")
writer = csv.DictWriter(csv_file, fieldnames=["image1", "image2", "prompt_type", "prompt_number", "prompt_text", "generated_text"])
writer.writeheader()

# ----- 5. Inference -----
for img1, img2 in image_pairs:
    img_path1 = os.path.join(dataset_folder, img1)
    img_path2 = os.path.join(dataset_folder, img2)
    for idx, prompt_template in enumerate(all_prompts):
        prompt_type = cot_types[idx]
        conversation = [
            {
                "role": "User",
                "content": prompt_template,
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
        print(f"--- Finished {prompt_type} #{idx+1} for {img1} and {img2}")
        writer.writerow({
            "image1": img1,
            "image2": img2,
            "prompt_type": prompt_type,
            "prompt_number": idx + 1,
            "prompt_text": prompt_template,
            "generated_text": answer.strip()
        })

csv_file.close()
print("!!!! All pair inference completed and saved to outputs/Task3_deepseek_finetune-res.csv")