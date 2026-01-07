# Prior Work Analysis Report

## Target Paper
**Title:** 36uy2GgAy6
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s core advance—minimax-optimal correlation estimation when X and Y are split across two privacy-constrained servers—rests on the modern local differential privacy (LDP) minimax program and information-constrained inference. Duchi, Jordan, and Wainwright established the channel-based LDP framework and separation between interactive and non-interactive protocols, which this work extends to a vertically partitioned two-server model with heterogeneous (ε,δ) budgets, translating their paradigm to cross-moment estimation needed for correlation. Acharya, Canonne, and Tyagi’s chi-square contraction method supplies a flexible lower-bound toolkit that directly supports the paper’s rate-optimality claims and its comparisons of interaction benefits under asymmetric privacy. On the constructive side, Kairouz, Oh, and Viswanath’s extremal-mechanism results inform the choice of per-server privatization for low-order moments (means and second moments), yielding near-optimal noise-accuracy tradeoffs in both non-interactive and interactive designs. At the mechanism level, Warner’s randomized response provides robust primitives for privatizing binary transforms (e.g., signs/thresholded features) that enable unbiased cross-moment estimation when raw pairs cannot be shared. For inference, Sheffet’s techniques for privately estimating covariance/OLS and forming valid confidence intervals guide the development of debiased correlation estimators with quantifiable uncertainty under injected noise. Finally, Bassily and Smith’s results on optimal non-interactive LDP aggregation anchor the analysis of one-shot protocols, clarifying when interaction is necessary. Together, these works directly enable the paper’s unified characterization of minimax rates and practical procedures for correlation across privacy barriers.

---
*Generated: 2026-01-07T00:02:04.929499*
