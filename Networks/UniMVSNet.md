# Rethinking Depth Estimation for Multi-View Stereo: A Unified Representation

## Abstract
- 提出了一个结合了回归和分类的统一focal loss

## Introduction
- MVS的损失函数主要分为regression（期望值计算）和clasification（argmax）两部分，回归可以获得亚像素的深度值，但是作为认为网络更需要的是直接获取深度值而不是通过权重的合并操作，因为不同的权重可能也会合并成相同的深度值，这种歧义会导致网络变得更复杂；分类网络无法获取更精确的深度值，但是他可以直接的道最有的深度估计，这确保了mvs的鲁棒性，概率体也可以直接反应置信度，这个回归网络就很难做到
- 作者融合了两者的优点，由于深度值离GT越近越有价值，而其他的深度值只会对深度估计产生负效应，作者受到这个启发，认为估计所有深度平面的权重是冗余的，我们只需要回归最有深度估计即可，总的来说，他的方法就是在找到最有深度平面后加了一个偏差值，并对这个偏差进行了处理来达到唯一结果

## Related work
- Traditional MVS
- Learning-based MVS

## Network architecture

<img width="672" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/e6e85853-4cf9-4895-ad3c-e62422cf2d03">

### Unified depth representation
- regression方法容易过拟合；classification方法无法预测准备的深度值；作者结合了两者的优点，首先用分类来分类最有的深度估计平面，然后回归来接近（偏差值）
- - Unity generate: generate the gt unity from gt depth, 首先给定gt深度值和深度估计值，将索引限定在图像内部和深度范围内部，当索引的平面到达真实值附近的时候并在他下一个索引之前（肯定是比他大的，因为索引是从小到大取的），那么我们就计算这个U的概率值（贴近这个平面的概率，离得越近，概率越大）

<img width="325" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/faf72884-ae5e-4a36-a8ca-814b25ee8cff">

- - Unity regression: regress the depth from the estimated unity,首先给定estimated unity U（前面Unity generate测的0和值）和深度估计值，我们首先找到有值的索引，然后在判断这个索引所在的深度值，如果索引在范围内部，那么我们就确定好他的间隔，offset的计算就是吧上述介绍的U的远近概率反过来，变成估计值占整个间隔的比例（概率越小，证明离得越近），然后✖️间隔值得到他的真值，最后的深度估计就是深度平面值加上这个索引值

<img width="336" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/7c921f89-c10b-4a9b-9718-deb81a8a7c28">

> unity generate找到每个像素点所深度估计值离哪个深度平面最近，并判断他的概率（贴近这个平面的概率）；unity regreesion是定义到这个索引平面和概率值，并反转得到这个（1-概率值）* 间隔所得的偏置

### Unified focal loss
- 作者沿用了focal loss，认为多层深度平面，但最终深度值只有一个，我们应该把注意力放在这一个上面，而减少其他平面层的影响和注意力，u是estimated unity，q是lab

<img width="486" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/c0f73081-273b-4ad7-a1f4-82f75649d8af">

- 由于q是lab值，并不适合我们的回归值，所以作者进一步改进了这个公式把它更贴合于回归的输入，作者增加了二元交叉熵，以满足回归值输入依然公式成立，将两分类问题转化为回归的公式
  
<img width="504" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/33c9d9aa-2dd1-49aa-90a9-62aba760c91c">

<img width="1200" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/4a3f63e6-2a6c-47bd-b9be-4b1dc773fc2a">

- 但是作者又发现了新的，这个公式忽略gt和深度估计值之间的关联，即绝对值内部的正负会直接影响到结果，作者将绝对的误差转为绝对的误差

<img width="528" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/beefd964-dab3-40a5-bfa8-c70ab5919fbd">

- 此外，注意力这个分数的取值范围会趋向于正无穷，因此加上个sigmoid函数来规定限制

<img width="526" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/8634eafd-9fdb-4255-ae85-2e7bc5c71672">

### UniMVSNet

- 作者对每一阶段都进行了计算，并给了超参数，最后得出最后的损失函数（也算是本文唯一的创新，简单但有效）

## Experiments
> 超参数有点多
- $\alpha^+$ = 1, $\alpha^-$ = 0.75,0.5,0.25
- $S_5^+ \in [1,3)$, $S_5^- \in [0,1)$, $\gamma$=2,1
  
## Ablation studies

- Benefits of unification
- Benefits of UFL
- Regression finetuning and less data

*DTU*  
| Model | view number | Acc.(mm)↓ | Comp.(mm)↓ | Overall(mm)↓ |
| :-: | :-: | :-: | :-: | :-: |
| UniMVSNet | 5 | 0.352 | 0.278 | 0.315 |

*Tanks and Temples*  
| Model | Train view | Mean↑ | Family↑ | Francis↑ | Horse↑ | LightHouse↑ | M60↑ | Panther↑ | Playground↑ | Train↑ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| TransMVSNet | 5 | 64.36 | 81.20 | 66.43 | 53.11 | 63.46 | 66.09 | 64.84 | 62.23 | 57.53 |

| Model | Train view | Mean↑ | Audiorium↑ | Ballroom↑ | Courtroom↑ | Museum↑ | Palace↑ | Temple↑ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| TransMVSNet | 5 | 38.96 | 28.33 | 44.36 | 39.74 | 52.89 | 33.80 | 34.63 |

## Thinking
为数不多纯公式推导的论文，算是我比较喜欢的论文形式，而且加的东西确实有道理，而且模块不影响内存占用，是个很不错很值得学习的论文，但是感觉不好改进,且超参数设置的很多
