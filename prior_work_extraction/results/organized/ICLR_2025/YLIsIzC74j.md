# Prior Work Analysis Report

## Target Paper

**Title:** LaMPlace: Learning to Optimize Cross-Stage Metrics in Macro Placement

**Conference:** ICLR 2025 (oral)

**Authors:** Zijie Geng, Jie Wang, Ziyan Liu, Siyuan Xu, Zhentao Tang, Shixiong Kai, Mingxuan Yuan, Jianye HAO, Feng Wu

**Keywords:** Macro placement, Chip design, EDA

**Abstract:** 
> Machine learning techniques have shown great potential in enhancing macro placement, a critical stage in modern chip design.
However, existing methods primarily focus on *online* optimization of *intermediate surrogate metrics* that are available at the current placement stage, rather than directly targeting the *cross-stage metrics*---such as the timing performance---that measure the final chip quality.
This is mainly because of the high computational costs associated with performing post-place...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**RouteNet: A Graph Neural Network for Routability and Congestion Prediction in VLSI Physical Design** (2018)
- *Authors:* H. Chen et al.
- *Direct Connection:* RouteNet established that downstream routing outcomes can be accurately predicted from early placement using a learned model, directly enabling LaMPlace’s strategy of training an offline predictor for cross-stage metrics and using it in-loop.

### 🔍 Gap Identification

**Chip Placement with Deep Reinforcement Learning** (2021)
- *Authors:* Azalia Mirhoseini et al.
- *Direct Connection:* This seminal RL macro placement system optimizes surrogate objectives (e.g., wirelength/congestion) rather than signoff metrics like timing, and its well-noted misalignment with final QoR directly motivates LaMPlace’s shift to optimizing cross-stage metrics.

### 📊 Baseline

**Circuit Training: An Open-Source Framework for ML-Driven Chip Placement** (2023)
- *Authors:* A. Shah et al.
- *Direct Connection:* As the primary open-source baseline implementing the Mirhoseini-style RL formulation with proxy costs, Circuit Training is the system LaMPlace improves upon by replacing online proxy optimization with a predictor-driven cross-stage objective.

### 🔧 Extension

**MaskPlace: Fast Chip Placement via Reinforcement Learning with Dynamic Action Masking** (2023)
- *Authors:* J. Lu et al.
- *Direct Connection:* MaskPlace introduced learning a spatial action mask to prune the macro placement search space; LaMPlace directly extends this masking idea by learning masks guided by predicted cross-stage metrics rather than proxy objectives.

### 🔗 Related Problem

**AutoDMP: Automated DREAMPlace-based Macro Placement** (2023)
- *Authors:* Y. Chen et al.
- *Direct Connection:* AutoDMP exemplifies strong proxy-driven (HPWL/density) macro placement built on DREAMPlace, highlighting the field’s dependence on intermediate surrogates that LaMPlace replaces with a learned predictor of final-stage metrics.

**DRC Hotspot Prediction Using Deep Learning** (2018)
- *Authors:* W. Liu et al.
- *Direct Connection:* This line of work showed that signoff-quality metrics (e.g., DRC violations) can be predicted from pre-routing layouts, providing the key insight that costly post-placement metrics can be approximated to guide earlier-stage decisions as LaMPlace does for timing.

---

## Synthesis: How Prior Work Led to This Paper

Reinforcement-learning-based macro placement demonstrated by Mirhoseini et al. formulated sequential macro placement and trained policies against proxy costs such as wirelength and congestion, establishing a powerful paradigm but one whose rewards were decoupled from final signoff quality. Circuit Training operationalized this approach as an open-source baseline with the same proxy-driven objective and costly, infrequent feedback from downstream tools. In parallel, MaskPlace introduced dynamic action masking to prune spatial choices during macro placement, proving that a learned mask can dramatically stabilize learning and speed the search without sacrificing quality. Outside direct optimization, RouteNet showed that routing congestion—a downstream, cross-stage outcome—can be predicted accurately from early placement features using learned models, providing rapid, differentiable feedback in lieu of full routing. Similarly, deep-learning-based DRC hotspot prediction demonstrated that high-cost signoff metrics can be approximated from early-stage layouts to inform design decisions. AutoDMP further underscored the community’s reliance on differentiable or heuristic proxies (HPWL/density) for efficiency, while still lacking direct optimization of final timing or manufacturability.
Together, these works revealed a gap: strong search procedures and masking exist, but they are guided by proxy objectives that can misalign with timing and other cross-stage metrics; meanwhile, learned surrogates can accurately approximate expensive downstream outcomes. LaMPlace synthesizes these insights by training an offline predictor for cross-stage metrics and using it online to drive a learned spatial mask, thus constraining macro placement toward regions that improve predicted timing and signoff quality while retaining the efficiency benefits of masked search.

---

*Analysis generated on: 2026-01-06T14:50:14.265346*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
