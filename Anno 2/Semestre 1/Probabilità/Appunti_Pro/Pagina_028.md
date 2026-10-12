<!-- Pagina 28 -->

(1) LA DISTRIBUZIONE DI POISSON

Problema: $X = n^{\circ}$ viaggiatori che transitano per una stazione in un giorno feriale qualsiasi

Assunzioni:
- $n^{\circ}$ potenziali viaggiatori $N$
- agiscono in maniera indipendente
- hanno tutti la stessa probabilità "di successo" (transito)

$$
\implies X \sim Bi(N, p)
$$

Definiamo $\lambda = N \cdot p$ tasso passaggio medio

$$
P(X=x) = \binom{N}{x} p^x (1-p)^{N-x}
$$
$$
= \binom{N}{x} \left(\frac{\lambda}{N}\right)^x \left(1-\frac{\lambda}{N}\right)^{N-x}
$$

Assumiamo che 

$$
\left\lbrace 
\begin{array}{l}
N \to \infty \\ 
p \to 0
\end{array}
\right. 
$$

e $\lambda \to$ costante

e calcoliamo il limite di $P(X=x)$: