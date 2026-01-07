# Prior Work Analysis Report

## Target Paper
**Title:** Ha6RTeWMd0
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

SAM 2’s core contribution—promptable segmentation that seamlessly spans images and videos with real-time streaming memory—emerges from three converging lines of prior work. First, Segment Anything (SAM) established promptable mask prediction and a scalable data-engine pipeline; SAM 2 generalizes this paradigm to time by retaining flexible prompts while collecting a massive video segmentation corpus via interactive annotation. Second, the video object segmentation community contributed the essential idea of memory-based temporal propagation: STM introduced key–value memories to carry segmentation cues across frames, while AOT demonstrated how transformers can associate current-frame tokens with stored memories for multi-object tracking and segmentation. SAM 2 internalizes these ideas into a streamlined, end-to-end transformer equipped with a streaming memory that updates with user prompts and past frames, enabling accuracy with far fewer interactions. Third, advances in transformer design for dense prediction and efficient video processing shaped SAM 2’s architecture: Mask2Former’s masked-attention mask decoding influenced a simple, general segmentation head, and MeMViT’s persistent memory/state provided a blueprint for low-latency, long-horizon video processing. Finally, the interactive prompting tradition from DEXTR furnished the human-in-the-loop interface—points and boxes—that SAM 2 leverages across both modalities. Together, these works directly underwrite SAM 2’s scalable data engine, promptable transformer with streaming memory, and strong accuracy-speed trade-off in images and videos.

---
*Generated: 2026-01-06T23:42:48.101337*
