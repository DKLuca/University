<!-- Pagina 97 -->

Esempio: frazione campionaria di elementi difettosi

Si analizzano $n = 40$ elementi, scelti a caso tra quelli prodotti da un certo macchinario. Il campione osservato è

$$
y = (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
$$
$$
0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) \comma
$$

dove $0$ e $1$ indicano, rispettivamente, se l'oggetto è o non è conforme agli standard di qualità.

In questo caso è naturale assumere $Y_i \sim \text{Bernoulli}(p)$, con $p \in (0, 1)$, perciò nel caso specifico $\theta = p$ e $\Theta = (0, 1)$.

La media campionaria $\overline{y}$, ossia la **frazione campionaria di elementi difettosi**, è una stima naturale di $p$. Con $3$ difettosi su $40$ si ottiene

$$
\widehat{p} = \frac{3}{40} = 0.075 \period
$$