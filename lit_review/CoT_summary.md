# CoT Structure Summary Table

| # | Year | Paper | CoT Family | Model(s) | Dataset(s) | Prompt Format | Notes | Example Prompt |
|---|------|-------|------------|----------|------------|----------------|-------|----------------|
| 1 | 2022 | Wei et al. – CoT Prompting | Stepwise | GPT-3 | GSM8K, AQuA | "Let's think step by step" | Introduced CoT for reasoning; foundational. | Q: If there are 3 cars and each has 4 wheels, how many wheels? A: Let's think step by step. First, each car has 4 wheels... |
| 2 | 2022 | Kojima et al. – Zero-shot CoT | Stepwise | GPT-3 | GSM8K, AQuA | Adds CoT phrase to zero-shot | Shows CoT can emerge with cue alone. | Q: John has 5 apples, gives away 2. How many left? A: Let's think step by step. John starts with 5... |
| 3 | 2023 | Lu et al. – Learn to Explain | Meta / Stepwise | PaLM | StrategyQA | CoT as supervised signal | CoT is part of the training target. | Q: Is sugar bad for you? A: [Rationale] Sugar can lead to health issues if consumed excessively. [Answer] Yes. |
| 4 | 2023 | Li et al. – Self-Taught Reasoner | Stepwise / Meta | GPT-3 | MathQA, CommonsenseQA | Self-generated CoT | Iterative self-refinement of reasoning. | *(empty)* |
| 5 | 2023 | Chen & Feng – Reasoning Like a Student | Modular / Meta | GPT-4 | Custom visual QA | Teacher-student prompt dialog | Multi-role CoT as conversation. | *(empty)* |
| 6 | 2023 | Zheng et al. – MM-ReAct | Modular | BLIP-2 + LLM | ScienceQA | Multi-agent: tool + LLM | Combines visual tool and LLM reasoning. | *(empty)* |
| 7 | 2023 | Gao et al. – Socratic VQA | Modular | BLIP-2 + LLaVA | VQAv2 | Questioner + explainer roles | Multi-turn modular prompting. Visual reasoning broken down by agent. | *(empty)* |
| 8 | 2023 | Zhou et al. – MiniGPT-4 | Visual-first | MiniGPT-4 | COCO, custom | Image + scene description first, then reasoning | Grounded CoT based on visual parsing, not text-only. | *(empty)* |
| 9 | 2023 | Mitra et al. – Knowledge-Aug CoT | Visual-first | Visual ChatGPT | OKVQA | External search tool + image input + prompt | Augments CoT with web search results + image context. | *(empty)* |
|10 | 2023 | Mondal et al. – UniVisualGPT | Visual-first | UniVisualGPT | GQA, VizWiz | Scene graph → step-by-step CoT | Visual-first parsing for scene + goal grounding. | *(empty)* |
|11 | 2023 | Zhang et al. – CoT-GNN | Contrastive | CoT-GNN | Image pairs | CoT from image comparison | Differences between paired images drive reasoning path. | *(empty)* |
|12 | 2023 | Yang et al. – Self-Taught CoT Transfer | Meta / Stepwise | GPT-3 | MathQA, CommonsenseQA | Prompt with few-shot CoT examples | Trains models to transfer CoT skills across domains. | Q: What is the boiling point of water? A: [CoT] Water boils at 100°C at sea level due to atmospheric pressure. [Answer] 100°C |
|13 | 2023 | Chen et al. – Prompting CoT for VQA | Modular | BLIP-2 | VQAv2 | Explicit step-by-step visual QA CoT | Guides attention across image + question with reasoning steps. | *(empty)* |
|14 | 2023 | Feng et al. – Teaching Prompt Design | Meta | GPT-4 | Custom | CoT as curriculum for teaching | Explores how humans teach CoT using example prompts + feedback. | *(empty)* |
