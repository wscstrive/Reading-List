# IterMVS: Iterative Probability Estimation for Efficient Multi-View Stereo
来自于ETH，和patchmatchnet属于同一个作者，主打以小内存来进行训练

## Abstract
- 引入了GRU-based estimator，通过将像素级的概率分布嵌入到隐藏层中，并进行了多次迭代操作来匹配多尺度的信息
- 损失函数运用了传统分类和回归结合的方法

## Introduction
- 介绍MVS；传统方法 $\to$深度学习方法；MVSNet的baseline介绍 $\to$ 两个MVS分支（cascade MVS限制了粗阶段导致的错误流入的细节段的不可逆 & Recurrent MVS增加了时间）

- Contributions
- - 将概率分布嵌入到GRU的隐藏状态中 $\to$ 不需要网络一直在内存中；每个阶段的多尺度信息的迭代来更新深度分布；同分辨率下更大的搜索范围并保持在整个范围内的跟踪
  - 更高效的深度估计策略，融合了分类和回归的方法（loss function）

> 过去的工作描述过多了

## Related work
- Traditional MVS.
- Data-driven MVS. 就是learning-based MVS
- Iterative Update.

## Network Architecture

<img width="603" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/f1360776-88cd-4119-a63e-b81b303d41f3">

### Multi-scale feature extractor
-输入的图像分为三个阶段，以1/2作为下次下采样率，通道数分别为16，32，64

### GRU-based probability estiamtor
- 在最粗糙尺度上，首先利用differentiable homography warping，深度范围采用inverse深度范围（不规则的采样假设对大尺度场景更有效），再利用分组相似性度量来集成参考和源图像的相似性s(2-views)，我们再利用2DCNN空啊美聚合信息并将Gto1，使用softmax沿着深度方向生成概率体
- 概率体可以为网络提供可视化信息（AA-RMVSNet中的inter-view module），但作者的权重就是简单的对概率体在深度方向上进行max，然后通过加权平均得到最终的相似性S(multi-views)

$$
\mathrm{w}_i(\mathrm{p})=max(\mathrm{P}_i(\mathrm{p},j)\mid j=0,1,...,D_1-1)
$$

<img width="255" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/7a2058c5-bb80-482e-abad-7ef4c11c6a68">

- 为了考虑空间联系，采用2D U-Net来处理 $S\in R^{W/8\times H/8\times D}$，最终得到的深度平面数降为1,再通过双线性插值和tanh的道出事的隐藏状态，即GRU的迭代从第二阶段开始，第一阶段更像是为第二阶段做参数准备
