<!-- Pagina 46 -->

DISTRIBUZIONE LOGNORMALE (8)

- Adatta per fenomeni ASIMMETRICI, con occasionali OUTLIERS

Sia $X \sim \mathcal{N}(\mu, \sigma^2)$, allora $Y = e^X$ ha una distribuzione LOGNORMALE di parametri $\mu$ e $\sigma^2$


$$
Y \sim \log\mathcal{N} (\mu, \sigma^2)
$$


- Ricaviamo la distribuzione di $Y$:

$$
F_Y (y; \mu, \sigma) = P(Y \leq y) \quad \text{per } \sigma > 0
$$

$$
= P(e^X \leq y) = P(X \leq \log(y))
$$

ovvero 

$$
F_Y(y; \mu, \sigma) = \Phi\left(\frac{\log(y) - \mu}{\sigma}\right)
$$

- Per la densità basta calcolare la derivata, ricordando che

$$
\Phi'(z) = \phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}
$$