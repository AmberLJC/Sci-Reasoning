# Prior Work Analysis Report

## Target Paper

**Title:** What does the Knowledge Neuron Thesis Have to do with Knowledge?

**Conference:** ICLR 2024 (spotlight)

**Authors:** Jingcheng Niu, Andrew Liu, Zining Zhu, Gerald Penn

**Keywords:** language model, knowledge neuron, model editing, formal and function competence, syntax, fact

**Abstract:** 
> We reassess the Knowledge Neuron (KN) Thesis: an interpretation of the mechanism underlying the ability of large language models to recall facts from a training corpus. This nascent thesis proposes that facts are recalled from the training corpus through the MLP weights in a manner resembling key-value memory, implying in effect that "knowledge" is stored in the network. Furthermore, by modifying the MLP modules, one can control the language model's generation of factual information. The plausib...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Language Models as Knowledge Bases?** (2019)
- *Authors:* Fabio Petroni et al.
- *Direct Connection:* It formulated factual recall in LMs via cloze-style probes and popularized the view that parameters store factual associations, which this paper adopts as the evaluation starting point before questioning whether such recall equates to 'knowledge'.

**Knowledge Neurons in Pretrained Transformers** (2022)
- *Authors:* Dai et al.
- *Direct Connection:* It introduced 'knowledge neurons' and a localization-and-editing procedure in MLPs, which this paper directly reuses to edit non-factual linguistic phenomena to probe the scope and limits of the knowledge-neuron thesis.

**Zero-Shot Relation Extraction via Reading Comprehension (ZSRE)** (2017)
- *Authors:* Omer Levy et al.
- *Direct Connection:* It supplies a standardized factual QA benchmark and evaluation protocol for post-edit behavior, which this paper uses to contrast factual editing outcomes with changes in linguistic phenomena.

**BLiMP: A Benchmark of Linguistic Minimal Pairs for English** (2020)
- *Authors:* Alex Warstadt et al.
- *Direct Connection:* It created controlled minimal-pair tests of formal grammatical competence, providing the syntactic diagnostics this paper uses to quantify how KN/ROME-style edits affect non-factual linguistic behavior.

### 💡 Inspiration

**Transformer Feed-Forward Layers Are Key-Value Memories** (2021)
- *Authors:* Mor Geva et al.
- *Direct Connection:* It argued MLP feed-forward layers implement key–value memory that stores token-level associations, the precise mechanistic premise this paper scrutinizes by testing whether the same mechanism also mediates syntactic and other linguistic behaviors.

### 📊 Baseline

**ROME: Locating and Editing Factual Associations in GPT** (2022)
- *Authors:* Kevin Meng et al.
- *Direct Connection:* It provided a causal weight-editing method targeting MLP key–value pairs (and the CounterFact evaluation), which this paper adopts as a primary editing baseline to show that identical interventions also alter syntactic behavior.

**MEMIT: Mass-Editing Memory in a Transformer** (2023)
- *Authors:* Kevin Meng et al.
- *Direct Connection:* It scaled ROME-style edits to many facts with layer-wise linear updates, a technique this paper benchmarks to demonstrate that mass MLP edits likewise modulate linguistic competence, challenging a 'facts-only' interpretation.

---

## Synthesis: How Prior Work Led to This Paper

Early evidence that language models store retrievable factual associations came from cloze-style probing, where parameters appeared to encode facts that could be recalled without explicit databases. Complementing this, work on the internal mechanics of transformers argued that feed-forward layers act as key–value memories, suggesting a concrete locus and mechanism by which such associations are represented. Building on these ideas, the knowledge neuron line of work operationalized the thesis by proposing methods to localize and directly edit neurons thought to store facts in MLP modules. Concurrently, causal intervention approaches such as ROME introduced precise weight-editing procedures targeting MLP key–value pairs, alongside factual evaluation resources like CounterFact, and later scaled to mass editing via MEMIT. Factual QA datasets such as ZSRE standardized how to measure whether an edit succeeds or generalizes, while BLiMP’s minimal-pair diagnostics provided controlled probes of formal grammatical competence across many syntactic phenomena. Together, these works supplied both the mechanistic hypothesis—that MLPs store factual knowledge—and the toolchain and benchmarks for intervening and evaluating edits. The natural open question, given the causal-editing tools and linguistic diagnostics, was whether the same MLP-targeted edits that alter factual recall are specific to “knowledge” or instead modulate broader linguistic competence. This paper synthesizes the editing protocols with syntactic evaluations to reveal that identical interventions systematically affect non-factual linguistic behavior, exposing a central limitation in the knowledge-neuron thesis and reframing what these edits truly control.

---

*Analysis generated on: 2026-01-06T18:34:36.596212*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
