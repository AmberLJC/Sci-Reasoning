# Prior Work Analysis Report

## Target Paper

**Title:** Subtractive Mixture Models via Squaring: Representation and Learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Lorenzo Loconte, Aleksanteri Mikulus Sladek, Stefan Mengel, Martin Trapp, Arno Solin, Nicolas Gillis, Antonio Vergari

**Keywords:** tractable inference, distribution estimation, probabilistic circuits, tensor networks

**Abstract:** 
> Mixture models are traditionally represented and learned by adding several distributions as components. Allowing mixtures to subtract probability mass or density can drastically reduce the number of components needed to model complex distributions. However, learning such subtractive mixtures while ensuring they still encode a non-negative function is challenging. We investigate how to learn and perform inference on deep subtractive mixtures by squaring them. We do this in the framework of probab...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Sum-Product Networks: A New Deep Architecture** (2011)
- *Authors:* Hoifung Poon et al.
- *Direct Connection:* This work established the tractable probabilistic circuit formalism with additive sum nodes that the present paper retains structurally while replacing purely additive mixtures by subtractive ones safeguarded through a global squaring.

**Probabilistic Circuits: A Unifying Framework for Tractable Probabilistic Models** (2020)
- *Authors:* Antonio Vergari et al.
- *Direct Connection:* This framework formalizes decomposability/determinism, tensorized mixtures, and learning/inference in probabilistic circuits, which the paper directly uses to define, learn, and analyze squared circuits that allow subtractions while keeping tractability.

**Nonnegative Rank, Decompositions, and Factorizations of Nonnegative Matrices** (1993)
- *Authors:* Joel Cohen et al.
- *Direct Connection:* The contrast between nonnegative rank and unrestricted rank from this line of work underpins the paper’s expressivity results, formalizing why allowing subtractions (then squaring) can yield exponential savings over additive mixtures.

### 💡 Inspiration

**Unsupervised Generative Modeling Using Matrix Product States** (2018)
- *Authors:* Zhao-Yu Han et al.
- *Direct Connection:* By modeling probabilities as the square of a signed tensor-network amplitude (Born rule), this paper provided the key idea that squaring can enforce nonnegativity while permitting destructive interference, directly inspiring the paper’s strategy of squaring subtractive circuits.

### 📊 Baseline

**Learning the Structure of Sum-Product Networks** (2013)
- *Authors:* Robert Gens et al.
- *Direct Connection:* This is the canonical additive-mixture SPN learning approach whose inability to represent cancellations motivates the new subtractive-by-squaring design and serves as a primary baseline the paper targets and improves upon.

### 🔧 Extension

**Probabilistic Sentential Decision Diagrams** (2014)
- *Authors:* Adnan Darwiche et al.
- *Direct Connection:* PSDDs supply the structured probabilistic circuit architecture on which the paper instantiates its squared subtractive mixtures, extending PSDDs beyond additive sums while preserving exact, tractable inference.

### 🔗 Related Problem

**On the Connection Between Sum-Product Networks and Tensor Networks** (2020)
- *Authors:* Robert Peharz et al.
- *Direct Connection:* By showing SPNs/PCs correspond to tensor decompositions, this work enables viewing circuits as tensorized mixtures, informing the paper’s positioning of squared subtractive circuits within a tensor-network-style representation and analysis.

---

## Synthesis: How Prior Work Led to This Paper

Sum-Product Networks introduced a tractable deep architecture where probability distributions are represented via additive sums over products under decomposability and completeness, fixing the template for exact inference in circuit form. Subsequent unification under probabilistic circuits clarified the semantics of decomposability/determinism and codified learning/inference routines as well as how circuit computations correspond to tensorized mixtures. PSDDs contributed a structured, deterministic circuit family that preserves tractability while aligning distributions with logical structure, serving as a practical backbone for scalable learning. In parallel, tensor-network generative modeling showed that one can model probabilities as the square of a signed amplitude—most notably with matrix product states—thereby permitting destructive interference while ensuring nonnegativity through squaring. Work connecting SPNs/PCs to tensor networks established that circuit computations implement tensor decompositions, making tensorized mixtures a natural lens for these models. Foundational results on nonnegative versus unrestricted ranks provided the mathematical rationale that forbidding subtraction can force exponentially larger nonnegative decompositions compared to signed ones. Taken together, these strands exposed a clear opportunity: circuits enforce tractability but are constrained by additivity; tensor-network Born models demonstrate that squaring recovers nonnegativity despite internal cancellations; and rank theory predicts exponential gains from allowing subtraction. The paper synthesizes these insights by defining and learning squared probabilistic circuits that permit subtractive mixtures, proving the predicted expressivity advantages and instantiating them on structured PCs (e.g., PSDDs) to retain tractable inference while achieving more compact, accurate density estimators.

---

*Analysis generated on: 2026-01-06T10:59:19.985950*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
