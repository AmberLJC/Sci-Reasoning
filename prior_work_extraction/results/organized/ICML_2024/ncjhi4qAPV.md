# Prior Work Analysis Report

## Target Paper
**Title:** ncjhi4qAPV
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Deep Learning with Differential Privacy** (2016)
- *Authors:* Martin Abadi et al.
- *Connection:* Abadi et al. formalized DP training for deep learning via DP-SGD, establishing the dominant problem formulation and mechanism that contemporary "public pretraining + private fine-tuning" workflows are meant to augment—precisely the setup this position paper interrogates.

**Semi-supervised Knowledge Transfer for Deep Learning from Private Training Data** (2017)
- *Authors:* Nicolas Papernot et al.
- *Connection:* PATE introduced the paradigm of leveraging public (non-private) data to improve utility under DP guarantees, a direct antecedent of the modern strategy of using large-scale public pretraining that this paper critically re-evaluates.

**LAION-5B: An open large-scale dataset for CLIP** (2022)
- *Authors:* Christoph Schuhmann et al.
- *Connection:* As a flagship web-scraped "public" dataset enabling massive pretraining, LAION-5B exemplifies the data sources whose privacy status this paper argues must be scrutinized in DP workflows.

### 💡 Inspiration

**Extracting Training Data from Large Language Models** (2021)
- *Authors:* Nicholas Carlini et al.
- *Connection:* This paper showed that LMs pretrained on web-scraped corpora can memorize and reveal verbatim training data, directly motivating the position paper’s claim that large-scale public pretraining should not be presumed privacy-preserving.

### 🔍 Gap Identification

**Evaluating Differentially Private Machine Learning in Practice** (2019)
- *Authors:* Bargav Jayaraman et al.
- *Connection:* By documenting severe utility degradations from DP training on standard benchmarks, this work motivated the community’s turn to public pretraining to recover accuracy—a reliance that the position paper questions on privacy and evaluation grounds.

### 🔗 Related Problem

**WILDS: A Benchmark of in-the-Wild Distribution Shifts** (2021)
- *Authors:* Pang Wei Koh et al.
- *Connection:* WILDS formalized evaluation under real distribution shifts, informing the position paper’s critique that standard benchmarks are ill-suited to measure transfer from public pretraining to sensitive domains.

**Stealing Machine Learning Models via Prediction APIs** (2016)
- *Authors:* Florian Tramèr et al.
- *Connection:* By demonstrating model extraction from third-party services, this work grounds the position paper’s observation that outsourcing compute for large pretrained models introduces additional privacy risks beyond differential privacy.

---

## Synthesis

The paper’s core argument emerges from three intertwined lines of prior work. First, Abadi et al. established the modern formulation of differentially private deep learning with DP-SGD, while Papernot et al. (PATE) introduced a concrete mechanism to combine DP with public data. Together, these works laid the foundation for today’s widely adopted recipe: leverage non-private public data to boost utility, then apply DP to the sensitive component. Second, Jayaraman and Evans quantified the sharp utility costs of DP in practice, catalyzing the field’s pivot to large-scale public pretraining as a remedy. The position paper’s central critique directly targets this solution, interrogating whether public pretraining genuinely preserves privacy. This concern is substantiated by evidence that web-scale models memorize and can reveal sensitive content: Carlini et al. demonstrated extraction of verbatim training data from large language models, showing that the very public corpora used for pretraining can embed privacy risks. Third, the paper questions how we measure generalization to sensitive domains. WILDS shaped thinking about out-of-distribution evaluation, highlighting that standard benchmarks often fail to capture real-world shifts—precisely the mismatch the paper emphasizes for sensitive-domain transfer. Finally, the reliance on large pretrained models often forces outsourcing to powerful third parties; Tramèr et al.’s model-stealing results underscore that such dependence introduces additional privacy threats, beyond DP guarantees. LAION-5B exemplifies the web-scraped datasets at the heart of these debates.

---
*Generated: 2026-01-06T23:09:26.476180*
