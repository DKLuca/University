<!-- Pagina 17 -->

(1) VALORE ATTESO CONDIZIONATO

- È la media della v.c. basata sulla distribuzione condizionata

$$
E(Y \mid X=x) = \begin{cases}
\sum_{y} y \, p_{Y \mid X}(y \mid x), & \text{caso discreto} \\
\int_{-\infty}^{\infty} y \, f_{Y \mid X}(y \mid x) \, dy, & \text{caso continuo}
\end{cases}
$$

- Interpretazione: è una sintesi della distribuzione di $Y$ quando $X=x$

- Analogamente definiamo la VARIANZA CONDIZIONATA
$$
V(Y \mid X=x)
$$

- Nota: $E(Y \mid X=x)$ e $V(Y \mid X=x)$ dipendono dal valore di $x$!

Se $X$ e $Y$ sono indipendenti
$$
E(Y \mid X=x) = E(Y) \quad \text{e} \quad V(Y \mid X=x) = V(Y)
$$