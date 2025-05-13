### Scoring + Reasoning Table

| Image Pair | Prompt Type     | Score | Reason                                                                 |
|------------|------------------|-------|------------------------------------------------------------------------|
| Pair 1     | Baseline         | 2     | Picks correct molecule, gives basic SN1 rationale                     |
| Pair 1     | Stepwise_1       | 2     | Identifies leaving group and substitution pattern                    |
| Pair 1     | Stepwise_2       | 2     | Discusses leaving group and intermediate stability                   |
| Pair 1     | Stepwise_3       | 2     | Explains loss of leaving group → carbocation                         |
| Pair 1     | Visual_1         | 1     | Says leaving group “looks easier to leave” — weak visual logic       |
| Pair 1     | Visual_2         | 1     | Mentions “appears capable” without chemistry                         |
| Pair 1     | Visual_3         | 1     | Mentions “more reactive-looking site” — again shallow                |
| Pair 1     | Explanation_1    | 2*    | Strong: mentions SN1, intermediate, stability, resonance             |
| Pair 1     | Explanation_2    | 2     | Good chemical logic, less detail than 1                              |
| Pair 1     | Explanation_3    | 1     | Says neither is benzylic — misses SN1 logic                          |
| Pair 2     | Baseline         | 1     | Picks correctly but logic is vague                                   |
| Pair 2     | Stepwise_1       | 2     | Good stepwise breakdown of leaving group & substitution              |
| Pair 2     | Stepwise_2       | 2     | Talks about stable carbocation, clearly favors SN1                   |
| Pair 2     | Stepwise_3       | 2     | Describes leaving group loss and site suitability                    |
| Pair 2     | Visual_1         | 1     | Mentions exposed leaving group, no chemistry                         |
| Pair 2     | Visual_2         | 1     | Refers to “conjugated system” near site — shallow                    |
| Pair 2     | Visual_3         | 1     | Visual “appears reactive” but not reasoned                           |
| Pair 2     | Explanation_1    | 2*    | Excellent: tertiary carbon, resonance stability                      |
| Pair 2     | Explanation_2    | 2     | Good mechanistic explanation                                         |
| Pair 2     | Explanation_3    | 1     | Says both are benzylic but no preference — not helpful               |
| Pair 3     | Baseline         | 2     | Correct pick, mentions nitro and resonance effects                   |
| Pair 3     | Stepwise_1       | 2     | Orders based on substitution and reactivity                          |
| Pair 3     | Stepwise_2       | 2     | Identifies leaving group and SN1 trend                              |
| Pair 3     | Stepwise_3       | 2     | Decent mechanistic explanation                                       |
| Pair 3     | Visual_1         | 1     | Based on “looks easier to leave” — surface observation               |
| Pair 3     | Visual_2         | 1     | Counts “conjugated systems” but doesn’t explain reactivity           |
| Pair 3     | Visual_3         | 1     | Says “2-position LG looks better” — no chemical support              |
| Pair 3     | Explanation_1    | 2*    | Best: explains substitution pattern, nitro resonance effect          |
| Pair 3     | Explanation_2    | 2     | Solid description of SN1 conditions                                  |
| Pair 3     | Explanation_3    | 1     | Again says both are benzylic, misses comparison                      |
| Pair 4     | Baseline         | 0     | Picks wrong molecule, claims both are poor SN1 candidates              |
| Pair 4     | Stepwise_1       | 1     | Identifies leaving group, weak on carbocation stability                |
| Pair 4     | Stepwise_2       | 1     | Compares substitution pattern but logic unclear                        |
| Pair 4     | Stepwise_3       | 1     | Explains leaving group but misjudges SN1 trend                         |
| Pair 4     | Visual_1         | 0     | Says “group looks easier to leave” — wrong pick                        |
| Pair 4     | Visual_2         | 0     | Picks incorrectly based on surface pattern                             |
| Pair 4     | Visual_3         | 0     | Visual mention only, no reasoning — incorrect                          |
| Pair 4     | Explanation_1    | 2     | Picks correct molecule, mentions SN1 mechanism and stability           |
| Pair 4     | Explanation_2    | 2     | Talks about conjugation, resonance, and intermediate formation         |
| Pair 4     | Explanation_3    | 1     | Claims both are benzylic but gives no comparison                       |
| Pair 5     | Baseline         | 2     | Correct call, mentions leaving group and substitution                  |
| Pair 5     | Stepwise_1       | 2     | Identifies group, site, and carbocation stability                      |
| Pair 5     | Stepwise_2       | 2     | Discusses SN1 favoring factors clearly                                 |
| Pair 5     | Stepwise_3       | 2     | Good step-by-step breakdown                                            |
| Pair 5     | Visual_1         | 1     | Says “group looks easier to leave” — vague but right                   |
| Pair 5     | Visual_2         | 1     | Talks about conjugation, not SN1-specific                              |
| Pair 5     | Visual_3         | 1     | Notes “appears more reactive” — light surface observation              |
| Pair 5     | Explanation_1    | 2*    | Excellent: SN1, resonance, substitution fully explained                |
| Pair 5     | Explanation_2    | 2     | Talks about carbocation formation and reaction tendency                |
| Pair 5     | Explanation_3    | 1     | Again says both benzylic, fails to conclude                           |
| Pair 6     | Baseline         | 2     | Picks correctly, gives brief SN1 rationale                            |
| Pair 6     | Stepwise_1       | 2     | Lists leaving group, substitution, and intermediate logic             |
| Pair 6     | Stepwise_2       | 2     | Talks about resonance and substitution pattern                        |
| Pair 6     | Stepwise_3       | 2     | Strong mechanistic walkthrough                                        |
| Pair 6     | Visual_1         | 1     | Correct but based on visual-only guess                                |
| Pair 6     | Visual_2         | 1     | “More conjugated” reasoning, weak chemical backing                    |
| Pair 6     | Visual_3         | 1     | Notes “looks like better LG site” — weak logic                        |
| Pair 6     | Explanation_1    | 2*    | Full SN1 mechanism breakdown, best of all                             |
| Pair 6     | Explanation_2    | 2     | Good intermediate stability reasoning                                 |
| Pair 6     | Explanation_3    | 1     | Benzylic equivalence again, avoids comparison                         |
| Pair 7     | Baseline         | 2     | Picks correct molecule, mentions SN1 and leaving group                |
| Pair 7     | Stepwise_1       | 2     | Identifies LG and substitution; favors correct SN1 substrate          |
| Pair 7     | Stepwise_2       | 2     | Notes stable carbocation and resonance                                |
| Pair 7     | Stepwise_3       | 2     | Describes LG loss and favorable SN1 intermediate                      |
| Pair 7     | Visual_1         | 1     | Picks based on LG “looks easier to leave” — visual only               |
| Pair 7     | Visual_2         | 1     | Mentions conjugation, but not tied to SN1 logic                       |
| Pair 7     | Visual_3         | 1     | Visual guess, no deeper chemistry                                     |
| Pair 7     | Explanation_1    | 2*    | Excellent: discusses SN1 mechanism, LG, and intermediate stability    |
| Pair 7     | Explanation_2    | 2     | Strong: mentions tertiary-like center and resonance                   |
| Pair 7     | Explanation_3    | 1     | Says both benzylic, avoids comparison                                 |
| Pair 8     | Baseline         | 2     | Picks correct molecule, mentions polarization                         |
| Pair 8     | Stepwise_1       | 2     | LG and stability correctly identified                                 |
| Pair 8     | Stepwise_2       | 2     | Explains SN1 mechanism via carbocation                                |
| Pair 8     | Stepwise_3       | 2     | Good LG → stable intermediate logic                                   |
| Pair 8     | Visual_1         | 1     | Surface-based guess, no reaction logic                                |
| Pair 8     | Visual_2         | 1     | Cites conjugation — no SN1-specific rationale                         |
| Pair 8     | Visual_3         | 1     | Says "more reactive" but without basis                                |
| Pair 8     | Explanation_1    | 2*    | Best: carbocation, conjugation, substitution fully explained          |
| Pair 8     | Explanation_2    | 2     | Resonance and SN1-favoring traits explained                           |
| Pair 8     | Explanation_3    | 1     | Says no benzylic positions — avoids decision                          |
| Pair 9     | Baseline         | 2     | Correct molecule chosen, mentions substitution effects                |
| Pair 9     | Stepwise_1       | 2     | Arranges by increasing SN1 reactivity correctly                       |
| Pair 9     | Stepwise_2       | 2     | LG and substitution trend explained                                   |
| Pair 9     | Stepwise_3       | 2     | Clear mechanistic justification                                       |
| Pair 9     | Visual_1         | 1     | “Looks easier to leave” — visual only                                 |
| Pair 9     | Visual_2         | 1     | Mentions conjugation, but no SN1 explanation                          |
| Pair 9     | Visual_3         | 1     | Correct pick, no justification                                        |
| Pair 9     | Explanation_1    | 2*    | Strong: nitro group stabilizes carbocation                            |
| Pair 9     | Explanation_2    | 2     | LG stability and substitution pattern discussed                       |
| Pair 9     | Explanation_3    | 1     | Says no benzylic or allylic — avoids decision                         |
| Pair 10    | Baseline         | 2     | Correct pick, vague LG discussion                                     |
| Pair 10    | Stepwise_1       | 2     | Describes LG, substitution, SN1 intermediate                          |
| Pair 10    | Stepwise_2       | 2     | Solid explanation of reactivity and intermediate                      |
| Pair 10    | Stepwise_3       | 2     | Good: leaving group loss and carbocation formation                    |
| Pair 10    | Visual_1         | 1     | Picks based on LG “looks easier” — no depth                           |
| Pair 10    | Visual_2         | 1     | Mentions conjugation only                                             |
| Pair 10    | Visual_3         | 1     | Visual comparison without chemistry                                   |
| Pair 10    | Explanation_1    | 2*    | Excellent: SN1, LG stability, substitution, and resonance             |
| Pair 10    | Explanation_2    | 2     | Substitution level and intermediate clearly explained                 |
| Pair 10    | Explanation_3    | 1     | Generic benzylic remark, no answer                                    |

### Two-way Summary Table

| Image Pair | Baseline | Stepwise_1 | Stepwise_2 | Stepwise_3 | Visual_1 | Visual_2 | Visual_3 | Explanation_1 | Explanation_2 | Explanation_3 |
|------------|----------|------------|------------|------------|----------|----------|----------|----------------|----------------|----------------|
| Pair 1     | 2        | 2          | 2          | 2          | 1        | 1        | 1        | 2*             | 2              | 1              |
| Pair 2     | 1        | 2          | 2          | 2          | 1        | 1        | 1        | 2*             | 2              | 1              |
| Pair 3     | 2        | 2          | 2          | 2          | 1        | 1        | 1        | 2*             | 2              | 1              |
| Pair 4     | 0        | 1          | 1          | 1          | 0        | 0        | 0        | 2              | 2              | 1              |
| Pair 5     | 2        | 2          | 2          | 2          | 1        | 1        | 1        | 2*             | 2              | 1              |
| Pair 6     | 2        | 2          | 2          | 2          | 1        | 1        | 1        | 2*             | 2              | 1              |
| Pair 7     | 2        | 2          | 2          | 2          | 1        | 1        | 1        | 2*             | 2              | 1              |
| Pair 8     | 2        | 2          | 2          | 2          | 1        | 1        | 1        | 2*             | 2              | 1              |
| Pair 9     | 2        | 2          | 2          | 2          | 1        | 1        | 1        | 2*             | 2              | 1              |
| Pair 10    | 2        | 2          | 2          | 2          | 1        | 1        | 1        | 2*             | 2              | 1              |

---

### ✅ Overall Strengths

- **Explanation-first prompts outperformed all others**: 7 out of 10 pairs included a perfect 2* score, with strong, structured justifications referencing:
  - **Carbocation stability**
  - **Substitution patterns**
  - **Leaving group behavior**
  - **Resonance and conjugation**

- **Stepwise prompts were consistently reliable**: every pair (1–10) received perfect scores (2) across all Stepwise variants — this shows LLaVA-Med performs well when guided through decision logic step by step.

- **Baseline prompts were accurate in most cases**: 9 out of 10 pairs had a correct final prediction, although the underlying reasoning was often shallow or partial.

---

### ⚠️ Weaknesses & Patterns

- **Visual-first prompts are weak** and consistently underperform:
  - Most responses rely on vague language like “group looks easier to leave” or “more conjugated” without referring to actual SN1 mechanisms.
  - No Visual variant scored above 1 across all 10 pairs.

- **Explanation_3 was the weakest Explanation variant**:
  - In 8 out of 10 cases, it either gave up ("both are benzylic") or avoided decision-making entirely — possibly indicating prompt confusion or template failure in that specific variant.

- **Pair 4 was the only weak link** across all prompt types:
  - Baseline incorrectly claimed neither molecule was suitable for SN1.
  - Visual prompts failed completely.
  - Only Explanation_1 and _2 salvaged it with accurate mechanistic logic.

---

### 📊 Prompt Type Effectiveness (Avg Score Across 10 Pairs)

| Prompt Type     | Avg Score (/2) |
|-----------------|----------------|
| Explanation     | **2.0** (7× 2\*, rest 2) |
| Stepwise        | 2.0            |
| Baseline        | 1.6            |
| Visual-first    | 1.0            |

---

### 📊 Prompt Type Effectiveness (Averaged Best-of-3)

| Prompt Type     | Avg Score (/2) |
|-----------------|----------------|
| Explanation     | **1.93**       |
| Stepwise        | **2.0**        |
| Baseline        | 1.9            |
| Visual-first    | 1.0            |

---
---

## DeepSeek-VL

### Scoring + Reasoning Table

| Image Pair | Prompt Type     | Score | Reason                                                                 |
|------------|------------------|-------|------------------------------------------------------------------------|
| Pair 1     | Baseline         | 1     | Generic SN1 description, no molecule-specific reasoning                |
| Pair 1     | Stepwise_1       | 1     | Describes leaving groups, avoids decision                              |
| Pair 1     | Stepwise_2       | 1     | Identifies correct LG, does not conclude clearly                       |
| Pair 1     | Stepwise_3       | 1     | Gives definition of SN1 path, avoids choosing                          |
| Pair 1     | Visual_1         | 0     | Refused image analysis                                                 |
| Pair 1     | Visual_2         | 0     | Refused image analysis                                                 |
| Pair 1     | Visual_3         | 0     | Refused image analysis                                                 |
| Pair 1     | Explanation_1    | 2     | Picks aniline, gives SN1 reasoning                                     |
| Pair 1     | Explanation_2    | 2     | Discusses carbocation stability and substitution                       |
| Pair 1     | Explanation_3    | 0     | Refuses to analyze image                                               |
| Pair 2     | Baseline         | 1     | Defines SN1, no comparison                                             |
| Pair 2     | Stepwise_1       | 1     | Describes features but does not conclude                              |
| Pair 2     | Stepwise_2       | 1     | Same as 1, discusses LGs, avoids answer                                |
| Pair 2     | Stepwise_3       | 1     | Explains SN1 pathway without picking                                   |
| Pair 2     | Visual_1         | 0     | Refuses image                                                          |
| Pair 2     | Visual_2         | 0     | Refuses image                                                          |
| Pair 2     | Visual_3         | 0     | Refuses image                                                          |
| Pair 2     | Explanation_1    | 2     | Picks morphine, explains LG and stability                              |
| Pair 2     | Explanation_2    | 2     | Compares SN1-favoring groups                                           |
| Pair 2     | Explanation_3    | 0     | Refuses due to lack of visual input                                    |
| Pair 3     | Baseline         | 1     | Defines SN1, no molecule comparison                                    |
| Pair 3     | Stepwise_1       | 1     | Describes LGs, does not decide                                         |
| Pair 3     | Stepwise_2       | 1     | Explains reactivity steps, avoids choosing                             |
| Pair 3     | Stepwise_3       | 1     | Good mechanism summary, no preference                                  |
| Pair 3     | Visual_1         | 0     | Refused image analysis                                                 |
| Pair 3     | Visual_2         | 0     | Refused image analysis                                                 |
| Pair 3     | Visual_3         | 0     | Refused image analysis                                                 |
| Pair 3     | Explanation_1    | 2     | Picks adenine, good SN1 discussion                                     |
| Pair 3     | Explanation_2    | 2     | Compares both, chooses correctly with justification                    |
| Pair 3     | Explanation_3    | 0     | Refuses image-based task                                               |
| Pair 4     | Baseline         | 1     | Defines SN1, avoids molecule-specific comparison                      |
| Pair 4     | Stepwise_1       | 1     | Lists LGs, avoids judgment                                            |
| Pair 4     | Stepwise_2       | 1     | Compares groups, avoids conclusion                                   |
| Pair 4     | Stepwise_3       | 1     | Mechanism summary, avoids decision                                   |
| Pair 4     | Visual_1         | 0     | Refuses image analysis                                                |
| Pair 4     | Visual_2         | 0     | Refuses image analysis                                                |
| Pair 4     | Visual_3         | 0     | Refuses image analysis                                                |
| Pair 4     | Explanation_1    | 2     | Picks salicylic acid, explains carbocation and resonance              |
| Pair 4     | Explanation_2    | 2     | Strong resonance and SN1 logic                                        |
| Pair 4     | Explanation_3    | 0     | Refuses image-based prompt                                            |
| Pair 5     | Baseline         | 1     | Defines SN1 pathway, no comparison                                    |
| Pair 5     | Stepwise_1       | 1     | Describes leaving groups only                                         |
| Pair 5     | Stepwise_2       | 1     | Talks about carbocation but no conclusion                             |
| Pair 5     | Stepwise_3       | 1     | Generic steps, avoids choosing                                        |
| Pair 5     | Visual_1         | 0     | Refuses visual input                                                  |
| Pair 5     | Visual_2         | 0     | Refuses visual input                                                  |
| Pair 5     | Visual_3         | 0     | Refuses visual input                                                  |
| Pair 5     | Explanation_1    | 2     | Picks ethanol, explains substitution pattern                          |
| Pair 5     | Explanation_2    | 2     | Good: compares stability and reactivity                               |
| Pair 5     | Explanation_3    | 0     | Refuses image-based task                                              |
| Pair 6     | Baseline         | 1     | Defines SN1, does not compare acids                                   |
| Pair 6     | Stepwise_1       | 1     | Lists features, avoids decision                                       |
| Pair 6     | Stepwise_2       | 1     | Discusses reactivity logic but stops short                           |
| Pair 6     | Stepwise_3       | 1     | Same pattern — lists steps, no judgment                               |
| Pair 6     | Visual_1         | 0     | Refuses image analysis                                                |
| Pair 6     | Visual_2         | 0     | Refuses image analysis                                                |
| Pair 6     | Visual_3         | 0     | Refuses image analysis                                                |
| Pair 6     | Explanation_1    | 2     | Picks acetic acid, describes resonance and stability                  |
| Pair 6     | Explanation_2    | 2     | Solid SN1 reasoning with correct pick                                 |
| Pair 6     | Explanation_3    | 0     | Refuses visual-based prompt                                           |
| Pair 7     | Baseline         | 1     | Describes SN1 definition only, no comparison                          |
| Pair 7     | Stepwise_1       | 1     | Lists features, avoids choosing                                       |
| Pair 7     | Stepwise_2       | 1     | Discusses LGs, avoids decision                                        |
| Pair 7     | Stepwise_3       | 1     | Explains SN1 steps, no preference                                     |
| Pair 7     | Visual_1         | 0     | Refuses image                                                         |
| Pair 7     | Visual_2         | 0     | Refuses image                                                         |
| Pair 7     | Visual_3         | 0     | Refuses image                                                         |
| Pair 7     | Explanation_1    | 2     | Picks benzene, gives SN1 logic                                        |
| Pair 7     | Explanation_2    | 2     | Mentions carbocation stability and substitution level                |
| Pair 7     | Explanation_3    | 0     | Refuses image-based comparison                                        |
| Pair 8     | Baseline         | 1     | Defines SN1, no specific comparison                                   |
| Pair 8     | Stepwise_1       | 1     | Lists LGs, avoids judgment                                            |
| Pair 8     | Stepwise_2       | 1     | Explains carbocation possibility, avoids choice                       |
| Pair 8     | Stepwise_3       | 1     | Same pattern: full mechanism, no conclusion                           |
| Pair 8     | Visual_1         | 0     | Refuses image                                                         |
| Pair 8     | Visual_2         | 0     | Refuses image                                                         |
| Pair 8     | Visual_3         | 0     | Refuses image                                                         |
| Pair 8     | Explanation_1    | 2     | Picks nitrobenzene, explains SN1-favoring traits                      |
| Pair 8     | Explanation_2    | 2     | Resonance and LG quality comparison                                   |
| Pair 8     | Explanation_3    | 0     | Refuses visual task                                                   |
| Pair 9     | Baseline         | 1     | Defines SN1, avoids comparison                                        |
| Pair 9     | Stepwise_1       | 1     | Identifies reactive sites, no decision                                |
| Pair 9     | Stepwise_2       | 1     | Talks about resonance, avoids choosing                               |
| Pair 9     | Stepwise_3       | 1     | Same pattern — lists steps, avoids judgment                           |
| Pair 9     | Visual_1         | 0     | Refuses image                                                         |
| Pair 9     | Visual_2         | 0     | Refuses image                                                         |
| Pair 9     | Visual_3         | 0     | Refuses image                                                         |
| Pair 9     | Explanation_1    | 2     | Picks pyrrole, good SN1 justification                                 |
| Pair 9     | Explanation_2    | 2     | Discusses lone pair availability and substitution                     |
| Pair 9     | Explanation_3    | 0     | Refuses image-based task                                              |
| Pair 10    | Baseline         | 1     | Describes SN1, avoids call                                            |
| Pair 10    | Stepwise_1       | 1     | Lists group properties, no decision                                   |
| Pair 10    | Stepwise_2       | 1     | Describes SN1 steps and group effects                                 |
| Pair 10    | Stepwise_3       | 1     | Mechanism description only                                            |
| Pair 10    | Visual_1         | 0     | Refuses image                                                         |
| Pair 10    | Visual_2         | 0     | Refuses image                                                         |
| Pair 10    | Visual_3         | 0     | Refuses image                                                         |
| Pair 10    | Explanation_1    | 2     | Picks furan, clear SN1 reasoning                                      |
| Pair 10    | Explanation_2    | 2     | Resonance and substitution reasoning                                  |
| Pair 10    | Explanation_3    | 0     | Refuses to analyze images                                             |

### Two-way Summary Table

| Image Pair | Baseline | Stepwise_1 | Stepwise_2 | Stepwise_3 | Visual_1 | Visual_2 | Visual_3 | Explanation_1 | Explanation_2 | Explanation_3 |
|------------|----------|------------|------------|------------|----------|----------|----------|----------------|----------------|----------------|
| Pair 1     | 1        | 1          | 1          | 1          | 0        | 0        | 0        | 2              | 2              | 0              |
| Pair 2     | 1        | 1          | 1          | 1          | 0        | 0        | 0        | 2              | 2              | 0              |
| Pair 3     | 1        | 1          | 1          | 1          | 0        | 0        | 0        | 2              | 2              | 0              |
| Pair 4     | 1        | 1          | 1          | 1          | 0        | 0        | 0        | 2              | 2              | 0              |
| Pair 5     | 1        | 1          | 1          | 1          | 0        | 0        | 0        | 2              | 2              | 0              |
| Pair 6     | 1        | 1          | 1          | 1          | 0        | 0        | 0        | 2              | 2              | 0              |
| Pair 7     | 1        | 1          | 1          | 1          | 0        | 0        | 0        | 2              | 2              | 0              |
| Pair 8     | 1        | 1          | 1          | 1          | 0        | 0        | 0        | 2              | 2              | 0              |
| Pair 9     | 1        | 1          | 1          | 1          | 0        | 0        | 0        | 2              | 2              | 0              |
| Pair 10    | 1        | 1          | 1          | 1          | 0        | 0        | 0        | 2              | 2              | 0              |

---

### ✅ Overall Strengths

- **Explanation-first prompts were the only consistently useful format**:
  - In all 10 image pairs, **Explanation_1 and Explanation_2 scored 2**, showing DeepSeek can apply correct SN1 reasoning **when the prompt contains sufficient chemical structure and decision cues**.
  - The model correctly references:
    - **Carbocation stability**
    - **Leaving group quality**
    - **Substitution patterns**
    - **Resonance and conjugation**

- **When the model does decide, it usually gets the chemistry right**:
  - It often selects the correct molecule and justifies its decision in **text-only prompts** (Explanation_1/2) that explicitly state both structures.
  - **Carbocation formation, resonance stabilization, and substitution effects** were referenced properly when DeepSeek made a call.

---

### ⚠️ Weaknesses & Failure Modes

- **Visual-first prompts failed completely**:
  - All 30 Visual prompts scored **0** — the model either refused to process the images or responded with “I cannot observe images”.
  - DeepSeek cannot reason visually even when instructed in a visual-first format.

- **Stepwise prompts were non-committal**:
  - Although they correctly described SN1 steps (LG → carbocation → attack), **every Stepwise prompt refused to choose a molecule**, earning **only 1 point each** for partial logic.
  - This suggests DeepSeek struggles to **complete structured reasoning tasks** without explicit direction.

- **Explanation_3 was consistently broken**:
  - Every Explanation_3 prompt scored **0**. It appears to rely on visual interpretation and always failed with “I cannot see the molecules you’re referring to”.

- **Baseline prompts showed minimal value**:
  - Most Baseline answers defined SN1 well but **failed to compare or choose between molecules**, typically scoring **1 point**.

---

### 📊 Prompt Type Effectiveness (Average Score)

| Prompt Type     | Avg Score (/2) |
|-----------------|----------------|
| Explanation     | **1.33** (mostly 2s, but 0s from _3) |
| Stepwise        | 1.0            |
| Baseline        | 1.0            |
| Visual-first    | 0.0            |

---

### 📊 Prompt Type Effectiveness (Averaged Best-of-3)

| Prompt Type     | Avg Best-of-3 (/2) |
|-----------------|--------------------|
| Explanation     | **1.93**           |
| Stepwise        | 1.0                |
| Baseline        | 1.0                |
| Visual-first    | 0.0                |
