# Prior Work Analysis Report

## Target Paper
**Title:** IYLNdCII48
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

CACTI’s core innovation fuses two inductive biases—data-driven masking and semantic column context—within a masked autoencoding framework. The masked-imputation pretext task for tabular data traces directly to VIME, while MAE provides the modern recipe for high-ratio masking and simple reconstruction training. CACTI departs from conventional i.i.d. random masks by embracing copy-masking, a strategy popularized by CSDI to mimic real-world missingness patterns during training; CACTI further refines it with median-truncated copy masking to prevent training from being dominated by pathological or uninformative mask instances. On the representation side, FT-Transformer established that treating each feature as a token and modeling inter-feature dependencies with attention is effective for tabular data. Complementing this, table–text pretraining works such as TAPAS showed that column headers and textual metadata encode useful semantics about relationships among columns. CACTI operationalizes this insight by injecting column names and descriptions as contextual inputs, allowing the model to align structural and semantic dependencies during reconstruction. Finally, classical deep imputation methods like GAIN and MIDA motivate CACTI’s focus on explicit handling of missingness (via masks) and reconstruction-based learning without adversarial instability. Together, these strands yield a tabular imputation method that is mask-aware, semantically informed, and robust across MCAR, MAR, and MNAR settings.

---
*Generated: 2026-01-07T00:21:32.376397*
