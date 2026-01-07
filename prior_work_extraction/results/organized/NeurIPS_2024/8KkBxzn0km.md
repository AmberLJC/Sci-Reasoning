# Prior Work Analysis Report

## Target Paper
**Title:** 8KkBxzn0km
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Saliency-driven Experience Replay (SER) fuses two mature lines of work: replay-centric continual learning and human visual saliency. Replay has proven to be a simple, strong baseline for class- and task-incremental learning—first via exemplar rehearsal as in iCaRL and subsequently through tiny episodic memory studies showing that even small buffers can stabilize learning. DER/DER++ refined this paradigm with logit matching atop memory replay, establishing a versatile backbone into which auxiliary signals can be injected. SER’s core idea is to inject such a signal by leveraging bottom-up visual saliency.

The saliency component stems from classic computational attention (Itti–Koch–Niebur), advanced by modern deep predictors like DeepGaze II that produce human-like fixation maps. Independently, the CNN literature has shown that attention maps can modulate features to improve recognition, as in CBAM’s spatial gating. SER bridges these insights: it treats accurate, pretrained saliency maps as an external, biologically grounded modulation signal applied during experience replay to guide gradient flow and representation updates in non-i.i.d. streams.

Finally, explanation-regularization work (Right for the Right Reasons) demonstrated that aligning model focus with human-relevant regions reduces reliance on spurious features and improves robustness. SER generalizes this to the continual setting: saliency-guided modulation during replay not only mitigates forgetting but also biases representations toward semantically meaningful, human-attended regions, yielding improved resistance to spurious correlations and adversarial attacks while enhancing state-of-the-art replay-based CL methods.

---
*Generated: 2026-01-06T23:33:35.534526*
