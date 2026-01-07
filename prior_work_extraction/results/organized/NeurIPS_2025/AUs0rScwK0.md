# Prior Work Analysis Report

## Target Paper
**Title:** AUs0rScwK0
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Sketched Gaussian Mechanism (SGM) unifies two lines of work—communication-efficient sketching and client-level differential privacy—under a single, tighter privacy analysis. On the communication side, early federated learning work by Konečný et al. framed the need for compressed/structured updates, and FETCHSGD established sketches (e.g., CountSketch) as practical client-side compressors. In parallel, the DP community showed that random projections themselves can act as privacy mechanisms, with Blocki et al. proving that Johnson–Lindenstrauss-type sketching affords privacy controlled by the sketch dimension. On the privacy side specific to FL, Geyer et al. formalized client-level DP via clipping and a Gaussian aggregator, instantiating the dominant baseline mechanism. Abadi et al. further cemented the clipping-plus-Gaussian template and tight accounting ethos, while Mironov’s Rényi Differential Privacy and the subsampled RDP/Analytical Moments Accountant of Wang–Balle–Kasiviswanathan provided the modern, sharp tools for composing iterative mechanisms under sampling.

SGM’s key contribution is to replace the prevailing “isolate-then-add” accounting—treat sketching’s privacy and the Gaussian mechanism independently—with a joint RDP analysis that captures how sketching’s linear randomness reshapes sensitivity and interacts with Gaussian noise. By leveraging RDP composition (and its subsampled variants), SGM quantifies the combined effect of sketch dimension and noise scale across rounds, yielding more flexible and strictly sharper guarantees than naïve composition. In essence, SGM operationalizes the theoretical DP of sketching in the federated setting and integrates it with the standard Gaussian mechanism using state-of-the-art RDP tools, thereby aligning communication efficiency with rigorous, improved client-level privacy.

---
*Generated: 2026-01-06T23:42:48.126472*
