<!-- ===== PAGINA 31 ===== -->

<!-- Pagina 31 -->

Infatti: $X = n^{\circ} \text{ accessi in } 3 \text{ minuti}$

$$
X \sim \mathcal{P}(\underbrace{1 \cdot 3}_{15})
$$

---

Proprietà:

$X_1 \sim \mathcal{P}(\lambda_1) \text{ , } X_2 \sim \mathcal{P}(\lambda_2) \text{ indip.}$

$$
X_1 + X_2 \sim \mathcal{P}(\lambda_1 + \lambda_2)
$$

$(\text{Prova: si utilizza la FUNZIONE GENERATRICE DEI MOMENTI, che vedremo})$

ES: Viaggiatori in transito per stazione

$X_1 = n^{\circ} \text{ arrivi tip } 1 \text{ (pendolari lavoratori)}$

$X_2 = \text{ "} \text{ "} \text{ "} 2 \text{ ( "} \text{ studenti)}$

$X_3 = \text{ "} \text{ "} \text{ "} 3 \text{ (occasionali)}$

$\downarrow X_K = \text{ "} \text{ "} \text{ "} K \text{ (}\dots\text{)}$
<span style="color:red">VIAGGIATORI TOTALI</span>

$$
X_T = X_1 + X_2 + \dots X_K \sim \mathcal{P}(\lambda_1 + \lambda_2 + \dots + \lambda_K)
$$

<!-- ===== PAGINA 32 ===== -->

<!-- Pagina 32 -->

# DISTRIBUZIONE UNIFORME CONTINUA

* $X$ v.c. continua con $f$ di densità costante nell'intervallo $(a,b)$, con $a, b \in \mathbb{R}$

$$
X \sim \mathcal{U}(a,b) \quad , \quad f_X(x; a, b) = \begin{cases} \frac{1}{b-a} &, a \le x \le b \\ 0 &, \text{altrove} \end{cases}
$$

> **[Nota Grafico: Grafico cartesiano della funzione di densità $f_X(x; a, b)$. Sull'asse delle ordinate è segnato il valore $\frac{1}{b-a}$, sull'asse delle ascisse sono segnati i punti $a$ e $b$. La funzione è costante a livello $\frac{1}{b-a}$ per $x \in [a, b]$ e zero altrove.]**

$$
E(X) = \frac{a+b}{2} \quad \text{per la simmetria}
$$

$$
V(X) = \frac{(b-a)^2}{12} \quad \text{calcoli semplici}
$$

$$
F_X(x; a, b) = \begin{cases} 0 &, x \le a \\ \frac{x-a}{b-a} &, a \le x \le b \\ 1 &, x \ge b \end{cases}
$$

<!-- ===== PAGINA 33 ===== -->

<!-- Pagina 33 -->

## III DISTRIBUZIONE NORMALE 2

$$
f_X(x; \mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \quad, x \in \mathbb{R}
$$

$$
X \sim N(\mu, \sigma^2)
$$

$$
n(x; \mu, \sigma) \quad (\text{Walpole et al.})
$$

- È la più importante distribuzione continua, si trova in moltissimi fenomeni fisici, biologici e anche socio-economici.

- Il grafico della f. di densità è la famosa "campana di Gauss".

> **[Nota Grafico: Schizzo del grafico di una funzione di densità normale a forma di campana, simmetrica rispetto all'asse verticale tratteggiato passante per il punto $\mu$ sull'asse orizzontale]**

- Si trova $E(X) = \mu$ (per simmetria), mentre $V(X) = \sigma^2$ richiede l'integrazione per parti

<!-- ===== PAGINA 34 ===== -->

<!-- Pagina 34 -->

* Proprietà: per qualsiasi scelta di $\mu \in \mathbb{R}$ e $\sigma > 0$
(Prova: vedi $F_x$)

> **[Nota Grafico: Schizzo di una curva gaussiana (campana) simmetrica rispetto all'asse centrale $\mu$. Sull'asse orizzontale sono indicati i punti $\mu-3\sigma$, $\mu-2\sigma$, $\mu-\sigma$, $\mu$, $\mu+\sigma$, $\mu+2\sigma$, $\mu+3\sigma$ con linee tratteggiate verticali che salgono dalla base verso la curva.]**

$$
P(\mu - \sigma \le X \le \mu + \sigma) \simeq 0.68
$$

$$
P(\mu - 2\sigma \le X \le \mu + 2\sigma) \simeq 0.95
$$

$$
P(\mu - 3\sigma \le X \le \mu + 3\sigma) \simeq 0.99
$$

Ecco perché possiamo utilizzare la distribuzione anche per grandezze fisiche che hanno un campo di variazione limitato (p.es., lunghezze ecc.)

* STANDARDIZZAZIONE

Sia $X \sim N(\mu, \sigma^2)$, definiamo

$$
Z = \frac{X - \mu}{\sigma} : \quad \text{si ha} \quad Z \sim N(0,1)
$$

<!-- ===== PAGINA 35 ===== -->

<!-- Pagina 35 -->

- Il risultato è un caso speciale di un risultato più generale: se $a, b \in \mathbb{R}$
  
$$
a + bX \sim \mathcal{N}\left(a + b\mu, \, b^2\sigma^2\right)
$$

Prova: si dimostra tramite la FUNZIONE GENERATRICE DEI MOMENTI, che vedremo ($f. \, g. \, m.$)

- Def $Z \sim \mathcal{N}(0,1)$ è la DISTRIBUZIONE NORMALE STANDARD (o STANDARDIZZATA)

Notazione:

$$
f_Z(z; 0, 1) = \phi(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}}
$$

$$
F_Z(z; 0, 1) = \Phi(z) = \int_{-\infty}^{z} \phi(t) \, dt
$$

↳ non ammette forma analitica: esistono però tabelle, le TAVOLE DELLA NORMALE

<!-- ===== PAGINA 36 ===== -->

<!-- Pagina 36 -->

Proprietà di $\Phi(z)$:

i) 

$$
\Phi(-z) = 1 - \Phi(z)
$$

per la simmetria di $\phi(z)$

ii) Utilizzo: sia $X \sim \mathcal{N}(\mu, \sigma^2)$

$$
P(x_1 < X < x_2) = P\left(\frac{x_1-\mu}{\sigma} < \underbrace{\frac{X-\mu}{\sigma}}_{Z \sim \mathcal{N}(0,1)} < \frac{x_2-\mu}{\sigma}\right)
$$

$$
= P\left(\frac{x_1-\mu}{\sigma} < Z < \frac{x_2-\mu}{\sigma}\right)
$$

$$
= \Phi\left(\frac{x_2-\mu}{\sigma}\right) - \Phi\left(\frac{x_1-\mu}{\sigma}\right)
$$

l'ultimo passaggio utilizza una proprietà vista della F.d. ripartizione nel caso continuo

Ovvero: la funzione $\Phi$ ci permette di calcolare prob. per $X$ v.c. normale qualsiasi.

Inoltre:

$$
F_X(x; \mu, \sigma) = \Phi\left(\frac{x-\mu}{\sigma}\right)
$$

<!-- ===== PAGINA 37 ===== -->

<!-- Pagina 37 -->

6

* PERCENTILI di $X \sim N(\mu, \sigma^2)$

$x_\alpha$: $F_X(x_\alpha; \mu, \sigma) = \alpha$, $0 < \alpha < 1$

$$
\Phi\left(\frac{x_\alpha - \mu}{\sigma}\right) = \alpha
$$

quindi 

$$
\frac{x_\alpha - \mu}{\sigma} = z_\alpha
$$

$$
\uparrow
$$

percentile di $N(0,1)$

$$
x_\alpha = \mu + \sigma \ z_\alpha
$$

* Si noti: $\Phi(z_\alpha) = \alpha$, $z_\alpha = \Phi^{-1}(\alpha)$

$$
\uparrow
$$

FUNZIONE QUANTILE

e per la simmetria di $\phi(z)$ attorno a $z=0$ si ottiene:

$$
z_{1-\alpha} = -z_\alpha
$$

* Percentili notevoli:
$z_{0.95} = 1.645$
$z_{0.975} = 1.96$
$z_{0.99} = 2.33$
$z_{0.995} = 2.58$

<!-- ===== PAGINA 38 ===== -->

<!-- Pagina 38 -->

ESEMPIO

$X = \text{durata certo tipo di batteria (ore)}$

$X \sim N(50, 25) \rightarrow \mu = 50, \sigma = 5$

$x_{0.05} = \sigma z_{0.05} + \mu = 50 + 5(-1.645)$

$$
= 41.775 \text{ ore}
$$

$x_{0.95} = \sigma z_{0.95} + \mu = 50 + 5(1.645)$

$$
= 58.225 \text{ ore}
$$

> **[Nota Grafico: Grafico di una distribuzione normale con media $\mu = 50$, punti critici a $41.775$ e $58.225$. Vengono evidenziate le aree di probabilità: $0.05$ nella coda di sinistra, $0.90$ nella parte centrale tratteggiata, e $0.05$ nella coda di destra.]**

ESEMPIO 6.5

$$
X \sim N(300, 50^2)
$$

$$
P(X > 362) = P\left(Z > \frac{362 - 300}{50}\right)
$$

$$
Z \sim N(0,1) \quad = P(Z > 1.24)
$$

$$
= 1 - \Phi(1.24) = 0.1075
$$

<!-- ===== PAGINA 39 ===== -->

<!-- Pagina 39 -->

# LA DISTRIBUZIONE NORMALE: COMPLEMENTI DI TEORIA

- Un risultato notevole:

## PROPOSIZIONE

Se $X_1, X_2, \dots, X_n$ v.c. INDIPENDENTI  
Con $X_i \sim N(\mu_i, \sigma_i^2)$, e $a_1, a_2, \dots, a_n \in \mathbb{R}$

$$
Y = \sum_{i=1}^n a_i X_i \sim N\left(\sum_{i=1}^n a_i \mu_i, \sum_{i=1}^n a_i^2 \sigma_i^2\right)
$$

*Prova:* si ottiene tramite la *f.g.m.* (che vedremo)

- CASO NOTEVOLE: $\mu_i = \mu$, $\sigma_i^2 = \sigma^2$, $a_i = \frac{1}{n} \quad \forall i$

$$
\overline{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right) \quad \begin{array}{l} \text{v.c.} \\ \text{MEDIA} \\ \text{CAMPIONARIA} \end{array}
$$

- È un risultato molto importante per la statistica inferenziale, come pure il risultato che segue

<!-- ===== PAGINA 40 ===== -->

<!-- Pagina 40 -->

1) TEOREMA DEL LIMITE CENTRALE (TLC)

$X_1, X_2, \dots, X_n$ $\boxed{\text{i.i.d.}}$

$E(X_i) = \mu$, $V(X_i) = \sigma^2$

sia $Z_n = \frac{\overline{X} - \mu}{\sigma/\sqrt{n}}$

allora $\lim_{n \to \infty} F_{Z_n}(z) = \Phi(z), \quad \forall z \in \mathbb{R}$

(Prova: anche qui si usa la f.g.m.)

- Interpretazione operativa del risultato:
per $n$ elevato, $Z_n \stackrel{a}{\sim} N(0, 1)$

ovvero $\boxed{\overline{X} \stackrel{a}{\sim} N\left(\mu, \frac{\sigma^2}{n}\right)}$

- Si può esprimere per la somma:
$\sum_{i=1}^{n} X_i \stackrel{a}{\sim} N(n\mu, n\sigma^2)$

<!-- ===== PAGINA 41 ===== -->

<!-- Pagina 41 -->

Osservazioni: (3)

- vale per ogni distribuzione, l'approssimazione è migliore per distribuzioni SIMMETRICHE e CONTINUE
- Se $Xi \sim N(\mu, \sigma^2)$, il risultato è ESATTO (non occorre invocare il teorema)
- Per $n \ge 30$ generalmente si ottiene una buona approssimazione

II DUE CASI NOTEVOLI

- BINOMIALE $X \sim Bi(n, p)$

$X = \sum_{i=1}^{n} Zi \quad, \quad Zi \sim Bernaulli(p)$

Applicando il TLC:

$\frac{X}{n} \sim N\left(p, \frac{p(1-p)}{n}\right)$

APPROSSIMAZIONE NORMALE DELLA BINOMIALE

$$
X \sim N(np, np(1-p))
$$

<!-- ===== PAGINA 42 ===== -->

<!-- Pagina 42 -->

- L'approssimazione è ritenuta buona se

$$
\begin{cases} np \ge 5 \\ n(1-p) \ge 5 \end{cases}
$$

- Correzione di continuità (CC):

$$
\begin{cases} P(X \le x) = \Phi\left(\frac{x + 0.5 - np}{\sqrt{np(1-p)}}\right) \\ P(X < x) = \Phi\left(\frac{x - 0.5 - np}{\sqrt{np(1-p)}}\right) \end{cases}
$$

- POISSON $x_1, x_2, \dots, x_n$ iid, $x_i \sim \mathcal{P}(\lambda)$

$$
\sum_{i=1}^{n} X_i \sim \mathcal{P}(n\lambda) \quad \text{ma anche}
$$

$$
\sum_{i=1}^{n} X_i \approx \mathcal{N}(n\lambda, n\lambda)
$$

$\text{Quindi: se}$

$\text{\color{red}APPROSSIMAZIONE}$
$\text{\color{red}NORMALE \quad DELLA}$
$\text{\color{red}POISSON}$

$$
X \sim \mathcal{P}(\lambda) \implies X \approx \mathcal{N}(\lambda, \lambda)
$$

l'approssimazione è ritenuta buona se $\lambda \ge 10$;
anche qui possiamo applicare una CC di $0.5$

<!-- ===== PAGINA 43 ===== -->

<!-- Pagina 43 -->

- ESERCIZIO 6.14

$$
p = P(\text{Recupero}) = 0.9
$$

$$
X = n^\circ \text{ pazienti che recuperano } (\text{su } 100)
$$

$$
X \sim Bi(100, 0.9), \text{ ovvero } X \dot{\sim} N(90, 9)
$$

1. $P(84 \le X \le 95) =$

   $= P(83.5 < X < 95.5) \quad Z \sim N(0, 1)$

   $\overset{!}{=} P(-2.17 < Z < 1.83)$

   $\overset{!}{\simeq} 0.9514 \quad \left[ \begin{array}{l} \cdot \text{ senza cc: } 0.9295 \\ \cdot \text{ esatta } : 0.9556 \end{array} \right]$

2. $P(X < 86) = P(X < 85.5) \simeq \Phi(-1.50)$
   
$$
\underbrace{\quad\quad\quad}_{0.0668}
$$

$$
\left[ \begin{array}{l} \text{senza cc:} \quad 0.0912 \\ \text{esatta}: \quad\quad 0.0726 \end{array} \right]
$$

<!-- ===== PAGINA 44 ===== -->

<!-- Pagina 44 -->

ESEMPIO

$X = n^\circ \text{particelle in una sospensione di } 5\text{ml}$

$\lambda = 50 \text{ particelle/ml} \longrightarrow \text{TASSO MEDIO}$

Calcolare

a) $P(235 \le X \le 265)$

Sotto le ipotesi del processo di Poisson (che sono ragionevoli in questo caso)

$X \sim P(250)$

Usiamo il TLC: $X \approx N(250, 250)$

Si ottiene

$$
P(-0.95 \le Z \le 0.95) = 0.6572
$$

$$
\left[ \begin{array}{l}
\text{con CC:} \quad 0.6730 \\
\text{esatta} \quad : \quad 0.6731
\end{array} \right] \quad \uparrow_{\text{senza CC}}
$$

b) $P(48 \le \bar{X} \le 52)$, $\bar{X} = n^\circ \text{ medio particelle/ml}$

<!-- ===== PAGINA 45 ===== -->

<!-- Pagina 45 -->

$$
\overline{X} = \frac{X}{5} \stackrel{a}{\sim} \mathcal{N}(50, 10)
$$

$$
\left(\text{NB: non è } \overline{X} \stackrel{a}{\sim} \mathcal{N}(50, 50) !\right)
$$

$$
P(48 \le \overline{X} \le 52) \simeq 0.4714
$$

c) Quanto deve essere il volume prelevato per ottenere una probabilità del punto precedente pari a $0.55$?

$$
\overline{X} = \frac{X}{v} \quad , \quad v = \text{volume prelevato}
$$

$$
\overline{X} \stackrel{a}{\sim} \mathcal{N}\left(50, \frac{50}{v}\right)
$$

> **[Nota Grafico: Schizzo di una curva normale (gaussiana) simmetrica centrata in $50$. L'area sotto la curva è ombreggiata e indicata con $0.95$. Sull'asse orizzontale sono indicati i punti $50$, $50 - (1.96)\sqrt{\frac{50}{v}}$ e $50 + \sqrt{\frac{50}{v}} \cdot (1.96)$]**

$$
\text{ovvero:} \quad 52 = 50 + \sqrt{\frac{50}{v}} \cdot (1.96) \implies V = 48.02 \text{ ml}
$$

<!-- ===== PAGINA 46 ===== -->

<!-- Pagina 46 -->

# DISTRIBUZIONE LOGNORMALE

* Adatta per fenomeni ASIMMETRICI, con occasionali OUTLIERS

Sia $X \sim N(\mu, \sigma^2)$, allora $Y = e^X$ ha una distribuzione LOGNORMALE di parametri $\mu$ e $\sigma^2$

$$
Y \sim \log N (\mu, \sigma^2)
$$

* Ricaviamo la distribuzione di $Y$:

$$
F_Y (y; \mu, \sigma) = P(Y \le y) \quad \text{per } \sigma > 0
$$

$$
= P(e^X \le y) = P(X \le \log(y))
$$

ovvero 

$$
F_Y(y; \mu, \sigma) = \Phi \left( \frac{\log(y) - \mu}{\sigma} \right)
$$

* Per la densità basta calcolarne la derivata, ricordando che

$$
\Phi'(z) = \phi(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}}
$$

<!-- ===== PAGINA 47 ===== -->

<!-- Pagina 47 -->

Per $y > 0$

$$
f_Y(y; \mu, \sigma) = \phi\left(\frac{\log(y) - \mu}{\sigma}\right) \cdot \frac{1}{\sigma} \cdot \frac{1}{y}
$$

Ovvero:

$$
f_Y(y; \mu, \sigma) = \begin{cases} 0 & y \le 0 \\ \frac{1}{\sqrt{2\pi}\sigma y} e^{-\frac{(\log(y) - \mu)^2}{2\sigma^2}} & y > 0 \end{cases}
$$

- Grafici: si veda Fig. 6.29

- ESEMPIO 6.22

$$
X \sim \log N(3.2, 1)
$$

$$
\log(X) \sim N(3.2, 1)
$$

$$
P(X > 8) = P(\log(X) > \log(8))
$$

$$
= 1 - \Phi\left(\frac{\log(8) - 3.2}{2}\right)
$$

$$
= 0.8688
$$

<!-- ===== PAGINA 48 ===== -->

<!-- Pagina 48 -->

- Proprietà: se $Y \sim \log N(\mu, \sigma^2)$ (10)

$$
E(Y) = e^{\mu + \sigma^2/2}
$$

$$
V(Y) = e^{2\mu + 2\sigma^2} - e^{2\mu + \sigma^2}
$$

( si trovano mediante fgm di $\log(Y)$ )

- $y_\alpha = e^{\mu + \sigma z_\alpha}$, sfrutto i percentili di $X = \log(Y)$

ESEMPIO 6.23

$Y =$ miglia vita di un dispositivo

$Y \sim \log N(\mu, \sigma^2)$, $\mu = 5.149$
$\sigma = 0.737$

$$
y_{0.05} = e^{5.149 + (0.737)(-1.645)}
$$

$$
= e^{3.537} = 51.625 \text{ miglia}
$$

<!-- ===== PAGINA 49 ===== -->

<!-- Pagina 49 -->

## DISTRIBUZIONI DI DURATA

Adatte a modellare la "durata di vita" (tempo di funzionamento corretto) di componenti di vario tipo. In opportune situazioni, anche Normale e Lognormale possono essere adatte a modellare tempi, ma le più usate distribuzioni di durata sono:

* Esponenziale
* Gamma
* Weibull

## Esponenziale

$X$ v.c. con f. di densità, per $\beta > 0$

$$
f_X(x; \beta) = \begin{cases} \frac{1}{\beta} e^{-\frac{x}{\beta}}, & x > 0 \\ 0, & x \le 0 \end{cases}
$$

$X \sim \mathcal{E}(1/\beta)$ o anche $X \sim \text{Exp}(1/\beta)$

<!-- ===== PAGINA 50 ===== -->

<!-- Pagina 50 -->

$$
\text{Nota: talvolta la distribuzione viene}
$$

$$
\text{parametrizzata in } \lambda = \frac{1}{\beta} \underbrace{\text{TASSO}}_{\uparrow} \nearrow_{\text{PARAMETRO DI SCALA}}
$$

$$
\left( \text{è del tutto equivalente} \right), X \sim \mathcal{E}(\lambda)
$$

- $F.$ di $\text{RIPARTIZIONE}:$

$$
F_X (x; \beta) = \begin{cases} 0 & x \le 0 \\ 1 - e^{-\frac{x}{\beta}} & x > 0 \end{cases}
$$

$$
\boxed{E(X) = \beta} \quad \boxed{V(X) = \beta^2}
$$

$$
\llcorner\!\!\!\rightarrow \text{Integrale per parti}
$$

- $\text{Percentili} : \quad 0 < \alpha < 1$

$$
1 - e^{-\frac{x_\alpha}{\beta}} = \alpha
$$

$$
\implies \boxed{x_\alpha = -[\log(1-\alpha)]\beta}
$$

<!-- ===== PAGINA 51 ===== -->

<!-- Pagina 51 -->

# RELAZIONE CON IL PROCESSO DI POISSON ($\rightarrow$ file d'attesa)

**PROPOSIZIONE** Dato un Processo di Poisson di tasso $\lambda > 0$, il tempo $T$ che intercorre tra 2 arrivi consecutivi è $T \sim \mathcal{E}(\lambda)$

<u>Prova</u>

* Otteniamo $F_T(t)$, verificando che ha la forma tipica della distribuzione esponenziale

* se $t \le 0$ ovviamente $P(T \le 0) = 0$
  
$$
\downarrow
$$

  è un tempo

* Se $t > 0$: per calcolare $P(T \le t)$ introduciamo la v.c. $X$

  
$$
X = n^\circ \text{ arrivi in } [0,t]
$$

  
$$
X \sim \mathcal{P}(\lambda t)
$$

> **[Nota Grafico: Asse temporale da $0$ a $t$. Nel punto $t$ c'è una freccia verticale verso il basso con l'etichetta "$1^\circ \text{ arrivo}$"]**

$$
P(T > t) = P(X=0) = e^{-\lambda t} \text{ quindi}
$$

$$
\underset{\text{PASSAGGIO CHIAVE}}{\uparrow}
$$

$$
P(T \le t) = 1 - e^{-\lambda t}
$$

<!-- ===== PAGINA 52 ===== -->

<!-- Pagina 52 -->

- PROPRIETÀ DI ASSENZA DI MEMORIA (4)

$$
X \sim \mathcal{E}(1/\beta) \quad t>0, t_0>0
$$

$$
\overline{P(X > t_0+t \mid X > t_0) = P(X>t)}
$$

Infatti:

$$
P(X > t_0+t \mid X > t_0) = \frac{P(X > t_0+t)}{P(X > t_0)}
$$

$$
= \frac{e^{-\frac{(t_0+t)}{\beta}}}{e^{-\frac{t_0}{\beta}}} = e^{-t/\beta} = P(X>t)
$$

- Nota: la proprietà implica la MANCANZA D'USURA per il componente.

$\hookrightarrow$ la distribuzione è adatta come modello per il tempo di funzionamento solo in condizioni molto particolari.

<!-- ===== PAGINA 53 ===== -->

<!-- Pagina 53 -->

## III. DISTRIBUZIONE GAMMA $\textcircled{5}$

Generalizza l'esponenziale, prende il nome dalla

$$
\text{FUNZIONE GAMMA} \quad \Gamma(\alpha) = \int_{0}^{\infty} x^{\alpha-1} e^{-x} \, dx, \text{ per } \alpha > 0
$$

$$
\begin{aligned}
\text{Proprietà}: \quad & \Gamma(n) = (n-1)! \quad \text{per } n \text{ intero} \\
& \Gamma(\alpha) = (\alpha-1) \, \Gamma(\alpha-1) \quad, \quad \alpha > 1 \\
& \Gamma(1/2) = \sqrt{\pi}
\end{aligned}
$$

$$
X \sim \text{ga}\left(\alpha, 1/\beta\right) \quad \begin{aligned} \alpha > 0 \\ \beta > 0 \end{aligned}
$$

$$
\underset{\text{DI FORMA}}{\text{PARAMETRO}} \quad \nearrow \quad \beta \rightarrow \underset{\text{DI SCALA}}{\text{PARAMETRO}}
$$

Ha f. densità di probabilità:

$$
f_X(x; \alpha, \beta) = \begin{cases} \dfrac{x^{\alpha-1} e^{-x/\beta}}{\beta^\alpha \, \Gamma(\alpha)} &, x > 0 \\[10pt] 0 &, x \le 0 \end{cases}
$$

<!-- ===== PAGINA 54 ===== -->

<!-- Pagina 54 -->

* PARAMETRIZZAZIONE ALTERNATIVA:

$$
\lambda = \frac{1}{\beta}
$$

$\text{TASSO}$

- Se $\alpha = 1 \implies X \sim \mathcal{E}\left(\frac{1}{\beta}\right)$

<u>ALTRI CASI PARTICOLARI</u>

- Se $\alpha$ è INTERO $\implies$ DISTRIBUZIONE DI ERLANG

- Se $\alpha = \frac{k}{2}$ ($k$ intero), $\beta = 2 \implies$ DISTRIBUZIONE CHI-QUADRATO

- Proprietà: 

$$
\begin{cases} E(X) = \alpha \beta \\ \\ V(X) = \alpha \beta^2 \end{cases}
$$

---

1. Teorema. $\longrightarrow$ RELAZIONE CON IL PROCESSO DI POISSON

$X_1, X_2, \dots, X_n \quad \text{indip.} \quad X_i \sim \mathcal{E}\left(\frac{1}{\beta}\right)$

$$
Y = \sum_{i=1}^n X_i \sim \text{Ga}\left(n, \frac{1}{\beta}\right)
$$

$\text{Prova:}$ usa la f.g.m.

<!-- ===== PAGINA 55 ===== -->

<!-- Pagina 55 -->

* Proprietà: se $\alpha$ è intero (distribuzione di Erlang) si può ottenere la $F_X$

Per $x > 0$:

$$
F_X(x; \alpha, \beta) = 1 - \sum_{j=0}^{\alpha-1} \frac{e^{-x/\beta} (x/\beta)^j}{j!}
$$

$\hookrightarrow$ F. di RIPARTIZIONE V.C. ERLANG

* Commenti: la distribuzione gamma offre un modello molto più flessibile della distribuzione esponenziale, per $\alpha \neq 1$ non gode della proprietà di assenza di memoria $\longrightarrow$ adatta a modellare fenomeni affetti da usura

* Ha inoltre un ruolo in relazione al processo di Poisson

<!-- ===== PAGINA 56 ===== -->

<!-- Pagina 56 -->

# 10. DISTRIBUZIONE WEIBULL

(8)

- Come la distribuzione gamma, estende la distr. esponenziale ma è molto più flessibile

$$
X \sim \text{Weibull}(\alpha, \beta)
$$

$$
f_X(x; \alpha, \beta) = \begin{cases} \alpha \beta \, x^{\beta-1} e^{-\alpha x^\beta}, & x > 0 \\ 0, & x \le 0 \end{cases}
$$

$\alpha > 0, \quad \beta > 0$
$\downarrow$
$\text{PARAMETRO DI FORMA}$

- Se $\beta = 1$, $\quad X \sim \mathcal{E}(\alpha)$

- F di ripartizione per $x > 0$:

$$
F_X(x; \alpha, \beta) = \int_0^x \alpha \beta \, t^{\beta-1} e^{-\alpha t^\beta} \, dt
$$

$$
\text{poniamo} \quad u = \alpha t^\beta
$$

$$
du = \alpha \beta \, t^{\beta-1} dt
$$

<!-- ===== PAGINA 57 ===== -->

<!-- Pagina 57 -->

$$
\int_0^{\alpha x^\beta} e^{-u} \, du = 1 - e^{-\alpha x^\beta}
$$

Avrò:

$$
F_X(x; \alpha, \beta) = \begin{cases} 0 & x \le 0 \\ 1 - e^{-\alpha x^\beta} & x > 0 \end{cases}
$$

* Con passaggi analoghi si ottiene

$$
E(X) = \frac{\Gamma\left(1 + \frac{1}{\beta}\right)}{\alpha^{1/\beta}}
$$

* ### TASSO DI GUASTO

$X$ V.C. DI DURATA (QUALSIASI)

$$
Z(x) = \frac{f_X(x)}{1 - F_X(x)}, \quad x > 0
$$

$$
1 - F_X(x) = \int_x^\infty f_X(t) \, dt \quad \text{AFFIDABILITÀ}
$$

La definizione di $Z(x)$ deriva dalla

$$
P(x < X < x + \varepsilon \mid X > x) = \frac{F_X(x + \varepsilon) - F_X(x)}{1 - F_X(x)}
$$

per $\varepsilon > 0$

<!-- ===== PAGINA 58 ===== -->

<!-- Pagina 58 -->

perciò

$$
\lim_{\varepsilon \to 0^+} \frac{P(x < X < x + \varepsilon \mid X > x)}{\varepsilon} = \frac{f_X(x)}{1 - F_X(x)} = Z(x)
$$

**(10)**

- Se $X \sim \text{Weibull}(\alpha, \beta)$

$$
Z(x) = \alpha \beta x^{\beta-1} \quad, \quad x > 0
$$

- per $\beta = 1$: $Z(x) = \alpha$, ASSENZA DI MEMORIA

- per $\beta > 1$: $Z(x)$ cresce con $x$, il componente si logora nel tempo. È il caso tipico.

- per $\beta < 1$: $Z(x)$ decresce con $x$, il componente si rafforza nel tempo. Poco comune.

<!-- ===== PAGINA 59 ===== -->

<!-- Pagina 59 -->

# La funzione generatrice dei momenti

* Data una v.c. $X$, la sua **funzione generatrice dei momenti (f.g.m.)** è la funzione reale con argomento $t \in \mathbb{R}$

$$
m_X(t) = E\left(e^{tX}\right)
$$

ovvero

$$
m_X(t) = \begin{cases} \sum e^{t x} p_X(x) & \text{se } X \text{ è discreta} \\ \int_{-\infty}^{+\infty} e^{t x} f_X(x) dx & \text{se } X \text{ è continua} \end{cases}
$$

* La f.g.m. esiste se la sommatoria o l'integrale sono finiti in un intervallo aperto che contiene lo zero, ovvero del tipo $(-t_0, t_0)$, con $t_0 > 0$.

<!-- ===== PAGINA 60 ===== -->

<!-- Pagina 60 -->

# Proprietà della f.g.m.

La f.g.m. (che nel caso continuo è simile alla trasformata di Fourier della funzione di densità) gode di alcune importanti proprietà:

1. Il comportamento della funzione nel punto $0$ è rilevante:

$$
\begin{aligned}
m_X(0) &= 1 \\
m'_X(0) &= E(X) \\
m''_X(0) &= E(X^2) \\
\dots &\quad \dots \\
m_X^{(n)}(0) &= E(X^n)
\end{aligned}
$$

2. Non è detto che la f.g.m. esista, ma **se esiste determina la distribuzione**, ovvero è in corrispondenza 1:1 con la funzione di ripartizione di $X$ (e quindi con $p_X$ o $f_X$);

---

<div style="font-size: small; display: flex; justify-content: space-between;">
<span>a.a 2024/2025 — R. Bellio</span>
<span>2 / 7</span>
</div>

