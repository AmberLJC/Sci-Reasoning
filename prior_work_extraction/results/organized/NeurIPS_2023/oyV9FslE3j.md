# Prior Work Analysis Report

## Target Paper
**Title:** oyV9FslE3j
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

TempBalance’s core contribution—treating layer-wise learning rates as temperatures and setting them using HT-SR metrics—rests on two converging lines of prior work. First, the Heavy-Tailed Self-Regularization (HT-SR) program (Martin & Mahoney, 2019; Martin & Mahoney, 2019) established that trained networks’ weight matrices exhibit heavy-tailed spectra, with per-layer power-law exponents serving as quantitative indicators of implicit self-regularization. These works not only supplied the statistical-mechanical lens but also provided practical, validated layer-wise metrics (e.g., PL exponents and log-norm aggregates) that correlate with generalization quality—precisely the signals TempBalance exploits to prioritize and calibrate layers.

Second, advances in optimization framed learning rate as a temperature-like control variable and demonstrated the utility of layer-wise scaling. Mandt et al. (2017) theoretically linked SGD’s stationary distribution to an effective temperature determined by learning rate and batch size, while Smith et al. (2018) operationalized this view via noise-scale control. In parallel, LARS (You et al., 2017) and LAMB (You et al., 2019) showed that adjusting learning rates per layer can stabilize and accelerate large-batch training, establishing a practical template for layer-wise adaptation.

Simsekli et al. (2019) closed the conceptual loop by revealing heavy-tailed characteristics in SGD noise, connecting optimization dynamics to the heavy-tailed perspective. TempBalance integrates these strands: it retains the proven effectiveness of layer-wise rate scaling, grounds the temperature interpretation in SGD theory, and replaces heuristic layer criteria with HT-SR spectral metrics to balance per-layer temperatures during training.

---
*Generated: 2026-01-06T23:42:48.031008*
