# :book: Knowledge introduction
1. [coordinate_trans](Preliminaries/Coordinate_transformation.md)

# homography_warp  

Homography transformation belongs to projective transformations and is commonly used to align one camera view to another. It can be roughly represented as follows:  

$$
\mathbf{p}_1  =  

\begin{bmatrix}
x_1 \\
y_1 \\
1
\end{bmatrix}=
H
\begin{bmatrix}
x_2 \\
y_2 \\
1
\end{bmatrix}=
\begin{bmatrix}
h_{11} & h_{12} & h_{13} \\
h_{21} & h_{22} & h_{23} \\
h_{31} & h_{32} & h_{33} 
\end{bmatrix}
\begin{bmatrix}
x_2 \\
y_2 \\
1
\end{bmatrix}=
H\cdot \mathbf{p_2}
$$

