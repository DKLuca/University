<!-- Pagina 101 -->

# Consistenza

Mentre la non distorsione è una proprietà desiderabile, la consistenza è un requisito necessario per uno stimatore ragionevole. Vale infatti

$$
\begin{aligned}
EQM(\widehat{\theta}) &= V(\widehat{\theta}) + (E(\widehat{\theta}) - \theta)^2 \,, \\
&= \text{varianza} + (\text{distorsione})^2 \,.
\end{aligned}
$$

La condizione di consistenza equivale allora a

$$
\left\lbrace
\begin{aligned}
&\lim_{n \to \infty} E(\widehat{\theta}) = \theta \,, \\
&\lim_{n \to \infty} V(\widehat{\theta}) = 0 \,.
\end{aligned}
\right.
$$

In pratica si richiede che lo stimatore sia non distorto (almeno per $n \to \infty$) e che la sua varianza diventi sempre più piccola, ossia la sua distribuzione si concentri sempre più attorno al valore $\theta$.

All'aumentare dell'informazione campionaria, sembra ragionevole richiedere che la conoscenza su $\theta$ diventi sempre più precisa.