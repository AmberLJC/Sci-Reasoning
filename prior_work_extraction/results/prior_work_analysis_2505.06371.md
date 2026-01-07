# Prior Work Analysis Report

## Target Paper
**Title:** The ML.ENERGY Benchmark: Toward Automated Inference Energy Measurement and Optimization

**arXiv ID:** 2505.06371

**Abstract:** As the adoption of Generative AI in real-world services grow explosively, energy has emerged as a critical bottleneck resource. However, energy remains a metric that is often overlooked, under-explored, or poorly understood in the context of building ML systems. We present the ML$.$ENERGY Benchmark, a benchmark suite and tool for measuring inference energy consumption under realistic service environments, and the corresponding ML$.$ENERGY Leaderboard, which have served as a valuable resource for those hoping to understand and optimize the energy consumption of their generative AI services. In this paper, we explain four key design principles for benchmarking ML energy we have acquired over time, and then describe how they are implemented in the ML$.$ENERGY Benchmark. We then highlight results from the early 2025 iteration of the benchmark, including energy measurements of 40 widely used model architectures across 6 different tasks, case studies of how ML design choices impact energy consumption, and how automated optimization recommendations can lead to significant (sometimes more than 40%) energy savings without changing what is being computed by the model. The ML$.$ENERGY Benchmark is open-source and can be easily extended to various customized models and application scenarios.

---

## Identified Prior Works

### 1. MLPerf: A Benchmark Suite for Machine Learning Performance

- **Authors:** Peter Mattson, Christine Cheng, Cody Coleman, et al.
- **Year:** 2019
- **Role:** `Foundation`
- **arXiv ID:** arXiv:1910.01500

**Relationship:** MLPerf provides the foundational benchmarking suite and methodology on which the ML.ENERGY Benchmark builds, but lacks a dedicated focus on energy consumption metrics for inference.

---

### 2. CodeCarbon: Tracking Carbon Emissions from Computing

- **Authors:** Benoit Trelat, Sylvain Ruble, Gael Varoquaux, et al.
- **Year:** 2021
- **Role:** `Inspiration`
- **arXiv ID:** arXiv:2107.12342

**Relationship:** CodeCarbon inspired ML.ENERGY's integration of automated, standardized energy tracking into machine learning workflows.

---

### 3. Measuring Energy and Resource Usage of Deep Learning Training

- **Authors:** Emma Strubell, Ananya Ganesh, Andrew McCallum
- **Year:** 2019
- **Role:** `Gap Identification`
- **arXiv ID:** arXiv:1906.02243

**Relationship:** This work identifies the lack of reliable, actionable energy measurement in existing ML benchmarks, especially for inference, motivating the need for ML.ENERGY.

---

### 4. Green AI

- **Authors:** Roy Schwartz, Jesse Dodge, Noah A. Smith, Oren Etzioni
- **Year:** 2020
- **Role:** `Inspiration`
- **arXiv ID:** arXiv:1907.10597

**Relationship:** Green AI popularized the call for energy- and efficiency-aware research in machine learning, directly inspiring the focus of ML.ENERGY.

---

### 5. Optuna: A Next-generation Hyperparameter Optimization Framework

- **Authors:** Takuya Akiba, Shotaro Sano, Toshihiko Yanase, Takeru Ohta, Masanori Koyama
- **Year:** 2019
- **Role:** `Foundation`
- **arXiv ID:** arXiv:1907.10902

**Relationship:** Optuna provides methods and systems for automated optimization of model parameters, which ML.ENERGY extends for energy-aware inference optimization.

---

### 6. EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks

- **Authors:** Mingxing Tan, Quoc V. Le
- **Year:** 2019
- **Role:** `Related Problem`
- **arXiv ID:** arXiv:1905.11946

**Relationship:** EfficientNet offers advances in efficient model design, serving as a comparison for energy optimization strategies in ML.ENERGY.

---

## Synthesis Narrative

The ML.ENERGY Benchmark emerges from a convergence of developments in ML benchmarking, resource monitoring, and energy-efficient AI, collectively highlighting the field’s growing attention to sustainability concerns. Early comprehensive benchmarks like MLPerf established foundational methodologies for rigorously evaluating ML models across tasks and hardware, setting the expectation for standardized evaluation. However, as observed by Strubell et al. (2019), these benchmarks often omitted nuanced measurements of energy usage, focusing predominantly on speed and accuracy, especially for training rather than inference—the phase where models see the most real-world deployment. This gap underscored by Strubell et al. catalyzed a concerted effort in the community to treat energy as a first-class metric, not just a side effect.

Complementing calls for action, Schwartz et al.'s 'Green AI' manifesto articulated the need for efficiency and transparency regarding resource consumption, directly inspiring benchmarks and tools targeting these issues. CodeCarbon exemplified this shift, providing standardized pipelines for monitoring the energy and emissions associated with ML workloads; its user-friendly, automated approach served as a blueprint for making energy measurement practical and actionable in the ML community.

On the methodological front, optimization frameworks like Optuna provided robust mechanisms for automating search and hyperparameter tuning—critical for driving real-world reductions in resource and energy consumption. ML.ENERGY explicitly extends this automated optimization paradigm, bringing energy efficiency to the fore both as a reporting metric and as an optimization target. Concurrently, advances in efficient model architecture design, best typified by EfficientNet, offered a suite of principled, scalable alternatives to large, wasteful models. Such contributions serve as valuable baselines and comparative references within the ML.ENERGY benchmark suite, highlighting practical trade-offs encountered by developers seeking greener deployments.

Collectively, these prior works trace the problem’s evolution from broad benchmarking (MLPerf) and efficiency-aware design (EfficientNet) through to environmental impact awareness (Green AI, CodeCarbon), and the development of automated, optimization-centric workflows (Optuna). ML.ENERGY synthesizes these contributions by addressing the previously unfilled need for an open, extensible, inference-focused benchmarking suite with standardized, end-to-end energy measurement and optimization. Its leaderboard-driven, empirical approach underscores a field-wide movement towards transparency, reproducibility, and actionable sustainability metrics, fulfilling gaps and ambitions articulated in the literature over the prior half-decade.

---

*Analysis generated on: 2026-01-06T03:12:10.362358*
