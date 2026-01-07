# Prior Work Analysis Report

## Target Paper
**Title:** DrUR87D4Hj
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—Attention Bias Optimization (ABO) for causal input attribution—emerges from three converging threads. First, foundational attribution tools such as Integrated Gradients and Transformer-tailored relevance propagation (Chefer et al.) provided widely used but imperfect baselines, revealing gradient saturation, context leakage, and tenuous links between attention and explanation. Second, attention-focused attribution (Abnar & Zuidema) highlighted that attention structure is informative yet non-causal when merely observed. ABO turns this observation into intervention by directly manipulating the attention mechanism. The feasibility of such targeted control stems from architectural advances that expose an explicit attention bias term: ALiBi established additive attention biases as a principled lever on attention logits. ABO exploits this lever, optimizing per-token biases to measure how steering attention changes generation, thereby quantifying causal influence without altering model weights. Third, causal perturbation ideas (representation erasure) demonstrated the value of interventions but suffered from distribution shift when tokens are removed. ABO preserves input integrity while still performing causal tests. Finally, insights from long-context studies like Lost in the Middle motivated a rigorous needle-in-a-haystack stress test, revealing that standard attributions over-credit irrelevant context as inputs grow. ABO is built to remain robust in this regime, combining parameter-efficient steering (inspired by prefix/prompt tuning) with attention-bias interventions to deliver stable, causal attributions that better reflect which tokens truly drive an LLM’s output.

---
*Generated: 2026-01-06T23:42:48.167665*
