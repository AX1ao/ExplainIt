from transformers import AutoTokenizer, AutoProcessor
from deepseek_vl.models import VLChatProcessor, MultiModalityCausalLM
from deepseek_vl.utils.io import load_pil_images
import torch
from PIL import Image
import os
import csv

# ----- 1. Setup Model -----
model_id = "deepseek-ai/deepseek-vl-7b-chat"
device = "cuda" if torch.cuda.is_available() else "cpu"

model = MultiModalityCausalLM.from_pretrained(model_id, trust_remote_code=True)\
    .to(torch.bfloat16).cuda().eval()
vl_chat_processor = VLChatProcessor.from_pretrained(model_id)
tokenizer = vl_chat_processor.tokenizer

# ----- 2. Define CoT Templates -----
prompts = {
    "baseline": '''<image_placeholder>First molecule.
        <image_placeholder>Second molecule.
        Which molecule is more reactive toward electrophilic aromatic substitution, the first or the second? Why?''',
    "stepwise": '''
        <image_placeholder>First molecule.
        <image_placeholder>Second molecule.
        First, note if the ring has electron-donating substituents.
        Then, note if it has electron-withdrawing substituents.
        Finally, determine which ring is more reactive toward electrophiles.
    ''',
    "visual_first": '''
        <image_placeholder>First molecule.
        <image_placeholder>Second molecule.
        Observe visible features: are there -OH, -NH₂, or -NO₂ groups?
        Count and compare electron-donating versus electron-withdrawing groups for both molecules.
    ''',
    "explanation_first": '''
        <image_placeholder>First molecule.
        <image_placeholder>Second molecule.
        Consider the net electronic effect (donating vs withdrawing) based on the visible substituents.
        Then predict which molecule will react faster toward EAS.
    '''
}

# ----- 3. Define image pairs -----
dataset_folder = ""  # Modify this if your images are in a specific path
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

# ----- 4. Output File -----
os.makedirs("outputs", exist_ok=True)
csv_file = open("outputs/Task1_deepseek_outputs.csv", "w", encoding="utf-8", newline="")
writer = csv.DictWriter(csv_file, fieldnames=["image1", "image2", "prompt_type", "prompt_text", "generated_text"])
writer.writeheader()

# ----- 5. Inference Loop -----
for img1, img2 in image_pairs:
    print(f" Processing pair: {img1} + {img2}")
    img_path1 = os.path.join(dataset_folder, img1)
    img_path2 = os.path.join(dataset_folder, img2)

    for prompt_type, raw_prompt in prompts.items():
        prompt_text = raw_prompt.replace("<image_placeholder_1>", "").replace("<image_placeholder_2>", "")

        conversation = [
            {
                "role": "User",
                "content": prompt_text,
                "images": [img_path1, img_path2]
            },
            {
                "role": "Assistant",
                "content": ""
            }
        ]

        # Load images
        images = load_pil_images(conversation)

        # Preprocess with explicit system_prompt=""
        prepare_inputs = vl_chat_processor(
            conversations=conversation,
            images=images,
            force_batchify=True,
            system_prompt=""
        ).to(model.device)

        # Inference
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

        # Decode result
        answer = tokenizer.decode(outputs[0].cpu().tolist(), skip_special_tokens=True)

        # Save result
        writer.writerow({
            "image1": img1,
            "image2": img2,
            "prompt_type": prompt_type,
            "prompt_text": prompt_text.strip(),
            "generated_text": answer.strip()
        })

        print(f" Finished {prompt_type} for {img1} and {img2}")

csv_file.close()
print("All inference completed and saved to outputs/Task1_deepseek_outputs.csv")