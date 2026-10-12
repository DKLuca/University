<!-- Pagina 21 -->

Otteniamo la distribuzione: definiamo prima cosa gli eventi
$$
A_i = \left\lbrace \text{Esce } 6 \text{ alla } i\text{-esima prova} \right\rbrace
$$
$$
i = 1, 2, 3
$$
$$
A_1, A_2, A_3 \quad \text{MUTUAMENTE INDIPENDENTI}
$$

$$
P(X=0) = P(A_1^c \cap A_2^c \cap A_3^c)
$$
$$
= P(A_1^c) P(A_2^c) P(A_3^c) = \left(\frac{5}{6}\right)^3
$$

$$
P(X=1) = P(A_1^c \cap A_2^c \cap A_3) + P(A_1^c \cap A_2 \cap A_3^c) + P(A_1 \cap A_2^c \cap A_3^c) = 3 \left(\frac{1}{6}\right)^1 \left(\frac{5}{6}\right)^2
$$

$$
P(X=2) = 3 \left(\frac{1}{6}\right)^2 \left(\frac{5}{6}\right)^1
$$

$$
P(X=3) = \left(\frac{1}{6}\right)^3
$$

In generale: per $X \sim \text{Bi}(n, p)$

$$
P(X=x) = \binom{n}{x} p^x (1-p)^{n-x}, \quad x=0, 1, \dots, n
$$