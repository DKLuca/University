---
fonte: "analogica_con_soluz_18_07_2024.pdf"
metodo: "ocr"
da_rivedere: true
---

oe scritta di Fondamenti di Elettronica
18 luglio 2024

METI OORHOMG! firvsssisivessosvevesiviers MabtCola: voice.

 


---

   
 
 
 
     
  
 
   
     
  
   
   
 
  
  
 
  
  
  
  
 
 

Soluzione del compito di Fondamenti di Elettonica
18 luglio 2024

1. Il cireuito é simmetrico ed inoltre, visto che Ving = 0, i due rami sono polarizzati esattamente
con le stesse tensioni. Per questo motivo le tensioni nei due transistori sono uguali (incluse quelle
di source), inducendo una corrente nulla su Rg. A questo punto, la corrente che scorre nei due
transistor 6 la stessa e vale Ig = 1 mA. Questo permette di ottenere le tensioni di drain che
valgono Vp; = Vp2 = Vou = Vop — Rito = 0 V. Tali tensioni inducono il funzionamento in
regime di saturazione di entrambi i MOSFET. Per cui, dalla corrente Io, possiamo calcolare anche
le tensioni Vos, = Vese = Vr + / Ht = 1.707 V. A questo punto le tensioni di source valgono

Vsi = Vso = —Vesi = —1.707 V.

tw

I due MOSFET sono uguali e polarizzati con le stesse tensioni/correnti in regime di saturazione.
Inoltre non c’ effetto di modulazione di canale per cui l’unico parametro differenziale da calcolare

€ 9m = 9m1 = Jm2 = BLM (Vesr — Vr) = 2.8 mS.
Il circuito equivalente ai piccoli segnali, opportunamente ridisegnato per evidenziare che esso 6 un
tripolo, é il seguente:

gm vgs2

 

. Rs .
vin vgsl vs vs2 > <— iout
Sin | WW | <— yout
vgs2 RL
gm vegsl Cs

 

t

3. Dal circuito si nota che la corrente di ingresso é sempre nulla, per cui otteniamo immediatamente
che:

 

 

mis) = Fe) =o (1
— Jin(s) a
yia(s) = Vout (8) gon (2)

 

Inoltre la corrente del generatore gmVgs1(s) scorre sul parallelo C's||Rs ed é uguale ed opposta
alla corrente del generatore gmV s2(s). Detto cid, si pud scrivere il seguente set di equazioni che
descrivono le tensioni nel circuito:

9mVos1 = gmn(Vin- Vs1) — —GmVos2 = 9mVs2 (3)
Vs. = Vin — Vs2 (4)
* Rs a)
Vs1 = Von — OmVoua* ge = Vea (1+ Se (5)
= Inks
Vin = Veo (2+ ors) (6)

A questo punto possiamo trovare facilmente le altre due componenti della matrice Y visto che
2 o imponiamo Vout = 0 allora out = 9mVgs2 = —9mVs2, mentre quando imponiamo Vj, = 0 da

Eq.(6) otteniamo che anche Vs = 0. Per cui:

    

 

—gm _____ 9m(1 + sCsRs)
2+ 9mRs +s: 2CsRs

 

  


---

Tous (8) 1
ra) = TS Dligeo™ Ra ©)

4. Il guadagno di tensione si calcola facilmente come:

— Vout(s) _ _ yar _ gmRi(1+sCsRs) _ gmRy_ __1+8CsRs
Av(s)= Fi (8) ~~ ym 2+9mRe ts: 20sRs  2+GmRa 149. Peake (9)

5. Chiaramente il circuito presenta un polo e uno zero i cui valori di frequenza valgono:

fp 1 2+ 9mRs

We
fe = 35° Gopg = 15:92 MHz (11)

Si tratta quindi di un circuito passa-alto i] cui guadagno a bassa frequenza vale Ay (0) = pet =

1.76, mentre i] guadagno ad alta frequenza é Ay (oo) = om Ry, = 4.24. Per cui il diagramma di Bode
del modulo di Ay é il seguente:

4

\Avi
