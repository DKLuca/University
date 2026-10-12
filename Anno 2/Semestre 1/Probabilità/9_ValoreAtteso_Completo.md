# Appunti di Probabilità - 9. Valore Atteso (Completo)

> Raccolta unificata: pagine 1 - 162 trascritte e validate.

---

## Pagina 1

VALORE ATTESO

Def $X$ v.c.: MEDIA o VALORE ATTESO di $X$ è (o SPERANZA MATEMATICA)

$$
\mu_X = E(X) = \begin{cases} \sum_x x \cdot p_X(x) & \text{CASO DISCRETO} \\ \int_{-\infty}^{\infty} x \cdot f_X(x) \, dx & \text{CASO CONTINUO} \end{cases}
$$

- Nota: similarità con $\bar{x}$ della stat. descrittiva

ES 4.2

Commesso viaggiatore, 2 appuntamenti (indip.):
- $1^\circ$ appuntamento: guadagno $1000$ dollari, prob. $70\%$
- $2^\circ$ " ": " $1500$ dollari, " $40\%$

$X = $ guadagno, v.c.

$$
\begin{array}{c|c}
x & p_X(x) \\
\hline
0 & 0.18 \\
1000 & 0.42 \\
1500 & 0.12 \\
2500 & 0.28 \\
\hline
& 1
\end{array}
\quad
\begin{aligned}
& E(X) = 1300 \text{ dollari} \\
& \quad \uparrow \\
& \text{GUADAGNO ATTESO}
\end{aligned}
$$

---

## Pagina 2

ES 4.3

$X =$ tempo vita dispositivo

$$
f_X(x) = \left\lbrace \begin{array}{ll} \frac{20000}{x^3}, & x > 100 \\ 0, & \text{altrove} \end{array} \right.
$$

$$
\left( \int_{100}^{\infty} \frac{20000}{x^3} dx = 20000 \cdot \left(-\frac{1}{2}\right) \left(x^{-2}\right)\Big|_{100}^{\infty} = 1 \right)
$$

$$
E(X) = \int_{100}^{\infty} x \frac{20000}{x^3} dx = 200 \text{ ore}, \begin{array}{l} \text{DURATA} \\ \text{MEDIA} \end{array}
$$

- PROPOSIZIONE

$$
E[g(X)] = \left\lbrace \begin{array}{ll} \sum_{x} g(x) P_X(x) & \text{CASO DISCR.} \\ \int_{-\infty}^{\infty} g(x) f_X(x) dx & \text{CASO CONT.} \end{array} \right.
$$

Nota: che $Y = g(X)$ sia v.c. è immediato dalla definizione di v.c.; il risultato ci permette di evitare di dover calcolare la distribuzione di $Y$ per calcolare $E(Y)$. Deriva dalle proprietà di sommatorie e integrali.

---

## Pagina 3

- Si estende a funzioni di $2$ (o più) v.c.: (3)

$$
E \left[ g(X,Y) \right] = 
\begin{cases}
\sum_{x} \sum_{y} g(x,y) p_{XY}(x,y) & \text{caso discreto} \\
\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} g(x,y) f_{XY}(x,y) \,dx\,dy & \text{caso continuo}
\end{cases}
$$

Il caso speciale $g(X,Y) = X$ o $g(X,Y) = Y$ sono immediati:

$$
E(X) = \sum_{x} \sum_{y} x \, p_{XY}(x,y) = \sum_{x} x \underbrace{\sum_{y} p_{XY}(x,y)}_{p_{X}(x)}
$$

(caso discreto) (per esempio)

ESERCIZIO 4.3

$C = \text{costo per giocare}$

$Y = \text{vincita netta}$

- vinco $3$ dollari con jack o regina
- vinco $5$ dollari con asso o re

$$
\begin{array}{c|c}
y & p_{Y}(y) \\
\hline
0 - C & 36/52 \\
3 - C & 8/52 \\
5 - C & 8/52 \\
\hline
& 1
\end{array}
$$

$C$ per gioco equo?

$E(Y) = 0$

---

## Pagina 4

$$
E(Y) = (0 - c) \frac{36}{52} + (3 - c) \frac{8}{52} + (5 - c) \frac{8}{52}
$$

$$
= \frac{16}{13} - c \implies c = \frac{16}{13} = 1.23 \text{ dollari}
$$

· ESER. 4.5

Rimborso max $200\,000 \text{ dollari}$ per assicurazione aereo

$$
P(\text{perdita totale}) = 0.002
$$

$$
P(\text{perdita } 50\%) = 0.01
$$

$$
P(\text{perdita } 25\%) = 0.1
$$

Premio per profitto medio $500 \text{ dollari}$?

$$
X = \text{Rimborso} \quad \begin{array}{c|c}
x & P_X(x) \\
\hline
200\,000 & 0.002 \\
100\,000 & 0.01 \\
50\,000 & 0.1 \\
0 & 0.888 \\
\hline
& 1
\end{array}
$$

$$
E(X) = 6400 \text{ dollari} : \text{premio} = 6400 \text{ dollari} + 500 \text{ dollari}
$$

$$
= 6900 \text{ dollari}
$$

---

## Pagina 5

ES 4.12

$$
\begin{array}{c|cc|c}
Y \diagdown X & 2 & 4 & p_Y(y) \\
\hline
1 & 0.10 & 0.15 & 0.25 \\
3 & 0.20 & 0.30 & 0.50 \\
5 & 0.10 & 0.15 & 0.25 \\
\hline
p_X(x) & 0.40 & 0.60 &
\end{array}
$$

$$
1. \; E(XY^2) = \sum_x \sum_y x \, y^2 \, p_{XY}(x,y) = 35.2
$$

$$
2. \; \mu_X = 2(0.40) + 4(0.60) = 3.2
$$

$$
\mu_Y = 1(0.25) + 3(0.50) + 5(0.25) = 3.0
$$

ES 4.14

$$
f_X(x) = \left\lbrace 
\begin{array}{ll}
\displaystyle\frac{1}{2000} \, e^{-\frac{x}{2000}}, & x > 0 \\
0, & x \le 0
\end{array}
\right.
$$

DENSITÀ ESPONENZIALE

$$
E(X) = \frac{1}{2000} \int_0^\infty x \, e^{-x/2000} \, dx
$$

PONGO

$$
z = \frac{x}{2000} \quad \longrightarrow \quad x = z \cdot 2000 \quad dx = dz \cdot 2000
$$

$$
= 2000 \int_0^\infty z \, e^{-z} \, dz = 2000 \cdot 1
$$

$$
\int_0^\infty z \, e^{-z} \, dz \underbrace{=}_{\text{PER PARTI}} \Big[ (-e^{-z}) \, z \Big]_0^\infty + \int_0^\infty e^{-z} \, dz = 1
$$

---

## Pagina 6

# VARIANZA E COVARIANZA (1)

$\text{Def}$ $V(X)$ è la VARIANZA di $X$ (o della sua distribuzione):

$$
\sigma_{X}^{2} = V(X) = E \left[ \left( X - \mu_{X} \right)^{2} \right] = \begin{cases} 
\sum_{x} \left( x - \mu_{x} \right)^{2} p_{X}(x) & \text{CASO DISCRETO} \\
\int_{-\infty}^{+\infty} \left( x - \mu_{X} \right)^{2} f_{X}(x) \, dx & \text{CASO CONTINUO}
\end{cases}
$$

Misura la VARIABILITÀ di $X$

- $\sigma_{X} = \sqrt{V(X)}$ è la DEVIAZIONE STANDARD di $X$

- $\text{Nota:}$ FORMULA DI CALCOLO (analoga a quella vista nella statistica descrittiva)

$$
E \left[ \left( X - \mu_{X} \right)^{2} \right] = E \left( X^{2} \right) - \mu_{X}^{2}
$$

$\text{Prova:}$ (caso continuo, caso discreto è analogo)

$$
V(X) = \int_{-\infty}^{+\infty} \left( x^{2} + \mu_{X}^{2} - 2 x \mu_{X} \right) f_{X}(x) \, dx
$$

$$
= \int_{-\infty}^{+\infty} x^{2} f_{X}(x) \, dx + \mu_{X}^{2} \underbrace{\int_{-\infty}^{+\infty} f_{X}(x) \, dx}_{1} - 2\mu_{X} \underbrace{\int_{-\infty}^{+\infty} x f_{X}(x) \, dx}_{\mu_{X}}
$$

---

## Pagina 7

- Nota: $V(x) = 0 \iff$ V.C. CON DISTRIBUZIONE DEGENERE

$$
\begin{array}{c|c}
x & p_x(x) \\
\hline
a & 1
\end{array}
$$

- $V[g(x)] = E \left\lbrace \left[ g(x) - \mu_{g(x)} \right]^2 \right\rbrace$ (è una costante)

che si calcola come:

$$
\sum_x \left[ g(x) - \mu_{g(x)} \right]^2 p_x(x)
$$

$$
\int_{-\infty}^{+\infty} \left( g(x) - \mu_{g(x)} \right)^2 f_x(x) dx
$$

$\rightarrow$ è l'applicazione di un risultato visto per il valore atteso

\underline{Def} COVARIANZA TRA $X$ e $Y$

$$
\sigma_{XY} = \text{cov}(X,Y) = E \left[ (X - \mu_X)(Y - \mu_Y) \right]
$$

Misura il grado della RELAZIONE LINEARE tra $X$ e $Y$

\underline{Prop} $\text{cov}(X,Y) = E(X \cdot Y) - E(X)E(Y)$

---

## Pagina 8

Di nuovo, possiamo considerare il caso continuo o quello discreto, i passaggi sono gli stessi. Qui prendiamo il caso discreto

$$
\operatorname{Cov}(X,Y) = \sum_x \sum_y (x - \mu_x)(y - \mu_y) \, p_{XY}(x,y)
$$

$$
= \sum_x \sum_y x y \, p_{XY}(x,y) - \mu_x \sum_x \sum_y y \, p_{XY}(x,y)
$$

$$
- \mu_y \sum_x x \sum_y p_{XY}(x,y) + \mu_x \cdot \mu_y \sum_x \sum_y p_{XY}(x,y)
$$

$$
= \sum_x \sum_y x y \, p_{XY}(x,y) - 2\mu_x \cdot \mu_y + \mu_x \cdot \mu_y
$$

$\underline{\qquad\qquad\qquad\qquad\qquad\qquad\qquad}$

$\text{Def}$: COEFFICIENTE DI CORRELAZIONE TRA $X$ e $Y$

$$
\rho_{XY} = \frac{\sigma_{XY}}{\sigma_X \sigma_Y}, \quad -1 \le \rho_{XY} \le 1
$$

- Se $Y = a + bX \implies \left\lbrace \begin{array}{l} \rho_{XY} = 1 \text{ per } b>0 \\ \rho_{XY} = -1 \text{ per } b<0 \end{array} \right. $

Ha la stessa interpretazione di $\sigma_{XY}$, con il vantaggio di essere privo di unità di misura e standardizzato (tra $-1$ e $1$)

---

## Pagina 9

ESEMPIO 4.13

$$
\begin{array}{c|ccc|c}
p_{XY}(x,y) & 0 & 1 & 2 & p_Y(y) \\
\hline
0 & 3/28 & 9/28 & 3/28 & 15/28 \\
\hline
1 & 6/28 & 6/28 & 0 & 12/28 \\
\hline
2 & 1/28 & 0 & 0 & 1/28 \\
\hline
p_X(x) & 10/28 & 15/28 & 3/28 & 1
\end{array}
$$

$$
E(XY) = \sum_{x} \sum_{y} x \, y \, p_{XY}(x,y) = 1 \cdot 1 \cdot \frac{6}{28} = \frac{3}{14}
$$

$$
E(X) = 3/4 \qquad E(Y) = 1/2
$$

$$
\text{cov}(X,Y) = \frac{3}{14} - \frac{3}{4} \cdot \frac{1}{2} = -\frac{9}{56}
$$

$$
V(X) = \frac{45}{112} \qquad V(Y) = \frac{9}{28} \qquad \rho_{XY} = \frac{\sigma_{XY}}{\sigma_X \sigma_Y} = -0.447
$$

---

## Pagina 10

PROPOSIZIONE \hfill (5)

Se $X$ e $Y$ sono v.c. indipendenti $\implies \rho_{XY} = 0$

Prova

$$
E(X \cdot Y) = \sum_{x} \sum_{y} x \, y \, p_{XY}(x,y)
$$

(Caso discreto)

$$
= \left( \sum_{x} x \, p_{X}(x) \right) \left( \sum_{y} y \, p_{Y}(y) \right)
$$

$$
= E(X) \, E(Y) \implies \text{Cov}(X,Y) = 0
$$

--------------------------------------------------

NOTA: Non vale il viceversa, come mostra l'esempio che segue

$$
\begin{array}{c|ccc}
Y \setminus X & -1 & 0 & 1 \\
\hline
0 & 0 & 0.5 & 0 \\
1 & 0.25 & 0 & 0.25
\end{array}
\quad
\begin{array}{l}
p_{XY}(x,y) \text{ per} \\
X \text{ e } Y \\
\text{ discrete}
\end{array}
$$

Si trova facilmente $\rho_{XY} = 0$, ma le due v.c. non sono indipendenti!

$$
(\text{Infatti } Y = |X|)
$$

---

## Pagina 11

(111) COMBINAZIONE LINEARE DI V.C. (1)

Risultati notevoli:

RIS 1 $a, b \in \mathbb{R}; E(aX+b) = a E(X)+b$
$X$ v.c.

Prova: (per $X$, ad es., discreta)

$$
E(aX+b) = \sum_{x} (ax+b) p_X(x)
$$

$$
= a \sum_{x} x p_X(x) + b \sum_{x} p_X(x)
$$

$$
= a \quad E(X) \quad + b
$$

RIS 2 Siano $h$ e $g$ due funzioni $\mathbb{R} \to \mathbb{R}$

$$
E\left[ g(X) + h(X) \right] = E\left[ g(X) \right] + E\left[ h(X) \right]
$$

Prova: si lascia per esercizio ($\text{\`e}$ analoga al caso precedente)

---

## Pagina 12

RIS 3 $a, b \in \mathbb{R}$ \quad $X, Y$ v.c. \hfill (2)

$a X + b Y$ è una COMBINAZIONE LINEARE delle due variabili con pesi $a$ e $b$

$$
E(a X + b Y) = a E(X) + b E(Y)
$$

Prova : (caso discreto)

$$
E(a X + b Y) = \sum_{x} \sum_{y} (a x + b y) \, p_{XY}(x,y)
$$

$$
= a \sum_{x} \sum_{y} x \, p_{XY}(x,y) + b \sum_{x} \sum_{y} y \, p_{XY}(x,y)
$$

$$
= a \, E(X) + b \, E(Y)
$$

utilizzando un risultato visto in precedenza

---

## Pagina 13

RIS 4 $g, h$ funzioni $\mathbb{R}^2 \longrightarrow \mathbb{R}$

$$
E \Big[ g(X, Y) + h(X, Y) \Big] = E \Big[ g(X, Y) \Big] + E \Big[ h(X, Y) \Big]
$$

Prova: si lascia per esercizio


RIS 5 $X_1, X_2, \dots, X_n$ v.c.
$a_1, a_2, \dots, a_n \in \mathbb{R}$

$$
Y = \sum_{i=1}^n a_i X_i \quad \begin{aligned}
&\text{COMBINAZIONE LINEARE} \\
&\text{delle } n \text{ v.c. con} \\
&\text{pesi } a_1, a_2, \dots, a_n
\end{aligned}
$$

$$
E(Y) = \sum_{i=1}^n a_i E(X_i)
$$

Prova: segue da RIS 3 per INDUZIONE


RIS 6 $a, b \in \mathbb{R}$, $X$ v.c.

$$
V(a X + b) = a^2 V(X)
$$

---

## Pagina 14

Prova: $V(\underbrace{aX+b}_{Y}) = E \left[ (Y - \mu_Y)^2 \right]$ (4)

$$
= E \left[ (aX+b - a\mu_X - b)^2 \right]
$$

$$
= E \left[ a^2(X-\mu_X)^2 \right] = a^2 V(X)
$$

RIS 7 $a, b \in \mathbb{R}$, $X, Y$ v.c.

$$
V(aX+bY) = a^2 V(X) + b^2 V(Y) + 2ab \operatorname{cov}(X,Y)
$$

Prova: $V(aX+bY) = E \left\lbrace \left[ (aX+bY) - (a\mu_X + b\mu_Y) \right]^2 \right\rbrace$

$$
= E \left\lbrace \left[ a(X-\mu_X) + b(Y-\mu_Y) \right]^2 \right\rbrace
$$

$$
= E \left\lbrace a^2(X-\mu_X)^2 + b^2(Y-\mu_Y)^2 + 2ab(X-\mu_X) \cdot (Y-\mu_Y) \right\rbrace = \rightarrow \text{applico RIS 5}
$$

$$
= a^2 E \left[ (X-\mu_X)^2 \right] + b^2 E \left[ (Y-\mu_Y)^2 \right] + 2ab \cdot E \left[ (X-\mu_X)(Y-\mu_Y) \right] \text{, ovvero il risultato}
$$

---

## Pagina 15

RIS 8 Se $X$ e $Y$ sono INDIPENDENTI

$$
V(a X + b Y) = a^2 V(X) + b^2 V(Y)
$$

si estende a $n$ v.c. INDIPENDENTI

$$
V\left(\sum_{i=1}^n a_i X_i\right) = \sum_{i=1}^n {a_i}^2 V(X_i)
$$

CASO NOTEVOLE di COMB. LINEARE

Def Date $X_1, \dots, X_n$ v.c.,
$\overline{X} = \frac{1}{n} \sum_{i=1}^n X_i$ è la v.c. MEDIA CAMPIONARIA

Nota: la notazione usata coincide, non a caso, con l'analoga definizione vista in statistica descrittiva. Eseguito l'esperimento, e osservati $n$ valori $x_1, x_2, \dots, x_n$, allora posso calcolare

$$
\overline{x} = \frac{1}{n} \sum_{i=1}^n x_i
$$

---

## Pagina 16

Proprietà di $\overline{X}$: ci interessa soprattutto il (6) caso di $n$ v.c. $i.i.d.$ ovvero INDIPENDENTI e IDENTICAMENTE DISTRIBUITE.

Se la distribuzione è la stessa per tutte le v.c., allora hanno tutte la stessa media e varianza:

$$
E(X_1) = E(X_2) = \dots = E(X_n) = \mu
$$

$$
V(X_1) = V(X_2) = \dots = V(X_n) = \sigma^2
$$

Si ha (da risultati precedenti)

$$
E(\overline{X}) = \mu
$$

$$
V(\overline{X}) = \frac{\sigma^2}{n}
$$

---

## Pagina 17

(1) VALORE ATTESO CONDIZIONATO

- È la media della v.c. basata sulla distribuzione condizionata

$$
E(Y \mid X=x) = \begin{cases}
\sum_{y} y \, p_{Y \mid X}(y \mid x), & \text{caso discreto} \\
\int_{-\infty}^{\infty} y \, f_{Y \mid X}(y \mid x) \, dy, & \text{caso continuo}
\end{cases}
$$

- Interpretazione: è una sintesi della distribuzione di $Y$ quando $X=x$

- Analogamente definiamo la VARIANZA CONDIZIONATA

$$
V(Y \mid X=x)
$$

- Nota: $E(Y \mid X=x)$ e $V(Y \mid X=x)$ dipendono dal valore di $x$!

Se $X$ e $Y$ sono indipendenti

$$
E(Y \mid X=x) = E(Y) \quad \text{e} \quad V(Y \mid X=x) = V(Y)
$$

---

## Pagina 18

III DISTRIBUZIONI DI PROBABILITÀ NOTEVOLI (DISCRETE) (1)

- Alcuni tipi di V.C. ricorrono spesso nella pratica $\implies$ MODELLI DI RIFERIMENTO

- Distribuzioni di probabilità DISCRETE o CONTINUE che dipendono da alcuni PARAMETRI $\vartheta = (\vartheta_1, \vartheta_2, \dots, \vartheta_p)$

$$
p_X(x; \vartheta) \quad \text{caso discreto}
$$

$$
f_X(x; \vartheta) \quad \text{caso continuo}
$$

(II) DISTRIBUZIONE DI BERNOULLI

Esperimento con 2 possibili risultati, "SUCCESSO" o "INSUCCESSO"

$$
1 \quad 0
$$

$$
P(\text{SUCCESSO}) = p \quad P(\text{INSUCCESSO}) = 1-p
$$

$p$, $0 < p < 1$ è il PARAMETRO

---

## Pagina 19

(2)

$$
X = \left\lbrace \begin{array}{ll} 1 & \text{SUCCESSO} \\ 0 & \text{INSUCCESSO} \end{array} \right.
$$

$$
\begin{array}{c|c||l}
x & P_X(x;p) & \\
\hline
0 & 1 - p & P(X=1) = p \\
1 & p & P(X=0) = 1-p
\end{array}
$$

la distribuzione

$$
E(X) = p
$$

$$
V(X) = p(1-p)
$$

In forma compatta: $P_X(x;p) = p^x(1-p)^{1-x}, \, x = 0, 1$

- Notazione:

$$
X \sim \text{Bernoulli}(p)
$$

ES: LANCIOMONETA, $\text{SUCCESSO} \implies \text{esce testa}$

$$
X \sim \text{Bernoulli}(0,5)
$$

---

## Pagina 20

DISTRIBUZIONE BINOMIALE (3)

Processo di Bernoulli:
1. Esperimento formato da $n$ prove ripetute
2. Esito binario (succ. / insucc.)
3. $P(\text{successo}) = p$, costante nelle varie prove
4. Prove INDIPENDENTI

Nota: Quando si hanno $n$ esperimenti indipendenti effettuati nelle stesse condizioni si parla di CAMPIONE CASUALE

$X = n^\circ$ successi nelle $n$ prove

$$
X \sim Bi(n, p) \quad x = 0, 1, \dots, n
$$

$$
0 < p < 1
$$

DISTRIBUZIONE BINOMIALE

ES: Lancio 3 volte un dado, successo $\Rightarrow$ esce $6$

$X = n^\circ$ di $6$ nelle 3 prove

$$
X \sim Bi(3, 1/6)
$$

---

## Pagina 21

Otteniamo la distribuzione: definiamo prima cosa gli eventi

$$
A_i = \left\lbrace \text{Esce } 6 \text{ alla } i\text{-esima prova} \right\rbrace
$$

$$
i = 1, 2, 3
$$

$$
A_1, A_2, A_3 \quad \text{MUTUAMENTE INDIPENDENTI}
$$

$$
P(X=0) = P(A_1^c \cap A_2^c \cap A_3^c)
$$

$$
= P(A_1^c) P(A_2^c) P(A_3^c) = \left(\frac{5}{6}\right)^3
$$

$$
P(X=1) = P(A_1^c \cap A_2^c \cap A_3) + P(A_1^c \cap A_2 \cap A_3^c) + P(A_1 \cap A_2^c \cap A_3^c) = 3 \left(\frac{1}{6}\right)^1 \left(\frac{5}{6}\right)^2
$$

$$
P(X=2) = 3 \left(\frac{1}{6}\right)^2 \left(\frac{5}{6}\right)^1
$$

$$
P(X=3) = \left(\frac{1}{6}\right)^3
$$

In generale: per $X \sim \text{Bi}(n, p)$

$$
P(X=x) = \binom{n}{x} p^x (1-p)^{n-x}, \quad x=0, 1, \dots, n
$$

---

## Pagina 22

* Il testo di Walpole et al. usa una simbologia particolare per $p_X(x; p)$, ovvero

$$
b(x; n, p) = \binom{n}{x} p^x (1-p)^{n-x}
$$

Proprietà:

$i)$ Posto $q = 1-p$ si ha

$$
\underbrace{(p+q)^n}_{1} = \sum_{x=0}^n \binom{n}{x} p^x (1-p)^{n-x} = 1
$$

$$
\llap{\phantom{(p+q)^n = }} \hookrightarrow \text{formula di Newton}
$$

a riprova che la distribuzione è ben definita

$ii)$ MEDIA e VARIANZA

$$
Z_i = \left\lbrace \begin{array}{lcl}
1 & \text{successo} & i\text{-esima prova} \\
0 & \text{insuccesso} & \text{"} \quad \text{"}
\end{array} \right.
$$

$$
Z_i \sim \text{Bernoulli}(p) \quad i = 1, \dots, n
$$

v.c. indipendenti

---

## Pagina 23

6

$$
X = Z_1 + Z_2 + \dots + Z_n
$$

Dai risultati sulle combinazioni lineari:

$$
E(X) = E \left( \sum_{i=1}^n Z_i \right) = \sum_{i=1}^n E(Z_i) = n p
$$

$$
V(X) = V \left( \sum_{i=1}^n Z_i \right) = \sum_{i=1}^n V(Z_i) = n p (1-p)
$$

- Area di applicazione

$\longrightarrow$ ESTRAZIONI CON REINSERIMENTO

- Controllo di qualità : PEZZO DIFETTOSO / NON DIFETTOSO

- Medicina : FARMACO FUNZIONA / NON FUNZIONA

---

## Pagina 24

III DISTRIBUZIONE IPERGEOMETRICA (1)

- Adatta a ESTRAZIONI SENZA REINSERIMENTO

  - $n$ prove, selezione senza reinserimento da $N$ unità

  - $K$ successi, $N-K$ insuccessi

$X = $ $n^\circ$ di successi nelle $n$ prove

$$
X \sim H(N, n, K)
$$

DISTRIBUZIONE IPERGEOMETRICA

$$
P(X=x) = \frac{\binom{K}{x} \binom{N-K}{n-x}}{\binom{N}{n}} = h(x; N, n, K)
$$

METODO DEL CONTEGGIO

Supporto:

$$
\left\lbrace
\begin{aligned}
0 &\leq x \leq n \\
n - (N-K) &\leq x \leq K
\end{aligned}
\right.
$$

$$
\max(0, n-(N-K)) \leq x \leq \min(n, K)
$$

---

## Pagina 25

- ES: 10 oggetti, 3 difettosi, 7 non difettosi

$N = 10$, $k = 7$, $X = n^{\circ}$ di non difettosi

Supporto: se 

$$
\left\lbrace 
\begin{array}{ll}
n = 4 & 1 \le x \le 4 \\
n = 8 & 5 \le x \le 7 \\
n = 3 & 0 \le x \le 3
\end{array}
\right.
$$

Nota: se $k \ge n$ e $N-k \ge n \implies 0 \le x \le n$

- PROPOSIZIONE

$$
E(X) = n \frac{k}{N} = n p \text{ se pongo } p = \frac{k}{N}
$$

$$
V(X) = n \frac{k}{N} \left( 1 - \frac{k}{N} \right) \frac{N-n}{N-1}
$$

$$
= n p (1-p) \frac{N-n}{N-1}
$$

Prova: (pura algebra, la prendiamo per buona)

---

## Pagina 26

Confronto con la binomiale: (3)

- Se estraggo CON REINSERIMENTO $X \sim \text{Bi}(n, p)$
- " " SENZA " " e $n \leq 0.05 N$

$$
H(N, n, K) \approx \text{Bi}\left(n, \frac{K}{N}\right)
$$

Se $n$ è piccolo in confronto a $N$ posso agire come se le estrazioni avvengano CON REINSERIMENTO!

- La distribuzione ipergeometrica si estende a più di 2 categorie, ma è poco usata

- UTILIZZO DELLA DISTRIBUZIONE IPERGEOMETRICA NEL CAMPIONAMENTO PER ACCETTAZIONE

Esercizio $5.18$

- Lotto $N = 50$, ne campiono $n = 5$ e accetto il lotto se al max $2$ sono difettosi

---

## Pagina 27

Proporzione di lotti con il 20% che saranno accettati? (4)

$$
K = 10 \qquad X = n^{\circ} \text{ difettosi } n = 5
$$

$$
X \sim H(50, 5, 10), \quad 0 \leq x \leq 5
$$

$$
P(X \leq 2) = \sum_{x=0}^{2} \frac{\binom{10}{x}\binom{40}{5-x}}{\binom{50}{5}} = 0.9517
$$

- Se uso $X \sim \text{Bi}(5, 0.2)$, $P(X \leq 2) = 0.9421$

- Esercizio 3.6

$$
N = 7 \quad K = 2 \text{ difettosi } \quad n = 3
$$

$$
X = n^{\circ} \text{ difettosi} \quad X \sim H(7, 3, 2)
$$

$$
x = 0, 1, 2
$$


$$
\begin{array}{c|c}
x & P_X(x) \\
\hline
0 & 2/7 \\
1 & 4/7 \\
2 & 1/7
\end{array}
$$

---

## Pagina 28

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

---

## Pagina 29

(2)

$$
\lim_{N \to \infty} P(X=n) = \lim_{N \to \infty} \frac{N!}{(N-n)! n!} \cdot \frac{\lambda^n}{N^n} \cdot \left(1 - \frac{\lambda}{N}\right)^N \cdot \left(1 - \frac{\lambda}{N}\right)^{-n}
$$

ovvero

$$
\lim_{N \to \infty} P(X=n) = \frac{\lambda^n e^{-\lambda}}{n!}
$$

$$
n = 0, 1, \dots
$$

- Il risultato giustifica la seguente definizione

$\underline{\text{Def}}$ $X$ v.c. di Poisson, con supporto $n = 0, 1, 2, \dots$

$$
P(X=n) = e^{-\lambda} \frac{\lambda^n}{n!}
$$

Commenti:
- È approssimazione della binomiale per $n$ elevato, $p$ piccolo e $\lambda = np$ costante
- Va bene per conteggi senza limite superiore

---

## Pagina 30

Proprietà:

$$
\left\lbrace
\begin{aligned}
E(X) &= \lambda \\
V(X) &= \lambda
\end{aligned}
\right.
\quad
\begin{aligned}
&\text{segue da proprietà delle} \\
&\text{serie, ma anche dalla} \\
&\text{approssimazione binomiale}
\end{aligned}
$$

(1) PROCESSO DI POISSON (omogeneo)

1. ARRIVI indipendenti nel tempo o nello spazio
2. Non ci sono arrivi simultanei
3. $\lambda$ tasso di arrivi medio in una unità di tempo (è lo stesso per tutte le unità)

$$
X = n^\circ \text{ arrivi in } t \text{ unità di } \begin{aligned}[t]&\text{tempo} \\ &\text{(spazio)}\end{aligned}
$$

$$
1 + 2 + 3 \implies X \sim \text{Poisson}(\lambda t)
$$

$$
(o \text{ anche si indica } \mathcal{P}(\lambda t))
$$

- ES: Accessi sito web (in un intervallo di tempo)

$$
\lambda = 5 \text{ accessi al minuto}
$$

$$
P(17 \text{ accessi in } 3 \text{ minuti}) = e^{-15} \frac{15^{17}}{17!} = 0.0847
$$

---

## Pagina 31

Infatti: $X = n^{\circ}$ accessi in $3$ minuti

$$
X \sim \mathcal{P}(\underbrace{1 \cdot 3}_{15})
$$

Proprietà:

$X_1 \sim \mathcal{P}(\lambda_1)$, $X_2 \sim \mathcal{P}(\lambda_2)$ indip.

$$
X_1 + X_2 \sim \mathcal{P}(\lambda_1 + \lambda_2)
$$

(Prova: si utilizza la FUNZIONE GENERATRICE DEI MOMENTI, che vedremo)

ES: Viaggiatori transito per stazione

$X_1 = n^{\circ}$ arrivi tipo $1$ (pendolari lavoratori)

$X_2 = " \quad " \quad " 2 ($ $" \quad studenti)$

$X_3 = " \quad " \quad " 3 ($ occasionali $)$

$\vdots$

$X_K = " \quad " \quad " K ($ $\dots$ $)$

VIAGGIATORI TOTALI $X_T = X_1 + X_2 + \dots + X_K \sim \mathcal{P}(\lambda_1 + \lambda_2 + \dots + \lambda_K)$

---

## Pagina 32

DISTRIBUZIONE UNIFORME CONTINUA

- $X$ v.c. continua con $f$ di densità costante nell'intervallo $(a, b)$, con $a, b \in \mathbb{R}$

$$
X \sim \mathcal{U}(a, b) \quad , \quad f_X(x; a, b) = \left\lbrace 
\begin{array}{ll}
\frac{1}{b-a} & , \, a \leq x \leq b \\
0 & \text{altrove}
\end{array}
\right.
$$

$$
E(X) = \frac{a+b}{2} \quad \text{per la simmetria}
$$

$$
V(X) = \frac{(b-a)^2}{12} \quad , \text{calcoli semplici}
$$

$$
F_X(x; a, b) = \left\lbrace 
\begin{array}{cc}
0 & x \leq a \\
\frac{x-a}{b-a} & a \leq x \leq b \\
1 & x \geq b
\end{array}
\right.
$$

---

## Pagina 33

III DISTRIBUZIONE NORMALE 2

$$
f_X(x; \mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}, \quad x \in \mathbb{R}
$$

$$
X \sim N(\mu, \sigma^2)
$$

$$
n(x; \mu, \sigma) \quad (\text{Walpole et al.})
$$

- È la più importante distribuzione continua, si trova in moltissimi fenomeni fisici, biologici e anche socio-economici.

- Il grafico della $f.$ di densità è la famosa "campana di Gauss".

[Inserire grafico della campana di Gauss centrata in $\mu$]

- Si trova $E(X) = \mu$ (per simmetria), mentre $V(X) = \sigma^2$ richiede l'integrazione per parti.

---

## Pagina 34

* Proprietà: per qualsiasi scelta di $\mu \in \mathbb{R}$ e $\sigma > 0$ (Prova: vedi $F_x$)

$$
P(\mu - \sigma \le X \le \mu + \sigma) \simeq 0.68
$$

$$
P(\mu - 2\sigma \le X \le \mu + 2\sigma) \simeq 0.95
$$

$$
P(\mu - 3\sigma \le X \le \mu + 3\sigma) \simeq 0.99
$$

Ecco perché possiamo utilizzare la distribuzione anche per grandezze fisiche che hanno un campo di variazione limitato (pesi, lunghezze ecc.)

* STANDARDIZZAZIONE

Sia $X \sim \mathcal{N}(\mu, \sigma^2)$, definiamo

$$
Z = \frac{X - \mu}{\sigma} : \text{si ha } Z \sim \mathcal{N}(0, 1)
$$

---

## Pagina 35

* Il risultato è un caso speciale di un risultato più generale: se $a, b \in \mathbb{R}$

$$
a + bX \sim \mathcal{N} \left( a + b\mu, \, b^2\sigma^2 \right)
$$

Prova: si dimostra tramite la FUNZIONE GENERATRICE DEI MOMENTI, che vedremo (f.g.m.)

* Def $Z \sim \mathcal{N}(0,1)$ è la DISTRIBUZIONE NORMALE STANDARD (o STANDARDIZZATA)

Notazione:

$$
f_Z(z; 0, 1) = \phi(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}}
$$

$$
F_Z(z; 0, 1) = \Phi(z) = \int_{-\infty}^{z} \phi(t) \, dt
$$

$\ll$ non ammette forma analitica: esistono però tabelle, le TAVOLE DELLA NORMALE

---

## Pagina 36

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

---

## Pagina 37

- PERCENTILI di $X \sim N(\mu, \sigma^2)$  (6)

$x_\alpha$: $F_X(x_\alpha, \mu, \sigma) = \alpha$, $0 < \alpha < 1$

$$
\Phi \left( \frac{x_\alpha - \mu}{\sigma} \right) = \alpha
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
x_\alpha = \mu + \sigma \, z_\alpha
$$

- Si noti: $\Phi(z_\alpha) = \alpha$, $z_\alpha = \Phi^{-1}(\alpha)$

$$
\uparrow
$$

FUNZIONE QUANTILE

e per la simmetria di $\phi(z)$ attorno a $z=0$ si ottiene:

$$
z_{1-\alpha} = - z_\alpha
$$

- Percentili notevoli

$$
z_{0.95} = 1.645
$$

$$
z_{0.975} = 1.96
$$

$$
z_{0.99} = 2.33 \quad z_{0.995} = 2.58
$$

---

## Pagina 38

ESEMPIO (7)

$X = \text{durata certo tipo di batteria (ore)}$

$X \sim N(50, 25) \rightarrow \mu = 50, \sigma = 5$

$x_{0.05} = \sigma z_{0.05} + \mu = 50 + 5(-1.645)$

$= 41.775 \text{ ore}$

$x_{0.95} = \sigma z_{0.95} + \mu = 50 + 5(1.645)$

$= 58.225 \text{ ore}$

[Disegno di una distribuzione normale con media 50, percentili 41.775 e 58.225, aree evidenziate 0.05, 0.90, 0.05]

ESEMPIO 6.5

$X \sim N(300, 50^2)$

$P(X > 362) = P\left(Z > \frac{362 - 300}{50}\right)$

$Z \sim N(0,1)$

$= P(Z > 1.24)$

$= 1 - \Phi(1.24) = 0.1075$

---

## Pagina 39

LA DISTRIBUZIONE NORMALE: COMPLEMENTI DI TEORIA (1)

- Un risultato notevole:

PROPOSIZIONE

Se $X_1, X_2, \dots, X_n$ v.c. INDIPENDENTI

con $X_i \sim N(\mu_i, \sigma_i^2)$ e $a_1, a_2, \dots, a_n \in \mathbb{R}$

$$
Y = \sum_{i=1}^n a_i X_i \sim N\left(\sum_{i=1}^n a_i \mu_i, \sum_{i=1}^n a_i^2 \sigma_i^2\right)
$$

Prova: si ottiene tramite la $f.g.m.$ (che vedremo)

- CASO NOTEVOLE: $\mu_i = \mu$, $\sigma_i^2 = \sigma^2$, $a_i = \frac{1}{n} \quad \forall i$

$$
\overline{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right) \quad \begin{array}{l} \text{v.c.} \\ \text{MEDIA} \\ \text{CAMPIONARIA} \end{array}
$$

- È un risultato molto importante per la statistica inferenziale, come pure il risultato che segue

---

## Pagina 40

10. TEOREMA DEL LIMITE CENTRALE (TLC)

$X_1, X_2, \dots, X_n \quad \boxed{i.i.d.}$

$E(X_i) = \mu, \quad V(X_i) = \sigma^2$

sia $Z_n = \frac{\overline{X} - \mu}{\sigma/\sqrt{n}}$

allora $\lim_{n \to \infty} F_{Z_n}(z) = \Phi(z), \quad \forall z \in \mathbb{R}$

(Prova: anche qui si usa la f.g.m.)

- Interpretazione operativa del risultato:

per $n$ elevato, $Z_n \stackrel{a}{\sim} N(0, 1)$

ovvero

$$
\overline{X} \stackrel{a}{\sim} N\left(\mu, \frac{\sigma^2}{n}\right)
$$

- Si può esprimere per la somma:

$$
\sum_{i=1}^{n} X_i \stackrel{a}{\sim} N(n\mu, n\sigma^2)
$$

---

## Pagina 41

Osservazioni:

- vale per ogni distribuzione, l'approssimazione è migliore per distribuzioni simmetriche e continue
- se $X_i \sim \mathcal{N}(\mu, \sigma^2)$, il risultato è esatto (non occorre invocare il teorema)
- per $n \ge 30$ generalmente si ottiene una buona approssimazione

DUE CASI NOTEVOLI

BINOMIALE $X \sim Bi(n, p)$

$X = \sum_{i=1}^{n} Z_i$, $Z_i \sim Bernoulli(p)$

Applicando il TLC:

$\frac{X}{n} \stackrel{a}{\sim} \mathcal{N}\left(p, \frac{p(1-p)}{n}\right)$

$X \stackrel{a}{\sim} \mathcal{N}(np, np(1-p))$

APPROSSIMAZIONE NORMALE DELLA BINOMIALE

---

## Pagina 42

- L'approssimazione è ritenuta buona se

$$
\begin{matrix}
\left\lbrace 
\begin{matrix}
n p \ge 5 \\
n(1-p) \ge 5
\end{matrix}
\right.
\end{matrix}
$$

- Correzione di continuità (cc):

$$
\begin{matrix}
\left\lbrace 
\begin{matrix}
P(X \le n) = \Phi \left( \frac{n + 0.5 - n p}{\sqrt{n p(1-p)}} \right) \\
P(X < n) = \Phi \left( \frac{n - 0.5 - n p}{\sqrt{n p(1-p)}} \right)
\end{matrix}
\right.
\end{matrix}
$$

- POISSON $x_1, x_2, \dots, x_n$ iid, $x_i \sim P(\lambda)$

$$
\sum_{i=1}^n X_i \sim P(n\lambda) \text{ ma anche}
$$

$$
\sum_{i=1}^n X_i \stackrel{a}{\sim} \mathcal{N}(n\lambda, n\lambda)
$$

Quindi: se

$$
X \sim P(\lambda) \implies X \stackrel{a}{\sim} \mathcal{N}(\lambda, \lambda)
$$

L'approssimazione è ritenuta buona se $\lambda \ge 10$; anche qui possiamo applicare una cc di $0.5$

---

## Pagina 43

- ESERCIZIO $6.14$

$p = P(\text{Recupero}) = 0.9$

$X = \text{n}^\circ \text{ pazienti che recuperano } (\text{su } 100)$

$X \sim \text{Bi}(100, 0.9)$, ovvero $X \approx \mathcal{N}(90, 9)$

1. $P(84 \leq X \leq 95) =$

$= P(83.5 < X < 95.5) \qquad Z \approx \mathcal{N}(0, 1)$

$= P(-2.17 < Z < 1.83)$

$\simeq 0.9514 \quad \begin{bmatrix} \text{senza CC: } 0.9295 \\ \text{esatta } : 0.9556 \end{bmatrix}$

2. $P(X < 86) = P(X < 85.5) \simeq \Phi(-1.50)$

$$
\underbrace{\quad \quad \quad \quad \quad \quad \quad \quad \quad \quad}_{0.0668}
$$

$\begin{bmatrix} \text{senza CC: } 0.0912 \\ \text{esatta } : 0.0726 \end{bmatrix}$

---

## Pagina 44

ESEMPIO

$X = n^{\circ}$ particelle in una sospensione di $5ml$

$\lambda = 50$ particelle/ml $\longrightarrow$ TASSO MEDIO

Calcolare

a) $P(235 \le X \le 265)$

Sotto le ipotesi del processo di Poisson (che sono ragionevoli in questo caso)

$$
X \sim \mathcal{P}(250)
$$

Usiamo il TLC: $X \stackrel{a}{\sim} \mathcal{N}(250, 250)$

Si ottiene

$$
P(-0.95 \le Z \le 0.55) = 0.6572
$$

$$
\left[
\begin{aligned}
\cdot \text{ con } CC &: 0.6730 \\
\cdot \text{ esatta } &: 0.6731
\end{aligned}
\right]
\qquad \begin{aligned}
\uparrow \\
\text{senza } CC
\end{aligned}
$$

b) $P(48 \le \overline{X} \le 52)$, $\overline{X} = n^{\circ} \text{medio}$ particelle/ml

---

## Pagina 45

$$
\overline{X} = \frac{X}{5} \stackrel{a}{\sim} \mathcal{N}(50, 10)
$$

$$
\left( \text{NB: non è } \overline{X} \stackrel{a}{\sim} \mathcal{N}(50, 50) ! \right)
$$

$$
P\left( 48 \le \overline{X} \le 52 \right) \simeq 0.4714
$$

c) Quanto deve essere il volume prelevato per ottenere una probabilità del punto precedente pari a $0.95$?

$$
\overline{X} = \frac{X}{v} \quad, v = \text{volume prelevato}
$$

$$
\overline{X} \stackrel{a}{\sim} \mathcal{N}\left(50, \frac{50}{v}\right)
$$

(Grafico della normale con area tratteggiata pari a $0.95$)

$$
50 - (1.96)\sqrt{\frac{50}{v}} \quad 50 \quad 50 + \sqrt{\frac{50}{v}} \cdot (1.96)
$$

Ovvero:

$$
52 = 50 + \frac{\sqrt{50}}{\sqrt{v}} (1.96) \Rightarrow V = 48.02 \text{ ml}
$$

---

## Pagina 46

DISTRIBUZIONE LOGNORMALE (8)

- Adatta per fenomeni ASIMMETRICI, con occasionali OUTLIERS

Sia $X \sim \mathcal{N}(\mu, \sigma^2)$, allora $Y = e^X$ ha una distribuzione LOGNORMALE di parametri $\mu$ e $\sigma^2$


$$
Y \sim \log\mathcal{N} (\mu, \sigma^2)
$$


- Ricaviamo la distribuzione di $Y$:

$$
F_Y (y; \mu, \sigma) = P(Y \leq y) \quad \text{per } \sigma > 0
$$

$$
= P(e^X \leq y) = P(X \leq \log(y))
$$

ovvero 

$$
F_Y(y; \mu, \sigma) = \Phi\left(\frac{\log(y) - \mu}{\sigma}\right)
$$

- Per la densità basta calcolare la derivata, ricordando che

$$
\Phi'(z) = \phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}
$$

---

## Pagina 47

per $y > 0$

$$
f_Y(y; \mu, \sigma) = \phi \left( \frac{\log(y) - \mu}{\sigma} \right) \cdot \frac{1}{\sigma} \cdot \frac{1}{y}
$$

ovvero:

$$
f_Y(y; \mu, \sigma) = \left\lbrace \begin{array}{ll} 0, & y \le 0 \\ \frac{1}{\sqrt{2\pi}\sigma y} e^{-\frac{(\log(y)-\mu)^2}{2\sigma^2}}, & y > 0 \end{array} \right.
$$

- Grafici: si veda Fig. 6.29

- ESEMPIO 6.22

$$
X \sim \log N (3.2, 1)
$$

$$
\log(X) \sim N(3.2, 1)
$$

$$
P(X > 8) = P(\log(X) > \log(8))
$$

$$
= 1 - \Phi \left( \frac{\log(8) - 3.2}{1} \right)
$$

$$
= 0.8688
$$

---

## Pagina 48

- Proprietà: se $Y \sim \log N(\mu, \sigma^2)$ (10)

$$
E(Y) = e^{\mu + \sigma^2/2}
$$

$$
V(Y) = e^{2\mu + 2\sigma^2} - e^{2\mu + \sigma^2}
$$

(Si trovano mediante f.g.m. di $\log(Y)$)

- $y_\alpha = e^{\mu + \sigma z_\alpha}$, sfrutto i percentili di $X = \log(Y)$

ESEMPIO 6.23

$Y =$ miglia vita di un dispositivo

$$
Y \sim \log N (\mu, \sigma^2), \quad \begin{aligned}
\mu &= 5.149 \\
\sigma &= 0.737
\end{aligned}
$$

$$
y_{0.05} = e^{5.149 + (0.737)(-1.645)}
$$

$$
= e^{3.537} = 51.625 \text{ miglia}
$$

---

## Pagina 49

(III) DISTRIBUZIONI DI DURATA (1)

Adatte a modellare la "durata di vita" (tempo di funzionamento corretto) di componenti di vario tipo. In opportune situazioni, anche Normale e Lognormale possono essere adatte a modellare tempi, ma le più usate distribuzioni di durata sono

* Esponenziale
* Gamma
* Weibull

(III) Esponenziale

$X$ v.c. con f. di densità, per $\beta > 0$

$$
f_X (x; \beta) = \left\lbrace \begin{array}{ll} \frac{1}{\beta} e^{-\frac{x}{\beta}}, & x > 0 \\ 0 & x \le 0 \end{array} \right.
$$

$X \sim \mathcal{E}(1/\beta)$ o anche $X \sim \text{Exp}(1/\beta)$

---

## Pagina 50

Nota: talvolta la distribuzione viene parametrizzata in $\lambda = \dfrac{1}{\beta}$ (TASSO, $\lambda$, PARAMETRO DI SCALA, $\beta$). 
($\text{\`e}$ del tutto equivalente), $X \sim \mathcal{E}(\lambda)$

- F. di RIPARTIZIONE:

$$
F_X(x; \beta) = \left\lbrace 
\begin{array}{ll}
0 & x \le 0 \\
1 - e^{-\dfrac{x}{\beta}}, & x > 0
\end{array}
\right.
$$

$$
E(X) = \beta
$$

$$
V(X) = \beta^2
$$

Integrale per parti

- Percentili: $0 < \alpha < 1$

$$
1 - e^{-\alpha/\beta} = \alpha
$$

$$
\implies x_\alpha = -\left[ \log(1-\alpha) \right] \beta
$$

---

## Pagina 51

* RELAZIONE CON IL PROCESSO DI POISSON ($\rightarrow$ file d'attesa) (3)

PROPOSIZIONE: Dato un Processo di Poisson di tasso $\lambda > 0$, il tempo $T$ che intercorre tra 2 arrivi consecutivi è $T \sim \mathcal{E}(\lambda)$

Prova

- Otteniamo $F_T(t)$, verificando che ha la forma tipica della distribuzione esponenziale.

- Se $t \le 0$ ovviamente $P(T \le 0) = 0$
  $\downarrow$
  è un tempo

- Se $t > 0$: per calcolare $P(T \le t)$ introduciamo la v.c. $X$

$$
X = n^\circ \text{ arrivi in } [0, t]
$$

$$
X \sim \mathcal{P}(\lambda t)
$$

$$
P(T > t) = P(X=0) = e^{-\lambda t}, \text{ quindi } P(T \le t) = 1 - e^{-\lambda t}
$$

(PASSAGGIO CHIAVE)

---

## Pagina 52

* PROPRIETÀ DI ASSENZA DI MEMORIA

$$
X \sim \mathcal{E}(1/\beta) \qquad t > 0, t_0 > 0
$$

$$
P(X > t_0 + t \mid X > t_0) = P(X > t)
$$

Infatti:

$$
\begin{aligned}
P(X > t_0 + t \mid X > t_0) &= \frac{P(X > t_0 + t)}{P(X > t_0)} \\
&= \frac{e^{-\frac{(t_0 + t)}{\beta}}}{e^{-\frac{t_0}{\beta}}} &= e^{-t/\beta} = P(X > t)
\end{aligned}
$$

* Nota: la proprietà implica la MANCANZA D'USURA per il componente

$\hookrightarrow$ la distribuzione è adatta come modello per il tempo di funzionamento solo in condizioni molto particolari

---

## Pagina 53

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

---

## Pagina 54

- PARAMETRIZZAZIONE ALTERNATIVA : $6$

$$
\lambda = 1 / \beta
$$

TASSO $\swarrow$

- Se $\alpha = 1 \implies X \sim \mathcal{E} (1/\beta)$

ALTRI CASI PARTICOLARI

- Se $\alpha$ e' INTERO $\implies$ DISTRIBUZIONE DI ERLANG

- Se $\alpha = \frac{k}{2}$ ($k$ intero), $\beta = 2 \implies$ DISTRIBUZIONE CHISPAZIO-QUADRATO

- Proprietà: 

$$
\left\lbrace 
\begin{aligned}
E(X) &= \alpha \beta \\
V(X) &= \alpha \beta^2
\end{aligned}
\right.
$$

- Teorema $\longrightarrow$ RELAZIONE CON IL PROCESSO DI POISSON
$X_1, X_2, \dots, X_n$ indip. $X_i \sim \mathcal{E}(1/\beta)$

$$
Y = \sum_{i=1}^{n} X_i \sim \mathcal{G}a (n, 1/\beta)
$$

Prova: usa la $f.g.m.$

---

## Pagina 55

* Proprietà: se $\alpha$ è intero (distribuzione di Erlang) si può ottenere la $F_X$

Per $x > 0$:

$$
F_X(x; \alpha, \beta) = 1 - \sum_{j=0}^{\alpha-1} \frac{e^{-x/\beta} (x/\beta)^j}{j!}
$$

$\rightarrow$ F. di RIPARTIZIONE v.c. ERLANG

* Commenti: la distribuzione gamma offre un modello molto più flessibile della distribuzione esponenziale; per $\alpha \neq 1$ non gode della proprietà di assenza di memoria $\rightarrow$ adatta a modellare fenomeni affetti da usura
* Ha inoltre un ruolo in relazione al processo di Poisson

---

## Pagina 56

10 DISTRIBUZIONE WEIBULL

* Come la distribuzione gamma, estende la distr. esponenziale ma è molto più flessibile

$$
X \sim \text{Weibull}(\alpha, \beta)
$$

$$
f_X(x; \alpha, \beta) = \left\lbrace
\begin{array}{ll}
\alpha \beta x^{\beta-1} e^{-\alpha x^\beta}, & x > 0 \\
0, & x \leq 0
\end{array}
\right.
$$

$\alpha > 0$, $\beta > 0$ (parametro di forma)

* Se $\beta = 1$, $X \sim \mathcal{E}(\alpha)$

* $F$ di ripartizione per $x > 0$:

$$
F_X(x; \alpha, \beta) = \int_0^x \alpha \beta t^{\beta-1} e^{-\alpha t^\beta} dt
$$

poniamo 

$$
\begin{array}{l}
u = \alpha t^\beta \\
du = \alpha \beta t^{\beta-1} dt
\end{array}
$$

---

## Pagina 57

$$
= \int_0^{\alpha x^\beta} e^{-u} du = 1 - e^{-\alpha x^\beta}
$$

Avendo:

$$
F_X(x; \alpha, \beta) = \begin{cases}
0, & x \le 0 \\
1 - e^{-\alpha x^\beta}, & x > 0
\end{cases}
$$

- Con passaggi analoghi si ottiene:

$$
E(X) = \frac{\Gamma\left(1 + \frac{1}{\beta}\right)}{\alpha^{1/\beta}}
$$

- TASSO DI GUASTO

$X$ V.C. DI DURATA (QUALSIASI)

$$
Z(x) = \frac{f_X(x)}{1 - F_X(x)}, \quad x > 0
$$

$$
1 - F_X(x) = \int_x^\infty f_X(t) dt \quad \text{AFFIDABILITÀ}
$$

La definizione di $Z(x)$ deriva dalla

$$
P(x < X < x + \varepsilon \mid X > x) = \frac{F_X(x + \varepsilon) - F_X(x)}{1 - F_X(x)} \quad \text{per } \varepsilon > 0
$$

---

## Pagina 58

(10)

perciò

$$
\lim_{\varepsilon \to 0^+} \frac{P(x < x < x + \varepsilon \mid x > x)}{\varepsilon} = \frac{f_x(x)}{1 - F_x(x)} = z(x)
$$

- Se $x \sim \text{Weibull}(\alpha, \beta)$

$$
z(x) = \alpha \beta x^{\beta-1}, \quad x > 0
$$

- per $\beta = 1$: $z(x) = \alpha$, ASSENZA DI MEMORIA

- per $\beta > 1$: $z(x)$ cresce con $x$, il componente si degrada nel tempo. È il caso tipico.

- per $\beta < 1$: $z(x)$ decresce con $x$, il componente si rafforza nel tempo. Poco comune.

---

## Pagina 59

# La funzione generatrice dei momenti

* Data una v.c. $X$, la sua **funzione generatrice dei momenti** (**f.g.m.**) è la funzione reale con argomento $t \in \mathbb{R}$

$$
m_X(t) = E \left( e^{t X} \right)
$$

ovvero

$$
m_X(t) = \begin{cases}
\sum e^{t x} p_X(x) & \text{se } X \text{ è discreta} \\
\int_{-\infty}^{+\infty} e^{t x} f_X(x)dx & \text{se } X \text{ è continua}
\end{cases}
$$

* La f.g.m. esiste se la sommatoria o l'integrale sono finiti in un intervallo aperto che contiene lo zero, ovvero del tipo $(-t_0, t_0)$, con $t_0 > 0$.

---

## Pagina 60

Proprietà della f.g.m.

La f.g.m. (che nel caso continuo è simile alla trasformata di Fourier della funzione di densità) gode di alcune importanti proprietà:

1. Il comportamento della funzione nel punto $0$ è rilevante

$$
\begin{aligned}
m_X(0) &= 1 \\
m'_X(0) &= E(X) \\
m''_X(0) &= E(X^2) \\
\dots &\quad \dots \\
m^{(n)}_X(0) &= E(X^n)
\end{aligned}
$$

2. Non è detto che la f.g.m. esista, ma **se esiste determina la distribuzione**, ovvero è in corrispondenza $1:1$ con la funzione di ripartizione di $X$ (e quindi con $p_X$ o $f_X$);

---

## Pagina 61

Proprietà della f.g.m.

3. Se $X$ e $Y$ sono indipendenti, si ottiene

$$
m_{X+Y}(t) = m_X(t) m_Y(t) \,.
$$

Più in generale: se $X_1, \dots, X_n$ sono indipendenti, e $S_n = \sum_{i=1}^n X_i$

$$
m_{S_n}(t) = \prod_{i=1}^n m_{X_i}(t) \,,
$$

e se le $X_i$ hanno tutte la stessa distribuzione

$$
m_{S_n}(t) = (m_X(t))^n \,.
$$

Commento: la proprietà 1. dà il nome al metodo (e a volte è utile), ma le proprietà importanti sono la 2. e la 3.

a.a 2024/2025 — R. Bellio
3 / 7

---

## Pagina 62

Alcune f.g.m. notevoli

$$
\begin{array}{|c|c|c|}
\hline
\text{Distribuzione di } X & m_X(t) & \text{Definita per} \\
\hline\hline
Bi(n, p) & (1 - p + e^t p)^n & \forall t \in \mathbb{R} \\
\hline
\mathcal{P}(\lambda) & e^{\lambda (e^t - 1)} & \forall t \in \mathbb{R} \\
\hline
\mathcal{N}(\mu, \sigma^2) & e^{\mu t + \frac{1}{2} \sigma^2 t^2} & \forall t \in \mathbb{R} \\
\hline
\mathcal{G}a(\alpha, 1/\beta) & \left(\frac{1}{1 - t \beta}\right)^\alpha & t < \frac{1}{\beta} \\
\hline\hline
\end{array}
$$

---

## Pagina 63

# Applicazioni notevoli

Usando le proprietà della f.g.m. si possono ottenere molti risultati sulle v.c.

* Otteniamo la f.g.m. di $X + Y$, con $X \sim \mathcal{P}(\lambda_1)$ e $Y \sim \mathcal{P}(\lambda_2)$, indipendenti

* dalla proprietà $3.$ (e usando la tabella) si ottiene

$$
m_{X+Y}(t) = m_X(t) \, m_Y(t) = e^{\lambda_1 (e^t - 1)} \, e^{\lambda_2 (e^t - 1)},
$$

$$
m_{X+Y}(t) = e^{(\lambda_1 + \lambda_2)(e^t - 1)}
$$

* Si riconosce la f.g.m. di una distribuzione $\mathcal{P}(\lambda_1 + \lambda_2)$, e allora dalla proprietà $2.$ segue che

$$
X + Y \sim \mathcal{P}(\lambda_1 + \lambda_2)
$$

* Il risultato si estende ad una somma di un numero qualsiasi di v.c. di Poisson indipendenti.

---

## Pagina 64

Applicazioni notevoli

* Si procede in maniera analoga per trovare la distribuzione della somma di v.c. normali, Gamma (con lo stesso parametro di scala $\beta$) o binomiali (con lo stesso parametro $p$) indipendenti.

* Analogamente, si ottiene la distribuzione di trasformazione lineare di una v.c. normale: i passi sono i seguenti
  * Sia $X \sim \mathcal{N}(\mu, \sigma^2)$ e $Y = a + b X$, con $a, b \in \mathbb{R}$
  * Si ottiene facilmente che

$$
m_Y(t) = E[e^{(a+b X)t}] = e^{a t} m_X(b t) = e^{(a+b\mu)t + b^2 t^2 \sigma^2/2},
$$

  e si riconosce la f.g.m. di una distribuzione $\mathcal{N}(a+b\mu, b^2 \sigma^2)$, per cui

$$
Y \sim \mathcal{N}(a+b\mu, b^2 \sigma^2).
$$

---

## Pagina 65

Applicazioni notevoli (continua)

* Un'altra applicazione notevole è quella per ottenere la distribuzione di una combinazione lineare di v.c. normali indipendenti.
* Anche il teorema del limite centrale si dimostra utilizzando la f.g.m.: se $X_1, \dots, X_n$ sono i.i.d. con $E(X_i) = \mu$ e $V(X_i) = \sigma^2$, si può verificare che la f.g.m. della v.c.

$$
Z_n = \frac{\overline{X} - \mu}{\sqrt{\frac{\sigma^2}{n}}}
$$

tende alla f.g.m. di una $\mathcal{N}(0, 1)$ per $n \to \infty$.

* Un altro risultato è che se $X \sim \mathcal{N}(\mu, \sigma^2)$, allora

$$
m_X(1) = E \left( e^X \right) = e^{\mu + \frac{1}{2}\sigma^2}
$$

è la media di $Y = e^X$ con distribuzione $\text{lognormale}(\mu, \sigma^2)$.

---

## Pagina 66

Introduzione all'inferenza statistica:
campionamento e distribuzioni campionarie

a.a $2024/2025$ --- R. Bellio

$1 / 28$

---

## Pagina 67

Inferenza Statistica

* Il punto di partenza di una indagine statistica è costituito da un insieme (la **popolazione di riferimento**), che costituisce l'ambito di interesse;
* gli elementi di questo insieme (persone, componenti elettronici, titoli azionari, $\dots$ ) vengono indicati come **unità statistiche**;
* sono disponibili dei **dati**, ovvero delle misurazioni/rilevazioni di certe caratteristiche di interesse, ottenuti per una parte delle unità statistiche (il **campione**, da cui *indagini campionarie*);
* una descrizione delle caratteristiche del campione è in genere ottenuta mediante tecniche di **statistica descrittiva**;
* l'**inferenza statistica** utilizza i dati del campione per fare delle affermazioni sulle caratteristiche di tutta la popolazione.

---

## Pagina 68

Lo schema qui sotto cerca di esemplificare la situazione. Le variabili di interesse sono rilevate solamente sulle unità statistiche che fanno parte del campione.

Nonostante le informazioni sulla popolazione siano incomplete, in un problema di inferenza si è però ambiziosi: con le informazioni rilevate sul solo campione l'obiettivo è arrivare a conclusioni su tutta la popolazione!

[Schema illustrativo con popolazione, campione, unità statistica (rappresentata da $x$)]

a.a $2024/2025$ --- R. Bellio
$3 / 28$

---

## Pagina 69

Motivazione per le indagini campionarie

* tempo e/o costo
* la popolazione di interesse può essere infinita e virtuale
* la rilevazione "distrugge" le unità statistiche e quindi, dopo una rilevazione esaustiva, la popolazione di partenza non interessa più perché non esiste più!
* precisione dei risultati: a volte rilevazioni campionarie (incomplete) portano a risultati più precisi di rilevazioni esaustive.

---

## Pagina 70

# Relazione tra popolazione e campione

* Supponiamo che la popolazione di riferimento siano i pezzi prodotti da svariati macchinari in un certo periodo di tempo, che sono presenti nel magazzino di una ditta $\dots$

* $\dots$ e che si sia interessati a conoscere il loro peso medio ma, per far presto, si voglia pesare solamente $10$ pezzi.

* Il primo problema diventa come scegliere i dieci pezzi da misurare; due possibilità veloci sono:

  A) scegliere **completamente a caso** $10$ dei pezzi presenti, e misurare il loro peso;

  B) scegliere $10$ pezzi a caso tra quelli più "semplici" da prendere (ad esempio, considerando un gruppo di $10$ pezzi posti vicino all'entrata del magazzino).

---

## Pagina 71

* In ambedue i casi, alla fine si ottengono 10 numeri (le 10 misurazioni del peso). Però per stimare il peso medio di tutti i pezzi presenti non è possibile utilizzare questi numeri nella stessa maniera nei due casi A) e B).

  * Nel primo caso posso pensare di stimare il peso medio utilizzando la media aritmetica delle 10 misurazioni fatte. Se non si è stati particolarmente sfortunati, i pezzi provengono da macchinari diversi ed è plausibile che la media delle dieci misure "cada vicino" al peso medio di tutti.

  * Nel secondo caso però occorre cautela: potremmo aver scelto pezzi prodotti tutti da un solo macchinario che produce pezzi con peso medio leggermente più basso, ed ottenere così un valore troppo basso.

Quello che cambia nei due casi è la **relazione tra la popolazione e il campione**.

a.a $2024/2025$ --- R. Bellio \hfill $6 / 28$

---

## Pagina 72

# Campione casuale semplice

L'esempio descrive la differenza tra un **campione casuale semplice**, che è **rappresentativo** della popolazione, e un **campione di convenienza**, che non lo è. Anche se è abbastanza intuitivo che il secondo non sia molto affidabile, purtroppo è spesso utilizzato nella pratica.

Un campione casuale semplice (c.c.s.) è un metodo per selezionare unità da una popolazione in maniera tale che ogni unità abbia la stessa possibilità di far parte del campione.

* Per ottenere un c.c.s. occorre **scegliere le unità totalmente a caso**.
* La scelta delle unità può avvenire con reinserimento oppure in blocco;
* per popolazioni infinite (o molto numerose), campionare con reinserimento o in blocco non porta a differenze sostanziali.

D'ora in poi si assumerà sempre di disporre di un c.c.s., estratto con reinserimento (esistono però schemi più sofisticati).

a.a 2024/2025 — R. Bellio 
7 / 28

---

## Pagina 73

L'indagine campionaria comporta sempre un errore

Per rendere utili le affermazioni fatte riguardo la popolazione è necessario cercare di quantificare il margine d'errore.

Esempio. Supponiamo di sperimentare un nuovo farmaco su $20$ pazienti e che solo uno di questi $20$ pazienti mostri effetti secondari indesiderati. Sembra naturale allora stimare la probabilità che il farmaco induca effetti tossici rilevanti come pari al $5\%$.

In questo caso la popolazione di riferimento è data da tutti i pazienti a cui potremmo pensare di somministrare il farmaco sotto analisi. È una popolazione virtuale e teoricamente infinita.

È chiaro che non è possibile affermare che la percentuale di tutti i possibili pazienti che potrebbero presentare problemi di tossicità sia esattamente uguale al $5\%$: è importante allora chiedersi di quanto potrebbe essere differente (ovvero quale sia l'\textbf{entità dell'errore}).

---

## Pagina 74

# Inferenza statistica e Probabilità

L'idea alla base dell'inferenza statistica si concretizza nel descrivere la relazione tra la popolazione e il campione utilizzando il calcolo delle probabilità.

Nella sostanza, si interpretano i risultati sperimentali (ovvero i dati disponibili) come uno dei tanti risultati che un meccanismo probabilistico (un esperimento casuale) poteva fornire.

Una conseguenza importante è che è possibile utilizzare in maniera naturale il calcolo delle probabilità per quantificare l'errore campionario.

---

## Pagina 75

# Ipotesi fondamentale per l'inferenza statistica

L'ipotesi fondamentale nell'inferenza statistica è che i dati campionari osservati, denotati anche con

$$
y = (y_1, \dots, y_n) ,
$$

siano la **realizzazione di** $n$ **variabili casuali** $Y_1, \dots, Y_n$.

Questo tiene conto del fatto che abbiamo estratto uno tra i molti possibili campioni, ovvero della presenza di **variabilità campionaria**. (L'ipotesi non sarebbe necessaria se potessimo osservare tutta la popolazione!)

Nel caso di un campione casuale semplice, le $n$ v.c. che si suppone abbiano generato i dati sono **variabili casuali indipendenti e identicamente distribuite** (i.i.d.)

---

## Pagina 76

# Inferenza statistica parametrica

La distribuzione assunta per le singole variabili dipende dalla natura dei dati. Ad esempio, per dati binari sarà naturale ipotizzare $Y_i \sim \text{Bernoulli}(p)$, per misurazioni $Y_i \sim \mathcal{N}(\mu, \sigma^2)$, per conteggi $Y_i \sim \mathcal{P}(\lambda)$, per tempi di guasto $Y_i \sim \mathcal{G}a(\alpha, 1/\beta)$ (o Weibull), etc.

In ogni caso, la distribuzione assunta per le v.c. del campione dipenderà da ignote costanti dette **parametri**, vale a dire le quantità $p, \mu, \sigma^2, \alpha, \beta \dots$

I parametri entrano nella definizione della distribuzione delle variabili del campione $Y_1, \dots, Y_n$. Nell'**inferenza statistica parametrica** si assume che la distribuzione delle v.c. del campione sia nota a meno dei valori dei parametri, che corrispondono tipicamente agli aspetti di interesse dell'analisi.

---

## Pagina 77

# Modello statistico parametrico

Le assunzioni viste vanno allora a definire un **modello statistico parametrico** per i dati del campione.

Riassumendo, l'idea di base è che i dati siano stati generati dalle v.c. $Y_1, \dots, Y_n$, dove:

1. le variabili $Y_i$ sono indipendenti;
2. tutte le $Y_i$ hanno la stessa distribuzione di probabilità;
3. tale distribuzione è nota a meno dei valori di uno o più parametri, indicati genericamente come $\theta = (\theta_1, \dots, \theta_d)$, $d \ge 1$.

Scopo dell'inferenza statistica è utilizzare i dati del campione per ottenere informazioni su $\theta$, i cui elementi sono valori di un certo insieme $\Theta$ (**spazio parametrico**).

---

## Pagina 78

Modello statistico parametrico: alcune osservazioni

* I tre punti citati rappresentano delle *assunzioni*, che non è detto siano necessariamente soddisfatte nella pratica.
* In ogni caso, tali ipotesi possono essere considerate al più una descrizione **semplice** ed **operativamente utile** di una realtà complessa, quindi ci possiamo accontentare di una validità almeno **approssimata**.
* Esistono comunque metodi per trattare dati con una certa struttura di dipendenza (come le serie storiche), o per prescindere dalla conoscenza della forma della distribuzione (i **metodi non parametrici**). Essi comunque sono un'estensione dei metodi della statistica parametrica.

---

## Pagina 79

# Statistiche e distribuzioni campionarie

Si chiama **statistica (campionaria)** ogni funzione dei dati, che viene usata per sintetizzare opportunamente il campione

$$
T = t(Y_1, \dots, Y_n) \, .
$$

Sono esempi di statistiche gli indici utilizzati nella statistica descrittiva

$$
\overline{Y}, S^2, \text{la mediana campionaria}, \dots,
$$

e occorre sempre distinguere tra la v.c. che rappresenta la statistica e il valore che tale statistica assume in un particolare campione osservato.

Tipicamente, è di interesse determinare la distribuzione di alcune statistiche di interesse, ovvero la loro **distribuzione campionaria**. A tal fine, si utilizzano i metodi probabilistici sviluppati per le funzioni di $n$ v.c. indipendenti.

---

## Pagina 80

Distribuzioni campionarie

Vedremo in sintesi alcuni risultati per variabili casuali indipendenti (con molti richiami a risultati visti in dettaglio in lezioni passate), e in particolare:

A) Risultati per variabili qualsiasi.

B) Risultati per variabili bernoulliane.

C) Risultati per variabili Poisson.

D) Risultati per variabili normali.

---

## Pagina 81

A) Richiami sulle somme di variabili casuali

* $Y_1, \dots, Y_n$ v.c. con $E(Y_1) = \mu_1, \dots, E(Y_n) = \mu_n$

$$
\Rightarrow E(Y_1 + \dots + Y_n) = \mu_1 + \dots + \mu_n.
$$

* $Y_1, \dots, Y_n$ v.c. indipendenti con $V(Y_1) = \sigma_1^2, \dots, V(Y_n) = \sigma_n^2$

$$
\Rightarrow V(Y_1 + \dots + Y_n) = \sigma_1^2 + \dots + \sigma_n^2.
$$

---

## Pagina 82

A) Richiami sulle somme di variabili casuali

Una conseguenza importante dei risultati appena visti riguarda la **variabile casuale media campionaria**

$$
\overline{Y} = \frac{1}{n} \sum_{i=1}^{n} Y_i
$$

* Se $Y_1, \dots, Y_n$ sono v.c. indipendenti con $E(Y_i) = \mu$ e $V(Y_i) = \sigma^2$, allora

$$
E(\overline{Y}) = \sum_{i=1}^{n} \frac{E(Y_i)}{n} = n \frac{\mu}{n} = \mu \, ,
$$

$$
V(\overline{Y}) = \sum_{i=1}^{n} \frac{V(Y_i)}{n^2} = n \frac{\sigma^2}{n^2} = \frac{\sigma^2}{n} \, .
$$

---

## Pagina 83

A) La v.c. varianza campionaria

Nel caso di variabili i.i.d., con $E(Y_i) = \mu$ e $V(Y_i) = \sigma^2$, ci sono dei risultati anche per **variabile casuale varianza campionaria**

$$
S^2 = \frac{1}{(n - 1)} \sum_{i=1}^{n} (Y_i - \overline{Y})^2
$$

- Se $Y_1, \dots, Y_n$ sono v.c. indipendenti con $E(Y_i) = \mu$ e $V(Y_i) = \sigma^2$, allora

$$
E(S^2) = \sigma^2
$$

$$
V(S^2) = (\sigma^2)^2 \left( \frac{2}{n - 1} + \frac{\kappa}{n} \right),
$$

con $\kappa$ costante che dipende dalla distribuzione ($0$ per $Y_i$ normali, ma non in generale).

---

## Pagina 84

A) Teorema del limite centrale

Teorema Sia $Y_1, Y_2, \dots$ una successione di v.c. indipendenti, ciascuna con $E(Y_i) = \mu$ e $V(Y_i) = \sigma^2$. Allora, posto $Z_n = \sqrt{n}(\overline{Y} - \mu)/\sigma$, per ogni $z$

$$
\lim_{n \to \infty} P(Z_n \le z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{z} e^{-t^2/2} dt = \Phi(z) \,.
$$

In simboli il teorema del limite centrale (t.l.c.) si denota scrivendo

$$
Z_n = \sqrt{n}\frac{(\overline{Y} - \mu)}{\sigma} \xrightarrow{\mathcal{D}} \mathcal{N}(0, 1) \,,
$$

dove $\xrightarrow{\mathcal{D}}$ si legge "converge in distribuzione".

Una lettura **pratica** del teorema del limite centrale è la seguente:

$$
\overline{Y} \stackrel{a}{\sim} \mathcal{N}\left\lbrace \mu, \frac{\sigma^2}{n} \right\rbrace \,,
$$

dove $\stackrel{a}{\sim}$ significa "distribuita approssimativamente".

---

## Pagina 85

A) Teorema del limite centrale: utilizzo

Il t.l.c. permette di approssimare la distribuzione di $\overline{Y}$, o, in maniera equivalente, della somma di $n$ v.c. i.i.d.

$$
\sum_{i=1}^{n} Y_i \stackrel{a}{\sim} \mathcal{N} \left( n \mu, n \sigma^2 \right) .
$$

Si tratta di un risultato molto utile, del tipo chiamato **per grandi campioni**, nel senso che l'approssimazione è migliore per dimensioni campionarie elevate. Più precisamente, *quanto* deve essere grande $n$ dipende dalla distribuzione della popolazione:
- se il campione proviene da una distribuzione quasi simmetrica, l'approssimazione è buona già per piccoli valori di $n$;
- se la distribuzione è molto asimmetrica, è necessario un valore di $n$ abbastanza grande;
- per la maggior parte delle distribuzioni, un campione di numerosità $30$ (o più) è sufficientemente elevato affinché l'approssimazione normale sia adeguata.

---

## Pagina 86

B) Risultati per variabili bernoulliane

Se consideriamo $n$ v.c. bernoulliane $Y_i \sim \text{Bernoulli}(p)$, $i=1,\dots,n$, indipendenti, si ottiene facilmente che

$$
\sum_{i=1}^{n} Y_i \sim Bi(n,p) \,,
$$

Per $n$ elevato è più semplice utilizzare il t.l.c., che permette di **approssimare la binomiale con la normale**.

Al crescere di $n$, la distribuzione di una v.c. binomiale di parametri $n$ e $p$ si "avvicina" sempre di più a quella di una normale con parametri $\mu = np$ e $\sigma^2 = np(1-p)$.

L'approssimazione è ritenuta buona se $np > 5$ e $n(1-p) > 5$ (eventualmente utilizzando **correzioni di continuità** ($\pm 0.5$)), che migliorano l'approssimazione normale per v.c. discrete).

---

## Pagina 87

a.a $2024/2025$ --- R. Bellio

$$
n=10, p=0.2
$$

$$
n=20, p=0.2
$$

$$
n=40, p=0.2
$$

$$
n=80, p=0.2
$$

$22 / 28$

---

## Pagina 88

C) Risultati per variabili Poisson

Se $Y_i \sim \mathcal{P}(\lambda_i)$, $i = 1, \dots, n$, indipendenti, allora

$$
\sum_{i=1}^{n} Y_i \sim \mathcal{P}\left(\sum_{i=1}^{n} \lambda_i\right).
$$

In particolare, per v.c. i.i.d. (dove $\lambda_i = \lambda$) si ottiene $\sum_{i=1}^{n} Y_i \sim \mathcal{P}(n\lambda)$. Anche in questo caso, tuttavia, il t.l.c. è spesso utilizzato, ovvero

$$
\sum_{i=1}^{n} Y_i \stackrel{a}{\sim} \mathcal{N}(n\lambda, n\lambda)\text{.}
$$

L'approssimazione è ritenuta buona se $n\lambda > 10$.

---

## Pagina 89

D) Risultati per variabili normali

Per il caso $Y_i \sim \mathcal{N}(\mu, \sigma^2)$, $i = 1, \dots, n$, indipendenti, esistono diversi risultati.

Come caso particolare della proprietà che combinazioni lineari di normali indipendenti sono ancora normali, si ottiene

$$
\overline{Y} \sim \mathcal{N}\left\lbrace \mu, \frac{\sigma^2}{n} \right\rbrace \,,
$$

$$
\sum_{i=1}^{n} Y_i \sim \mathcal{N}(n\mu, n\sigma^2) \,,
$$

senza alcuna approssimazione!

Altri risultati richiedono preliminarmente la definizione di due distribuzioni collegate alla normale, ovvero la **distribuzione chi-quadrato** e la **distribuzione $t$ di Student**.

---

## Pagina 90

La distribuzione chi-quadrato

La somma di $n$ v.c. normali standard indipendenti elevate al quadrato ha distribuzione chi-quadrato con $n$ gradi di libertà, in simboli $\chi_{n}^{2}$. Ovvero, se $Z_{i} \sim \mathcal{N}(0, 1)$, $i = 1, \dots, n$, indipendenti,

$$
Y = \sum_{i=1}^{n} Z_{i}^{2} \sim \chi_{n}^{2}
$$

La distribuzione è un caso particolare di distribuzione Gamma, con $\alpha = n / 2$ e $\beta = 2$, e allora si trova $E(Y) = n$ e $V(Y) = 2n$.

Funzione di densità

---

## Pagina 91

La distribuzione $t$ di Student

Date due v.c. indipendenti, $Z \sim \mathcal{N}(0, 1)$ e $X \sim \chi^2_n$, allora

$$
Y = \frac{Z}{\sqrt{X/n}},
$$

ha distribuzione $t$ di Student con $n$ gradi di libertà, $Y \sim t_n$.
Molto simile alla normale standard, a cui tende rapidamente al crescere di $n$, con $E(Y) = 0$ e $V(Y) = n / (n - 2)$.

Funzione di densità

---

## Pagina 92

Altri risultati per la distribuzione normale

* Per la varianza campionaria, vale

$$
\frac{\sum_{i=1}^{n} (Y_i - \overline{Y})^2}{\sigma^2} = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1} \, .
$$

* $\overline{Y}$ e $S^2$ sono v.c. indipendenti.

* Media campionaria standardizzata e media campionaria **studentizzata**

$$
\frac{\overline{Y} - \mu}{\sqrt{\frac{\sigma^2}{n}}} \sim \mathcal{N}(0,1) \, , \qquad \frac{\overline{Y} - \mu}{\sqrt{\frac{S^2}{n}}} \sim t_{n-1} \, .
$$

---

## Pagina 93

Un risultato per due campioni indipendenti

Se $X_1, \dots, X_{n_X}$ e $Y_1, \dots, Y_{n_Y}$ rappresentano due c.c.s. **tra loro indipendenti**, con $X_i \sim \mathcal{N}\left( \mu_X, \sigma_X^2 \right)$ e $Y_i \sim \mathcal{N}\left( \mu_Y, \sigma_Y^2 \right)$, allora utilizzando la proprietà che combinazioni lineari di v.c. sono normali si ottiene

$$
\overline{X} - \overline{Y} \sim \mathcal{N}\left( \mu_X - \mu_Y, \frac{\sigma_X^2}{n_X} + \frac{\sigma_Y^2}{n_Y} \right) \, ,
$$

con il risultato che vale in maniera approssimata (via t.l.c.) nel caso di medie campionarie di campioni non normali.

---

## Pagina 94

Stima puntuale e controllo del modello

---

## Pagina 95

# I problemi dell'inferenza statistica

Utilizzando il campione osservato $y = (y_1, \dots, y_n)$, alla luce del modello statistico parametrico prescelto, si vogliono ricavare informazioni sul parametro ignoto $\theta \in \Theta$. I principali problemi inferenziali sono suddivisibili in tre classi:

* **stima puntuale**: si vuole ottenere, sulla base dei dati del campione $y$, un valore numerico per $\theta$;
* **stima intervallare**: si vuole ottenere, sulla base dei dati del campione $y$, un sottoinsieme di $\Theta$ in cui è plausibilmente incluso $\theta$;
* **verifica di ipotesi**: data una congettura o un'ipotesi su $\theta$, si vuole verificare, sulla base dei dati del campione $y$, se essa è accettabile, cioè in accordo con i dati osservati.

---

## Pagina 96

# Stima puntuale

Ipotizziamo allora di aver specificato un modello statistico parametrico per i dati del campione, ovvero una distribuzione di probabilità per $Y_i$ che indichiamo genericamente con $p(y_i; \theta)$, funzione di probabilità o di densità.

L'obiettivo della stima puntuale è utilizzare i dati per ottenere un valore plausibile del parametro, ovvero una sua **stima**.

In molti casi, esiste un modo abbastanza intuitivo per ottenere una stima di $\theta$.

---

## Pagina 97

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

---

## Pagina 98

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

---

## Pagina 99

# Stime e stimatori

La **stima** di un parametro è definita come un **valore** numerico ottenuto dai dati osservati del campione $y_1, \dots, y_n$.

Si definisce **stimatore** di un parametro di interesse una **variabile casuale** funzione delle v.c. $Y_1, \dots, Y_n$ che generano i valori osservati (quindi lo stimatore è una statistica e la stima ne è il valore osservato con i dati).

In generale, se $\theta$ è parametro di interesse, si denota con $\widehat{\theta}$ sia la stima $\widehat{\theta}(y_1, \dots, y_n)$ che lo stimatore $\widehat{\theta}(Y_1, \dots, Y_n)$, è poi il contesto a rendere chiaro a quale delle due ci si riferisce.

Due punti importanti:

* Dato uno stimatore, come posso stabilire se si tratta di un buon stimatore ? (**Proprietà di uno stimatore**).
* Come posso reperire un buon stimatore? (**Metodi di stima**)

---

## Pagina 100

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

---

## Pagina 101

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

---

## Pagina 102

# Precisione della stima

Per confrontare due (o più) stimatori consistenti di uno stesso parametro, è sufficiente confrontare il loro errore quadratico medio: lo stimatore con $EQM$ minore sarà preferibile.

Se gli stimatori sono non distorti, il confronto si riduce a verificare quale stimatore ha la minor varianza a parità di numerosità del campione (e si parla allora di **stimatore più efficiente** tra quelli considerati).

La radice della varianza di uno stimatore è detta **errore standard** (o talvolta **incertezza**)

$$
\sigma_{\widehat{\theta}} = \sqrt{V(\widehat{\theta})},
$$

e la sua valutazione con i dati del campione è detta **errore standard stimato** $\widehat{\sigma}_{\widehat{\theta}}$. L'errore standard stimato è generalmente utilizzato come misura della **precisione di stima**, ed è riportato assieme ad essa.

---

## Pagina 103

Esempi

* Modello bernoulliano
Se $Y_i \sim \text{Bernoulli}(p)$, uno stimatore di $p$ è la media campionaria, cioè $\widehat{p} = \overline{Y}$. Si ottiene

$$
E(\widehat{p}) = p \, , \qquad V(\widehat{p}) = \frac{p(1-p)}{n} \, .
$$

Lo stimatore è non distorto e consistente, e vale inoltre $\sigma_{\widehat{p}} = \sqrt{p(1-p)/n}$.
Con $n = 40$ e $\widehat{p} = 0.075$, si ottiene $\widehat{\sigma}_{\widehat{p}} = 0.0416$.

* Modello Poisson
Se $Y_i \sim \mathcal{P}(\lambda)$, uno stimatore di $\lambda$ è di nuovo la media campionaria, $\widehat{\lambda} = \overline{Y}$. Si ottiene

$$
E(\widehat{\lambda}) = \lambda \, , \qquad V(\widehat{\lambda}) = \frac{\lambda}{n} \, .
$$

Lo stimatore è non distorto e consistente.

a.a 2024/2025 --- R. Bellio \hfill 10 / 26

---

## Pagina 104

* Modello normale
Se $Y_i \sim \mathcal{N}(\mu, \sigma^2)$, allora $\overline{Y}$ e $S^2$ sono due stimatori per $\mu$ e $\sigma^2$. Si ottiene

$$
E(\overline{Y}) = \mu \,, \quad V(\overline{Y}) = \frac{\sigma^2}{n} \,,
$$

$$
E(S^2) = \sigma^2 \,, \quad V(S^2) = \frac{2(\sigma^2)^2}{(n-1)} \,.
$$

Entrambi gli stimatori sono non distorti e consistenti; il denominatore $(n-1)$ nella definizione di $S^2$ serve proprio ad ottenere la non distorsione.

---

## Pagina 105

Per lo stimatore alternativo (e più intuitivo) per la varianza

$$
\widehat{\sigma}^2 = \frac{\sum_{i=1}^{n} (Y_i - \overline{Y})^2}{n}
$$

si ottiene

$$
E(\widehat{\sigma}^2) = \frac{(n-1)}{n} \sigma^2 \, , \quad V(\widehat{\sigma}^2) = \frac{(n-1)}{n} \cdot \frac{2(\sigma^2)^2}{n} \, ,
$$

per cui si tratta comunque di uno stimatore consistente.

---

## Pagina 106

# Lo stimatore media campionaria

In generale, dato un qualsiasi modello statistico parametrico, la media campionaria $\overline{Y}$ è sempre uno stimatore non distorto e consistente di $\mu = E(Y_i)$, dato che, se $\sigma^2 = V(Y_i)$

$$
E(\overline{Y}) = \mu \, , \qquad V(\overline{Y}) = \frac{\sigma^2}{n} \, .
$$

La consistenza della media campionaria va sotto il nome di **legge dei grandi numeri**. Inoltre, il teorema del limite centrale assicura che la distribuzione di $\overline{Y}$ è approssimativamente normale.

Si noti inoltre che

$$
\sigma_{\overline{Y}} = \frac{\sigma}{\sqrt{n}} \, .
$$

In presenza di outliers, è preferibile utilizzare una media troncata, eliminando una percentuale (piccola) di dati. La media troncata è un esempio di **stimatore robusto**.

---

## Pagina 107

# Metodi di stima

Esistono vari metodi di stima. In casi semplici, si utilizza il **metodo dell'analogia**, che ci porta a stimare la media con la media campionaria, la varianza con la varianza campionaria e così via.

Per situazioni generali, esistono vari metodi per reperire stimatori.

Tra gli altri, citiamo il **metodo della massima verosimiglianza**, che per molti versi è quello preferibile, ed è utilizzato nei software statistici per stimare i parametri di distribuzioni quali la Gamma e la Weibull, e per modelli statistici più complessi.

---

## Pagina 108

Controllo empirico del modello

Alla luce dei dati disponibili $y = (y_1, \dots, y_n)$, per procedere con i metodi dell'inferenza statistica parametrica è necessario specificare un modello per i dati, ovvero una distribuzione di probabilità per le variabili casuali indipendenti $Y_1, \dots, Y_n$.

In certi casi la specificazione (soprattutto per dati continui) può essere non banale, ed è allora necessario procedere ad un **controllo empirico del modello**.

A tal fine, si utilizzano
- Metodi della statistica descrittiva, come l'**istogramma** o la **funzione di ripartizione empirica**.
- I **grafici di probabilità**.

---

## Pagina 109

Controllo mediante istogramma

L'istogramma nell'ambito inferenziale può essere interpretato come una **stima della funzione di densità**.

* La stima è valida a prescindere da quale sia la vera distribuzione dei dati.
* La stima è migliore per grandi campioni, cioè quando l'informazione campionaria aumenta.

Il controllo si effettua confrontando l'istogramma con la funzione di densità del modello teorico, con i **parametri** del modello teorico rimpiazzati da opportune **stime**.

---

## Pagina 110

Esempio: PM (bassa quota)

I dati sembrano avere una distribuzione asimmetrica: un modello adatto sembra essere la distribuzione Gamma, con $\widehat{\alpha} = 2.03$ e $\widehat{\beta} = 1.82$.

Dati su scala originale

---

## Pagina 111

Esempio: PM (bassa quota)

In alternativa, è possibile effettuare la trasformazione $x_i = \sqrt[4]{y_i}$, e utilizzare un modello normale, con $\mu = \bar{x}$ e $\sigma^2 = s_x^2$.

---

## Pagina 112

Controllo mediante funzione di ripartizione empirica

In maniera analoga, è possibile utilizzare la funzione di ripartizione empirica, definita come

$$
\widehat{F}_n(x) = \frac{1}{n} \sum_{i=1}^n I_x(y_i) = \frac{\text{Numero di osservazioni } \le x}{n},
$$

dove $I_x(y_i)$ è una opportuna funzione indicatrice

$$
I_x(y_i) = \left\lbrace 
\begin{array}{ll}
1 & \text{se } y_i \le x \\
0 & \text{se } y_i > x
\end{array}
\right.
$$

La funzione di ripartizione empirica stima la vera funzione di ripartizione, quindi il controllo in questo caso si fa confrontandola con la funzione di ripartizione del modello teorico.

---

## Pagina 113

# Grafici di probabilità

I **grafici di probabilità** (o **carte di probabilità**) consentono di confrontare la distribuzione ipotizzata per i dati (teorica) con i dati campionari. Sono la tecnica più comunemente utilizzata.

Se $F(\cdot)$ indica la funzione di ripartizione teorica, i grafici sono dei diagrammi di dispersione delle coppie $\left( F(y_i), \widehat{F}_n(y_i) \right)$, oppure (equivalentemente) delle coppie $\left( F^{-1}(y_i), \widehat{F}_n^{-1}(y_i) \right)$, $i = 1, \dots, n$.

Anche in questo caso, occorre rimpiazzare i parametri del modello teorico con le stime ottenute dai dati.

Se il modello teorico è corretto, i punti tenderanno ad essere allineati lungo una linea retta.

---

## Pagina 114

Grafici di probabilità normali

I grafici di probabilità si possono costruire per tutte le distribuzioni continue, però i più utilizzati sono i **grafici delle probabilità normali**, che consentono di confrontare i dati con il modello teorico normale.

Si ottengono mediante un algoritmo in 3 passi

1. Considero $n$ valori equispaziati tra $0$ e $1$

$$
p_i = \frac{i - 0.5}{n}, \qquad i = 1, \dots, n .
$$

2. Rappresento con un diagramma di dispersione le coppie $(\Phi^{-1}(p_i), y_{(i)})$.
3. Se il modello normale è corretto, i punti tenderanno ad essere disposti lungo una linea retta.

---

## Pagina 115

Situazioni di allontanamento dalla normalità possono aversi con **asimmetria** o **code pesanti**.

Asimmetria

Quantili empirici

Quantili teorici

Code pesanti

Quantili empirici

Quantili teorici

a.a $2024/2025$ --- R. Bellio

$22 / 26$

---

## Pagina 116

Esempio: PM (bassa quota)

Dati su scala originale
Quantili campionari
Quantili teorici

Dati trasformati
Quantili campionari
Quantili teorici

a.a $2024/2025$ --- R. Bellio
$23 / 26$

---

## Pagina 117

# Esempio: contaminazione d'alluminio

I dati si riferiscono ad un campione di $n = 22$ contaminazioni d'alluminio (ppm).

$$
\begin{}
30 & 30 & 60 & 63 & 70 & 79 & 87 \\
90 & 101 & 102 & 115 & 118 & 119 & 119 \\
120 & 125 & 140 & 145 & 172 & 182 & \\
183 & 191 & 222 & 244 & 291 & 511 &
\end{}
$$

Cerchiamo un modello che sia appropriato per questi dati, scegliendo tra le distribuzioni normale, lognormale, esponenziale e Weibull, costruendo i grafici di probabilità per ciascuna di queste distribuzioni.

---
a.a 2024/2025 — R. Bellio \hfill 24 / 26

---

## Pagina 118

Normale

Lognormale

Dati

Quantili teorici

Dati

Quantili teorici

Il modello lognormale è più appropriato di quello normale...

a.a $2024 / 2025$ — R. Bellio

$25 / 26$

---

## Pagina 119

Esponenziale & Weibull

... e fornisce un miglior adattamento ai dati anche rispetto ai modelli esponenziale e Weibull.

a.a $2024/2025$ --- R. Bellio

$26 / 26$

---

## Pagina 120

STIMA PER INTERVALLO

* Stima puntuale "manca" certamente il vero $\theta$
* Stima per intervallo: $\hat{\theta}_L < \theta < \hat{\theta}_U$
Dipende dal valore osservato di $\hat{\theta}$ (e dalla sua distribuzione campionaria), è INSIEME DI VALORI PLAUSIBILI per $\theta$ alla luce dei dati

* AMPIEZZA dell'intervallo: Indicazioni su accuratezza di $\hat{\theta}$

Def

$$
P\left(\hat{\theta}_L < \theta < \hat{\theta}_U\right) = 1 - \alpha, \quad 0 < \alpha < 1
$$

$$
\forall \theta \in \Theta
$$

Per un campione osservato: $\hat{\theta}_L < \theta < \hat{\theta}_U$ è un INTERVALLO DI CONFIDENZA PER $\theta$, e i valori $\hat{\theta}_L$ e $\hat{\theta}_U$ sono i LIMITI DI CONFIDENZA

* Abbrevieremo INTERVALLO DI CONFIDENZA con IC

---

## Pagina 121

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

---

## Pagina 122

$$
P\left(\overline{x} - z_{1 - \alpha/2} \frac{\sigma}{\sqrt{n}} < \mu < \overline{x} + z_{1 - \alpha/2} \frac{\sigma}{\sqrt{n}}\right) = 1 - \alpha
$$

$\longrightarrow$ IC di livello $(1 - \alpha)$ per $\mu$:

$$
\overline{x} - z_{1 - \alpha/2} \frac{\sigma}{\sqrt{n}} < \mu < \overline{x} + z_{1 - \alpha/2} \frac{\sigma}{\sqrt{n}}
$$

$$
\overline{x} \pm z_{1 - \alpha/2} \frac{\sigma}{\sqrt{n}} \longrightarrow \begin{array}{l} \text{IC OSSERVATO} \\ \text{(calcolato con i dati)} \end{array}
$$

- Il risultato è esatto (nel senso che la probabilità di inclusione è $1 - \alpha$) per campioni normali o $n$ elevato.
- Approssimazione accettabile nel caso non normale per $n \ge 30 \longrightarrow$ RISULTATO VALIDO PER GRANDI CAMPIONI.
- Nota: ampiezza IC $$ 2 \; z_{1 - \alpha/2} \frac{\sigma}{\sqrt{n}} $$
  - AUMENTA per $(1 - \alpha) \longrightarrow 1$
  - AUMENTA per $\sigma$ che aumenta
  - DIMINUISCE al crescere di $n$

---

## Pagina 123

ES: Produzione pezzi meccanici

$$
n = 100, \quad \overline{x} = 12.05, \quad \underset{\sigma = 0.2}{\text{SI SUPPONE}}
$$

IC $95\%$ per $\mu$:

$$
12.05 - (1.96) \frac{0.2}{\sqrt{10}} < \mu < 12.05 + (1.96) \frac{0.2}{\sqrt{10}}
$$

$$
\underbrace{}_{\substack{\uparrow \\ z_{0.975}}} \quad \underbrace{}_{0.0392}
$$

$$
(12.011, 12.089)
$$

Siamo "fiduciosi / confidenti" al $95\%$ che l'errore nella stima di $\mu$ non supera $0.0392$.

INTERPRETAZIONE IC

Dato un intervallo osservato, non possiamo dire che includerà $\mu$ con probabilità $(1-\alpha)$: infatti, la probabilità si riferisce all'intervallo con estremi le V.C., non a quello osservato!

L'unica garanzia che abbiamo è che, in un numero molto elevato di campioni ottenuti nelle stesse condizioni gli intervalli calcolati su quella formula includevano il vero $\mu$ il $95\%$ delle volte.

È questo il senso di "essere fiduciosi o confidenti" al $95\%$.

---

## Pagina 124

(5)

$1^{\circ}$ CAMPIONE

$2^{\circ}$ CAMPIONE

$3^{\circ}$ CAMPIONE

$4^{\circ}$ CAMPIONE

$5^{\circ}$ CAMPIONE

i campioni
con $IC$ che
non include
$\mu$ sono il $5\%$

$\mu$

UTILIZZARE $IC$ per DIMENSIONARE
IL CAMPIONE

Fissato $e = z_{1-\alpha/2} \dfrac{\sigma}{\sqrt{n}}$, errore nella
stima di $\mu$

Conoscendo $\sigma$ e $(1-\alpha)$ posso ottenere $n$:

$$
n = \left\lbrace \frac{z_{1-\alpha/2} \sigma}{e} \right\rbrace^2
$$

ES: Fisso $e = 0.015$ e $0.95$ $\sigma = 0.2$

$n = 1.56^2 \cdot 0.2^2 / 0.015^2 = 682.95 \rightarrow 683$

---

## Pagina 125

- LIMITI DI CONFIDENZA UNILATERALI \quad (6)

(IC su il solo limite inferiore o superiore)

$$
\overline{x} - z_{1-\alpha} \frac{\sigma}{\sqrt{n}} \qquad \overline{x} + z_{1-\alpha} \frac{\sigma}{\sqrt{n}}
$$

Infatti: $P\left(\overline{X} - z_{1-\alpha} \cdot \frac{\sigma}{\sqrt{n}} < \mu\right) = 1-\alpha$

Utili in particolari situazioni

ES: $\overline{x} - z_{0.95} \frac{(0.2)}{10} = 12.017$

$(12.017, \, \infty) \longrightarrow \begin{matrix} \text{IC su il} \\ \text{solo} \\ \text{limite} \\ \text{inferiore} \\ \text{di livello } 95\% \end{matrix}$

(7) IL CASO DI $\sigma$ IGNOTA

- Se $\sigma^2$ è ignota (caso tipico nelle applicazioni) viene rimpiazzata da $s^2$, la stima campionaria.

- Se $n$ è elevato, l'effetto della sostituzione è trascurabile

---

## Pagina 126

* Se $n$ è piccolo ($n < 30$), l'effetto esiste, e la teoria richiede che $X_i \sim \mathcal{N}\left\lbrace \mu, \sigma^2 \right\rbrace$: per campioni normali si ottiene allora

$$
T = \frac{\overline{x} - \mu}{\sqrt{\frac{S^2}{n}}} \sim t_{n-1}
$$

e l'IC è quindi

$$
\overline{x} \pm t_{n-1; 1-\alpha/2} \frac{S}{\sqrt{n}}
$$

*(Nota: percentile $1-\alpha/2$ di $t_{n-1}$)*

* Nota: se $n$ è elevato $t_{n-1} \sim \mathcal{N}(0,1)$, confermando che per grandi campioni l'effetto di utilizzare $S^2$ è trascurabile.

ESEMPIO 3.5: $n=7$, $\overline{x} = 10.0$, $S = 0.283$
$(1-\alpha) = 0.95$, $t_{6; 0.975} = 2.447$

$$
10 \pm 2.447 \frac{(0.283)}{\sqrt{7}} = (9.74, 10.26)
$$

---

## Pagina 127

NOTA

$$
\sigma_{\overline{x}} = \frac{\sigma}{\sqrt{n}} = \text{ERRORE STANDARD}
$$

$$
\widehat{\sigma}_{\overline{x}} = \frac{s}{\sqrt{n}} = \text{ERRORE STANDARD STIMATO}
$$

IC per $\mu$ (grandi campioni):

$$
\left\lbrace
\begin{array}{lclcl}
\overline{x} & \pm & z_{1-\alpha/2} \sigma_{\overline{x}} & , & \sigma \text{ NOTA} \\
\overline{x} & \pm & z_{1-\alpha/2} \widehat{\sigma}_{\overline{x}} & , & \sigma \text{ IGNOTA}
\end{array}
\right.
$$

(10) INTERVALLI DI PREVISIONE (CASO NORMALE)

- Siamo interessati a PREVEDERE il valore di una V.C. prima della sua realizzazione, sulla base dei dati di un campione osservato

$$
X_1, X_2, \dots, X_n \quad \text{CCS} \quad X_i \sim N(\mu, \sigma^2)
$$

(DATI DISPONIBILI)

$X_0$ IGNOTA

$$
X_0 \sim N(\mu, \sigma^2) \text{, indipendente dalle altre v.c.}
$$

---

## Pagina 128

CASO $6$ NOTA:

$$
X_0 - \overline{X} \sim \mathcal{N}\left(\mu - \mu, \sigma^2 + \frac{\sigma^2}{n}\right)
$$

$$
Z = \frac{X_0 - \overline{X}}{\sigma \sqrt{1 + \frac{1}{n}}} \sim \mathcal{N}(0, 1)
$$

Con passaggi analoghi a quelli per IC per $\mu$:

$$
P\left(\overline{X} - z_{1-\alpha/2} \sigma \sqrt{1 + \frac{1}{n}} < X_0 < \overline{X} + z_{1-\alpha/2} \sigma \sqrt{1 + \frac{1}{n}}\right) = 1 - \alpha
$$

$$
\longrightarrow \quad \overline{X} \pm z_{1-\alpha/2} \sigma \sqrt{1 + \frac{1}{n}}
$$

INTERVALLO DI PREVISIONE (IP) DI LIVELLO $(1 - \alpha)$

- Se $\sigma$ è IGNOTA: $\overline{X} \pm t_{n-1; 1-\alpha/2} S \sqrt{1 + \frac{1}{n}}$

e per $n$ elevato posso usare $z_{1-\alpha/2}$ invece di $t_{n-1; 1-\alpha/2}$

NOTA: $\left\lbrace \begin{array}{l} \text{gli intervalli di previsione sono sempre piú} \\ \text{ampi degli IC per } \mu\text{, e non hanno ampiezza} \\ \text{che } \longrightarrow 0 \text{ per } n \to \infty \end{array}\right.$

---

## Pagina 129

ESEMPIO 9.7:

$X_0 = \text{ammontare prestito prossimo cliente}$

DATI: $n = 50$ 

$\overline{x} = 257300$ dollari

$s = 25000$ dollari (DATI STORICI)

IP di livello $95\%$ :

$$
257300 \pm (1.96) 25000 \sqrt{1 + \frac{1}{50}}
$$

$$
= (207812, 306788)
$$

NOTA: IC per $\mu$ è invece $(250370, 264230)$

IP vengono spesso usati per individuare VALORI ANOMALI (OUTLIERS):

Un' osservazione è anomala se NON è inclusa nell'IP calcolato senza includere quell'osservazione nel campione

---

## Pagina 130

IC DIFFERENZA TRA DUE MEDIE (CASO NUMEROSITÀ CAMPIONARIE ELEVATE)

* Alcuni problemi inferenziali coinvolgono DUE CAMPIONI (indipendenti), relativi a due diverse sotto-popolazioni.

ASSUNZIONI

i) $X_1, X_2, \dots, X_{n_X}$ CCS

$$
E(X_i) = \mu_X \quad , \quad V(X_i) = \sigma^2_X \quad \text{NOTA}
$$

ii) $Y_1, Y_2, \dots, Y_{n_Y}$ CCS

$$
E(Y_i) = \mu_Y \quad , \quad V(Y_i) = \sigma^2_Y \quad \text{NOTA}
$$

iii) I DUE CAMPIONI SONO INDIPENDENTI

Dal TLC:

$$
\begin{aligned}
\downarrow \quad & \overline{X} \stackrel{a}{\sim} N\left(\mu_X, \frac{\sigma^2_X}{n_X}\right) \\
n_X, n_Y \ge 30 \quad & \overline{Y} \stackrel{a}{\sim} N\left(\mu_Y, \frac{\sigma^2_Y}{n_Y}\right)
\end{aligned}
$$

Inoltre, da iii) segue che $\overline{X}$ e $\overline{Y}$ sono V.C. INDIPENDENTI

---

## Pagina 131

Quindi:

$$
\overline{X} - \overline{Y} \stackrel{a}{\sim} N \left( \mu_X - \mu_Y, \frac{\sigma_X^2}{n_X} + \frac{\sigma_Y^2}{n_Y} \right)
$$

$$
Z = \frac{(\overline{X} - \overline{Y}) - (\mu_X - \mu_Y)}{\sqrt{\frac{\sigma_X^2}{n_X} + \frac{\sigma_Y^2}{n_Y}}} \stackrel{a}{\sim} N(0, 1)
$$

IC per $\mu_X - \mu_Y$ di livello $(1-\alpha)$, caso VARIANZE NOTE e GRANDI CAMPIONI:

$$
(\overline{x} - \overline{y}) \pm z_{1-\alpha/2} \sqrt{\frac{\sigma_X^2}{n_X} + \frac{\sigma_Y^2}{n_Y}}
$$

- ESATTO per V.C. NORMALI

---

## Pagina 132

III CASO VARIANZE IGNOTE 3

$\rightarrow$ campioni elevati, rimpizziamo $\sigma_x^2$ e $\sigma_y^2$
con le stime $S_x^2$ e $S_y^2$, senza ulteriori cambiamenti
($n_x \geq 30$, $n_y \geq 30$)

$\rightarrow$ piccoli campioni, V.C. NORMALI con VARIANZE
IGNOTE E NON NECESSARIAMENTE UGUALI: usiamo


$$
T = \frac{(\overline{X} - \overline{Y}) - (\mu_x - \mu_y)}{\sqrt{\frac{S_x^2}{n_x} + \frac{S_y^2}{n_y}}} \sim t_{\nu}
$$

$\rightarrow$ RISULTATO APPROSSIMATO, ma l'errore è trascurabile


$$
\nu = \frac{\left(\frac{S_x^2}{n_x} + \frac{S_y^2}{n_y}\right)^2}{\left[\frac{\left(\frac{S_x^2}{n_x}\right)^2}{n_x - 1} + \frac{\left(\frac{S_y^2}{n_y}\right)^2}{n_y - 1}\right]}
$$

, ARROTONDATO ALL'INTERO INFERIORE

FORMULA di WELCH / SATTERTHWAITE


$$
IC: \quad \left( \overline{x} - \overline{y} \right) \pm t_{\nu; 1 - \alpha/2} \sqrt{\frac{S_x^2}{n_x} + \frac{S_y^2}{n_y}}
$$

---

## Pagina 133

- Esistono formule anche per il caso di VARIANZE IGNOTE MA UGUALI

$$
(\overline{x} - \overline{y}) \pm t_{n_x + n_y - 2; 1 - \alpha/2} \ s_p \sqrt{\frac{1}{n_x} + \frac{1}{n_y}}
$$

$$
s^2_p = \frac{(n_x - 1) s^2_x + (n_y - 1) s^2_y}{n_x + n_y - 2} \quad \begin{matrix} \text{STIMA} \\ \text{"POOLED"} \\ \text{DELLA VARIANZA} \end{matrix}
$$

- In pratica, l'IC con la formula di WELCH può essere usato anche se le varianze sono uguali.

ES 9.22

$$
\begin{matrix}
\underline{\text{FARMAC 1}} & \underline{\text{FARMAC 2}} \\
n_x = 14 & n_y = 16 \\
\overline{x} = 17 & \overline{y} = 19 \\
s^2_x = 1.5 & s^2_y = 1.8
\end{matrix}
$$

- IC $95\%$ : il testo calcola $(0.70, 3.30)$, assumendo uguali varianze.

- Formula di Welch: $\nu = 27.9 \implies \nu = 27$

$$
t_{27; \, 0.995} = 2.771
$$

---

## Pagina 134

$$
(\bar{y} - \bar{x}) \pm 2.771 \sqrt{\frac{1.5}{14} + \frac{1.8}{16}}
$$

$$
\Rightarrow (0.701, \, 3.299)
$$

(III) OSSERVAZIONI APPAIATE

ESEMPIO: Misuro carico di rottura per $n=8$ provini di tessuto (diversi tra loro) su due diversi macchinari

$$
\begin{array}{cccc}
\text{PROVINO} & \text{MACC. 1} & \text{MACC. 2} & \text{DIFFERENZA} \\
1 & 74 & 78 & -4 \\
2 & 76 & 79 & -3 \\
3 & 74 & 75 & -1 \\
4 & 69 & 66 & 3 \\
5 & 58 & 63 & -5 \\
6 & 71 & 70 & 1 \\
7 & 66 & 66 & 0 \\
8 & 65 & 67 & -2
\end{array}
$$

$x_1, x_2, \dots, x_n$ ccs $1^{\circ}$ MACCHINARIO

$y_1, y_2, \dots, y_n$ ccs $2^{\circ}$ MACCHINARIO

---

## Pagina 135

PROBLEMA: $X_i$ e $Y_i$ (stesso provino) (6)

NON SONO INDIPENDENTI!

Ci aspettiamo $\rho_{X_i, Y_i} > 0$ (e infatti $r_{x, y} > 0$)

Non possiamo usare le formule per campioni indipendenti!

SOLUZIONE: Considero le $n$ DIFFERENZE

$$
D_i = X_i - Y_i, \quad i = 1, 2, \dots, n \quad \text{CCS}
$$

$$
\begin{aligned}
E(D_i) &= \mu_X - \mu_Y = \mu_D \\
V(D_i) &= \sigma_D^2 \quad \text{IGNOTA}
\end{aligned}
$$

$\hookrightarrow$ Uso formula per IC per $\mu$ caso singolo campione, con varianza ignota

$$
\hat{\mu}_D \pm t_{n - 1; 1 - \alpha/2} \sqrt{\frac{S_D^2}{n}}
$$

- Al solito, per $n$ elevato uso $z_{1 - \alpha/2}$, invece di $t_{n - 1; 1 - \alpha/2}$

---

## Pagina 136

Nell'esempio: $\hat{\mu}_D = \bar{d} = -1.375$

$s_D = 2.669$

$1-\alpha = 0.95 \text{, } t_{7; 0.975} = 2.364$

IC $95\%$ per $\mu_D$ : $(-3.607 \text{, } 0.857)$

che include il valore $0$, che implica

$\mu_X = \mu_Y$

---

## Pagina 137

(11) IC PER UNA PROPORZIONE

$X_1, X_2, \dots, X_n \quad \text{CCS} \quad X_i \sim \text{Bernoulli}(p)$

$X = \sum_{i=1}^{n} X_i \quad , \quad \hat{p} = \frac{X}{n} = \bar{X}$

$\text{TLC}: \hat{p} \stackrel{\alpha}{\sim} \mathcal{N}\left(p, \frac{p(1-p)}{n}\right)$

Infatti $\mu = p \quad \text{e} \quad \sigma^2 = p(1-p)$

- Se particolarizziamo l'IC per $p$ nel caso di grandi campioni otteniamo:

$$
\hat{p} \pm z_{1-\alpha/2} \sqrt{\frac{p(1-p)}{n}}
$$

Che tuttavia non è utilizzabile perché $p$ non è noto!

- Se $n$ è elevato, rimpiazzo $p$ con $\hat{p}$:

$$
\hat{p} \pm z_{1-\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} \quad \begin{array}{l} \text{IC CLASSICO} \\ \to \text{RISTRATTO} \\ \text{A } (0,1) \end{array}
$$

---

## Pagina 138

IC MIGLIORATI

Hanno senso se $n$ non è elevato (come criterio approssimato potremmo adottare $n \hat{p} \text{ o } n (1 - \hat{p}) < 5$).

Ne esistono di diversi tipi, tra i quali:
- Il metodo del testo di Walpole et al., che tuttavia è molto complesso ("Metodo 2")
- Il metodo di Agresti e Coull, che invece è molto semplice: la formula dell'IC è la stessa, ma si applica dopo aver AGGIUNTO 2 SUCCESSI e 2 INSUCCESSI al campione osservato!

- ESEMPIO 9.14:

$$
n = 500 \quad x = 340 \quad \begin{matrix} \text{Abbonati ad un servizio} \\ \text{(nuclei famigliari)} \end{matrix}
$$

$$
p = \text{probabilità che una famiglia a caso si abboni}
$$

$$
= \text{proporzione di famiglie abbonate}
$$

$$
\hat{p} = \frac{340}{500} = 0.68 \quad \left( \tilde{p} = \frac{342}{504} = 0.679 \right)^{\text{Per } A-C:}
$$

---

## Pagina 139

3 diversi IC:

IC classico $(0.639, 0.721)$

IC Metodo 2 $(0.638, 0.719)$

IC Agresti-Coull $(0.638, 0.719)$

Ippotizziano $n=50$ e $x=34$ ($\hat{p}=0.68$)

IC classico $(0.551, 0.809)$

IC Metodo 2 $(0.542, 0.792)$

IC A-C $(0.541, 0.792)$

$n=25$ e $x=17$: $\hat{p}=0.68$ ($n(1-\hat{p})=8$)

IC Classico $(0.457, 0.863)$

IC Metodo 2 $(0.484, 0.828)$

IC A-C $(0.482, 0.828)$

$n=25$ e $x=21$ ($n(1-\hat{p})=4$)

IC Classico $(0.696, 0.984)$

IC Metodo 2 $(0.653, 0.936)$

IC A-C $(0.646, 0.941)$

$\longrightarrow$ Il metodo A-C coniuga SEMPLICITÀ e ACCURATEZZA!

---

## Pagina 140

DIMENSIONAMENTO DEL CAMPIONE (4)

$$
n = \frac{z_{1-\alpha/2}^2 \sigma^2}{e^2} \longrightarrow \frac{z_{1-\alpha/2}^2 p(1-p)}{e^2}
$$

- La formula generale è inutilizzabile, salvo che non si disponga di una stima preliminare di $p$.

- In caso contrario pongo $p = 1/2$ (caso "peggiore", dato che è il valore che rende massima $p(1-p)$).

IC PER LA DIFFERENZA TRA DUE PROPORZIONI (II)

i) $X_1, X_2, \dots, X_{n_x}$ CCS $X_i \sim \text{Bernoulli}(p_x)$

ii) $Y_1, Y_2, \dots, Y_{n_y}$ CCS $Y_i \sim \text{Bernoulli}(p_y)$

iii) I DUE CAMPIONI SONO INDIPENDENTI

- Di nuovo, particolarizziamo le formule generali; rimpiazzando $p_x$ e $p_y$ con le loro stime nella radice

---

## Pagina 141

IC classici (per grandi campioni):

$$
(\hat{p}_x - \hat{p}_y) \pm z_{1-\alpha/2} \sqrt{\frac{\hat{p}_x(1-\hat{p}_x)}{n_x} + \frac{\hat{p}_y(1-\hat{p}_y)}{n_y}}
$$

Ristretto all'intervallo $(-1, 1)$

- IC migliorati: il metodo di Agresti-Coull si applica anche in questo caso, si ottiene aggiungendo $1$ successo e $1$ insuccesso a ciascun campione ($2 + 2$ in totale) e applicando poi la formula

---

## Pagina 142

(1) VERIFICA D'IPOTESI: CONCETTI GENERALI

Nel seguito verranno introdotte molte definizioni (IN BLU)

- Un' IPOTESI STATISTICA è una CONGETTURA riguardante una o più (sotto) popolazioni.
$\rightarrow$ è un' AFFERMAZIONE su $\theta$ di un MODELLO STATISTICO PARAMETRICO

Idea di base: sulla base dei DATI, decidiamo se RIFIUTARE o NO l'ipotesi.

ES: Dati binari, $12$ difettosi su $100$, è ragionevole concludere che $p = \text{PROP. DIFETTOsi}$ sia $> 10\%$?

(2) IPOTESI NULLA e ALTERNATIVA

- IPOTESI NULLA $H_0$: è l'ipotesi da verificare
- IPOTESI ALTERNATIVA $H_1$: è l'ipotesi che vale se RIFIUTO $H_0$.

ES: Dati binari

$$
\left\lbrace 
\begin{aligned}
H_0 &: p = 0,10 \\
H_1 &: p > 0,10
\end{aligned}
\right.
$$

---

## Pagina 143

2

Mediante la verifica d'ipotesi

$$
\begin{matrix}
& & \swarrow & & & \searrow \\
\text{RIFIUTO } H_0 & \text{se c'è sufficiente} & & & & \text{NON RIFIUTO} \\
\text{evidenza nei dati} & & & & & H_0 \text{ in} \\
& & & & & \text{caso contrario}
\end{matrix}
$$

Analogia con un processo penale

$$
\left\lbrace
\begin{aligned}
& H_0 : \text{imputato innocente} \longrightarrow \text{"status quo"} \\
& H_1 : \text{imputato colpevole}
\end{aligned}
\right.
$$

$$
\left\lbrace
\begin{aligned}
& \text{Con prove schiaccianti} \longrightarrow \text{imputato è} \\
& \phantom{\text{Con prove schiaccianti}} \text{condannato} \\
& \phantom{\text{Con prove schiaccianti}} (\text{RIFIUTO } H_0) \\
& \text{In mancanza di} \\
& \text{prove} \longrightarrow \text{imputato non viene} \\
& \phantom{\text{In mancanza di}} \text{condannato} \\
& \phantom{\text{In mancanza di}} (\text{NON RIFIUTO } H_0)
\end{aligned}
\right.
$$

- \underline{STATISTICA TEST} : è una statistica che \\
($T$ o $Z$) utilizziamo per decidere \\
se rifiutare o meno $H_0$ \\
$\llcorner$ Viene utilizzata per effettuare il TEST d'ipotesi

---

## Pagina 144

- Sia $T$ la statistica test prescelta: i valori possibili della statistica vengono divisi in $2$ gruppi:

- Regione Critica: sono i valori che portano al rifiuto di $H_0$

$\underline{\text{RIMANENTI VALORI}}$ : non portano al rifiuto di $H_0$

ES: 

$$
\text{ES: } \left\lbrace \begin{array}{l} H_0: p = 0.10 \\ H_1: p > 0.10 \end{array} \right. \quad \begin{array}{l} X_1, X_2, \dots, X_n \\ \text{CCS}, n=100 \\ X_i \sim \text{Bernoulli}(p) \end{array}
$$

Poniamo 

$$
T = \sum_{i=1}^{100} X_i
$$

$$\text{Regione Critica}_{R_C} = \left\lbrace T > 15 \right\rbrace$$

[Grafico della retta dei numeri:]
- Da $0$ a $15$: $\text{NON RIFIUTO } H_0$
- Da $15$ a $100$: $\text{RIFIUTO } H_0$

Nota: se $t \in R_C$ si dice che "IL RISULTATO È SIGNIFICATIVO (CONTRO $H_0$)"

---

## Pagina 145

(4)

* ERRORI nella verifica d'ipotesi

* ERRORE $I^\circ$ TIPO: Rifiuto $H_0$ quando è VERA

* ERRORE $II^\circ$ TIPO: NON RIFIUTO $H_0$ quando è FALSA

L'errore di $I^\circ$ TIPO è ritenuto più grave: si pensi all'analogia con il processo penale

* LIVELLO di SIGNIFICATIVITÀ (AMPIEZZA DEL TEST)

* $\alpha = P(\text{ERRORE } I^\circ \text{ TIPO})$

ES: $\alpha = P(T > 15 \ ; \ p = 0.10)$

$$
= \sum_{t=16}^{100} \binom{100}{t} \ 0.10^t \ (0.90)^{100-t} = 0.04
$$

È un valore basso, il che è una buona proprietà perché voglio commettere ERRORE $I^\circ$ TIPO raramente

Associato al livello $\alpha$ esiste anche

* $\beta = P(\text{ERRORE } II^\circ \text{ TIPO})$

---

## Pagina 146

Nell'esempio: $\beta$ è una funzione del valore di $p$,
tra quelli $> 0.10$

$$
\beta(p) = P(T \le 15 \text{ ; } p)
$$

Se

$$
\begin{aligned}
p &= 0.15 \qquad \beta = 0.568 \\
p &= 0.20 \qquad \beta = 0.129 \\
p &= 0.40 \qquad \beta = 0.0004
\end{aligned}
$$

[Grafico cartesiano con asse y $\beta(p)$ e asse x $p$. Sul grafico sono indicati i punti $0.96$ sull'asse y, e $0.10$ e $0.3$ sull'asse x]

* POTENZA di un Test: è $1-\beta$ ovvero la PROBABILITÀ di un CORRETTO RIFIUTO $H_0$

$\underline{\text{Nota bene}}$: $\alpha$ e $\beta$ sono collegati tra loro, non posso annullarli simultaneamente.
In pratica: fissiamo $\alpha$ ad un valore basso, e verifichiamo il valore di $\beta$.

---

## Pagina 147

PROPRIETÀ: per un test CONSISTENTE (ragionevole), (6)
per $\alpha$ fissato si ha che $\beta$ decresce dell'aumentare della dimensione del campione
$\longrightarrow$ posso agire su $\beta$ aumentando $n$

ES.: Ipotizziamo di raddoppiare $n=200$

$$
R_C = \left\lbrace T > 27 \right\rbrace
$$

$$
\alpha = \sum_{t=28}^{200} P(T=t; p=0.10) = 0.043
$$

$\llap$ $\llap$ lo più o meno come prima

Se

$$
\begin{aligned}
p &= 0.15 : \quad \beta = 0.317 \\
p &= 0.20 : \quad \beta = 0.011 \\
p &= 0.25 : \quad \beta \approx 0
\end{aligned}
\left\lbrace
\begin{aligned}
&\text{più bassi} \\
&\text{del caso} \\
&n=100
\end{aligned}
\right.
$$

---

## Pagina 148

ES: STATISTICA TEST NORMALE (7)

$n = 36$ pesi $X_1, \dots, X_n$ CCS

$\sigma = 3.6 \, \text{kg}$ (NOTA)

$$
\left\lbrace 
\begin{array}{l}
E(X_i) = \mu \\
V(X_i) = \sigma^2
\end{array}
\right.
$$

$$
\left\lbrace 
\begin{array}{l}
H_0: \quad \mu = 68 \\
H_1: \quad \mu \neq 68 \longrightarrow \text{cioè } \mu > 68 \text{ oppure } \mu < 68
\end{array}
\right.
$$

$$
T = \overline{X} \sim N\left(\mu, \frac{3.6^2}{36}\right) \quad \begin{smallmatrix} \text{STATISTICA} \\ \text{TEST} \end{smallmatrix}
$$

$$
R_C = \left\lbrace T < 66.8 \quad \text{oppure} \quad T > 69.2 \right\rbrace
$$

$$
\alpha = P_{H_0}\left(\overline{X} < 66.8\right) + P_{H_0}\left(\overline{X} > 69.2\right)
$$

$$
\parallel
$$

$$
0.0228 \quad + 0.0228 = 0.0455
$$

$\beta$ dipende dal vero $\mu$: per

$$
\begin{array}{l}
\mu = 69 \longrightarrow \beta = 0.630 \\
\mu = 70 \longrightarrow \beta = 0.0912 \\
\mu = 71 \longrightarrow \beta = 0.013
\end{array}
$$

---

## Pagina 149

* DISTRIBUZIONE NULLA di $T$ : vale sotto $H_0$
* DISTRIBUZIONE ALTERNATIVA di $T$ : " " $H_1$

* TIPI DI IPOTESI

* IPOTESI ALTERNATIVA UNILATERALE


$$
\left\lbrace 
\begin{aligned}
H_0: &\quad \theta = \theta_0 \\
H_1: &\quad \theta > \theta_0 \left( \text{oppure } \theta < \theta_0 \right)
\end{aligned}
\right.
\quad \nearrow^{\text{TEST AD UNA CODA}}
$$


NOTA BENE $H_0: \theta \leq \theta_0$ è lo stesso se $H_1: \theta > \theta_0$

* IPOTESI ALTERNATIVA BILATERALE


$$
\left\lbrace 
\begin{aligned}
H_0: &\quad \theta = \theta_0 \\
H_1: &\quad \theta \neq \theta_0
\end{aligned}
\right.
\quad \longrightarrow^{\text{TEST A DUE CODE}}
$$

---

## Pagina 150

- Come scelgo $H_0$ e $H_1$? Dipende dal contesto applicativo, da quali informazioni sono disponibili e a quale conclusione si vuole giungere.

ES 1: Se $p=0.10$ era il tasso di prodotti difettosi e sospetto sia peggiorato, l'alternativa ragionevole è $p > 0.10$.

ES 2: Se $\mu = 68$ era un peso medio ragionevole, ma non abbiamo informazioni riguardo in quale direzione potrebbe essere diversa, allora $\mu \neq 68$ è l'alternativa ragionevole.

IL $P$-VALUE

- PROCESSO DECISIONALE nella VERIFICA D'IPOTESI
- Fisso $\alpha = 0.05$ (oppure $\alpha = 0.01$, di solito)
- Se uso una statistica Test $Z \sim N(0, 1)$ sotto $H_0$ per un test bilaterale ottengo

$$
R_C = \left\lbrace z < -1.96 \cup z > 1.96 \right\rbrace
$$

$R_{0.05}$ $\to$ per indicare il valore di $\alpha$

---

## Pagina 151

(10)

[Grafico di una distribuzione normale con aree di coda evidenziate etichettate $\alpha/2$ e valori $-1.96$, $0$, $1.96$ sull'asse delle ascisse]

- Tuttavia $z_{\text{oss}} = 2$ o $z_{\text{oss}} = 4$, che cadono entrambe in $R_{0.05}$, forniscono evidenze molto diverse! Questo è quantificato dal P-VALUE

- Il P-VALUE è una STATISTICA calcolata sul campione osservato: è definita come

IL LIVELLO PIÙ BASSO A CUI RISULTA SIGNIFICATIVO IL VALORE OSSERVATO DELLA STATISTICA TEST

ES: 

$$
z_{\text{oss}} = 2 \quad p = P_{H_0} (\left\vert Z \right\vert > 2) = 0.0455
$$

$\hookrightarrow$ EVIDENZA MODERATA CONTRO $H_0$

$$
z_{\text{oss}} = 4 \quad p = P_{H_0} (\left\vert Z \right\vert > 4) = 0.0000633
$$

$\hookrightarrow$ EVIDENZA FORTE CONTRO $H_0$

---

## Pagina 152

- In pratica: calcolo $P\text{-}\mathrm{VALUE}$ e lo confronto con una soglia (che, in pratica, corrisponde al valore di $\alpha$)

$\text{TABELLA SPESSO (ma non sempre) UTILIZZATA}$


| Valori $P\text{-}\mathrm{VALUE}$ | Evidenza contro $H_0$ |
| :--- | :--- |
| $0.05 < p \le 0.1$ | $\text{MARGINALE (molto debole)}$ |
| $0.01 < p \le 0.05$ | $\text{MODERATA}$ |
| $0.001 < p \le 0.01$ | $\text{FORTE}$ |
| $p \le 0.001$ | $\text{MOLTO FORTE}$ |


- Esiste una differenza sostanziale tra $\text{SIGNIFICATIVITÀ STATISTICA}$ e $\text{SIGNIFICATIVITÀ INGEGNERISTICA O SCIENTIFICA}$

$\text{N.B.}$

$$
\text{STATISTICA TEST} \in R_\alpha \iff P\text{-}\mathrm{VALUE} \le \alpha
$$

---

## Pagina 153

VERIFICA DI IPOTESI SULLA MEDIA (VARIANZA NOTA)

$X_1, X_2, \dots, X_n$ ccs 
$n$ elevato

$$
\left\lbrace \begin{aligned}
E(X_i) &= \mu \\
V(X_i) &= \sigma^2 \text{ NOTA}
\end{aligned} \right.
$$

TLC: $\overline{X} \stackrel{a}{\sim} N \left(\mu, \frac{\sigma^2}{n}\right)$

$$
\left\lbrace \begin{aligned}
H_0 &: \mu = \mu_0 \\
H_1 &: \mu \neq \mu_0
\end{aligned} \right.
$$

Sotto $H_0 \quad \overline{X} \stackrel{a}{\sim} N \left(\mu_0, \frac{\sigma^2}{n}\right)$

$$
Z = \frac{\overline{X} - \mu_0}{\sqrt{\frac{\sigma^2}{n}}} \quad \text{STATISTICA TEST}
$$

$R_\alpha = \left\lbrace z < z_{\alpha/2} \text{ oppure } z > z_{1-\alpha/2} \right\rbrace$
$\phantom{R_\alpha} = \left\lbrace |z| > z_{1-\alpha/2} \right\rbrace$

---

## Pagina 154

* $\alpha$ è $P(\text{ERRORE I}^{\circ}\text{ TIPO})$, infatti:

$$
P_{H_0}\left(\lvert Z \rvert > z_{1-\alpha/2}\right) = \alpha \quad (\text{per } n \text{ elevato})
$$

* $\text{P-VALUE} : \quad p = P_{H_0}\left(Z > \lvert z_{oss} \rvert \cup Z < -\lvert z_{oss} \rvert\right)$

$$
= 2 \, P_{H_0}\left(Z > \lvert z_{oss} \rvert\right) = 2 \left(1 - \Phi\left(\lvert z_{oss} \rvert\right)\right)
$$

* $H_1$ UNILATERALE

$$
\left\lbrace 
\begin{aligned}
H_0 &: \mu = \mu_0 \quad (\text{o anche } \mu \le \mu_0) \\
H_1 &: \mu > \mu_0
\end{aligned}
\right.
$$

$$
R_{\alpha} = \left\lbrace Z > z_{1-\alpha} \right\rbrace
$$

$\text{P-VALUE} : \quad p = P_{H_0}\left(Z > z_{oss}\right) = 1 - \Phi(z_{oss})$

* Per il caso $\left\lbrace 
\begin{aligned}
H_0 &: \mu = \mu_0 \quad (\text{o anche } \mu \ge \mu_0) \\
H_1 &: \mu < \mu_0
\end{aligned}
\right.$

---

## Pagina 155

si ottiene

$$
R_\alpha = \lbrace z < z_\alpha \rbrace
$$

$$
p = P_{H_0} \left( z < z_{oss} \right) = \Phi(z_{oss})
$$

ESEMPIO 10.4

$$
\mu_0 = 8.0 \text{ kg} \quad \text{carico di rottura} \longrightarrow \text{affermazione produttore}
$$

$$
CCS \quad n = 50 \quad \overline{x} = 7.8 \text{ kg} \quad \sigma = 0.5
$$

$$
\begin{cases}
H_0 \colon \mu = 8 \\
H_1 \colon \mu \neq 8
\end{cases}
\quad \alpha = 0.01
$$

$$
R_{0.01} = \lbrace |z| > 2.575 \rbrace
$$

$$
z_{oss} = \frac{7.8 - 8.0}{0.5 / \sqrt{50}} = -2.83 \longrightarrow \text{RIFIUTO } H_0
$$

$$
p = 2 P_{H_0} (z > 2.83) = 0.0046
$$

---

## Pagina 156

III RELAZIONE CON IC (4)

* Non rifiuto $H_0$ se $- z_{1-\alpha/2} < Z < z_{1-\alpha/2}$
ovvero se $- z_{1-\alpha/2} < \dfrac{\overline{x} - \mu_0}{\sigma/\sqrt{n}} < z_{1-\alpha/2}$

$$
\overline{x} - z_{1-\alpha/2} \dfrac{\sigma}{\sqrt{n}} < \mu_0 < \overline{x} + z_{1-\alpha/2} \dfrac{\sigma}{\sqrt{n}}
$$

* In altri termini: Non Rifiuto $H_0$ in (con $R_\alpha$) \left\lbrace \begin{array}{l} H_0: \mu = \mu_0 \\ H_1: \mu \neq \mu_0 \end{array} \right.

se $\mu_0 \in IC$ per $\mu$ di livello $1-\alpha$

LIVELLO $IC = 1 - P(\text{errore } I^\circ \text{TIPO})$

* Ovvero:

- Posso usare $IC$ per effettuare verifica d'ipotesi
- Posso definire $IC$ utilizzando la verifica d'ipotesi

* Per $H_1$ unilaterale la relazione vale con $IC$ unilaterale

---

## Pagina 157

(1) CASO $\sigma^2$ IGNOTA (5)

- GRANDI CAMPIONI ($n \geq 30$): rimpiazzo $\sigma^2$ con $S^2$
- PICCOLI CAMPIONI: abbiamo risultati per campioni NORMALI

$$
X_1, X_2, \dots, X_n \text{ ccs } X_i \sim N(\mu, \sigma^2)
$$

$$
\left\lbrace \begin{aligned}
H_0: &\quad \mu = \mu_0 \\
H_1: &\quad \mu \neq \mu_0
\end{aligned} \right.
$$

Sotto $H_0$:

$$
T = \frac{\overline{X} - \mu_0}{\sqrt{\frac{S^2}{n}}} \sim t_{n-1}
$$

$$
R_\alpha = \left\lbrace |t| > t_{n-1; 1-\alpha/2} \right\rbrace
$$

P-VALUE:

$$
p = 2 \left( 1 - F_{t_{n-1}}(|t_{oss}|) \right)
$$

---

## Pagina 158

$H_1: \mu > \mu_0 \quad R_\alpha = \left\lbrace t > t_{n-1; 1-\alpha} \right\rbrace$ 
$$ p = 1 - F_{t_{n-1}} (t_{oss}) $$

$H_1: \mu < \mu_0 \quad R_\alpha = \left\lbrace t < \underbrace{t_{n-1; \alpha}}_{-t_{n-1; 1-\alpha}} \right\rbrace$
$$ p = F_{t_{n-1}} (t_{oss}) $$

---

## Pagina 159

VERIFICA D'IPOTESI SULLE MEDIE DI DUE CAMPIONI $7$

1) VARIANZE NOTE ($e$ CAMPIONI ELEVATI)

2) VARIANZE IGNOTE

3) DATI APPAIATI

- 1) VARIANZE NOTE (GRANDI CAMPIONI)

ASSUNZIONI:

i) $X_1, X_2, \dots, X_{n_x}$ CCS 
$n_x$ elevato

$$
\left\lbrace
\begin{aligned}
E(X_i) &= \mu_X \\
V(X_i) &= \sigma_X^2
\end{aligned}
\right.
$$

NOTA

ii) $Y_1, Y_2, \dots, Y_{n_y}$ CCS
$n_y$ elevato

$$
\left\lbrace
\begin{aligned}
E(Y_i) &= \mu_Y \\
V(Y_i) &= \sigma_Y^2
\end{aligned}
\right.
$$

NOTA

iii) I DUE CAMPIONI SONO INDIPENDENTI

$$
\left\lbrace
\begin{aligned}
H_0 &\colon \mu_X = \mu_Y \\
H_1 &\colon \mu_X \neq \mu_Y \\
&\phantom{:} \quad > \\
&\phantom{:} \quad <
\end{aligned}
\right.
$$

Si estende a

$$
H_0 \colon \mu_X - \mu_Y = \Delta_0
$$

---

## Pagina 160

$$
Z = \frac{\overline{X} - \overline{Y} - \Delta_0}{\sqrt{\frac{\sigma_X^2}{n_X} + \frac{\sigma_Y^2}{n_Y}}} \stackrel{a}{\sim} N(0, 1) \text{ sotto } H_0
$$

$$
z_{oss} = \frac{\overline{x} - \overline{y} - \Delta_0}{\sqrt{\frac{\sigma_X^2}{n_X} + \frac{\sigma_Y^2}{n_Y}}} \quad\quad R_\alpha = \lbrace |z| > z_{1-\alpha/2} \rbrace
$$

$$
p = 2 \left( 1 - \Phi(|z_{oss}|) \right)
$$

- Per varianze ignote, ma campioni elevati:
stesse formule utilizzando $s_X^2$ e $s_Y^2$

2) Varianze ignote (e possibilmente diverse)

- Campioni normali (e piccoli)

$$
T = \frac{\overline{X} - \overline{Y} - \Delta_0}{\sqrt{\frac{s_X^2}{n_X} + \frac{s_Y^2}{n_Y}}} \sim t_\nu \text{ sotto } H_0
$$

$\nu = \text{ formula di WELCH / SATTERTHWAITE}$

---

## Pagina 161

$$
R_\alpha = \left\lbrace |t| > t_{0; 1 - \alpha/2} \right\rbrace
$$

- Per $H_1$ unilaterale, $R_\alpha$ è come nel caso per grandi campioni rimpiazzando i percentili della $N(0,1)$ con quelli della $t$

3) DATI APPAIATI

$X_i$ e $Y_i$ RILEVATI SULLA STESSA UNITA (NON INDIPENDENTI)

$$
D_i = X_i - Y_i \quad, i = 1, \dots, n
$$

$$
D_i \sim N(\mu_D, \sigma^2_D) \quad (\text{CASO NORMALE})
$$

$$
T = \frac{\overline{D} - \Delta_0}{\sqrt{\frac{S^2_D}{n}}} \sim t_{n-1} \quad \text{sotto } H_0
$$

Nota:

$$
\begin{cases}
H_0: \mu_X - \mu_Y = \Delta_0 \\
H_1: \mu_X - \mu_Y \neq \Delta_0 \\
\phantom{H_1: \mu_X - \mu_Y} >_{<}
\end{cases}
\longrightarrow
\begin{cases}
H_0: \mu_D = \Delta_0 \\
H_1: \mu_D \neq \Delta_0 \\
\phantom{H_1: \mu_D} >_{<}
\end{cases}
$$

---

## Pagina 162

(11) VERIFICA D'IPOTESI PER UNA PROPORZIONE (1)

$X_1, X_2, \dots, X_n \quad C.C.S.$

$X_i \sim \text{Bernoulli } (p)$

$$
\left\lbrace 
\begin{aligned}
H_0: &\quad p = p_0 \\
H_1: &\quad p \neq p_0
\end{aligned}
\right.
$$

$\hookrightarrow$ oppure $H_1$ UNILATERALE

Sotto $H_0$: 

$$
n \hat{p} = \sum_{i=1}^n X_i \sim B(n, p_0)
$$

$$
TLC \quad \hat{p} \stackrel{a}{\sim} N\left(p_0, \frac{p_0(1-p_0)}{n}\right)
$$

STATISTICA TEST: di solito si usa la v.c. standardizzata

$$
Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}} \stackrel{a}{\sim} N(0,1)
$$

Sotto $H_0$

---

