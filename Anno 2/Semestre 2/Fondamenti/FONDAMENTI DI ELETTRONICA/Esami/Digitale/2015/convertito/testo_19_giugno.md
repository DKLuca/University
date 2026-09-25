---
fonte: "testo_19_giugno.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Prova scritta di Fondamenti di Elettronica

                                            19 giugno 2015 parte digitale

Nome: . . . . . . . . . . . . . . . .. . . . .Cognome: . . . . . . . . . . . . . . . . . . . . . .Matricola: . . . . . . . . . . . .
Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . ../ . . . . . ./ . . . . .= . . . . . . . . .
Sia VDD=1.8V e si assumano i seguenti parametri tecnologici per i MOSFET:
                                   Parametro                        n-MOSFET                p-MOSFET
                                   VTO [V]                                 0.4                   -0.4
                                   ’ [A/V2]                             300                     150
                                    [V1/2]                                  0                      0
                                    [V-1]                                   0                      0
                                   LMIN [m]                             0.15                    0.15
                                   COX [fF/m2]                             20                     20
                                   CGSO [fF/m]                            0.5                    0.5

Si assuma per tutti i transistori L=LMIN e nel calcolo dei transitori si consideri la transizione
completata al 90% della escursione totale del segnale. Si trascuri il self-loading. Con riferimento alla
porta logica riportate di seguito (in cui i transistori nMOS e pMOS dell’inverter sono dimensionati al
fine di avere lo stesso di salita e di discesa) ed assumendo C L=50fF,




si risponda ai seguenti quesiti:
     1) (5 punti) Determinare la funzione logica F(A,B,C).
     2) (3 punti) Assumendo che i transistori nMOS della rete di pull-down della porta a monte
        abbiano Sn=1, determinare Sp per i pMOS della rete di pull-up al fine di avere lo stesso tempo
        di salita e di discesa di caso peggiore.
     3) (3 punti) Determinare la capacità d’ingresso della porta.
     4) (7 punti) Dimensionare i transistori dell’invertitore al fine di minimizzare il ritardo
        complessivo della porta.
     5) (6 punti) Calcolare il tempo di ritardo complessivo per ogni configurazione degli ingressi.
     6) (6 punti) Calcolare la potenza dinamica dissipata dalla porta quando lavora ad una frequenza
        di 500MHz assumendo che gli ingressi A, B e C abbiamo tutti una probabilità del 50% di
        essere a ‘1’.
