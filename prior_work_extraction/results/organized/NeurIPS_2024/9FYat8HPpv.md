# Prior Work Analysis Report

## Target Paper
**Title:** 9FYat8HPpv
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

SpikeReveal’s core idea—recovering a temporally resolved sequence from a single real blurry image by leveraging spike streams in a self-supervised manner—rests on two pillars: a physics-grounded formation model and robust learning that avoids synthetic-to-real pitfalls. The EDI framework (Pan et al., 2019) is the most direct antecedent, explicitly tying a blurry exposure to latent frames via high-rate asynchronous measurements; SpikeReveal substitutes events with spike streams and builds an analogous spike–blur–latent relationship. In parallel, learning-based event reconstruction (Rebecq et al., 2019) established that sparse high-frequency signals carry sufficient information to reconstruct dense intensity video, while Time Lens (Tulyakov et al., 2021) showed how such signals can synthesize high-FPS content between frames—both informing SpikeReveal’s use of spikes as temporal scaffolding to unfold sequences from a single blur.

On the sensor side, prior spike-camera work (Zheng et al., 2021) modeled spike generation and demonstrated supervised spike-to-intensity recovery, directly preceding SpikeReveal’s move to self-supervision and joint modeling with the blur image. Finally, mainstream deblurring literature and datasets (Nah et al., 2017; Rim et al., 2020) exposed generalization issues from synthetic to real blur, motivating SpikeReveal’s self-supervised, cascaded training on real inputs with a reblurring-style consistency rooted in its spike-guided formation model. Together, these works converge on SpikeReveal’s key contribution: a theoretically grounded, self-supervised framework that exploits spike streams to unlock temporally coherent sequences from real blurry inputs.

---
*Generated: 2026-01-06T23:39:42.966966*
