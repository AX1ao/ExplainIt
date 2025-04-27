# Full Text Analysis of Model's Task 0: Molecule Identification

## Overview

This evaluation focused on the model's ability to **identify molecules** purely from images, across **four prompt types**:
- Baseline
- Stepwise
- Visual-first
- Explanation-first

Each of the 19 molecules was tested under these prompts. The results were scored as:
- ✅ Correct
- ⚠️ Partially Correct
- ❌ Incorrect

## General Observations

- **Success Rate**:  
  Only a few molecules were correctly identified across all prompts.  
  Many outputs showed **partial understanding** but struggled with precision.

- **Prompt Type Trends**:  
  - **Baseline**: Frequently vague or incorrect. Lacked depth.  
  - **Stepwise**: Helped break down visual elements, but still prone to wrong conclusions.  
  - **Visual-first**: Sometimes improved bond/ring recognition, but chemical identification was often shallow.  
  - **Explanation-first**: Surprisingly weak; explanations often went off-track into chemistry facts without tying them back to the image.

- **Common Failure Modes**:
  - **Confusing structures** (e.g., benzene vs. cyclohexane, furan vs. pentagon)
  - **Overcomplicating simple molecules** (e.g., butane described as a polymer chain)
  - **Mislabeling functional groups** (e.g., hydroxyl groups missed or wrongly identified)
  - **Confusing similar molecules** (e.g., cholesterol vs cortisol)

- **Best Performing Images**:
  - **1,3-dimethylbenzene**: Clear benzene recognition in some prompts
  - **Carbon-dioxide**: Easy double-bond structure was correctly noted
  - **Alkohol_benzylowy**: Some prompts caught benzyl alcohol features

- **Worst Performing Images**:
  - **Guainin.png**: Total misidentification across prompts
  - **Hydrogen-chloride.png**: Incorrect (thought it was CO, NH₄⁺, etc.)
  - **Butane_simple.png**: Simple zigzag misread as random lines

---

## Detailed Insights by Category

### 1. Correct Identifications (✅)

These were usually achieved when:
- The molecule was simple (CO₂, benzene rings).
- Visual patterns like rings or double bonds were obvious.
- The prompt structure helped focus attention on key visual clues.

Notably, **Visual-first** sometimes helped with ring systems.

### 2. Partial Identifications (⚠️)

Most partial outputs showed:
- Correct recognition of **general shape** (e.g., "six-membered ring" or "hexagon")  
- Incorrect assignment of **functional groups** or **bond types**  
- Vague general chemistry descriptions without matching the molecule precisely.

Stepwise prompts helped models *start* better, but final identification was still weak.

### 3. Incorrect Identifications (❌)

Frequent mistakes included:
- **Overinterpreting** simple molecules as complex ones.
- **Mixing molecule types**: calling an alkane a phenol, or a cyclic molecule an amine.
- **Describing visual features but not identifying the molecule**.
- **Confusing carbon, oxygen, and nitrogen counts**.

Baseline prompts and Explanation-first prompts both heavily contributed to wrong answers.

---

## Prompt Type Performance Summary

| Prompt Type      | Strengths | Weaknesses |
|------------------|-----------|------------|
| **Baseline**     | Sometimes catches obvious features | Frequently shallow and vague |
| **Stepwise**     | Good at listing features step-by-step | Tends to miss final correct ID |
| **Visual-first** | Better at describing shapes, rings | Still weak at chemical specificity |
| **Explanation-first** | Richer chemistry language | Prone to hallucinating wrong structures |

---

## Final Reflection

Task 0 ("Identify the molecule") exposed a major gap between **visual pattern recognition** and **chemical understanding**.

The model often **sees shapes** (like rings, chains, bonds) but **fails to map them to molecule names correctly**.  
Chemical-specific prompts and guidance are still necessary to bridge this gap.

This highlights that in **scientific domains**, surface-level CoT prompting is not enough — models need much **deeper domain grounding**.

---

# 📈 Next Steps

- Design better prompts with stronger chemical grounding.
- Possibly add molecule vocabulary examples during priming.
- Experiment with giving models multiple-choice options for identification.
- Evaluate if model finetuning on molecule datasets would improve performance.

