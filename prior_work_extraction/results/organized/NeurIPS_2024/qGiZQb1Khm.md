# Prior Work Analysis Report

## Target Paper
**Title:** qGiZQb1Khm
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s core contribution—provably detecting whether an LLM was trained on synthetic data produced by a watermarked generator—fuses two lines of work: training-data tracing and LLM text watermarking. Sablayrolles et al. (Radioactive Data) established the central idea that small, structured perturbations can imprint a signature on model parameters, enabling post-hoc attribution; the present work translates this paradigm to language models by treating the watermark’s token-selection bias as the signature and analyzing its survival through fine-tuning. Kirchenbauer et al.’s LLM watermark provides the concrete mechanism and detection statistic (z-score over greenlist/redlist token usage) whose weak residual becomes the target signal inside the fine-tuned model. The statistical rigor of the detection pipeline echoes classical spread-spectrum watermarking (Cox et al.), using correlation-style aggregation and hypothesis testing to deliver calibrated p-values even when individual signals are faint.
Prior auditing methods centered on instance-level memorization—canaries and extraction (Carlini et al. 2019; 2021)—or membership inference (Shokri et al. 2017), which require known suspect strings or lack reliable guarantees in this setting. By contrast, this paper elevates attribution to the dataset level: it links detectability to watermark robustness, its prevalence in the fine-tuning corpus, and the dynamics of fine-tuning, and shows that residual statistical bias can be measured directly from an open-weight model’s logits/outputs. In doing so, it unifies watermark design with radioactive-data tracing, yielding a practical and theoretically grounded test for "training on synthetic, watermarked text."

---
*Generated: 2026-01-06T23:33:36.269129*
