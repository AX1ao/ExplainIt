from transformers import AutoTokenizer, AutoProcessor
from deepseek_vl.models import VLChatProcessor, MultiModalityCausalLM
from deepseek_vl.utils.io import load_pil_images
import torch
from PIL import Image
import os

# ----- 1. Setup Model -----
model_id = "deepseek-ai/deepseek-vl-7b-chat"
device = "cuda" if torch.cuda.is_available() else "cpu"

model = MultiModalityCausalLM.from_pretrained(model_id, trust_remote_code=True)
		.to(torch.bfloat16).cuda().eval()
vl_chat_processor = VLChatProcessor.from_pretrained(model_id)
tokenizer = vl_chat_processor.tokenizer

# ----- 2. Define CoT Templates -----
prompts = {
    "baseline": "<image_placeholder>What is this molecule?",
    "stepwise": '''
    	<image_placeholder>Let's analyze this molecule step by step.
		First, identify the types of atoms present in the structure.
		Then, examine how these atoms are connected — are they forming rings, chains, or branches?
		Finally, based on the overall connectivity and functional groups observed, infer the most likely identity of this molecule.
	''',
    "visual_first": '''
    	<image_placeholder>Carefully observe the visual structure of the molecule.
		Which atoms are present, and how are they arranged?
		Look for distinctive features such as rings, branching chains, or functional groups.
		Based on these visual observations, deduce the most likely identity of this molecule.
	''',
    "explanation_first": '''
    	<image_placeholder>Recall that molecular structures can often be identified by recognizing patterns such as ring formations, functional groups, and atom connectivity.
		Given this knowledge, observe the molecule carefully.
		What structural features do you notice?
		Now, apply your understanding to infer the molecule's identity.
	'''
}

# ----- 3. Define your image list -----
image_folder = "./your_image_folder"
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png'))]

# ----- 4. Output File -----
os.makedirs("outputs", exist_ok=True)
output_file = open("outputs/all_inference_results.txt", "w", encoding="utf-8")

# ----- 5. Inference Loop -----
for img_name in image_files:
    print(f"🔵 Processing image: {img_name}")
    img_path = os.path.join(image_folder, img_name)
    img = Image.open(img_path).convert("RGB")
    
    for prompt_type, prompt_template in prompts.items():
        conversation = [
            {
                "role": "User",
                "content": prompt_template,
                "images": [img_path]
            },
            {
                "role": "Assistant",
                "content": ""
            }
        ]
        
        # Load image into processor
        images = load_pil_images(conversation)
        
        # Preprocess
        prepare_inputs = vl_chat_processor(
            conversations=conversation,
            images=images,
            force_batchify=True
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
        
        # Decode
        answer = tokenizer.decode(outputs[0].cpu().tolist(), skip_special_tokens=True)
        
        # Save result
        output_file.write(f"===== Image: {img_name} | Prompt: {prompt_type} =====\n")
        output_file.write(answer.strip() + "\n\n")
        print(f"✅ Finished {prompt_type} for {img_name}")

output_file.close()
print("🎉 All inference completed and saved to outputs/all_inference_results.txt")