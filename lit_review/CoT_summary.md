# CoT Structure Summary Table

| **Paper** | **CoT Family** | **Model(s)** | **Dataset(s)** | **Prompting Style** | **Notes / Quotes** |
|----------|----------------|--------------|----------------|----------------------|---------------------|
| Wei et al. (2022) – Chain-of-Thought Prompting | Stepwise | GPT-3 | GSM8K, AQuA | "Let's think step by step" | Foundational work in CoT prompting |
| Kojima et al. (2022) – Zero-shot CoT | Stepwise | GPT-3 | GSM8K, AQuA | Zero-shot + CoT cue | Simple prompt elicits reasoning |
| Lu et al. (2023) – Learn to Explain | Meta / Stepwise | PaLM | StrategyQA | CoT as supervised training signal | Teaches model to produce CoT |
| Li et al. (2023) – Self-Taught Reasoner | Stepwise / Meta | GPT-3 | MathQA, CommonsenseQA | Prompted with self-generated CoT | Model refines its own CoT |
| Chen & Feng (2023) – Reasoning Like a Student | Modular / Meta | GPT-4 | Custom visual QA | Role-based prompting | Uses tutor-student simulation |
| Zheng et al. (2023) – MM-ReAct | Modular | BLIP-2 + LLM | ScienceQA | Multi-agent: visual tool + LLM | Modular agent-style CoT |
| Gao et al. (2023) – Socratic VQA | Modular | BLIP-2 + LLaVA | VQAv2 | Questioner + Explainer | Agentized roles create CoT |
| Zhou et al. (2023) – MiniGPT-4 | Visual-first | MiniGPT-4 | COCO, custom | Image-grounded prompts | Scene understanding before text |
| Mitra et al. (2023) – Knowledge-Augmented CoT | Visual-first | Visual ChatGPT | OKVQA | Uses search tools in reasoning | Grounded tool use |
| Mondal et al. (2023) – UniVisualGPT | Visual-first | UniVisualGPT | GQA, VizWiz | Scene graph-based CoT | Visual parser supports CoT |
| Zhang et al. (2023) – CoT-GNN | Contrastive | CoT-GNN | Image pairs | Scene comparison | Differences drive reasoning |
| Yang et al. (2023) – Self-Taught CoT Transfer | Meta / Stepwise | GPT-3 | MathQA, CommonsenseQA | Few-shot teaching + transfer | CoT learning from samples |
| Chen et al. (2023) – Prompting CoT for VQA | Modular | BLIP-2 | VQAv2 | Multi-step visual reasoning | Explicit visual steps prompted |
| Feng et al. (2023) – Teaching Prompt Design | Meta | GPT-4 | Custom | Prompt as curriculum | Studies how humans teach CoT |

