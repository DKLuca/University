<!-- Pagina 29 -->

(2)

$$
\lim_{N \to \infty} P(X=n) = \lim_{N \to \infty} \frac{N!}{(N-n)! n!} \cdot \frac{\lambda^n}{N^n} \cdot \left(1 - \frac{\lambda}{N}\right)^N \cdot \left(1 - \frac{\lambda}{N}\right)^{-n}
$$

ovvero

$$
\lim_{N \to \infty} P(X=n) = \frac{\lambda^n e^{-\lambda}}{n!}
$$

$$
n = 0, 1, \dots
$$

- Il risultato giustifica la seguente definizione

$\underline{\text{Def}}$ $X$ v.c. di Poisson, con supporto $n = 0, 1, 2, \dots$

$$
P(X=n) = e^{-\lambda} \frac{\lambda^n}{n!}
$$

Commenti:
- È approssimazione della binomiale per $n$ elevato, $p$ piccolo e $\lambda = np$ costante
- Va bene per conteggi senza limite superiore