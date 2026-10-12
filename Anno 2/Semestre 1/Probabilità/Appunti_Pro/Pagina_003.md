<!-- Pagina 3 -->

- Si estende a funzioni di $2$ (o più) v.c.: (3)

$$
E \left[ g(X,Y) \right] = 
\begin{cases}
\sum_{x} \sum_{y} g(x,y) p_{XY}(x,y) & \text{caso discreto} \\
\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} g(x,y) f_{XY}(x,y) \,dx\,dy & \text{caso continuo}
\end{cases}
$$

Il caso speciale $g(X,Y) = X$ o $g(X,Y) = Y$ sono immediati:

$$
E(X) = \sum_{x} \sum_{y} x \, p_{XY}(x,y) = \sum_{x} x \underbrace{\sum_{y} p_{XY}(x,y)}_{p_{X}(x)}
$$
(caso discreto) (per esempio)

ESERCIZIO 4.3

$C = \text{costo per giocare}$

$Y = \text{vincita netta}$

- vinco $3$ dollari con jack o regina
- vinco $5$ dollari con asso o re

$$
\begin{array}{c|c}
y & p_{Y}(y) \\
\hline
0 - C & 36/52 \\
3 - C & 8/52 \\
5 - C & 8/52 \\
\hline
& 1
\end{array}
$$

$C$ per gioco equo?

$E(Y) = 0$