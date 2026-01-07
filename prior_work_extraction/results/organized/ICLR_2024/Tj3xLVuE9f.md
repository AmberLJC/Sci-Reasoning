# Prior Work Analysis Report

## Target Paper

**Title:** On the Foundations of Shortcut Learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Katherine Hermann, Hossein Mobahi, Thomas FEL, Michael Curtis Mozer

**Keywords:** shortcut learning, spurious correlations, architectural inductive bias

**Abstract:** 
> Deep-learning models can extract a rich assortment of features from data. Which features a model uses depends not only on *predictivity*---how reliably a feature indicates training-set labels---but also on *availability*---how easily the feature can be extracted from inputs. The literature on shortcut learning has noted examples in which models privilege one feature over another, for example texture over shape and image backgrounds over foreground objects. Here, we test hypotheses about which in...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Shortcut Learning in Deep Neural Networks** (2020)
- *Authors:* Robert Geirhos et al.
- *Direct Connection:* It articulated the notion that models prefer 'shortcuts'—features that are easier to extract than the intended signal—directly motivating this paper’s formalization of feature 'availability' and its quantitative study of shortcut use.

### 💡 Inspiration

**ImageNet-trained CNNs are biased towards texture; increasing shape bias improves accuracy and robustness** (2019)
- *Authors:* Robert Geirhos et al.
- *Direct Connection:* Its texture-over-shape finding suggested that locality and global integration govern ease of extraction, which this work systematically manipulates to test how availability competes with predictivity.

**Approximating CNNs with Bag-of-Local-Features models works surprisingly well on ImageNet** (2019)
- *Authors:* Wieland Brendel et al.
- *Direct Connection:* Showing that local texture patches suffice for high ImageNet accuracy implied an architectural bias toward local cues, which informed the hypothesis and experiments that treat locality as a key determinant of feature availability.

**On the Spectral Bias of Neural Networks: Towards Understanding the Frequency Principle** (2019)
- *Authors:* Nasim Rahaman et al.
- *Direct Connection:* Its result that networks learn low-frequency components first motivated the design of latent features with controlled frequency content to probe how frequency-based availability affects shortcut selection.

### 🔍 Gap Identification

**Distributionally Robust Neural Networks for Group Shifts: On the Importance of Regularization for Invariance** (2020)
- *Authors:* Shiori Sagawa et al.
- *Direct Connection:* By framing spurious correlation primarily in terms of group-wise predictivity (e.g., Waterbirds) and optimizing worst-group risk, it left unaddressed how availability shapes feature choice—a limitation this work targets with a new bias metric and controlled datasets.

### 🔧 Extension

**Invariant Risk Minimization** (2019)
- *Authors:* Martin Arjovsky et al.
- *Direct Connection:* The Colored MNIST setup with a core feature (digit shape) and a spurious feature (color) provided the two-feature generative template that this paper generalizes by decoupling predictivity from ease-of-extraction and introducing continuous availability knobs.

### 🔗 Related Problem

**Unmasking Clever Hans predictors and assessing what machines really learn** (2019)
- *Authors:* Sebastian Lapuschkin et al.
- *Direct Connection:* By uncovering cases where models rely on spurious context (e.g., backgrounds, watermarks) rather than the intended object, it provided concrete shortcut phenomena that this work reproduces in a controlled generative form to measure over-reliance.

---

## Synthesis: How Prior Work Led to This Paper

Shortcut learning was crystallized as a central paradigm by work showing that deep networks preferentially exploit features that are easier to extract than the intended signal, framing such cues as “shortcuts” rather than mere noise. Empirical evidence that ImageNet CNNs favor texture over shape pinpointed locality and global integration as determinants of ease, while bag-of-local-features results demonstrated that local patches can carry enough discriminative signal to drive high accuracy, revealing an architectural bias toward local, texture-like cues. Complementary theory established that networks tend to learn low-frequency or simpler components first, suggesting a frequency-based notion of feature ease. In parallel, the IRM framework introduced a clean two-feature synthetic template (Colored MNIST) to study spurious correlations via environments that modulate feature-label predictivity, and group-robust training/evaluation highlighted the worst-group failure modes when spurious correlations dominate, often illustrated by background–foreground confounds. Explanatory analyses of “Clever Hans” failures further documented real-world reliance on contextual artifacts like backgrounds and watermarks.
Together these works exposed a gap: existing benchmarks and methods largely operationalize spuriousness through predictivity (correlation strength) or environment variation, but lack a principled handle on the ease with which features are extracted. The present study synthesizes these insights by introducing a minimal generative setup with two latent features whose predictivity and availability (via locality, frequency, and linear decodability) can be independently tuned, and by defining a shortcut-bias metric to quantify over-reliance, thereby unifying empirical, architectural, and theoretical threads into a controlled analysis of when and why shortcuts prevail.

---

*Analysis generated on: 2026-01-06T10:20:04.522736*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
