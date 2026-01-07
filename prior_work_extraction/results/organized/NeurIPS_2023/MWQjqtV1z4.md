# Prior Work Analysis Report

## Target Paper
**Title:** MWQjqtV1z4
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper departs from the classic RMAB paradigm inaugurated by Whittle (1988), which uses a Lagrangian relaxation to decompose a multi-armed control problem into single-armed subproblems. Subsequent works—Bertsimas and Niño-Mora (2000), Niño-Mora (2001), and Hawkins (2003)—refined this relaxation program, offering linear-programming and partial-conservation-law tools to craft implementable policies (indices or priority rules) from single-armed surrogates. In the large-system regime, Weber and Weiss (1990) pioneered asymptotic optimality arguments for many-arm RMABs, later formalized and extended by Verloop (2016), who established asymptotic optimality under the Uniform Global Attractor Property (UGAP), a demanding dynamical assumption on the fluid/mean-field limit.

The NeurIPS 2023 paper’s key innovation—Follow-the-Virtual-Advice (FtVA)—sits squarely on this lineage but changes the implementation mechanism. Instead of deriving an index or closed-form priority from the relaxed problem, FtVA simulates any chosen single-armed policy (as enabled by Whittle/Hawkins/Bertsimas–Niño-Mora) for each arm and then carefully steers the real system toward these virtual trajectories. This simulate-and-steer construction yields a policy with an O(1/√N) optimality gap for average-reward RMABs while avoiding UGAP. In discrete time, the authors replace UGAP with a simpler synchronization assumption that still covers instances where UGAP fails. Thus, FtVA preserves the intellectual core of the single-armed relaxation approach but circumvents the traditional global-attractor bottleneck, expanding the class of RMABs admitting provably near-optimal scalable control.

---
*Generated: 2026-01-06T23:42:49.068555*
