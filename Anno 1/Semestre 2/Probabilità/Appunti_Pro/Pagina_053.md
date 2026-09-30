<!-- Pagina 53 -->

(III) DISTRIBUZIONE GAMMA (5)

Generalizza l'esponenziale, prende il nome dalla

$$
\text{FUNZIONE GAMMA} \quad \Gamma(\alpha) = \int_0^\infty x^{\alpha-1} e^{-x} \, dx, \text{ per } \alpha > 0
$$

$$
\begin{align*}
\text{Proprietà:} \quad &\Gamma(n) = (n-1)! \quad \text{per } n \text{ intero} \\
&\Gamma(\alpha) = (\alpha-1) \, \Gamma(\alpha-1) \, , \quad \alpha > 1 \\
&\Gamma(1/2) = \sqrt{\pi}
\end{align*}
$$

$$
X \sim \text{Ga}\left(\alpha, \frac{1}{\beta}\right) \quad \begin{aligned} &\alpha > 0 \\ &\beta > 0 \end{aligned}
$$

$$
\begin{array}{ccc}
\text{PARAMETRO} && \beta \to \text{PARAMETRO} \\
\text{DI FORMA} && \text{DI SCALA}
\end{array}
$$

Ha f. densità di probabilità:

$$
f_X(x; \alpha, \beta) = \begin{lbrace}
\frac{x^{\alpha-1} e^{-x/\beta}}{\beta^\alpha \, \Gamma(\alpha)} \, , & x > 0 \\
0 \, , & x \le 0
\end{brace}
$$