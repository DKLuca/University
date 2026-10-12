<!-- Pagina 52 -->

* PROPRIETÀ DI ASSENZA DI MEMORIA

$$
X \sim \mathcal{E}(1/\beta) \qquad t > 0, t_0 > 0
$$

$$
P(X > t_0 + t \mid X > t_0) = P(X > t)
$$

Infatti:

$$
\begin{aligned}
P(X > t_0 + t \mid X > t_0) &= \frac{P(X > t_0 + t)}{P(X > t_0)} \\
&= \frac{e^{-\frac{(t_0 + t)}{\beta}}}{e^{-\frac{t_0}{\beta}}} &= e^{-t/\beta} = P(X > t)
\end{aligned}
$$

* Nota: la proprietà implica la MANCANZA D'USURA per il componente

$\hookrightarrow$ la distribuzione è adatta come modello per il tempo di funzionamento solo in condizioni molto particolari