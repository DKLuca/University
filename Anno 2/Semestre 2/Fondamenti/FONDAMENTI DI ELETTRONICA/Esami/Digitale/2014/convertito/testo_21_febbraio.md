---
fonte: "testo_21_febbraio.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Prova scritta di Fondamenti di Elettronica
                                                     21 febbraio 2014
                                                       parte digitale
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . = . . . . . . . . .

     Sia VDD =2.5V e si assumano i seguenti parametri tecnologici per i MOSFET:

                                                    Parametro             n-MOSFET               p-MOSFET
                                                      VT O [V]                 0.5                    -0.5
                                                    β ′ [µA/V2 ]               300                    100
                                                      γ[V1/2 ]                 0.0                    0.0
                                                      λ [V−1 ]                 0.0                    0.0
                                                    LM IN [µm]                0.35                   0.35
                                                         Cox              10 [fF/µm2 ]           10 [fF/µm2 ]
                                                         CGS0             1.0 [fF/µm]            1.0 [fF/µm]

Si assuma per tutti i transistori L=LM IN e nel calcolo dei transitori si consideri la transizione
completata al 90% della escursione totale del segnale.
    Si consideri un buffer composto da una catena di 5 invertitori, il primo dei quali ad area minima, che
pilota una capacitá CL =1pF. Gli invertitori sono dimensionati in modo che il tempo di salita sia uguale
al tempo di discesa.
    Si risponda ai seguenti quesiti:

    1. (6 punti) si determini la capacitá d’ingresso Ci di un invertitote ad area minima;

    2. (6 punti) si calcoli il ritardo minimo tp0 corrispondente ad un invertitore ad area minima che pilota
       una capacitá Ci ;

    3. (9 punti) si determini il ritardo complessivo del buffer considerando che ogni invertitore sia dimen-
       sionato il doppio del precedente;

    4. (9 punti) si calcoli la potenza dinamica dissipata dal buffer nel suo complesso quando lavora ad
       una frequenza di 300MHz avendo in ingresso una sequenza casuale di bit con eguale probabilitá di
       essere ’1’ o ’0’.
