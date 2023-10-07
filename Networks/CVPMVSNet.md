# Cost Volume Pyramid Based Depth Inference for Multi-View Stereo(CVPR2020)

> 与CasMVSNet不同种类的级联网络，也是个很有意思的结构，主要是她的准确度已经逼近了传统方法，这个真的很难得，值的一看

## :sparkles: Motivation
- MVSNet的3D CNN内存消耗大，R-MVSNet的GRU时间成本高，Point-MVSNet的时间成本会随着迭代次数呈线性增长，作者提出了代价体金字塔，时间比Point-MVSNet快了6倍。

## Contribution
- 构建更加compact、computational efficient的网络
- 提出的代价体金字塔是基于深度残差搜索范围和网络分辨率
- 速度比其他的网络更快，精确度更高

## Related work
- Point-MVSNet共享similar insight来预测和细化深度图
- PWCNet使用空间代价体获取最优光流估计

## result
 
*DTU*  
| Model | view number | Acc.(mm)↓ | Comp.(mm)↓ | Overall(mm)↓ | 
| :-: | :-: | :-: | :-: | :-: |
| CVPMVSNet | 3 | 0.296 | 0.406 | 0.351 |

*Tanks and Temples*  
| Model | Train view | Mean↑ | Family↑ | Francis↑ | Horse↑ | LightHouse↑ | M60↑ | Panther↑ | Playground↑ | Train↑ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| CVPMVSNet | 5 | 54.03 | 76.50 | 47.74 | 36.34 | 55.12 | 57.28 | 54.28 | 57.43 | 47.54 |

## Network Architecture

<img width="704" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/fb8fdfba-037a-431c-8250-cecc6c209001">

### feature pyramid

- 存在的方法对高分辨率图像进行多尺度特征提取，最后输出低分辨率图
- 首先构成L+1层的图像金字塔，然后采用特征提取网络以1/2为下采样率，对输入的图像进行下采样来获取不同尺度的特征图，相比于传统方法，减少了内存的同时提高了效果

### Cost Volume Pyramid


