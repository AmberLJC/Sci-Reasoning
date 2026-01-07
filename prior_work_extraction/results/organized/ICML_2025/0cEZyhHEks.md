# Prior Work Analysis Report

## Target Paper
**Title:** 0cEZyhHEks
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Transformer Feed-Forward Layers Are Key-Value Memories** (2021)
- *Authors:* Mor Geva et al.
- *Connection:* Established the notion that parametric factual knowledge is stored and retrieved via MLP ‘memory’ mechanisms, providing the conceptual groundwork for distinguishing parametric memory from contextual information that JuICE explicitly steers between.

**In-context Learning and Induction Heads** (2022)
- *Authors:* Catherine Olsson et al.
- *Connection:* Identified induction (context) heads and head-level circuit roles in transformers, directly informing the memory-head vs context-head framing that JuICE revisits and refines with its superposition finding.

### 💡 Inspiration

**Toy Models of Superposition in Neural Networks** (2022)
- *Authors:* Nelson Elhage et al.
- *Connection:* Introduced and analyzed superposition as a fundamental representational phenomenon, directly inspiring JuICE’s hypothesis and empirical discovery that influential attention heads can carry both contextual and parametric signals simultaneously.

### 🔍 Gap Identification

**Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned** (2019)
- *Authors:* Elena Voita et al.
- *Connection:* Argued for head specialization and pruning, an assumption of functional exclusivity that the present work challenges by revealing superpositioned heads serving both memory and context roles.

**Locating and Editing Factual Knowledge in GPT** (2022)
- *Authors:* Kevin Meng et al.
- *Connection:* Demonstrated parametric knowledge localization and editing but requires model modification; JuICE addresses this gap by providing a test-time, no-finetuning intervention that selectively favors parametric memory or context.

### 📊 Baseline

**DoLa: Decoding by Contrasting Language Models Improves Factuality** (2023)
- *Authors:* Luo et al.
- *Connection:* Pioneered a dual-run, test-time decoding strategy to improve factuality; JuICE builds on the dual-run idea but targets attention-head-level interventions to resolve memory–context conflicts.

### 🔧 Extension

**Are Sixteen Heads Really Better than One?** (2019)
- *Authors:* Paul Michel et al.
- *Connection:* Showed head importance can be probed via ablation, a technique JuICE extends by identifying a set of reliable heads whose targeted intervention drives the model toward either parametric beliefs or contextual knowledge.

---

## Synthesis

The core of Taming Knowledge Conflicts in Language Models rests on re-examining how transformers balance in-weights (parametric) memory with in-context information and intervening at test time to steer that balance. Foundationally, Geva et al. established that MLP layers function as key–value memories, formalizing the parametric memory side of the dichotomy. Complementing this, Olsson et al. characterized induction (context) heads, grounding the view that specific attention heads propagate contextual evidence. Earlier interpretability work—especially Voita et al.—popularized the assumption of head specialization, often treating heads as single-purpose and pruneable, an assumption the present paper directly challenges. Anthropic’s theory of superposition (Elhage et al.) provided the conceptual lens for polysemantic feature sharing; this paper translates that insight to attention heads, uncovering superposition between contextual and memory signals within the very heads thought to be exclusive. On the intervention front, ROME (Meng et al.) localized and edited parametric knowledge but required model modification, motivating a no-finetuning, test-time approach. DoLa’s dual-run decoding demonstrated the efficacy of contrastive, test-time strategies, which JuICE adapts to the attention mechanism to disambiguate superposed signals. Finally, methods for identifying important heads (Michel et al.) inform JuICE’s selection of reliable heads, enabling principled head-level interventions. Together, these works directly shape JuICE’s key innovation: a dual-run, attention-head-targeted test-time method that resolves memory–context conflicts by exploiting and counteracting head-level superposition.

---
*Generated: 2026-01-06T23:07:19.621521*
