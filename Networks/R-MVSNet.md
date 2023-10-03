# Recurrent MVSNet for High-resolution Multi-view Stereo Depth Inference(CVPR2019)


## :sparkles: Motivation
- 使用GRU将3D-CNN的三次方计算量转换为深度方向的序列形式的2次方

## Contribution
- 减少内存消耗
- :dizzy:	为后续循环神经网络处理mvs提供了新思路

## Think
- 💫将 3D 转换为一系列 2D 卷积运算，牺牲时间换内存。 虽然内存消耗问题得到了解决，但它引发了新的时序问题，而且损失了3D-CNN中对空间感知的信息的获取，但分解并处理 3D CNN 是一个很好的切入点。

## result
 
*DTU*  
| Model | view number | Acc.(mm)↓ | Comp.(mm)↓ | Overall(mm)↓ |
| :-: | :-: | :-: | :-: | :-: |
| R-MVSNet(D=256) | 3 | 0.385 | 0.459 | 0.422 |
| R-MVSNet(D=512) | 3 | 0.383 | 0.452 | 0.417 |

*Tanks and Temples*  
| Model | Train view | Mean↑ | Family↑ | Francis↑ | Horse↑ | LightHouse↑ | M60↑ | Panther↑ | Playground↑ | Train↑ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| R-MVSNet | 5 | 43.48 | 55.99 | 28.55 | 25.07 | 50.79 | 53.96 | 50.86 | 47.90 | 34.69 |

## Network Architecture

<img width="703" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/7a349e37-69ea-4e08-aa4e-f0541bf4b6d3">

