# Recurrent MVSNet for High-resolution Multi-view Stereo Depth Inference(CVPR2019)

- Task
> Infer the depth map for the reference image by one reference image align with several source images
- :sparkles: Motivation
> Use GRU to convert the three-dimensional calculation amount of 3D-CNN into a sequence form in the depth direction.
- Key insight
> Encode camera geometries through differentiable homography warping to build 3D cost volume  
> Enable end-to-end training  
> Adapt arbitrary number of input images  
> Multi-scale 3D convolutions and regree inital depth map  
> refine the depth map

- Contribution
> 1. reduce computeral memory.
> 2. Provide new ideas for solving 3D regularization

- Think
> Convert 3D to a series of 2D convolution operations, sacrificing time for memory. Although the memory consumption problem is solved, it raises new timing issues, but decomposing 3D CNN is a good starting point.
- result
 
*DTU*  
| Model | view number | Acc.(mm)↓ | Comp.(mm)↓ | Overall(mm)↓ |
| :-: | :-: | :-: | :-: | :-: |
| MVSNet | 5 | 0.396 | 0.527 | 0.462 |

*Tanks and Temples*  
| Model | Train view | Mean↑ | Family↑ | Francis↑ | Horse↑ | LightHouse↑ | M60↑ | Panther↑ | Playground↑ | Train↑ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| MVSNet | 5 | 43.48 | 55.99 | 28.55 | 25.07 | 50.79 | 53.96 | 50.86 | 47.90 | 34.69 |

