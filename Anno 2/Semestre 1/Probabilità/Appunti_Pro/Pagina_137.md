<!-- Pagina 137 -->

(11) IC PER UNA PROPORZIONE

$X_1, X_2, \dots, X_n \quad \text{CCS} \quad X_i \sim \text{Bernoulli}(p)$

$X = \sum_{i=1}^{n} X_i \quad , \quad \hat{p} = \frac{X}{n} = \bar{X}$

$\text{TLC}: \hat{p} \stackrel{\alpha}{\sim} \mathcal{N}\left(p, \frac{p(1-p)}{n}\right)$

Infatti $\mu = p \quad \text{e} \quad \sigma^2 = p(1-p)$

- Se particolarizziamo l'IC per $p$ nel caso di grandi campioni otteniamo:

$$
\hat{p} \pm z_{1-\alpha/2} \sqrt{\frac{p(1-p)}{n}}
$$

Che tuttavia non è utilizzabile perché $p$ non è noto!

- Se $n$ è elevato, rimpiazzo $p$ con $\hat{p}$:

$$
\hat{p} \pm z_{1-\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} \quad \begin{array}{l} \text{IC CLASSICO} \\ \to \text{RISTRATTO} \\ \text{A } (0,1) \end{array}
$$