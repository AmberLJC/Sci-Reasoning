# Prior Work Analysis Report

## Target Paper
**Title:** UnslcaZSnb
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

DiCo’s key innovation—replacing global self-attention with a fully convolutional diffusion backbone while preserving expressivity and scaling—stands on two converging lines of prior work. On the diffusion side, DDPM introduced the denoising objective with U-Net ConvNets, and ADM showed that carefully engineered conv U-Nets could scale to state of the art. DiT then reframed the denoiser as a Transformer, revealing strong scaling but incurring high compute; DiCo takes DiT as both target and diagnostic, arguing that DiT’s attention predominantly captures local structure and is thus over-provisioned. This contention is grounded theoretically by work showing self-attention can reduce to (dynamic) convolution, and empirically by the success of local/windowed vision Transformers.
On the architecture side, ConvNeXt demonstrated that modernized ConvNets—with depthwise separable convolutions, larger kernels, and simplified designs—can rival ViTs, providing a template for scalable conv-based denoisers. Yet ConvNets historically suffer higher channel redundancy than Transformers. Here, channel attention mechanisms are pivotal: SE-Nets established channel-wise recalibration to enhance informative channels, while ECA-Net showed how to realize this efficiently without heavy MLPs. DiCo integrates these insights into a compact channel attention module that activates more diverse channels, mitigating redundancy and restoring performance lost when naively replacing attention with convolution—yielding a scalable, efficient, all-conv diffusion model.

---
*Generated: 2026-01-07T00:05:12.557558*
