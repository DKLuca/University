---
fonte: "testo_6_febbraio.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Prova scritta di Fondamenti di Elettronica
                                                      7 febbraio 2014
                                                       parte digitale
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . = . . . . . . . . .

     Sia VDD =2.0V e si assumano i seguenti parametri tecnologici per i MOSFET:

                                                    Parametro             n-MOSFET               p-MOSFET
                                                      VT O [V]                 0.5                    -0.5
                                                    β ′ [µA/V2 ]               200                    100
                                                      γ[V1/2 ]                 0.0                    0.0
                                                      λ [V−1 ]                 0.0                    0.0
                                                    LM IN [µm]                0.25                   0.25
                                                         Cox              10 [fF/µm2 ]           10 [fF/µm2 ]
                                                         CGS0             1.0 [fF/µm]            1.0 [fF/µm]

Si assuma per tutti i transistori L=LM IN e nel calcolo dei transitori si consideri la transizione
completata al 90% della escursione totale del segnale.
    Si consideri un buffer composto da una catena di invertitori, il primo dei quali ad area minima, che
pilota una capacitá CL =1pF. Gli invertitori sono dimensionati in modo che il tempo di salita sia uguale
al tempo di discesa.
    Si risponda ai seguenti quesiti:

    1. (6 punti) si determini la capacitá d’ingresso Ci di un invertitote ad area minima;

    2. (6 punti) si calcoli il ritardo minimo tp0 corrispondente ad un invertitore ad area minima che pilota
       una capacitá Ci ;

    3. (9 punti) si determini il numero ottimo di invertitori che compongono il buffer; si noti che la teoria
       dice che ogni invertitore dovrebbe essere e volte il precedente e che questo risulta in un numero di
       stadi ottimo Nopt = ln(CL /Ci ); in questo caso peró si richiede che ogni invertitore sia 3 volte il
       precedente; questo richiede di ricavare una nuova espressione per Nopt ;

    4. (9 punti) calcolare il ritardo del buffer considerando per N i due interi piú vicini al valore ottenuto
       al punto precedente; nel caso non si sia risolto il punto precedente, usare gli interi piú vicini a
       ln(CL /Ci ).
