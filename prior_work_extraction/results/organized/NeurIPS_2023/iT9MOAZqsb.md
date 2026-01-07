# Prior Work Analysis Report

## Target Paper
**Title:** iT9MOAZqsb
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core innovation—an analytic mean-field framework that explains adversarial training dynamics in random deep networks, derives tight Lp/Lq adversarial loss bounds, and predicts architectural/width effects—emerges at the intersection of robust optimization and mean-field analyses of deep nets. Goodfellow et al. established Lp-bounded adversarial perturbations and loss formulations, while Madry et al. cast robustness as a principled min–max training problem; these define the objective whose dynamics Kumano et al. set out to analyze. Classical mean-field theory for random deep networks (Schoenholz et al.) provided variance and gradient propagation recursions and edge-of-chaos conditions, but did not address adversarial objectives or evolving weight statistics during robust training. NTK theory (Jacot et al.) characterized infinite-width training in the lazy regime; however, its static-kernel assumption misses the feature and variance evolution central to adversarial optimization. Architecturally, residual shortcuts (He et al.) are known to stabilize deep training; Kumano et al. theoretically confirm that, under adversarial training, networks without shortcuts are generally not trainable and that increasing width alleviates this limitation—linking robustness to mean-field trainability conditions. Finally, certified defenses (Wong & Kolter) demonstrated that upper-bounding worst-case adversarial loss is feasible, and robustness–accuracy trade-off results (Tsipras et al.) suggested capacity tensions; Kumano et al. synthesize these threads by deriving empirically tight, analytic upper bounds across Lp/Lq settings and proving that adversarial training reduces effective capacity, while quantifying how width and dimensionality modulate these effects.

---
*Generated: 2026-01-06T23:42:48.044610*
