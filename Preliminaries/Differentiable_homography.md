# Rigid body transformation
<img src="https://github.com/elleryw0518/MVS/assets/101634608/6acf03ea-423c-4f51-acd6-a9601b1736a3" alt="rigib_body" width="400px">  

- Assume that the coordinates of a point P in the Euclidean space in the two coordinate systems are P1 and P2 respectively:
  
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
<img src="https://github.com/elleryw0518/MVS/assets/101634608/03f8c570-cc81-496e-bd01-9a9adbb730ec" alt="translation" width="350px">  

## Rotation
![rotation](https://github.com/elleryw0518/MVS/assets/101634608/d885560e-3a30-43e9-8379-11204747e3cf)
# Coordinate systems
> World coordinate system, Camera coordinate system, Image coordinate system, and Pixel coordinate system.
## World coordinate system -> Camera coordinate system
<img src="https://github.com/elleryw0518/MVS/assets/101634608/9737703f-520c-4dcd-9366-4e235df499ae" alt="world- camera" width="300px">  
- This transformation is a rigid body transformation and does not cause deformation. The world coordinate system is a special coordinate system that was introduced because of the camera to determine the position of each thing. So, we only need to align the camera coordinate system with the world coordinate system.  

$$
\begin{bmatrix}
X_c \\
Y_c \\
Z_c
\end{bmatrix}=
R
\begin{bmatrix}
X_w \\
Y_w \\
Z_w
\end{bmatrix}+
T \Longrightarrow 
\begin{bmatrix}
X_c \\
Y_c \\
Z_c \\
1
\end{bmatrix}=
\begin{bmatrix}
R & T \\
0^T & 1 \\
\end{bmatrix}
\begin{bmatrix}
X_w \\
Y_w \\
Z_w \\
1
\end{bmatrix}
$$  

## Camera coordinate system -> Image coordinate system
<img src="https://github.com/elleryw0518/MVS/assets/101634608/40e405ec-e0df-4ba7-9dde-14a3e5e5b888" alt="camera-image" width="300px">


## Image coordinate system -> Pixel coordinate system


# Homography_warp

# Reference
1. [深入理解旋转矩阵和平移向量的本质](https://zhuanlan.zhihu.com/p/141597984)
2. [【相机标定】四个坐标系之间的变换关系](https://cloud.tencent.com/developer/article/1820935)
