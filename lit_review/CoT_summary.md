# CoT Structure Summary Table

| # | Year | Paper | CoT Family | Model(s) | Dataset(s) | Prompt Format | Notes |
|---|------|-------|------------|----------|------------|----------------|-------|
| 1 | 2022 | Wei et al. – CoT Prompting | Stepwise | GPT-3 | GSM8K, AQuA | "Let's think step by step" | Introduced CoT as a reasoning enhancer for arithmetic QA tasks. Baseline for most CoT work. |
| 2 | 2022 | Kojima et al. – Zero-shot CoT | Stepwise | GPT-3 | GSM8K, AQuA | Adds "Let's think step by step" to zero-shot prompt | Shows CoT can be triggered without examples. |
| 3 | 2023 | Lu et al. – Learn to Explain | Meta / Stepwise | PaLM | StrategyQA | CoT as supervised signal | Teaches model to generate CoT via rationale + answer. Highlights interpretability and planning. |
| 4 | 2023 | Li et al. – Self-Taught Reasoner | Stepwise / Meta | GPT-3 | MathQA, CommonsenseQA | Generates CoT, reuses its own best | Self-boosting model with iterative self-CoT refinement. |
| 5 | 2023 | Chen & Feng – Reasoning Like a Student | Modular / Meta | GPT-4 | Custom visual QA | Role-based prompting: teacher + student | Combines CoT generation and CoT teaching via dialog. |
| 6 | 2023 | Zheng et al. – MM-ReAct | Modular | BLIP-2 + LLM | ScienceQA | Multi-agent prompt: vision tool + reasoning agent | Combines external visual tool use with LLM CoT reasoning. |
| 7 | 2023 | Gao et al. – Socratic VQA | Modular | BLIP-2 + LLaVA | VQAv2 | Questioner + explainer roles | Multi-turn modular prompting. Visual reasoning broken down by agent. |
| 8 | 2023 | Zhou et al. – MiniGPT-4 | Visual-first | MiniGPT-4 | COCO, custom | Image + scene description first, then reasoning | Grounded CoT based on visual parsing, not text-only. |
| 9 | 2023 | Mitra et al. – Knowledge-Aug CoT | Visual-first | Visual ChatGPT | OKVQA | External search tool + image input + prompt | Augments CoT with web search results + image context. |
|10 | 2023 | Mondal et al. – UniVisualGPT | Visual-first | UniVisualGPT | GQA, VizWiz | Scene graph → step-by-step CoT | Visual-first parsing for scene + goal grounding. |
|11 | 2023 | Zhang et al. – CoT-GNN | Contrastive | CoT-GNN | Image pairs | CoT from image comparison | Differences between paired images drive reasoning path. |
|12 | 2023 | Yang et al. – Self-Taught CoT Transfer | Meta / Stepwise | GPT-3 | MathQA, CommonsenseQA | Prompt with few-shot CoT examples | Trains models to transfer CoT skills across domains. |
|13 | 2023 | Chen et al. – Prompting CoT for VQA | Modular | BLIP-2 | VQAv2 | Explicit step-by-step visual QA CoT | Guides attention across image + question with reasoning steps. |
|14 | 2023 | Feng et al. – Teaching Prompt Design | Meta | GPT-4 | Custom | CoT as curriculum for teaching | Explores how humans teach CoT using example prompts + feedback. |
