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

<img width="698" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/4bc12e5e-6048-4ea6-9b81-64b599cafd22">

## network review
- 作者首先利用特征金字塔网络将输入图像I分别三个阶段，第一阶段分辨率为输入图像的1/16，为最粗糙阶段；第二阶段为1/4；第三阶段为初始图像大小，网络总体被分为三个阶段，每个阶段分别是homography warp, cost volume construction and reguization, depth estimation

## coarse-to-fine manner
- 作者首先会规定网络一个初始深度范围，如以往的方法一样，并对第一阶段进行基本的mvsnet流水线操作，得到了一张1/16的深度图； 
- 随后，在进行第二阶段时，第一阶段输出的深度值规定为第二阶段的初始范围的中心平面，并在上下两侧分别进行拓展范围，然后继续基本的mvsnet流水线；  
- 第三阶段重复第二阶段的过程，但深度范围的中心平面来自于第二阶段的深度图；  
- 通过这样的方式，网络可以将资源更专注于更有意义的深度范围区域，保证效率的同时提高了结果。

这里是随着阶段推进，对单应性变换的一个公式变化

$$
\mathbf{H}_i^d=d\mathbf{K}_i \mathbf{T}_i \mathbf{T}_1^{-1} \mathbf{K}_1^{-1} 
$$

> 网络很依赖于第一阶段的深度图输出，但目前来看这个流水线还没有被其他方法给取代
