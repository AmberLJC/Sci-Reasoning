# Prior Work Analysis Report

## Target Paper

**Title:** Understanding Factual Recall in Transformers via Associative Memories

**Conference:** ICLR 2025 (spotlight)

**Authors:** Eshaan Nichani, Jason D. Lee, Alberto Bietti

**Keywords:** transformers, associative memories, factual recall, storage capacity, training dynamics

**Abstract:** 
> Large language models have demonstrated an impressive ability to perform factual recall. Prior work has found that transformers trained on factual recall tasks can store information at a rate proportional to their parameter count. In our work, we show that shallow transformers can use a combination of associative memories to obtain such near optimal storage capacity. We begin by proving that the storage capacities of both linear and MLP associative memories scale linearly with parameter count. W...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Hopfield Networks is All You Need** (2020)
- *Authors:* Hubert Ramsauer et al.
- *Direct Connection:* By casting attention as a modern Hopfield associative memory, this work provided the conceptual and mathematical lens used here to treat attention value matrices as associative memories and analyze their capacity.

**Neural networks and physical systems with emergent collective computational abilities** (1982)
- *Authors:* John J. Hopfield
- *Direct Connection:* Classical associative memory capacity results from Hopfield networks underlie this paper’s linear-in-parameters capacity benchmarks, which are adapted and proved for linear and MLP memories inside transformers.

**Language Models as Knowledge Bases?** (2019)
- *Authors:* Fabio Petroni et al.
- *Direct Connection:* By framing factual recall as retrieving stored knowledge from language models, this work motivates the formal synthetic factual-recall task used here to enable precise capacity analysis.

### 💡 Inspiration

**In-context Learning and Induction Heads** (2022)
- *Authors:* Catherine Olsson et al.
- *Direct Connection:* The demonstration that a single attention head performs key–value associative retrieval directly informs the constructive proof that a one-layer attention module can store and recall factual pairs via its value matrices.

### 🔍 Gap Identification

**Locating and Editing Factual Associations in GPT** (2022)
- *Authors:* Kevin Meng et al.
- *Direct Connection:* Because this work showed factual associations localize in MLP layers and can be edited, it motivated the present paper’s analysis and its key result that both MLPs and the attention value matrices can alternatively store facts with near–parameter-optimal capacity.

### 🔧 Extension

**Transformer Feed-Forward Layers Are Key-Value Memories** (2021)
- *Authors:* Mor Geva et al.
- *Direct Connection:* Building on the finding that FFNs implement key–value memories, this paper formalizes and proves linear storage capacity for MLP associative memories and constructs a shallow transformer that solves factual recall by using the MLP as the memory.

---

## Synthesis: How Prior Work Led to This Paper

Feed-forward layers in transformers were shown to act as key–value memories, with learned keys and values implementing direct associative lookup (Geva et al.). This mechanistic view connected the FFN to explicit storage of input–output associations rather than mere feature transformation. Concurrently, practical knowledge-editing studies demonstrated that factual associations are often localized in MLP layers and can be altered with targeted, low-rank updates (Meng et al.), underscoring that factual knowledge can be weight-encoded and suggesting a concrete locus of memory. From the attention side, the induction-head mechanism illustrated that even a single attention head can perform key–value retrieval by matching keys and copying corresponding values (Olsson et al.), highlighting attention as an associative lookup primitive. The associative-memory perspective was formalized by modern Hopfield theory, which recasts attention as energy-based retrieval over stored patterns (Ramsauer et al.), and rooted in classical results showing linear-in-neuron storage capacity for associative memories (Hopfield, 1982). Finally, the notion of factual recall as a knowledge-retrieval problem for language models was crystallized by probing setups like LAMA (Petroni et al.), providing a clean recall objective. Taken together, these works revealed two plausible loci for storing facts—FFN key–value memories and attention value matrices—yet left open principled capacity guarantees and their tradeoff. The present paper synthesizes these insights by proving linear storage capacity for linear and MLP associative memories, and by constructing a shallow transformer that achieves perfect factual recall using either the value matrices or the MLP, thereby characterizing when and how transformers can reach near–parameter-optimal factual storage and trade memory between modules.

---

*Analysis generated on: 2026-01-06T09:28:06.916664*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
