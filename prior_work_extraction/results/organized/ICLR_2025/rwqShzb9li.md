# Prior Work Analysis Report

## Target Paper

**Title:** Linear Representations of Political Perspective Emerge in Large Language Models

**Conference:** ICLR 2025 (oral)

**Authors:** Junsol Kim, James Evans, Aaron Schein

**Keywords:** large language model, political perspective, ideology, representation learning

**Abstract:** 
> Large language models (LLMs) have demonstrated the ability to generate text that realistically reflects a range of different subjective human perspectives. This paper studies how LLMs are seemingly able to reflect more liberal versus more conservative viewpoints among other political perspectives in American politics. We show that LLMs possess linear representations of political perspectives within activation space, wherein more similar perspectives are represented closer together. To do so, we ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Out of One, Many: Using Language Models to Simulate Human Samples** (2023)
- *Authors:* Lisa P. Argyle et al.
- *Direct Connection:* Their evidence and prompting methodology for eliciting group-specific viewpoints from LMs directly motivated our persona prompts that condition models to write from specific lawmakers’ perspectives to expose ideological signals.

**Congress: A Political-Economic History of Roll Call Voting (DW-NOMINATE)** (1997)
- *Authors:* Keith T. Poole and Howard Rosenthal
- *Direct Connection:* We rely on the DW-NOMINATE ideology scores introduced by this work as the continuous ground-truth targets for supervising and validating our head-wise linear probes.

### 💡 Inspiration

**What Does BERT Look At? An Analysis of BERT’s Attention** (2019)
- *Authors:* Kevin Clark et al.
- *Direct Connection:* By demonstrating specialized attention heads and head-level analysis methods, this paper motivated our search for and identification of specific attention heads whose activations linearly encode political perspective.

**Toy Models of Superposition in Neural Networks** (2022)
- *Authors:* Nelson Elhage et al.
- *Direct Connection:* The superposition and linear feature hypothesis from this work underpins our central claim and test that political perspectives correspond to approximately linear directions in LLM activation space.

### 🔍 Gap Identification

**Whose Opinions Do Language Models Reflect?** (2023)
- *Authors:* Shibani Santurkar et al.
- *Direct Connection:* By showing that LMs’ outputs align with particular population opinions but not explaining the internal mechanism, this work motivates our move from behavioral bias measurement to identifying linear internal representations tied to a validated ideology scale.

### 🔧 Extension

**BERT Rediscovers the Classical NLP Pipeline** (2019)
- *Authors:* Ian Tenney et al.
- *Direct Connection:* This work introduced layerwise linear probing to decode specific properties from transformer activations, which we directly extend by applying head-wise linear probes to predict continuous DW-NOMINATE ideology from LLM activations during persona-conditioned generation.

### 🔗 Related Problem

**Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned** (2019)
- *Authors:* Elena Voita et al.
- *Direct Connection:* Their finding that a sparse subset of mid-layer heads carry key signals directly informed our head-wise probing strategy and interpretation that ideology-predictive heads concentrate in middle layers.

---

## Synthesis: How Prior Work Led to This Paper

Layerwise probing introduced the idea that linear classifiers can decode specific properties from transformer activations, revealing where information emerges across depth (Tenney et al., 2019). Analyses of attention laid the groundwork for head-level interpretability, showing specialized heads and practical techniques to study them (Clark et al., 2019), and further established that a sparse subset of mid-layer heads often carry the most functionally relevant signals (Voita et al., 2019). From a representational perspective, the superposition hypothesis argued that features are linearly embedded and can be recovered by simple decoders even when distributed, motivating linear readouts as a principled test for semantic directions in activation space (Elhage et al., 2022). In parallel, social-science–oriented work demonstrated that prompting language models with demographic or persona cues can elicit distinct group-specific viewpoints (Argyle et al., 2023), while empirical audits showed that model outputs reflect particular populations’ opinions without clarifying the internal basis of those behaviors (Santurkar et al., 2023). Finally, DW-NOMINATE provided a validated, continuous ideology scale to anchor any representation of political perspective (Poole & Rosenthal, 1997). Together, these strands suggested a path: elicit politically informative generations via persona prompts for named lawmakers, record head-level activations, and test for linear structure by predicting DW-NOMINATE scores. Combining head-wise interpretability with linear probing and a behavioral elicitation paradigm allowed a direct bridge from outputs to mechanisms, revealing sparse mid-layer heads whose activations form linear representations organizing political perspective.

---

*Analysis generated on: 2026-01-06T08:20:54.164661*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
