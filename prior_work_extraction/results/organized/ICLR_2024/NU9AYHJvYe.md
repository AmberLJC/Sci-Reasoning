# Prior Work Analysis Report

## Target Paper

**Title:** Optimal Sample Complexity of Contrastive Learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Noga Alon, Dmitrii Avdiukhin, Dor Elboim, Orr Fischer, Grigory Yaroslavtsev

**Keywords:** learning theory, sample complexity, vc dimension, contrastive learning, metric learning

**Abstract:** 
> Contrastive learning is a highly successful technique for learning representations of data from labeled tuples, specifying the distance relations within the tuple. We study the sample complexity of contrastive learning, i.e. the minimum number of labeled tuples sufficient for getting high generalization accuracy. We give tight bounds on the sample complexity in a variety of settings, focusing on arbitrary distance functions,  $\ell_p$-distances, and tree metrics. Our main result is an (almost) o...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Learning a Distance Metric from Relative Comparisons** (2003)
- *Authors:* Matthew Schultz and Thorsten Joachims
- *Direct Connection:* This work formalized triplet-based relative-comparison supervision—labels of the form d(xi,xj) < d(xi,xk)—which is exactly the tuple-labeling problem whose hypothesis class the paper bounds via VC/Natarajan dimension.

**Adaptively Learning the Crowd Kernel** (2011)
- *Authors:* Ofer Tamuz et al.
- *Direct Connection:* By showing that Euclidean embeddings can be learned from triplet comparisons in practice via adaptive querying, this paper crystallized the metric-learning-from-triplets setting and motivated precise sample-complexity analysis for such tuple labels.

**Multiclass Learnability and the ERM Principle** (2011)
- *Authors:* Amit Daniely, Sivan Sabato, Shai Ben-David, and Shai Shalev-Shwartz
- *Direct Connection:* This work connects multiclass sample complexity to the Natarajan dimension, which the paper leverages by casting tuple-based distance comparisons as multiclass decisions and then bounding the corresponding Natarajan dimension.

### 💡 Inspiration

**Low-Dimensional Embedding Using Adaptively Selected Ordinal Data** (2011)
- *Authors:* Kevin G. Jamieson and Robert D. Nowak
- *Direct Connection:* Their O(nd log n) active-query guarantees for ordinal embedding into Rd highlighted the nd dependence that the current work proves (up to logs) to be necessary and sufficient in the passive, distribution-free setting and extends to general ℓp and tree metrics.

### 🔍 Gap Identification

**A Theory of Unsupervised Learning via Contrastive Learning** (2019)
- *Authors:* Arun Saunshi, Orestis Plevrakis, Sanjeev Arora, et al.
- *Direct Connection:* While providing theory for contrastive objectives, this line focused on view-based unsupervised settings and did not address sample complexity for recovering metric relations from labeled tuples, motivating the present distribution-free, optimal analysis.

### 🔧 Extension

**Bounding the Vapnik–Chervonenkis Dimension of Concept Classes Parameterized by Real Numbers** (1995)
- *Authors:* Paul W. Goldberg and Mark R. Jerrum
- *Direct Connection:* The general O(W log W) VC-dimension bound for classes defined by polynomial inequalities is instantiated here with W = n·d and inequalities of the form ∥xi−xj∥p ≤ ∥xi−xk∥p to derive tight upper bounds on sample complexity.

---

## Synthesis: How Prior Work Led to This Paper

Relative-comparison supervision for metric learning was crystallized by work showing that one can learn distances from triplet labels of the form “xi is closer to xj than xk.” Early formulations made this precise and positioned triplet judgments as the core unit of information for representation learning. Practical systems demonstrated that Euclidean embeddings can be recovered from such triplets, especially when queries are adaptively selected, establishing that tuple-labeled metric learning is both feasible and useful. On the theoretical side, active ordinal-embedding results proved that O(nd log n) triplet queries suffice to embed n points in Rd up to similarity, strongly suggesting an intrinsic nd dependence. Independently, classical learning-theory results bounded the VC dimension of real-parameterized concept classes defined by polynomial inequalities by O(W log W), exactly the regime encountered when distance comparisons can be written as polynomial relations in the embedding parameters. Complementing this, multiclass learnability theory tied sample complexity to the Natarajan dimension, providing the vehicle to convert dimension bounds for tuple-labeling problems into distribution-free sample-complexity guarantees. Meanwhile, theory for contrastive learning primarily analyzed view-based unsupervised objectives, leaving the sample complexity of metric recovery from labeled tuples largely open. Together, these strands pointed to a gap: obtain tight, distribution-free passive sample-complexity bounds for triplet-supervised metric learning across ℓp and structured metrics. The synthesis is to cast triplet comparisons as multiclass classification, leverage parametric VC/Natarajan dimension machinery to get sharp O(nd log n) upper bounds, and pair them with matching Ω(nd) lower bounds, thereby pinning down optimal rates.

---

*Analysis generated on: 2026-01-06T10:44:43.489822*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
