# Prior Work Analysis Report

## Target Paper

**Title:** Negative Label Guided OOD Detection with Pretrained Vision-Language Models

**Conference:** ICLR 2024 (spotlight)

**Authors:** Xue Jiang, Feng Liu, Zhen Fang, Hong Chen, Tongliang Liu, Feng Zheng, Bo Han

**Keywords:** OOD detection

**Abstract:** 
> Out-of-distribution (OOD) detection aims at identifying samples from unknown classes, playing a crucial role in trustworthy models against errors on unexpected inputs.  
Extensive research has been dedicated to exploring OOD detection in the vision modality. 
{Vision-language models (VLMs) can leverage both textual and visual information for various multi-modal applications, whereas few OOD detection methods take into account information from the text modality. 
In this paper, we propose a novel...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Learning Transferable Visual Models From Natural Language Supervision** (2021)
- *Authors:* Alec Radford et al.
- *Direct Connection:* NegLabel relies on CLIP’s zero-shot image–text similarity formulation to compute confidence over textual labels, enabling its post hoc OOD scoring with large pools of negative labels.

### 💡 Inspiration

**Learning from Complementary Labels** (2017)
- *Authors:* Takeshi Ishida et al.
- *Direct Connection:* NegLabel is inspired by the complementary-label paradigm—using labels that indicate what a sample is not—and transfers this idea to VLMs by operationalizing many complementary (negative) text labels to guide OOD scoring.

### 🔍 Gap Identification

**Deep Anomaly Detection with Outlier Exposure** (2019)
- *Authors:* Dan Hendrycks et al.
- *Direct Connection:* NegLabel is motivated by OE’s limitation of requiring auxiliary OOD images and retraining, achieving a similar ‘exposure to negatives’ effect purely through textual negative labels in a post hoc manner.

### 📊 Baseline

**CLIPN: Image-Driven Negative Prompt Learning for Zero-Shot Out-of-Distribution Detection** (2023)
- *Authors:* First author et al.
- *Direct Connection:* NegLabel builds on the idea of negative textual guidance introduced by CLIPN, but replaces learned negative prompts with a large corpus-driven set of negative labels and a new OOD score designed to exploit them without training.

**Zero-Shot Out-of-Distribution Detection via CLIP** (2022)
- *Authors:* First author et al.
- *Direct Connection:* NegLabel targets the same zero-shot VLM-based OOD setting as ZOC and addresses its sensitivity to limited auxiliary label sets by systematically leveraging vast negative label corpora with a tailored OOD score.

### 🔗 Related Problem

**Energy-based Out-of-Distribution Detection** (2020)
- *Authors:* Weitang Liu et al.
- *Direct Connection:* NegLabel extends energy-style scoring by integrating contrast between positive in-distribution labels and a large set of negative labels, theoretically analyzing why this negative-label-informed score separates OOD data.

---

## Synthesis: How Prior Work Led to This Paper

CLIP established a practical zero-shot classification mechanism by aligning images and textual labels in a shared embedding space, making confidence measurable via image–text similarity. Complementary-label learning showed that supervision describing what an instance does not belong to can be made statistically useful, motivating the use of negative label information in decision-making. Energy-based OOD detection highlighted the power of scoring functions that reflect relative logit/energy structure rather than raw softmax, pointing to contrastive, theoretically grounded scores for separating in- and out-of-distribution inputs. Outlier Exposure demonstrated that auxiliary negatives substantially improve OOD detection but at the cost of collecting OOD images and retraining, surfacing the need for a post hoc pathway to “expose” models to negatives. Within the VLM arena, ZOC operationalized zero-shot OOD detection directly on CLIP by leveraging auxiliary label sets, while CLIPN introduced negative textual guidance through learned negative prompts, concretely showing that negatives in the text space can enhance zero-shot OOD detection.
Together, these works suggested a clear opportunity: achieve OE-like benefits without images by using textual negatives; make the negative signal scalable and training-free; and design a score that leverages negative labels in a theoretically justified way. Negatives learned as prompts (CLIPN) and small auxiliary label pools (ZOC) hinted at the mechanism but were limited in scope or required learning. Building on CLIP’s similarity framework, complementary-label insights, and energy-style scoring, the current paper aggregates a vast corpus of negative labels and crafts a new OOD score that contrasts positives against many negatives, delivering a simple post hoc method with strong empirical and theoretical support.

---

*Analysis generated on: 2026-01-06T12:16:38.187632*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
