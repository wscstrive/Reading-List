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
