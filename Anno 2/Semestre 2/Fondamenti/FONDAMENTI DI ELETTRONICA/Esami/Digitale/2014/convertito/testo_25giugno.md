---
fonte: "testo_25giugno.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Prova scritta di Fondamenti di Elettronica

                                                      25 giugno 2014

                                                        parte digitale

Nome: . . . . . . . . . . . . . . . .. . . . .Cognome: . . . . . . . . . . . . . . . . . . . . . .Matricola: . . . . . . . . . . . .
Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . ./……….= . . . . . . . . .
Sia VDD=2V e si assumano i seguenti parametri tecnologici per i MOSFET:
 Parametro                      n-MOSFET               p-MOSFET
 VTO [V]                               0.5                  -0.5
 ’ [A/V2]                           200                    100
  [V1/2]                                0                      0
  [V-1]                                 0                      0
 LMIN [m]                           0.25                   0.25
 COX [fF/m2]                           10                     10
 CGSO [fF/m]                          1.0                    1.0


Si assuma per tutti i transistori L=LMIN e nel calcolo dei transitori si consideri la transizione
completata al 90% della escursione totale del segnale. Si trascuri il self-loading.
Si risponda ai seguenti quesiti:
    1) (6 punti) Si disegni la porta logica dinamica DOMINO che implementa la funzione logica
       F=AB+CDE.
    2) (6 punti) Si calcoli la potenza dinamica dissipata dalla porta domino di cui sopra quando pilota
       un carico di 30fF e lavora ad una frequenza di clock di 500MHz con ingressi che hanno egual
       probabilità di essere 0 e 1.
    3) (6 punti) Si calcoli il ritardo tp0 della tecnologia in tabella, ovvero il tempo di ritardo di un
       invertitore ad area minima che pilota un altro invertitore ad area minima.
    4) (6 punti) Si consideri un buffer formato da una catena di 5 invertitori di cui il primo è ad area
       minima e gli altri sono dimensionati in maniera progressiva con ogni stadio grande 3 volte il
       precedente; calcolare il tempo di ritardo complessivo quando il buffer pilota una capacità di
       1pF.
    5) (6 punti) Calcolare la dissipazione complessiva del buffer (capacità degli invertitori + carico
       finale) quando lavora con un segnale di ingresso ad onda quadra con frequenza di 500MHz.
