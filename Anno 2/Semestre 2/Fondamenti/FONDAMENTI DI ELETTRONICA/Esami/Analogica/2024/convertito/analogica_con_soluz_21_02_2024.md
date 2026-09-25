---
fonte: "analogica_con_soluz_21_02_2024.pdf"
metodo: "ocr"
da_rivedere: true
---

~
—
e 1S
a8
\\ \" v
a? i :
go Pp
= rs : |
At ~
sa NS IR ht
\ Wl} \
SF [SP [Sy le ei
= \\
il de 3
Pde 7
HEEEREEE EEE ae
Nie :
¢ Lx + Sos
E Al | 5 (Sis $8 2
>\>

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 


---

Soluzione del compito di Fondamenti di Elettonica
21 febbraio 2024 |

1. Ipotizziamo il BJT acceso e in regione normale. Non essendoci effetto Early, La corrente nel BJT
é definita dal seguente sistema di equazioni:

 

Iz = BRS “Ic (1) |
Br
_ Vee— Ves — Vi
I,
Ves = Valn— (3) |
Is |

Sostituendo Eq.(1) in Eq.(2), otteniamo

risolto con il metodo iterativo:

 

Il transistore T> é connesso a diodo per cui lavora sicuramente in saturazione. Quindi:

2_ Vee — Ves (4)

Ips2 = BMOS (y.,4 —Vr) R

2
da cui si ottiene un’equazione di secondo grado in Vs, le cui soluzioni sono: Vgs; = 3.32 Ve
Vaso = —3.32 V. Chiaramente la seconda é da scartare. Il transistore T; vede la stessa Vas e,
supponendolo anch’esso in saturazione, otteniamo Ips3 = Ips2 = 2.683 mA (il circuito é uno
specchio di corrente).
Ora la corrente sulla resistenza Rc vale Ipc = Ic—Ips3 = 1.356 mA, per cui Vo = RoIrc = 4.07 V. |
Tale valore verifica le ipotesi che il BJT lavori in regione normale e che Ty sia in saturazione.

 

2. I parametri differenziali del BJT valgono: rre = Vin8r/Ic = 634 2 € gmp = Ic /Vin = 158 mS.
I due MOSFET invece sono polarizzati alla stessa tensione, per cui possiamo calcolare un’unica
9mm = Bmos(Ves — Vr) = 2.3 mS. Non vengono considerati, infine, né l'effetto Early, né la
modulazione di canale, quindi non abbiamo né ree, né ras.

Lo specchio di corrente si comporta come un generatore ideale di corrente, quindi al piccolo segnale
pué essere visto come un lato aperto e quindi escluso dal circuito equivalente ai piccoli segnali, il
quale risulta essere quello di un doppio carico, come indicato in figura:

vi ib io vo

 

3. Con riferimento al circuito qui sopra, per tenere calcolare le componenti della matrice ammettenze,
possiamo lavorare nel dominio del tempo (non ci sono effetti reattivi) e utilizzare la loro definizione:

ij ip 1
= — = = — 48
iG wee aaa

 

 


---

 

 

 

i
= — =0
yi2 eal Mees
Yat Vilyco tree + (Bo+1ieRe Tre +(Bo+1)Re
lo to 1
= — = —~ = — = 0.333 mS
el ike ke

 

questo perché, quando imponiamo v; = 0, otteniamo che —iprre = (80 + 1)ipRe, da cui i, = 0.

. Per calcolare i] guadagno di tensione sfruttiamo la matrice della ammettenze appena calcolata ed
otteniamo:
Ay a _ 21 — BoRc
y= Tee + (80 + 1)Re
. In assenza di effetto Early, la corrente nel BJT é impostata dalla tensione V; e quindi risulta fissata.
Quindi il punto di lavoro di T; é bloccato. La sua corrente Ic, poi, si ripartisce sulla resistenza Re
e sullo specchio di corrente. Un’eventuale variazione di R cambierebbe la corrente nello specchio,
per cui cambierebbe anche quella sulla resistenza Ro (la somma deve essere costante e pari a Ic),
andando a modificare la tensione Vo in uscita.
Se R aumenta, la corrente nello specchio diminuisce, mentre quella di Rc aumenta. Di conseguenza
aumenta anche Vo, rischiando di mandare in saturazione il BJT. Invece, se R cala, la corrente nello
‘specchio aumenta, diminuendo la corrente su Rc e Vo. In questo secondo caso, non ci sono rischi
per il BJT di uscire dalla regione normale.
Visto che il punto di lavoro del BJT non cambia con R, il guadagno del circuito é sempre lo stesso,
in quanto rj_ in Eq.(5) rimane fissata da Ic.

=-14.4 (5)
