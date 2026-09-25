---
fonte: "testo_10_luglio.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Prova scritta di Fondamenti di Elettronica
                                                       10 luglio 2012
                                                       parte digitale
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

     Sia VDD =2V e si assumano i seguenti parametri tecnologici per i MOSFET:

                                                   Parametro             n-MOSFET                p-MOSFET
                                                     VT O [V]                 0.35                   -0.35
                                                   β 0 [µA/V2 ]               250                     150
                                                     γ[V1/2 ]                  0.0                     0.0
                                                     λ [V−1 ]                  0.0                     0.0
                                                   LM IN [µm]                 0.12                    0.12
                                                        Cox              8.0 [fF/µm2 ]           8.0 [fF/µm2 ]
                                                        CGS0             1.0 [fF/µm]             1.0 [fF/µm]

Si assuma per tutti i transistori L=L M IN e nel calcolo dei transitori si consideri la transizione
completata al 90% della escursione totale del segnale.
    Si consideri una porta logica statica CMOS che implementi la funzione logica F = (A + B)C e piloti
un carico puramente capacitivo CL =30fF, trascurando l’effetto del self-loading. Si risponda ai seguenti
quesiti:

    1. (6 punti) si disegnino le reti di pull-up e pull-down FACENDO uso di un invertitore sull’uscita ed
       assumendo che gli ingressi A,B e C siano disponibili solo in forma vera;

    2. (6 punti) si assuma che tutti gli nMOS della rete di pull-down abbiano un dimensionamento S n
       e tutti i pMOS della rete di pull-up un dimensionamente S p ; si indichino con Sn,inv ed Sp,inv i
       dimensionamenti del nMOS e del pMOS che compongono l’invertitore che pilota C L e che rispettano
       βn0 Sn,inv =βp0 Sp,inv ; si dimensionino quindi Sn ed Sp in modo da avere un tempo di salita di caso
       peggiore ed un tempo di discesa di caso peggiore uguali tra loro ed una capacitá vista da ciascun
       ingresso (A, B e C) pari a 1fF ;

    3. (6 punti) si trovino i valori di Sn,inv ed Sp,inv che minimizzano il ritardo di caso peggiore della porta
       (invertitore incluso), assumendo che la capacitá vista dalle reti di pull-up e pull-down sia la sola
       capacitá di ingresso dell’invertitore; si calcoli il ritardo complessivo di caso peggiore;

    4. (6 punti) si calcolino il tempo di salita e quello di discesa (non per forza uguali) nel caso migliore
       (invertitore incluso);

    5. (6 punti) si calcoli la potenza dinamica dissipata dal circuito (invertitore incluso) quando funziona ad
       una frequenza di clock fc =500MHz assumendo che i tre ingressi siano statisticamente indipendenti
       ed abbiano probabilitá di essere ’1’ pari a P A = PB = PC =0.5. Anche in questo caso si assuma
       che la capacitá vista dalle reti di pull-up e pull-down sia la sola capacitá di ingresso dell’invertitore.
