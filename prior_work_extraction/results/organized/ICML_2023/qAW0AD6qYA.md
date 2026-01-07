# Prior Work Analysis Report

## Target Paper
**Title:** qAW0AD6qYA
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing** (1995)
- *Authors:* Yoav Benjamini et al.
- *Connection:* The BHN method directly embeds the Benjamini–Hochberg FDR control procedure, and the paper’s multiple-hypothesis-testing framing of noisy-label detection relies fundamentally on this result.

**Using Trusted Data to Train Deep Networks on Noisy Labels** (2018)
- *Authors:* Dan Hendrycks et al.
- *Connection:* This work established the practical and theoretical value of leveraging a small trusted (clean) subset in noisy-label learning; the present paper adopts this assumption and repurposes the clean set to calibrate hypothesis tests for label-error detection.

### 💡 Inspiration

**MentorNet: Learning Data-Driven Curriculum for Very Deep Neural Networks on Corrupted Labels** (2018)
- *Authors:* Lu Jiang et al.
- *Connection:* MentorNet demonstrated how a small clean set can supervise sample selection/weighting, directly inspiring the present work’s insight to leverage clean data to supervise noisy-label detection rather than only robust training.

### 🔍 Gap Identification

**Confident Learning: Estimating Uncertainty in Dataset Labels** (2021)
- *Authors:* Curtis G. Northcutt et al.
- *Connection:* Confident Learning provides strong label-error detection without formal FDR guarantees; the new paper explicitly addresses this gap by casting detection as multiple testing and controlling FDR with BH.

### 📊 Baseline

**CleanNet: Transfer Learning for Scalable Image Classifier with Label Noise** (2018)
- *Authors:* Kyunghyun Lee et al.
- *Connection:* CleanNet uses a small clean set to learn a verifier for mislabeled samples; the proposed BHN directly improves upon this clean-data-driven detection paradigm by providing principled FDR control via BH.

**DivideMix: Learning with Noisy Labels as Semi-supervised Learning** (2020)
- *Authors:* Junnan Li et al.
- *Connection:* DivideMix separates clean/noisy samples via mixture modeling and heuristics; BHN contrasts by replacing heuristic thresholding with BH-based testing to control FDR, yielding stronger detection guarantees.

---

## Synthesis

The core innovation of this paper is to recast noisy-label detection—with access to a small clean subset—as a multiple hypothesis testing problem and to integrate the Benjamini–Hochberg (BH) procedure into deep models for explicit FDR control. This rests squarely on Benjamini and Hochberg (1995), whose step-up procedure provides the statistical backbone BHN embeds to guarantee false discovery control in detection. The second pillar is the clean-data assumption: Hendrycks et al. (2018) showed that a small trusted set can be leveraged to improve learning under label noise; BHN extends this idea from robust training to principled detection by using clean data to calibrate tests. Among clean-data-based detectors, CleanNet (2018) is the most directly comparable baseline—also exploiting a small clean set—yet lacks formal error-rate guarantees; BHN addresses precisely this limitation by importing BH-based control. Strong detection methods without trusted data, notably Confident Learning (Northcutt et al., 2021), motivated the need for statistical control since they provide high-quality scores but no FDR guarantees. MentorNet (2018) further inspired the notion that clean labels can guide sample selection, an idea BHN reinterprets through the lens of hypothesis testing for detection. Finally, DivideMix (2020), a leading sample-selection baseline, highlights the prevailing reliance on heuristic thresholds; BHN replaces these with BH-driven decisions, converting performance gains into provable FDR control.

---
*Generated: 2026-01-06T23:09:26.556641*
