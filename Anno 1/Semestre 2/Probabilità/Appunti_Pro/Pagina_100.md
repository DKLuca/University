<!-- Pagina 100 -->

Proprietà di uno stimatore

Si considera il comportamento dello stimatore al variare del campione, ovvero la vicinanza della sua distribuzione al valore del parametro. Due definizioni:

* $E(\widehat{\theta} - \theta)$ è la **distorsione** di $\widehat{\theta}$;
* $EQM(\widehat{\theta}) = E\left[(\widehat{\theta} - \theta)^2\right]$ è l'**errore quadratico medio** di $\widehat{\theta}$.

La loro espressione è una funzione del parametro $\theta$ e della dimensione campionaria $n$.

Si parla allora di

* **Stimatore non distorto**: ha distorsione nulla, cioè $E(\widehat{\theta}) = \theta$.
* **Stimatore consistente (in media quadratica)**: al crescere della dimensione campionaria


$$
EQM(\widehat{\theta}) \to 0.
$$