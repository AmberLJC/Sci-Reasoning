# Prior Work Analysis Report

## Target Paper

**Title:** On the Expressiveness of Rational ReLU Neural Networks With Bounded Depth

**Conference:** ICLR 2025 (spotlight)

**Authors:** Gennadiy Averkov, Christopher Hojny, Maximilian Merkert

**Keywords:** expressive power, depth, exact representations, ReLU networks, mixed volumes, lattice polytopes, number theory

**Abstract:** 
> To confirm that the expressive power of ReLU neural networks grows with their depth, the function $F_n = \max (0,x_1,\ldots,x_n )$ has been considered in the literature.
  A conjecture by Hertrich, Basu, Di Summa, and Skutella [NeurIPS 2021] states that any ReLU network that exactly represents $F_n$ has at least $\lceil \log_2 (n+1) \rceil$ hidden layers.
  The conjecture has recently been confirmed for networks with integer weights by Haase, Hertrich, and Loho [ICLR 2023].

  We follow up on th...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**On the Depth of ReLU Networks: The Max Function F_n as a Depth Witness** (2021)
- *Authors:* Benedikt Hertrich et al.
- *Direct Connection:* This NeurIPS 2021 paper introduced F_n = max(0, x1, …, xn) as the canonical witness and conjectured the ceil(log2(n+1)) depth lower bound for exact representation with ReLU networks, defining the problem and target bound that the present work partially confirms for rational weights.

**On the Number of Linear Regions of Deep Neural Networks** (2014)
- *Authors:* G. F. Montúfar et al.
- *Direct Connection:* Their polyhedral/region-count framework for piecewise-linear ReLU functions provides the structural lens (via affine pieces and combinatorial growth across layers) that this paper leverages when translating weight restrictions into limits on how depth can expand the max-structure of F_n.

### 💡 Inspiration

**Tropical Geometry of Deep Neural Networks** (2020)
- *Authors:* R. Zhang et al.
- *Direct Connection:* By recasting ReLU networks as max-plus/tropical objects with associated Newton polytopes, this work motivates the mixed-volume and lattice-polytope viewpoint that underpins the number-theoretic and geometric analysis used here to derive depth lower bounds under rational weight constraints.

### 🔍 Gap Identification

**Complexity of Linear Regions in Deep Networks** (2019)
- *Authors:* B. Hanin et al.
- *Direct Connection:* They show region-count bounds can be loose and decoupled from exact representability, sharpening the need for exact-function witnesses like F_n and motivating the search for precise depth lower bounds under additional constraints such as weight arithmetic.

### 🔧 Extension

**Depth Lower Bounds for ReLU Networks with Integer Weights** (2023)
- *Authors:* Christian Haase et al.
- *Direct Connection:* Their proof that any integer-weight ReLU network exactly computing F_n needs at least ceil(log2(n+1)) hidden layers is the immediate precursor whose depth-lower-bound methodology and witness function F_n this work generalizes from integer weights to rational (N-ary) weights.

### 🔗 Related Problem

**Benefits of Depth in Neural Networks** (2016)
- *Authors:* M. Telgarsky
- *Direct Connection:* This depth-separation work clarified how compositional structure amplifies expressivity, directly motivating the use of simple, compositional witnesses (like F_n via binary max trees) and framing why proving exact-depth lower bounds is both natural and nontrivial.

---

## Synthesis: How Prior Work Led to This Paper

Hertrich, Basu, Di Summa, and Skutella established F_n = max(0, x1, …, xn) as a canonical witness for studying depth, formulating the precise conjecture that exact computation of F_n with ReLU networks requires a logarithmic number of hidden layers. Haase, Hertrich, and Loho then confirmed this conjecture for integer-weight networks, showing ceil(log2(n+1)) depth is unavoidable in that arithmetic setting and showcasing techniques that track how max-composition propagates through layers. Parallel developments on the geometry of ReLU networks—most notably the tropical viewpoint of Zhang, Naitzat, and Lim—connect ReLU computation to max-plus algebra and Newton polytopes, providing the polyhedral/mixed-volume machinery to reason about how algebraic constraints restrict combinatorial growth. Earlier structural work by Montúfar, Pascanu, Cho, and Bengio quantified how piecewise-linear regions expand with depth, giving a combinatorial template, while Hanin and Rolnick highlighted that region counts alone can misrepresent exact representability, pushing the field toward function-specific certificates. Telgarsky’s depth-separation results reinforced the centrality of compositional witnesses in exposing depth advantages. Taken together, these works isolate F_n as the right exact witness, supply a proven integer-weight lower bound, and furnish geometric tools to relate arithmetic constraints to combinatorial expressivity. The present paper synthesizes these threads by replacing integrality with rational N-ary constraints and, via tropical/polyhedral reasoning, converts denominator structure into limits on per-layer “max-arity,” yielding ceil(log3(n+1)) for decimal fractions and a general Ω(ln n / ln ln N) lower bound—thereby partially confirming the original conjecture beyond the integer case.

---

*Analysis generated on: 2026-01-06T10:32:18.022034*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
