<!-- Pagina 41 -->

Osservazioni:

- vale per ogni distribuzione, l'approssimazione è migliore per distribuzioni simmetriche e continue
- se $X_i \sim \mathcal{N}(\mu, \sigma^2)$, il risultato è esatto (non occorre invocare il teorema)
- per $n \ge 30$ generalmente si ottiene una buona approssimazione

DUE CASI NOTEVOLI

BINOMIALE $X \sim Bi(n, p)$

$X = \sum_{i=1}^{n} Z_i$, $Z_i \sim Bernoulli(p)$

Applicando il TLC:

$\frac{X}{n} \stackrel{a}{\sim} \mathcal{N}\left(p, \frac{p(1-p)}{n}\right)$

$X \stackrel{a}{\sim} \mathcal{N}(np, np(1-p))$

APPROSSIMAZIONE NORMALE DELLA BINOMIALE