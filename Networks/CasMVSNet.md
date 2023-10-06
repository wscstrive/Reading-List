# Cascade Cost Volume for High-Resolution Multi-View Stereo and Stereo Matching (CVPR2020)

> 最喜欢的mvs框架，简单而充满了潜力。

## :sparkles: Motivation
- 以往的方法由于3D cost volumes的限制，他们会选择下采样特征图以减少后续任务的内存和时间损耗，但也因此限制于低分辨率的输出。本方法选择基于特征金字塔以由粗到细的方式构建3D代价体，并且通过前一阶段的输出在逐渐narrow每个阶段的深度范围，最终达到高分辨率的输出。

## Contribution
- :dizzy: 开启了由粗到细的Cascade MVS时代
- 再由粗到细的过程中，通过逐渐narrow深度范围来让确保网络是中专注于更加有意义的区域

## result
 
*DTU*  
| Model | view number | Acc.(mm)↓ | Comp.(mm)↓ | Overall(mm)↓ |
| :-: | :-: | :-: | :-: | :-: |
| CasMVSNet | 3 | 0.325 | 0.385 | 0.355 |

*Tanks and Temples*  
| Model | Train view | Mean↑ | Family↑ | Francis↑ | Horse↑ | LightHouse↑ | M60↑ | Panther↑ | Playground↑ | Train↑ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| CasMVSNet | 5 | 56.42 | 76.36 | 58.45 | 46.20 | 55.53 | 56.11 | 54.02 | 58.17 | 46.56 |

# Network Architecture

