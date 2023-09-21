# Rigid body transformation
![rigib-body.png](https://i.postimg.cc/pV3RBpZH/rigib-body.png)
![1](https://camo.githubusercontent.com/https://postimg.cc/fJYrsYTS)
Assume that the coordinates of a point P in the Euclidean space in the two coordinate systems are P1 and P2 respectively:
  
$$
p_2 = R p_1 + t,\ p_1=(x, y, z),\ p_2=(x', y', z') 
$$
  
where R is rotation matrix, t is translation matrix.
i.e.,:  

$$
\begin{bmatrix}
x' \\
y' \\
z'
\end{bmatrix} =
\begin{bmatrix}
r_{11} & r_{12} & r_{13} \\
r_{21} & r_{22} & r_{23} \\
r_{31} & r_{32} & r_{33}
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix} +
\begin{bmatrix}
t_1 \\
t_2 \\
t_3
\end{bmatrix}
$$  
> Notice: The position and orientation of rigid objects can be transformed while their shape and size remain unchanged.  
Degrees of freedom: 6 (3 rotations and 3 translations)  
Rotation matrix: _3*3_? Rotation around an axis affects other axes, and the coordinates are related to each other  
Translation matrix: _3*1_? coordinates are independent of each other  
## Translation
[![translation.png](https://i.postimg.cc/fL6NKRdy/translation.png)](https://postimg.cc/ygXt6BvC)
## Rotation
[![rotation.png](https://i.postimg.cc/xCDFCNV0/rotation.png)](https://postimg.cc/94bBgMfS)  
# Coordinate systems
> World coordinate system, Camera coordinate system, and Pixel coordinate system.
## World coordinate system -> Camera coordinate system
> The transformation from the world coordinate system to the camera coordinate system is a rigid body transformation and does not cause deformation.

## Camera coordinate system -> Pixel coordinate system

# Homography_warp

# Reference
1. [深入理解旋转矩阵和平移向量的本质](https://zhuanlan.zhihu.com/p/141597984)
2. [【相机标定】四个坐标系之间的变换关系](https://cloud.tencent.com/developer/article/1820935)
