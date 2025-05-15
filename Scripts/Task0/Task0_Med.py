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
image_folder = "/content"
save_folder = "/content/outputs_llava"
os.makedirs(save_folder, exist_ok=True)

# === 3. Define 4 Prompt Templates ===
prompt_templates = {
    "Baseline": "What is this molecule?",

    "Stepwise CoT": """
    	Let's analyze this molecule step by step.
		First, identify the atoms present in the structure.
		Then, observe how the atoms are connected — are there any rings, chains, or branches?
		Finally, based on the overall connectivity and functional groups observed, what is the most likely identity of this molecule?
	""",

    "Visual-First CoT": """
    	Carefully observe the visual structure of the molecule.
		Which atoms are present, and how are they arranged?
		Look for distinctive features such as rings, branching chains, or functional groups.
		Based on these visual observations, deduce the most likely identity of this molecule.
	""",

    "Explanation-First CoT": """
    	A molecule can often be identified by analyzing its key features:
			1. The types of atoms present (e.g., carbon, hydrogen, oxygen, nitrogen).
			2. The connectivity between atoms, such as rings, chains, or branches.
			3. Specific functional groups like hydroxyl (OH), carbonyl (C=O), or amine (NH₂).
		Now, examine the given image.
		Which atoms and structural patterns are present?
		Based on these observations and known chemical structures, what is the most likely identity of this molecule?
	"""
}

# === 6. Infer for each image and collect outputs into one file ===
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png'))]
output_file = os.path.join(save_folder, "all_outputs.txt")
with open(output_file, "w") as f:
    for img_file in image_files:
        img_path = os.path.join(image_folder, img_file)
        print(f" Processing Image: {img_file}")
        f.write(f"===== Image: {img_file} =====\n\n")

        for style, prompt in prompt_templates.items():
            print(f"  Using Prompt Style: {style}")

            args = types.SimpleNamespace(
                model_path=model_path,
                model_base=None,
                model_name=get_model_name_from_path(model_path),
                query=prompt,
                conv_mode=None,
                image_file=img_path,
                sep=",",
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

print("All Done! Outputs saved to:", output_file)