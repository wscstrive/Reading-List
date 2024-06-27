# TransMVSNet: Global Context-aware Multi-view Stereo Network with Transformers

## Abstract
- 作者将MVS视为沿着极线一对多的匹配任务，并首次使用Transformer应用于MVS（但我记得之前有一篇MVSTR好像比他早，whatever）
- FMT：self-attention（图像内部的上下文信息）和cross-attenion（图像之间的特征交互）->只针对最粗糙阶段
- ARF：为了更好的过渡到FMT中，作者对FPN增加了可变形卷积操作
- pair-wise feature correlation：作用更像是减少内存和时间

## Introduction

- MVS的本质是沿着极线的一对多的匹配任务，MVS的baseline存在两个问题：（1）缺少全局特征；（2）特征提取只是简单的提取源视图特征，潜在的图像间的联系没有考虑在内
- 最近的transformer在特征匹配任务有着优异的成果，作者遵循LoFTR采用了inter和intra-attention来进行分别的特征提取（其实基本没有变化）
- ARF和pari-wise feature correlation可以给FMT更好的过渡，并取得了完整度很好的效果

## Related work
- learning-based MVS
- Transformer for feature matching

## network architecture

<img width="659" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/4dbf8831-eb1c-4d65-ae92-444548fd1988">

### network overview 
- casmvsnet的baseline

### feature matching transformer

- dot-product attention和linear-attention(可以将常见的attention时间复杂度降为O（n）)
- intra-attenion是对图像内部的全局上下文信息的获取和inter-attention是获取不同图像见的特征交互信息，对于inter但是作者没有去更新参考图像的特征图，估计是怕早生影响到参数图像（4intra-att*4inter-att），由于无法拓展到更精细阶段，作者运用了上采样和跳跃连接进行处理
- ARF是在FPN的上采样阶段采用了可变形卷积，以更好的适合FMT的应用
- 将transformed后的特征图相关联得到c（<>这个我不知道是什么操作），然后对c进行max在乘以它本身，有点类似于aarmvsnet里面的inter-view module，但是有些不同，但是总体差别不大

$$
c_i^{(d)}(\mathrm{p})=<\mathcal{F}_0(\mathrm{p}),\hat{\mathcal{F}}_i^{(d)}(\mathrm{p})>
$$

<img width="245" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/20224dc7-3b1e-4157-9e7c-604978805942">

### Loss function
- 由于作者考虑深度平面有很多，但真实参数只有一个，因此减少错误平面的监督，重点关注在真实参数上，作者做了一点改变，作者用了最近火热的focal loss

$$
\mathcal{L}=\sum_{\mathrm{p}\in \Psi}-(1-P^{(\tilde{d})}(\mathrm{p}))^{\gamma}\mathrm{log} (P^{(\tilde{d})}(\mathrm{p}))
$$
- 对于训练中 $\tilde{d}$ = 0, 评估中 $\tilde{d}$ = 2

## Experiments
- 8*2080ti, 结果不好没道理的

## Limitations
- attention限制了网络在很多方面的限制，计算成本和时间成本也比较高

*DTU*  
| Model | view number | Acc.(mm)↓ | Comp.(mm)↓ | Overall(mm)↓ |
| :-: | :-: | :-: | :-: | :-: |
| TransMVSNet | 5 | 0.321 | 0.289 | 0.305 |

*Tanks and Temples*  
| Model | Train view | Mean↑ | Family↑ | Francis↑ | Horse↑ | LightHouse↑ | M60↑ | Panther↑ | Playground↑ | Train↑ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| TransMVSNet | 5 | 65.52 | 80.92 | 65.83 | 56.94 | 62.54 | 63.06 | 60.00 | 60.20 | 58.67 |

| Model | Train view | Mean↑ | Audiorium↑ | Ballroom↑ | Courtroom↑ | Museum↑ | Palace↑ | Temple↑ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| TransMVSNet | 5 | 37.00 | 24.84 | 44.59 | 34.77 | 46.49 | 34.69 | 36.92 |

## Thinking
transofmer限制了网络拓展到更精细阶段，事实上比起在粗糙阶段的transformer应用，精细阶段更加重要，粗糙阶段的特征增强会通过阶段的递进逐渐失去增强的优势。
