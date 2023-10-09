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
- 首先氛围三个不同尺度，最大尺度进行利用可变形卷积来丰富语义信息，并将另两个尺度进行采样到原分辨率上，最后合并在一起，最后feature channels=16+8+8

$$
\mathrm{f}'(\mathrm{p})=\sum_{k} w_k\cdot \mathrm{f}(\mathrm{p}+\mathrm{p}_k+\Delta \mathrm{p}_k)\cdot \Delta m_k  
$$

### Inter-view Adapative Aggregation
