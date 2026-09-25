---
fonte: "testo_17settembre.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Prova scritta di Fondamenti di Elettronica

                                        17 settembre 2014 parte digitale

Nome: . . . . . . . . . . . . . . . .. . . . .Cognome: . . . . . . . . . . . . . . . . . . . . . .Matricola: . . . . . . . . . . . .
Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . ../ . . . . . . /. . . . . . . = . . . . . . . . .
Sia VDD=2V e si assumano i seguenti parametri tecnologici per i MOSFET:
 Parametro                        n-MOSFET               p-MOSFET
 VTO [V]                                 0.5                  -0.5
 ’ [A/V2]                             200                    100
  [V1/2]                                  0                      0
  [V-1]                                   0                      0
 LMIN [m]                             0.25                   0.25
 COX [fF/m2]                             10                     10
 CGSO [fF/m]                            1.0                    1.0


Si assuma per tutti i transistori L=LMIN e nel calcolo dei transitori si consideri la transizione
completata al 90% della escursione totale del segnale. Si trascuri il self-loading.




Con riferimento allo schema riportato sopra, in cui tutti i gate sono implementati in logica CMOS
statica, si risponda ai seguenti quesiti:
     1) (3 punti) Si indichi la funzione logica F(A,B,C,D).
     2) (3 punti) Assumendo che gli nMOS delle porte NAND siano ad area minima, si dimensionino
        i transistori pMOS delle porte NAND al fine di avere tempo di salita e di discesa di caso
        peggiore (delle sole porte NAND) uguali. Determinare la capacità di ingresso.
     3) (6 punti) Si dimensionino i transistori nMOS e pMOS della porta NOR al fine di minimizzare
        il ritardo complessivo di caso peggiore, avendo al contempo uguali tempo di salita e di discesa
        di caso peggiore. Si noti che le capacità CX sono le capacità di ingresso della porta NOR, che
        costituiscono l’unico carico visto dalle porte NAND. CL=100fF.
     4) (6 punti) Calcolare il tempo di ritardo complessivo di caso peggiore.
     5) (6 punti) Si calcoli la potenza dissipata sulla capacità CL e sulle capacità CX assumendo di
        lavorare con una frequenza di clock di 500MHz con gli ingressi A, B, C e D che hanno eguale
        probabilità di essere ‘1’ o ‘0’ (cioè PA=PB=PC=PD=0.5).
     6) (6 punti) Implementare lo stesso schema (a 2 stadi) usando una logica dinamica di tipo np-
        CMOS (detta anche NORA).
