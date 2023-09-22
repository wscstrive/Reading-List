
# :book: Knowledge introduction
1. [coordinate_trans](Preliminaries/Coordinate_transformation.md)

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
