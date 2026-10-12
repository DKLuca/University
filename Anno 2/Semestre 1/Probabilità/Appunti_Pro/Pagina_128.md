<!-- Pagina 128 -->

CASO $6$ NOTA:

$$
X_0 - \overline{X} \sim \mathcal{N}\left(\mu - \mu, \sigma^2 + \frac{\sigma^2}{n}\right)
$$

$$
Z = \frac{X_0 - \overline{X}}{\sigma \sqrt{1 + \frac{1}{n}}} \sim \mathcal{N}(0, 1)
$$

Con passaggi analoghi a quelli per IC per $\mu$:

$$
P\left(\overline{X} - z_{1-\alpha/2} \sigma \sqrt{1 + \frac{1}{n}} < X_0 < \overline{X} + z_{1-\alpha/2} \sigma \sqrt{1 + \frac{1}{n}}\right) = 1 - \alpha
$$

$$
\longrightarrow \quad \overline{X} \pm z_{1-\alpha/2} \sigma \sqrt{1 + \frac{1}{n}}
$$

INTERVALLO DI PREVISIONE (IP) DI LIVELLO $(1 - \alpha)$

- Se $\sigma$ è IGNOTA: $\overline{X} \pm t_{n-1; 1-\alpha/2} S \sqrt{1 + \frac{1}{n}}$

e per $n$ elevato posso usare $z_{1-\alpha/2}$ invece di $t_{n-1; 1-\alpha/2}$

NOTA: $\left\lbrace \begin{array}{l} \text{gli intervalli di previsione sono sempre piú} \\ \text{ampi degli IC per } \mu\text{, e non hanno ampiezza} \\ \text{che } \longrightarrow 0 \text{ per } n \to \infty \end{array}\right.$