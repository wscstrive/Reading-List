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
- Input: RGB images with 3✖️H✖️W resolution
- Ouput: feature maps with C✖️H/4✖️W/4 resolution


### Cost Volume constrution
  
### Depth Map
