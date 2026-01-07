# Prior Work Analysis Report

## Target Paper

**Title:** Holistically Evaluating the Environmental Impact of Creating Language Models

**Conference:** ICLR 2025 (spotlight)

**Authors:** Jacob Morrison, Clara Na, Jared Fernandez, Tim Dettmers, Emma Strubell, Jesse Dodge

**Keywords:** machine learning, artificial intelligence, language model, large language models, environmental impact, carbon emissions, water usage

**Abstract:** 
> As the performance of artificial intelligence systems has dramatically increased, so too has the environmental impact of creating these systems. While many model developers release estimates of the power consumption and carbon emissions from the final training runs for their latest models, there is comparatively little transparency into the impact of model development, hardware manufacturing, and total water usage throughout. In this work, we estimate the real-world environmental impact of devel...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Energy and Policy Considerations for Deep Learning in NLP** (2019)
- *Authors:* Emma Strubell et al.
- *Direct Connection:* This paper established accounting for the full development cycle (e.g., hyperparameter tuning) in NLP energy/carbon estimates, which we directly generalize to include hardware manufacturing and water use across the entire LLM creation process.

**Quantifying the Carbon Emissions of Machine Learning** (2019)
- *Authors:* Alexandre Lacoste et al.
- *Direct Connection:* We adopt and build on their core carbon-accounting formulation—linking power, PUE, and location-specific grid intensity—to compute emissions, then extend the scope to multi-stage development and integrate manufacturing and water impacts.

### 🔍 Gap Identification

**Towards the Systematic Reporting of the Energy and Carbon Footprints of Machine Learning** (2020)
- *Authors:* Peter Henderson et al.
- *Direct Connection:* By highlighting the lack of lifecycle reporting and proposing standardized tracking, this work directly motivates our holistic, transparent accounting across development, training, and hardware manufacturing.

### 📊 Baseline

**Estimating the Carbon Footprint of BLOOM, a 176B Parameter Language Model** (2022)
- *Authors:* Sasha Luccioni et al.
- *Direct Connection:* Their LLM-scale case study, including amortized embodied hardware emissions, serves as the primary methodological baseline that we extend from final training runs to the full development lifecycle while adding comprehensive water accounting.

### 🔧 Extension

**Making AI Less Thirsty: Uncovering and Addressing the Secret Water Footprint of AI Models** (2023)
- *Authors:* Pengfei Li et al.
- *Direct Connection:* We adapt their water-use estimation via WUE and cooling-water modeling and extend it from isolated training events to end-to-end LLM development and integrate it alongside carbon and manufacturing impacts.

### 🔗 Related Problem

**Carbon Emissions and Large Neural Network Training** (2021)
- *Authors:* David Patterson et al.
- *Direct Connection:* Their analysis of datacenter efficiency, regional grid carbon intensity, and scheduling informs our parameterization of location- and infrastructure-dependent factors in life-cycle emissions and water estimates.

---

## Synthesis: How Prior Work Led to This Paper

Early work on environmental impacts in NLP showed that reported training costs often ignore the broader development process; notably, Strubell et al. quantified the energy and carbon of hyperparameter tuning and ablations, establishing that the true footprint extends beyond a single final run. Lacoste et al. provided the core accounting framework translating metered energy, datacenter PUE, and regional grid carbon intensity into CO2e, enabling standardized, comparable estimates. At LLM scale, Luccioni et al. presented a concrete case study for BLOOM that went beyond runtime power to include amortized embodied emissions from hardware manufacturing, demonstrating how hardware life-cycle considerations materially affect totals. Patterson et al. analyzed how datacenter efficiency, regional grid mixes, and scheduling practices shape emissions, emphasizing the importance of infrastructure-aware parameterization. Henderson et al. called for systematic, lifecycle-oriented reporting practices and instrumentation to capture real-world energy use across experiments. Complementing carbon accounting, Li et al. introduced a practical methodology for quantifying AI’s water footprint using datacenter water usage effectiveness and cooling models, revealing a significant but previously overlooked dimension. Together, these works reveal a methodological toolkit and a gap: estimates often focus on a single training run, omit water, or only partially consider embodied impacts. The natural next step is to unify these strands—combining standardized carbon accounting with embodied hardware and water-use models—and to apply them across the entire model development pipeline with real operational traces. By synthesizing lifecycle boundaries from BLOOM-style analyses, PUE/WUE-based estimators, and full-development accounting advocated by Strubell and Henderson, a holistic evaluation of creating language models becomes possible and policy-relevant.

---

*Analysis generated on: 2026-01-06T07:18:32.370468*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
