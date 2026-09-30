<!-- Pagina 10 -->

PROPOSIZIONE \hfill (5)

Se $X$ e $Y$ sono v.c. indipendenti $\implies \rho_{XY} = 0$

Prova

$$
E(X \cdot Y) = \sum_{x} \sum_{y} x \, y \, p_{XY}(x,y)
$$

(Caso discreto)

$$
= \left( \sum_{x} x \, p_{X}(x) \right) \left( \sum_{y} y \, p_{Y}(y) \right)
$$

$$
= E(X) \, E(Y) \implies \text{Cov}(X,Y) = 0
$$

--------------------------------------------------

NOTA: Non vale il viceversa, come mostra l'esempio che segue

$$
\begin{array}{c|ccc}
Y \setminus X & -1 & 0 & 1 \\
\hline
0 & 0 & 0.5 & 0 \\
1 & 0.25 & 0 & 0.25
\end{array}
\quad
\begin{array}{l}
p_{XY}(x,y) \text{ per} \\
X \text{ e } Y \\
\text{ discrete}
\end{array}
$$

Si trova facilmente $\rho_{XY} = 0$, ma le due v.c. non sono indipendenti!

$$
(\text{Infatti } Y = |X|)
$$