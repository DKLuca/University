<!-- Pagina 121 -->

(1) IC per la MEDIA (CASO SINGOLO CAMPIONE) (2)

$X_1, X_2, \dots, X_n$ ccs (iid) \left\lbrace 
\begin{array}{l}
E(X_i) = \mu \\
V(X_i) = \sigma^2
\end{array}
\right.

- $\overline{X} = \frac{1}{n} \sum_{i=1}^n X_i \approx \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$ TLC

(e (per ora) si suppone $\sigma^2$ nota)

$$
Z = \frac{\overline{X} - \mu}{\sqrt{\frac{\sigma^2}{n}}} \approx \mathcal{N}(0,1)
$$

( $\cdot$ Nota: se $X_i \sim \mathcal{N}(\mu, \sigma^2)$ il risultato è esatto!)

- Per definizione di percentile:

$$
P\left(-z_{1-\alpha/2} < Z < z_{1-\alpha/2}\right) \stackrel{\nearrow \text{ percentile } \mathcal{N}(0,1)}{\stackrel{\longrightarrow}{\text{per } n \text{ elevato}}} 1-\alpha
$$

$$
P\left(-z_{1-\alpha/2} < \frac{\overline{X}-\mu}{\sigma/\sqrt{n}} < z_{1-\alpha/2}\right) = 1-\alpha
$$

- Ora il passo decisivo è riesprimere la doppia diseguaglianza in termini di $\mu$: