# MVSNet: Depth Inference for Unstructured Multi-View Stereo  

- background: MVS is a core problem of CV.Traditional MVS have shown great results.
- :sparkles: motivation: Traditional MVS rely on hand-crafted similarity metric and engineered  regularization result in can't handle challenge scenes. Rencent MVS that using CNN to improve quanlity, but theses methods fails to fully use multi-view information and restricts by huge memory consumption of 3D volume.
- result:
| Model | view number | Acc.(mm)↓ | Comp.(mm)↓ | Overall(mm)↓ |
| :-: | :-: | :-: | :-: | :-: |
| MVSNet | 5 | 0.396 | 0.527 | 0.462 |

## Network Architecture
