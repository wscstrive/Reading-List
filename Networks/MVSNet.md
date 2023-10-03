# MVSNet: Depth Inference for Unstructured Multi-View Stereo (ECCV 2018)

## :sparkles: Motivation
- 传统的 MVS 依赖于手工设计的相似性度量和工程正则化，导致无法处理具有挑战性的场景。 最近的MVS使用CNN来提高质量，但这些方法未能充分利用多视图信息并且受到巨大内存的限制

## Contribution
- 利用单应性变换构建3D代价体
- 将三维重建问题分解为逐视图的深度估计问题，并且是端到端的网络
- 可以更加适应不同的输入图像数量
- 给MVS方向提供了一个整体流程，不管后续的recurrent-mvs还是casacde-mvs都是基于这个流程进行改进的，整体框架没有变换

## result
 
*DTU*  
| Model | view number | Acc.(mm)↓ | Comp.(mm)↓ | Overall(mm)↓ |
| :-: | :-: | :-: | :-: | :-: |
| MVSNet | 5 | 0.396 | 0.527 | 0.462 |

*Tanks and Temples*  
| Model | Train view | Mean↑ | Family↑ | Francis↑ | Horse↑ | LightHouse↑ | M60↑ | Panther↑ | Playground↑ | Train↑ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| MVSNet | 5 | 43.48 | 55.99 | 28.55 | 25.07 | 50.79 | 53.96 | 50.86 | 47.90 | 34.69 |


## Network Architecture

<img width="1399" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/e5c74cad-d95f-447e-bca9-53b037e8d098">

### Feature extract
- Input: N * RGB images with 3✖️H✖️W resolution

<img width="323" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/187b7c61-54cd-4b8c-8480-0d3a234a0423">

- Ouput: feature maps with C✖️H/4✖️W/4 resolution

<img width="360" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/79b5544b-8ccd-4832-b4be-0fa5ec031447">

- Feature extraction consists of eight 2D convolutional neural networks, and downsampling operations x2 are performed on the 3rd and 6th layers. After each convolutional layer, BN and ReLu are used to improve the stability of the network.

- The paper says that downsampling can embed initial neighbor information into the feature channel of the final output and won't lose useful context information (this needs to be further discussed, I feel that an FPN design like cascade can better retain the initial information)

### Cost Volume constrution

[Differentiable homography](Preliminaries/Homography.md)(i think this equation that in paper is wrong)

> 这个操作更像是说，先建立一个可以容纳特征体的三维空间，然后将源特征体放入其中。 通过利用两个相机坐标系的内参数和外参数进行变换将源特征体变换到参考相机角度下的特征体，并利用采样运算填补了变换后的空缺。 从某种意义上说，此时的源特征体已经成为参考相机角度的特征体，但其中包含的信息来自于源特征体。->特征体添加了深度维度。

<img width="427" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/97afc739-6598-4957-83ff-3ae02522de24">


- To adapt arbitrary number of input views, author use variance-based method to build a cost volume. Variance provide information about the feature differences.

<img width="476" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/5e6d9370-ac21-4f8a-9968-171d305a1850">

> 后续方法有两个改进。 一是增加不同观点的重要性权重，二是采用pwcnet中的分组相关成本衡量方法。

### Depth Map
- The paper uses 3D-CNN to fuse spatial information of the cost volume to ensure that each pixel information will take more consideration of 3D information. In addition, 3D-CNN will reduce the feature channel of the cost volume from 32 to 1.   
> 个人感觉这一步有点像全连接分类方法。 对于每个深度平面，我们将所有特征通道信息压缩到一个深度平面，总共N个深度平面，并利用深度学习的特性将其更新为最佳属性，从而判断该体素更适合分类在哪个平面上。

Then we will get a probability initial volume:

<img width="305" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/227ba799-ceb5-4f14-b795-d5be1df7c089">

Using softmax or argmax to generate final probability volume. Normalization to indicate which layer has greater probability is more intuitive than the initial probability volume:

<img width="309" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/a8b2f2ee-f42a-4b4e-a01f-b2cd8f70adce">

Finally, author compute the expectation value along the depth direction

<img width="164" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/a6a099e3-2ab4-4493-8ec4-8388dc4835c3">

### Loss
Simple difference calculation between results and real ground truth

<img width="477" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/3cd9302d-9063-4a34-ab54-2d2d8eb09430">
