---
fonte: "analogica_con_soluz_06_09_2024.pdf"
metodo: "ocr"
da_rivedere: true
---

Prova scritta di Fondamenti di Elettronica
6 Settembre 2024

INGING ree rare esas etree ene sede ere Gognomies memati manecue cere Matricolar! <ccccvcins.

Punti Assegnati: ...... Yi sisie Wiener [aeons Picnsemt bares Vere er ede

In riferimento al circuito di Fig. 1 si chiede di:

1. Trascurando l’effetto Early e considerando un modello a soglia per il solo diodo D, dis-
egnare qualitativamente la caratteristica statica Vo = f(Vin) del circuito per 0 < Vin < Veg,
calcolando i valori di tensione per i quali il BJT si accende, rimane in regione normale o va in
saturazione, (11 Punti)

2. Determinare il valore di Vec,sat considerando o = 0.8. (2 punti)

3. Tenendo conto dell’effetto Early e delle capacita del BJT, calcolare i parametri differenziali e
disegnare il circuito equivalente ai piccoli segnali per il punto di lavoro corrispondente a Vin = 3.9 V.
Anche in questo caso considerare il modello a soglia per il diodo D. (6 Punti)

4. Calcolare la matrice Y del circuito, considerando Vin e Vo i nodi di ingresso e di uscita del doppio
bipolo. (6 punti)

5. Trovare lespressione del guadagno di corrente di corto circuito A;cco e dimensionare i condensatori
C e C2 in modo tale che Aj,cc presenti un polo p = 3 krad/s e uno zero z = 900 krad/s. (5 punti)

Vez =5V, Vin =25 mV, R= kQ,
Q: Is = 10-4 A, Bro = fo = 100, Br = 1, Va = 30 V, Cac = 100 pF, Caz = 300 pF,

D: Vy,p = 0.6 V.

 

Figura 1


---

Soluzione del compito di Fondamenti di Elettronica
settembre 2009

1. Fino a che la tensione V,, non é sufficiente bassa per mandare in conduzione il diodo, la base del
transistore risulta isolata. Per tanto il transistore rimarrd spento fino tanto che Vin > Vx — Vy.» =
4.4 V. Per V;,, < 4.4 V, il transistore comincia a condurre in regione normale e sulla sua giunzione
base-emettitore cade una tensione Veg = Vex — Vin — Vy,p. Per cui risulta:

Ver — Vin — V;
Io = Igexp (222?)

Di conseguenza la tensione Vp risulta:

Vo = Rls exp jae Ee = = = |

Per tensioni Vin molto basse, il transistore Q entra nella regione di saturazione e Vo = Vezr—Vec,sat-
Questo accade quando la tensione di collettore sale fino al valore di tensione della base:

—

Vin + V>,p = Risexp ( Vin

Risolvendo iterativamente quest’equazione non lineare

 

 

Via + Vi
Hie Se 5 oe n( +)
in EE 7D th a oe
si ottiene:
it Vin [V]
1/ 42
2) 3.727
3 | 3.730
4 | 3.730

 

 

 

 

per cui il transistore entra in regione di saturazione, quando V;,, = 3.73 V. La caratteristica statica
del circuito é la seguente:

   

 

 

3 44 Vv

ae
re eecereerneees

FIGURA 1


---

2. Il valore di Ver,sae vale:

obp + Gr+1
(1—2)8p

3. Il circuito equivalente per piccoli segnali é mostrato in Fig.2.

C2
_ Fl
all a Bot

Viste’ Vaal ( ) =0.15V

 

 

   

 

Te

FIGURA 2

Per Vin = 3.9 V, il transistore lavora in regione normale, per cui la corrente di collettore vale:

Ie = Isexp (“EY =) = 4.85 pA
per cui si ottiene:
Tre = Aalin — 515 ko
tf = = 6.18 Ma
9m = 7 =0.101 ms

Tl guadagno di corrente di corto circuito é espresso come segue:

(1

Aico = TOL 5 + Oua\ran Fi
dove Cy = Car + C, and Cho = Cac + C2
4. Il polo e lo zero del guadagno di corrente di corto circuito valgono:

1
= TpE(Che + Cac)
Im

ys. =
* Che

per cui i valori di capacitd necessari sono C; = 131.7 pF e C2 = 115.5 pF.

()
(2)
(3)

(4)
(5)

Il valore del guadagno di corrente di corto circuito a w = 20 krad/s é pari a Aj qo = 14.84.
