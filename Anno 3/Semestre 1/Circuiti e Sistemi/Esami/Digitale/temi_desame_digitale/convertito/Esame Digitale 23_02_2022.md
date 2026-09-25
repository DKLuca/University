---
fonte: "Esame Digitale 23_02_2022.pdf"
metodo: "ocr"
da_rivedere: true
---

Prova Scritta di Circuiti e Sistemi Elettronici
(DIGITALE)
23 Febbraio 2022

Si consideri una tecnologia CMOS i cui_ gate devono avere tempi di
salita e discesa simmetrici. Si vuole utilizzare la metodologia del logical effort

5 pas
per determinare il tempo di attraversamento di una serie di gate logici e trovare i
dimensionamenti ottimi che ne consentono la minimizzazione tenendo in consider-
azione la presenza di interconnessioni tra un gate e Valtro.

re

 

INo—

7 Gi G2

OUT
°

 

 

 

 

 

 

 

 

 

 

 

sa, OS

I

1. Dato il circuito dove per il momento si assume G1 e G2 dud generici bate
=. si ne di a

 

a parametri concentrati a pi-greco ad 1 cella elit) si utilizzi il metodo di Elmore
per calcolare il ritardd t IN-A = un’escursione del lel segnale al 90%.

Si consiglia di scrivere il ritardo nella P| = tyo [gi (hi + hwi) +71 + Pwal
dove i coefficienti g,, hy e p;, in accordo con la metodologia del logical effort,
sono definiti come g; = Ryu Cy /tpo, hi = Ca/Cy e py = RuC,1/tpo (con C;; la
capacita di ingresso di un generico gate logico e R, la resistenza di uscita del
generico gate considerando gia un’escursione del segnale al 90%) mentre hy;
€ Pwi Sono termini introdotti dalla presenza dell’interconnessione.__


---

 

C+ soot

 

 

2. Si scriva l’espressione della condizione che minimizza il ritardo dal nodo IN

al nodo OUT assumendo che i parametri delle interconnessioni non possano
essere modificati dalla procedura di minimizzazione,| In particolare si riporti—

di ingresso del gate stesso.

. Calcolare la capacita di ingresso del gate G2 che minimizza il ritardo come

ricavato al punto 2). Si considerino ora i gate G1 e G2 come un gate NAND»
e NOR; rispettivamente, | Sono noti i seguenti parametri: le interconnessioni
hanno una resistenza per unita di lunghezza r= 28 2./m e capacita per unita
di lunghezza c=0.45 fF/um.|La lunghezza della prima interconnessione é di
40m, mentre la seconda é di 801m. Vengono inoltre forniti: i) il ritardo
caratteristico della tecnologia ty) = 20ps; e ii) la capacita di ingresso di un
transistore a dimensionamento minimo (quindi con W =L= Drain) Cm =
2.5fF. La conducibilitad intrinseca dei transistori nMOS 6 pari a Br, =300
HA/V? mentre quella dei transistori pMOS vale Bi, =150 wA/V*. Il gate
NAND; ha un dimensionamento della rete di pull-up pari a Sp,vanp=2 f,,/ By.


---

Soluzione della prova Scritta di Circuiti e Sistemi Elettronici
(DIGITALE)
23 Febbraio 2022

1. Il circuito equivalente utilizzando una cella a II per descrivere l’interconnessione, diventa:

Secondo il modello di Elmore possiamo scrivere:

CG C
trn—a,90% = 2-37 = 2.3 [(Gn * a Rei+ (= + Ca) (Roi + Rwv)|

= 23 [Rex (Cwi + Ca) + Rwi ( + Ca) + RerCp|

definendo Ry = 2.3R¢; la resistenza da utilizzare nel modello del logical-effort, e moltiplicando
e dividendo per il tempo caratteristico della tecnologia t,o otteniamo:

 

Ra, C C; R C Ra,

tin—A.90% te tpo t1etl wi 4: t2 +23 Wi Wi + Ca ey tipl
typo Ca Cy tpo 2 tyo

—— ~- ~ ~ —S
a1 hwithi Pwi PL

= tpo [gr (ha + hwi) + pi + Pw) -
Si nota che, nel caso in cui Cy e Ryi siano nulli, si ottiene il risultato noto tyy_490% =
tpo (gihi + p1)-
. Grazie al risultato di cui al punto precedente possiamo scrivere:
trn-ovT.90% = tpo {[g1 (hi + hw) + Pr + Pwr] + [92 (ha + hwa) + P2 + Pwal}

e sapendo che hg = Cz/C2 ed esplicitando in funzione di h; otteniamo

2.3K Ci
t1n-ouT.90% = tpo {[o (hy + hwi) + we ( + inCu) + n| + E (ase) + pw2 + »| |
to 2 Cuhi

Visto che Cj; é noto essendo un parametro di progetto, l’unica dipendenza dai dimensionamenti
si ha attraverso h;, dunque minimizzare ty~—our significa annullare il termine 0t/0h1.
ot Rwi Cr+Cwe _

 

— = O23 een OS —
Bag ee eee ee
Rwi Cr Cw2
= 91 + 2.83—Cy — g2 = - =0
n no Ct 2 Gane Cah
—— ——

ha/hi hwa/hi

si ottiene quindi

R
(a + 235 cn) hy = go (ho + hwa)-


---
