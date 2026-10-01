<!-- Pagina 64 -->

Applicazioni notevoli

* Si procede in maniera analoga per trovare la distribuzione della somma di v.c. normali, Gamma (con lo stesso parametro di scala $\beta$) o binomiali (con lo stesso parametro $p$) indipendenti.

* Analogamente, si ottiene la distribuzione di trasformazione lineare di una v.c. normale: i passi sono i seguenti
  * Sia $X \sim \mathcal{N}(\mu, \sigma^2)$ e $Y = a + b X$, con $a, b \in \mathbb{R}$
  * Si ottiene facilmente che

$$
m_Y(t) = E[e^{(a+b X)t}] = e^{a t} m_X(b t) = e^{(a+b\mu)t + b^2 t^2 \sigma^2/2},
$$

  e si riconosce la f.g.m. di una distribuzione $\mathcal{N}(a+b\mu, b^2 \sigma^2)$, per cui

$$
Y \sim \mathcal{N}(a+b\mu, b^2 \sigma^2).
$$