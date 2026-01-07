# Prior Work Analysis Report

## Target Paper
**Title:** mu7Er7f9NQ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core innovation—constructing tight, anytime-valid confidence sequences for means of bounded random vectors via a general gambling framework—rests on the supermartingale logic inaugurated by Ville, which guarantees time-uniform validity from wealth processes. Shafer and Vovk’s game-theoretic formulation provides the conceptual substrate: inference is conducted through bets whose capital processes (e-processes) certify evidence. Building on this, Howard, Ramdas, and coauthors supplied a general recipe for confidence sequences using nonnegative supermartingales and mixture constructions for bounded processes; the present work extends that scalar recipe to categorical and multidimensional observations through a simple reduction, yielding multivariate CSs.
A key design element is the adoption of a mixture portfolio, explicitly inspired by Cover’s universal portfolio, to aggregate across portfolio choices and produce powerful multivariate test supermartingales. This exploitation of wealth aggregation mirrors universal portfolio ideas and is operationalized using coin-betting principles from Orabona and Pál, which translate parameter-free online gains into robust capital processes—crucial for adaptive, tight CSs without delicate tuning.
For the application to sampling without replacement in finite categorical populations, the framework aligns with classical finite-population concentration (Serfling), enabling tailored anytime-valid CSs that respect the reduced variance structure inherent to without-replacement sampling. Collectively, these works supply (i) the validity engine (Ville; Shafer–Vovk), (ii) the modern CS construction toolkit (Howard et al.; Waudby-Smith & Ramdas), and (iii) the multivariate strength via portfolio mixtures (Cover) and coin-betting adaptivity (Orabona & Pál), culminating in the paper’s general, tight gambling-based CSs for bounded random vectors.

---
*Generated: 2026-01-06T23:42:48.072272*
