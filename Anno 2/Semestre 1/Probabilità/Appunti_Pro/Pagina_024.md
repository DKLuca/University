<!-- Pagina 24 -->

III DISTRIBUZIONE IPERGEOMETRICA (1)

- Adatta a ESTRAZIONI SENZA REINSERIMENTO

  - $n$ prove, selezione senza reinserimento da $N$ unità

  - $K$ successi, $N-K$ insuccessi

$X = $ $n^\circ$ di successi nelle $n$ prove

$$
X \sim H(N, n, K)
$$
DISTRIBUZIONE IPERGEOMETRICA

$$
P(X=x) = \frac{\binom{K}{x} \binom{N-K}{n-x}}{\binom{N}{n}} = h(x; N, n, K)
$$

METODO DEL CONTEGGIO

Supporto:

$$
\left\lbrace
\begin{aligned}
0 &\leq x \leq n \\
n - (N-K) &\leq x \leq K
\end{aligned}
\right.
$$

$$
\max(0, n-(N-K)) \leq x \leq \min(n, K)
$$