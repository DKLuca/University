---
fonte: "testo_19_giugno.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Prova scritta di Fondamenti di Elettronica
                                                      19 giugno 2012
                                                       parte digitale
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

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
    Si consideri una porta logica statica CMOS che implementi la funzione logica F = AB + C e piloti
un carico puramente capacitivo CL =30fF, trascurando l’effetto del self-loading. Si risponda ai seguenti
quesiti:

    1. si disegnino le reti di pull-up e pull-down senza fare uso di un invertitore sull’uscita ed assumendo
       che gli ingressi A,B e C siano disponibili sia in forma vera che in forma negata;

    2. si assuma che tutti gli nMOS abbiano un dimensionamento S n e tutti i pMOS un dimensionamente
       Sp ; si dimensionino Sn ed Sp in modo da avere un tempo di salita di caso peggiore ed un tempo di
       discesa di caso peggiore pari entrambi a 300ps;

    3. si calcoli la capacitá di ingresso della porta logica;

    4. si calcoli il tempo di salita (o di discesa, a seconda della caso) per ogni possibile configurazione
       degli ingressi;

    5. si calcoli la potenza dinamica dissipata dal circuito quando funziona ad una frequenza di clock
       fc =600MHz assumendo che i tre ingressi siano statisticamente indipendenti ed abbiano probabilità
       di essere ad uno pari a PA = PB = PC =0.5.
