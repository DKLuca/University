---
fonte: "Esame digitale 21_01_2025.pdf"
metodo: "ocr"
da_rivedere: true
---

tricola Se
ae 21 Gennaio 2025

Prova Scritta di Elettronica Digitale

21 Gennaio 2025

Si riportino negli spazi bianchi l’espressione analitica ed il valore nu-

i transistori L=Layrn-
merico dei risultati.
Si consideri una tecnologia CMOS i cui gate devono avere tempi di salita e discesa simmetrici
e per Ja quale sono note le conducibilita intrinseche dei transistori n-MO p-MOS /%/,=60014/V? e
8=400nA/ V?, la capacita di gate del transistore a dimensionamento imo C .T5fF ed il parasitic
effort Pinv=0.75 dell’invertitore. La tensione di soglia in modulo
Vr=0.35V ¢ la tensione di alimentazione @ Vpp=1. Ve.
In riferimento a tale tecnologia si consideri un

capacita di carico a valle della
In relazione al circuito in og a it

 


---

 

7 oF, valle della linea per une transizione di
»0 di assest nenta tstt al 10% @ va 8 ea.

soli i] tempo assestall

alcoli i I

ta del NOR.

2) (Punti 3) Si «

  

salita dell’us

3) (Punti 10) Si proponga una modifica del cireuito che, senza modificare la capacité di ingresso, riesca.
a pilotare la linea in modo da minimizzarne il tempo di assestamento. Si indichi chiaramente quali
gate si intendono aggiungere, in quale punto del circuito e si determinino i dimensionamenti dei
gate. Si calcoli inoltre il ritardo complessivo del circnito dagli ingressi all’uscita della linea.

 


---

www.uniue

Soluzione della Prova Scritta di Elettronica Digitale
21 Gennaio 2025

1) La impedenza caratteristica della linea & z=/1/ce=200N ed il tempo di volo vale t1=LenVic=210ps.
La resistenza equivalente del gate NOR per la transizione di salita pud essere calcolata come

2F(Vro/Vpp)

Rio =
Be TSA RELY DB

= 5152

dove si ¢ tenuto conto del fatto che la resistenza equivalente del driver ai fini del pilotaggio della linea vale

(Riz/2.3), indicando con Ryp la resistenza equivalente per il metodo del logical effort. Il coefficiente di
riflessione alla sorgente vale quindi
Rhor — 2
= Rnor =% _ 0.441
Rnor — 20

mentre la tensione che il gate NOR riesce ad iniettare in linea alla commutazione di salita vale:

Ps

Vio = ] Vpp ~ 0.419V

z
Rnor + 20
mentre il coefficiente di riflessione al carico vale pL@l.

2)L’analisi al punto precedente indica che il gate NOR é poco conduttivo per il pilotaggio di una linea con
29=2002. Infatti, il gate riesce ad iniettare in linea solo una piccola frazione di Vpp alla commutazione

di salita, ed inoltre produce un coefficiente di riflessione alla sorgente grande in modulo e positivo, che si
traduce in ampie riflessioni alla sorgente.

La tensione al carico agli istanti t=ty + 2nty; (con n=0, 1, 2,3---) pud essere espressa come

Vi (ty) = (1+ pc) Vso = 0.838V Vi (3tp) = Ve (ty) + (1 + pr)prpsVso ~ 1.21V
Vi(Sty1) = Vi.(3t) + (1 + p2)(pxps)?Vs0 ~1.37V Ve (7ty2) = Vel5tp) + (1+ p2)(pnps)®Ven ~1.44V

La tensione Vz; @ una funzione monotona crescente del tempo € possiamo quindi calcolare il tempo di
assestamento f,,; come I’stante che corrisponde ad una tensione Vz, maggiore di 0.9Vpp=1.35 V. Abbiamo
pertanto t.=5t,=1.05 ns.

3) Per pilotare la linea in modo da minimizzare il tempo di assestamente ts & opportuno pilotarla con
un invertitore (che chiameremo B1) dimensionato affinché abbia una resistenza equivalente paria z. A

tal fine imponiamo s
2F(Vro/Vop) _ is

2.3- Sm 8iVpp
dove Sp; @ il dimensionamento del transistore n-MOS dell’invertitore B1. Dalla precedente relazione
otteniamo Sg;=10.3. Prendiamo come valore intero $g;=10 a cui corrisponde una capacita di ingresso
Cmi=18.78. Ja etme e sate

Nel nuovo circuito il tempo di assestamento della linea é pari a ty, ed il ritardo complessivo risulta
pari al ritardo con cui il NOR pilota l’invertitore, piti un tempo di volo. Otteniamo quindi

Ra=

ty = bo (Gnor Ca1/Cnor + Pnor) + th

I parametri del gate NOR sono

 

Jnor =

=2.2  pnor = Spiny = 2.25 — Chor = (1+ 32)SpnorCan = 16.5fF

ed il ritardo caratteristico della tecnologia pari & pari a tp=(RinviCine1)=10.81ps, con

2F(Vro/Vpp)

Rinw = 2.3 Sp18;,Vpp

=4.74kKEQ Ci = (1+ €)Can = L875 fF -

Sostiruendo i valori numerici ottteniamo (,~252 ps.
