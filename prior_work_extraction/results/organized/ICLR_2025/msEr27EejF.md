# Prior Work Analysis Report

## Target Paper

**Title:** Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking

**Conference:** ICLR 2025 (spotlight)

**Authors:** Cassidy Laidlaw, Shivam Singhal, Anca Dragan

**Keywords:** reward hacking, reward gaming, overoptimization, occupancy measures

**Abstract:** 
> Because it is difficult to precisely specify complex objectives, reinforcement learning policies are often optimized using proxy reward functions that only approximate the true goal. However, optimizing proxy rewards frequently leads to reward hacking: the optimized reward function ceases to be a good proxy and the resulting policy performs poorly with respect to the unspecified true reward. Principled solutions to reward hacking have been impeded by the lack of a good definition for the problem...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**The Inverse Reward Design Problem** (2017)
- *Authors:* Hadfield-Menell et al.
- *Direct Connection:* By formalizing designed rewards as proxies valid primarily on a training (reference) distribution and highlighting out-of-distribution failure, it provides the foundational proxy-vs-true reward framing and the distributional lens that this paper operationalizes via correlation on a reference policy’s occupancy.

**Learning to Summarize with Human Feedback** (2020)
- *Authors:* Stiennon et al.
- *Direct Connection:* It instantiated RLHF with a learned reward model and KL regularization to a reference model—an empirical recipe whose observed overoptimization issues motivate the need for a formal definition and whose KL term is theoretically justified by this paper’s analysis.

### 💡 Inspiration

**Categorizing Variants of Goodhart’s Law** (2019)
- *Authors:* Manheim and Garrabrant
- *Direct Connection:* This work frames reward hacking as the breakdown of correlation between a proxy and true objective under optimization, directly inspiring the paper’s formal correlation-based definition of reward hacking conditioned on a reference policy’s distribution.

### 🔍 Gap Identification

**Concrete Problems in AI Safety** (2016)
- *Authors:* Amodei et al.
- *Direct Connection:* This paper popularized reward hacking/specification gaming and explicitly noted the lack of principled definitions and mitigations, a gap the current work addresses with a precise definition and theory-backed mitigation.

### 📊 Baseline

**Training Language Models to Follow Instructions with Human Feedback** (2022)
- *Authors:* Ouyang et al.
- *Direct Connection:* As the standard RLHF baseline using PPO with a KL penalty to a reference policy, it is the primary system whose reward-model overoptimization this work explains and mitigates via reference-policy regularization grounded in the new definition.

### 🔗 Related Problem

**Direct Preference Optimization: Your Language Model is Secretly a Reward Model** (2023)
- *Authors:* Rafailov et al.
- *Direct Connection:* DPO’s objective explicitly ties policy updates to a fixed reference model, and this paper’s theory explains such reference-anchored objectives as mitigating reward hacking by preserving proxy–true correlation on the reference occupancy.

**Safe Policy Improvement with Baseline Bootstrapping** (2019)
- *Authors:* Laroche et al.
- *Direct Connection:* SPIBB shows that constraining deviation from a baseline policy’s occupancy yields safety guarantees, directly informing this paper’s mitigation that regularization to a reference policy prevents correlation breakdown and reward hacking.

---

## Synthesis: How Prior Work Led to This Paper

Manheim and Garrabrant articulated Goodhart’s law in optimization settings as the collapse of correlation between a proxy and the true objective once the proxy is pushed hard, crystallizing the exact failure mode central to reward hacking. The Inverse Reward Design problem formalized designed rewards as proxies that are only reliable on a training or reference distribution, emphasizing distribution shift as the locus where proxies fail and providing a precise proxy–true reward framing. Concrete Problems in AI Safety surfaced reward hacking and specification gaming as concrete risks and highlighted the lack of principled definitions and guarantees. In applied alignment, RLHF systems like Learning to Summarize with Human Feedback and the widely used InstructGPT setup introduced learned reward models with a KL penalty to a reference model, revealing both the practical prevalence of reward overoptimization and an empirical mitigation via reference-anchored updates. Direct Preference Optimization went further by baking a fixed reference model into a closed-form objective, implicitly constraining distribution shift. In parallel, SPIBB demonstrated in RL that constraining divergence from a baseline policy’s occupancy can provably safeguard performance.
Together, these works reveal a consistent picture: proxies are reliable only on the reference distribution; optimizing them can break proxy–true alignment; and anchoring to a reference policy can preserve reliability. The current paper synthesizes these insights by giving a formal, correlation-based definition of reward hacking on the reference policy’s occupancy and proving that regularizing toward the reference policy prevents correlation breakdown—thereby unifying and theoretically grounding the KL-regularization heuristics in RLHF and reference-anchored objectives like DPO, while directly addressing the long-standing definitional gap.

---

*Analysis generated on: 2026-01-06T07:16:28.589579*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
