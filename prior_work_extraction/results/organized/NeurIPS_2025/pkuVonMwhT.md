# Prior Work Analysis Report

## Target Paper
**Title:** pkuVonMwhT
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Neural Atlas Graphs (NAGs) fuse two historically distinct lines of work: 2D-editable neural atlases and 3D object-centric scene graphs. On the atlas side, Deferred Neural Rendering (Thies et al., 2019) established neural textures as view-dependent 2D atlases that are easy to author and edit. Dynamic view-synthesis methods such as NSFF (Li et al., 2020) and DynIBaR (Li et al., 2023) demonstrated that dynamic scenes benefit from layered decompositions and occlusion-aware compositing, but they typically rely on a coarse two-layer (foreground/background) model that struggles with multiple occluding objects.
On the compositional side, GIRAFFE (Niemeyer & Geiger, 2021) and related object-centric NeRFs (e.g., Object-NeRF, 2021) showed that representing scenes as sets of transformable object nodes supports manipulation and 3D ordering. Neural Scene Graphs (Ost et al., 2021) further grounded this idea in the autonomous-driving domain, leveraging masks and bounding boxes to learn object nodes as implicit volumes—powerful but difficult to edit consistently.
NAGs combine these threads by making every scene-graph node a view-dependent neural atlas. This preserves the 2D editability and high resolution of atlas-based methods while enabling true multi-object composition with explicit 3D ordering and interactions from scene-graph models. Finally, the practicality of fitting many high-resolution nodes at test time is underpinned by efficiency advances such as Instant-NGP (Müller et al., 2022), which popularized fast encodings for neural fields. Together, these works directly motivate NAGs’ core contribution: a hybrid scene-graph-of-atlases representation that is both editable and capable of modeling complex dynamic scenes.

---
*Generated: 2026-01-07T00:21:32.337208*
