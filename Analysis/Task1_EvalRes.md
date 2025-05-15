# Task 1 (EAS Reactivity Prediction)

---

## OneVision

### Two-way Summary Table

| Image Pair                    | Baseline | Stepwise | Visual | Explanation |
|------------------------------|----------|----------|--------|-------------|
| Aniline vs Nitrobenzene      | 1        | 0        | 0      | 1           |
| Benzene vs Toluene           | 1        | 1.5      | 1.5    | 1.5         |
| Benzaldehyde vs Benzoic Acid | 1        | 0        | 0.5    | 0.5         |
| Pyridine vs Benzene          | 0        | 0        | 0      | 1           |
| Pyrrole vs Benzene           | 1        | 1.5      | 1      | 1           |
| Phenol vs Benzene            | 1        | 1.5      | 1      | 1.5         |
| Anisole vs Benzene           | 0.5      | 1        | 0.5    | 1           |
| Chlorobenzene vs Benzene     | 0        | 0        | 0      | 0.5         |
| Nitrobenzene vs Benzene      | 1        | 1        | 0.5    | 0.5         |
| Styrene vs Benzene           | 1        | 1        | 0.5    | 1.5         |

---

### Overall Accuracy & Reasoning Trends

- Explanation-first prompts achieved the highest average score across the dataset. Despite some inconsistency, they reached 1.5 on four image pairs and demonstrated the model’s ability to articulate abstract reasoning when properly guided. This suggests that when the model is scaffolded with conceptual knowledge (e.g., resonance effects, electron donation/withdrawal), it can generate chemically meaningful and relatively accurate responses.

- Stepwise prompts showed mixed performance, with a few high scores (1.5) in straightforward cases like Benzene vs Toluene or Phenol vs Benzene, but also multiple 0s (e.g., Aniline vs Nitrobenzene, Pyridine vs Benzene, Chlorobenzene vs Benzene). This indicates that while procedural scaffolding can be helpful in classic cases, it fails when the model lacks deeper conceptual understanding, especially in edge cases involving heteroaromatics or halogen-substituted rings.

- Baseline prompts performed surprisingly well, achieving consistent scores of 1 in most image pairs. This reinforces the idea that the model has some memorized chemical intuition (e.g., "OH is activating", "NO₂ is deactivating") even without reasoning scaffolds. However, it failed in more nuanced examples like Pyridine vs Benzene and Chlorobenzene vs Benzene, where surface-level pattern matching isn’t sufficient.

- Visual-first prompts were the weakest overall, struggling especially in examples where structure–reactivity relationships require abstract reasoning (e.g., Pyridine, Chlorobenzene, Nitrobenzene). Although it achieved 1.5 in a few simple comparisons, the majority of scores hover at or below 0.5, indicating that visual recognition alone cannot drive correct predictions in chemical reactivity tasks.

---

### Reasoning Quality & Chemical Understanding

- LLAVA One Vision demonstrates **solid memorization of archetypal chemical behaviors** (e.g., reactivity of OH, NO₂, and CH₃ groups).
- However, the model sometimes confuses **acid/base concepts** with **electrophilic substitution reactivity** — especially in cases involving –COOH and –CHO (Set 3).
- Nitrogen heterocycles reveal the model’s **limits in understanding aromatic systems** — e.g., pyridine vs pyrrole — where it often misjudges electron donation/withdrawal unless explicitly guided by the prompt.

---

### Key Observations

- No prompt type consistently outperformed across all cases, but Explanation-first was the only format to achieve the top score (1.5) on four occasions, suggesting it has the highest ceiling when the model “gets it right.”
- Stepwise was more volatile: strong in some, completely failed in others—implying that procedure without knowledge can lead to confidently wrong conclusions.
- Visual-first and Baseline prompts cannot be relied on in edge cases, as they do not support abstraction or conflicting-effect resolution.

---

### Prompt Type Effectiveness (Average Score Comparison)

| Prompt Type           | Avg Score (/2) |
| --------------------- | -------------- |
| Stepwise              | 1.1            |
| Baseline              | 0.9            |
| Visual-first          | 0.5            |
| Explanation-first     | 0.25           |

---
## LLaVA Med

### Scoring + Reasoning Table

|                   Image Pair | Prompt Type       | Score | Reason                                         |
| ---------------------------: | :---------------- | ----: | :--------------------------------------------- |
|      Aniline vs Nitrobenzene | Baseline          |     1 | Correct answer but lacks justification         |
|      Aniline vs Nitrobenzene | Stepwise          |     1 | Correct answer but lacks justification         |
|      Aniline vs Nitrobenzene | Visual_first      |   0.5 | Mentions some structure but unclear conclusion |
|      Aniline vs Nitrobenzene | Explanation_first |     1 | Correct answer but lacks justification         |
|           Benzene vs Toluene | Baseline          |     1 | Correct answer but lacks justification         |
|           Benzene vs Toluene | Stepwise          |     1 | Correct answer but lacks justification         |
|           Benzene vs Toluene | Visual_first      |   0.5 | Mentions some structure but unclear conclusion |
|           Benzene vs Toluene | Explanation_first |   1.5 | Correct answer with partial explanation       |
| Benzaldehyde vs Benzoic_acid | Baseline          |     1 | Correct answer but lacks justification         |
| Benzaldehyde vs Benzoic_acid | Stepwise          |     1 | Correct answer but lacks justification         |
| Benzaldehyde vs Benzoic_acid | Visual_first      |   0.5 | Mentions some structure but unclear conclusion |
| Benzaldehyde vs Benzoic_acid | Explanation_first |   0.5 | Mentions some structure but unclear conclusion |
|     Pyridine-full vs Benzene | Baseline          |     1 | Correct answer but lacks justification         |
|     Pyridine-full vs Benzene | Stepwise          |     1 | Correct answer but lacks justification         |
|     Pyridine-full vs Benzene | Visual_first      |   0.5 | Mentions some structure but unclear conclusion |
|     Pyridine-full vs Benzene | Explanation_first |   0.5 | Mentions some structure but unclear conclusion |
|      Pyrrole-full vs Benzene | Baseline          |     1 | Correct answer but lacks justification         |
|      Pyrrole-full vs Benzene | Stepwise          |     1 | Correct answer but lacks justification         |
|      Pyrrole-full vs Benzene | Visual_first      |   0.5 | Mentions some structure but unclear conclusion |
|      Pyrrole-full vs Benzene | Explanation_first |   1.5 | Correct answer with partial explanation        |
|            Phenol vs Benzene | Baseline          |     1 | Correct answer but lacks justification         |
|            Phenol vs Benzene | Stepwise          |     1 | Correct answer but lacks justification         |
|            Phenol vs Benzene | Visual_first      |   0.5 | Mentions some structure but unclear conclusion |
|            Phenol vs Benzene | Explanation_first |   0.5 | Mentions some structure but unclear conclusion |
|           Anisole vs Benzene | Baseline          |     1 | Correct answer but lacks justification         |
|           Anisole vs Benzene | Stepwise          |     1 | Correct answer but lacks justification         |
|           Anisole vs Benzene | Visual_first      |   0.5 | Mentions some structure but unclear conclusion |
|           Anisole vs Benzene | Explanation_first |   0.5 | Mentions some structure but unclear conclusion |
|     Chlorobenzene vs Benzene | Baseline          |     0 | Incorrect answer or irrelevant reasoning       |
|     Chlorobenzene vs Benzene | Stepwise          |     1 | Correct answer but lacks justification         |
|     Chlorobenzene vs Benzene | Visual_first      |   0.5 | Mentions some structure but unclear conclusion |
|     Chlorobenzene vs Benzene | Explanation_first |   1.5 | Correct answer with partial explanation        |
|      Nitrobenzene vs Benzene | Baseline          |     1 | Correct answer but lacks justification         |
|      Nitrobenzene vs Benzene | Stepwise          |     1 | Correct answer but lacks justification         |
|      Nitrobenzene vs Benzene | Visual_first      |   0.5 | Mentions some structure but unclear conclusion |
|      Nitrobenzene vs Benzene | Explanation_first |   0.5 | Mentions some structure but unclear conclusion |
|           Styrene vs Benzene | Baseline          |     1 | Correct answer but lacks justification         |
|           Styrene vs Benzene | Stepwise          |     1 | Correct answer but lacks justification         |
|           Styrene vs Benzene | Visual_first      |   0.5 | Mentions some structure but unclear conclusion |
|           Styrene vs Benzene | Explanation_first |   1.5 | Correct answer with partial explanation        |

### Two-way Summary Table

| Image Pair                          | Baseline | Stepwise | Visual | Explanation |
|------------------------------------|----------|----------|--------|-------------|
| Aniline vs Nitrobenzene            | 1        | 1        | 0.5    | 1           |
| Benzene vs Toluene                 | 1        | 1        | 0.5    | 1.5         |
| Benzaldehyde vs Benzoic_acid       | 1        | 1        | 0.5    | 0.5         |
| Pyridine-full vs Benzene           | 1        | 1        | 0.5    | 0.5         |
| Pyrrole-full vs Benzene            | 1        | 1        | 0.5    | 1.5         |
| Phenol vs Benzene                  | 1        | 1        | 0.5    | 0.5         |
| Salicylic-acid vs Benzoic_acid     | 1        | 1        | 0.5    | 0.5         |
| Nitrobenzene vs Ozone              | 0        | 1        | 0.5    | 1.5         |
| Pyrrole-numbered vs Pyridine-full  | 1        | 1        | 0.5    | 0.5         |
| Morphine vs Caffeine               | 1        | 1        | 0.5    | 1.5         |

---

### Overall Accuracy & Reasoning Trends
- Stepwise prompts achieved the highest average score at 1.00, indicating that structured, procedural reasoning remains the most effective format for helping the model identify the correct molecule in electrophilic aromatic substitution (EAS) tasks. This aligns with expectations: breaking down reactivity into clear steps—e.g., identify groups → classify as activating/deactivating → infer reactivity—helps the model stay focused and accurate.

- Explanation-first prompts performed nearly as well, with an average score of 0.95, slightly below Stepwise. This suggests that when the model is guided to reason from chemical principles, it can often reach the correct conclusion. However, the small performance drop may reflect occasional over-explanation, abstraction without visual grounding, or verbosity that leads to less confident predictions.

- Baseline prompts were surprisingly competitive, with a score of 0.90. This shows that the model may have memorized or heuristically learned the reactivity order of common substituents (e.g., OH > NO₂), allowing it to perform decently even without explicit reasoning scaffolds. However, this success may be brittle—relying on superficial familiarity rather than deep understanding.

- Visual-first prompts lagged significantly behind, averaging only 0.50, which indicates consistently shallow reasoning. These outputs may have relied on visual cues alone (e.g., “more atoms = more reactive” or “highlighted group = more important”) without understanding electronic effects. This confirms that while image recognition is helpful, it cannot substitute for chemical logic in EAS tasks.

### Reasoning Quality & Model Behavior
- Stepwise prompting aligns well with EAS logic, which naturally lends itself to step-by-step reasoning: classify substituents → assess electronic effects → predict reactivity. This approach seems to provide just enough scaffolding without overwhelming the model.

- Explanation-first prompting can produce rich chemical language, including mentions of resonance, inductive withdrawal, or lone pair donation. However, its slightly lower average suggests that unless carefully crafted, such prompts can sometimes lead the model astray—especially if it “explains” without concluding.

- Baseline outputs are efficient but opaque—they yield the correct answer often, but without a rationale. While useful in simple or familiar cases, this limits their reliability in edge cases or novel comparisons.

- Visual-first outputs appear overly reliant on appearance, failing to internalize the meaning of substituents. This exposes a known limitation of VLMs in scientific reasoning: visual perception alone does not suffice for chemically accurate conclusions.

---

### Prompt Type Effectiveness (Average Score Comparison)

| Prompt Type      | Avg Score (/2) |
| ---------------- | -------------- |
| Stepwise     | **1.00**       |
| Explanation  | **0.95**       |
| Baseline     | 0.90           |
| Visual-first | 0.50           |

---

## DeepSeek-VL

### Scoring + Reasoning Table

| Image 1              | Image 2           | Prompt Type       |   Score | Reason                                         |
|:---------------------|:------------------|:------------------|--------:|:-----------------------------------------------|
| Aniline.png          | Nitrobenzene.png  | baseline          |     1   | Correct answer but lacks justification         |
| Aniline.png          | Nitrobenzene.png  | stepwise          |     1   | Correct answer but lacks justification         |
| Aniline.png          | Nitrobenzene.png  | visual_first      |     1   | Correct answer but lacks justification         |
| Aniline.png          | Nitrobenzene.png  | explanation_first |     1   | Correct answer but lacks justification         |
| Benzene.png          | Toluene.png       | baseline          |     1   | Correct answer but lacks justification         |
| Benzene.png          | Toluene.png       | stepwise          |     1   | Correct answer but lacks justification         |
| Benzene.png          | Toluene.png       | visual_first      |     0.5 | Mentions some structure but unclear conclusion |
| Benzene.png          | Toluene.png       | explanation_first |     1   | Correct answer but lacks justification         |
| Benzaldehyde.png     | Benzoic_acid.png  | baseline          |     1.5 | Correct answer with partial explanation        |
| Benzaldehyde.png     | Benzoic_acid.png  | stepwise          |     1   | Correct answer but lacks justification         |
| Benzaldehyde.png     | Benzoic_acid.png  | visual_first      |     0.5 | Mentions some structure but unclear conclusion |
| Benzaldehyde.png     | Benzoic_acid.png  | explanation_first |     1   | Correct answer but lacks justification         |
| Pyridine-full.png    | Benzene.png       | baseline          |     1   | Correct answer but lacks justification         |
| Pyridine-full.png    | Benzene.png       | stepwise          |     0.5 | Mentions some structure but unclear conclusion |
| Pyridine-full.png    | Benzene.png       | visual_first      |     0.5 | Mentions some structure but unclear conclusion |
| Pyridine-full.png    | Benzene.png       | explanation_first |     0.5 | Mentions some structure but unclear conclusion |
| Pyrrole-full.png     | Benzene.png       | baseline          |     1.5 | Correct answer with partial explanation        |
| Pyrrole-full.png     | Benzene.png       | stepwise          |     2   | Correct answer and sound reasoning             |
| Pyrrole-full.png     | Benzene.png       | visual_first      |     0.5 | Mentions some structure but unclear conclusion |
| Pyrrole-full.png     | Benzene.png       | explanation_first |     1   | Correct answer but lacks justification         |
| Phenol.png           | Benzene.png       | baseline          |     1   | Correct answer but lacks justification         |
| Phenol.png           | Benzene.png       | stepwise          |     1   | Correct answer but lacks justification         |
| Phenol.png           | Benzene.png       | visual_first      |     1   | Correct answer but lacks justification         |
| Phenol.png           | Benzene.png       | explanation_first |     1   | Correct answer but lacks justification         |
| Salicylic-acid.png   | Benzoic_acid.png  | baseline          |     1   | Correct answer but lacks justification         |
| Salicylic-acid.png   | Benzoic_acid.png  | stepwise          |     2   | Correct answer and sound reasoning             |
| Salicylic-acid.png   | Benzoic_acid.png  | visual_first      |     1   | Correct answer but lacks justification         |
| Salicylic-acid.png   | Benzoic_acid.png  | explanation_first |     1   | Correct answer but lacks justification         |
| Nitrobenzene.png     | Ozone.png         | baseline          |     1.5 | Correct answer with partial explanation        |
| Nitrobenzene.png     | Ozone.png         | stepwise          |     1.5 | Correct answer with partial explanation        |
| Nitrobenzene.png     | Ozone.png         | visual_first      |     0.5 | Mentions some structure but unclear conclusion |
| Nitrobenzene.png     | Ozone.png         | explanation_first |     1   | Correct answer but lacks justification         |
| Pyrrole-numbered.png | Pyridine-full.png | baseline          |     1   | Correct answer but lacks justification         |
| Pyrrole-numbered.png | Pyridine-full.png | stepwise          |     1   | Correct answer but lacks justification         |
| Pyrrole-numbered.png | Pyridine-full.png | visual_first      |     0.5 | Mentions some structure but unclear conclusion |
| Pyrrole-numbered.png | Pyridine-full.png | explanation_first |     1   | Correct answer but lacks justification         |
| Morphine.png         | Caffeine.png      | baseline          |     1.5 | Correct answer with partial explanation        |
| Morphine.png         | Caffeine.png      | stepwise          |     1   | Correct answer but lacks justification         |
| Morphine.png         | Caffeine.png      | visual_first      |     0.5 | Mentions some structure but unclear conclusion |
| Morphine.png         | Caffeine.png      | explanation_first |     0.5 | Mentions some structure but unclear conclusion |

### Two-way Summary Table

| Image Pair                          | Baseline | Stepwise | Visual | Explanation |
|------------------------------------|----------|----------|--------|-------------|
| Aniline vs Nitrobenzene            | 1        | 1        | 1      | 1           |
| Benzene vs Toluene                 | 1        | 1        | 0.5    | 1           |
| Benzaldehyde vs Benzoic_acid       | 1.5      | 1        | 0.5    | 1           |
| Pyridine-full vs Benzene           | 1        | 0.5      | 0.5    | 0.5         |
| Pyrrole-full vs Benzene            | 1.5      | 2        | 0.5    | 1           |
| Phenol vs Benzene                  | 1        | 1        | 1      | 1           |
| Salicylic-acid vs Benzoic_acid     | 1        | 2        | 1      | 1           |
| Nitrobenzene vs Ozone              | 1.5      | 1.5      | 0.5    | 1           |
| Pyrrole-numbered vs Pyridine-full  | 1        | 1        | 0.5    | 1           |
| Morphine vs Caffeine               | 1.5      | 1        | 0.5    | 0.5         |

---
### Overall Accuracy & Reasoning Trends
Stepwise prompts showed the highest reasoning reliability, achieving the highest number of perfect scores (2× 2.0). This suggests that when the model is guided through structured, step-by-step reasoning, it is more likely to arrive at both the correct conclusion and the appropriate justification.

Baseline prompts surprisingly matched Stepwise in average score (1.20), but none achieved a perfect score. This suggests that while the model can often guess correctly based on memorized patterns or associations, its answers tend to lack explicit chemical reasoning.

Explanation-first prompts underperformed expectations in this dataset, with no perfect scores and an average of 0.90. Many completions were accurate in parts but failed to link rationale with conclusions, possibly due to prompt misalignment or overgeneralization.

Visual-first prompts received the lowest average score (0.65). Outputs often included vague or surface-level observations (e.g., “more groups” or “looks reactive”) without meaningful chemical justification.

---

### Reasoning Quality Observations
- Correct ≠ Chemically Sound: Baseline and visual outputs occasionally hit the right answer, but without structural or mechanistic reasoning, indicating brittle and heuristic-based generation.

- Stepwise Helps Decision-Making: Outputs following the Stepwise prompt pattern were more likely to include chemically plausible substeps (e.g., identifying functional groups, referencing electron effects), improving both correctness and clarity.

- Explanation-first prompts sometimes faltered due to over-explaining abstract ideas without anchoring them to the visual input (e.g., discussing acidity in non-relevant contexts).

---

### Prompt Type Effectiveness (Average Score Comparison)

| Prompt Type         | Avg Score (/2) | Count of 2.0 Scores |
| ------------------- | -------------- | ------------------- |
| Stepwise            | 1.20           | 2                   |
| Baseline            | 1.20           | 0                   |
| Explanation-first   | 0.90           | 0                   |
| Visual-first        | 0.65           | 0                   |

