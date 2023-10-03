# Recurrent MVSNet for High-resolution Multi-view Stereo Depth Inference(CVPR2019)

## Task
- Infer the depth map for the reference image by one reference image align with several source images
## :sparkles: Motivation
- Use GRU to convert the three-dimensional calculation amount of 3D-CNN into a sequence form in the depth direction.
## Key insight
- Encode camera geometries through differentiable homography warping to build 3D cost volume  
- Enable end-to-end training  
- Adapt arbitrary number of input images  
- Multi-scale 3D convolutions and regree inital depth map  
- refine the depth map

## Contribution
- reduce computeral memory.
- Provide new ideas for solving 3D regularization

## Think
- Convert 3D to a series of 2D convolution operations, sacrificing time for memory. Although the memory consumption problem is solved, it raises new timing issues, but decomposing 3D CNN is a good starting point.

## result
 
*DTU*  
| Model | view number | Acc.(mm)↓ | Comp.(mm)↓ | Overall(mm)↓ |
| :-: | :-: | :-: | :-: | :-: |
| R-MVSNet(D=256) | 3 | 0.385 | 0.459 | 0.422 |
| R-MVSNet(D=512) | 3 | 0.383 | 0.452 | 0.417 |

*Tanks and Temples*  
| Model | Train view | Mean↑ | Family↑ | Francis↑ | Horse↑ | LightHouse↑ | M60↑ | Panther↑ | Playground↑ | Train↑ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| R-MVSNet | 5 | 43.48 | 55.99 | 28.55 | 25.07 | 50.79 | 53.96 | 50.86 | 47.90 | 34.69 |

## Network Architecture

<img width="703" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/7a349e37-69ea-4e08-aa4e-f0541bf4b6d3">

