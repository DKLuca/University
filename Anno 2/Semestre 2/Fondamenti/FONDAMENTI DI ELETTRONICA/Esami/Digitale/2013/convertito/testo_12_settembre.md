---
fonte: "testo_12_settembre.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Prova scritta di Fondamenti di Elettronica
                                                    12 settembre 2013
                                                       parte digitale
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . = . . . . . . . . .

     Sia VDD =1.8V e si assumano i seguenti parametri tecnologici per i MOSFET:

                                                    Parametro             n-MOSFET               p-MOSFET
                                                      VT O [V]                 0.4                    -0.4
                                                    β 0 [µA/V2 ]               200                    100
                                                      γ[V1/2 ]                 0.0                     0.0
                                                      λ [V−1 ]                 0.0                     0.0
                                                    LM IN [µm]                0.15                   0.15
                                                         Cox              10 [fF/µm2 ]           10 [fF/µm2 ]
                                                         CGS0             1.0 [fF/µm]            1.0 [fF/µm]

Si assuma per tutti i transistori L=L M IN e nel calcolo dei transitori si consideri la transizione
completata al 90% della escursione totale del segnale.
    Si consideri la porta logica in figura con C L =30fF, trascurando l’effetto del self-loading.
                                               A
                                                                 B
                                  I1
                                               A
                                                                                   INV1                   INV2
                                  I2                                        O1                  O2                       F
                                               A
                                                                 B
                                  I3                                                                                            CL
                                               A

                                  I4
     Si risponda ai seguenti quesiti:

    1. (6 punti) si determini la funzione logica implementata;

    2. (6 punti) si dimensioni l’invertitore INV2 al fine di minimizzare il ritardo complessivo, sapendo che
       l’invertitore INV1 é ad area minima (ovvero, S n,inv1 =1 e Sp,inv1 = ) e che si vogliono i tempi di
       salita uguali a quelli di discesa;

    3. (6 punti) calcolare il tempo di ritardo complessivo, considerando per i pass-transistors lo schema
       seguente:
                                                                                                                 Rp

                                                                                                 Cp                            Cp


         con Cp =2fF e Rp = 2kΩ (quando il pass-transitor é acceso, infinita altrimenti);

    4. (6 punti) si determinino la minima e massima tensione che si raggiunge al nodo O1;

    5. (6 punti) si calcoli la potenza dinamica dissipata dalla porta (considerando solo l’energia richiesta
       per caricare CL ) assumendo un frequenza di clock di 300MHz ed ingressi con uguale probabilitá di
       essere 1 o 0.
