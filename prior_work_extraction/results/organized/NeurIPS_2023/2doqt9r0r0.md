# Prior Work Analysis Report

## Target Paper
**Title:** 2doqt9r0r0
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The NeurIPS 2023 paper’s core advance—an O(log n)-regret, polynomial-time algorithm that controls both connection and movement costs for online k-clustering—sits at the intersection of dynamic facility models and movement-aware online optimization. Its most direct precursor is Fotakis et al. (2021), which introduced the same online clustering-with-movement framework but only achieved O(k)-regret on the connection cost; the new work closes this gap by jointly controlling movement and service and improving the factor to O(log n). The technical route follows the movement-cost paradigm from metrical task systems on trees (Bubeck–Cohen–Lee–Lee), where entropic mirror-descent potentials balance service and movement. To extend guarantees beyond trees, the paper leverages FRT embeddings, whose O(log n) distortion naturally explains the appearance of the logarithmic factor in the regret bound when moving from HSTs to general metrics. On the modeling and coupling of costs over time, dynamic facility-location work (Eisenstat–Mathieu–Schabanel) provides a canonical way to account for facility movement and its interplay with assignment costs, guiding both problem formulation and analysis. Finally, classical online facility location (Meyerson) and structural results for k-median via local search (Arya et al.) supply the service-cost control and exchange/triangle-inequality tools needed to compare online decisions to the best fixed centers. Together, these threads yield a polynomial-time algorithm that upgrades prior guarantees to an O(log n) bound on total cost.

---
*Generated: 2026-01-06T23:42:48.041924*
