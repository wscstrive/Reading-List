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

- 为了考虑空间联系，采用2D U-Net来处理 $S\in R^{W/8\times H/8\times D}$，最终得到的深度平面数降为1,再通过双线性插值和tanh的道出事的隐藏状态$h_{k-1}$，即GRU的迭代从第二阶段开始，第一阶段更像是为第二阶段做参数准备

#### Iterative update

> 用了很多的操作，对一些参数的维度介绍少了一些

- 在后续阶段，我们的逆深度范围计算,并确保 $R_{l-1} < R_{l}$ 以在跟高分辨率上有着更多的深度区间信息去采集

<img width="762" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/e7c6e704-3d4d-476b-8f40-7684dd15dee2">

> $R_l$是每个像素在逆深度范围内的间隔（超参数）

- pixel-wise view weights-> $2\times $ upsampled(整合匹配相似度)-> level-wise 2D U-Net(聚合邻边信息并减少通道到1)
- mathcing similarities-> concatenate 3 levels $\in R^{W/4\times H/4\times (N_1+N_2+N_3)}$-> concatenate S和$D_{k-1]$->x_k(GRU的输入和$h_{k-1}$)

<img width="251" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/3755a55f-38b8-4e13-8088-6a310b025695">

#### Depth prediction（同时适用于初始阶段层）

- 对于输出的隐藏状态-> 2D CNN->softmax-> probabilties P
- 以前的方法提取深度值采用的使用argmax和soft argmax，前者运用概率图和one-hot衡量KL散度，没有考虑离散化的像素（即物理像素外的偏差像素点），后者衡量概率图和gt值的距离，但依赖于单峰分布（受概率分布影响较大），作者结合了两种模式，先运用armax对概率体进行最大值索引，然后通过局部逆范围来生成深度估计

<img width="160" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/1656378d-f238-4d09-ab5a-90d1568a6419">

<img width="301" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/8225af2d-4845-47e1-afe4-669d89403f22">
> 感觉有点像加权平均的感觉

#### Confidence estimation
- hidden state h-> 2D CNN+sigmoid -> confidence C

### Spatial upsampling
- 作者用的是光流估计（RAFT）里的9 nearest neighbors

### Loss function
> 由于文章所设计的小细节很多，整体的损失函数非常的多，对每个部分进行了监督和优化，总体氛围两部分，初始化L+上采样L+（分类+回归+置信）L
- 首先需要计算一个初始深度图（最粗阶段的），先计算逆范围的值，然后倒数过来即可

<img width="637" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/a91665e4-1806-49ff-af73-941fc65db0b9">

-随后我们上采样D_initial获取D，并得到它的逆深度图
<img width="293" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/b4b785e3-a0e7-4579-a81c-68e65fdfdb8b">

<img width="307" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/af7c9dea-e951-4007-94c9-abcf74a5e430">

- initial和上采样的损失函数在建立在逆深度范围内，class是简单的交叉熵，regress是对迭代过程中损失监督，并且值考虑classification的索引已确定了上下限，conf像熵函数的变形操作，C^*也做了一定的限制，保持在超参数控制范围内，
> 总体来说，损失函数是有多个L1损失函数和交叉熵函数构成，但作者把每个不同模块都充分考虑到了，精确到了每个阶段，做的很棒，就是看起来很绕

## Experiments

### details

- interval R_l:$R_1=2^{-7},R_2=2^{-5},R_3=2^{-3}$
- N=4,4,4
- D=256,r=4
- ! one 2080ti（优势）

### Ablation study
> 足够多的消融实验，工作量巨大
- depth prediction
- confidence
- scale of feature
- depth upsampling
- pixel-wise view weight
- number of iterations
- number of views

## Thinking
> 增加的东西蛮多的，工作量也很大，但是正文的排版需要结合代码去看，光看论文容易迷糊，有点跳步
> 最大的优势在于内存消耗很少，但同时模块很多，作者用了很多的2DCNN和一些激活函数，无法确定通过多次的卷积操作会不会对结果造成影响，导致深度图会变得平滑
