# Prior Work Analysis Report

## Target Paper

**Title:** Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models

**Conference:** ICLR 2025 (oral)

**Authors:** Javier Ferrando, Oscar Balcells Obeso, Senthooran Rajamanoharan, Neel Nanda

**Keywords:** Mechanistic Interpretability, Hallucinations, Language Models

**Abstract:** 
> Hallucinations in large language models are a widespread problem, yet the mechanisms behind whether models will hallucinate are poorly understood, limiting our ability to solve this problem. Using sparse autoencoders as an interpretability tool, we discover that a key part of these mechanisms is entity recognition, where the model detects if an entity is one it can recall facts about. Sparse autoencoders uncover meaningful directions in the representation space, these detect whether the model re...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Transformer Feed-Forward Layers Are Key-Value Memories** (2021)
- *Authors:* Mor Geva et al.
- *Direct Connection:* Established that factual associations about entities are stored in MLP layers as key–value memories, grounding this paper’s hypothesis that an entity-recognition feature gates access to those memories and thus controls hallucination/refusal.

**Toy Models of Superposition in Neural Networks** (2022)
- *Authors:* Nelson Elhage et al.
- *Direct Connection:* Showed that neural features are superposed and that sparse methods can disentangle them, providing the theoretical basis for using sparse autoencoders to isolate an interpretable “entity-knownness” direction.

### 💡 Inspiration

**Language Models (Mostly) Know What They Know** (2022)
- *Authors:* Saurabh Kadavath et al.
- *Direct Connection:* Demonstrated that LMs possess internal signals about their own knowledge and uncertainty, directly motivating this paper’s search for a concrete, mechanistic “knowledge awareness” representation that predicts refusal vs. hallucination.

### 🔧 Extension

**Sparse Feature Circuits: Discovering Interpretable Features in Language Models** (2024)
- *Authors:* Chris Olah et al.
- *Direct Connection:* Demonstrated that SAEs trained on LM activations yield monosemantic features that support causal analysis, directly enabling this paper’s extraction of entity-recognition features and their causal manipulation.

**Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 with Sparse Autoencoders** (2024)
- *Authors:* Will Bricken et al.
- *Direct Connection:* Provided scalable SAE training recipes and evidence of robust, transferable features, which this paper leverages to reliably discover and transfer “knowledge awareness” directions across models.

### 🔗 Related Problem

**Locating and Editing Factual Associations in GPT (ROME)** (2022)
- *Authors:* Kevin Meng et al.
- *Direct Connection:* Introduced causal intervention techniques to locate and manipulate factual knowledge in specific layers, which this paper adapts by steering along discovered SAE feature directions to causally toggle refusal and hallucination.

---

## Synthesis: How Prior Work Led to This Paper

Prior work established three pillars that are directly relevant here. First, research on LM self-knowledge showed that models can internally signal when they know or don’t know answers, revealing usable epistemic information in hidden states. Second, mechanistic studies of factual storage found that feed-forward layers act as key–value memories, where entity representations cue retrieval of attributes; this implies that detecting whether an entity has a retrievable memory should predict answerability. Third, causal editing methods like ROME demonstrated that intervening on specific internal representations can predictably alter factual outputs, validating that targeted activation-level manipulations can control behavior. Complementing these, theoretical and empirical advances on superposition argued that many features are entangled and that sparse approaches can disentangle them, while sparse autoencoder work showed that SAEs trained on LM activations yield monosemantic, causally meaningful features and provided scalable training protocols that make such features robust and transferable. Together, these works suggest that an interpretable, sparse feature could encode whether an entity is “known,” and that causal steering along this feature should modulate answering behavior. The current paper synthesizes these insights by using SAEs to discover entity-recognition directions that reflect self-knowledge, empirically tying them to refusal versus hallucination, and demonstrating causal control—thus providing a mechanistic account and an actionable handle on hallucinations that naturally follows from the prior landscape.

---

*Analysis generated on: 2026-01-06T13:43:11.857386*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
