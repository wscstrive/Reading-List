# Generalized Binary Search Network for Highly-Efficient Multi-View Stereo
> idea和motivation很不错
## Abstract
- coarse-to-fine 并没有很好的解决内存问题，作者设计更高效的网络，将MVS视为1D search problem
- 首先将MVS设计为2分类搜索问题即是对概率体切割成2bin，并在切割的正bin（包含正确的深度值的bin）的两边添加一个额外的容忍错误区域，这样我们的网络设置在一个更小范围的深度估计内
 
## Introduction
> 前面的铺垫有点长
- 将MVS设计为一个二分类搜索问题，bin的中间值来表示这段区间，但无法保证选择的bin中gt也在这块里面，错误的判断会在后续进行叠加；1.给这个bin增加错误容忍区域，适当加强这个区间，2.如果出现错误的判断，网络会中止这个像素的前向传播，使他不会影响后续的训练，3.网络在每个阶段都更新参数，而不是所有阶段训练完才更新，更加高效

## Related work
- Traditional MVS
- Learning-based MVS

## Network architecture

<img width="689" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/66d81089-a495-453b-bef7-02eb4ca8e354">

### Image encoding

- FPN中增加了DCN来增加图像的强大表征能力

### cost volume regularization
- 在构建cost volume中采用group-wise correlation，能够更加高效的构建ful cost volume
- 为了聚合所有的cost volume，使用3D CNN来计算weight，并运用加权平均得到最后的fused 3D cost volume

$$
\mathbf{V}(j,\mathbf{p},g)=\frac{\sum_{i=1}^{N-1}\mathbf{W}_i(\mathbf{p})\cdot\mathbf{V}_i(j,\mathbf{p},g)}{\sum_{i=1}^{N-1}\mathbf{W}_i(\mathbf{p})} 
$$

- 之后对V采用3D UNet和softmax得到一种的probability volume P

### Binary search for MVS

- 对深度假设范围中间切一刀，为了确定选择哪一个bin，我们对P进行argmax，然后根据索引选择
- 对于下一阶段，同上面的做法，也就是2分法，但分类存在错误，不稳定
  
### Generalized binary search for MVS

- 为了解决误差堆积和训练问题，作者设计了三个机制来优化这个BiNet，
- 1.Error tolerance bins：在选择的bin两边分别拓展了一部分长度（ETB），作者在补充材料中试着在一边添加ETB发现效果也很好（补充材料没看到）
- 2.Gradient-maksed optimization：解决误差堆积问题，作者通过gt设计了一个gt_mask图，然后去和选择的bin进行比较，gt_mask在bin内部，证明这个像素是valid的，网络只会去更新valid的像素，而不会花费时间在invalid pixel上
### Loss function
- cross-entropy

- 3.Memory-efficient training：过去的方法通常会平均所有阶段的损失总值，需要消耗巨大的内存空间，作者每训练完一个阶段就进行损失函数的计算，节省了内存，更加高效


## Experiments
- 以往的方法首先1200,1600->1024,1280->(downscale)512,640,而作者选择通过随意crop，这反而提高了效果

## Ablation work
- effect of different search strategies
- effect of stage number
- effect of ETB number
- effect of memory-efficient training

*DTU*   *random cropping
| Model | view number | Acc.(mm)↓ | Comp.(mm)↓ | Overall(mm)↓ |
| :-: | :-: | :-: | :-: | :-: |
| GBiNet | 5 | 0.327 | 0.268 | 0.298 |
| GBiNet* | 5 | 0.315 | 0.262 | 0.289 |


*Tanks and Temples*  
| Model | Train view | Mean↑ | Family↑ | Francis↑ | Horse↑ | LightHouse↑ | M60↑ | Panther↑ | Playground↑ | Train↑ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| GBiNet | 7 | 61.42 | 79.77 | 67.69 | 51.81 |61.25 |60.37 |55.87 |60.67 |53.89|

| Model | Train view | Mean↑ | Audiorium↑ | Ballroom↑ | Courtroom↑ | Museum↑ | Palace↑ | Temple↑ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| GBiNet | 7 | 37.32 | 29.77 | 42.12 | 36.30 | 47.69 | 31.11 | 36.93 |

## Thinking
GBi的后处理很好的解决了BiNet留下的问题，但random crop像是一个trick
