---
fonte: "testo_13_febbraio.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Prova scritta di Fondamenti di Elettronica
                                                     13 febbraio 2013
                                                       parte digitale
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . /. . . . . . = . . . . . . . . .

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
                                               φ                                               VDD
                                                                  M2


                                               A                                                                        F
                                               A            PD                                                    CL
                                                                                    C inv
                                               B
                                               B

                                                   φ              M1



    Si consideri la logica dinamica DOMINO in figura, che pilota un carico puramente capacitivo C L =30fF,
trascurando l’effetto del self-loading. Si risponda ai seguenti quesiti:

    1. (6 punti) si disegni lo schema della rete di pull-down per implementare la funzione EX-OR tra A e
       B sull’uscita F;

    2. (6 punti) assumendo che i transistori M1, M2 e la rete di pull-down siano tutti a dimensionamento
       minimo, si determini il dimensionamento dell’invertitore che minimizza il ritardo di propagazione
       di caso peggiore dell’intera porta (invertitore compreso); nel dimensionamento dell’invertitore si
       dimensioni il pMOS in modo che il tempo di salita dell’invertitore sia uguale al suo tempo di
       discesa;

    3. (6 punti) si calcoli il ritardo complessivo della porta, per ogni possibile configurazione degli ingressi,
       nella fase di valutazione;

    4. (6 punti) si determini la durata della fase di precarica;

    5. (6 punti) si determini la potenza dinamica dissipata dalla porta (nel suo complesso) quando la
       frequenza di clock vale 500MHz, assumendo che gli ingressi A e B siano mutuamente incorrelati e
       con probabilitá del 50% di essere ’1’.
