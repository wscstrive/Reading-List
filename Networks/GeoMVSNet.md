# GeoMVSNet: Learning Multi-View Stereo with Geometry Perception (CVPR 2022)

> 从全场景方面考虑深度重建。很舒服的文章结构

## Abstract
- 以前的方面忽略了几盒信息，导致脆弱的cost matching and sub-optimal results
- 从全场景角度出发，整合了geometric clues
- - a two branch geometry fusion network
  - coarse probability volume的嵌入
  - frequency domain filtering
  - 基于Gaussian-Mixture Model的depth distribution similarity loss

## Introduction
- cascade没有考虑早期阶段的valuable insight; dcnn和transformer没有充分探索几何线索
- a two branch fusion network聚合粗阶段的几何先验信息；coarse probability volumes嵌入到finer regularization network，并将正则化的3D改为了2D，轻量级且有效；frequenct domian filtering strategy受到curriculum learning的启发（embed coarse into finer），减少冗余的高频纹理；Gaussian-Mixture Model和PauTa Criterion可以描述隐藏在深度分布的long tailing中太近或太远的信息。


## Related Works
- learning-based mvs
- improvements for mvs in post-pyramid era

<img width="1027" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/0b50c5b5-2ecd-48e1-99d7-ae6742647684">

## Methodology

### Geometry Awareness for Robust Cost Matching
- 作者对cascade的结构进行了调整，使得每个阶段不共享same constituents；不使用繁重的外部依赖，而是利用网络本身有所有的信息，例如粗阶段的depth estimation和probability volume
- Geometric prior guided feature fusion

$$
Branch(z)=\hat{\mathcal{B}}([D_{\uparrow }^{\ell},\mathcal{B}([I_{0}^{\ell+1},D_{\uparrow }^{\ell}])]) 
$$
