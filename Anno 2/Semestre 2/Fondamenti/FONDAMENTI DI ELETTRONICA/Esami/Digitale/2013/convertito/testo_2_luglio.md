---
fonte: "testo_2_luglio.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Prova scritta di Fondamenti di Elettronica
                                                       2 luglio 2013
                                                       parte digitale
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . = . . . . . . . . .

     Sia VDD =2V e si assumano i seguenti parametri tecnologici per i MOSFET:

                                                  Parametro             n-MOSFET                  p-MOSFET
                                                    VT O [V]                 0.5                       -0.5
                                                  β 0 [µA/V2 ]               200                       100
                                                    γ[V1/2 ]                 0.0                        0.0
                                                    λ [V−1 ]                 0.0                        0.0
                                                  LM IN [µm]                0.15                      0.15
                                                       Cox             10.0 [fF/µm2 ]            10.0 [fF/µm2 ]
                                                       CGS0             1.0 [fF/µm]               1.0 [fF/µm]

Si assuma per tutti i transistori L=L M IN e nel calcolo dei transitori si consideri la transizione
completata al 90% della escursione totale del segnale.
    Si consideri la porta logica statica CMOS in figura con C L =30fF e si trascuri l’effetto del self-loading
(ovvero, ogni stadio vede come carico solo la capacitá di ingresso dello stadio a valle).

                                                                Vdd

                                 A
                                  A
                                 B
                                   B                     PU
                                 C                                                 inv1                     inv2
                                   C
                                                                                                                                F

                                                                                                                                    CL
                                 A
                                  A
                                 B                         PD
                                   B
                                 C
                                   C




     Si risponda ai seguenti quesiti:

    1. (6 punti) si disegnino le reti di pull-up e pull-down per implementare la funzione F = AB+BC +AC,
       assumendo che gli ingressi A,B e C siano disponibili sia in forma vera che negata;

    2. (9 punti) si assuma che tutti gli nMOS della rete di pull-down abbiano un dimensionamento S n e
       tutti i pMOS della rete di pull-up un dimensionamente S p ; si dimensionino Sn ed Sp al fine di avere
       una capacitá di ingresso minore di 3fF avendo tempi di carica e scarica di caso peggiore uguali tra
       loro;

    3. (6 punti) si determinino Sn,inv2 ed Sp,inv2 (i dimensionamenti del nMOS e del pMOS che com-
       pongono l’invertitore 2 che pilota C L e che rispettano βn0 Sn,inv =βp0 Sp,inv ) al fine di minimizzare il
       ritardo complessivo dei due invertitori in cascata; l’invertitore 1 é ad area minima, cioé S n,inv1 =1
       e Sp,inv1 = βn0 /βp0 ;

    4. (9 punti) si calcolino il tempo di salita (o di discesa) del circuito complessivo (la porta logica + i
       due invertitori) per ciascuna configurazione degli ingressi.
