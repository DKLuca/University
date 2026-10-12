<!-- Pagina 22 -->

* Il testo di Walpole et al. usa una simbologia particolare per $p_X(x; p)$, ovvero

$$
b(x; n, p) = \binom{n}{x} p^x (1-p)^{n-x}
$$

Proprietà:

$i)$ Posto $q = 1-p$ si ha

$$
\underbrace{(p+q)^n}_{1} = \sum_{x=0}^n \binom{n}{x} p^x (1-p)^{n-x} = 1
$$
$$
\llap{\phantom{(p+q)^n = }} \hookrightarrow \text{formula di Newton}
$$

a riprova che la distribuzione è ben definita

$ii)$ MEDIA e VARIANZA

$$
Z_i = \left\lbrace \begin{array}{lcl}
1 & \text{successo} & i\text{-esima prova} \\
0 & \text{insuccesso} & \text{"} \quad \text{"}
\end{array} \right.
$$

$$
Z_i \sim \text{Bernoulli}(p) \quad i = 1, \dots, n
$$

v.c. indipendenti