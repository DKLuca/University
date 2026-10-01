<!-- Pagina 76 -->

# Inferenza statistica parametrica

La distribuzione assunta per le singole variabili dipende dalla natura dei dati. Ad esempio, per dati binari sarà naturale ipotizzare $Y_i \sim \text{Bernoulli}(p)$, per misurazioni $Y_i \sim \mathcal{N}(\mu, \sigma^2)$, per conteggi $Y_i \sim \mathcal{P}(\lambda)$, per tempi di guasto $Y_i \sim \mathcal{G}a(\alpha, 1/\beta)$ (o Weibull), etc.

In ogni caso, la distribuzione assunta per le v.c. del campione dipenderà da ignote costanti dette **parametri**, vale a dire le quantità $p, \mu, \sigma^2, \alpha, \beta \dots$

I parametri entrano nella definizione della distribuzione delle variabili del campione $Y_1, \dots, Y_n$. Nell'**inferenza statistica parametrica** si assume che la distribuzione delle v.c. del campione sia nota a meno dei valori dei parametri, che corrispondono tipicamente agli aspetti di interesse dell'analisi.