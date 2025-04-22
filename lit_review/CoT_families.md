# 📚 Chain-of-Thought Structure Families

This table categorizes 14 key papers into 5 distinct CoT structure families based on how they formulate, teach, or apply reasoning chains in multimodal or language tasks.

| **Family** | **Definition** | **Paper** | **Year** | **Example Prompt** | **Why It Belongs** |
|------------|----------------|-----------|----------|---------------------|---------------------|
| Stepwise | Classic step-by-step CoT triggered by explicit reasoning cues | Wei et al. – CoT Prompting | 2022 | Q: If there are 3 cars... A: Let's think step by step... | Foundational CoT work showing direct reasoning chains |
| ↑ | ↑ | Kojima et al. – Zero-shot CoT | 2022 | Q: John has 5 apples... A: Let's think step by step... | Demonstrates zero-shot CoT by adding cue alone |
| ↑ / Meta | ↑ | Li et al. – Self-Taught Reasoner | 2023 | *(none)* | Model generates and refines its own CoT iteratively |
| Modular / Meta | CoT emerges through modular roles or tool-assisted dialog | Chen & Feng – Reasoning Like a Student | 2023 | *(none)* | Simulates teacher-student dialog to construct CoT |
| ↑ | ↑ | Zheng et al. – MM-ReAct | 2023 | *(none)* | Uses visual tool → LLM reasoning split across agents |
| ↑ | ↑ | Gao et al. – Socratic VQA | 2023 | *(none)* | Distinct roles (questioner + explainer) guide the CoT |
| ↑ | ↑ | Chen et al. – Prompting CoT for VQA | 2023 | *(none)* | Visual questions are answered step-by-step via modular blocks |
| Visual-first | Reasoning starts from parsed visual content or tools | Zhou et al. – MiniGPT-4 | 2023 | *(none)* | Reasoning grounded in image descriptions before CoT |
| ↑ | ↑ | Mitra et al. – Knowledge-Aug CoT | 2023 | *(none)* | Augments reasoning with visual + retrieved info |
| ↑ | ↑ | Mondal et al. – UniVisualGPT | 2023 | *(none)* | Builds reasoning steps from scene graphs and image states |
| Contrastive | CoT formed by comparing multiple inputs/scenes | Zhang et al. – CoT-GNN | 2023 | *(none)* | Uses differences between image pairs to drive logic |
| Meta / Stepwise | CoT is taught or transferred explicitly across domains | Lu et al. – Learn to Explain | 2023 | Q: Is sugar bad... A: [Rationale] ... [Answer] Yes. | Supervised CoT targets teach interpretable logic |
| ↑ | ↑ | Yang et al. – Self-Taught CoT Transfer | 2023 | Q: What is the boiling point... A: [CoT] ... | Shows how CoT prompting is transferred across tasks |
| Meta | ↑ | Feng et al. – Teaching Prompt Design | 2023 | *(none)* | Investigates how humans teach CoT via prompt design |

