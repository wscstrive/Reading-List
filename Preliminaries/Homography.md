
# :book: Knowledge introduction
1. [coordinate_trans](Preliminaries/Coordinate_transformation.md)

# plane_sweeping  

- Assumption: All objects only have diffuse reflection, and define a near plane and a far plane, and it must be ensured that the object is located between the two planes, and then the space between the near plane and the far plane can be divided by a series of dense parallel planes.
- Input: A series of calibrated photos and the projection matrix corresponding to the shooting camera
<img src="https://github.com/elleryw0518/MVS/assets/101634608/24059444-b3b7-4434-be1a-794b32cb31fd" alt="plane_sweeping" width="300px">  
<img src="https://github.com/elleryw0518/MVS/assets/101634608/29519eaa-ae7a-4766-8a56-1df5de43f9c5" alt="plane_sweeping1" width="300px"> 

> epipolar plane π: The plane composed of two camera coordinate points and the measured object point  
> epipolar line l: The intersection of the polar plane and the graph plane  
> Image plane I1, I2: The image plane is actually behind the optical center. It is equivalent to bringing it to the front, but it is more intuitive to understand 

According to the epipolar feature, that is, the matching point on another image must be on the corresponding epipolar line. By giving a reference point o and an epipolar line, we can reduce the full graph search to searching along the epipolar line.



# homography_warp  

<img src="https://github.com/elleryw0518/MVS/assets/101634608/40dfcd27-b0ec-47ca-817c-7baea371bafb" alt="homo1" width="300px">   


Homography is a concept in projective geometry, also known as projective transformation. It maps points (three-dimensional homogeneous vectors) on one projective plane to another projective plane, and maps straight lines into straight lines, which has line-preserving properties. In general, homography is a linear transformation about three-dimensional homogeneous vectors, which can be represented by a 3*3 non-singular matrix H.


$$
\mathbf {p}_2 = H\cdot \mathbf{p_1}
$$

$$
\Longrightarrow 
\begin{bmatrix}
x_2 \\
y_2 \\
1
\end{bmatrix}=
H
\begin{bmatrix}
x_1 \\
y_1 \\
1
\end{bmatrix}=
\begin{bmatrix}
h_{11} & h_{12} & h_{13} \\
h_{21} & h_{22} & h_{23} \\
h_{31} & h_{32} & h_{33}
\end{bmatrix}
\begin{bmatrix}
x_1 \\
y_1 \\
1
\end{bmatrix}
$$

<img src="https://github.com/elleryw0518/MVS/assets/101634608/7c29db0a-25d7-4815-80e6-3f0dad8fb6ee" alt="homo" width="400px">  


# Reference
1. [单应变换 | Homography](http://liuxiao.org/kb/3dvision/geometry/%E5%8D%95%E5%BA%94%E5%8F%98%E6%8D%A2-homography/)
2. [立体视觉入门指南（2）：关键矩阵（本质矩阵，基础矩阵，单应矩阵）](https://zhuanlan.zhihu.com/p/377794028)
3. [Plane-sweeping](https://www.codetd.com/article/2992701)
