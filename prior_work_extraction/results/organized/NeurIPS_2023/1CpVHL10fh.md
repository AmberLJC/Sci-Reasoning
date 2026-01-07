# Prior Work Analysis Report

## Target Paper
**Title:** 1CpVHL10fh
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

CLASH’s core contribution—early stopping for harm that is sensitive to treatment effect heterogeneity—arises by fusing two mature literatures: sequential monitoring from clinical trials/online testing and causal machine learning for heterogeneous treatment effects (HTE). On the monitoring side, the O’Brien–Fleming boundaries and the Lan–DeMets alpha‑spending framework establish how to control Type I error across repeated interim looks; Johari–Pekelis–Walsh adapt these ideas to anytime‑valid inference in A/B testing. CLASH inherits this sequential validity but redirects it from aggregate effects to subgroup‑specific harm, the locus where conventional procedures can miss minority harms.
On the HTE side, causal forests (Wager & Athey) and causal trees (Athey & Imbens) provide honest, data‑adaptive subgroup discovery and asymptotically valid CATE estimation. Meta‑learners (Künzel et al.) generalize this into a modular plug‑in architecture, allowing CLASH to be broadly applicable across learners and outcomes. Because adaptive subgroup learning can bias inference, CLASH leverages orthogonalization and cross‑fitting from double/debiased machine learning (Chernozhukov et al.) to preserve valid uncertainty quantification when combining flexible learners with sequential testing. Together, these components yield a principled procedure that repeatedly learns who is at risk, monitors those groups with proper spending of statistical error, and stops promptly when harm manifests—even if confined to a minority subgroup—thereby closing a gap left by aggregate early‑stopping methods in both clinical trials and online experiments.

---
*Generated: 2026-01-07T00:02:04.827073*
