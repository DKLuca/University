<!-- Pagina 30 -->

Proprietà:
$$
\left\lbrace
\begin{aligned}
E(X) &= \lambda \\
V(X) &= \lambda
\end{aligned}
\right.
\quad
\begin{aligned}
&\text{segue da proprietà delle} \\
&\text{serie, ma anche dalla} \\
&\text{approssimazione binomiale}
\end{aligned}
$$

(1) PROCESSO DI POISSON (omogeneo)

1. ARRIVI indipendenti nel tempo o nello spazio
2. Non ci sono arrivi simultanei
3. $\lambda$ tasso di arrivi medio in una unità di tempo (è lo stesso per tutte le unità)

$$
X = n^\circ \text{ arrivi in } t \text{ unità di } \begin{aligned}[t]&\text{tempo} \\ &\text{(spazio)}\end{aligned}
$$

$$
1 + 2 + 3 \implies X \sim \text{Poisson}(\lambda t)
$$
$$
(o \text{ anche si indica } \mathcal{P}(\lambda t))
$$

- ES: Accessi sito web (in un intervallo di tempo)
$$
\lambda = 5 \text{ accessi al minuto}
$$
$$
P(17 \text{ accessi in } 3 \text{ minuti}) = e^{-15} \frac{15^{17}}{17!} = 0.0847
$$