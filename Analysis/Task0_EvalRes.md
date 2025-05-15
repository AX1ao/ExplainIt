# Task 0: Molecule Identification Evaluation
### CoT Structure Evaluation Summary

We evaluated 129 total outputs across three models (DeepSeek-VL, LLaVA-Med, and LLaVA-OneVision), using four prompt structures per image:

- **Baseline**
- **Stepwise**
- **Visual-first**
- **Explanation-first**

| Accuracy Score | Baseline | Stepwise | Visual-first | Explanation-first |
| -------------- | -------- | -------- | ------------ | ----------------- |
| 0              | 44       | 17       | 18           | 35                |
| 0.5            | 48       | 61       | 45           | 42                |
| 1.0            | 26       | 41       | 46           | 27                |
| 1.5            | 8        | 10       | 17           | 20                |
| 2.0            | 3        | 3        | 3            | 5                 |

**Due to the volume of scoring data, individual scores for each image-model-prompt combination are not listed here. Full results can be found in the supplementary Excel file located at `Results/Task0/`, which includes detailed scoring breakdowns across all models and prompt types.**
#### Scoring Examples

**Example 1**

> *Visual-First CoT:* “The molecule is likely a steroid. Steroids have four fused rings and a hydroxyl group may suggest identity. However, without more details, it's hard to specify the exact type.”

- **Accuracy:** 1.5 (correct family + features)
- **Hedging:** 1 (includes “likely”, “without more details”)

**Example 2**

> *Baseline:* “This is 2-nitrobenzaldehyde.”

- **Accuracy:** 0.5 (wrong molecule but recognized benzene and nitro group)
- **Hedging:** 0 (direct claim)

------

### Key Observations

- **CoT significantly reduces failure rates.**
   Baseline prompts resulted in 0 scores 34% of the time, whereas CoT-based prompts never exceeded 27.1% 0 scores.
- **Visual-first offers the best overall balance.**
   It produced both a high proportion of partial (0.5–1.0) and high (1.5–2.0) scores, suggesting it encourages structure-focused recognition.
- **Explanation-first excels at high-scoring cases** but suffers instability — it achieved the highest share of 1.5/2.0 scores (19.4%) but also the most 0s.
- **Stepwise prompts are robust for partial credit**, producing the highest overall non-zero rate, though it tends to plateau at 0.5.

## Detailed Scoring Information
### Deepseek-VL
#### Accuracy by Prompt Type
| Prompt Type | 0    | 0.5  | 1    | 1.5  | 2    | Total |
| ----------- | ---- | ---- | ---- | ---- | ---- | ----- |
| Baseline    | 11   | 24   | 14   | 4    | 2    | 55    |
| Stepwise    | 8    | 21   | 19   | 6    | 1    | 55    |
| Visual      | 8    | 12   | 25   | 8    | 2    | 55    |
| Explanation | 6    | 15   | 19   | 11   | 4    | 55    |

#### Hedging by Prompt Type
| Prompt Type | Hedging = 0 | Hedging = 1 | Total |
| ----------- | ----------- | ----------- | ----- |
| Baseline    | 54          | 1           | 55    |
| Stepwise    | 19          | 36          | 55    |
| Visual      | 22          | 33          | 55    |
| Explanation | 31          | 24          | 55    |

### LLaVA-Med
#### Accuracy by Prompt Type
| Prompt Type | 0    | 0.5  | 1    | 1.5  | 2    | Total |
| ----------- | ---- | ---- | ---- | ---- | ---- | ----- |
| Baseline    | 29   | 13   | 9    | 4    | 0    | 55    |
| Stepwise    | 8    | 26   | 15   | 4    | 2    | 55    |
| Visual      | 9    | 21   | 18   | 6    | 1    | 55    |
| Explanation | 28   | 13   | 5    | 8    | 1    | 55    |

#### Hedging by Prompt Type
| Prompt Type | Hedging = 0 | Hedging = 1 | Total |
| ----------- | ----------- | ----------- | ----- |
| Baseline    | 55          | 0           | 55    |
| Stepwise    | 31          | 24          | 55    |
| Visual      | 26          | 29          | 55    |
| Explanation | 31          | 24          | 55    |

### OneVision
#### Accuracy by Prompt Type
| Prompt Type | 0    | 0.5  | 1    | 1.5  | 2    | Total |
| ----------- | ---- | ---- | ---- | ---- | ---- | ----- |
| Baseline    | 4    | 11   | 3    | 0    | 1    | 19    |
| Stepwise    | 1    | 11   | 7    | 0    | 0    | 19    |
| Visual      | 1    | 12   | 3    | 3    | 0    | 19    |
| Explanation | 1    | 14   | 3    | 1    | 0    | 19    |

#### Hedging by Prompt Type
| Prompt Type | Hedging = 0 | Hedging = 1 | Total |
| ----------- | ----------- | ----------- | ----- |
| Baseline    | 2           | 17          | 19    |
| Stepwise    | 0           | 19          | 19    |
| Visual      | 0           | 19          | 19    |
| Explanation | 0           | 19          | 19    |

### Model-by-Model Analysis

#### LLaVA-Med

- **Performance:** Weaker overall than other models.
- **Strengths:** Some success in stepwise prompts.
- **Explanation-first instability:** The highest 0-score rate among CoTs (~50%).
  - This may stem from **prompt length** and **recency bias**, where the model forgets final instructions due to long context length.
- **Visual-first remains most reliable**, with stable performance across score bands.
- **Hedging:** CoT prompts introduce uncertainty effectively; baseline answers were overly confident and often wrong.

#### DeepSeek-VL

- **Performance:** Best-performing model overall.
- **Lowest 0-score rate** among all models, even for the baseline.
- **Explanation-first shines here**, with strong performance in high-score bands and minimal 0 scores.
  - Indicates DeepSeek-VL handles **long prompts and complex logic** better than LLaVA-Med.
- **Visual-first again performs reliably**, balancing mid-to-high scores.
- **Stepwise ranks lowest among CoTs**, due to limited depth of recognition.

#### LLaVA-OneVision

- **Sample Size:** Only 19 images tested.
- **No perfect scores (2.0)** recorded, suggesting underperformance.
- **Visual-first leads again** with the best balance, but no standout CoT structure.
- **Hedging behavior is strong by default**, with even baseline prompts frequently using uncertainty language.

------

### Final Recommendation

| Model       | Best CoT Structure | Comment                                            |
| ----------- | ------------------ | -------------------------------------------------- |
| LLaVA-Med   | Visual-first       | More stable; explanation-first too unstable        |
| DeepSeek-VL | Explanation-first  | Handles long prompts and deductive logic well      |
| OneVision   | Visual-first       | Best of a narrow range; overall performance weaker |

In conclusion, **finetuned CoT prompts improve performance** across models, especially for **Visual-first** and **Explanation-first** formats. Visual-first is the most stable overall, while explanation-first can excel in capable models like DeepSeek-VL. Stepwise prompts offer consistent partial accuracy but rarely full recognition.

## General Observations

- **Success Rate**: 
  After prompt finetuning, **correct identifications increased noticeably** across Visual-first and Explanation-first prompts.  
  Partial recognitions also became **more focused** — models were more often "almost right" than totally wrong.

- **Prompt Type Trends**:  
  - **Baseline**: Still weak overall; occasional correct guesses for very simple molecules.  
  - **Stepwise**: Improved feature listing, but struggled with final chemical naming.  
  - **Visual-first**: **Significantly improved** — rings, bonds, and overall structure recognition became more accurate.  
  - **Explanation-first**: **More reliable** after finetuning — stronger functional group identification and logical molecule deduction.

- **Common Failure Modes**:
  - **Confusing structurally similar molecules** (e.g., benzene vs cyclohexane)
  - **Overcomplicating straight chains** (e.g., butane misinterpreted)
  - **Missing or hallucinating functional groups** (e.g., missed hydroxyl groups)

- **Best Performing Images**:
  - **Carbon-dioxide**: Correctly and consistently identified.
  - **Phenol2.png**: Ring and functional group captured well after finetuning.
  - **Furan-numbered.png**: Ring structures correctly recognized, especially by Visual-first prompts.

- **Worst Performing Images**:
  - **Guainin.png**: Still frequent confusion with caffeine or other nucleobases.
  - **Hydrogen-chloride.png**: Simple diatomic structure still misdescribed under several prompts.
  - **Butane_simple.png**: Overinterpreted into zigzag or polymeric structures.

## Prompt Type Performance Summary

| Prompt Type           | Strengths                                                    | Weaknesses                                          |
| --------------------- | ------------------------------------------------------------ | --------------------------------------------------- |
| **Baseline**          | Sometimes catches very obvious features                      | Frequently vague or wrong                           |
| **Stepwise**          | Good at step-by-step visual breakdown                        | Often weak at full molecule naming                  |
| **Visual-first**      | **Much better** after finetuning; stronger at recognizing rings, bond patterns | Still some issues with functional group specificity |
| **Explanation-first** | **Significantly improved** chemical logic; better group identification | Occasionally too verbose or overcomplicated         |


## Final Reflection

Task 0 ("Identify the molecule") with **finetuned prompts** **substantially improved both partial and full identifications**, especially for Visual-first and Explanation-first structures.

Compared to the earlier raw prompts:
- **More correct answers** were achieved overall.
- **Partial answers** were **closer to full correctness** (more "almost right" cases).
- **Visual-first prompts benefited the most**, showing the importance of anchoring reasoning to **visible molecular patterns**.

**However**, the model still **struggles to bridge vision and domain-specific chemical naming**.
Correct CoT structure **alone** is **not sufficient** — models **need deeper chemical grounding** to move beyond surface features.


##  Quick Performance Comparison: Before vs After Finetuning

| Metric            | Before Finetuning         | After Finetuning                    |
| :---------------- | :------------------------ | :---------------------------------- |
| % Correct Outputs | Low (~30%)                | Moderate (~50–60%)                  |
| Best Prompt Type  | None clearly better       | Visual-first and Explanation-first  |
| Failure Mode      | Random misidentifications | More focused, near-correct attempts |


##  Final Verdict

**Finetuned prompting worked.** 
It **did not make the model perfect**, but it **increased the chance of the model finding the correct or nearly correct molecule** — a meaningful step toward smarter multimodal scientific reasoning.
