<!-- Pagina 36 -->

Proprietà di $\overline{\Phi}(z)$:

$$
i) \quad \overline{\Phi}(-z) = 1 - \overline{\Phi}(z)
$$

per la simmetria di $\phi(z)$

$$
ii) \quad \text{utilizzo:} \quad \text{sia } X \sim \mathcal{N}(\mu, \sigma^2)
$$

$$
P(x_1 < X < x_2) = P\left( \frac{x_1 - \mu}{\sigma} < \frac{X - \mu}{\sigma} < \frac{x_2 - \mu}{\sigma} \right)
$$

$$
= P\left( \frac{x_1 - \mu}{\sigma} < Z < \frac{x_2 - \mu}{\sigma} \right)
$$

$$
= \overline{\Phi}\left( \frac{x_2 - \mu}{\sigma} \right) - \overline{\Phi}\left( \frac{x_1 - \mu}{\sigma} \right)
$$

l'ultimo passaggio utilizza una proprietà vista della F. di ripartizione nel caso continuo

Ovvero: la funzione $\overline{\Phi}$ ci permette di calcolare prob. per $X$ v.c. normale qualsiasi

Inoltre:

$$
F_X(x; \mu, \sigma) = \overline{\Phi}\left( \frac{x - \mu}{\sigma} \right)
$$