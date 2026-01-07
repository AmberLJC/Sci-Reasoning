# Prior Work Analysis Report

## Target Paper
**Title:** aUAG1WS7J2
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

FedCBDR’s core innovation is to make replay-based federated class-incremental learning explicitly class-balanced by coordinating memory construction from a global perspective and reweighting the objective to correct bias between replayed and new classes. The replay foundation is inherited from iCaRL, which introduced class-wise exemplar management and herding to preserve old knowledge, and from DER, which established that augmenting rehearsal with logit/representation matching strengthens retention. Building on these rehearsal paradigms, FedCBDR introduces a class-aware, importance-sensitive sampler that is globally coordinated across clients—a natural federated generalization of iCaRL’s per-class exemplar logic, now informed by global statistics.
At the objective level, LUCIR and BiC directly address the characteristic bias toward newly introduced classes in class-incremental settings. Their rebalancing and bias-correction mechanisms motivate FedCBDR’s reweighted training objective to mitigate the skew between abundant new samples and scarce replayed ones. Complementing this, Class-Balanced Loss provides a principled recipe for per-class weighting based on effective sample counts, which underlies FedCBDR’s class-wise reweighting to tackle both within-buffer and across-task imbalances.
Finally, the federated constraint—preserving privacy while forming a global view—draws on data-free distillation ideas typified by FedDF, which aggregates client knowledge without sharing raw data. FedCBDR adapts this to reconstruct global representations of prior tasks that guide class-aware sampling, achieving privacy-preserving, globally balanced replay across heterogeneous clients.

---
*Generated: 2026-01-07T00:21:32.268210*
