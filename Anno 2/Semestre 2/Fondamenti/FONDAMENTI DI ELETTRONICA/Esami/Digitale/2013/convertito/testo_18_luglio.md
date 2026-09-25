---
fonte: "testo_18_luglio.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Prova scritta di Fondamenti di Elettronica
                                                       18 luglio 2013
                                                       parte digitale
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . = . . . . . . . . .

     Sia VDD =2V e si assumano i seguenti parametri tecnologici per i MOSFET:

                                                  Parametro             n-MOSFET                    p-MOSFET
                                                    VT O [V]                 0.5                         -0.5
                                                  β 0 [µA/V2 ]               200                         100
                                                    γ[V1/2 ]                 0.0                          0.0
                                                    λ [V−1 ]                 0.0                          0.0
                                                  LM IN [µm]                0.15                        0.15
                                                       Cox             10.0 [fF/µm2 ]              10.0 [fF/µm2 ]
                                                       CGS0             1.0 [fF/µm]                 1.0 [fF/µm]

Si assuma per tutti i transistori L=L M IN e nel calcolo dei transitori si consideri la transizione
completata al 90% della escursione totale del segnale.
    Si consideri la porta logica dinamica DOMINO in figura con C L =30fF e si trascuri l’effetto del self-
loading (ovvero, ogni stadio vede come carico solo la capacitá di ingresso dello stadio a valle).
                                                                         Vdd


                                                            ck                               inv

                                                                                                                     F


                                                  A                                                                CL
                                                   A
                                                  B                     PD
                                                    B
                                                  C
                                                    C


                                                              ck




     Si risponda ai seguenti quesiti:

    1. (5 punti) si disegni la rete di pull-down per implementare la funzione F = AB+BC+AC, assumendo
       che gli ingressi A,B e C siano disponibili sia in forma vera che negata;

    2. (5 punti) si assuma un dimensionamento unitario per tutti gli nMOS e i pMOS del gate dinamico
       (transitori di clock + rete di PD) e si calcoli la capacitá vista dagli ingressi;

    3. (5 punti) si determini il dimensionamento S n,inv e Sp,inv del nMOS e del pMOS che compongono
       l’invertitore che pilota CL (che rispettano βn0 Sn,inv =βp0 Sp,inv ) al fine di minimizzare il ritardo com-
       plessivo di caso peggiore della porta nel suo complesso (gate dinamico + invertitore);

    4. (5 punti) si calcoli il tempo di ritardo complessivo (gate dinamico + invertitore) per ogni configu-
       razione degli ingressi che attiva il PD in fase di valutazione;

    5. (5 punti) si calcoli la durata della fase di precarica;

    6. (5 punti) si determini la potenza dissipata dal circuito quando la frequenza di clock é di 500MHz;
       si assuma che gli ingressi siano incorrelati tra loro ed abbiano uguale probabilitá di essere ’0’ o ’1’.
