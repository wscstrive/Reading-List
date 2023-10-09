# AA-RMVSNet: Adaptive Aggregation Recurrent Multi-view Stereo Network

## Abstract
- 为了提高thin objects和大low-textured surfaces，intra-view aggregation module通过使用context-aware convolution和multi-scale aggregation来提取图像特征
- 为了适应不同复杂场景，inter-view cost volume aggregation module可以适应pixel-wise view aggregation, 它可以对所有views有更好的匹配
- 对于3D CNNs, 我们使用recurrent structure来允许更高分辨率和更精细的假设平面扫描

## Introduction
- 2DCNN的固定感受野的局限；context-aware feature没有得到充分利用；像素可视化问题需要得到关注（遮挡问题）
- intra-view aggregation module将以特征聚合到多尺度区域来丰富纹理信息
- inter-view aggregation module应用在cost volume aggregation进行更好的多视图匹配以克服遮挡问题
- LSTM减少内存需求

### contributions
- intra-view feature aggregation module
- inter-view cost volume aggregation module

## Related work
- Traditional MVS
- Learning-based MVS

## Network architecture

<img width="690" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/e87b51ae-9c3e-4cf2-a5fb-195677a4c238">

### Intra-view Adaptive Aggregation

<img width="323" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/a659d541-3942-4fc9-94ad-5ff408023198">

- 首先氛围三个不同尺度，最大尺度进行利用可变形卷积来丰富语义信息，并将另两个尺度进行采样到原分辨率上，最后合并在一起，最后feature channels=16+8+8

$$
\mathrm{f}'(\mathrm{p})=\sum_{k} w_k\cdot \mathrm{f}(\mathrm{p}+\mathrm{p}_k+\Delta \mathrm{p}_k)\cdot \Delta m_k  
$$

### Inter-view Adapative Aggregation

<img width="319" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/4c8295b4-1ffc-4cff-9fd0-6a90eaccb6e2">

- 作者两两特征体比对，然后进行得到不同代价体的权重信息，以考虑哪个视图值得被优先考虑，从而减少噪声印象，提高遮挡区域的可见性信息

$$
\mathrm{C}^{(d)} = \frac{1}{N-1} \sum_{i=1}^{N-1}[1+w(\mathrm{c}_i^{(d)})]\odot \mathrm{c}_i^{(d)}   
$$

- 权重+1位了避免过度平滑

### Recurrent Cost Regularization
将 <img width="93" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/1286f586-2954-46bb-b5a5-4b2faae152cc">进行卷积层切割成4个响亮，然后让LSTM处理，得到最后的v
> 这一步骤说的很随意，没有讲清楚，如何切割，怎么划分？不看代码全是问号

### Loss Function
如RMVSNet一样一个交叉熵损失函数来考虑像素级概率分布问题

## Experiments
- H，W，D，N=160，120，192，7（dtu）
- H，W，D，N=800，600，512，7（dtu）

## Result

*DTU*
|Method|Views|Acc|Comp|Overall|
|:-:|:-:|:-:|:-:|:-:|
|AA-RMVSNet|7|0.376|0.339|0.357|

*Tanks and Temples*
| Model | Train view | Mean↑ | Family↑ | Francis↑ | Horse↑ | LightHouse↑ | M60↑ | Panther↑ | Playground↑ | Train↑ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| AA-RMVSNet | 7 | 61.51 | 77.77 | 59.53 | 51.53 | 64.02 | 64.05 | 59.47 | 60.85 | 54.90 |

## Thinking

inter-view模块对后续在代价体构建方面起了很多的作用，收到后续工作的大力使用，从不同视图的重要性差异去减少噪声图像的影响
