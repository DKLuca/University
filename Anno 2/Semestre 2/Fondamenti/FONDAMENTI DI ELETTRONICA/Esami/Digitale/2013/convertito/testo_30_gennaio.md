---
fonte: "testo_30_gennaio.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Prova scritta di Fondamenti di Elettronica
                                                      30 gennaio 2013
                                                       parte digitale
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . = . . . . . . . . .

     Sia VDD =2V e si assumano i seguenti parametri tecnologici per i MOSFET:

                                                     Parametro            n-MOSFET               p-MOSFET
                                                       VT O [V]                0.5                    -0.5
                                                     β 0 [µA/V2 ]              300                    150
                                                       γ[V1/2 ]                0.0                     0.0
                                                       λ [V−1 ]                0.0                     0.0
                                                     LM IN [µm]               0.15                   0.15
                                                          Cox             8 [fF/µm2 ]            8 [fF/µm2 ]
                                                          CGS0            1.0 [fF/µm]            1.0 [fF/µm]

Si assuma per tutti i transistori L=L M IN e nel calcolo dei transitori si consideri la transizione
completata al 90% della escursione totale del segnale.

                                                                                               VDD
                                   A
                                   A
                                              Pass−Trans.
                                  C          Complementari
                                                                                                                      CL
                                  C


                                                                                                           R eq

                                                                                        Ceq                                    C eq


   Si consideri una porta logica statica a pass-transistor del tipo indicato in figura, che piloti un carico
puramente capacitivo CL =30fF, trascurando l’effetto del self-loading.
   Si risponda ai seguenti quesiti:

    1. (10 punti) si disegni lo schema della rete di pass-transistors che implementa la funzione NOR a 3
       ingressi;

    2. (10 punti) assumendo che i pass-transitors possano essere schematizzati con un modello a pi-greco
       come in figura, dove Ceq =1fF e Req =2kΩ (quando il pass-transitor conduce, altrimenti la R eq é
       sostituita da un circuito aperto), si determini il dimensionamento dell’invertitore che minimizza il
       ritardo di propagazione di caso peggiore dell’intera porta (pass-transistors + invertitore); nel di-
       mensionamento dell’invertitore si dimensioni il pMOS in modo che il tempo di salita dell’invertitore
       sia uguale al suo tempo di discesa;

    3. (10 punti) si calcoli il ritardo complessivo della porta per ogni possibile configurazione degli ingressi.
