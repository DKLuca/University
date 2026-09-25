---
fonte: "testo_25_settembre.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Prova scritta di Fondamenti di Elettronica
                                                    25 settembre 2012
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
    Si consideri la porta logica in figura con C L =30fF, trascurando l’effetto del self-loading.
                                                                            Vdd

                                                             B              C

                                                                    A
                                                                                                      CL
                                                                            B
                                                              A
                                                                            C

     Si risponda ai seguenti quesiti:

    1. si determini la funzione logica implementata.

    2. Si assuma che tutti gli nMOS abbiano un dimensionamento S n =1 e tutti i pMOS un dimension-
       amente Sp =2; si determini il tempo di salita (o di discesa, a seconda dei casi) per ogni possibile
       configurazione degli ingressi.

    3. Si calcoli la potenza dinamica dissipata dal circuito quando funziona ad una frequenza di clock
       fc =500MHz assumendo che i tre ingressi siano statisticamente indipendenti ed abbiano probabilità
       di essere ad uno pari a PA = PB = PC =0.5.

    4. Si implementi la stessa funzione logica con un circuito dinamico di tipo ”domino”.

    5. Con riferimento al circuito domino di cui al punto precedente, assumendo che tutti i transistori
       (sia del blocco φn che dell’invertitore) abbiano Sn =1 e Sp =2 si determini la potenza dinamica
       dissipata quando si lavora ad una frequenza di clock f c =500MHz, assumendo che i tre ingressi siano
       statisticamente indipendenti ed abbiano probabilità di essere ad uno pari a P A = PB = PC =0.5;
       nel calcolo si includa sia l’energia per caricare C L che quella per caricare la capacitá d’ingresso
       dell’invertitore (anche in questo caso si trascuri il self-loading).
