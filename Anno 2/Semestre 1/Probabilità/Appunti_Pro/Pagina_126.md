<!-- Pagina 126 -->

* Se $n$ è piccolo ($n < 30$), l'effetto esiste, e la teoria richiede che $X_i \sim \mathcal{N}\left\lbrace \mu, \sigma^2 \right\rbrace$: per campioni normali si ottiene allora

$$
T = \frac{\overline{x} - \mu}{\sqrt{\frac{S^2}{n}}} \sim t_{n-1}
$$

e l'IC è quindi

$$
\overline{x} \pm t_{n-1; 1-\alpha/2} \frac{S}{\sqrt{n}}
$$
*(Nota: percentile $1-\alpha/2$ di $t_{n-1}$)*

* Nota: se $n$ è elevato $t_{n-1} \sim \mathcal{N}(0,1)$, confermando che per grandi campioni l'effetto di utilizzare $S^2$ è trascurabile.

ESEMPIO 3.5: $n=7$, $\overline{x} = 10.0$, $S = 0.283$
$(1-\alpha) = 0.95$, $t_{6; 0.975} = 2.447$

$$
10 \pm 2.447 \frac{(0.283)}{\sqrt{7}} = (9.74, 10.26)
$$