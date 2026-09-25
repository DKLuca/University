---
fonte: "analogica_con_soluz_19_09_2024.pdf"
metodo: "ocr"
da_rivedere: true
---

Prova scritta di Fondamenti di Elettronica
19 settembre 2024

santaks tes Cognome: . i605 22 0cb sees bey essere see Matricola; --
Punti Assegnati: ....../+++++
Con riferimento al circuito di Fig. 1:

1. Trascurando l'effetto Early, determinare Ry e Ry in modo tale da polarizzare il transistore nella
condizione Vo=0 V, Ig=10 pA. (5 punti}

. Determinare di quanto varierebbe Ja tensione di uscita Vo (a parita di Rg e Ry, caicolate al punto
precedente) nel caso il transistore presentasse una tensione di Early V4 = 20 V- Suggerimento:
esprimere le equazioni del circuito in funzione di Ig. (9 punti)

. Nell’ipotesi che la tensione di alimentazione sia affetta da un rumore veo di piccola ampiezza che
si sovrappone al valore di Voc, disegnare il circuito equivalente ai piccoli segnali che descrive it
funzionamento del circuito. In questo caso, si trascuri leffetto Early ¢ si usi ii punto di lavoro
trovato al punto 1 per calcolare i parametri differenziali. (3 punti)

Per il circuito troyato al punto 3, determinare la funzione di trasferimento Vo(s)/Veo(s) ne} dominio
dei piccoli segnali. (8 punti)

- Sfruttando il risultato al punto 4, determinare la variazione della, tensione di uscita corrisponderente
all'applicazione di una tensione di alimentazione Veo = 2.05 V. (3 punti)

 

Veg = -2.-V; Voo = 2 Vs Vin = 288 mV, Ig = 10 fA, Bro = 100.

 


---

    

Soluzione del compito di Fondamenti di Elettronica
19 settembre 2024

1. Per Vo=0, poiché Vg = Rglg > 0 il transistore é certamente in regione normale di funzionamento.
In condizioni stazionarie ho:

     
  
 
     
          
  
   
    
  
  
 
 
   
   
  
     

  

 

Voo = Var + Ralp Q)

  

La tensione Vy del transistore si calcola facilmente come:

  

Srolp

Ves = Vin in
s

 

= 0.65347 V (2)

da cui:

‘ec Yoo — Ven ~ 134.6 kQ (3)
B
Vo — Vss
= WORNss 349 (4
iy Brolp )

2. Il circuito é deseritto dalle seguenti equazioni:

ms
le = Bela = Bro(1+"B2) In )
Veo = Va-Vo= Relea —Vo (6)
Vo = Vss+Rrle (7)
ms Vas vee) 3

= ol) (0 °
Ves = Veo—Rals (9)

Ora, sostituendo le Eq. (5) e (6) in (7) ¢ (8), il sistema si riduce a:

tp — Ve
Vo. = Ves+Risro(1+ “5 —"2) tp (10)
Vi;
Brolin = Isexp (522) (il)
Ves = Veo-Rals (12)

Le Eq. (11) (12) non sono altro che le Eq. (2) e (3) del punto precedente, per cui il loro risultato
saré identico a prima, cioé Veg = 0.05347 Ve Ty = 10 pA. A questo punto non resta che risolvere
Eg. {10}, quindi:

i Vas + RiBeo (1+ Rain) Tz

= 0.1224 V (13)
=
2 1+ Bageale

8. Il eireuito ai piccoli segnali il seguente:

 


---

 

i cui parametri differenziali sono ry = Vix /Ip = 2.58 kM e Bo = Bro = 100.
i. 4. Dal circuito di cui sopra si calcola:

 

Re
Ve = eae
CO 8L( Bo + 1)I(s) + rel (s) + Tascr:
Vo = Rrfol(s) (14)
per cui otteniamo
i
hee AoRt a GoR,(1 + sCRp)
Voc SLB +1) +1 + pete 8 ReOL(o +1) + a((Go + DL + CRarm) + Ra + 1
(15)
5. Poiché applicare una tensione costante significa lavorare per w=0, otteniamo:
MOT Bohn _ = 145 16
ee (16)

In questo caso la variazione rispetto al punto di lavoro Veo = 2 V é pari a tec=50 mV, per cui
Vanalisi di piccolo segnale ci stima una yariazione sull'uscita pari a vo = 72.9 mv.
Pertanto Vo = Vo + vo = 72.9 mV.
