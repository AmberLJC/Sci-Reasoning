# Prior Work Analysis Report

## Target Paper

**Title:** Error Norm Truncation: Robust Training in the Presence of Data Noise for Text Generation Models

**Conference:** ICLR 2024 (spotlight)

**Authors:** Tianjian Li, Haoran Xu, Philipp Koehn, Daniel Khashabi, Kenton Murray

**Keywords:** language generation, language modeling, machine translation, robustness, estimating data quality

**Abstract:** 
> Text generation models are notoriously vulnerable to errors in the training data. With the wide-spread availability of massive amounts of web-crawled data becoming more commonplace, how can we enhance the robustness of models trained on a massive amount of noisy web-crawled text? In our work, we propose Error Norm Truncation (ENT), a robust enhancement method to the standard training objective that truncates noisy data. Compared to methods that only uses the negative log-likelihood loss to estim...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Self-Paced Learning for Latent Variable Models** (2010)
- *Authors:* M. P. Kumar et al.
- *Direct Connection:* ENT adopts the self-paced principle of discarding/attenuating high-loss training examples, but replaces the loss-based criterion with a distribution-aware error norm tailored to generative token prediction.

**Dual conditional cross-entropy filtering of noisy parallel corpora** (2018)
- *Authors:* Marcin Junczys-Dowmunt
- *Direct Connection:* This influential MT data-filtering method relies on (model) cross-entropy/NLL to assess sentence quality, the exact NLL-only heuristic ENT critiques and generalizes by leveraging the distribution of non-target tokens.

### 💡 Inspiration

**Neural Text Generation with Unlikelihood Training** (2020)
- *Authors:* Sean Welleck et al.
- *Direct Connection:* Unlikelihood explicitly leverages probabilities of non-target tokens in the training signal, providing the key insight that ENT generalizes into a principled error norm over the non-target distribution for noise-aware truncation.

### 🔍 Gap Identification

**On the Impact of Noise in Neural Machine Translation** (2018)
- *Authors:* Huda Khayrallah et al.
- *Direct Connection:* Their analysis shows that noisy web/parallel data substantially harms generation models and that NLL-based filtering is imperfect, motivating ENT’s search for a more faithful noise indicator than target-only NLL.

### 📊 Baseline

**Co-teaching: Robust Training of Deep Neural Networks with Extremely Noisy Labels** (2018)
- *Authors:* Bo Han et al.
- *Direct Connection:* As a primary small-loss selection baseline, Co-teaching’s loss-thresholding motivates ENT’s truncation, with ENT directly improving the selection signal by using a token-distribution error norm rather than NLL alone.

**Generalized Cross Entropy Loss for Training Deep Neural Networks with Noisy Labels** (2018)
- *Authors:* Zhilu Zhang et al.
- *Direct Connection:* GCE is a standard robust alternative to cross-entropy under label noise that ENT explicitly improves upon by using a truncation signal derived from the full non-target token distribution instead of modifying the loss scalar.

### 🔗 Related Problem

**Dynamic Data Selection for Neural Machine Translation** (2017)
- *Authors:* Marlies van der Wees et al.
- *Direct Connection:* DDS uses cross-entropy-based scores to select training data over time, and ENT directly refines this selection idea by replacing sentence-level NLL heuristics with a per-token distributional error norm.

---

## Synthesis: How Prior Work Led to This Paper

Self-paced learning introduced the core idea of improving robustness by prioritizing or discarding examples based on a difficulty signal derived from loss, establishing truncation as a training primitive. Co-teaching operationalized the “small-loss” principle for noisy labels by dropping high-loss examples, offering a practical baseline for robust data selection during training. Generalized Cross Entropy provided a widely used alternative to cross-entropy that tempers sensitivity to noise but still relies on target-only supervision signals. In machine translation, dual conditional cross-entropy filtering became a dominant approach to clean noisy parallel corpora using model cross-entropy/perplexity, while dynamic data selection extended cross-entropy-based selection across training to emphasize better data over time. Khayrallah and Koehn systematically documented how noise in parallel/web data degrades neural MT and highlighted the limitations of relying purely on likelihood-based heuristics. Unlikelihood training, in contrast to target-only losses, explicitly used non-target token probabilities to guide generation, demonstrating that the full predictive distribution contains actionable training signals beyond the target token.
Together these works revealed both the promise and the limits of loss/NLL-based truncation and filtering: they can remove noise, but target-only scores are myopic. The natural next step was to retain the truncation framework while upgrading the signal used to decide what to trust. ENT synthesizes these threads by computing a distribution-aware error norm over non-target tokens for token-level truncation, directly addressing the documented failures of NLL-only selection and extending non-target-aware training signals into a robust example-filtering criterion for text generation.

---

*Analysis generated on: 2026-01-06T10:08:17.665376*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
