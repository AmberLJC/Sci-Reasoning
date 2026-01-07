# Prior Work Analysis Report

## Target Paper

**Title:** Information Retention via Learning Supplemental Features

**Conference:** ICLR 2024 (spotlight)

**Authors:** Zhipeng Xie, Yahe Li

**Keywords:** Information Retention, Few-shot Learning, Deep Neural Network

**Abstract:** 
> The information bottleneck principle provides an information-theoretic method for learning a good representation as a trade-off between conciseness and predictive ability, which can reduce information redundancy, eliminate irrelevant and superfluous features, and thus enhance the in-domain generalizability. However, in low-resource or out-of-domain scenarios where the assumption of i.i.d does not necessarily hold true, superfluous (or redundant) relevant features may be supplemental to the mainl...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**The Information Bottleneck Method** (1999)
- *Authors:* Naftali Tishby et al.
- *Direct Connection:* The paper explicitly positions its "information retention" objective as a counterpoint to the Information Bottleneck’s compression trade-off, reframing the goal from squeezing representations to keeping multiple relevant signals for prediction under shift.

### 💡 Inspiration

**Just Train Twice: Improving Group Robustness Without Training Group Information** (2021)
- *Authors:* Evan Z. Liu et al.
- *Direct Connection:* The staged residual-learning idea in JTT—first train a standard model, then focus subsequent training on what it misses—inspires the paper’s sequence of learning mainline features first and then targeting residual signals as supplemental features.

**Learning from Failure: De-biasing Neural Networks by Learning to Identify Failure** (2020)
- *Authors:* Junho Nam et al.
- *Direct Connection:* LfF’s complementary-training setup (bias-only versus debiased learner) informs the explicit separation and coordinated training of "mainline" and "supplemental" feature pathways that the paper uses to encourage diverse, complementary cues.

### 🔍 Gap Identification

**Deep Variational Information Bottleneck** (2017)
- *Authors:* Alexander A. Alemi et al.
- *Direct Connection:* By operationalizing IB in deep networks and encouraging compression that prunes redundant cues, VIB highlights the very mechanism this work seeks to avoid through a supplemental-feature pathway and staged training that preserves redundant-but-useful signals.

**Gradient Starvation: A Learning Proclivity in Neural Networks** (2021)
- *Authors:* Mohammad Pezeshki et al.
- *Direct Connection:* The observation that early-learned dominant features suppress gradients for alternative predictive features directly motivates the paper’s three-stage design to relieve suppression so that supplemental features can be effectively learned.

### 📊 Baseline

**Invariant Risk Minimization** (2019)
- *Authors:* Martin Arjovsky et al.
- *Direct Connection:* IRM serves as the principal OOD baseline that enforces invariance by removing spurious features, against which this paper contrasts by retaining such signals as supplemental features and combining them with mainline cues.

### 🔗 Related Problem

**Shortcut Learning in Deep Neural Networks** (2020)
- *Authors:* Robert Geirhos et al.
- *Direct Connection:* Evidence that networks default to easy, shortcut cues motivates intentionally learning additional, diverse cues rather than suppressing them, which this paper operationalizes via its supplemental-feature learning framework.

---

## Synthesis: How Prior Work Led to This Paper

The Information Bottleneck framework formalized representation learning as a trade-off between compression and prediction, providing a powerful rationale for discarding redundant input information. Its deep instantiation, the Variational Information Bottleneck, concretely implements this pressure to compress, encouraging networks to prune features deemed superfluous for in-domain accuracy. However, the phenomenon of gradient starvation shows that early, dominant features suppress gradients needed to learn alternative predictive cues, leaving potentially useful signals underexploited. Empirical studies of shortcut learning further reveal that deep models gravitate to easy proxies, often overlooking diverse cues that could help under distribution shift. In parallel, staged and complementary training ideas emerged in robustness work: Just Train Twice introduced a two-stage procedure that first learns a strong model and then concentrates on residual errors to uncover overlooked signals, while Learning from Failure trains complementary predictors (bias-only versus debiased) to encourage learning features that the other misses. Invariant Risk Minimization, a standard OOD baseline, instead removes non-invariant cues to seek robust predictors. Together, these works expose a tension: compression and invariance can discard redundant-but-relevant cues, while learning dynamics suppress alternative features; yet staged, complementary training can recover missed signals. The current paper naturally integrates these insights by replacing compression with retention and designing a three-stage supervised framework that first learns mainline features, then deliberately learns supplemental, complementary features without being suppressed, and finally combines them to improve robustness in low-resource and shifted settings.

---

*Analysis generated on: 2026-01-06T12:59:04.274177*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
