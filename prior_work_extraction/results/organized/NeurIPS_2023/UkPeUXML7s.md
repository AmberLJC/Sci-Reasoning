# Prior Work Analysis Report

## Target Paper
**Title:** UkPeUXML7s
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s main advance is to explain why and how heavy-tailed stationary behavior emerges in practical, finite-data training where SGD repeatedly cycles over a dataset. Prior heavy-tail theories largely rested on online, i.i.d. sampling and infinite-data assumptions. Two streams of work directly feed into this result. First, heavy-tail modeling of SGD noise: Simsekli and collaborators formalized that mini-batch gradient noise obeys α-stable laws via generalized CLT, and Yaida provided empirical/theoretical evidence that constant–step size SGD exhibits non-Gaussian, heavy-tailed stationary behavior. These studies motivate a tail-focused theory but assume i.i.d. sampling, leaving the finite-dataset, multi-pass mechanism unclear. Second, offline SGD analysis: Shamir and Gürbüzbalaban–Ozdaglar–Parrilo established the distinct Markovian nature of without-replacement/random-reshuffling dynamics and provided tools (e.g., Poisson equation approaches) to study multi-pass SGD. Building on the Markov chain stability toolkit of Meyn and Tweedie, the present paper proves that the stationary distribution of offline SGD inherits power-law tails only approximately. Crucially, the deviation from an ideal power law is quantified using empirical-measure convergence rates in Wasserstein distance (Fournier–Guillin), directly tying the tail approximation error to the finiteness of data. Together, these works enable a precise bridge: replacing the online infinite-data assumption with finite-sample, multi-pass dynamics while preserving (approximately) the heavy-tailed stationary behavior—and rigorously controlling the approximation via statistical rates of empirical distribution convergence.

---
*Generated: 2026-01-06T23:42:49.127731*
