# MVSNet: Depth Inference for Unstructured Multi-View Stereo (ECCV 2018)

- Task
> Infer the depth map for the reference image by one reference image align with several source images
- :sparkles: Motivation
> Traditional MVS rely on hand-crafted similarity metric and engineered regularization result in can't handle challenge scenes. Rencent MVS that using CNN to improve quanlity, but theses methods fails to fully use multi-view information and restricts by huge memory consumption of 3D volume.
- Key insight
> Encode camera geometries through differentiable homography warping to build 3D cost volume  
> Enable end-to-end training  
> Adapt arbitrary number of input images  
> Multi-scale 3D convolutions and regree inital depth map  
> refine the depth map

- Contribution
> 1. 3D cost volume is built upon the camera frustum
> 2. decouple MVS to per-view depth map estiamtion, which make large-scale reconstruction
> 3. adapt arbitrary number of input images  
- result
 
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

- The paper says that downsampling can embed initial neighbor information into the feature channel of the final output and won't lose useful context information (this needs to be discussed, I feel that an fpn design like cascade can better retain the initial information)

### Cost Volume constrution

[Differentiable homography](Preliminaries/Homography.md)(i think this equation that in paper is wrong)

Let me talk about my own views, this operation is more like to say that first establishing a three-dimensional space that can tolerate the feature body, and then putting the source feature body into it. Through using internal and external parameter of the two camera coordinate systems to transformation, and then using sampling operation fills the gaps. In a sense, the source feature volume at this time has become a feature volume from reference camera's perspective, but the information contained comes from the source feature volume.->feature volume is add depth demension.

<img width="427" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/97afc739-6598-4957-83ff-3ae02522de24">

Cost Metric

To adapt arbitrary number of input views, author use variance-based method to build a cost volume. Variance provide information about the feature differences.

<img width="476" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/5e6d9370-ac21-4f8a-9968-171d305a1850">

There are two improvements in subsequent methods. One is to increase the importance weight of different views, and the other is to adopt the group correlation cost measurement method in pwcnet.

### Depth Map
The paper uses 3D-CNN to fuse spatial information of the cost volume to ensure that each pixel information will take more consideration of 3D information. In addition, 3D-CNN will reduce the feature channel of the cost volume from 32 to 1.   
Personally, I feel that this step is a bit like a fully connected classification method. For each depth plane, we compress all feature channel information into a depth plane, totally N depth plane, and use the characteristics of deep learning to update it to the best attributes , thereby judging which plane this voxel is more suitable to be classified on.

Then we will get a probability initial volume():

<img width="305" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/227ba799-ceb5-4f14-b795-d5be1df7c089">

Using softmax or argmax to generate final probability volume. Normalization to indicate which layer has greater probability is more intuitive than the initial probability volume:

<img width="309" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/a8b2f2ee-f42a-4b4e-a01f-b2cd8f70adce">

Finally, author compute the expectation value along the depth direction

<img width="164" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/a6a099e3-2ab4-4493-8ec4-8388dc4835c3">

### Loss
Simple difference calculation between results and real ground truth, nothing novel

<img width="477" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/3cd9302d-9063-4a34-ab54-2d2d8eb09430">
