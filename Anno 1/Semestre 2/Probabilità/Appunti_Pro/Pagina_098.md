<!-- Pagina 98 -->

# Esempio: peso di scatole di prodotto

Una macchina produce scatole di un certo prodotto di peso nominale $1\text{ Kg.}$, ma in realtà aventi distribuzione $\mathcal{N}(\mu, \sigma^2)$.

Si vuole stimare il peso medio effettivo e la varianza sulla base di un campione casuale semplice di $n = 20$ pezzi.

Dopo l'estrazione del campione si ottiene

$$
\overline{y} = 1.007\text{ Kg}\,, \quad s = 0.0027\text{ Kg}\,.
$$

Appare naturale porre $\widehat{\mu} = 1.007$ e $\widehat{\sigma}^2 = 0.0027^2 = 7.29 \times 10^{-6}$.

Per valutare la proporzione di scatole comprese nell'intervallo $1 \pm 0.01$, si utilizzano poi le consuete formule per la normale, ovvero

$$
\Phi \left( \frac{1.01 - 1.007}{0.0027} \right) - \Phi \left( \frac{0.99 - 1.007}{0.0027} \right) = 0.867\,.
$$