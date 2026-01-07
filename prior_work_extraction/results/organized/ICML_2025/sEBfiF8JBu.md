# Prior Work Analysis Report

## Target Paper
**Title:** sEBfiF8JBu
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

PANDAS builds on two converging lines of work: the mechanics of in-context learning and the evolving toolkit of jailbreak attacks, with a special focus on long-context vulnerabilities. From the ICL side, Min et al. showed that models strongly imitate patterns in demonstrations, a key insight PANDAS operationalizes via Positive Affirmations and Negative Demonstrations to steer model behavior toward compliance despite safety training. Complementing this, Rubin et al.’s retrieval-based exemplar selection motivates PANDAS’s Adaptive Sampling, which conditions the many-shot fabrications on the target topic to maximize in-context influence.
Long-context works shape PANDAS’s core setting and analysis. Liu et al.’s Lost in the Middle exposes recency and positional biases that PANDAS exploits by crafting extended fabricated dialogues and validates via attention analysis, explaining why strategically placed affirmations and demonstrations override safety alignment. On the attack/benchmark front, Zou et al.’s universal adversarial prompting (GCG) establishes strong baselines and the need for robust, generalizable jailbreak techniques; PANDAS addresses this by leveraging length and curated demonstrations rather than model gradients. Red-teaming frameworks (Perez et al.) and standardized safety benchmarks (HarmBench) directly inform ManyHarm’s construction and PANDAS’s evaluation methodology. Finally, role-playing jailbreak studies reveal that affirmative persona framing increases unsafe compliance, an effect PANDAS formalizes and amplifies through its Positive Affirmations module. Together, these works directly enable PANDAS’s hybrid design—demonstration-driven steering, topic-aware sampling, and long-context exploitation—to substantially advance many-shot jailbreaking performance.

---
*Generated: 2026-01-07T00:05:12.563530*
