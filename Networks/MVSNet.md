# MVSNet: Depth Inference for Unstructured Multi-View Stereo  

- background
> MVS is a core problem of CV.Traditional MVS have shown great results.
- :sparkles: motivation
> Traditional MVS rely on hand-crafted similarity metric and engineered  regularization result in can't handle challenge scenes. Rencent MVS that using CNN to improve quanlity, but theses methods fails to fully use multi-view information and restricts by huge memory consumption of 3D volume.
- result:
 
*DTU*  
| Model | view number | Acc.(mm)↓ | Comp.(mm)↓ | Overall(mm)↓ |
| :-: | :-: | :-: | :-: | :-: |
| MVSNet | 5 | 0.396 | 0.527 | 0.462 |

*Tanks and Temples*  
| Model | view number | Mean↑ | Family↑ | Francis↑ | Horse↑ | LightHouse↑ | M60↑ | Panther↑ | Playground↑ | Train↑ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| MVSNet | 5 | 43.48 | 55.99 | 28.55 | 25.07 | 50.79 | 53.96 | 50.86 | 47.90 | 34.69 |


## Network Architecture

<img width="1399" alt="image" src="https://github.com/elleryw0518/MVS/assets/101634608/e5c74cad-d95f-447e-bca9-53b037e8d098">


