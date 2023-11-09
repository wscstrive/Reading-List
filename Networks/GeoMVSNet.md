# GeoMVSNet: Learning Multi-View Stereo with Geometry Perception (CVPR 2022)

> 从全场景方面考虑深度重建。很舒服的文章结构

## Abstract
- 以前的方面忽略了几何信息，导致脆弱的cost matching and sub-optimal results
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


## Methodology

<img width="1027" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/0b50c5b5-2ecd-48e1-99d7-ae6742647684">

### Geometry Awareness for Robust Cost Matching
- 作者对cascade的结构进行了调整，使得每个阶段不共享same constituents；不使用繁重的外部依赖，而是利用网络本身有所有的信息，例如粗阶段的depth estimation和probability volume
- Geometric prior guided feature fusion. 将RGB图、深度图、FPN的特征图通过卷积操作(2*UNet)结合在一起得到精细后的特征，从而aligned不同角度的源特征

$$
Branch(z)=\hat{\mathcal{B}}([D_{\uparrow }^{\ell},\mathcal{B}([I_{0}^{\ell+1},D_{\uparrow }^{\ell}])]) 
$$

$$
F_{0}^{\ell+1}(z)=Fusion(\bar{F}_0^{\ell+1}(z)\oplus Branch(z)) 
$$

- Probablility volume geometry embedding. 将3D'position map'嵌入到cost regularization network中
作者减少了3D UNet的卷积核改为了（kkk->1kk）,提高了效率但缺乏深度维度的信息嵌入（其实效果也是很不错，并没有很大的改动）；为了增强深度信息，作者在对probability的 volume的每个切片进行了depth-aware positional encoding，这样就可以从各个层面去了解深度信息，而不会错乱.confience+full-scene function

### Geometry Enhancement in Frequency Domain
- 上面的方法以及很好的增强了几何感知，但面对infinite sky和边界处，reprojection out of bound而导致增加计算负担。因此作者首先运用了RGB-guided depth refinement，但这种方法会导致深度图-过度拟合-到数据集中的图像，而MVS的目标是match; 运用DFT将深度图转换为2D离散信号并再转为频域问题。低通滤波器可以很好的缓解高频信息（去掉复杂和无法理解的信息，其实就是做了一个mask-like的东西）；随后作者提出了一个curriculum learning，没太理解，提出的比较突兀（应该需要结合代码去理解）

$$
\mathcal{F}^{\ell}(u,v)=\sum_{x=0}^{W-1}\sum_{y=0}^{H-1}D^\ell(x,y)e^{-j2\pi(\frac{ux}{W}+\frac{vy}{H})}   
$$

$$
\tilde{D}^\ell(x,y) =\frac{1}{WH}\sum_{u=0}^{W-1}\sum_{v=0}^{H-1}\tilde{F}^\ell(u,v)e^{j2\pi(\frac{ux}{W}+\frac{vy}{H})}   
$$

### Mixed-Gaussian Depth Distribution Model
- 以往的方法只考虑像素级的深度特征，而没有建模全场景的深度分布（对几何感知很重要）；作者将场景主要分为三类（centered object&orbiting camera; surrounding object&self-rotating camera; aerial photograpth，随后作者采用Gaussian Mixtured Models去结合不同分布的高斯分布。（但最后的结果中作者选择的场景K=1，其实用的就是普通的高斯分布）

$$
p(d|\Omega)=\sum_{i=1}^{K}\omega_{i}\Phi(d|\theta_{i})
$$

$$
\Phi(d|\theta_{i})=\frac{1}{\sqrt{2\pi}\sigma_{i}}exp(-\frac{(d-\mu_{i})^2}{2\sigma_{i}^2} ) 
$$

$$
0\le \omega_{i} \le 1, sum_{i=1}^{K}\omega_i=1 
$$


### Loss Functions

- Pixel-wise classification(regression mode会在早期进入局部循环)

$$
Loss_{pw}=\sum_{z\in\Psi}(-P_{GT}(z)log[P(z)]) 
$$

- Kullback-Leibler Divergence metric

$$
Loss_{dds}=\sum_{m=0,z\in\Upsilon }^{M'}\tilde{p}(z)(log\;\tilde{p}(z)-log\;\mathcal{N}_{GT}(z))
$$

$$
\Upsilon=\Psi \cap \bigcup_{i=1}^{K}((\mu _i-3\sigma _i,\mu _i+3\sigma _i)) 
$$

- - $$Loss=\sum_{\ell =0}^{L}(\lambda_1^\ell Loss_{pw}+\lambda_2^\ell Loss_{dds})$$
