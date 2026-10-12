<!-- Pagina 5 -->

ES 4.12

$$
\begin{array}{c|cc|c}
Y \diagdown X & 2 & 4 & p_Y(y) \\
\hline
1 & 0.10 & 0.15 & 0.25 \\
3 & 0.20 & 0.30 & 0.50 \\
5 & 0.10 & 0.15 & 0.25 \\
\hline
p_X(x) & 0.40 & 0.60 &
\end{array}
$$

$$
1. \; E(XY^2) = \sum_x \sum_y x \, y^2 \, p_{XY}(x,y) = 35.2
$$

$$
2. \; \mu_X = 2(0.40) + 4(0.60) = 3.2
$$

$$
\mu_Y = 1(0.25) + 3(0.50) + 5(0.25) = 3.0
$$

ES 4.14

$$
f_X(x) = \left\lbrace 
\begin{array}{ll}
\displaystyle\frac{1}{2000} \, e^{-\frac{x}{2000}}, & x > 0 \\
0, & x \le 0
\end{array}
\right.
$$

DENSITÀ ESPONENZIALE

$$
E(X) = \frac{1}{2000} \int_0^\infty x \, e^{-x/2000} \, dx
$$

PONGO

$$
z = \frac{x}{2000} \quad \longrightarrow \quad x = z \cdot 2000 \quad dx = dz \cdot 2000
$$

$$
= 2000 \int_0^\infty z \, e^{-z} \, dz = 2000 \cdot 1
$$

$$
\int_0^\infty z \, e^{-z} \, dz \underbrace{=}_{\text{PER PARTI}} \Big[ (-e^{-z}) \, z \Big]_0^\infty + \int_0^\infty e^{-z} \, dz = 1
$$