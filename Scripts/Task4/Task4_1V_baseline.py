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
# --- Step 3: 20 Stepwise Prompts for Acid/Base Comparison ---
baseline_prompt = ["Which molecule is more likely to undergo an SN1 reaction, and why?"]

cot_types = ["Baseline"] * len(baseline_prompt)

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
    
    for idx, prompt_text in enumerate(baseline_prompt):
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
output_csv = "Task4_Baseline_Res0.csv"
with open(output_csv, mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["image1", "image2", "prompt_type", "prompt_number", "prompt_text", "generated_text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"\n✅ All results saved to {output_csv}")
