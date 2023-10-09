# Cost Volume Pyramid Based Depth Inference for Multi-View Stereo(CVPR2020)

> 与CasMVSNet不同种类的级联网络，也是个很有意思的结构，主要是她的准确度已经逼近了传统方法，这个真的很难得，值的一看

## Abstract
build a cost volume pyramid  in a coarse-to-fine manner

- 一个紧凑、轻量级、高效的网络并允许估计高分辨率深度图
- 作者首先在最粗糙阶段通过对前向平面层的均匀采样构建初始cost volume, 随后根据给定的深度估计使用pixelwise depth residual来迭代构建新的cost volume来perform depth map refinement.
- 构建cost volume pyramid比Pointmvsnet在点云上更加高效； 同时时间快6倍

## Introduction
> while traditional methods before deep learning era have ..., they still suffer from... 这段话的过渡方式学习到了

- 传统方法遭在朗伯表面好，但在光照变化、低纹理区域和反射会有不可靠的匹配结果
- MVSNet的内存需要是cubic->(hand hign resolution)R-MVSNet更长的run-time->(efficient network)PointMVSNet随着迭代次数线性增长run-time

- CVPMVSNet在最粗阶段的采样深度下构建compact cost volume->(next level)当前阶段的深度估计的另句进行残差深度搜索，使用3DCNNs构建partial cost volume来正则化，速度是6x faster than SOTA network
- 网络在predict&refine方面share similar insight with PointMVSNet，但有四点不同
  - 网络构建的cost volume是基于常规grid，在runtime比点云更快
  - cost volume基于深度sample和图像分辨率的关系
  - 多尺度的3DCNN来覆盖更大的感受野，在残差深度估计的剧本上更加平滑
  - 我们的input和output可以保持小分辨率不变


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

- 存在的方法对高分辨率图像进行多尺度特征提取，最后输出低分辨率图，作者提出的方法在低分辨率有着更多有用的信息
- 首先构成L+1层的图像金字塔，然后采用特征提取网络以1/2为下采样率，对输入的图像进行下采样来获取不同尺度的特征图，相比于传统方法，减少了内存的同时提高了效果

### Cost Volume Pyramid

- 首先在最粗糙的极端进行着，和MVSNet一样的homo_warp和基于variance-based cost volume construction操作
- 对于不同尺度的金字塔连接，作者运用前一阶段的深度图上采样，并运功空间cost volume生成一个深度残差值。作为认为相邻像素的深度位移是相关的，常规的3D卷积可以给深度残差估计提供更有用的信息
- 得到上一深度图的上采样（D↑），然后另深度残差深度间隔为（d=s/M），作者将不同深度平面上的点投影到了各个视图上，然后在采用基于varance-based cost volume construction进行构建
> s为深度搜索范围，M是深度平面数量

<img width="320" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/b965bbd2-80b0-4a1f-a5e2-da5e9305e04c">

### Depth Map inference

- 作者认为普通的采样操作会让采样点的距离过近而无法提供有效信息，作者采用投影参考点到源视图再反投影回参考图像优化采样点的位置
- 粗阶段的深度图如常规一样，精细阶段是通过上一阶段的上采样深度图加上该阶段的期望值计算

### Loss Function
简单的L1损失函数

## Experiments

- GT：下采样到160✖️128
- pyramid levels：2
- depth hypothese：48（coarsest），8

## Ablation study
- training pyramid levels
- evaluation pixel interval settings

# Thinking
在没看代码的前提，没搞清楚迭代和金字塔层数的关系
