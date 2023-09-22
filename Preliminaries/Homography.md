
# :book: Knowledge introduction
1. [coordinate_trans](Preliminaries/Coordinate_transformation.md)

# homography_warp  

<img src="https://github.com/elleryw0518/MVS/assets/101634608/40dfcd27-b0ec-47ca-817c-7baea371bafb" alt="homo1" width="300px">  


Homography transformation belongs to projective transformations and is commonly used to align one camera view to another. It can be roughly represented as follows:  


$$
\mathbf {p}_2 = H\cdot \mathbf{p_r}
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

