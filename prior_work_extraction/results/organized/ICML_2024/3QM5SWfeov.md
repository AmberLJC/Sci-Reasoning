# Prior Work Analysis Report

## Target Paper
**Title:** 3QM5SWfeov
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

MALIBO’s core contribution—meta-learning a likelihood-free query utility that transfers across tasks while explicitly modeling task uncertainty—grows from two converging lines of work. Classical Bayesian optimization (Snoek et al., 2012) established surrogate-driven acquisition strategies, while subsequent transfer extensions (Swersky et al., 2013) modeled task similarity to accelerate optimization on new problems. Practical meta-learning for BO emerged via warm-starting (Feurer et al., 2015) and scalable deep surrogates (DNGO; Snoek et al., 2015), but these approaches remained tied to explicit surrogates that can become sensitive to heterogeneous input scales and noise across tasks. In parallel, the meta-learning community developed task-distribution modeling: Conditional Neural Processes (Garnelo et al., 2018) enabled meta-learned surrogates across functions, and probabilistic meta-learning (PLATIPUS; Finn et al., 2018) emphasized representing uncertainty over task identity for robust adaptation. The idea of learning the acquisition mechanism itself (Volpp et al., 2020) demonstrated that query selection can be meta-learned, yet still typically depended on surrogate predictions. MALIBO synthesizes these insights by discarding explicit surrogates and directly learning a transferable utility of queries, while incorporating an explicit task-uncertainty component to guard against negative transfer when new tasks are dissimilar or sparsely observed. An auxiliary model further stabilizes adaptation, yielding a scalable, robust meta-BO procedure that outperforms surrogate-centric meta-learners on diverse benchmarks.

---
*Generated: 2026-01-07T00:02:04.894054*
