---
fonte: "Circuiti_digitale.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       1
                                                                           ELETTRONICI
                                                                              FREQUENCIES


                            Metodologia del Logical Effort
❑ Data una funzione logica i chip designer si devono chiedere quale sia la miglior topologia del circuito →
  qui ci occuperemo solamente di gate logici realizzati in tecnologia CMOS
❑ Scelta la topologia bisogna dimensionare i transistori (che dimensioni fisiche devono avere? Transistori
  con area molto grande avranno correnti di output grandi ma anche capacità di ingresso grandi!)

❑ Come possiamo minimizzare il
  ritardo di un segnale che attraversa
  i gate logici?




                                                                                                           1




                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       2
                                                                           ELETTRONICI
                                                                              FREQUENCIES


                            Metodologia del Logical Effort
  → La metodologia del Logical Effort consente di dare una prima risposta a queste domande in modo
    sistematico attraverso dei modelli algebrici relativamente semplici e compatti
  → É un buon punto di partenza per valutare differenti tipi di chip design evitando approcci molto dispendiosi in
    termini di tempo e risorse




                                                                                                           2
                          CIRCUITI
                     ELECTRONIC    E SISTEMI
                                CICUITS FOR HIGH       3
                                              ELETTRONICI
                                                 FREQUENCIES


             Invertitore CMOS
    ❑ Assumeremo caratteristiche statiche simmetriche (per massimizzare i
      margini di rumore)




                 ▪ Per massimizzare NMH voglio VIHmin piccolo
                 ▪ Per massimizzare NML voglio VILmax grande

                                      → VLT=VDD/2                  3




                          CIRCUITI
                     ELECTRONIC    E SISTEMI
                                CICUITS FOR HIGH       4
                                              ELETTRONICI
                                                 FREQUENCIES




Dobbiamo determinare le condizioni che portano a VLT=VDD/2         4
                                                                                CIRCUITI
                                                                           ELECTRONIC    E SISTEMI
                                                                                      CICUITS FOR HIGH       5
                                                                                                    ELETTRONICI
                                                                                                       FREQUENCIES


                                                         𝑉 = 𝑉𝑇𝑝 = 𝑉𝑇
❑ Affinché VLT=VDD/2 dobbiamo avere                     ൝ 𝑇𝑛
                                                             𝛽𝑛 = 𝛽𝑝

DIMOSTRAZIONE




                                                                                                                                                                          5




                                                                                CIRCUITI
                                                                           ELECTRONIC    E SISTEMI
                                                                                      CICUITS FOR HIGH       6
                                                                                                    ELETTRONICI
                                                                                                       FREQUENCIES
                        conducibilità intrinseca

                             𝑊 ′
❑ sappiamo che 𝛽𝑛 =           𝛽             con             𝛽𝑛′ = 𝜇𝑛 𝐶𝑜𝑥
                             𝐿 𝑛
           dimensionamento   𝑆𝑛




                                                                                                                                         [ J.A del Alamo, Nature, vol 479, p.317, 2011]
                                                       TEM image                   TEM image




                                          [Sangya D. et al., Scientific Reports,   [B. Mereu et al., Appl. Phys. A 80, 253–257 (2005)]                                    6
                                          vol.7, n°8257 (2017) ]
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       7
                                                                             ELETTRONICI
                                                                                FREQUENCIES


                 Capacità di ingresso di un invertitore CMOS
                allora                         𝑆𝑝 𝛽𝑛′
   se 𝛽𝑛 = 𝛽𝑝            𝑆𝑛 𝛽𝑛′ = 𝑆𝑝 𝛽𝑝′   →     =
                                               𝑆𝑛 𝛽𝑝′

                                dimensionamento         𝜀
                                relativo 𝛼
                                La capacità di ingresso CINV
                                dell’inverter CMOS sarà data dalla
                                somma delle capacità di gate, date da:

                                ❑ capacità intrinseche di canale
                                ❑ capacità parassite


                                               𝐶𝐺𝐴𝑇𝐸 ≅ 𝑊𝐿𝐶𝑂𝑋 + 𝑊𝐶𝐺𝑆0 +𝑊𝐶𝐺𝐷0

                                                                         2𝑊𝐶𝐺𝑆0
                                                                                              7




                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       8
                                                                             ELETTRONICI
                                                                                FREQUENCIES

Dunque:    𝐶𝐼𝑁𝑉 ≅ 𝐶𝑝𝑀𝑂𝑆 + 𝐶𝑛𝑀𝑂𝑆

                   ≅ 𝑆𝑛 1 + 𝛼 𝐶𝑀1

DIMOSTRAZIONE




                                                                                              8
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       9
                                                                             ELETTRONICI
                                                                                FREQUENCIES


Calcoliamo il tempo di commutazione dell’invertitore definito come:
tempo necessario affinché a fronte di una commutazione istantanea della tensione di ingresso (da 0V a VDD, o
viceversa), il nodo di uscita compia un’escursione del 90%.
Assumiamo anche che:
❑ Il carico sia un condensatore a capacità costante
❑ Per semplificare i calcoli trascuriamo la modulazione di IDS (di saturazione) da VDS (λ=0)



                       𝑡𝑟 =tempo di salita: affinché l’uscita passi da tensione di 0V al valore VOHmin=0.9VDD

                                           𝑉𝑂𝐻𝑚𝑖𝑛 −𝑉𝐷𝐷
                                                         𝑑𝑉𝐷𝑆
                                𝑡𝑟 = 𝐶𝐿         න
                                                         𝐼𝑝𝑀𝑂𝑆
                                             −𝑉𝐷𝐷

                                                𝑉𝑇
                                           2𝐹
                                               𝑉𝐷𝐷
                                    = 𝐶𝐿
                                            𝛽𝑝 𝑉𝐷𝐷

                                                                                                          9




                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       10
                                                                             ELETTRONICI
                                                                                FREQUENCIES



                                       𝑡𝑟 + 𝑡𝑓       1  1   1    𝑉𝑇
                                𝑡𝑝 =           = 𝐶𝐿       +   𝐹
                                          2         𝑉𝐷𝐷 𝛽𝑛 𝛽𝑝   𝑉𝐷𝐷



          Definiamo la resistenza efficacie dell’invertitore come:
                           1  1   1    𝑉𝑇
                𝑅𝐼𝑁𝑉 =          +   𝐹                        Dipende da parametri tecnologici e dimensionamenti:
                          𝑉𝐷𝐷 𝛽𝑛 𝛽𝑝   𝑉𝐷𝐷                    ❑ conducibilità intrinseca 𝛽𝑛′
                                                             ❑ tensione di soglia 𝑉𝑇
                           1   2       𝑉𝑇                    ❑ tensione di alimentazione 𝑉𝐷𝐷
                      =        ′    𝐹
                          𝑉𝐷𝐷 𝛽𝑛 𝑆𝑛   𝑉𝐷𝐷                    ❑ dimensionamenti 𝑆𝑛 , 𝑆𝑝
                                                             ❑ come definiamo estinzione transitorio




                                                                                                         10
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       11
                                                                             ELETTRONICI
                                                                                FREQUENCIES

CALCOLO DEL TEMPO DI PROPAGAZIONE INVERTER CMOS




                                                                                                             11




                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       12
                                                                             ELETTRONICI
                                                                                FREQUENCIES

dunque       𝑡𝑝 = 𝑅𝐼𝑁𝑉 𝐶𝐿

                               𝐶𝐿
                = 𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉
                              𝐶𝐼𝑁𝑉

                 è un parametro tecnologico che non dipende
                 dal dimensionamento assoluto S ma solo da
                 quello relativo α

                                                               𝐶𝐿
                                                 𝑡𝑝 = 𝑡𝑝0
                                                              𝐶𝐼𝑁𝑉

 𝑡𝑝0 è un tempo caratteristico della tecnologia (dipende da 𝛽𝑛′ , 𝑉𝑇 , 𝑉𝐷𝐷 , da come definisco l’esaurimento di un
 transitorio) e corrisponde al ritardo di un invertitore che ha 𝐶𝐿 = 𝐶𝐼𝑁𝑉 assumendo trascurabili la capacità parassite
 del transistore stesso viste ad nodo di uscita


 Il ritardo è stato quindi separato in:
 ❑ Un termine tecnologico 𝑡𝑝0
 ❑ Un termine che dipende dal dimensionamento attraverso 𝐶𝐼𝑁𝑉
                                                                                                             12
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       13
                                                                           ELETTRONICI
                                                                              FREQUENCIES


Nella metodologia del Logical Effort, i ritardi da considerare sono quelli di caso peggiore, inoltre si suppone che
i gate siano simmetrici quindi con tempi di salita e di discesa uguali (𝑡𝑟 = 𝑡𝑓 )
                                                                                               𝑉𝑇
                                                                                                2𝐹ൗ𝑉
                                                                                                     𝐷𝐷
Per il generico gate definiamo la resistenza equivalente della rete di pull-down come: 𝑅𝑡 = ′
                                                                                           𝛽𝑛 𝑆𝑛,𝑒𝑞 𝑉𝐷𝐷



                                                                   dove ricordiamo che si suppone
                                                                              𝑆𝑛,𝑒𝑞 𝛽𝑛′ = 𝑆𝑝,𝑒𝑞 𝛽𝑝′

                                                                   per avere 𝑡𝑟 = 𝑡𝑓 (di caso peggiore) se
                                                                   𝑉𝑇𝑛 = 𝑉𝑇𝑝 = 𝑉𝑇




                                                                                                             13




                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       14
                                                                           ELETTRONICI
                                                                              FREQUENCIES


   ESEMPIO di ritardi di caso peggiore



                                                Se tutti i MOSFET hanno lo stesso dimensionamento:
                                                Il ritardo di caso peggio della rete di pull-down è quello che si
                                                ha attraverso il percorso A-B-C (e non attraverso A-D)




                                                                                                             14
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       15
                                                                              ELETTRONICI
                                                                                 FREQUENCIES


Introduciamo un po’ di simbologia:

𝐶𝑡 : capacità di ingresso del generico gate logico
𝐶𝑝𝑡 :capacità parassita al nodo di uscita prodotto dai transistori del gate che
sto considerando a causa di: capacità di giunzione 𝐶𝐷𝐵 , da
𝐶𝑂𝑈𝑇 : capacità di uscita dovuta solamente ai gate connessi a valle del gate
logico in esame (non comprende capacità di uscita del gate in esame!)




                Il generico ritardo diventa: 𝑡𝑝 = 𝑅𝑡 𝐶𝑂𝑈𝑇 + 𝑅𝑡 𝐶𝑝𝑡

                                                           𝐶𝑂𝑈𝑇
                                                = 𝑅𝑡 𝐶𝑡         + 𝑅𝑡 𝐶𝑝𝑡
                                                            𝐶𝑡

                                                            𝑅𝑡 𝐶𝑡   𝐶𝑂𝑈𝑇     𝑅𝑡 𝐶𝑝𝑡
                                                = 𝑡𝑝0                    +
                                                          𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉 𝐶𝑡     𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉
                                                                                               15




                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       16
                                                                              ELETTRONICI
                                                                                 FREQUENCIES




                                             𝑅𝑡 𝐶𝑡        𝐶𝑂𝑈𝑇         𝑅𝑡 𝐶𝑝𝑡
                               𝑡𝑝 = 𝑡𝑝0                          +
                                           𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉       𝐶𝑡        𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉

                                            LOGICAL ELECTRICAL PARASITIC
                                            EFFORT    EFFORT    EFFORT
                                               g            h            p


                                             𝑡𝑝 = 𝑡𝑝0 𝑔ℎ + 𝑝
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       17
                                                                           ELETTRONICI
                                                                              FREQUENCIES




                                          𝑡𝑝 = 𝑡𝑝0 𝑔ℎ + 𝑝
NOTE:
❑ 𝐶𝑡 è ∝ dimensionamento 𝑆𝑛,𝑒𝑞 ( o 𝑆𝑝,𝑒𝑞 )                    𝑅𝑡 𝐶𝑡 non dipende dal dimensionamento assoluto
❑ 𝑅𝑡 è ∝−1 dimensionamento 𝑆𝑛,𝑒𝑞 ( o                          Lo stesso vale per il termine 𝑅𝑡 𝐶𝑝𝑡
  𝑆𝑝,𝑒𝑞 )



 ❑ Ne deriva che logical effort (g) e parasitic effort (p) non dipendono dal dimensionamento assoluto dei
   transistori (al limite da quello relativo che consente di avere tempi di ritardo di caso peggiore di salita e
   di discesa uguali)
 ❑ L’electric effort (h) dipende dal dimensionamento attraverso 𝐶𝑡
 ❑ 𝑡𝑝0 è un ritardo di riferimento in relazione al quale possiamo definire un ritardo normalizzato del gate che
   stiamo considerando

                                                                                                          17




                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       18
                                                                           ELETTRONICI
                                                                              FREQUENCIES


                            Parasitic Effort di un invertitore
                                       𝑅𝑡 𝐶𝑝𝑡   caso di inverter        𝑅𝐼𝑁𝑉 𝐶𝑝𝐼𝑁𝑉
                                  𝑝=                               𝑝=
                                        𝑡𝑝0                                𝑡𝑝0

Calcoliamo 𝐶𝑝𝐼𝑁𝑉 → essa dipende da 𝐶𝐺𝐷 e 𝐶𝐷𝐵




                                                                                                          18
                                                  CIRCUITI
                                             ELECTRONIC    E SISTEMI
                                                        CICUITS FOR HIGH       19
                                                                      ELETTRONICI
                                                                         FREQUENCIES




                                                                      𝐶𝑒𝑞1 = 2 𝑊𝑛 𝐶𝐺𝑆0 + 𝑊𝑝 𝐶𝐺𝑆0 +
                                                                               1
                                                                             + 𝑊𝑛 𝐿𝑛 + 𝑊𝑝 𝐿𝑝 𝐶𝑜𝑥 𝑅𝐷𝐷
                                                                               2




                                                                      𝐶𝑒𝑞2 = 𝐾𝑒𝑞 𝑊𝐿𝑆 𝐶𝑗0




                                                                                                 19




                                                  CIRCUITI
                                             ELECTRONIC    E SISTEMI
                                                        CICUITS FOR HIGH       20
                                                                      ELETTRONICI
                                                                         FREQUENCIES


              𝐶𝑝𝐼𝑁𝑉 = 𝐶𝑒𝑞1 + 𝐶𝑒𝑞2,𝑛 + 𝐶𝑒𝑞2,𝑝
                                                1
                    = 2 𝑊𝑛 𝐶𝐺𝑆0 + 𝑊𝑝 𝐶𝐺𝑆0 +         𝑊𝑛 𝐿𝑛 + 𝑊𝑝 𝐿𝑝 𝐶𝑜𝑥 𝑅𝐷𝐷 + 𝐾𝑒𝑞 𝑊𝑛 + 𝑊𝑝 𝐿𝑆 𝐶𝑗0
                                                2


❑ assumendo che 𝐿𝑛 = 𝐿𝑝 = 𝐿𝑚𝑖𝑛
❑ raccogliamo 𝑊 Τ𝐿
❑ sapendo che 𝑆𝑛 = 𝑊𝑛 Τ𝐿 e 𝑆𝑝 = 𝑊𝑝 Τ𝐿
❑ e che 𝑆𝑝 = 𝛼𝑆𝑛

                                              1
               𝐶𝑝𝐼𝑁𝑉 = 𝑆𝑛 1 + 𝛼   2𝐶𝐺𝑆0 LMIN + 𝐶𝑜𝑥 𝑅𝐷𝐷 LMIN2 + 𝐾𝑒𝑞 𝐿𝑆,𝐷 𝐶𝑗0 LMIN
                                              2


                                     𝐶𝑝1 : capacità parassita prodotta al nodo
                                     di uscita dell’invertitore da transistori con
                                     dimensioni minime W=L=LMIN

                                         𝐶𝑝𝐼𝑁𝑉 = 𝑆𝑛 1 + 𝛼 𝐶𝑝1

                                                                                                 20
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       21
                                                                             ELETTRONICI
                                                                                FREQUENCIES

               ESEMPIO di calcolo di capacità di ingresso e resistenze equivalenti → Gate NAND


NOTE sui gate realizzati in tecnologia CMOS:
❑ Se l’uscita è 1(0) la rete di pull-down(pull-up) è spenta → VOL=0V e VOH=VDD
❑ In condizioni stazionarie solo la rete di pull-up (-down) è accesa/spenta (spenta/accesa) → consumo di
  potenza nulla in condizioni stazionarie
❑ Funzioni logiche sono «calcolate» sia da reti di pull-up che di pull-down → gate CMOS con fan-in N ha
  solitamente 2N MOSFETS (non sempre, si veda il caso del gate XOR)
❑ Anche se nelle reti di pull-down e pull-up ci sono transistori in serie/parallelo questo non complica lo studio
  dei valori VOL e VOH → determinati solo dallo stato di
                          accensione/spegnimento e non
                          dalla conducibilità dei MOSFET




                                                                                                             21




                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       22
                                                                             ELETTRONICI
                                                                                FREQUENCIES

               ESEMPIO di calcolo di capacità di ingresso e resistenze equivalenti → Gate NAND2

                  de Morgan                  step 1) imporre simmetria 𝑡𝑓 = 𝑡𝑟 di caso
   𝐹 𝐴, 𝐵 = 𝐴𝐵                𝐴ҧ + 𝐵ത
                                             peggiore
                                                  ricordiamo che:
                                                  ▪ se trascuriamo effetto body (𝛾 = 0)
                                                  ▪ se assumiamo conduttanza di uscita in
                                                      saturazione nulla (λ = 0)




                                                                                                               1
                                                                                                  𝑆𝑒𝑞 =
                                                                                                          1ൗ + 1ൗ
                                                                                                            𝑆1   𝑆2




                                                                              𝜀
                                                                  𝑆𝑝,𝑁𝐴𝑁𝐷 =     𝑆
                                                                              2 𝑛,𝑁𝐴𝑁𝐷
                                                                                                             22
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       23
                                                                            ELETTRONICI
                                                                               FREQUENCIES

DIMOSTRAZIONE




                                                                                                   23




                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       24
                                                                            ELETTRONICI
                                                                               FREQUENCIES

step 2) grazie al dimensionamento relativo trovato in step1), calcoliamo la capacità di ingresso

                                                                    𝜀
                                            𝐶𝑡,𝑁𝐴𝑁𝐷 = 𝑆𝑛,𝑁𝐴𝑁𝐷 1 +     𝐶
                                                                    2 𝑀1
DIMOSTRAZIONE




                                                                                                   24
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       25
                                                                           ELETTRONICI
                                                                              FREQUENCIES

step 3) calcoliamo la capacità parassita al nodo di uscita del gate NAND

                                           𝐶𝑝,𝑁𝐴𝑁𝐷 = 𝑆𝑛,𝑁𝐴𝑁𝐷 1 + 𝜀 𝐶𝑝1

DIMOSTRAZIONE




                                                                                                25




                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       26
                                                                           ELETTRONICI
                                                                              FREQUENCIES

              ESEMPIO di calcolo di capacità di ingresso e resistenze equivalenti → Gate XOR2

                                   step 1) imporre simmetria 𝑡𝑓 = 𝑡𝑟 di caso peggiore

                                                                  𝑆𝑝,𝑋𝑂𝑅 = 𝜀𝑆𝑛,𝑋𝑂𝑅



                                                       capacità di ingresso
                                                                  𝐶𝑡,𝑋𝑂𝑅 = 𝑆𝑛,𝑋𝑂𝑅 1 + 𝜀 𝐶𝑀1




                                                       capacità parassita
                                                                  𝐶𝑝,𝑋𝑂𝑅 = 2𝑆𝑛,𝑋𝑂𝑅 1 + 𝜀 𝐶𝑝1




                                                                                                26
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       27
                                                                            ELETTRONICI
                                                                               FREQUENCIES


                                           GATE in SCALA
Modello di ritardi visto fin’ora prevede che il generico gate sia caratterizzato da 3 parametri:

                                                     𝑅𝑡 , 𝐶𝑡 , 𝐶𝑝𝑡
(c’è poi 𝐶𝑂𝑈𝑇 che dipende solamente da quello che sta a valle del gate)
In questo modo si definiscono:
▪ Logical Effort g
▪ Parasitic Effort p
▪ Electrical Effort h


In presenza di una versione scalata del gate in cui tutti i dimensionamenti dei MOSFET vengono
moltiplicati per 𝐾𝑠𝑐 e si avrà:
   ▪ 𝐶𝑖𝑛 = 𝐾𝑠𝑐 𝐶𝑡
   ▪ 𝑅𝑖 = 𝑅𝑡 Τ𝐾𝑠𝑐
   ▪ 𝐶𝑝𝑖 = 𝐾𝑠𝑐 𝐶𝑝𝑡

  Inoltre 𝑡𝑝 = 𝑅𝑖 𝐶𝑜𝑢𝑡 + 𝐶𝑝𝑖
                                                                                                         27




                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       28
                                                                            ELETTRONICI
                                                                               FREQUENCIES


Cerchiamo di capire come e se il ritardo del gate scalato è legato in modo semplice al gate di riferimento




                                                                                                         28
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       29
                                                                           ELETTRONICI
                                                                              FREQUENCIES



                                            𝑡𝑝,𝐾 = 𝑡𝑝0 𝑔ℎ′ + 𝑝


Da questo risultato di deduce che, fissata una topologia di gate CMOS e definiti i vincoli che garantiscono 𝑡𝑟 = 𝑡𝑓
di caso peggiore:
❑ g e p non dipendono dai dimensionamenti assoluti → cioè se tutti i dimensionamenti sono moltiplicati per 𝐾𝑠𝑐 ,
  g e p non cambiano rispetto al caso con 𝐾𝑠𝑐 =1
❑ L’electrical effort h è inversamente proporzionale a 𝐾𝑠𝑐




                                                                                                           29




                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       30
                                                                           ELETTRONICI
                                                                              FREQUENCIES

Fissati:
❑ La topologia del gate CMOS
❑ I relativi dimensionamenti
→ si può calcolare 𝐶𝐼𝑁 e, nota 𝐶𝑂𝑈𝑇 (che dipende da eventuali gate connessi a valle/interconnessioni, dal carico
  in generale ma non dalle capacità parassite del gate stesso sul nodo di uscita) si può calcolare l’electrical
  effort h del gate (che dipende dai dimensionamenti)
A differenza di h, g rappresenta l’effetto della topologia sul ritardo del circuito e non del dimensionamento dei
transistori




                                                                                                           30
                                                            CIRCUITI
                                                       ELECTRONIC    E SISTEMI
                                                                  CICUITS FOR HIGH       1
                                                                                ELETTRONICI
                                                                                   FREQUENCIES

                                                    Summary
               𝑅𝑡 𝐶𝑡      𝐶𝑂𝑈𝑇          𝑅𝑡 𝐶𝑝𝑡        ▪ 𝑡𝑝0 è il ritardo di un inverter caricato dalla sua capacità di
 𝑡𝑝 = 𝑡𝑝0                         +
             𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉     𝐶𝑡         𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉         ingresso (senza parassiti né capacità esterne)
                                                      ▪ 𝑔 e 𝑝: fissata topologia e vincoli su dimensionamenti relativi di
                                                        nMOS e pMOS che garantiscono 𝑡𝑓 = 𝑡𝑟 (di caso peggiore) →
             LOGICAL ELECTRICAL PARASITIC               dipendono dalla tecnologia (𝛽𝑛′ , 𝑉𝑇 , 𝑉𝐷𝐷 , da come definisco
             EFFORT    EFFORT    EFFORT
                                                        l’esaurimento di un transitorio) e non dai dimensionamenti
                g           h             p             assoluti
                                                      ▪ L’electric effort (h) dipende dal dimensionamento attraverso 𝐶𝑡


              𝑡𝑝 = 𝑡𝑝0 𝑔ℎ + 𝑝

Equazione fondamentale per il metodo del logical
effort che mostra linearità del ritardo con 𝐶𝑂𝑈𝑇


                                                                                                                 1




                                                            CIRCUITI
                                                       ELECTRONIC    E SISTEMI
                                                                  CICUITS FOR HIGH       2
                                                                                ELETTRONICI
                                                                                   FREQUENCIES

                                                    Summary
  In presenza di una versione scalata del gate in cui tutti i dimensionamenti dei MOSFET vengono moltiplicati per
  𝐾𝑠𝑐 e si avrà:
    ▪ 𝐶𝑖𝑛 = 𝐾𝑠𝑐 𝐶𝑡
    ▪ 𝑅𝑖 = 𝑅𝑡 Τ𝐾𝑠𝑐
    ▪ 𝐶𝑝𝑖 = 𝐾𝑠𝑐 𝐶𝑝𝑡
                                                  𝑡𝑝,𝐾𝑠𝑐 = 𝑡𝑝0 𝑔ℎ′ + 𝑝              con ℎ′ = ℎൗ𝐾
                                                                                                   𝑠𝑐



  Da questo risultato di deduce che, fissata una topologia di gate CMOS e definiti i vincoli che garantiscono 𝑡𝑟 = 𝑡𝑓
  di caso peggiore:
  ❑ g e p non dipendono dai dimensionamenti assoluti → cioè se tutti i dimensionamenti sono moltiplicati per 𝐾𝑠𝑐 ,
    g e p non cambiano rispetto al caso con 𝐾𝑠𝑐 =1
  ❑ L’electrical effort h è inversamente proporzionale a 𝐾𝑠𝑐



                                                                                                                 2
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       3
                                                                              ELETTRONICI
                                                                                 FREQUENCIES


                                      Calcolo del logical effort g

 Dunque si può dire che:
                                          cioè g è il rapporto 𝐶𝑡 su 𝐶𝐼𝑁𝑉 se dimensiono il gate affinché abbia la
             𝐶𝑡
       𝑔=           se     𝑅𝑡 =𝑅𝐼𝑁𝑉       stessa resistenza equivalente dell’inverter di riferimento → cioè se eroga
            𝐶𝐼𝑁𝑉                          la stessa corrente di uscita dell’inverter di riferimento


 oppure:

             𝑅𝑡                           cioè g è il rapporto 𝑅𝑡 su 𝑅𝐼𝑁𝑉 se dimensiono il gate affinché abbia la
       𝑔=           se     𝐶𝑡 =𝐶𝐼𝑁𝑉       stessa capacità di ingresso dell’inverter di riferimento
            𝑅𝐼𝑁𝑉




                                       (è possibile calcolare g in entrambi i modi)
                                                                                                             3




                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       4
                                                                              ELETTRONICI
                                                                                 FREQUENCIES

ESEMPIO: Gate NAND con fan-in=«n»

metodo 1) Usiamo definizione di g che richiede di uguagliare le correnti di uscita del
gate NAND con quelle dell’invertitore di riferimento con dimensionamento 𝑆𝐼𝑁𝑉

                                                       𝐶𝑡,𝑁𝐴𝑁𝐷 𝑛 + 𝜀
                                             𝑔𝑁𝐴𝑁𝐷 =          =
                                                        𝐶𝐼𝑁𝑉    1+𝜀
DIMOSTRAZIONE




                                                                                                             4
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       5
                                                                              ELETTRONICI
                                                                                 FREQUENCIES


                                                      𝐶𝑡,𝑁𝐴𝑁𝐷 𝑛 + 𝜀
                                           𝑔𝑁𝐴𝑁𝐷 =           =
                                                       𝐶𝐼𝑁𝑉    1+𝜀

 Si nota che g-NAND:
 ❑ Non dipende da dimensionamenti assoluti → perciò neanche dal dimensionamento dell’inverter di riferimento
                                             ′
 ❑ Dipende dalla tecnologia attraverso 𝜀 = 𝛽𝑛ൗ𝛽′
                                                 𝑝

 ❑ Dal fan-in attraverso «n»




                                                                                                            5




                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       6
                                                                              ELETTRONICI
                                                                                 FREQUENCIES

ESEMPIO: Gate NAND con fan-in=«n»

 metodo 2) Usiamo definizione di g che richiede di uguagliare la capacità di ingresso del gate con quella
 dell’inverter di riferimento

                                                         𝑅𝑡   𝑛+𝜀
                                            𝑔𝑁𝐴𝑁𝐷 =         =
                                                        𝑅𝐼𝑁𝑉 1 + 𝜀
 DIMOSTRAZIONE




                                                                                                            6
                                             CIRCUITI
                                        ELECTRONIC    E SISTEMI
                                                   CICUITS FOR HIGH       7
                                                                 ELETTRONICI
                                                                    FREQUENCIES

ESEMPIO: Gate NOR con fan-in=«n»

                                             𝐶𝑡    1 + 𝑛𝜀
                                   𝑔𝑁𝑂𝑅 =        =
                                            𝐶𝐼𝑁𝑉    1+𝜀
  DIMOSTRAZIONE




                                                                                  7




                                             CIRCUITI
                                        ELECTRONIC    E SISTEMI
                                                   CICUITS FOR HIGH       8
                                                                 ELETTRONICI
                                                                    FREQUENCIES

ESEMPIO: Gate XOR a 2 ingressi

                                   𝑔𝑋𝑂𝑅 = 2

  DIMOSTRAZIONE




                                                                                  8
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       9
                                                                            ELETTRONICI
                                                                               FREQUENCIES


La capacità parassita sul nodo di uscita cresce con il numero di ingressi → parasitic effort




                                                                                                             9




                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       10
                                                                            ELETTRONICI
                                                                               FREQUENCIES


                                           Parasitic Effort p
E’ il contributo al ritardo di un gate dovuto a capacità parassita sul nodo di uscita prodotta dai transistori dello
stesso gate
Abbiamo già visto che p non dipende dai dimensionamenti assoluti dunque:
❑ tutti i gate con medesima topologia e stessi vincoli sui dimensionamenti di nMOS e pMOS hanno stesso
  valore di p

              Calcolo di p:

                          𝐶𝑝𝑡                                     𝑅𝑡
                    𝑝=           se    𝑅𝑡 =𝑅𝐼𝑁𝑉             𝑝=           se    𝐶𝑝𝑡 =𝐶𝐼𝑁𝑉
                         𝐶𝐼𝑁𝑉                                    𝑅𝐼𝑁𝑉

             In entrambi i casi dobbiamo tenere conto della capacità parassita sul nodo di uscita




                                                                                                            10
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       11
                                                                             ELETTRONICI
                                                                                FREQUENCIES

              Quali sono le capacità che contribuiscono a p?


  ❑ Capacità parassite CGDp
  ❑ Capacità di giunzione 𝐶𝐷𝐵
  ❑ Capacità di canale 𝐶𝐺𝐷𝐶 e 𝐶𝐺𝐵



  Trascureremo l’ultimo contributo (capacità di canale) ai fini di:
  ❑ Ottenere espressioni analitiche compatte
  ❑ La capacità di canale dipende dal regime di funzionamento ed è complicato, nel caso di molti gate, tenere in
    conto il loro contributo sul nodo di uscita.




                                                                                                       11




                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       12
                                                                             ELETTRONICI
                                                                                FREQUENCIES

DERIVAZIONE DI p




                                                                                                       12
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       13
                                                                              ELETTRONICI
                                                                                 FREQUENCIES


Dunque se 𝑅𝑡 =𝑅𝐼𝑁𝑉
                                                                 𝑛
                                                             σ𝑖=1
                                                               𝑝
                                                                  𝑆𝑖 𝐶𝑝1
                                                   𝑝=
                                                         𝑆𝐼𝑁𝑉 1 + 𝜀 𝐶𝑀1

 Analizziamo il caso più semplice: il calcolo di p dell’invertitore → infatti per definizione in quel caso si ha che
                                                     𝑅𝑡 =𝑅𝐼𝑁𝑉

                                   𝑆𝐼𝑁𝑉 1 + 𝜀 𝐶𝑝1   𝐶𝑝1 𝐿𝑀𝐼𝑁 2𝐶𝐺𝑆0 + 𝐿𝑆 𝐶𝑗0 𝐾𝑒𝑞
                          𝑝𝐼𝑁𝑉 =                  =    = 2
                                   𝑆𝐼𝑁𝑉 1 + 𝜀 𝐶𝑀1 𝐶𝑀1    𝐿𝑀𝐼𝑁 𝐶𝑜𝑥 + 2𝐿𝑀𝐼𝑁 𝐶𝐺𝑆0




                                                                                                                13




                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       14
                                                                              ELETTRONICI
                                                                                 FREQUENCIES


Generalizzando al caso di gate CMOS diversi dall’invertitore
                                                             𝑛
                                                          σ𝑖=1
                                                            𝑝
                                                               𝑆𝑖 𝐶𝑝1
                                           𝑝𝐺𝐴𝑇𝐸 =
                                                       𝑆𝐼𝑁𝑉 1 + 𝜀 𝐶𝑀1

                                                            𝑛
                                                            𝑝
                                                          σ𝑖=1 𝑆𝑖
                                                   =                   𝑝𝐼𝑁𝑉
                                                       𝑆𝐼𝑁𝑉 1 + 𝜀

❑ Ricordiamo che questo modello approssimato trascura le capacità intrinseche di canale




                                                                                                                14
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       15
                                                                              ELETTRONICI
                                                                                 FREQUENCIES


Calcolo del parasitic effort in NANDn




                                                                                                               15




                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       16
                                                                              ELETTRONICI
                                                                                 FREQUENCIES

𝑝𝑁𝐴𝑁𝐷 e 𝑝𝑁𝑂𝑅 aumentano linearmente con il fan-in

❑ attraverso simulazioni si vede che l’aumento è più che lineare con il fan-in
    ❑ Infatti un ruolo importante è dato anche dalle capacità parassite sui nodi interni delle reti di pull-up e pull-
       down
    ❑ In questi calcoli analitici si trascura anche il fatto che la conduzione nei transistori dipende dall’effetto body
       (per cui la tensione di soglia cambia quando 𝑉𝑆 ≠ 𝑉𝐵 )
❑ in aggiunta al punto precedente, per il calcolo del parasitic effort si dovrebbe anche tenere in considerazione
  l’ordine di commutazione dei MOSFET che costituiscono il gate:




                                                                                                               16
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       17
                                                                              ELETTRONICI
                                                                                 FREQUENCIES

Ottenere formule analitiche compatte per il parasitic effort p è complicato. C’è però da dire che la procedura di
minimizzazione del ritardo in presenza di una serie di gate non coinvolgerà il parasitic effort dei gate




                                                                                                                17




                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       18
                                                                              ELETTRONICI
                                                                                 FREQUENCIES

  Ricapitolando:
  ❑ Il dimensionamento relativo degli nMOS e pMOS (𝛼) viene fissato dalla condizione di tempi di salita e discesa
    uguali di caso peggiore


  ❑ La topologia del gate (tipo di gate logico, fan-in, …) e il dimensionamento relativo 𝛼 determinano il valore di
     ❑ logical effort g
     ❑ parasitic effort p


  ❑ L‘ottimizzazione dei ritardi che seguirà è legata alle transizioni di caso peggiore da cui derivano le espressioni
    per i dimensionamenti relativi, le espressioni di g, h e p.
      ❑ Se c’è un percorso di segnale nel quale il gate ha una transizione che non è quella di caso peggiore, non
          possiamo usare i parametri del logical effort calcolati nell’ipotesi di transizioni di salita e discesa di caso
          peggiore




                                                                                                                18
                                                           CIRCUITI
                                                      ELECTRONIC    E SISTEMI
                                                                 CICUITS FOR HIGH       19
                                                                               ELETTRONICI
                                                                                  FREQUENCIES

                                Ritardo di due gate in cascata
              Gate 1                  Gate 2
                                                                          ❑ obiettivo: minimizzare il ritardo
                                                                          ❑ Assumiamo note le topologie dei gate
                                                                            → 𝑔1 e 𝑔2 note
                                                                          ❑ Assumiamo che il primo stadio sia a
                                                                            dimensionamento fissato
                                                                            → 𝐶𝐼𝑁1 ( e 𝑆𝑛1 ) è fissata
                                                                            → ℎ1 non è fissato e varia con 𝐶𝐼𝑁2
   𝑡𝑝 = 𝑡𝑝0 𝑔1 ℎ1 + 𝑝1 + 𝑡𝑝0 𝑔2 ℎ2 + 𝑝2

      = 𝑡𝑝0 𝑔1 ℎ1 + 𝑔2 ℎ2 + 𝑝1 + 𝑝2

                             𝑃: 𝑝𝑎𝑡ℎ 𝑝𝑎𝑟𝑎𝑠𝑖𝑡𝑖𝑐 𝑒𝑓𝑓𝑜𝑟𝑡


           𝐶𝑂𝑈𝑇 𝐶𝐼𝑁2                  𝐶𝑂𝑈𝑇
    ℎ1 =       =             ℎ2 =
            𝐶𝑡   𝐶𝐼𝑁1                 𝐶𝐼𝑁2                                                                      19




                                                           CIRCUITI
                                                      ELECTRONIC    E SISTEMI
                                                                 CICUITS FOR HIGH       20
                                                                               ELETTRONICI
                                                                                  FREQUENCIES


             𝐶𝑂𝑈𝑇 𝐶𝐼𝑁2
      ℎ1 =       =
              𝐶𝑡   𝐶𝐼𝑁1

             𝐶𝑂𝑈𝑇
      ℎ2 =
             𝐶𝐼𝑁2

                                                                                 𝐶𝐼𝑁2 𝐶𝑂𝑈𝑇 𝐶𝑂𝑈𝑇
❑ Definiamo una nuova quantità:        𝑃𝑎𝑡ℎ 𝑒𝑙𝑒𝑐𝑡𝑟𝑖𝑐𝑎𝑙 𝑒𝑓𝑓𝑜𝑟𝑡: 𝐻   𝐻 ≜ ℎ1 ℎ2 =       ∙     =
                                                                                 𝐶𝐼𝑁1 𝐶𝐼𝑁2   𝐶𝐼𝑁1




▪ Due ipotesi:
    ❑ dimensioniamo il gate 2 di modo che sia grande (cioè 𝑆2 grande)
    ❑ dimensioniamo il gate 2 di modo che sia piccolo (cioè 𝑆2 piccolo)




                                                                                                                20
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       21
                                                                            ELETTRONICI
                                                                               FREQUENCIES


                        𝐻
  𝑡𝑝 = 𝑡𝑝0 𝑔1 ℎ1 + 𝑔2      +𝑃
                        ℎ1
                                        𝜕𝑡𝑝
 Minimizzare 𝑡𝑝 vuol dire calcolare         =0
                                        𝜕ℎ1

 Perché minimizzare solamente rispetto a ℎ1 ?
 - Sappiamo che H e un dato noto del problema
 - 𝑔1 e 𝑔2 dipendono dalla topologia dei gate ma non dal dimensionamento
 - P dipende da 𝑝1 e 𝑝2 ma questi dipendono SOLO dalla topologia e vincolo sui dimensionamenti relativi α
 - → l’unico parametro libero è ℎ1


  𝜕𝑡𝑝               𝐻            yields
      = 𝑡𝑝0 𝑔1 − 𝑔2 2 = 0                 𝑔1 ℎ1 = 𝑔2 ℎ2
  𝜕ℎ1              ℎ1

  Introduciamo una nuova entità: 𝑓: 𝑆𝑡𝑎𝑔𝑒 𝐸𝑓𝑓𝑜𝑟𝑡          𝑓 ≜ 𝑔ℎ
                                                                                                      21




                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       22
                                                                            ELETTRONICI
                                                                               FREQUENCIES


❑ Ritardo minimo quando stage effort f sono uguali
        → Non vuol dire che i ritardi dei due gate siano gli stessi!

❑ Introduciamo altre nuove entità:

         𝑃𝑎𝑡ℎ 𝐿𝑜𝑔𝑖𝑐𝑎𝑙 𝐸𝑓𝑓𝑜𝑟𝑡 ∶ 𝐺            𝐺 ≜ 𝑔1 𝑔2

                                                                               𝐶𝑂𝑈𝑇
          𝑃𝑎𝑡ℎ 𝐸𝑓𝑓𝑜𝑟𝑡 ∶ 𝐹                   𝐹 ≜ 𝑔1 ℎ1 𝑔2 ℎ2 = 𝐺𝐻 = 𝑔1 𝑔2
                                                                               𝐶𝐼𝑁1


                                           𝜕𝑡𝑝               𝐻            yields
❑ Riscriviamo la condizione di ottimo          = 𝑡𝑝0 𝑔1 − 𝑔2 2 = 0                    𝑔1 ℎ1 = 𝑔2 ℎ2
                                           𝜕ℎ1              ℎ1


                                                                               𝐶𝑂𝑈𝑇
         𝑆𝑡𝑎𝑔𝑒 𝐸𝑓𝑓𝑜𝑟𝑡 𝑂𝑡𝑡𝑖𝑚𝑜: 𝑓መ           𝑓መ = 𝑔1 ℎ1 = 𝑔2 ℎ2 = 𝐹 =    𝑔1 𝑔2
                                                                               𝐶𝐼𝑁1

                                                                                                      22
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       23
                                                                            ELETTRONICI
                                                                               FREQUENCIES

  Determinazione dei dimensionamenti




                                                                                                     23




                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       24
                                                                            ELETTRONICI
                                                                               FREQUENCIES

❑ In questo modo troviamo che il tempo ottimo di propagazione del segnale attraverso i due gate:

       𝑡𝑜𝑡𝑡 = 𝑡𝑝0 𝑔1 ℎ1 + 𝑔2 ℎ2 + 𝑃


                              𝐶𝑂𝑈𝑇
            = 𝑡𝑝0 2 𝑔1 𝑔2          +𝑃
                              𝐶𝐼𝑁1


Ricordiamo che i dati noti erano:
❑ logical effort g di tutti i gate logici
❑ 𝐶𝑂𝑈𝑇
❑ Dimensionamenti del primo stadio (𝐶𝐼𝑁1 )




           Notiamo che 𝑡𝑜𝑡𝑡 ↓ se 𝐶𝐼𝑁1 ↑: potrei pensare di fare in modo che 𝐶𝐼𝑁1 sia molto grande!

                                                                                                     24
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       25
                                                                              ELETTRONICI
                                                                                 FREQUENCIES

 Notiamo che 𝑡𝑜𝑡𝑡 ↓ se 𝐶𝐼𝑁1 ↑: potrei pensare di fare in modo che 𝐶𝐼𝑁1 sia molto grande!
                    → attenzione però che chi pilota il gate 1 si troverebbe un carico «difficile» da pilotare




 L’ottimizzazione ha senso solo assieme ad un vincolo sulle capacità che il circuito mostra ai gate che stanno a
 monte → cioè ci deve essere un vincolo su 𝐶𝐼𝑁




                                                                                                                 25




                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       26
                                                                              ELETTRONICI
                                                                                 FREQUENCIES

Caso semplice di: serie di due invertitori



                    𝜀𝑆1              𝜌𝜀𝑆1


                   𝑆1               𝜌𝑆1




                                                                                                                 26
                                                                   CIRCUITI
                                                              ELECTRONIC    E SISTEMI
                                                                         CICUITS FOR HIGH       27
                                                                                       ELETTRONICI
                                                                                          FREQUENCIES

                                           Circuiti con diramazioni
Estendiamo precedente studio finalizzato a minimizzare i ritardi al caso in cui fan-out è maggiore di 1


                                                                                 Parte della corrente del gate i carica 𝐶𝑖+1 e
                                                                                 un’altra parte carica la capacità di off-path

                                                                                        𝐶𝑖+1 + 𝐶𝑜𝑓𝑓−𝑝𝑎𝑡ℎ
                                                                                 ℎ𝑖 =
                                                                                               𝐶𝑖

                                                                                        𝐶𝑖+1 𝐶𝑖+1 + 𝐶𝑜𝑓𝑓−𝑝𝑎𝑡ℎ
                                                                                   =
                         stadio i                                                        𝐶𝑖        𝐶𝑖+1
                                             stadio i+1

                                                                                         𝑟𝑖          𝑏𝑖 : 𝑏𝑟𝑎𝑛𝑐ℎ𝑖𝑛𝑔 𝑒𝑓𝑓𝑜𝑟𝑡

  In relazione al percorso di segnale complessivo definiamo il Path Branching Effort B
                                                                           𝑁

                                                                     𝐵 = ෑ 𝑏𝑖
                                                                                                                         27
                                                                          𝑖=1




                                                                   CIRCUITI
                                                              ELECTRONIC    E SISTEMI
                                                                         CICUITS FOR HIGH       28
                                                                                       ELETTRONICI
                                                                                          FREQUENCIES

  Il path electric effort H diventa:
            𝑁
                    𝐶2 𝐶3    𝐶𝑂𝑈𝑇 𝐶𝑂𝑈𝑇
      𝐻 = ෑ 𝑟𝑖 =      × × ⋯×     =
                    𝐶1 𝐶2     𝐶𝑛   𝐶1
            𝑖=1



  Dunque lo stage effort f del generico gate diventa

                                                          𝑓 = 𝑔𝑖 ℎ𝑖 = 𝑔𝑖 𝑟𝑖 𝑏𝑖

  E quindi il path effort F nel caso di diramazioni diventa

                                       𝑁             𝑁                      𝑁
                                                                                              𝐶𝑂𝑈𝑇
                                 𝐹 = ෑ 𝑔𝑖 ℎ𝑖 = ෑ 𝑔𝑖 𝑟𝑖 𝑏𝑖 = 𝐺𝐵 ෑ 𝑟𝑖 = 𝐺𝐵𝐻 = 𝐺𝐵
                                                                                               𝐶𝐼𝑁
                                       𝑖=1          𝑖=1                    𝑖=1


                                    Equazione per il path effort F alla base dell’ottimizzazione
                                                            del ritardo


                                                                                                                         28
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       29
                                                                              ELETTRONICI
                                                                                 FREQUENCIES

                                                   Summary
                                𝑅𝑡 𝐶𝑡                                                                    𝐶𝑂𝑈𝑇
𝑔: 𝐿𝑜𝑔𝑖𝑐𝑎𝑙 𝐸𝑓𝑓𝑜𝑟𝑡        𝑔=                                    𝐻: 𝑃𝑎𝑡ℎ 𝐸𝑙𝑒𝑐𝑡𝑟𝑖𝑐𝑎𝑙 𝐸𝑓𝑓𝑜𝑟𝑡    𝐻 = ෑ 𝑟𝑖 =
                              𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉                                                                   𝐶𝐼𝑁
                                                                                                   𝑖
                            𝐶𝑂𝑈𝑇                                                               𝑁
ℎ: 𝐸𝑙𝑒𝑐𝑡𝑟𝑖𝑐𝑎𝑙 𝐸𝑓𝑓𝑜𝑟𝑡     ℎ=                                                                                   𝐶𝑂𝑈𝑇
                             𝐶𝑡                                𝐹: 𝑃𝑎𝑡ℎ 𝐸𝑓𝑓𝑜𝑟𝑡              𝐹 = ෑ 𝑔𝑖 ℎ𝑖 = 𝐺𝐵
                                                                                                               𝐶𝐼𝑁
                                𝑅𝑡 𝐶𝑝𝑡                                                         𝑖=1
𝑝: 𝑃𝑎𝑟𝑎𝑠𝑖𝑡𝑖𝑐 𝐸𝑓𝑓𝑜𝑟𝑡      𝑝=
                              𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉
                                                               መ 𝑆𝑡𝑎𝑔𝑒 𝐸𝑓𝑓𝑜𝑟𝑡 𝑜𝑡𝑡𝑖𝑚𝑜
                                                               𝑓:                          𝑓መ = 𝐹
                              𝐶𝑖+1 + 𝐶𝑜𝑓𝑓−𝑝𝑎𝑡ℎ
𝑏: 𝐵𝑟𝑎𝑛𝑐ℎ𝑖𝑛𝑔 𝐸𝑓𝑓𝑜𝑟𝑡      𝑏𝑖 =
                                    𝐶𝑖+1

𝐵: 𝑃𝑎𝑡ℎ 𝐵𝑟𝑎𝑛𝑐ℎ𝑖𝑛𝑔 𝐸𝑓𝑓𝑜𝑟𝑡 𝐵 = ෑ 𝑏𝑖
                                    𝑖


𝑃: 𝑃𝑎𝑡ℎ 𝑃𝑎𝑟𝑎𝑠𝑖𝑡𝑖𝑐 𝐸𝑓𝑓𝑜𝑟𝑡        𝑃 = ෍ 𝑝𝑖
                                        𝑖


𝐺: 𝑃𝑎𝑡ℎ 𝐿𝑜𝑔𝑖𝑐𝑎𝑙 𝐸𝑓𝑓𝑜𝑟𝑡          𝐺 = ෑ 𝑔𝑖
                                                                                                           29
                                        𝑖




                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       30
                                                                              ELETTRONICI
                                                                                 FREQUENCIES


In un problema di ottimizzazione:
❑ 𝐶𝑂𝑈𝑇 e 𝐶𝐼𝑁 sono dati noti
❑ La conoscenza della tipologia di gate logico implica la conoscenza di 𝑔𝑖
❑ La topologia del circuito consente di determinare 𝑏𝑖



L’ottimizzazione consiste nell’opportuno dimensionamento degli stadi al fine di partizionare il ritardo in modo da
minimizzarlo



                                    Ottimizzo il ritardo a numero di stadi fissato
            Due
            casi
                                    Il numero di stadi è un parametro
                                    dell’ottimizzazione

                                                                                                           30
                                                                  CIRCUITI
                                                             ELECTRONIC    E SISTEMI
                                                                        CICUITS FOR HIGH       31
                                                                                      ELETTRONICI
                                                                                         FREQUENCIES

                     Ottimizzazione a numero di stadi fissato
❑ Topologia nota
❑ Numero di stadi
❑ 𝑔𝑖 e 𝑏𝑖 noti, e anche 𝐻 = 𝐶𝑂𝑈𝑇 /𝐶𝐼𝑁

Obiettivo: dimensionare gli stadi per minimizzare il ritardo complessivo

                                                  𝑁

                                         𝑡𝑎𝑑 = ෍ 𝑔𝑖 ℎ𝑖 + 𝑝𝑖
                                                 𝑖=1

                                                 𝑁                   𝑁

                                        𝑡𝑎𝑑 = ෍ 𝑔𝑖 𝑏𝑖 𝑟𝑖 + 𝑝𝑖 = ෍ 𝑔𝑖 𝑏𝑖 𝑟𝑖 + 𝑃
                                                 𝑖=1                𝑖=1


                                   𝑁
                   𝐶𝑂𝑈𝑇
Ricordiamo che 𝐻 =      = ෑ 𝑟𝑖
                    𝐶𝐼𝑁
                               𝑖=1

                                                                                                       31




                                                                  CIRCUITI
                                                             ELECTRONIC    E SISTEMI
                                                                        CICUITS FOR HIGH       32
                                                                                      ELETTRONICI
                                                                                         FREQUENCIES

               𝑁
                                         𝐻
         𝐻 = ෑ 𝑟𝑖            𝑟𝑁 =
                                       ς𝑁−1
                                        𝑖=1 𝑟𝑖
              𝑖=1

                               𝑁                       𝑁                  𝑁−1
                                                                                      𝐻
                        𝑡𝑎𝑑 = ෍ 𝑔𝑖 ℎ𝑖 + 𝑝𝑖 = ෍ 𝑔𝑖 𝑏𝑖 𝑟𝑖 + 𝑃 = ෍ 𝑔𝑖 𝑟𝑖 𝑏𝑖 + 𝑔𝑁               +𝑃
                                                                                    ς𝑁−1
                                                                                     𝑖=1 𝑟𝑖
                              𝑖=1                      𝑖=1                𝑖=1




                                                                                                       32
                                                                 CIRCUITI
                                                            ELECTRONIC    E SISTEMI
                                                                       CICUITS FOR HIGH       33
                                                                                     ELETTRONICI
                                                                                        FREQUENCIES
                                    𝑁−1
                                                𝐻
Minimizziamo il ritardo 𝑡𝑎𝑑 = ෍ 𝑔𝑖 𝑟𝑖 𝑏𝑖 + 𝑔𝑁 ς𝑁−1                +𝑃
                                    𝑖=1                  𝑖=1 𝑟𝑖



                𝜕𝑡𝑎𝑑                      𝜕𝑡𝑎𝑑                           𝑔𝑁 𝐻
                     อ         =0              อ         = 𝑔𝑗 𝑏𝑗 −                +0=0
                 𝜕𝑟𝑗                       𝜕𝑟𝑗                         ς𝑁−1
                                                                        𝑖=1 𝑟𝑖 𝑟𝑗
                         𝑗≠𝑁                       𝑗≠𝑁

                                                                     𝑔𝑁 𝑟𝑁
                                                         = 𝑔𝑗 𝑏𝑗 −         +0=0
                                                                      𝑟𝑗

                                                         = 𝑔𝑗 𝑏𝑗 𝑟𝑗 = 𝑔𝑁 𝑟𝑁     ∀𝑗 ≠ 𝑁


 CONDIZIONE DI OTTIMO: Lo stage effort di tutti gli stadi deve essere:

                                             𝑓መ = 𝑔𝑖 𝑏𝑖 𝑟𝑖 = 𝐹 = 𝑔𝑁 𝑟𝑁
                                                            𝑁
                                                                                 ∀𝑗 ≠ 𝑁


                                              𝑁
                                                                                    𝑁
 Il tempo di ritardo ottimo diventa: 𝑡𝑎𝑑 = ෍ 𝑔𝑖 ℎ𝑖 𝑟𝑖 + 𝑃                     𝑡𝑎𝑑 = 𝑁 𝐹 + 𝑃
                                              𝑖=1                                                                 33




                                                                 CIRCUITI
                                                            ELECTRONIC    E SISTEMI
                                                                       CICUITS FOR HIGH       34
                                                                                     ELETTRONICI
                                                                                        FREQUENCIES

                     Come utilizzare il metodo di ottimizzazione
❑ Sono noti 𝑏 e 𝑔 di ogni stadio, 𝐶𝑂𝑈𝑇 e 𝐶𝐼𝑁 → e dunque 𝐹 e 𝑓መ
❑ Partiamo dall’ultimo stadio visto che 𝐶𝑂𝑈𝑇 = 𝐶𝑖+1
❑ Se conosciamo: 𝑏𝑖 , 𝑔𝑖 , 𝐶𝑖+1 , 𝑓መ possiamo calcolare la capacità di
  ingresso dello stadio i-esimo dato che                                   𝐶𝑖+1
                                                     𝑓መ = 𝑔𝑖 𝑏𝑖 𝑟𝑖 = 𝑔𝑖 𝑏𝑖
                                                                            𝐶𝑖
                                                                                                 𝑔𝑖 𝑏𝑖 𝐶𝑖+1
❑ In particolare per l’ultimo stadio: 𝑏𝑁 = 1, e quindi 𝐶𝑁 = 𝑔𝑁 𝐶𝑂𝑈𝑇 Τ𝑓መ                   𝐶𝑖 =
                                                                                                     𝑓መ
                                                                                                   𝑔𝑖−1 𝑏𝑖−1 𝐶𝑖
❑ Nota 𝐶𝑖 ho la 𝐶𝑂𝑈𝑇 dello stadio 𝑖 − 1 → Proseguo a ritroso!                             𝐶𝑖−1 =
                                                                                                        𝑓መ


❑ Ci fermiamo dimensionando il secondo stadio visto che il primo stadio ha dimensionamento fissato (𝐶𝐼𝑁 è nota,
  è una specifica di progetto)
     ❑ Come double-check si può verificare che 𝐶1 = 𝐶𝐼𝑁 (se 𝐶1 calcolata corrisponde a quella data dal
       problema)
                                                                                                                  34
                                                              CIRCUITI
                                                         ELECTRONIC    E SISTEMI
                                                                    CICUITS FOR HIGH       35
                                                                                  ELETTRONICI
                                                                                     FREQUENCIES

Esempio di dimensionamenti

                          y
                                          z



                          y
                                          z




                                          z




                                                                                                                35




                                                              CIRCUITI
                                                         ELECTRONIC    E SISTEMI
                                                                    CICUITS FOR HIGH       36
                                                                                  ELETTRONICI
                                                                                     FREQUENCIES

                                                     Alcune note
                                                         𝜕𝑏𝑖
❑ Nella derivazione del modello si è assunto che             =0   cioè che 𝑏𝑖 non dipende dai dimensionamenti
                                                         𝜕𝑟𝑖
                                  𝑁−1
 𝜕𝑡𝑎𝑑                                               𝐻
      อ         = 0 con   𝑡𝑎𝑑 = ෍ 𝑔𝑖 𝑟𝑖 𝑏𝑖 + 𝑔𝑁           +𝑃
  𝜕𝑟𝑗                                             ς𝑁−1
                                                   𝑖=1 𝑟𝑖
          𝑗≠𝑁                     𝑖=1


                              𝐶𝑖+1 + 𝐶𝑜𝑓𝑓−𝑝𝑎𝑡ℎ
  ricordiamo che 𝑏𝑖 =
                                    𝐶𝑖+1
❑ 𝐶𝑖+1 = 𝐶𝑜𝑛−𝑝𝑎𝑡ℎ è proporzionale al dimensionamento 𝑖 + 1

❑ Affinchè 𝑏𝑖 non dipenda dal dimensionamento, anche 𝐶𝑜𝑓𝑓−𝑝𝑎𝑡ℎ deve                 stadio i       stadio i+1
  essere proporzionale al dimensionamento dello stadio i+1

❑ Se però 𝐶𝑜𝑓𝑓−𝑝𝑎𝑡ℎ è data:
     ❑ capacità di un’interconnessione                               𝑏𝑖 dipenderà dal dimensionamento e
                                                                     l’equazione di ottimo sarà diversa da
     ❑ capacità di ingresso di un gate a dimensionato fissato        quella calcolata                           36
                                                               CIRCUITI
                                                          ELECTRONIC    E SISTEMI
                                                                     CICUITS FOR HIGH       37
                                                                                   ELETTRONICI
                                                                                      FREQUENCIES

                      Ottimizzazione a numero variabile di stadi
 Se modifichiamo il numero di stadi è possibile ottenere un ritardo inferiore?

 ❑ Vogliamo determinare il numero di invertitori da aggiungere per minimizzare il ritardo

                 𝑔𝑖 = 1

                             𝐶𝑂𝑈𝑇
                    𝐹 = 𝐺𝐵
                              𝐶𝐼𝑁

 ❑ 𝑛1 = numero di stadi iniziali
 ❑ 𝑛2 = numero di invertitori da aggiungere
 ❑ 𝑁 = 𝑛1 + 𝑛2
 ❑ Sappiamo già che dati N stadi, il ritardo minimo si ha quando 𝑓መ =
                                                                                𝑁
                                                                                    𝐹 (di ogni stadio) e dunque

                      𝑛1
             𝑁
     𝑡Ƹ𝑎𝑑 = 𝑁 𝐹 + ෍ 𝑝𝑖 + 𝑁 − 𝑛1 𝑝𝐼𝑁𝑉
                      𝑖=1
                                                                                                                  37




                                                               CIRCUITI
                                                          ELECTRONIC    E SISTEMI
                                                                     CICUITS FOR HIGH       38
                                                                                   ELETTRONICI
                                                                                      FREQUENCIES

             𝜕𝑡Ƹ𝑎𝑑
Calcoliamo            assumendo 𝑁𝜖 ℝ
              𝜕𝑁
     𝜕𝑡Ƹ𝑎𝑑     1      1       −1
           = 𝐹 𝑁 + 𝑁𝐹 𝑁 𝑙𝑛 𝐹 ∙ 2 + 𝑝𝐼𝑁𝑉
      𝜕𝑁                      𝑁
                      1
     𝜕𝑡Ƹ𝑎𝑑    1   𝐹 𝑁 𝑙𝑛 𝐹
           = 𝐹𝑁 −          + 𝑝𝐼𝑁𝑉
      𝜕𝑁             𝑁

     𝜕𝑡Ƹ𝑎𝑑     1     1      1                   ora la condizione di ottimo
           = 𝐹 𝑁 − 𝐹 𝑁 𝑙𝑛 𝐹 𝑁 + 𝑝𝐼𝑁𝑉            dipende da F e da 𝑝𝐼𝑁𝑉
      𝜕𝑁
                1
Definiamo 𝜌= 𝐹 𝑁
                                                           𝜌 ≅ 0,71𝑝𝐼𝑁𝑉 +2,82
                                                           𝜌 esatta
      𝜌 1 − 𝑙𝑛𝜌 + 𝑝𝐼𝑁𝑉 = 0
                          soluzione analitica
                          approssimata

       𝜌 ≅ 0,71𝑝𝐼𝑁𝑉 +2,82



                                                                                                                  38
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       39
                                                                            ELETTRONICI
                                                                               FREQUENCIES

                                   ❑ 𝜌 ci dice qual è lo stage effort ottimo da usare nei circuiti della nostra
    𝜌 1 − 𝑙𝑛𝜌 + 𝑝𝐼𝑁𝑉 = 0             tecnologia per avere il ritardo ottimo (che è caratteristico della tecnologia
                                     (attraverso 𝑝𝐼𝑁𝑉 ) e non dipende dal circuito in esame)
                                   ❑ mentre 𝑓መ è lo stage effort ottimo di un dato circuito dove sono noti path
    𝜌 ≅ 0,71𝑝𝐼𝑁𝑉 +2,82               effort e numero di stadi con numero di stadi fissato

❑ dato un circuito con path effort F trovo il numero di stadi N necessario affinché lo stage effort di tutti gli
  stadi sia pari a 𝜌


                            calcoliamo
❑ Noti 𝜌 e 𝑝𝑎𝑡ℎ 𝑒𝑓𝑓𝑜𝑟𝑡 𝐹                 ෡ = 𝑙𝑛𝐹 Τ𝑙𝑛𝜌
                                         𝑁

❑ Il ritardo sarà dunque dato da
                                                                         𝑛1
                                                   ෡
                                                  ෡𝑁 𝐹 + 𝑁
                                           𝑡Ƹ𝑎𝑑 = 𝑁      ෡ − 𝑛1 𝑝𝐼𝑁𝑉 + ෍ 𝑝𝑖
                                                                         𝑖=1




                                                                                                            39




                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       40
                                                                            ELETTRONICI
                                                                               FREQUENCIES

ESEMPIO: buffer di invertitori




                                                                                                            40
                                                    CIRCUITI
                                               ELECTRONIC    E SISTEMI
                                                          CICUITS FOR HIGH       41
                                                                        ELETTRONICI
                                                                           FREQUENCIES

                                            Alcune note
 ❑ Supponiamo che inizialmente il circuito abbia un numero di stadi 𝑛1 e di ottenere un numero ottimo di
         ෡ > 𝑛1
   stadi 𝑁

                      ෡ − 𝑛1 = 𝑛2 stadi (ma se 𝑁
 ❑ Dovremo aggiungere 𝑁                        ෡ ∈ℝ lo sarà anche 𝑛2 )

 ❑ 𝑛2 dovrà essere un numero intero! Dobbiamo capire come scegliere 𝑛2

                                                Soluzione 1
 ❑ Se usiamo 𝑁  ෡ calcolato mediante 𝑁
                                     ෡ = 𝑙𝑛𝐹 Τ𝑙𝑛𝜌 , sappiamo che lo stage ottimo è 𝜌 ma se approssimiamo 𝑁
                                                                                                         ෡
                                                                         𝑁
   con un numero intero, dobbiamo ricalcolare lo stage effort ottimo 𝜌 = 𝐹 sul numero di stadi che abbiamo
   deciso di utilizzare
     ❑ Possiamo dimensionare tutti gli stadi in modo tale che abbiano lo stesso stage effort pari a quello
       ricalcolato a valle della scelta di 𝑁 intero
                                                Soluzione 2
❑ Usiamo lo stage effort calcolato mediante 𝜌 ≅ 0,71𝑝𝐼𝑁𝑉 +2,82. In questo modo però non possiamo imporre
  lo stesso stage effort 𝑓መ = 𝜌 in tutti gli stadi. Infatti il primo stadio avrà uno stage effort diverso
                                                                                                    41




                                                    CIRCUITI
                                               ELECTRONIC    E SISTEMI
                                                          CICUITS FOR HIGH       42
                                                                        ELETTRONICI
                                                                           FREQUENCIES

ESEMPIO di ottimizzazione di ritardi




 stadio 1     stadio 2     stadio 3




                                                                                                    42
                                                      CIRCUITI
                                                 ELECTRONIC    E SISTEMI
                                                            CICUITS FOR HIGH       43
                                                                          ELETTRONICI
                                                                             FREQUENCIES

ESEMPIO di ottimizzazione di ritardi




 stadio 1     stadio 2     stadio 3




                                                                                                       43




                                                      CIRCUITI
                                                 ELECTRONIC    E SISTEMI
                                                            CICUITS FOR HIGH       44
                                                                          ELETTRONICI
                                                                             FREQUENCIES

                                  Sensibilità a numero stadi
 ❑ Cosa accade al ritardo quando ci si discosta dalla condizione di ottimo per il numero di stadi o per i
   dimensionamenti?
             ෡ il numero ottimo di stadi (con 𝑁
 ❑ Definiamo 𝑁                                ෡ ∈ 𝑅) e supponiamo che il numero di stadi usato sia N = s𝑁
                                                                                                        ෡

 ❑ Semplifichiamo i calcoli assumendo stadi con stesso parasitic effort



  ❑ Ritardo ottimo                                           ❑ Ritardo non-ottimo
                      ෡                                                             𝑁
             ෡ =𝑁
         𝑡𝑎𝑑 𝑁  ෡     𝑁
                               ෡ 𝜌+𝑝
                          𝐹+𝑝 =𝑁                                      𝑡𝑎𝑑 𝑁 = 𝑁         𝐹+𝑝




                                                                                                       44
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       45
                                                                           ELETTRONICI
                                                                              FREQUENCIES


                     1              1
    𝑡𝑎𝑑 𝑁    ෡ 𝜌𝑠 + 𝑝
            𝑠𝑁           𝜌𝑠 + 𝑝                                       𝑝𝐼𝑁𝑉 = 1        𝜌 = 3.59
 𝑟=       =           =𝑠
        ෡
    𝑡𝑎𝑑 𝑁    ෡ 𝜌+𝑝
             𝑁           𝜌+𝑝                                           𝑝𝐼𝑁𝑉 = 2       𝜌 = 4.32
❑ Nota la tecnologia (𝜌 e 𝑝) grafichiamo r vs s

❑ Il ritardo sale molto di più quando vengono




                                                            r
                                             ෡
  usati meno stadi rispetto al numero ottimo 𝑁




    è sempre meglio approssimare per eccesso

                                                                                  s




                                                                                                     45




                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       46
                                                                           ELETTRONICI
                                                                              FREQUENCIES

                              Sensibilità ai dimensionamenti
                 ෡ sia intero
❑ Supponiamo che 𝑁
❑ Supponiamo anche che in uno degli stadi sia presente un dimensionamento diverso da quello ottimo
  (limiti tecnologici, …)
                                1
                               𝐹 𝑁෡ 𝜌
    Il path effort sarà   𝑓𝑖 =     =
                                𝑠    𝑠

❑ Lo stadio che precede avrà stage effort diverso da quello ottimo

                            𝑓𝑖−1 = 𝑠𝜌




                                                                                                     46
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       47
                                                                            ELETTRONICI
                                                                               FREQUENCIES

                                 Sensibilità ai dimensionamenti
❑ Gli 𝑁 − 2 stadi conservano lo stage effort ottimo 𝐹 1Τ𝑁෡                        𝑝𝐼𝑁𝑉 = 1                    𝜌 = 3.59
❑ Assumendo tutti uguali i parasitic effort                                       𝑝𝐼𝑁𝑉 = 2                    𝜌 = 4.32

                            ෡
       𝑡ෞ              ෡
        𝑎𝑑 = 𝑡𝑎𝑑 𝑠=1 = 𝑁
                            𝑁
                                𝐹+𝑝                                                                       𝑁=3

     mentre




                                                              r
                                              ෡
                                              𝑁
                                               𝐹                                                                   𝑁=6
               ෡ − 2 𝑁෡ 𝐹 + 𝑁𝑝
       𝑡𝑎𝑑 𝑠 = 𝑁            ෡ + 𝑠 𝑁෡ 𝐹 +
                                              𝑠



        𝑡𝑎𝑑 𝑁   𝑁𝜌  ෡ − 2𝜌 + 𝜌𝑠 + 𝜌
                ෡ + 𝑁𝑝
     𝑟=       =                   𝑠
            ෡
        𝑡𝑎𝑑 𝑁        ෡ + 𝑁𝑝
                     𝑁𝜌  ෡

                        𝜌
                        𝜌𝑠 +
                        𝑠 − 2𝜌
                                                                                               s
                 =1+
                     ෡ 𝜌+𝑝
                     𝑁                                  è sempre meglio approssimare per eccesso                     47




                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       1
                                                                            ELETTRONICI
                                                                               FREQUENCIES

                                                   Summary
                                  𝑅𝑡 𝐶𝑡                                                                           𝐶𝑂𝑈𝑇
𝑔: 𝐿𝑜𝑔𝑖𝑐𝑎𝑙 𝐸𝑓𝑓𝑜𝑟𝑡        𝑔=                                  𝐻: 𝑃𝑎𝑡ℎ 𝐸𝑙𝑒𝑐𝑡𝑟𝑖𝑐𝑎𝑙 𝐸𝑓𝑓𝑜𝑟𝑡             𝐻 = ෑ 𝑟𝑖 =
                                𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉                                                                          𝐶𝐼𝑁
                                                                                                          𝑖
                            𝐶𝑂𝑈𝑇                                                                      𝑁
ℎ: 𝐸𝑙𝑒𝑐𝑡𝑟𝑖𝑐𝑎𝑙 𝐸𝑓𝑓𝑜𝑟𝑡     ℎ=                                                                                              𝐶𝑂𝑈𝑇
                             𝐶𝑡                              𝐹: 𝑃𝑎𝑡ℎ 𝐸𝑓𝑓𝑜𝑟𝑡                    𝐹 = ෑ 𝑔𝑖 ℎ𝑖 = 𝐺𝐵
                                                                                                                          𝐶𝐼𝑁
                                  𝑅𝑡 𝐶𝑝𝑡                                                             𝑖=1
𝑝: 𝑃𝑎𝑟𝑎𝑠𝑖𝑡𝑖𝑐 𝐸𝑓𝑓𝑜𝑟𝑡      𝑝=
                                𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉                    መ 𝑆𝑡𝑎𝑔𝑒 𝐸𝑓𝑓𝑜𝑟𝑡 𝑜𝑡𝑡𝑖𝑚𝑜             𝑓መ = 𝑔𝑖 𝑏𝑖 𝑟𝑖 = 𝐹
                                                                                                              𝑁
                                                             𝑓:
                                𝐶𝑖+1 + 𝐶𝑜𝑓𝑓−𝑝𝑎𝑡ℎ
𝑏: 𝐵𝑟𝑎𝑛𝑐ℎ𝑖𝑛𝑔 𝐸𝑓𝑓𝑜𝑟𝑡      𝑏𝑖 =
                                      𝐶𝑖+1
                                                             𝜌: 𝑆𝑡𝑎𝑔𝑒 𝐸𝑓𝑓𝑜𝑟𝑡 𝑜𝑡𝑡𝑖𝑚𝑜 ≅ 0,71𝑝𝐼𝑁𝑉 +2,82
𝐵: 𝑃𝑎𝑡ℎ 𝐵𝑟𝑎𝑛𝑐ℎ𝑖𝑛𝑔 𝐸𝑓𝑓𝑜𝑟𝑡 𝐵 = ෑ 𝑏𝑖
                                     𝑖


𝑃: 𝑃𝑎𝑡ℎ 𝑃𝑎𝑟𝑎𝑠𝑖𝑡𝑖𝑐 𝐸𝑓𝑓𝑜𝑟𝑡          𝑃 = ෍ 𝑝𝑖
                                         𝑖


𝐺: 𝑃𝑎𝑡ℎ 𝐿𝑜𝑔𝑖𝑐𝑎𝑙 𝐸𝑓𝑓𝑜𝑟𝑡            𝐺 = ෑ 𝑔𝑖
                                                                                                                         1
                                         𝑖
                                                                       stadio i   stadio i+1
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       2
                                                                            ELETTRONICI
                                                                               FREQUENCIES

                                                  Summary
In un problema di ottimizzazione:
❑ 𝐶𝑂𝑈𝑇 e 𝐶𝐼𝑁 sono dati noti
❑ La conoscenza della tipologia di gate logico implica la conoscenza di 𝑔𝑖
❑ La topologia del circuito consente di determinare 𝑏𝑖



L’ottimizzazione consiste nell’opportuno dimensionamento degli stadi al fine di partizionare il ritardo in modo da
minimizzarlo

                                                    Due casi




                        Ottimizzazione a numero              Ottimizzazione del ritardo
                             di stadi fissato                    aggiungendo, se
                                                               necessario, inveritori
                                                                                                            2




                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       3
                                                                            ELETTRONICI
                                                                               FREQUENCIES

                      Ottimizzazione a numero di stadi fissato
CONDIZIONE DI OTTIMO: Lo stage effort di tutti gli stadi deve essere:


                                                                                                    𝐶𝑂𝑈𝑇
                                        𝑓መ = 𝑔𝑖 𝑏𝑖 𝑟𝑖 = 𝐹 = 𝑔𝑁 𝑟𝑁
                                                       𝑁
                                                                      ∀𝑗 ≠ 𝑁         con   𝐹 = 𝐺𝐵
                                                                                                     𝐶𝐼𝑁



                                           𝑁
                                                                          𝑁
Il tempo di ritardo ottimo diventa: 𝑡𝑎𝑑 = ෍ 𝑔𝑖 𝑏𝑖 𝑟𝑖 + 𝑃            𝑡𝑎𝑑 = 𝑁 𝐹 + 𝑃
                                          𝑖=1




                                                                                                            3
                                                                CIRCUITI
                                                           ELECTRONIC    E SISTEMI
                                                                      CICUITS FOR HIGH       4
                                                                                    ELETTRONICI
                                                                                       FREQUENCIES

                         Ottimizzazione a numero variabile di stadi
❑ L’inserimento di invertitori non modifica il path effort F (perché 𝑔𝑖𝑛𝑣 = 1)                                                1              1
                                                                                                                𝑡𝑎𝑑 𝑁    ෡ 𝜌𝑠 + 𝑝
                                                                                                                        𝑠𝑁           𝜌𝑠 + 𝑝
                                                                                                       𝑟=             =           =𝑠
           𝜌 ≅ 0,71𝑝𝐼𝑁𝑉 +2,82 calcoliamo ෡                                                                          ෡
                                                                                                                𝑡𝑎𝑑 𝑁    ෡ 𝜌+𝑝
                                                                                                                         𝑁           𝜌+𝑝
❑ Noti ቊ                                 𝑁 = 𝑙𝑛𝐹 Τ𝑙𝑛𝜌
             𝑝𝑎𝑡ℎ 𝑒𝑓𝑓𝑜𝑟𝑡 𝐹
                                                                                                                       𝑝𝐼𝑁𝑉 = 1       𝜌 = 3.59
                                                                                                        2
                                                     ෡ non sarà un numero intero → devo
                                                     𝑁                                                                 𝑝𝐼𝑁𝑉 = 2       𝜌 = 4.32
                                                                                                            2
                                                     approssimarlo con un numero intero
                                                     (sempre meglio per eccesso)




                                                                                                       r
                                                          ora ci sono due strade

                                                                                                                                  2      2
                                                                                                                              s

             ricalcolo lo stage effort ottimo con N                     assumo lo stage effort ottimo uguale
             intero                                                     a quello con 𝑁 ∈ ℛ cioè 𝑓መ = 𝜌 per gli
                         𝑓መ = 𝑔𝑖 𝑏𝑖 𝑟𝑖 = 𝐹                              N-1 stadi. Ci sarà poi uno stadio con
                                        𝑁
                                                                        𝑓≠𝜌
                              𝑛1                                                           𝑛1
                     𝑁
           𝑡Ƹ𝑎𝑑 = 𝑁 𝐹 + ෍ 𝑝𝑖 + 𝑁 − 𝑛1 𝑝𝐼𝑁𝑉                         𝑡Ƹ𝑎𝑑 = 𝑁 − 1 𝜌 + 𝑓 + ෍ 𝑝𝑖 + 𝑁 − 𝑛1 𝑝𝐼𝑁𝑉
                              𝑖=1                                                          𝑖=1
        ❑ 𝑛1 = numero di stadi iniziali                                                                                           4
        ❑ 𝑛2 = numero di invertitori da aggiungere
        ❑ 𝑁 = 𝑛1 + 𝑛2




                                                                CIRCUITI
                                                           ELECTRONIC    E SISTEMI
                                                                      CICUITS FOR HIGH       5
                                                                                    ELETTRONICI
                                                                                       FREQUENCIES


Importante ricordare che:

 ❑ 𝜌 ci dice qual è lo stage effort ottimo da usare nei circuiti della nostra tecnologia per avere il ritardo
   ottimo (che è caratteristico della tecnologia (attraverso 𝑝𝐼𝑁𝑉 ) e non dipende dal circuito in esame)
 ❑ mentre 𝑓መ è lo stage effort ottimo di un dato circuito dove sono noti path effort e numero di stadi




                                                                                                                                  5
                                                                  CIRCUITI
                                                             ELECTRONIC    E SISTEMI
                                                                        CICUITS FOR HIGH       6
                                                                                      ELETTRONICI
                                                                                         FREQUENCIES

                        Calibrazione del modello del logical effort
La calibrazione del modello consiste nell’estrazione di 𝑡𝑝0
e 𝑝𝑖𝑛𝑣 basata sulla simulazione del comportamento
dell’invertitore al variare della capacità di carico (quindi
                                                                                          𝑡𝑝,𝑖𝑛𝑣 = 𝑡𝑝0 𝑔ℎ + 𝑝𝑖𝑛𝑣
dell’electrical effort h), attraverso un’adeguata struttura di
test.

                                   Non è il circuito adatto per calibrare il modello del logical effort.
                                   Soluzione migliore: caricare l’invertitore con invertitori identici.
                                   h corrisponde al numero di stadi connessi all’uscita del gate il
                                   cui ritardo intendiamo caratterizzare




                                                                                ❑ 𝑡𝑝0 ∶ pendenza della retta interpolatrice
                                                                                ❑ 𝑝𝑖𝑛𝑣 𝑡𝑝0 ∶intercetta con l’asse verticale
                                                                          𝑡𝑝0
                               𝑡𝑝0 × 𝑝𝑖𝑛𝑣

                                                                                                                                     6




                                                                  CIRCUITI
                                                             ELECTRONIC    E SISTEMI
                                                                        CICUITS FOR HIGH       7
                                                                                      ELETTRONICI
                                                                                         FREQUENCIES

      struttura di test necessaria alla calibrazione del modello
                                     𝑡𝑝

                                                                                ❑ Tengo conto del tempo di transizione in ingresso
      a               a               a               a                         ❑ Capacità prodotte dai transistori variano con le
                                                                                  tensioni

                                                                                ❑ Gate «a» sono quelli lungo i quali si propaga il
                                                                                  ritardo
                b              b                b               b               ❑ Gate «b» forniscono (h-1) degli h gate di carico
                                                                                  per i gate «a»
                                                                                ❑ I gate «c» servono a fare in modo che le uscite
                                                                                  dei gate «b» non commutino troppo velocemente
            c              c                c               c                     → la presenza di questi gate è necessaria per
                                                                                  rallentare il transitorio all’uscita del gate «b» che
                                                                                  per effetto Miller potrebbe comportare errori non
                                                                                  trascurabili nella stima del ritardo


  primi due stadi forniscono                        il quarto stadio
  una pendenza «realistica» dei                     fornisce      una
  fronti in ingresso al DUT                         capacità di carico
  (Device Under Test)                               «realistica»     al
                                                                                                                                     7
                                                    DUT stesso.
                                 CIRCUITI
                            ELECTRONIC    E SISTEMI
                                       CICUITS FOR HIGH       8
                                                     ELETTRONICI
                                                        FREQUENCIES

struttura di test necessaria alla calibrazione del modello




                     Circuito di test per h=2

                                                                      8




                                 CIRCUITI
                            ELECTRONIC    E SISTEMI
                                       CICUITS FOR HIGH       9
                                                     ELETTRONICI
                                                        FREQUENCIES

struttura di test necessaria alla calibrazione del modello




                                                                      9
                    Circuito di test per h=4
                                                 CIRCUITI
                                            ELECTRONIC    E SISTEMI
                                                       CICUITS FOR HIGH       10
                                                                     ELETTRONICI
                                                                        FREQUENCIES


Modello nMOS           Modello pMOS                     NMOS:              PMOS:
                                                        L=0.35u,           L=0.35u,
+VTO=-0.4 [V]       +VTO=0.4 [V]
                                                        W=0.35u,           W=0.7u,
+KP=200e-6 [A/V^2] +KP=400e-6 [A/V^2]
+GAMMA=0.5 [V^1/2] +GAMMA=0.5 [V^1/2]
+PHI=0.9 [V]        +PHI=0.9 [V]
+NSUB=6e17 [cm-3]   +NSUB=6e17 [cm-3]
+LAMBDA=0.05 [V^-1] +LAMBDA=0.05 [V^-1]
+TOX=4e-9 [m]       +TOX=4e-9 [m]                                 𝑝𝑠
+CGSO=8e-10 [F/m]   +CGSO=8e-10 [F/m]
+CGDO=8e-10 [F/m]   +CGDO=8e-10 [F/m]
+CJ=2e-3[F/m^2]     +CJ=2e-3[F/m^2]                                                    →       da
+PB=1 [V]           +PB=1 [V]                                                              simulazioni
+MJ=0.5             +MJ=0.5

                                                                                       →
                                                                                           da teoria




                                                                                                 10




                                                 CIRCUITI
                                            ELECTRONIC    E SISTEMI
                                                       CICUITS FOR HIGH       11
                                                                     ELETTRONICI
                                                                        FREQUENCIES

                           struttura di test non ottimale

                                  ❑ In questo caso 𝐶𝑜𝑢𝑡 corrisponde a 𝐶𝑖𝑛 per ℎ = 1
                                  ❑ Valori di ℎ > 1 vengono ottenuti aumentando il valore della
                                    capacità di uscita




                                  ❑ Si ottengono i seguenti valori:

                  𝑡𝑝0 ≅ 4.5𝑝𝑠 (con precedente struttura di test avevamo ottenuto 𝑡𝑝0 ≅ 12 𝑝𝑠)
                  𝑝𝑖𝑛𝑣 ≅ 1.33 (con precedente struttura di test avevamo ottenuto 𝑝𝑖𝑛𝑣 ≅ 0.75 )


𝑡𝑝0 piccolo significa poca dipendenza di 𝑡𝑝 da ℎ → dovuto al fatto che l’aumento del carico non
influisce sulla forma d’onda del fronte di ingresso (che rimane ideale)
                                                                                                 11
                                                    CIRCUITI
                                               ELECTRONIC    E SISTEMI
                                                          CICUITS FOR HIGH       12
                                                                        ELETTRONICI
                                                                           FREQUENCIES




                                Interconnessioni



                                                                                         12




                                                    CIRCUITI
                                               ELECTRONIC    E SISTEMI
                                                          CICUITS FOR HIGH       13
                                                                        ELETTRONICI
                                                                           FREQUENCIES

                                       Interconnessioni




❑ Non c’è abbastanza spazio sulla superficie del chip per
  creare le connessioni elettriche necessarie → si creano
  interconnessioni in direzione out-of-plane
❑ Circuiti integrati complessi possono avere fino a 10 o
  più layer di interconnessioni
                                                                                         13
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       14
                                                                            ELETTRONICI
                                                                               FREQUENCIES

                                           Interconnessioni




                                                                                                         14




                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       15
                                                                            ELETTRONICI
                                                                               FREQUENCIES

                     Materiali per realizzare interconnessioni
Per molti decenni: interconnessioni in alluminio
PRO:
❑ nonostante abbia conducibilità minore di Au e Cu, ha una
  minore resistenza di contatto con il silicio
❑ buona adesione su SiO2
❑ realizzabili mediante semplice evaporazione termica
  (melting point 660°C)
CONTRO:
                                                                      [from Microchip fabrication - Peter van Zant.]
❑ Se in contatto con Si, a 577°C si forma una miscela
  eutettica → può essere un problema ad esempio nel caso di
  shallow junctions
❑ Lo scaling dei transistori (e quindi delle interconnessioni) ha
  portato a problemi di elettromigrazione
   ▪ Per ridurre problemi di elettromigrazione
      ▪ → 0.5-4% Cu aggiunto ad Al
      ▪ ma per scaling molto spinto la resistività è troppo                                              15
          alta → si passa a Cu (late 1990s)
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       16
                                                                              ELETTRONICI
                                                                                 FREQUENCIES

                              Materiali per realizzare interconnessioni
Fino a circa 1990 si usava Al. All’incirca dalla generazione 180nm in poi, vista la necessità di fare
interconnessioni più vicine e più piccole per far fronte a scaling transistori, si è passati al Cu (𝜌𝐶𝑢 < 𝜌𝐴𝑙 ).

❑ Gli atomi di Cu diffondono nel silicio e deteriorano le proprietà dei MOSFET.
→ vengono introdotte diffusion barriers (solitamente TiW or TiN or TaN or metal silicides)


❑ Separazione netta, durante i
  processi produttivi dei transistori
  in: FEOL e BEOL per evitare
  contaminazioni.




                                                                                                              16




                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       17
                                                                              ELETTRONICI
                                                                                 FREQUENCIES

                          Tecniche per realizzare interconnessioni: PVD

                                                    Sputter deposition process              Magnetron sputtering
                   Thermal evaporator

                                          wafers



high vacuum
(5 × 10−5 −
1 × 10−7 mbar)
                                      evaporation
      heater                          source




                 deposition rate ~Å/sec                                   deposition rate ~nm/sec




                                                                                                              17
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       18
                                                                              ELETTRONICI
                                                                                 FREQUENCIES

                    Tecniche per realizzare interconnessioni: CVD
 Reazioni chimiche: es riduzione di esafluoruro di tungsteno
 2WF6 + 3Si → 2W + 3SiF4
 2WF6 + 3H2 → 2W + 6HF



        Tecniche per realizzare interconnessioni: Electroplating


                                                 Utilizzato solitamente per
            𝑤𝑎𝑓𝑒𝑟
                                                 interconnessioni in Cu



                                                                   yields
                                                2𝐶𝑢++ + 2𝐻2 𝑂               2𝐶𝑢 𝑠 + 𝑂2 𝑔 + 4𝐻 +
                                                                                                           18




                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       19
                                                                              ELETTRONICI
                                                                                 FREQUENCIES

                                             Interconnessioni

                                                                  𝑉𝑂𝐿𝑚𝑎𝑥 =0.1𝑉𝐷𝐷                   𝑉𝑇
                                                                                     𝑑𝑉𝑜      2𝐹
                                Fino ad ora:                                                      𝑉𝐷𝐷
                                                        𝑡𝑓 = 𝐶𝑊        න                  = 𝐶𝑊 ′        = 𝐶𝑊 𝑅𝑖𝑛𝑣
                          interconnessione come                                    𝐼𝑀𝑛 𝑉𝑜     𝛽𝑛 𝑆𝑛 𝑉𝐷𝐷
                           capacità verso massa                       𝑉𝐷𝐷




ALCUNE NOTE. Il modello implica che:
❑ Non ci sono accoppiamenti con interconnessioni circostanti
❑ Queste interconnessioni non hanno un tempo caratteristico → diminuisco 𝑡𝑝 in modo
  arbitrario diminuendo la resistenza 𝑅𝑖𝑛𝑣

Sotto opportune ipotesi: linee come combinazione di resistenze, induttanze, capacità a parametri distribuiti

                                                                                                           19
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       20
                                                                             ELETTRONICI
                                                                                FREQUENCIES

                                            Interconnessioni




                                                                                                             20




                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       21
                                                                             ELETTRONICI
                                                                                FREQUENCIES

                                            Interconnessioni
ALCUNE NOTE
❑ Scaling della tecnologia → tempi di interconnessione non sono migliorati e possono diventare preponderanti sul
  tempo di ritardo totale
❑ Accoppiamenti capacitivi tra interconnessioni → cross-talk
❑ L’alimentazione deve essere portata a tutti i circuiti → cadute di tensione resistive e induttive generano disturbi
    • Infatti linee di alimentazione connesse ai gate logici sono molto disturbate → alimentazioni parte digitale e
      analogica separate
❑ Problemi di signal integrity
❑ Interconnessioni hanno complessivamente capacità grandi → il pilotaggio richiede molta energia (es. linee di
  clock)




                                                                                                             21
                                                     CIRCUITI
                                                ELECTRONIC    E SISTEMI
                                                           CICUITS FOR HIGH       22
                                                                         ELETTRONICI
                                                                            FREQUENCIES



        Due scenari

Interconnessioni locali
𝐿𝑒𝑛 è legata a distanza tra i gate → si riduce con
lo scaling della tecnologia                            Parametro         Relazione           Int.Locale            Int,Globale
                                                         𝑊, 𝐻, 𝑡𝑑𝑖                                1Τ𝑆                 1Τ𝑆
Interconnessioni globali                                    𝐿𝑒𝑛                                   1Τ𝑆                  𝑆𝑐ℎ
                                                            𝑅𝑖𝑛𝑡              𝜌                     𝑆                𝑆 2 𝑆𝑐ℎ
Linee che si diramano lungo tutto il chip.                                       𝐿
                                                                             𝐻𝑊 𝑒𝑛
Con scaling della tecnologia i transistori sono             𝐶𝑖𝑛𝑡            𝜀𝑑𝑖                   1Τ𝑆                  𝑆𝑐ℎ
                                                                                𝑊𝐿𝑒𝑛
sempre più piccoli e le dimensioni dei chip                                 𝑡𝑑𝑖
sempre più grandi.                                           𝑡𝑤             𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡               1                𝑆 2 𝑆𝑐ℎ 2
❑ L’area dei chip (𝐴𝑐ℎ ) è aumentata                   𝑆 > 1 è il fattore di scaling dei transistori;
                                                       𝑆𝑐ℎ > 1 è il fattore di scaling legato all’area del chip;
❑ Si dimostra che in media 𝐿𝑚𝑎𝑥 ≅      𝐴𝑐ℎ /2                                                                           22




                                                     CIRCUITI
                                                ELECTRONIC    E SISTEMI
                                                           CICUITS FOR HIGH       23
                                                                         ELETTRONICI
                                                                            FREQUENCIES




                                                                                                                        23
                                                            CIRCUITI
                                                       ELECTRONIC    E SISTEMI
                                                                  CICUITS FOR HIGH       24
                                                                                ELETTRONICI
                                                                                   FREQUENCIES


Ci occuperemo per semplicità di interconnessioni isolate → no cross talk



       𝐼 𝑥       𝑟∆𝑥            𝑙∆𝑥                    𝐼 𝑥 + ∆𝑥



 𝑉 𝑥                                𝑐∆𝑥                   𝑔∆𝑥      𝑉 𝑥 + ∆𝑥



                                   ∆𝑥




                                                                                                              24




                                                            CIRCUITI
                                                       ELECTRONIC    E SISTEMI
                                                                  CICUITS FOR HIGH       25
                                                                                ELETTRONICI
                                                                                   FREQUENCIES

                                              Interconnessioni
Modello a parametri concentrati                                      Modello a parametri distribuiti
                                                            ❑ Correnti variano lungo i conduttori ed elementi circuitali.
❑ dimensioni fisiche del circuito tali che: correnti
                                                              Tensioni tra punti lungo conduttori o all’interno di
  attraverso conduttori e tensioni ai capi di
                                                              elementi circuitali variano
  conduttori non variano.
                                                            ❑ Tensioni e correnti sono funzioni del tempo e dello
❑ Tensioni e correnti sono funzioni solo del
                                                              spazio: 𝑉 𝑥, 𝑡 , 𝐼 𝑥, 𝑡
  tempo: 𝑉 𝑡 , 𝐼 𝑡
                                                            ❑ Saranno presenti equazioni differenziali alle derivate
❑ Saranno presenti equazioni differenziali alle
                                                              parziali
  derivate totali                                                                            25 𝑐𝑚
                                                                                        𝑅𝑠


                                                                                                             𝑅𝐿 = ∞


                                                                𝑓 = 300𝑀𝐻𝑧

                                                                     𝑐   3 × 108
                                                                λ=     =         = 1𝑚
                                                                     𝑓 300 × 106
                                                                                                              25
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       26
                                                                             ELETTRONICI
                                                                                FREQUENCIES

                                           Interconnessioni


❑ Ci sono linee che a causa della resistività del
  materiale e sezioni molto piccole → hanno                            Linee dispersive RC
  resistenza per unità di lunghezza molto alta
  che domina sulle componenti induttive



❑ Ci sono linee dove a causa dell’alta conducibilità
  e grande sezione → dominano effetti induttivi                        Linee senza perdite




                                                                                                             26




                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       27
                                                                             ELETTRONICI
                                                                                FREQUENCIES

                                        Linee dispersive RC
         𝑟∆𝑥          𝑙∆𝑥
                                                         𝑉𝑟 = 𝐼 𝑥 𝑟∆𝑥
                                                                     𝑑𝐼 𝑥
                            𝑐∆𝑥                           𝑉𝑙 = 𝑙∆𝑥
                                                                      𝑑𝑡

                                                         ❑ Supponiamo      che     la    corrente   cresca
                                                           linearmente da 0 a 𝐼0 in un tempo 𝜏.


                                                    𝐼0


                                                                                𝑑𝐼 𝑥   𝐼0                       𝐼0
                                                                                     =               𝑉𝑙 ≅ 𝑙∆𝑥
                                                                                 𝑑𝑡     𝜏                        𝜏

                                                                                             𝑡
                                                                   𝜏                                         27
                                                            CIRCUITI
                                                       ELECTRONIC    E SISTEMI
                                                                  CICUITS FOR HIGH       28
                                                                                ELETTRONICI
                                                                                   FREQUENCIES


                                               𝐼0
      Se 𝑉𝑙 ≪ 𝑉𝑟 :                       𝑙∆𝑥      ≪ 𝑟∆𝑥𝐼0               𝑙 ≪ 𝑟𝜏
                                                𝜏

      ❑ Se abbiamo a che fare con linee tanto resistive e poco induttive pilotate in un tempo sufficientemente alto
        → possiamo considerare soddisfatta 𝑙 ≪ 𝑟𝜏



      𝐼 𝑥         𝑟∆𝑥               𝐼 𝑥 + ∆𝑥
                                                                       𝑅𝑖𝑛𝑡 = 𝑟𝐿𝑒𝑛       resistenza della linea

𝑉 𝑥                     𝑐∆𝑥                     𝑉 𝑥 + ∆𝑥               𝐶𝑖𝑛𝑡 = 𝑐𝐿𝑒𝑛       capacità della linea




                         ∆𝑥


                                                                                                                  28




                                                            CIRCUITI
                                                       ELECTRONIC    E SISTEMI
                                                                  CICUITS FOR HIGH       29
                                                                                ELETTRONICI
                                                                                   FREQUENCIES

                     Capacità e Resistenza dell’interconnessione
                                                                    𝜀𝑑𝑖
                                                           𝐶𝑖𝑛𝑡 =       𝑊𝐿𝑒𝑛 = 𝑐𝑝𝑝 𝐿𝑒𝑛
                                                                    𝑡𝑑𝑖
                                                                                     𝑐𝑝𝑝 parallel plate capacitance
            𝐿𝑒𝑛

                                                                            𝜌          𝐿𝑒𝑛
 𝐻                                                         𝑅𝑖𝑛𝑡 = 𝑟𝐿𝑒𝑛 =      𝐿𝑒𝑛 = 𝑅□
                                                                           𝐻𝑊          𝑊
                              𝑡𝑑𝑖                                                    𝑅□ : resistenza per quadro: è la
                  𝑊                                                                  resistenza di una linea quadrata con
                                                                                     𝑊 = 𝐿𝑒𝑛 , con resistività 𝜌 e spessore
                                                                                     𝐻




                                                                                                                  29
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       30
                                                                           ELETTRONICI
                                                                              FREQUENCIES

              Effetto pelle: è rilevante per le nostre applicazioni?
                                                    𝜌
Se abbiamo densità di correnti uniformi →     𝑟=
                                                   𝐻𝑊

A frequenze alte diventa rilevante l’effetto pelle → la corrente non sarà uniforme nella sezione del conduttore




                                                                                →
                                                               diminuisce esponenzialmente                  𝑑
                                                                                                        −
                                                               allontanandosi dall’interfaccia   𝐽 = 𝐽0 𝑒 𝛿

                                                                                                  𝜌
    esempio                                                        spessore efficace    𝛿=
                                                                                                 𝜋𝜇𝑓
    𝜌𝐴𝑙 = 2.7 𝜇Ω/𝑐𝑚
                        → 𝛿 = 2.6𝜇𝑚
    𝑓 = 1𝐺𝐻𝑧


    𝛿 grande rispetto alle dimensioni della sezione di una interconnessione
                         → possiamo trascurare effetto pelle
                                                                                                                30




                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       31
                                                                           ELETTRONICI
                                                                              FREQUENCIES

                           Capacità dell’interconnessione


        𝐿𝑒𝑛


𝐻
                                               modello non molto
                                                  accurato!!
               𝑊         𝑡𝑑𝑖




                                si vede come per tecnologie molto
                                scalate si ha che H>>W dunque
                                dobbiamo includere fringing effects
                                                                                                                31
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       32
                                                                           ELETTRONICI
                                                                              FREQUENCIES

                        Capacità dell’interconnessione
              𝑊

          𝐻                                                𝜀𝑑𝑖
                                                   𝑐𝑝𝑝 =       𝑊
                                                           𝑡𝑑𝑖
                         𝑡𝑑𝑖                                                 𝐶𝑖𝑛𝑡
                                                                        𝑐=        = 𝑐𝑝𝑝 + 𝑐𝑓𝑟
                                                                              𝐿

                                                                                         𝑊       2𝜋
                                                                                 = 𝜀𝑑𝑖      +
                                                        2𝜋                               𝑡𝑑𝑖 𝑙𝑛 4𝑡𝑑𝑖 + 𝐻
                                   𝑐𝑓𝑟 = 𝜀𝑑𝑖                                                       𝐻
                                                         2𝑡𝑑𝑖 + 𝐻
          𝐻                                      cosh−1
                                                            𝐻
                               se 𝑡𝑑𝑖 >> 𝐻

                  𝑡𝑑𝑖                                2𝜋
                                         = 𝜀𝑑𝑖
                                                    4𝑡𝑑𝑖 + 𝐻
                                                 𝑙𝑛
                                                       𝐻
                                                                                                     32




                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       33
                                                                           ELETTRONICI
                                                                              FREQUENCIES

                        Capacità dell’interconnessione
          𝑊       2𝜋                                 se W diminuisce, 𝑐 può essere dominata da 𝑐𝑓𝑟
𝑐 = 𝜀𝑑𝑖      +
          𝑡𝑑𝑖 𝑙𝑛 4𝑡𝑑𝑖 + 𝐻
                    𝐻




                                                                              𝜀𝑑𝑖 = 𝜀𝑆𝑖𝑂2 = 3.9



                                                                                                     33
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       34
                                                                           ELETTRONICI
                                                                              FREQUENCIES

All’aumentare dello scaling, le interconnessioni saranno più vicine → ci sarà una capacità inter-wire: 𝑐𝑖𝑤




                                                                     supponiamo che 𝑊 ed 𝑆 diminuiscono
                                                                     mantenendo costante il rapporto 𝐻/𝑇𝑑𝑖




                                                                                                             34




                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       35
                                                                           ELETTRONICI
                                                                              FREQUENCIES

esempio
                                                     values for typical 0.25 μm        Supponiamo di avere una linea
                                                     CMOS process. The table rows      di clock in Al che si estende per
                                                     represent the top plate of the    10cm di larghezza 1μm che
                                                     capacitor, the columns the        giace sul primo layer di
                                                     bottom    plate.  The      area   metalizzazione in alluminio
                                                     capacitances are expressed in
                                                     aF/μm2,    while  the    fringe
                                                     capacitances (given in the
                                                     shaded rows) are in aF/μm
                                                     [Rabaey-Digital     Integrated
                                                     Circuits]



                                                     Inter-wire capacitance per
                                                     unit wire length for different
                                                     interconnect layers of typical
                                                     0.25 μm CMOS process.
                                                     The capacitances are
                                                     expressed in aF/μm, and are
                                                     for minimally-spaced wire
                                                                                                             35
                                                      CIRCUITI
                                                 ELECTRONIC    E SISTEMI
                                                            CICUITS FOR HIGH       36
                                                                          ELETTRONICI
                                                                             FREQUENCIES

                         Resistenza dell’interconnessione
            𝐿𝑒𝑛                                                             𝜌          𝐿𝑒𝑛
                                                           𝑅𝑖𝑛𝑡 = 𝑟𝐿𝑒𝑛 =      𝐿𝑒𝑛 = 𝑅□
                                                                           𝐻𝑊          𝑊

    𝐻                                                        𝑅□ : resistenza per quadro: è la resistenza di una
                                                             linea quadrata con 𝑊 = 𝐿𝑒𝑛 , con resistività 𝜌 e
                  𝑊            𝑡𝑑𝑖                           spessore 𝐻




                                                                                                         36




                                                      CIRCUITI
                                                 ELECTRONIC    E SISTEMI
                                                            CICUITS FOR HIGH       37
                                                                          ELETTRONICI
                                                                             FREQUENCIES

esempio
Supponiamo di avere una linea di clock in Al che si estende per 10cm di larghezza 1μm che giace sul primo layer di
metalizzazione.




                                                                                                         37
                                                              CIRCUITI
                                                         ELECTRONIC    E SISTEMI
                                                                    CICUITS FOR HIGH       38
                                                                                  ELETTRONICI
                                                                                     FREQUENCIES

                           Ritardo intrinseco dell’interconnessione
       𝐼 𝑥     𝑟∆𝑥                  𝐼 𝑥 + ∆𝑥                            𝑉 𝑥, 𝑡 = 𝑉 𝑥 + ∆𝑥, 𝑡 + 𝐼 𝑥, 𝑡 𝑟∆𝑥
                                                                    ቐ                           𝜕𝑉 𝑥 + ∆𝑥, 𝑡
                                                                     𝐼 𝑥, 𝑡 = 𝐼 𝑥 + ∆𝑥, 𝑡 + 𝑐∆𝑥
                                                                                                      𝜕𝑡
𝑉 𝑥                   𝑐∆𝑥                           𝑉 𝑥 + ∆𝑥




                                                                                          →
                                                                        𝑉 𝑥 + ∆𝑥, 𝑡 − 𝑉 𝑥, 𝑡
                                                                                             = −𝑟𝐼 𝑥, 𝑡
                                                                                 ∆𝑥
                          ∆𝑥                                         𝐼 𝑥 + ∆𝑥, 𝑡 − 𝐼 𝑥, 𝑡      𝜕𝑉 𝑥 + ∆𝑥, 𝑡
                                                                                          = −𝑐
                                                                             ∆𝑥                     𝜕𝑡
 se ∆𝑥 → 0

  𝜕𝑉 𝑥, 𝑡
           = −𝑟𝐼 𝑥, 𝑡
    𝜕𝑥
 𝜕𝐼 𝑥, 𝑡       𝜕𝑉 𝑥, 𝑡
          = −𝑐
   𝜕𝑥            𝜕𝑡
                                                                                                                38




                                                              CIRCUITI
                                                         ELECTRONIC    E SISTEMI
                                                                    CICUITS FOR HIGH       39
                                                                                  ELETTRONICI
                                                                                     FREQUENCIES

                           Ritardo intrinseco dell’interconnessione
   𝜕𝑉 𝑥, 𝑡
            = −𝑟𝐼 𝑥, 𝑡
     𝜕𝑥                            ricaviamo           𝜕 2 𝑉 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡
  𝜕𝐼 𝑥, 𝑡       𝜕𝑉 𝑥, 𝑡                                       2   = 𝑟𝑐           Equazione di diffusione
           = −𝑐                                            𝜕𝑥            𝜕𝑡
    𝜕𝑥            𝜕𝑡
                                                       Analoga a quella della diffusione del calore.
 𝑉𝑖𝑛              𝑉𝑜𝑢𝑡                                 Usata per descrivere la variazione della concentrazione di
                                                       una certa quantità (es: materia, momento, energia) all’interno
                     simbolo per rete distribuita      di una specifica regione rispetto a variazioni spaziali e
                                                       temporali)



Per studiare questo sistema dobbiamo imporre dei vincoli:
❑ Condizione iniziale: Linea scarica   → 𝑉 𝑥, 0 = 0 ∀𝑥 > 0                          dobbiamo trovare
                                                                                                       𝑉 𝑥, 𝑡 𝑝𝑒𝑟 t>0
❑ Condizioni al contorno per x=0,L:                   → 𝑉 0, 𝑡 = 𝑉𝑖𝑛 𝑡 ∀ 𝑡 > 0
                                                      → I 𝐿, 𝑡 = 0 ∀ 𝑡 > 0                                      39
                                                                    CIRCUITI
                                                               ELECTRONIC    E SISTEMI
                                                                          CICUITS FOR HIGH       40
                                                                                        ELETTRONICI
                                                                                           FREQUENCIES

                                 Ritardo intrinseco dell’interconnessione
                                                                                                         notazione:
𝜕 2 𝑉 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡             Sfruttiamo la trasformata di Laplace                                    𝑉ෘ 𝑥, 𝑠 indica la trasformata di
       2
           = 𝑟𝑐
    𝜕𝑥            𝜕𝑡                                                          𝜕 2 𝑉ෘ 𝑥, 𝑠
                                                                                                            Laplace di 𝑉 𝑥, 𝑡 . con 𝑠 ∈ ℂ
                                         𝑟𝑐 𝑠𝑉ෘ 𝑥, 𝑠 − 𝑉 𝑥, 0−          =
                                                                                 𝜕𝑥 2
                                                                   condizione iniziale: rete scarica quindi 𝑉 𝑥, 0− = 0

                                                                𝜕 2 𝑉ෘ 𝑥, 𝑠
                                                 𝑟𝑐𝑠𝑉ෘ 𝑥, 𝑠 =
                                                                     𝜕𝑥 2
                                                                   soluzione generale


                                        𝑉ෘ 𝑥, 𝑠 = 𝐴 𝑠 𝑒 𝑥 𝑟𝑐𝑠 + 𝐵 𝑠 𝑒 −𝑥 𝑟𝑐𝑠


                  𝜕𝑉 𝑥, 𝑡
 ricordando che           = − 𝑟𝐼 𝑥, 𝑡
                    𝜕𝑥
 possiamo scrivere                              1 𝜕𝑉ෘ 𝑥, 𝑠      𝑠𝑐                𝑠𝑐
 l’espressione per la corrente    𝐼ሙ 𝑥, 𝑠 = −              =       𝐵 𝑠 𝑒 −𝑥 𝑟𝑐𝑠 −    𝐴 𝑠 𝑒 +𝑥 𝑟𝑐𝑠
                                                𝑟 𝜕𝑥            𝑟                 𝑟
                                                                                                                                  40




                                                                    CIRCUITI
                                                               ELECTRONIC    E SISTEMI
                                                                          CICUITS FOR HIGH       41
                                                                                        ELETTRONICI
                                                                                           FREQUENCIES

                                 Ritardo intrinseco dell’interconnessione
❑ Abbiamo bisogno di 2 condizioni al contorno:

BC1:         𝑉 0, 𝑡 = 𝑉𝑖𝑛 𝑡 ∀𝑡 > 0

             𝐼ሙ 𝐿, 𝑠
BC2:                 = 𝑌ෘ 𝐿, 𝑠     : ammettenza di un generico carico
            𝑉ෘ 𝐿, 𝑠

Applicando BC1 e BC2 scriviamo

𝑉ෘ 0, 𝑠 = 𝐴 𝑠 + 𝐵 𝑠
                                                                    risolvendo per 𝐴 𝑠 e 𝐵 𝑠 e inserendo le soluzioni
               𝑠𝐶𝑖𝑛𝑡 𝐵 𝑠 𝑒 − 𝑟𝑐𝑠 − 𝐴 𝑠 𝑒 + 𝑟𝑐𝑠
𝑌ෘ 𝐿, 𝑠 =                                                           nell’espressione per il potenziale scriviamo
               𝑅𝑖𝑛𝑡 𝐵 𝑠 𝑒 − 𝑟𝑐𝑠 + 𝐴 𝑠 𝑒 + 𝑟𝑐𝑠
                                                                                                                 𝑁(𝑠)
                                                                                            𝑉ෘ 𝑥, 𝑠 = 𝑉ේ
                                                                                                       𝑖𝑛 0, 𝑠
                                                                                                                 𝐷(𝑠)
                                                                                                                                  41
                                                                CIRCUITI
                                                           ELECTRONIC    E SISTEMI
                                                                      CICUITS FOR HIGH       42
                                                                                    ELETTRONICI
                                                                                       FREQUENCIES

                           Ritardo intrinseco dell’interconnessione
                         𝑁(𝑠)                           𝑠𝐶𝑖𝑛𝑡              𝑥                                      𝑥
    𝑉ෘ 𝑥, 𝑠 = 𝑉ේ
               𝑖𝑛 0, 𝑠            dove        𝑁 𝑠 =           cosh    1−        𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 + 𝑌 𝐿, 𝑠 sinh     1−       𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                         𝐷(𝑠)                           𝑅𝑖𝑛𝑡               𝐿                                      𝐿


                                                        𝑠𝐶𝑖𝑛𝑡
                                              𝐷 𝑠 =           cosh    𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 + 𝑌 𝐿, 𝑠 sinh    𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                                        𝑅𝑖𝑛𝑡

                                                 1
Nel caso specifico di input a gradino 𝑉ේ
                                       𝑖𝑛 0, 𝑠 =   e di ammettenza 𝑌 𝐿, 𝑠 = 0 (linea di lunghezza L
                                                                  𝑠
senza carico connesso in x=L) e scriviamo
                                                                      𝑥
                                                           1 cosh 1 − 𝐿 𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                                 𝑉ෘ 𝑥, 𝑠 =
                                                           𝑠     cosh 𝑠𝑅 𝐶     𝑖𝑛𝑡 𝑖𝑛𝑡


 E dunque, nel caso particolare di x = 𝐿:
                                                                           1
                                                      𝑉ෘ 𝐿, 𝑠 =                                                         42
                                                                  𝑠 cosh   𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡




                                                                CIRCUITI
                                                           ELECTRONIC    E SISTEMI
                                                                      CICUITS FOR HIGH       43
                                                                                    ELETTRONICI
                                                                                       FREQUENCIES


Ci sono delle soluzioni approssimate dell’equazione differenziale per x = 𝐿 come ad esempio:


                                                      𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡                           𝑡 < 0.1𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                       𝑉0 𝑒𝑟𝑓𝑐
                         𝑉 𝐿𝑒𝑛 , 𝑡 =                     4𝑡
                                                         −2.536𝑡           −9.4641𝑡       𝑡 > 0.1𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                         𝑉0   1 − 1.366𝑒 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 + 0.366𝑒 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡


                         2 𝑥 −𝑦2
dove 𝑒𝑟𝑓𝑐 𝑥 = 1 −          න 𝑒   𝑑𝑦           error-function
                          𝜋 0                 complementare


per avere un’escursione del 9 % ad una distanza 𝐿𝑒𝑛 dall’inizio
delle linea dove viene applicato il gradino di tensione, deve
passare un tempo pari a


                            𝑡 = 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                                                                                                        43
                                                                                                                         CIRCUITI
                                                                                                                    ELECTRONIC    E SISTEMI
                                                                                                                               CICUITS FOR HIGH       44
                                                                                                                                             ELETTRONICI
                                                                                                                                                FREQUENCIES

                                                             Ritardo intrinseco dell’interconnessione
         Soluzione più generale ∀𝑥 con input a gradino
                                                                                                                                         Si nota la presenza di:
                                                      𝑥
                                  1 cosh            1−𝐿                𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                                                                                                                         ❑ polo semplice in 𝑠0 = 0
            𝑉 𝑥, 𝑠 =
                                  𝑠     cosh                  𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡                                                                 ❑ infiniti poli semplici (radici di cosh                                            𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 = 0)
                                                                                                                                                in 𝑠𝑘 = −𝑝𝑘 / 𝑅𝐶 per ogni intero 𝑘 ≥ 1

                                                                                                                                                       2𝑘 − 1 2 𝜋 2         𝑘≥1
                                                                                                                                                      𝑝𝑘 =
          maggiori informazioni in:                                                                                                                        4
         [Vasant B. Rao, "Delay Analysis of the Distributed RC                                                                          I residui corrispondenti a ogni polo sono 𝜌0 = 1
         Line", 32nd Design Automation Conference, 1995]
                                                                                                                                                                    𝑥         𝜋
                                                                                                                                                     −4 cos 1 − 𝐿 2𝑘 − 1 2
                                                                                                                                        e 𝜌 (𝑥) =                                   per 𝑘 ≥ 1
                                                                                                                                             𝑘
                                                                                                                                                      2𝑘 − 1 𝜋 sin 2𝑘 − 1 𝜋Τ2
                                                                                                                                                                                               soluzione nel dominio del tempo
                                     ∞                                                                                                                                                  ∞
                                           4 sin 𝑘 − 1Τ2 𝜋 𝑥 Τ𝐿 − 4𝑅 𝐶                            2𝑘−1 2 𝜋2 𝑡
    𝑣 𝑥, 𝑡 = 1 − ෍                                              𝑒   𝑖𝑛𝑡 𝑖𝑛𝑡                                                                                𝑣 𝑥, 𝑡 = 1 + ෍ 𝜌𝑘 𝑥 𝑒 𝑠𝑘 𝑡
                                                 2𝑘 − 1 𝜋
                                     𝑘=1                                                                                            𝜋                                                   𝑘=1
                                                                                                                 sin     2𝑘 − 1       = −1 𝑘+1                                                                                              44
                                                                                                                                    2




                                                                                                                         CIRCUITI
                                                                                                                    ELECTRONIC    E SISTEMI
                                                                                                                               CICUITS FOR HIGH       45
                                                                                                                                             ELETTRONICI
                                                                                                                                                FREQUENCIES
                                                                                          B=u; % update the right-hand-side
clear all                                                                                                                                                                           %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                                                                                %==================================                                                 %                 METHOD 3: approximated-analytic solution                %
%--------------------------------------------------------------------------                     figure(1)                                                                           %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Input data                                                                                    subplot(2,1,1);
Len=0.1; % interconnection length (m)                                                           plot(x,u);                                                                          OutputVoltage_ApproxAnalytic=zeros(size(t));
T=200e-9;    % simulation time (s)                                                              xlabel('x [m]');                                                                    for i=1:numel(t)
                                                                                                axis ([0 Len 0 V0*1.1]);                                                                if t(i)<0.1*R*C
dx=1e-3;   % space discretization step                                                          TimStamp=['t=',num2str(t(i),'%2.3e\n'),'s'];                                                OutputVoltage_ApproxAnalytic(i)=2*V0*erfc(sqrt(R*C/(4*t(i))));
dt=1.5e-10; % time discretization step                                                          ylabel('V(x) [V]')                                                                      elseif t(i)>=0.1*(R*C)
                                                                                                title(TimStamp);                                                                    OutputVoltage_ApproxAnalytic(i)=...
r=0.075; % resistance per unit width (Ohm/um)                                                                                                                                                   V0*(1-1.366*exp(-2.536*t(i)/(R*C))+0.366*exp(-9.4641*t(i)/(R*C)));
c=110;   % capacitance per unit width (aF/um)                                                   %==================================                                                         %     else
                                                                                                OutputVoltage_Euler(i)=u(end); % save the voltage value at the end of                       %         V(i)=0.31;
V0= 1;    % voltage step amplitude                                                              % transmission the line                                                                 end
                                                                                                                                                                                    end
%--------------------------------------------------------------------------                     subplot(2,1,2);                                                                     figure(2)
% convert into MKS units                                                                        plot(t,OutputVoltage_Euler);                                                        plot(t,OutputVoltage_ApproxAnalytic,'b','linewidth',2);
r=r/1e-6;                                                                                       xlabel('t [s]');
c=c*1e-18/1e-6;                                                                                 ylabel('Vout(x=L_e_n) [V]');
                                                                                                axis ([0 T 0 V0*1.1]);                                                              legend('Fully numeric','Semi Analytical ','Approx. Analytical');
% calculate space and time domain                                                               shg
x=0:dx:Len;                                                                                     drawnow
t=0:dt:T;                                                                                 end

                                                                                          %==================================
                                                                                          figure(2)
                                                                                                                                                                                        supponiamo      di  avere    una
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%            METHOD 1: fully numeric - BACKWARD EULER METHOD              %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                                                                          plot(t,OutputVoltage_Euler,'k','linewidth',2);
                                                                                          hold on
                                                                                          shg
                                                                                                                                                                                        interconnessione in Al realizzata
%% ************************************************************************
                                                                                          legend('Fully numeric');
                                                                                          xlabel('t [s]');                                                                              sulla prima metallizzazione di
% determine entries for the matrix used for Backward Euler scheme                         ylabel('Vout(x=L_e_n) [V]');

F=1/(r*c)*dt/(dx^2);
                                                                                                                                                                                        larghezza 1μm
Diagonal   = diag((1+2*F)*ones(numel(x),1));    %inserisci elementi diagonali             %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
UpDiagon   = diag(-F*ones(numel(x)-1,1),1);
DownDiagon = diag(-F*ones(numel(x)-1,1),-1);
                                                %inserisci elementi sopra-diagonale
                                                %inserisci elementi sotto-diagonale
                                                                                          %                      METHOD 2: semi-analytic solution                   %
                                                                                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                    𝑐 = 𝑊 × 30 + 2 × 40 𝑎𝐹/𝜇𝑚
M=Diagonal+UpDiagon+DownDiagon;                                                           R=r*Len;

%--------------------------------------------------------------------------
% set bounday conditions
                                                                                          C=c*Len;

                                                                                          index_summation=5;
                                                                                                                                                                                         𝑟 = 0.075/𝑊Ω/𝜇𝑚
% (For Dirichlet BC: 1 coefficient in position (1,1)                                      functionTosum=zeros(numel(x), numel(t));
M(1,:)=0; % delete all entries in the first row                                           figure(3)
M(1,1)=1; % place the coefficient                                                         plot(t,OutputVoltage_Euler,'k','linewidth',4);
                                                                                          hold on
% (For Neumann BC: (three points first derivative) dv/dx=[3*v(x)-4v(x-h)+v(x-2*h)]/(2*h)) xlabel('t [s]');
M(end,:)=0; % delete all entries in the first row                                         ylabel('Vout(x=L_e_n) [V]');
M(end,end)=3;    % place the coefficient                                                  for k=1:index_summation
M(end,end-1)=-4; % place the coefficient
M(end,end-2)=+1; % place the coefficient                                                      temp=transpose(4*sin((k-1/2)*pi*x/Len)/((2*k-1)*pi))*exp(-((2*k-1)^2*pi^2.*t)/(4*R*C));
                                                                                              functionTosum=functionTosum+temp;
%--------------------------------------------------------------------------                   OutputVoltage_SemiAnalytic=1-functionTosum;
% set initial condition                                                                       pause(3)
B=zeros(numel(x),1);                                                                          plot(t,OutputVoltage_SemiAnalytic(end,:),'r','linewidth',2);
B(1)=1;                                                                                       title(['Summation index k=',num2str(k)])
                                                                                              shg
%--------------------------------------------------------------------------                   drawnow
OutputVoltage_Euler=nan(size(t));                                                         end

for i=1:numel(t)
    % force Boundary Conditions                                                           figure(2)
    B(1)=V0;
    B(end)=0;
                                                                                          plot(t,OutputVoltage_SemiAnalytic(end,:),'r','linewidth',2);
                                                                                          hold on
                                                                                                                                                                                                                                            45
    %---------------------------------
    u=M\B; %solve linear system                                                           legend('Fully numeric','Semi Analytical ');
    %---------------------------------
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       46
                                                                            ELETTRONICI
                                                                               FREQUENCIES


                                                                     90% → 1.0𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 = 82.5𝑛𝑠




                                                                     50% → 0.38𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 = 31.4𝑛𝑠




               31.4ns          82.5ns




 Per una rete RC a parametri concentrati, il ritardo per un’escursione del segnale in uscita da       a9 %
                                          non vale 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 ‼
                                                                                                             46




                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       47
                                                                            ELETTRONICI
                                                                               FREQUENCIES


                     𝑅𝑖𝑛𝑡
                                                                                         𝑡
                                                                                     −
                                                                 𝑉𝑜𝑢𝑡 = 𝑉0 1 − 𝑒 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡

        𝑉0                           𝐶𝑖𝑛𝑡          𝑉𝑜𝑢𝑡                          se vogliamo 𝑉𝑜𝑢𝑡 =90%


                                                                 𝑡 = 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 ln 10 ≅ 2.3𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡


Per avere la stessa escursione di 𝑉𝑜𝑢𝑡 nel circuito a parametri concentrati, serve un tempo pari a

                                                       𝑡 = 2.3𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡


❑ La linea a parametri distribuiti è più veloce di quella a parametri concentrati!

E’ un risultato atteso visto che, preso un punto x tra e 𝐿𝑒𝑛 , se guardo verso la sorgente vedo una resistenza
< 𝑅𝑖𝑛𝑡 → questo vuol dire transitorio più veloce rispetto al circuito a parametri concentrati

                                                                                                             47
                                                              CIRCUITI
                                                         ELECTRONIC    E SISTEMI
                                                                    CICUITS FOR HIGH       1
                                                                                  ELETTRONICI
                                                                                     FREQUENCIES

                           Ritardo intrinseco dell’interconnessione
       𝐼 𝑥     𝑟∆𝑥                  𝐼 𝑥 + ∆𝑥                               𝑉 𝑥, 𝑡 = 𝑉 𝑥 + ∆𝑥, 𝑡 + 𝐼 𝑥, 𝑡 𝑟∆𝑥
                                                                    ൞                              𝜕𝑉 𝑥 + ∆𝑥, 𝑡
                                                                        𝐼 𝑥, 𝑡 = 𝐼 𝑥 + ∆𝑥, 𝑡 + 𝑐∆𝑥
                                                                                                         𝜕𝑡
𝑉 𝑥                   𝑐∆𝑥                           𝑉 𝑥 + ∆𝑥




                                                                                             →
                                                                        𝑉 𝑥 + ∆𝑥, 𝑡 − 𝑉 𝑥, 𝑡
                                                                                             = −𝑟𝐼 𝑥, 𝑡
                                                                                 ∆𝑥
                          ∆𝑥                                         𝐼 𝑥 + ∆𝑥, 𝑡 − 𝐼 𝑥, 𝑡      𝜕𝑉 𝑥 + ∆𝑥, 𝑡
                                                                                          = −𝑐
                                                                             ∆𝑥                     𝜕𝑡
 se ∆𝑥 → 0

  𝜕𝑉 𝑥, 𝑡
           = −𝑟𝐼 𝑥, 𝑡
    𝜕𝑥
 𝜕𝐼 𝑥, 𝑡       𝜕𝑉 𝑥, 𝑡
          = −𝑐
   𝜕𝑥            𝜕𝑡
                                                                                                                    1




                                                              CIRCUITI
                                                         ELECTRONIC    E SISTEMI
                                                                    CICUITS FOR HIGH       2
                                                                                  ELETTRONICI
                                                                                     FREQUENCIES

                           Ritardo intrinseco dell’interconnessione
   𝜕𝑉 𝑥, 𝑡
            = −𝑟𝐼 𝑥, 𝑡
     𝜕𝑥                            ricaviamo           𝜕 2 𝑉 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡
  𝜕𝐼 𝑥, 𝑡       𝜕𝑉 𝑥, 𝑡                                       2   = 𝑟𝑐              Equazione di diffusione
           = −𝑐                                            𝜕𝑥            𝜕𝑡
    𝜕𝑥            𝜕𝑡
                                                       Analoga a quella della diffusione del calore.
 𝑉𝑖𝑛              𝑉𝑜𝑢𝑡                                 Usata per descrivere la variazione della concentrazione di
                                                       una certa quantità (es: materia, momento, energia) all’interno
                     simbolo per rete distribuita      di una specifica regione rispetto a variazioni spaziali e
                                                       temporali)



Per studiare questo sistema dobbiamo imporre dei vincoli:
❑ Condizione iniziale: Linea scarica   → 𝑉 𝑥, 0 = 0 ∀𝑥 > 0                             dobbiamo trovare
                                                                                                          𝑉 𝑥, 𝑡 𝑝𝑒𝑟 t>0
❑ Condizioni al contorno per x=0,L:                   → 𝑉 0, 𝑡 = 𝑉𝑖𝑛 𝑡 ∀ 𝑡 > 0
                                                      → I 𝐿, 𝑡 = 0 ∀ 𝑡 > 0                                          2
                                                                    CIRCUITI
                                                               ELECTRONIC    E SISTEMI
                                                                          CICUITS FOR HIGH       3
                                                                                        ELETTRONICI
                                                                                           FREQUENCIES

                                 Ritardo intrinseco dell’interconnessione
                                                                                                         notazione:
𝜕 2 𝑉 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡             Sfruttiamo la trasformata di Laplace                                      𝑉ෘ 𝑥, 𝑠 indica la trasformata di
       2
           = 𝑟𝑐
    𝜕𝑥            𝜕𝑡                                                          𝜕 2 𝑉ෘ 𝑥, 𝑠
                                                                                                              Laplace di 𝑉 𝑥, 𝑡 . con 𝑠 ∈ ℂ
                                         𝑟𝑐 𝑠𝑉ෘ 𝑥, 𝑠 − 𝑉 𝑥, 0−          =
                                                                                 𝜕𝑥 2
                                                                   condizione iniziale: rete scarica quindi 𝑉 𝑥, 0− = 0

                                                                𝜕 2 𝑉ෘ 𝑥, 𝑠
                                                 𝑟𝑐𝑠𝑉ෘ 𝑥, 𝑠 =
                                                                     𝜕𝑥 2
                                                                   soluzione generale


                                        𝑉ෘ 𝑥, 𝑠 = 𝐴 𝑠 𝑒 𝑥 𝑟𝑐𝑠 + 𝐵 𝑠 𝑒 −𝑥 𝑟𝑐𝑠


                  𝜕𝑉 𝑥, 𝑡
 ricordando che           = − 𝑟𝐼 𝑥, 𝑡
                    𝜕𝑥
 possiamo scrivere                              1 𝜕𝑉ෘ 𝑥, 𝑠      𝑠𝑐                𝑠𝑐
 l’espressione per la corrente    𝐼ሙ 𝑥, 𝑠 = −              =       𝐵 𝑠 𝑒 −𝑥 𝑟𝑐𝑠 −    𝐴 𝑠 𝑒 +𝑥 𝑟𝑐𝑠
                                                𝑟 𝜕𝑥            𝑟                 𝑟
                                                                                                                                      3




                                                                    CIRCUITI
                                                               ELECTRONIC    E SISTEMI
                                                                          CICUITS FOR HIGH       4
                                                                                        ELETTRONICI
                                                                                           FREQUENCIES

                                 Ritardo intrinseco dell’interconnessione
❑ Abbiamo bisogno di 2 condizioni al contorno:

BC1:         𝑉 0, 𝑡 = 𝑉𝑖𝑛 𝑡 ∀𝑡 > 0

             𝐼ሙ 𝐿, 𝑠
BC2:                 = 𝑌ෘ 𝐿, 𝑠     : ammettenza di un generico carico
            𝑉ෘ 𝐿, 𝑠

Applicando BC1 e BC2 scriviamo

𝑉ෘ 0, 𝑠 = 𝑉ේ
           𝑖𝑛 𝑠 = 𝐴 𝑠 + 𝐵 𝑠
                                                                    risolvendo per 𝐴 𝑠 e 𝐵 𝑠 e inserendo le soluzioni
               𝑠𝐶𝑖𝑛𝑡 𝐵 𝑠 𝑒 − 𝑟𝑐𝑠 − 𝐴 𝑠 𝑒 + 𝑟𝑐𝑠
 𝑌ෘ 𝐿, 𝑠 =                                                          nell’espressione per il potenziale scriviamo
               𝑅𝑖𝑛𝑡 𝐵 𝑠 𝑒 − 𝑟𝑐𝑠 + 𝐴 𝑠 𝑒 + 𝑟𝑐𝑠
                                                                                                              𝑁(𝑠)
                                                                                            𝑉ෘ 𝑥, 𝑠 = 𝑉ේ
                                                                                                       𝑖𝑛 𝑠
                                                                                                              𝐷(𝑠)
                                                                                                                                      4
                                                                CIRCUITI
                                                           ELECTRONIC    E SISTEMI
                                                                      CICUITS FOR HIGH       5
                                                                                    ELETTRONICI
                                                                                       FREQUENCIES

                         Ritardo intrinseco dell’interconnessione
                      𝑁(𝑠)                               𝑠𝐶𝑖𝑛𝑡               𝑥                                        𝑥
    𝑉ෘ 𝑥, 𝑠 = 𝑉ේ
               𝑖𝑛 𝑠                dove       𝑁 𝑠 =            cosh     1−        𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 + 𝑌 𝐿, 𝑠 sinh       1−       𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                      𝐷(𝑠)                               𝑅𝑖𝑛𝑡                𝐿                                        𝐿


                                                         𝑠𝐶𝑖𝑛𝑡
                                              𝐷 𝑠 =            cosh     𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 + 𝑌 𝐿, 𝑠 sinh    𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                                         𝑅𝑖𝑛𝑡

                                              1
Nel caso specifico di input a gradino 𝑉ේ
                                       𝑖𝑛 𝑠 =   e di ammettenza ෙ𝑌 𝐿, 𝑠 = 0 (linea di lunghezza L
                                                                𝑠
senza carico connesso in x=L) scriviamo
                                                                       𝑥
                                                            1 cosh 1 − 𝐿 𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                                  𝑉ෘ 𝑥, 𝑠 =
                                                            𝑠     cosh 𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡

 E dunque, nel caso particolare di x = 𝐿:
                                                                             1
                                                      𝑉ෘ 𝐿, 𝑠 =
                                                                    𝑠 cosh   𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡                                      5




                                                                CIRCUITI
                                                           ELECTRONIC    E SISTEMI
                                                                      CICUITS FOR HIGH       6
                                                                                    ELETTRONICI
                                                                                       FREQUENCIES


Ci sono delle soluzioni approssimate dell’equazione differenziale per x = 𝐿 come ad esempio:


                                                    𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡                               𝑡 < 0.1𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                     𝑉0 𝑒𝑟𝑓𝑐
                       𝑉 𝐿, 𝑡 =                        4𝑡
                                                        −2.536𝑡           −9.4641𝑡          𝑡 > 0.1𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                      𝑉0     1 − 1.366𝑒 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 + 0.366𝑒 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡


                       2 𝑥 −𝑦2
dove 𝑒𝑟𝑓𝑐 𝑥 = 1 −        න 𝑒   𝑑𝑦             error-function
                        𝜋 0                   complementare


per avere un’escursione del 90% ad una distanza 𝐿𝑒𝑛 dall’inizio
delle linea dove viene applicato il gradino di tensione, deve
passare un tempo pari a


                             𝑡 = 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                                                                                                             6
                                                                                                                         CIRCUITI
                                                                                                                    ELECTRONIC    E SISTEMI
                                                                                                                               CICUITS FOR HIGH       7
                                                                                                                                             ELETTRONICI
                                                                                                                                                FREQUENCIES

                                                             Ritardo intrinseco dell’interconnessione
         Soluzione più generale ∀𝑥 con input a gradino
                                                                                                                                         Si nota la presenza di:
                                 𝑥
                      1 cosh 1 − 𝐿 𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡                                                                                            ❑ polo semplice in 𝑠0 = 0
            𝑉ෘ 𝑥, 𝑠 =
                      𝑠     cosh 𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡                                                                                              ❑ infiniti poli semplici (radici di cosh 𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 = 0)
                                                                                                                                           in 𝑠𝑘 = −𝑝𝑘 / 𝑅𝐶 per ogni intero 𝑘 ≥ 1

                                                                                                                                                       2𝑘 − 1 2 𝜋 2         𝑘≥1
                                                                                                                                                      𝑝𝑘 =
          maggiori informazioni in:                                                                                                                        4
         [Vasant B. Rao, "Delay Analysis of the Distributed RC                                                                          I residui corrispondenti a ogni polo sono 𝜌0 = 1
         Line", 32nd Design Automation Conference, 1995]
                                                                                                                                                                    𝑥         𝜋
                                                                                                                                                     −4 cos 1 − 𝐿 2𝑘 − 1 2
                                                                                                                                        e 𝜌 (𝑥) =                                   per 𝑘 ≥ 1
                                                                                                                                             𝑘
                                                                                                                                                      2𝑘 − 1 𝜋 sin 2𝑘 − 1 𝜋Τ2
                                                                                                                                                                                               soluzione nel dominio del tempo
                                     ∞                                                                                                                                                  ∞
                                           4 sin 𝑘 − 1Τ2 𝜋 𝑥 Τ𝐿 − 4𝑅 𝐶                            2𝑘−1 2 𝜋2 𝑡
    𝑣 𝑥, 𝑡 = 1 − ෍                                              𝑒   𝑖𝑛𝑡 𝑖𝑛𝑡                                                                                𝑣 𝑥, 𝑡 = 1 + ෍ 𝜌𝑘 𝑥 𝑒 𝑠𝑘 𝑡
                                                 2𝑘 − 1 𝜋
                                     𝑘=1                                                                                             𝜋                                                  𝑘=1
                                                                                                                 sin     2𝑘 − 1        = −1 𝑘+1                                                                                               7
                                                                                                                                     2




                                                                                                                         CIRCUITI
                                                                                                                    ELECTRONIC    E SISTEMI
                                                                                                                               CICUITS FOR HIGH       8
                                                                                                                                             ELETTRONICI
                                                                                                                                                FREQUENCIES
                                                                                          B=u; % update the right-hand-side
clear all                                                                                                                                                                           %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                                                                                %==================================                                                 %                 METHOD 3: approximated-analytic solution                %
%--------------------------------------------------------------------------                     figure(1)                                                                           %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Input data                                                                                    subplot(2,1,1);
Len=0.1; % interconnection length (m)                                                           plot(x,u);                                                                          OutputVoltage_ApproxAnalytic=zeros(size(t));
T=200e-9;    % simulation time (s)                                                              xlabel('x [m]');                                                                    for i=1:numel(t)
                                                                                                axis ([0 Len 0 V0*1.1]);                                                                if t(i)<0.1*R*C
dx=1e-3;   % space discretization step                                                          TimStamp=['t=',num2str(t(i),'%2.3e\n'),'s'];                                                OutputVoltage_ApproxAnalytic(i)=2*V0*erfc(sqrt(R*C/(4*t(i))));
dt=1.5e-10; % time discretization step                                                          ylabel('V(x) [V]')                                                                      elseif t(i)>=0.1*(R*C)
                                                                                                title(TimStamp);                                                                    OutputVoltage_ApproxAnalytic(i)=...
r=0.075; % resistance per unit width (Ohm/um)                                                                                                                                                   V0*(1-1.366*exp(-2.536*t(i)/(R*C))+0.366*exp(-9.4641*t(i)/(R*C)));
c=110;   % capacitance per unit width (aF/um)                                                   %==================================                                                         %     else
                                                                                                OutputVoltage_Euler(i)=u(end); % save the voltage value at the end of                       %         V(i)=0.31;
V0= 1;    % voltage step amplitude                                                              % transmission the line                                                                 end
                                                                                                                                                                                    end
%--------------------------------------------------------------------------                     subplot(2,1,2);                                                                     figure(2)
% convert into MKS units                                                                        plot(t,OutputVoltage_Euler);                                                        plot(t,OutputVoltage_ApproxAnalytic,'b','linewidth',2);
r=r/1e-6;                                                                                       xlabel('t [s]');
c=c*1e-18/1e-6;                                                                                 ylabel('Vout(x=L_e_n) [V]');
                                                                                                axis ([0 T 0 V0*1.1]);                                                              legend('Fully numeric','Semi Analytical ','Approx. Analytical');
% calculate space and time domain                                                               shg
x=0:dx:Len;                                                                                     drawnow
t=0:dt:T;                                                                                 end

                                                                                          %==================================
                                                                                          figure(2)
                                                                                                                                                                                        supponiamo      di  avere    una
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%            METHOD 1: fully numeric - BACKWARD EULER METHOD              %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                                                                          plot(t,OutputVoltage_Euler,'k','linewidth',2);
                                                                                          hold on
                                                                                          shg
                                                                                                                                                                                        interconnessione in Al realizzata
%% ************************************************************************
                                                                                          legend('Fully numeric');
                                                                                          xlabel('t [s]');                                                                              sulla prima metallizzazione di
% determine entries for the matrix used for Backward Euler scheme                         ylabel('Vout(x=L_e_n) [V]');

F=1/(r*c)*dt/(dx^2);
                                                                                                                                                                                        larghezza 1μm
Diagonal   = diag((1+2*F)*ones(numel(x),1));    %inserisci elementi diagonali             %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
UpDiagon   = diag(-F*ones(numel(x)-1,1),1);
DownDiagon = diag(-F*ones(numel(x)-1,1),-1);
                                                %inserisci elementi sopra-diagonale
                                                %inserisci elementi sotto-diagonale
                                                                                          %                      METHOD 2: semi-analytic solution                   %
                                                                                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                          𝑐 = 30 + 2 × 40 𝑎𝐹/𝜇𝑚
M=Diagonal+UpDiagon+DownDiagon;                                                           R=r*Len;
                                                                                          C=c*Len;
%--------------------------------------------------------------------------
                                                                                                                                                                                                          0.075
                                                                                                                                                                                                 𝑟=             = 0.075 Ω/𝜇𝑚
% set bounday conditions                                                                  index_summation=5;
% (For Dirichlet BC: 1 coefficient in position (1,1)                                      functionTosum=zeros(numel(x), numel(t));

                                                                                                                                                                                                            𝑊
M(1,:)=0; % delete all entries in the first row                                           figure(3)
M(1,1)=1; % place the coefficient                                                         plot(t,OutputVoltage_Euler,'k','linewidth',4);
                                                                                          hold on
% (For Neumann BC: (three points first derivative) dv/dx=[3*v(x)-4v(x-h)+v(x-2*h)]/(2*h)) xlabel('t [s]');
M(end,:)=0; % delete all entries in the first row                                         ylabel('Vout(x=L_e_n) [V]');
M(end,end)=3;    % place the coefficient                                                  for k=1:index_summation
M(end,end-1)=-4; % place the coefficient
M(end,end-2)=+1; % place the coefficient                                                      temp=transpose(4*sin((k-1/2)*pi*x/Len)/((2*k-1)*pi))*exp(-((2*k-1)^2*pi^2.*t)/(4*R*C));
                                                                                              functionTosum=functionTosum+temp;
%--------------------------------------------------------------------------                   OutputVoltage_SemiAnalytic=1-functionTosum;
% set initial condition                                                                       pause(3)
B=zeros(numel(x),1);                                                                          plot(t,OutputVoltage_SemiAnalytic(end,:),'r','linewidth',2);
B(1)=1;                                                                                       title(['Summation index k=',num2str(k)])
                                                                                              shg
%--------------------------------------------------------------------------                   drawnow
OutputVoltage_Euler=nan(size(t));                                                         end

for i=1:numel(t)
    % force Boundary Conditions                                                           figure(2)
    B(1)=V0;
    B(end)=0;
                                                                                          plot(t,OutputVoltage_SemiAnalytic(end,:),'r','linewidth',2);
                                                                                          hold on
                                                                                                                                                                                                                                              8
    %---------------------------------
    u=M\B; %solve linear system                                                           legend('Fully numeric','Semi Analytical ');
    %---------------------------------
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       9
                                                                            ELETTRONICI
                                                                               FREQUENCIES


                                                                     90% → 1.0𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 = 82.5𝑛𝑠




                                                                     50% → 0.38𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 = 31.4𝑛𝑠




               31.4ns          82.5ns




 Per una rete RC a parametri concentrati, il ritardo per un’escursione del segnale in uscita da 0 a 90%
                                          non vale 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 ‼
                                                                                                           9




                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       10
                                                                            ELETTRONICI
                                                                               FREQUENCIES


                     𝑅𝑖𝑛𝑡
                                                                                         𝑡
                                                                                     −
                                                                 𝑉𝑜𝑢𝑡 = 𝑉0 1 − 𝑒 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡

        𝑉0                           𝐶𝑖𝑛𝑡          𝑉𝑜𝑢𝑡                          se vogliamo 𝑉𝑜𝑢𝑡 =90%


                                                                 𝑡 = 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 ln 10 ≅ 2.3𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡


Per avere la stessa escursione di 𝑉𝑜𝑢𝑡 nel circuito a parametri concentrati, serve un tempo pari a

                                                       𝑡 = 2.3𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡


❑ La linea a parametri distribuiti è più veloce di quella a parametri concentrati!

E’ un risultato atteso visto che, preso un punto x tra 0 e 𝐿𝑒𝑛 , se guardo verso la sorgente vedo una resistenza
< 𝑅𝑖𝑛𝑡 → questo vuol dire transitorio più veloce rispetto al circuito a parametri concentrati

                                                                                                          10
                                                              CIRCUITI
                                                         ELECTRONIC    E SISTEMI
                                                                    CICUITS FOR HIGH       11
                                                                                  ELETTRONICI
                                                                                     FREQUENCIES

                                    Modelli a parametri concentrati
Posso rappresentare una linea distribuita con una opportuna successione di celle a parametri
concentrati con struttura a L, T o π
       𝑅                                       𝑅/2         𝑅/2


                    𝐶                                               𝐶/2         𝐶/2


                𝑅                                             𝑅/2                      𝑅/2



          𝐶/2                 𝐶/2               𝐶/4                 𝐶/4             𝐶/4                   𝐶/4


       𝑅/2          𝑅/2                                 𝑅/4          𝑅/4     𝑅/4          𝑅/4


                    𝐶                                    𝐶/2                 𝐶/2
                                                                                                                   11




                                                              CIRCUITI
                                                         ELECTRONIC    E SISTEMI
                                                                    CICUITS FOR HIGH       12
                                                                                  ELETTRONICI
                                                                                     FREQUENCIES

   Indipendentemente dal tipo di rete utilizzata (L, T o π) dovrà risultare


      𝑁
                                                      Le rappresentazioni circuitali delle interconnessioni viste ora
     ෍ 𝑅𝑖 = 𝑅𝑖𝑛𝑡 = 𝑟𝐿𝑒𝑛                               (L, T o π), sono utili per determinare in modo analitico le
     𝑖=1                                              costanti di tempo dominanti delle reti di resistenze e
      𝑁                                               capacita → formule di Elmore
     ෍ 𝐶𝑖 = 𝐶𝑖𝑛𝑡 = 𝑐𝐿𝑒𝑛                               Consentono di calcolare la costante di tempo al prim’ordine
     𝑖=1                                              (o, similmente il primo momento della risposta impulsiva) →
                                                      è un’approssimazione della costante di tempo reale.


                        𝑅1            𝑅2                𝑅3                   𝑅𝑛−1               𝑅𝑛



                             𝐶1            𝐶2                𝐶3                 𝐶𝑛−1                 𝐶𝑛




                                                                                                                   12
                                                                     CIRCUITI
                                                                ELECTRONIC    E SISTEMI
                                                                           CICUITS FOR HIGH       13
                                                                                         ELETTRONICI
                                                                                            FREQUENCIES


              𝑅1               𝑅2        𝑉2                                                   𝑅𝑛
                                               𝑅3                        𝑅𝑛−1


                   𝐶1               𝐶2              𝐶3                     𝐶𝑛−1                    𝐶𝑛



    per il nodo 2:
                  𝑑𝑉2 𝑉1 − 𝑉2 𝑉3 − 𝑉2               per trovare 𝑉1 e 𝑉3 devo ripetere la stessa procedura
              𝐶      =       +
                  𝑑𝑡    𝑅2      𝑅3




                                                                                  →
                                                    trovo tante equazioni differenziali quando sono i nodi




                                                                                  →
                                                                     complicato da risolvere

                                                          𝑁                           𝑁
→ Formule di Elmore: consentono
di calcolare, in un dato nodo, la                   𝜏𝑖 = ෍ 𝐶𝑘 𝑅𝑘𝑖     con 𝑅𝑘𝑖 = ෍ 𝑅𝑗 ∈ [𝑝𝑒𝑟𝑐𝑜𝑟𝑠𝑖 𝑠 → 𝑖 ˄𝑝𝑒𝑟𝑐𝑜𝑟𝑠𝑖 𝑠 → 𝑘 ]
costante di tempo dominante come                         𝑘=1                      𝑘=1
                                                                                                                    13




                                                                     CIRCUITI
                                                                ELECTRONIC    E SISTEMI
                                                                           CICUITS FOR HIGH       14
                                                                                         ELETTRONICI
                                                                                            FREQUENCIES
                                                               𝑁                          𝑁
                                         𝑅3
                                                         𝜏𝑖 = ෍ 𝐶𝑘 𝑅𝑘𝑖     con 𝑅𝑘𝑖 = ෍ 𝑅𝑗 ∈ [𝑝𝑒𝑟𝑐𝑜𝑟𝑠𝑖 𝑠 → 𝑖 ˄𝑝𝑒𝑟𝑐𝑜𝑟𝑠𝑖 𝑠 → 𝑘 ]
                                                               𝑘=1                        𝑘=1
                                          𝐶3
A      𝑅1            𝑅2


         𝐶1               𝐶2
                                         𝑅4
                                                    B

                                          𝐶4




     𝜏𝐴→𝐵
     = 𝐶1 𝑅1
     + 𝐶2 𝑅1 + 𝑅2
     + 𝐶3 𝑅1 + 𝑅2
     + 𝐶4 𝑅1 + 𝑅2 + 𝑅4


                                                                                                                    14
                                                                     CIRCUITI
                                                                ELECTRONIC    E SISTEMI
                                                                           CICUITS FOR HIGH       15
                                                                                         ELETTRONICI
                                                                                            FREQUENCIES

 A          𝑅1             𝑅2         B    𝑅3               𝑅4



                 𝐶1             𝐶2              𝐶3               𝐶4




  𝜏𝐴→𝐵
  = 𝐶1 𝑅1
  + 𝐶2 𝑅1 + 𝑅2
  + 𝐶3 𝑅1 + 𝑅2
  + 𝐶4 𝑅1 + 𝑅2




                                                                                                                      15




                                                                     CIRCUITI
                                                                ELECTRONIC    E SISTEMI
                                                                           CICUITS FOR HIGH       16
                                                                                         ELETTRONICI
                                                                                            FREQUENCIES


Nel caso di assenza di diramazioni
                                                                 𝑁    𝑘           𝑁        𝑁

                                                       𝜏0→𝑁 = ෍ 𝐶𝑘 ෍ 𝑅𝑗 = ෍ 𝑅𝑘 ෍ 𝐶𝑗
                                                                𝑘=1   𝑗=1        𝑘=1    𝑗=𝑘

 Sfruttando la rappresentazione a parametri concentrati con
 schema a L, di una linea a parametri distribuiti, avremo
          𝑅𝑖𝑛𝑡
     𝑅𝑖 =             ∀𝑖 ∈ 1, … , 𝑁
           𝑁                                                              1
                                                                             𝑁         𝑘
                                                                                             1
                                                                                                     𝑁
          𝐶𝑖𝑛𝑡                                                   𝜏0→𝑁 =      ෍ 𝐶𝑖𝑛𝑡 ෍ 𝑅𝑖𝑛𝑡 = 2 ෍ 𝐶𝑖𝑛𝑡 𝑘 𝑅𝑖𝑛𝑡
     𝐶𝑖 =             ∀𝑖 ∈ 1, … , 𝑁                  e dunque             𝑁2                𝑁
           𝑁                                                                𝑘=1        𝑗=1          𝑘=1
                                                                                                          𝑁
                                                                                                 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
        𝑅𝑖𝑛𝑡 /N           𝑅𝑖𝑛𝑡 /N         𝑅𝑖𝑛𝑡 /N          𝑅𝑖𝑛𝑡 /N                             =           ෍𝑘
  IN                                                                      OUT                      𝑁2
                                                                                                          𝑘=1
                                                                                                           𝑁(𝑁 + 1)
                                                                                               = 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
        𝐶𝑖𝑛𝑡 /𝑁            𝐶𝑖𝑛𝑡 /𝑁         𝐶𝑖𝑛𝑡 /𝑁          𝐶𝑖𝑛𝑡 /𝑁                                          2𝑁 2


                                                                                                                      16
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       17
                                                                            ELETTRONICI
                                                                               FREQUENCIES


                      𝑁(𝑁 + 1)
   𝜏0→𝑁 = 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                        2𝑁 2

                              𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡   dunque il ritardo al 90% che vale circa 2.3𝜏 diventa
      Se 𝑁 → ∞           𝜏=
                                 2




                                                                 →
                                                              2.3
                                                                  𝑅 𝐶
                                                               2 𝑖𝑛𝑡 𝑖𝑛𝑡




                                                                 →
                                                       e quasi uguale a 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡




                                                                                                            17




                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       18
                                                                            ELETTRONICI
                                                                               FREQUENCIES

                                      Linea pilotata da un driver
❑ L’interconnessione è pilotata da un driver → Il più semplice è un invertitore
                                                                 →




                                                  Il ritardo complessivo dipenderà da
                                               ❑ ritardo dell’interconnessione
                                               ❑ caratteristiche del driver

Notiamo anche che l’analisi di un driver connesso ad una linea non è di facile trattazione → sarebbe necessario
stabilire cosa fornisce il driver in input alla linea e usare questa informazione come condizione al contorno per la
soluzione dell’equazione di diffusione

 Per eliminare tale complessità:
 ❑ assumiamo una commutazione istantanea dell’ingresso dell’invertitore
 ❑ che le capacità parassite sul nodo di uscita dell’invertitore siano piccole rispetto a 𝐶𝑖𝑛𝑡 in modo tale tra
   trascuralre
 ❑ l’interconnessione viene schematizzata mediante parametri concentrati 𝐶𝑖𝑛𝑡 e 𝑅𝑖𝑛𝑡
                                                                                                            18
                                                                  CIRCUITI
                                                             ELECTRONIC    E SISTEMI
                                                                        CICUITS FOR HIGH       19
                                                                                      ELETTRONICI
                                                                                         FREQUENCIES


      𝑉𝐼𝐼         𝑅𝑖𝑛𝑡   𝑉𝑂𝐼
                                                   Rispetto ai casi già studiati in precedenza, ora tra transistore e
            𝐼𝐷𝑆                                    capacità di uscita è presente la resistenza 𝑅𝑖𝑛𝑡




                                                                                      →
𝑉𝑖𝑛
                               𝐶𝑖𝑛𝑡          𝐶𝐿
                                                   ci sono due potenziali incogniti 𝑉𝑂𝐼 e 𝑉𝐼𝐼

                                                   Le espressioni per la corrente in regime di saturazione e di triodo
                                                   sono note → potremmo calcolare analiticamente il ritardo.




                                                                                      →
                                                  Otterremmo espressioni complicate → per ovviare a questo
                                                  problema semplifichiamo la relazione tra tensione e corrente del
                                                  transistore




                                                                                                                 19




                                                                  CIRCUITI
                                                             ELECTRONIC    E SISTEMI
                                                                        CICUITS FOR HIGH       20
                                                                                      ELETTRONICI
                                                                                         FREQUENCIES

                                                              𝑅𝑖𝑛𝑡

                                                       𝐼𝐷𝑆
                                      𝑉𝑖𝑛
                                                                       𝐶𝑖𝑛𝑡      𝐶𝐿




                           saturazione                                             triodo
                         𝑅𝑖𝑛𝑡                                                         𝑅𝑖𝑛𝑡



            𝐼𝑑𝑟                       𝐶𝑖𝑛𝑡        𝐶𝐿                      𝑅𝑑𝑟                   𝐶𝑖𝑛𝑡   𝐶𝐿



                   Tempo di scarica: T1                                         Tempo di scarica: T2
                                                                                                                 20
                                                                   CIRCUITI
                                                              ELECTRONIC    E SISTEMI
                                                                         CICUITS FOR HIGH       21
                                                                                       ELETTRONICI
                                                                                          FREQUENCIES

                                                                                         𝑉𝐼𝐼         𝑅𝑖𝑛𝑡   𝑉𝑂𝐼
      approssimazioni
                                                            𝑉𝐷𝑆                                𝐼𝐷𝑆
      1) 𝑉𝐷𝑆 < 𝑉𝑥 , cioè in regione triodo:         𝐼𝐷𝑆 =
                                                            𝑅𝑑𝑟              𝑉𝑖𝑛
                                                                                                                  𝐶𝑖𝑛𝑡   𝐶𝐿
      2) 𝑉𝐷𝑆 > 𝑉𝑥 , cioè in regione di saturazione            𝐼𝐷𝑆 = 𝐼𝑑𝑟


      𝐼𝐷𝑆                                                     Assumiamo come condizione iniziale che la linea sia carica
                                                                               𝑉𝐼𝐼 𝑡 = 0 = 𝑉𝑂𝐼 𝑡 = 0 = 𝑉𝐷𝐷
 𝐼𝑑𝑟
                                                             FASE 1: nMOS in saturazione → scarica a corrente costante
                                                                                        𝐼𝐷𝑆 = 𝐼𝑑𝑟 = 𝑐𝑜𝑛𝑠𝑡
                                                                                                                         𝑑𝑉𝑂𝐼
             𝑅𝑑𝑟 −1                                                equazione che governa la scarica è: 𝐶𝐿 + 𝐶𝑖𝑛𝑡              = −𝐼𝑑𝑟
                                                                                                                          𝑑𝑡
                                                   𝑉𝐷𝑆                                                    𝐼𝑑𝑟
                                                                                     𝑉𝑂𝐼 𝑡 = 𝑉𝐷𝐷 −               𝑡
                   𝑉𝑥                                                                                  𝐶𝐿 + 𝐶𝑖𝑛𝑡

                                                          𝑉𝑂𝐼 𝑡 diminuisce linearmente finchè 𝑉𝐼𝐼 = 𝑉𝑥 per 𝑡 = 𝑡1         21




                                                                   CIRCUITI
                                                              ELECTRONIC    E SISTEMI
                                                                         CICUITS FOR HIGH       22
                                                                                       ELETTRONICI
                                                                                          FREQUENCIES


Quando 𝑉𝐼𝐼 = 𝑉𝑥 cioè quando 𝑉𝐼𝐼 = 𝑉𝑂𝐼 − 𝑅𝑖𝑛𝑡 𝐼𝑑𝑟 = 𝑉𝑥


                                              𝐼𝑑𝑟
                                   𝑉𝐷𝐷 −            𝑡 − 𝑅𝑖𝑛𝑡 𝐼𝑑𝑟 = 𝑉𝑥      dalla quale ricaviamo il tempo 𝑡1
                                           𝐶𝐿 + 𝐶𝑖𝑛𝑡 1

                                                                                                        𝑉𝐷𝐷 − 𝑉𝑥
                                                                              𝑡1 = 𝐶𝐿 + 𝐶𝑖𝑛𝑡 𝑅𝑖𝑛𝑡                 −1
                                                                                                         𝑅𝑖𝑛𝑡 𝐼𝑑𝑟
             𝑉𝐼𝐼            𝑅𝑖𝑛𝑡    𝑉𝑂𝐼
                                                                    se 𝑅𝑖𝑛𝑡 è tale per cui 𝑅𝑖𝑛𝑡 𝐼𝑑𝑟 > 𝑉𝐷𝐷 − 𝑉𝑥 vuol dire che il
                      𝐼𝐷𝑆
                                                                    transitorio in cui l’nMOS è in saturazione non esiste
𝑉𝑖𝑛                                                                 → in altre parole il transistore parte in regione triodo
                                          𝐶𝑖𝑛𝑡      𝐶𝐿

                                                                   Tensione al noto 𝑂𝐼 al tempo 𝑡1 :
                                                                                   𝑉𝑂𝐼 𝑡1 = 𝑉𝑥 + 𝑅𝑖𝑛𝑡 𝐼𝑑𝑟



                                                                                                                          22
                                                                  CIRCUITI
                                                             ELECTRONIC    E SISTEMI
                                                                        CICUITS FOR HIGH       23
                                                                                      ELETTRONICI
                                                                                         FREQUENCIES

FASE 2: l’nMOS è in triodo e secondo l’approssimazione precedente, lo possiamo vedere come fosse una
resistenza di valore 𝑅𝑑𝑟

  𝑉𝐼𝐼         𝑅𝑖𝑛𝑡         𝐼𝐶
                                                                                                                     𝑑𝑉𝑂𝐼
                                                    𝑅𝑡𝑜𝑡 = 𝑅𝑑𝑟 + 𝑅𝑖𝑛𝑡                                   𝐼𝐶 = 𝐶𝑡𝑜𝑡
                                                                                                                      𝑑𝑡
         𝐼𝑅          𝑉𝑂𝐼                                                                                 𝐼𝑅 = −𝐼𝐶
                                                    𝐶𝑡𝑜𝑡 = 𝐶𝑖𝑛𝑡 + 𝐶𝐿
                                                                                                              𝑉𝐼𝐼   𝑉𝑂𝐼
𝑅𝑑𝑟                             𝐶𝑖𝑛𝑡        𝐶𝐿                                                          𝐼𝑅 =      =
                                                                                                             𝑅𝑑𝑟 𝑅𝑡𝑜𝑡

                                                                                                       𝑉𝑂𝐼         𝑑𝑉𝑂𝐼
                                                                                                   −        = 𝐶𝑡𝑜𝑡
                                                                                                       𝑅𝑡𝑜𝑡         𝑑𝑡
                                                                                            𝑡2                 𝑉𝑂𝐼 𝑡2
                                                                                                     𝑑𝑡               𝑑𝑉𝑂𝐼
                                                                                          න −               =න
                                                                                           0      𝑅𝑡𝑜𝑡 𝐶𝑡𝑜𝑡   𝑉𝑂𝐼 𝑡1   𝑉𝑂𝐼

                                       𝑉𝑂𝐼 𝑡1
              𝑡2 = 𝑅𝑡𝑜𝑡 𝐶𝑡𝑜𝑡 ln                                                                                      𝑉𝑂𝐼 𝑡1
                                       0.1𝑉𝐷𝐷                                                    𝑡2 = 𝑅𝑡𝑜𝑡 𝐶𝑡𝑜𝑡 ln
                                                                                                                     𝑉𝑂𝐼 𝑡2
                                →




                                    𝑉𝑥 + 𝑅𝑖𝑛𝑡 𝐼𝑑𝑟    considerando il transitorio esaurito per
          𝑡2 = 𝑅𝑡𝑜𝑡 𝐶𝑡𝑜𝑡 ln                                    𝑉𝑂𝐼 𝑡2 = 0.1𝑉𝐷𝐷
                                       0.1𝑉𝐷𝐷                                                                                 23




                                                                  CIRCUITI
                                                             ELECTRONIC    E SISTEMI
                                                                        CICUITS FOR HIGH       24
                                                                                      ELETTRONICI
                                                                                         FREQUENCIES


                                                    𝑉𝐷𝐷 − 𝑉𝑥                                𝑉𝑥 + 𝑅𝑖𝑛𝑡 𝐼𝑑𝑟
              𝑇90% = 𝑇1 + 𝑇2 = 𝐶𝑖𝑛𝑡 + 𝐶𝐿 𝑅𝑖𝑛𝑡                 − 1 + 𝑅𝑖𝑛𝑡 + 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 + 𝐶𝐿 ln
                                                     𝑅𝑖𝑛𝑡 𝐼𝑑𝑟                                  0.1𝑉𝐷𝐷

  dipende da
  ❑ parametri dell’interconnessione: 𝑅𝑖𝑛𝑡 e 𝐶𝑖𝑛𝑡
  ❑ caratteristiche del driver: 𝐼𝑑𝑟 , 𝑅𝑑𝑟 e 𝑉𝑥


 Nel caso di interconnessioni sufficientemente lunghe e/o di driver con dimensionamenti sufficientemente grandi
 (quindi 𝐼𝑑𝑟 grandi)
                                                       𝑅𝑖𝑛𝑡 𝐼𝑑𝑟 ≈ 𝑉𝐷𝐷 − 𝑉𝑥

 in questo caso 𝑡1 ≪ 𝑡2

 e in particolare possiamo scrivere

          𝑠𝑒 𝑡1 → 0                                              𝑇90% ≈ 2.3 𝑅𝑖𝑛𝑡 + 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 + 𝐶𝐿
        ቊ
         𝑠𝑒 𝑉𝑥 + 𝑅𝑖𝑛𝑡 𝐼𝑑𝑟 ≈ 𝑉𝐷𝐷
                                                                                                                              24
                                                            CIRCUITI
                                                       ELECTRONIC    E SISTEMI
                                                                  CICUITS FOR HIGH       25
                                                                                ELETTRONICI
                                                                                   FREQUENCIES


                                 𝑇90% ≈ 2.3 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 + 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 + 𝑅𝑖𝑛𝑡 𝐶𝐿 + 𝑅𝑑𝑟 𝐶𝐿



      Il termine 2.3 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 è il ritardo intrinseco dell’interconnessione «a parametri concentrati» corrispondente ad
      un’escursione del segnale del 90%
      sappiamo che è il ritardo intrinseco di una interconnessione a parametri distribuiti corrispondente ad
      un’escursione al 90% è pari a 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 .


      In modo empirico teniamo conto della natura distribuita dell’interconnessione scrivendo (per 𝑡1 → 0)

                                 𝑇90% ≈ 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 + 2.3 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 + 𝑅𝑖𝑛𝑡 𝐶𝐿 + 𝑅𝑑𝑟 𝐶𝐿


                                        ≈ 𝑟𝑐𝐿𝑒𝑛 2 + 2.3 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 + 𝑅𝑖𝑛𝑡 𝐶𝐿 + 𝑅𝑑𝑟 𝐶𝐿

  se 𝐶𝐿 ≪ 𝐶𝑖𝑛𝑡 allora:

                                                 𝑇90% ≈ 𝑟𝑐𝐿𝑒𝑛 2 + 2.3𝑅𝑑𝑟 𝑐𝐿𝑒𝑛
                                                                                                              25




                                                            CIRCUITI
                                                       ELECTRONIC    E SISTEMI
                                                                  CICUITS FOR HIGH       26
                                                                                ELETTRONICI
                                                                                   FREQUENCIES

                                                      Riepilogo
                                                 𝑉𝐷𝐷 − 𝑉𝑥                                𝑉𝑥 + 𝑅𝑖𝑛𝑡 𝐼𝑑𝑟
              𝑇90% = 𝑇1 + 𝑇2 = 𝐶𝑖𝑛𝑡 + 𝐶𝐿 𝑅𝑖𝑛𝑡              − 1 + 𝑅𝑖𝑛𝑡 + 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 + 𝐶𝐿 ln
                                                  𝑅𝑖𝑛𝑡 𝐼𝑑𝑟                                  0.1𝑉𝐷𝐷


                       𝑅𝑖𝑛𝑡                                             𝑠𝑒 𝑡1 → 0
                                                                      ቊ
                                                                       𝑠𝑒 𝑉𝑥 + 𝑅𝑖𝑛𝑡 𝐼𝑑𝑟 ≈ 𝑉𝐷𝐷
                 𝐼𝐷𝑆
𝑉𝑖𝑛                                                     𝑇90% ≈ 2.3 𝑅𝑖𝑛𝑡 + 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 + 𝐶𝐿
                                 𝐶𝑖𝑛𝑡       𝐶𝐿
                                                        𝑇90% = 2.3 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 + 2.3 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 + 𝑅𝑖𝑛𝑡 𝐶𝐿 + 𝑅𝑑𝑟 𝐶𝐿

                                                                     In modo empirico 2.3 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 → 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡


                                                           𝑇90% = 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 + 2.3 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 + 𝑅𝑖𝑛𝑡 𝐶𝐿 + 𝑅𝑑𝑟 𝐶𝐿

                                                                     se 𝐶𝐿 ≪ 𝐶𝑖𝑛𝑡

                         dipende dal quadrato della
                                                          𝑇90% ≈ 𝑟𝑐𝐿𝑒𝑛 2 + 2.3𝑅𝑑𝑟 𝑐𝐿𝑒𝑛                        26
                            lunghezza della linea!
                                                            CIRCUITI
                                                       ELECTRONIC    E SISTEMI
                                                                  CICUITS FOR HIGH       27
                                                                                ELETTRONICI
                                                                                   FREQUENCIES


Nel caso in cui 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 ≪ 2.3𝑅𝑑𝑟 𝐶𝑖𝑛𝑡                                              𝑇90% ≈ 𝑟𝑐𝐿𝑒𝑛 2 + 2.3𝑅𝑑𝑟 𝑐𝐿𝑒𝑛




                                                                                                  →
Allora 𝑇90% è molto simile a quello di un driver caricato con capacità 𝐶𝑖𝑛𝑡              𝑇90% ≈ 2.3𝑅𝑑𝑟 𝑐𝐿𝑒𝑛




                                                                                                              27




                                                            CIRCUITI
                                                       ELECTRONIC    E SISTEMI
                                                                  CICUITS FOR HIGH       28
                                                                                ELETTRONICI
                                                                                   FREQUENCIES


                  Interconnessione RC come semplice capacità 𝐶𝑖𝑛𝑡
Quando possiamo considerare l’interconnessione RC come semplice capacità 𝐶𝑖𝑛𝑡 ?


riconsideriamo:      𝑇90% ≈ 𝑟𝑐𝐿𝑒𝑛 2 + 2.3𝑅𝑑𝑟 𝑐𝐿𝑒𝑛

                   se, ad esempio, 2.3𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 > 10𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡

                                𝑅𝑖𝑛𝑡             𝑅𝑑𝑟        se questa condizione è verificata allora possiamo
                     𝑅𝑑𝑟 > 10        → 𝐿𝑒𝑛 < 2.3            considerare la linea puramente capacitiva e trascurare
                                2.3              10𝑟
                                                            gli effetti resistivi della linea


                                                      𝑅𝑑𝑟   allora dobbiamo tenere in considerazione della
                           se invece      𝐿𝑒𝑛 > 2.3
                                                      10𝑟   natura distribuita della rete RC



                                                                                                              28
                                                                CIRCUITI
                                                           ELECTRONIC    E SISTEMI
                                                                      CICUITS FOR HIGH       29
                                                                                    ELETTRONICI
                                                                                       FREQUENCIES

                              Determinazione dei parametri del driver
  sappiamo che la corrente di saturazione vale

                        𝛽𝑛
         𝐼𝑠𝑎𝑡 = 𝐼𝑑𝑟 =      𝑉 − 𝑉𝑇 2     dove per semplicità trascuriamo il termine 1 + λ𝑉𝐷𝑠
                        2 𝐷𝐷

      per quanto riguarda il termine 𝑅𝑑𝑟 e 𝑉𝑥 ricordiamo che in regione triodo

                                           𝛽𝑛
                                   𝐼𝐷𝑆 =      2 𝑉𝐺𝑆 − 𝑉𝑇 𝑉𝐷𝑆 − 𝑉𝐷𝑆 2             dove anche in questo caso trascuriamo la modulazione della
                                           2                                     lunghezza di canale λ


                                      𝐼𝐷𝑆 è funzione quadratica di 𝑉𝐷𝑆 !




                            La determinazione di 𝑅𝑑𝑟 e 𝑉𝑥 può avvenire in due modi diversi
                                                                                                                                29




                                                                CIRCUITI
                                                           ELECTRONIC    E SISTEMI
                                                                      CICUITS FOR HIGH       30
                                                                                    ELETTRONICI
                                                                                       FREQUENCIES

                              Determinazione dei parametri del driver
 𝐼𝐷𝑆
                                            Metodo 1) Estrapoliamo la relazione 𝐼𝐷𝑆 - 𝑉𝐷𝑆 sulla base del tratto lineare
                                                      nell’intorno di 𝑉𝐷𝑆 = 0
𝐼𝑑𝑟
                                                              𝜕𝐼𝐷𝑆
                                                                   ቤ           = 𝛽𝑛 𝑉𝐷𝑆 − 𝑉𝑇 − 𝛽𝑛 𝑉𝐷𝑆 ቚ            = 𝛽𝑛 𝑉𝐷𝑆 − 𝑉𝑇
                                                              𝜕𝑉𝐷𝑆 𝑉                                      𝑉𝐷𝑆 =0
                                                                       𝐷𝑆 =0



                                                                                1
                                           𝑉𝐷𝑆                 𝑅𝑑𝑟 =                                 e         𝑉𝑥 = 𝑅𝑑𝑟 𝐼𝑑𝑟
                                                                        𝛽𝑛 𝑉𝐷𝑆 − 𝑉𝑇 𝑉
                                                                                         𝐷𝑆 =0
          𝑉𝑥(1) 𝑉𝐷𝐷 − 𝑉𝑇 = 𝑉𝑥(2)
                                                          stiamo sovrastimando 𝐼𝐷𝑆                 in regione triodo e quindi
                                                          sottostimando il ritardo
 Metodo 2)

               𝑉𝑥(2)      𝑉𝐷𝐷 − 𝑉𝑇          2
       𝑅𝑑𝑟 =         =               =
                𝐼𝑑𝑟    𝛽𝑛          2   𝛽𝑛 𝑉𝐷𝐷 − 𝑉𝑇
                       2 𝑉𝐷𝐷 − 𝑉𝑇
       stiamo sottostimando 𝐼𝐷𝑆         in regione triodo e quindi                                                              30
       sovrastimando il ritardo
                                                      CIRCUITI
                                                 ELECTRONIC    E SISTEMI
                                                            CICUITS FOR HIGH       31
                                                                          ELETTRONICI
                                                                             FREQUENCIES

                                            𝑅𝑖𝑛𝑣 = 𝑅𝑑𝑟 ? ?
Supponiamo che con la metodologia del Logical Effort si determini una resistenza equivalente di un invertitore
simmetrico parti a 𝑅𝑖𝑛𝑣

Ricordando che 𝑅𝑖𝑛𝑣 è definita al 90% dell’escursione del segnale di uscita

Posso assumere 𝑅𝑖𝑛𝑣 = 𝑅𝑑𝑟 e usarla per calcolare il ritardo?


      No, perché 𝑅𝑖𝑛𝑣 è definita già al 90% dell’escursione dunque il valore da usare per il pilotaggio
      dell’interconnessione sarà:
                                                      𝑅𝑖𝑛𝑣
                                              𝑅𝑑𝑟 =
                                                      2.3


      questo perché 𝑅𝑑𝑟 rappresenta una resistenza a tutti gli effetti mentre 𝑅𝑖𝑛𝑣 , di nuovo, è definita al
      90% dell’escursione


                                                                                                           31




                                                      CIRCUITI
                                                 ELECTRONIC    E SISTEMI
                                                            CICUITS FOR HIGH       32
                                                                          ELETTRONICI
                                                                             FREQUENCIES

esempio




                                                                                                           32
                                                              CIRCUITI
                                                         ELECTRONIC    E SISTEMI
                                                                    CICUITS FOR HIGH       33
                                                                                  ELETTRONICI
                                                                                     FREQUENCIES


 Se il termine 𝑟𝑐𝐿𝑒𝑛 2 risulta molto maggiore di 2.3𝑅𝑑𝑟 𝑐𝐿𝑒𝑛 , allora, anche
                                                                                             𝑇90% ≈ 𝑟𝑐𝐿𝑒𝑛 2 + 2.3𝑅𝑑𝑟 𝑐𝐿𝑒𝑛
 agendo sul dimensionamento del transistore non si otterranno
 miglioramenti significativi del ritardo



                      Dobbiamo partizionare l’interconnessione!



❑ Partizionamento di interconnessioni – ripetitori ad area minima
❑ Partizionamento di interconnessioni – ripetitori a dimensionamento ottimo
❑ Ripetitori in cascata




                                                                                                                    33




                                                              CIRCUITI
                                                         ELECTRONIC    E SISTEMI
                                                                    CICUITS FOR HIGH       34
                                                                                  ELETTRONICI
                                                                                     FREQUENCIES


        Partizionamento di interconnessioni – ripetitori ad area minima

 Se il termine 2.3𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 < 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 il ritardo è dominato fortemente dall’interconnessione e l’unico modo per
 ridurre il ritardo è attraverso un partizionamento della linea con l’inserimento di opportuni driver (ripetitori)

      𝑅𝑑𝑟      𝑅𝑖𝑛𝑡 /𝑘          𝑅𝑑𝑟      𝑅𝑖𝑛𝑡 /𝑘         𝑅𝑑𝑟       𝑅𝑖𝑛𝑡 /𝑘           𝑅𝑑𝑟      𝑅𝑖𝑛𝑡 /𝑘         𝑅𝑑𝑟
𝑉𝑖𝑛


            𝐶𝑖𝑛𝑡 /𝑘                   𝐶𝑖𝑛𝑡 /𝑘                  𝐶𝑖𝑛𝑡 /𝑘                     𝐶𝑖𝑛𝑡 /𝑘                       𝐶𝐿
                          𝐶𝑑𝑟                      𝐶𝑑𝑟                                                  𝐶𝑑𝑟



                                𝑇90% ≈ 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 + 2.3 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 + 𝑅𝑖𝑛𝑡 𝐶𝐿 + 𝑅𝑑𝑟 𝐶𝐿

                                                   𝐿𝑒𝑛    𝐿𝑒𝑛                    𝐿𝑒𝑛 2
                            𝑇90% = 𝑘 2.3 𝑅𝑑𝑟 𝑐         +𝑟     𝐶𝑑𝑟 + 𝑅𝑑𝑟 𝐶𝑑𝑟 + 𝑟𝑐
                                                    𝑘      𝑘                      𝑘

                                                                             𝐿𝑒𝑛 2
                                 = 2.3 𝑅𝑑𝑟 𝑐𝐿𝑒𝑛 + 𝑟𝐿𝑒𝑛 𝐶𝑑𝑟 + 𝑘𝑅𝑑𝑟 𝐶𝑑𝑟 + 𝑟𝑐                                          34
                                                                              𝑘
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       35
                                                                             ELETTRONICI
                                                                                FREQUENCIES


      Partizionamento di interconnessioni – ripetitori ad area minima

  𝑑𝑇90%          𝐿𝑒𝑛 2                                           𝑟𝑐𝐿2𝑒𝑛
        = 0 → 𝑟𝑐       = 2.3𝑅𝑑𝑟 𝐶𝑑𝑟                   𝑘𝑜𝑡𝑡 =
   𝑑𝑘             𝑘                                            2.3𝑅𝑑𝑟 𝐶𝑑𝑟


    ritardo intrinseco di          ritardo driver
          un tratto di            caricato da 𝐶𝑑𝑟
      interconnessione


 sostituendo 𝑘𝑜𝑡𝑡 nell’espressione di 𝑇90% troviamo:


             𝑇90% = 2.3 𝑅𝑑𝑟 𝑐𝐿𝑒𝑛 + 𝑟𝐿𝑒𝑛 𝐶𝑑𝑟 + 2𝐿𝑒𝑛 2.3𝑅𝑑𝑟 𝐶𝑑𝑟 𝑟𝑐


                            𝑅𝑑𝑟 𝐶𝑖𝑛𝑡   𝑅𝑖𝑛𝑡 𝐶𝑑𝑟
                                                                                                        35




                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       36
                                                                             ELETTRONICI
                                                                                FREQUENCIES


      Partizionamento di interconnessioni – ripetitori ad area minima

                                  𝑇90% = 2.3 𝑅𝑑𝑟 𝑐𝐿𝑒𝑛 + 𝑟𝐿𝑒𝑛 𝐶𝑑𝑟 + 2𝐿𝑒𝑛 2.3𝑅𝑑𝑟 𝐶𝑑𝑟 𝑟𝑐


❑ Notiamo come il ritardo dipende linearmente e non più quadraticamente da 𝐿𝑒𝑛
❑ I termini 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 e 𝑅𝑖𝑛𝑡 𝐶𝑑𝑟 non vengono modificati dall’ottimizzazione
❑ Il k non sarà un numero intero → vale quanto detto nel caso di uso della metodologia del logical effort
❑ Quando devo aspettarmi un netto miglioramento rispetto al caso di interconnessione non partizionata?




                                                                                                        36
                                                                    CIRCUITI
                                                               ELECTRONIC    E SISTEMI
                                                                          CICUITS FOR HIGH       37
                                                                                        ELETTRONICI
                                                                                           FREQUENCIES

  esempio




                                                                                                                              37




                                                                    CIRCUITI
                                                               ELECTRONIC    E SISTEMI
                                                                          CICUITS FOR HIGH       38
                                                                                        ELETTRONICI
                                                                                           FREQUENCIES

 Partizionamento di interconnessioni – ripetitori a dimensionamento ottimo
Se nell’espressione per il ritardo il termine 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 = 𝑅𝑑𝑟 𝑐𝐿𝑒𝑛 (che non è stato modificato dall’ottimizzazione) è
rilevante → possiamo provare a ridurre 𝑅𝑑𝑟

In questo caso i parametri di progetto sono:
❑k
                                               sappiamo che avrò         𝑅𝑑𝑟
❑ Il dimensionamento h dei driver                                              𝑟𝑎𝑝𝑝𝑟𝑒𝑠𝑒𝑛𝑡𝑎 𝑙𝑎 𝑛𝑢𝑜𝑣𝑎 𝑅𝑑𝑟
                                                                        ቐ ℎ
                                                                         𝐶𝑑𝑟 ℎ 𝑟𝑎𝑝𝑝𝑟𝑒𝑠𝑒𝑛𝑡𝑎 𝑙𝑎 𝑛𝑢𝑜𝑣𝑎 𝐶𝑑𝑟


        𝑅𝑑𝑟 /ℎ   𝑅𝑖𝑛𝑡 /𝑘          𝑅𝑑𝑟 /ℎ      𝑅𝑖𝑛𝑡 /𝑘          𝑅𝑑𝑟 /ℎ       𝑅𝑖𝑛𝑡 /𝑘     𝑅𝑑𝑟 /ℎ      𝑅𝑖𝑛𝑡 /𝑘          𝑅𝑑𝑟 /ℎ
  𝑉𝑖𝑛


              𝐶𝑖𝑛𝑡 /𝑘                      𝐶𝑖𝑛𝑡 /𝑘                      𝐶𝑖𝑛𝑡 /𝑘                  𝐶𝑖𝑛𝑡 /𝑘                           𝐶𝐿
                           ℎ𝐶𝑑𝑟                         ℎ𝐶𝑑𝑟                                                  ℎ𝐶𝑑𝑟




                                                                                                                              38
                                                            CIRCUITI
                                                       ELECTRONIC    E SISTEMI
                                                                  CICUITS FOR HIGH       39
                                                                                ELETTRONICI
                                                                                   FREQUENCIES

                            Dimensionamento ottimo dei ripetitori

In questo caso i parametri di progetto sono:
❑k
                                           sappiamo che avrò       𝑅𝑑𝑟
❑ Il dimensionamento h dei driver                                        𝑟𝑎𝑝𝑝𝑟𝑒𝑠𝑒𝑛𝑡𝑎 𝑙𝑎 𝑛𝑢𝑜𝑣𝑎 𝑅𝑑𝑟
                                                                  ቐ ℎ
                                                                   𝐶𝑑𝑟 ℎ 𝑟𝑎𝑝𝑝𝑟𝑒𝑠𝑒𝑛𝑡𝑎 𝑙𝑎 𝑛𝑢𝑜𝑣𝑎 𝐶𝑑𝑟
  Similmente al caso precedente

                                     𝑅𝑑𝑟   𝐿𝑒𝑛    𝐿𝑒𝑛                        𝑅𝑑𝑟                     𝐿𝑒𝑛 2
                    𝑇90% = 𝑘 2.3         𝑐     +𝑟                 𝐶𝑑𝑟 ℎ +           𝐶𝑑𝑟 ℎ     + 𝑟𝑐
                                      ℎ     𝑘      𝑘                          ℎ                       𝑘


                                  𝑅𝑑𝑟                       𝑅𝑑𝑟                             𝐿𝑒𝑛 2
                         = 2.3        𝑐𝐿𝑒𝑛 + 𝑟𝐿𝑒𝑛 𝐶𝑑𝑟 ℎ + 𝑘                 𝐶𝑑𝑟 ℎ   + 𝑟𝑐
                                   ℎ                         ℎ                               𝑘

  Cerchiamo la condizione di ottimo rispetto al dimensionamento del driver h
                                                          𝑑𝑇90%
                                                                =0
                                                           𝑑ℎ
                                                                                                             39




                                                            CIRCUITI
                                                       ELECTRONIC    E SISTEMI
                                                                  CICUITS FOR HIGH       40
                                                                                ELETTRONICI
                                                                                   FREQUENCIES

                            Dimensionamento ottimo dei ripetitori
 𝑑𝑇90%                           𝑑𝑇90%    𝑅𝑑𝑟 𝑐𝐿𝑒𝑛
       =0                              =−          + 𝑟𝐿𝑒𝑛 𝐶𝑑𝑟 = 0
  𝑑ℎ                              𝑑ℎ        ℎ2




                                                                         Notiamo che i termini che dipendono da
                                            𝑅𝑑𝑟 𝑐      𝑅𝑑𝑟 𝐶𝑖𝑛𝑡
                                  ℎ𝑜𝑡𝑡 =          =                      k non dipendono da h → quindi 𝑘𝑜𝑡𝑡 è
                                            𝑟𝐶𝑑𝑟       𝑅𝑖𝑛𝑡 𝐶𝑑𝑟          quello trovato in precedenza


 Sostituendo le espressioni di ℎ e 𝑘 nell’espressione di 𝑇90% troviamo:

                                       𝑇90% = 2 2.3 + 2.3 𝐿𝑒𝑛 𝑅𝑑𝑟 𝐶𝑑𝑟 𝑟𝑐


                                               𝑇90% ≈ 7.6𝐿𝑒𝑛 𝑅𝑑𝑟 𝐶𝑑𝑟 𝑟𝑐


                                                                                                             40
                                                                                    CIRCUITI
                                                                               ELECTRONIC    E SISTEMI
                                                                                          CICUITS FOR HIGH       41
                                                                                                        ELETTRONICI
                                                                                                           FREQUENCIES


   𝑇90% = 2.3 𝑅𝑑𝑟 𝑐𝐿𝑒𝑛 + 𝑟𝐿𝑒𝑛 𝐶𝑑𝑟 + 2𝐿𝑒𝑛 2.3𝑅𝑑𝑟 𝐶𝑑𝑟 𝑟𝑐                                      → ottimizzando numero di tratti di linea k e con dim.min.


   𝑇90% = 7.6𝐿𝑒𝑛 𝑅𝑑𝑟 𝐶𝑑𝑟 𝑟𝑐                   → ottimizzando numero di tratti di linea k e il dimensionamento dei driver h


 La seconda espressione mostra che il miglioramento di 𝑇90% è rilevante quando i ritardi 𝑅𝑑𝑟 𝑐𝐿𝑒𝑛 e 𝑟𝐿𝑒𝑛 𝐶𝑑𝑟
 sono molto diversi dopo la prima ottimizzazione



          𝑅𝑑𝑟 𝑐          𝑅𝑑𝑟 𝐶𝑖𝑛𝑡                  se 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 ≪ 𝑅𝑖𝑛𝑡 𝐶𝑑𝑟                                            Contraddice l’ipotesi alla base del
 ℎ𝑜𝑡𝑡 =         =                                                                                  ℎ≪1               dimensionamento degli stadi con h>1
          𝑟𝐶𝑑𝑟           𝑅𝑖𝑛𝑡 𝐶𝑑𝑟
                                                                                                                     che vorrebbe far diminuire la
                                                                                                                     resistenza      dei     driver    a
 In particolare il miglioramento di 𝑇90% è rilevante quando                                                          dimensionamento minimo

  𝑅𝑑𝑟 𝑐𝐿𝑒𝑛 ≫ 𝑟𝐿𝑒𝑛 𝐶𝑑𝑟
൝                                                             si verifica quando 𝑅𝑑𝑟 𝑐 ≫ 𝑟𝐶𝑑𝑟
 𝑅𝑑𝑟 𝑐𝐿𝑒𝑛 ≫ 𝐿𝑒𝑛 2.3𝑅𝑑𝑟 𝐶𝑑𝑟 𝑟𝑐

          2.3 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 𝑅𝑖𝑛𝑡 𝐶𝑑𝑟                                                                                                                                      41




                                                                                    CIRCUITI
                                                                               ELECTRONIC    E SISTEMI
                                                                                          CICUITS FOR HIGH       42
                                                                                                        ELETTRONICI
                                                                                                           FREQUENCIES

          Partizionamento di interconnessioni – ripetitori ad area minima
                   𝑉𝑖𝑛       𝑅𝑑𝑟                             𝑅𝑑𝑟                           𝑅𝑑𝑟                             𝑅𝑑𝑟
                                         𝑅𝑖𝑛𝑡 /𝑘                       𝑅𝑖𝑛𝑡 /𝑘                        𝑅𝑖𝑛𝑡 /𝑘                          𝑅𝑖𝑛𝑡 /𝑘            𝑅𝑑𝑟


                                    𝐶𝑖𝑛𝑡 /𝑘                 𝐶𝑑𝑟     𝐶𝑖𝑛𝑡 /𝑘                𝐶𝑑𝑟             𝐶𝑖𝑛𝑡 /𝑘               𝐶𝑖𝑛𝑡 /𝑘                𝐶𝑑𝑟          𝐶𝐿




                                                                                                                                𝑟𝑐𝐿2𝑒𝑛
                  𝑇90% = 2.3 𝑅𝑑𝑟 𝑐𝐿𝑒𝑛 + 𝑟𝐿𝑒𝑛 𝐶𝑑𝑟 + 2𝐿𝑒𝑛 2.3𝑅𝑑𝑟 𝐶𝑑𝑟 𝑟𝑐                                           𝑘𝑜𝑡𝑡 =
                                                                                                                              2.3𝑅𝑑𝑟 𝐶𝑑𝑟

 Partizionamento di interconnessioni – ripetitori a dimensionamento ottimo
            𝑉𝑖𝑛     𝑅𝑑𝑟 /ℎ                         𝑅𝑑𝑟 /ℎ                         𝑅𝑑𝑟 /ℎ                         𝑅𝑑𝑟 /ℎ                          𝑅𝑑𝑟 /ℎ
                                   𝑅𝑖𝑛𝑡 /𝑘                        𝑅𝑖𝑛𝑡 /𝑘                        𝑅𝑖𝑛𝑡 /𝑘                         𝑅𝑖𝑛𝑡 /𝑘


                             𝐶𝑖𝑛𝑡 /𝑘                ℎ𝐶𝑑𝑟 𝐶𝑖𝑛𝑡 /𝑘                   ℎ𝐶𝑑𝑟             𝐶𝑖𝑛𝑡 /𝑘               𝐶𝑖𝑛𝑡 /𝑘                ℎ𝐶𝑑𝑟           𝐶𝐿




                                                                                            𝑟𝑐𝐿2𝑒𝑛                         𝑅𝑑𝑟 𝑐           𝑅𝑑𝑟 𝐶𝑖𝑛𝑡
                  𝑇90% ≈ 7.6𝐿𝑒𝑛 𝑅𝑑𝑟 𝐶𝑑𝑟 𝑟𝑐                                    𝑘𝑜𝑡𝑡 =                          ℎ𝑜𝑡𝑡 =             =                                   42
                                                                                          2.3𝑅𝑑𝑟 𝐶𝑑𝑟                       𝑟𝐶𝑑𝑟            𝑅𝑖𝑛𝑡 𝐶𝑑𝑟
                                                               CIRCUITI
                                                          ELECTRONIC    E SISTEMI
                                                                     CICUITS FOR HIGH       43
                                                                                   ELETTRONICI
                                                                                      FREQUENCIES

  esempio




                                                                                                          43




                                                               CIRCUITI
                                                          ELECTRONIC    E SISTEMI
                                                                     CICUITS FOR HIGH       44
                                                                                   ELETTRONICI
                                                                                      FREQUENCIES

                                                  Ripetitori in cascata
Se possiamo considerare l’interconnessione come una pura capacità 𝐶𝑖𝑛𝑡 = 𝑐𝐿𝑒𝑛
Usiamo quanto già appreso in precedenza

            𝑅𝑑𝑟                    𝑅𝑑𝑟 /𝑓            𝑅𝑑𝑟 /𝑓 2                  𝑅𝑑𝑟 /𝑓 (𝑛−1) 𝑅
     𝑉𝑖𝑛                                                                                     𝑖𝑛𝑡
             1                     𝑓                 𝑓2                         𝑓 (𝑛−1)
                                                                                        𝐶𝑖𝑛𝑡
                     𝑓𝐶𝑖𝑛𝑡             𝑓 2 𝐶𝑖𝑛𝑡                 𝑓 (𝑛−1) 𝐶𝑖𝑛𝑡                         𝐶𝐿




 In questo caso i parametri di progetto sono:
 ❑ Il numero 𝑛 degli invertitori
 ❑ Il fattore 𝑓 di aumento progressivo dei dimensionamenti → step-up ratio

 Si nota come i primi 𝑛 − 1 stadi abbiano come carico la capacità di ingresso dello stadio che segue → dunque il
 loro ritardo sarà 2.3𝑓𝑅𝑑𝑟 𝐶𝑑𝑟
                                                                                                          44
                                                             CIRCUITI
                                                        ELECTRONIC    E SISTEMI
                                                                   CICUITS FOR HIGH       45
                                                                                 ELETTRONICI
                                                                                    FREQUENCIES

 L’ultimo invertitore che è connesso direttamente all’interconnessione avrà un ritardo dato da:

                                                                                                          𝑅𝑑𝑟
  se 𝐶𝐿 ≪ 𝐶𝑖𝑛𝑡 allora:      𝑇90% ≈ 𝑟𝑐𝐿𝑒𝑛 2 + 2.3𝑅𝑑𝑟 𝑐𝐿𝑒𝑛                          𝑇90% = 𝑟𝑐𝐿𝑒𝑛 2 + 2.3          𝑐𝐿
                                                                                                         𝑓 (𝑛−1) 𝑒𝑛


 E dunque il ritardo complessivo sarà dato da

                                                                          𝑅𝑑𝑟
                                    𝑇90% = 2.3 𝑛 − 1 𝑓𝑅𝑑𝑟 𝐶𝑑𝑟 + 2.3             𝐶 + 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                                                         𝑓 (𝑛−1) 𝑖𝑛𝑡

                                                                           𝑅𝑑𝑟
                                    𝑇90% = 2.3 𝑛 − 1 𝑓𝑅𝑑𝑟 𝐶𝑑𝑟 + 2.3             𝑐𝐿 + 𝑟𝑐𝐿𝑒𝑛 2
                                                                         𝑓 (𝑛−1) 𝑒𝑛

 Il valore ottimo si ottiene annullando le derivate rispetto a 𝑛 e 𝑓

    𝑑𝑇90%                 ln 𝑓
          = 0 → 𝐶𝑑𝑟 − 𝑐𝐿𝑒𝑛 𝑛 = 0                                         𝐶𝑖𝑛𝑡      𝑐𝐿𝑒𝑛
      𝑑𝑛                   𝑓                                    𝑛 = ln        = ln
                                                            ൞            𝐶𝑑𝑟        𝐶𝑑𝑟
    𝑑𝑇90%            𝑐𝐿𝑒𝑛
          = 0 → 𝐶𝑑𝑟 − 𝑛 = 0                                               𝑓=𝑒
     𝑑𝑓               𝑓                                                                                               45




                                                             CIRCUITI
                                                        ELECTRONIC    E SISTEMI
                                                                   CICUITS FOR HIGH       46
                                                                                 ELETTRONICI
                                                                                    FREQUENCIES


                         𝑅𝑑𝑟                                                                          𝑐𝐿𝑒𝑛
𝑇90% = 𝑟𝑐𝐿𝑒𝑛 2 + 2.3          𝑐𝐿      sostituendo risultati trovati
                                                                              𝑇90% = 2.3𝑒𝑅𝑑𝑟 𝐶𝑑𝑟 ln        + 𝑟𝑐𝐿𝑒𝑛 2
                       𝑓 (𝑛−1) 𝑒𝑛            in precedenza                                             𝐶𝑑𝑟

                                                                                                      da confrontare con

 Si vede come l’approccio che prevede una cascata di invertitori:                    𝑇90% ≈ 2.3𝑅𝑑𝑟 𝑐𝐿𝑒𝑛 + 𝑟𝑐𝐿𝑒𝑛 2

 ❑ riduce drasticamente il termine legato al driver 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡
 ❑ non modifica il ritardo intrinseco della linea 𝑟𝑐𝐿𝑒𝑛 2 (che dipende quadraticamente dalla lunghezza della linea)


  L’utilità di questo approccio sarà efficacie nel caso in cui 2.3𝑅𝑑𝑟 𝑐𝐿𝑒𝑛 ≫ 𝑟𝑐𝐿𝑒𝑛 2




                                                                                                                      46
                                                                CIRCUITI
                                                           ELECTRONIC    E SISTEMI
                                                                      CICUITS FOR HIGH       47
                                                                                    ELETTRONICI
                                                                                       FREQUENCIES

 esempio




                                                                                                           47




                                                                CIRCUITI
                                                           ELECTRONIC    E SISTEMI
                                                                      CICUITS FOR HIGH       48
                                                                                    ELETTRONICI
                                                                                       FREQUENCIES

                                                  Alcuni risultati
𝑇90% di una linea RC in Al (𝜌𝐴𝑙 = 3𝜇Ω𝑐𝑚), 𝑐 = 3𝑝𝐹/𝑐𝑚, DRIVER: 𝑅𝑑𝑟 = 10𝑘Ω, 𝐶𝑑𝑟 = 3𝑓𝐹


                                              (𝑟 = 300Ω𝑐𝑚)                                (𝑟 = 18750Ω𝑐𝑚)




        ❑ Resistività r bassa → ritardo caso singolo buffer è lineare (non
          dominato da 𝑟𝑐𝐿𝑒𝑛 2 )
        ❑ Pilotaggio con driver ripetuti a dimensionamento minimo è poco
          efficacie
        ❑ Con driver ottimizzati, essendo 𝑅𝑑𝑟 𝑐 ≫ 𝑟𝐶𝑑𝑟 , 𝑇90% è molto minore                               48
                                                                     CIRCUITI
                                                                ELECTRONIC    E SISTEMI
                                                                           CICUITS FOR HIGH       49
                                                                                         ELETTRONICI
                                                                                            FREQUENCIES

                                                       Alcuni risultati
𝑇90% di una linea RC in polySi (𝜌𝑝𝑜𝑙𝑦𝑆𝑖 = 1000𝜇Ω𝑐𝑚), 𝑐 = 3𝑝𝐹/𝑐𝑚, DRIVER: 𝑅𝑑𝑟 = 10𝑘Ω, 𝐶𝑑𝑟 = 3𝑓𝐹


                                                  (𝑟 = 100𝑘Ω𝑐𝑚)                                                     (𝑟 = 625𝑘Ω𝑐𝑚)




        ❑ Ritardo intrinseco della linea dominante per lunghezze di circa 103 𝜇𝑚 → infatti il ritardo con singolo driver aumenta in
          modo quadratic con 𝐿𝑒𝑛
        ❑ Pilotaggio con cascata di driver risulta poco efficace vista l’importanza del ritardo intrinseco
        ❑ 𝑅𝑑𝑟 𝑐 paragonabile a 𝑟𝐶𝑑𝑟 → l’ottimizzazione dei dimensionamento dei ripetitori non produce un grande miglioramento 49
          rispetto al ripetitore minimo




                                                                     CIRCUITI
                                                                ELECTRONIC    E SISTEMI
                                                                           CICUITS FOR HIGH       50
                                                                                         ELETTRONICI
                                                                                            FREQUENCIES

                                                       Alcuni risultati
𝑇90% di una linea in Tungsten silicide (𝜌𝑊𝑆𝑖2 = 130𝜇Ω𝑐𝑚), 𝑐 = 3𝑝𝐹/𝑐𝑚, DRIVER: 𝑅𝑑𝑟 = 10𝑘Ω, 𝐶𝑑𝑟 = 3𝑓𝐹


                                                  (𝑟 = 13𝑘Ω𝑐𝑚)                                                      (𝑟 = 81.25𝑘Ω𝑐𝑚)




        ❑ Resistività intermedia tra polisilicio e alluminio → proprietà dei ritardi intermedia rispetto ai due casi precedenti



                                                                                                                                    50
                                                                 CIRCUITI
                                                            ELECTRONIC    E SISTEMI
                                                                       CICUITS FOR HIGH       51
                                                                                     ELETTRONICI
                                                                                        FREQUENCIES


                                   Interconnessioni a basse perdite
  Abbiamo visto come possiamo schematizzare un tratto ∆𝑥 di linea
            𝑟∆𝑥         𝑙∆𝑥
                                                        Sappiamo che l’induttanza è definita come rapporto 𝜃
                                                                                                           𝑖




                                                                                                 →
𝑉𝑖𝑛                                                        𝑉𝑜𝑢𝑡          𝑙 sarà quindi definita in base al flusso di campo
                                    𝑐∆𝑥
                                                                           magnetico per unità di lunghezza della linea




                                                                                                 →
                                                                       Questa definizione, che è corretta, risulta laboriosa
                                                                                        nel nostro caso

 Stimiamo 𝑙 sfruttando il fatto che: un conduttore immerso in un materiale isolante omogeneo si ha che
                                                                   1    𝜀𝑑𝑖 𝜇𝑑𝑖 𝜀𝑑𝑖
                                                            𝑙𝑐 =    2 =     2  ≈ 2
                                                                   𝑣𝑙    𝑣𝑙0    𝑣𝑙0

      ❑ dove 𝑣𝑙 è la velocità della luce nel dielettrico
                                                                                                                      51
      ❑ dove 𝑣𝑙0 è la velocità della luce nel vuoto




                                                                 CIRCUITI
                                                            ELECTRONIC    E SISTEMI
                                                                       CICUITS FOR HIGH       52
                                                                                     ELETTRONICI
                                                                                        FREQUENCIES


  Possiamo quindi calcolare il valore di
  induttanza per unità di lunghezza una volta
  nota la capacità per unità di lunghezza come:


                      1 1    1 𝜀𝑑𝑖 𝜇𝑑𝑖 1 𝜀𝑑𝑖
                 𝑙=      2 =       2  ≈    2
                      𝑐 𝑣𝑙   𝑐 𝑣𝑙0      𝑐 𝑣𝑙0




      Il sistema di equazioni che descrive il circuito RLC sarà


      𝜕𝑉 𝑥, 𝑡                𝜕𝐼 𝑥, 𝑡
              = −𝑟𝐼 𝑥, 𝑡 − 𝑙                                          𝜕 2 𝑉 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡      𝜕 2 𝑉 𝑥, 𝑡
        𝜕𝑥                     𝜕𝑡
      𝜕𝐼 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡                                                   2
                                                                                 = 𝑟𝑐         + 𝑙𝑐
                                                                          𝜕𝑥            𝜕𝑡             𝜕𝑡 2
              = −𝑐
        𝜕𝑥           𝜕𝑡                   ❑ Derivando rispetto a
                                            x la prima equazione                       𝜕𝑉 𝑥, 𝑡   1 𝜕 2 𝑉 𝑥, 𝑡
                                          ❑ Sostituendo nella                   = 𝑟𝑐           + 2
                                            seconda si ottiene                           𝜕𝑡     𝑣𝑙     𝜕𝑡 2           52
                                                           CIRCUITI
                                                      ELECTRONIC    E SISTEMI
                                                                 CICUITS FOR HIGH       53
                                                                               ELETTRONICI
                                                                                  FREQUENCIES


    𝜕 2 𝑉 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡   1 𝜕 2 𝑉 𝑥, 𝑡
               = 𝑟𝑐         +                     E’ un’equazione di propagazione con attenuazione
        𝜕𝑥 2          𝜕𝑡      𝑣𝑙2 𝜕𝑡 2



                                                                                       𝑉 𝑥, 𝑡 → 𝑉 𝑥, 𝜔
    Risulta conveniente trasformare il tempo nel dominio delle frequenze           ቊ
                                                                                        𝐼 𝑥, 𝑡 → 𝐼 𝑥, 𝜔




     𝜕𝑉 𝑥, 𝑡                𝜕𝐼 𝑥, 𝑡                                    𝜕𝑉 𝑥, 𝜔
             = −𝑟𝐼 𝑥, 𝑡 − 𝑙                                                    = − 𝑟 + 𝑗𝜔𝑙 𝐼 𝑥, 𝜔
       𝜕𝑥                     𝜕𝑡                                         𝜕𝑥
     𝜕𝐼 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡                                              𝜕𝐼 𝑥, 𝜔
             = −𝑐                                                              = −𝑗𝜔𝑐𝑉 𝑥, 𝜔
       𝜕𝑥           𝜕𝑡
                                    Trasformo nel dominio delle           𝜕𝑥
                                            frequenze

                                                                         Equazione dei telegrafisti
                                                                          (con conduttanza g=0)


                                                                                                                53




                                                           CIRCUITI
                                                      ELECTRONIC    E SISTEMI
                                                                 CICUITS FOR HIGH       54
                                                                               ELETTRONICI
                                                                                  FREQUENCIES


Sfruttiamo il fatto che, per una generica linea RLC (anche con una eventuale conduttanza g in parallelo al
condensatore), si può dimostrare che per una linea infinitamente lunga

        𝑉 𝑥, 𝜔                                                                           𝑟 + 𝑗𝜔𝑙      𝑟 + 𝑗𝜔𝑙
               =𝑍 𝜔        impedenza generalizzata                dove      𝑍 𝜔 =                ≈
        𝐼 𝑥, 𝜔                                                                           𝑔 + 𝑗𝜔𝑐        𝑗𝜔𝑐
                           non dipende dalla sezione x!!

       e dove      𝑉 𝑥, 𝜔 = 𝑉 0, 𝜔 𝑒 − 𝑗𝜔𝑐 𝑟+𝑗𝜔𝑙 𝑥
                                             𝛾 𝜔 costante di propagazione


Restringiamo l’analisi nel caso in cui       𝑟 ≪ 𝜔𝑙

In altre parole stiamo analizzando il comportamento alle alte frequenze (più alte di 𝑟/𝑙)


                   𝑗𝜔𝑙            𝑙   1                      In questo caso l’impedenza
        𝑍 𝜔 ≈          = 𝑍0 =       =    = 𝑣𝑙 𝑙               caratteristica è reale e non
                   𝑗𝜔𝑐            𝑐 𝑣𝑙 𝑐
                                                                     dipende da 𝜔
                                                                                                                54
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       55
                                                                           ELETTRONICI
                                                                              FREQUENCIES


In questo caso la costante di propagazione diventa

                                                                           𝑟 𝑐
                                      𝛾 𝜔 =    𝑗𝜔𝑐 𝑟 + 𝑗𝜔𝑙 ≈ 𝑗𝜔 𝑙𝑐 +
                                                                           2 𝑙


                           1
                    𝑣𝑙 =
                           𝑙𝑐                          𝜔   𝑟
ricordando che                                𝛾 𝜔 ≈𝑗     +
                           𝑙                           𝑣𝑙 2𝑍0
                    𝑍0 =
                           𝑐


                                                                          𝜔     𝑟
                                                                        −𝑗 𝑥 −
 e dunque il potenziale risulta   𝑉 𝑥, 𝜔 = 𝑉 0, 𝜔 𝑒 −𝛾 𝜔 𝑥 = 𝑉 0, 𝜔 𝑒     𝑣𝑙 𝑒 2𝑍0 𝑥



                                                           = 𝑉 0, 𝜔 𝑒 −𝑗𝜔𝑡𝑓𝑙 𝑒 −𝛼𝑥
  ❑ dove 𝑡𝑓𝑙 = 𝑥 Τ𝑣𝑙 è il tempo di volo
  ❑ dove 𝛼 = 𝑟Τ2𝑍0 è la costante di attenuazione                                                       55




                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       56
                                                                           ELETTRONICI
                                                                              FREQUENCIES

                                          𝑉 𝑥, 𝜔 = 𝑉 0, 𝜔 𝑒 −𝑗𝜔𝑡𝑓𝑙 𝑒 −𝛼𝑥


  ❑ Il potenziale presenta un termine di sfasamento nel
    dominio delle frequenze 𝑒 −𝑗𝜔𝑡𝑓𝑙 → un ritardo nel
    dominio del tempo che dipende dalla posizione x ( infatti
    𝑡𝑓𝑙 = 𝑥 Τ𝑣𝑙 )
  ❑ tale ritardo non dipende dalla frequenza → linea non
    dispersiva
  ❑ C’è un termine di attenuazione esponenziale 𝑒 −𝛼𝑥 : onda
    iniettata al tempo t=0 alla sezione x=0 raggiunge la
    generica sezione x con attenuazione che dipende dal
    rapporto tra resistività per unità di lunghezza r e
    l’impedenza caratteristica 𝑍0

  ❑ Visto che abbiamo assunto 𝑟 ≪ 𝜔𝑙 stiamo facendo un’analisi in frequenza valida per “alte“ frequenze.
      ❑ → questo approccio non descrive completamente la linea di trasmissione e non è sufficiente per
        calcolare la risposta dell’interconnessione ad un gradino di tensione
                                                                                                       56
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       57
                                                                             ELETTRONICI
                                                                                FREQUENCIES


❑ Tornando alla linea di lunghezza infinita con stimolo in ingresso dato da un gradino di potenziale, la tensione
  al tempo t e sezione x sarà data da:

                                                   𝑥                              0𝑦 ≤0
              𝑉 𝑥, 𝑡 = 𝑉0 𝑒 −𝛼𝑥 + 𝑓𝑠𝑙 𝑥, 𝑡 𝑢 𝑡 −                             𝑢 𝑦 ቊ
                                                   𝑣𝑙                             1𝑦 ≥0

                     = 𝑉0 𝑒 −𝛼𝑥 + 𝑓𝑠𝑙 𝑥, 𝑡 𝑢 𝑡 − 𝑡𝑓𝑙                        𝑓𝑠𝑙 𝑥, 𝑡 è una generica funzione lentamente
                                                                            variabile sulle scale temporali di un tempo di
                                                                            volo 𝑡𝑓𝑙 e tale che
                                                                                  lim 𝑒 −𝛼𝑥 + 𝑓𝑠𝑙 𝑥, 𝑡   →1
                                                                                  𝑡→∞



                                               𝑉 𝑥, 𝑡 è costituito da:

                                               ❑ una componente 𝑉0 𝑒 −𝛼𝑥 che raggiunge 𝑥 in un tempo 𝑡𝑓𝑙

                                               ❑ una componente lenta 𝑓𝑠𝑙 𝑥, 𝑡 che garantisce il raggiungimento
                                                 di 𝑉0 in un tempo sufficientemente lungo
                                                                                                                57




                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       58
                                                                             ELETTRONICI
                                                                                FREQUENCIES

                Linea con forti perdite e a basse perdite

               Fortemente dispersiva                                           Basse perdite
                      𝑒 −𝛼𝐿𝑒𝑛 < 0.08                                             𝑒 −𝛼𝐿𝑒𝑛 > 0.78
                →




                                                                            →




                     𝑟𝐿𝑒𝑛                                                       𝑟𝐿𝑒𝑛
                          > 2.5                                                      < 0.25
                     2𝑍0                                                        2𝑍0
                →




                                                                            →




                               𝑍0                                                          𝑍0
                     𝐿𝑒𝑛 > 5                                                       𝐿𝑒𝑛 <
                               𝑟                                                           2𝑟
              poco meno del 10% dell’onda                                quasi l’80% dell’onda iniettata
              iniettata raggiunge l’uscita                               raggiunge l’uscita della linea
              della linea in un tempo pari a                             in un tempo pari a 𝑡𝑓𝑙
              𝑡𝑓𝑙
                                                                                                                58
                                                                CIRCUITI
                                                           ELECTRONIC    E SISTEMI
                                                                      CICUITS FOR HIGH       1
                                                                                    ELETTRONICI
                                                                                       FREQUENCIES


                                                Interconnessioni rlc
      Abbiamo visto come possiamo schematizzare un tratto ∆𝑥 di linea
                𝑟∆𝑥           𝑙∆𝑥                                                                                          𝜃
                                                                   Sappiamo che l’induttanza è definita come rapporto
                                                                                                                           𝑖




                                                                                               →
                                                                       𝑙 sarà quindi definita in base al flusso di campo
𝑉𝑖𝑛                                 𝑐∆𝑥                    𝑉𝑜𝑢𝑡          magnetico per unità di lunghezza della linea




                                                                                               →
                                                                    Questa definizione, che è corretta, risulta laboriosa
                                                                    nel nostro caso (nelle prossime slide vediamo come
                                                                         ricavare un’espressione più agevole per 𝑙)

      Il sistema di equazioni che descrive il circuito RLC sarà
      𝜕𝑉 𝑥, 𝑡                𝜕𝐼 𝑥, 𝑡
              = −𝑟𝐼 𝑥, 𝑡 − 𝑙                                       𝜕 2 𝑉 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡      𝜕 2 𝑉 𝑥, 𝑡
        𝜕𝑥                     𝜕𝑡
      𝜕𝐼 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡                                                2
                                                                              = 𝑟𝑐         + 𝑙𝑐
                                                                       𝜕𝑥            𝜕𝑡             𝜕𝑡 2
              = −𝑐
        𝜕𝑥           𝜕𝑡                   ❑ Derivando rispetto a
                                            x la prima equazione
                                          ❑ Sostituendo nella                                                       1
                                            seconda si ottiene




                                                                CIRCUITI
                                                           ELECTRONIC    E SISTEMI
                                                                      CICUITS FOR HIGH       2
                                                                                    ELETTRONICI
                                                                                       FREQUENCIES

  DIMOSTRAZIONE




                                                                                                                    2
                                                           CIRCUITI
                                                      ELECTRONIC    E SISTEMI
                                                                 CICUITS FOR HIGH       3
                                                                               ELETTRONICI
                                                                                  FREQUENCIES


                                           Interconnessioni rlc
Ora notiamo che nel caso particolare in cui 𝑟=0 si ha che:

 𝜕 2 𝑉 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡      𝜕 2 𝑉 𝑥, 𝑡            𝜕 2 𝑉 𝑥, 𝑡      𝜕 2 𝑉 𝑥, 𝑡
        2
            = 𝑟𝑐         + 𝑙𝑐                                  = 𝑙𝑐
     𝜕𝑥            𝜕𝑡             𝜕𝑡 2                  𝜕𝑥 2            𝜕𝑡 2
                                            Questa equazione per linea non-dissipativa assomiglia all’equazione di
                                            propagazione di un’onda (equazione di d'Alembert):

                                                             1 𝜕 2 𝑢(𝒓, 𝑡)          caso 1D     𝜕 2 𝑢 𝑥, 𝑡   1 𝜕 2 𝑢(𝑥, 𝑡)
                                              ∇2 𝑢(𝒓, 𝑡) −                 =0                              −               =0
                                                             𝑣 2 𝜕𝑡 2                               𝜕𝑥 2     𝑣 2 𝜕𝑡 2

                                            dove 𝑢(𝑥, 𝑡) rappresenta l’intensità dell’onda nel punto 𝑥 e al tempo 𝑡 e
                                            con 𝑣 : velocità di propagazione dell’onda nel mezzo.


                                                                                               1
                                                                         E dunque:      𝑙𝑐 =
                                                                                               𝑣𝑙2


                                                                                                                        3




                                                           CIRCUITI
                                                      ELECTRONIC    E SISTEMI
                                                                 CICUITS FOR HIGH       4
                                                                               ELETTRONICI
                                                                                  FREQUENCIES


                                                Alcuni esempi
        Linea coassiale                            Linea coplanare                                        Linea bifilare

                        𝑟2                                       𝑟                                          𝑟              𝑟
                                                                                                                 ℎ
                   𝑟1                                        ℎ
                                                                                                                  2𝜋𝜀
                                                                                                       𝑐=
                                                                                                                    ℎ2 − 2𝑟
                                                    2𝜋𝜀                    𝜇        ℎ                        cosh−1
          2𝜋𝜀                                                                                                         2𝑟 2
     𝑐=                     𝜇 𝑟2             𝑐=                      𝑙=      cosh−1
             𝑟          𝑙=   ln                          ℎ                2𝜋        𝑟                       𝜇         ℎ2 − 2𝑟
          ln 𝑟2            2𝜋 𝑟1                  cosh−1 𝑟                                              𝑙=     cosh−1
              1                                                                                            2𝜋           2𝑟 2
             1                                           1                                                 1
      𝑙𝑐 =       = 𝜀𝜇 = 𝜀𝑑𝑖 𝜇𝑑𝑖 𝜀0 𝜇0             𝑙𝑐 =       = 𝜀𝜇 = 𝜀𝑑𝑖 𝜇𝑑𝑖 𝜀0 𝜇0                    𝑙𝑐 = 2 = 𝜀𝜇 = 𝜀𝑑𝑖 𝜇𝑑𝑖 𝜀0 𝜇0
             𝑣𝑙2                                         𝑣𝑙2                                              𝑣𝑙
                                 1                                           1                                               1
                      = 𝜀𝑑𝑖 𝜇𝑑𝑖 2                                 = 𝜀𝑑𝑖 𝜇𝑑𝑖 2                                      = 𝜀𝑑𝑖 𝜇𝑑𝑖 2
                                𝑣0                                          𝑣0                                               𝑣0

La velocità di propagazione di una onda in questi casi è pari alla velocità della luce nel mezzo che riempie la linea e
NON dipende dalle caratteristiche geometriche della linea!
                                                                                                                4
Si può dimostrare che lo stesso vale anche per linee non-distorcenti (𝑟𝑐 = 𝑔𝑙) o per segnali ad «alte frequenze»
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       5
                                                                              ELETTRONICI
                                                                                 FREQUENCIES


                                                 Alcune note
Si può dimostrare che solamente nei casi di linea non dispersiva (𝑟 = 0) oppure non-distorcenti (𝑟𝑐 = 𝑔𝑙) per
segnali ad «alte frequenze» (𝑟 ≪ 𝜔𝑙) la velocità di propagazione di un segnale non dipende dalla sua pulsazione
𝜔. In termini generali, invece, la velocità di propagazione può dipendere dalla pulsazione del segnale
     → un segnale generico (che può essere scomposto nelle sue componenti armoniche mediante trasformata di
        Fourier) verrà tanto più distorto quanto è lunga la linea di trasmissione dato che le sue componenti spettrali
        viaggeranno a velocità diverse nella linea di trasmissione!




                                                                                                               5




                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       6
                                                                              ELETTRONICI
                                                                                 FREQUENCIES



Possiamo quindi calcolare il valore di induttanza per unità di lunghezza una volta nota la capacità per unità di
lunghezza come:


                                                    1 1    1 𝜀𝑑𝑖 𝜇𝑑𝑖 1 𝜀𝑑𝑖
                                               𝑙=      2 =       2  ≈    2
                                                    𝑐 𝑣𝑙   𝑐 𝑣𝑙0      𝑐 𝑣𝑙0




                                                                                                               6
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       7
                                                                              ELETTRONICI
                                                                                 FREQUENCIES


    𝜕 2 𝑉 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡   1 𝜕 2 𝑉 𝑥, 𝑡
               = 𝑟𝑐         +                    E’ un’equazione di propagazione con attenuazione
        𝜕𝑥 2          𝜕𝑡      𝑣𝑙2 𝜕𝑡 2


   Assumiamo che la linea di trasmissione sia
   connessa ad un generatore di tensione                                          L’unico parametro è x!
                                                              𝑉 𝑥, 𝑡 → 𝑉𝜔 𝑥
   sinusoidale con pulsazione 𝜔 → passo al                ቊ                       Nel caso di scomposizione di un segnale
                                                              𝐼 𝑥, 𝑡 → 𝐼𝜔 𝑥
   regime armonico introducendo i fasori                                          con Fourier, ∀𝜔 avrò un set di equazioni.
   complessi 𝑉𝜔 𝑥 e 𝐼𝜔 𝑥


    𝜕𝑉 𝑥, 𝑡                𝜕𝐼 𝑥, 𝑡                                     𝑑𝑉𝜔 𝑥
            = −𝑟𝐼 𝑥, 𝑡 − 𝑙                                                     = − 𝑟 + 𝑗𝜔𝑙 𝐼𝜔 𝑥
      𝜕𝑥                     𝜕𝑡                                          𝑑𝑥
    𝜕𝐼 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡                                                 𝑑𝐼𝜔 𝑥
            = −𝑐                                                                 = −𝑗𝜔𝑐𝑉𝜔 𝑥
      𝜕𝑥           𝜕𝑡
                                   Trasformo nel dominio delle              𝑑𝑥
                                           frequenze

                                                                          Equazione dei telegrafisti
                                                                           (con conduttanza g=0)

                                                                       Questa equazione va scritta
                                                                        per ogni pulsazione 𝜔 !!                 7




                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       8
                                                                              ELETTRONICI
                                                                                 FREQUENCIES


Sfruttiamo il fatto che, per una generica linea RLC (anche con una eventuale conduttanza g in parallelo al
condensatore), si può dimostrare che per una linea infinitamente lunga (cioè: senza onde riflesse)

        𝑉𝜔 𝑥                                                                           𝑟 + 𝑗𝜔𝑙         𝑟 + 𝑗𝜔𝑙
             =𝑍 𝜔         impedenza generalizzata                  dove       𝑍 𝜔 =            ≈
        𝐼𝜔 𝑥                                                                           𝑔 + 𝑗𝜔𝑐           𝑗𝜔𝑐
                          non dipende dalla sezione x!!

       e dove       𝑉𝜔 𝑥 = 𝑉𝜔 0 𝑒 − 𝑗𝜔𝑐 𝑟+𝑗𝜔𝑙 𝑥
                                             𝛾 𝜔 costante di propagazione

            Restringiamo l’analisi nel caso in cui 𝑟 ≪ 𝜔𝑙 (caso di basse perdite)

         In altre parole stiamo analizzando il comportamento alle alte frequenze (più alte di 𝑟/𝑙)


                          𝑗𝜔𝑙            𝑙   1                      In questo caso l’impedenza
                𝑍 𝜔 ≈         = 𝑍0 =       =    = 𝑣𝑙 𝑙              caratteristica è reale e non
                          𝑗𝜔𝑐            𝑐 𝑣𝑙 𝑐
                                                                           dipende da 𝝎
                                                                                                                 8
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       9
                                                                           ELETTRONICI
                                                                              FREQUENCIES


In questo caso (cioè se 𝑟 ≪ 𝜔𝑙 ) la costante di propagazione diventa

                                                                         𝑟 𝑐
                                      𝛾 𝜔 =    𝑗𝜔𝑐 𝑟 + 𝑗𝜔𝑙 ≈ 𝑗𝜔 𝑙𝑐 +
                                                                         2 𝑙


                           1
                    𝑣𝑙 =
                           𝑙𝑐                          𝜔   𝑟
ricordando che                                𝛾 𝜔 ≈𝑗     +
                           𝑙                           𝑣𝑙 2𝑍0
                    𝑍0 =
                           𝑐


                                                                    𝜔     𝑟
                                                                  −𝑗 𝑥 −
 e dunque il potenziale risulta   𝑉𝜔 𝑥 = 𝑉𝜔 0 𝑒 −𝛾 𝜔 𝑥 = 𝑉𝜔 0 𝑒     𝑣𝑙 𝑒 2𝑍0 𝑥



                                                       = 𝑉𝜔 0 𝑒 −𝑗𝜔𝑡𝑓𝑙 𝑒 −𝛼𝑥
  ❑ dove 𝑡𝑓𝑙 = 𝑥 Τ𝑣𝑙 è il tempo di volo
  ❑ dove 𝛼 = 𝑟Τ 2𝑍0 è la costante di attenuazione                                                          9




                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       10
                                                                           ELETTRONICI
                                                                              FREQUENCIES

                                          𝑉𝜔 𝑥 = 𝑉𝜔 0 𝑒 −𝑗𝜔𝑡𝑓𝑙 𝑒 −𝛼𝑥


  ❑ Il potenziale presenta un termine di sfasamento nel
    dominio delle frequenze 𝑒 −𝑗𝜔𝑡𝑓𝑙 → un ritardo nel
    dominio del tempo che dipende dalla posizione x ( infatti
    𝑡𝑓𝑙 = 𝑥 Τ𝑣𝑙 )
  ❑ tale ritardo non dipende dalla frequenza → linea non
    dispersiva
  ❑ C’è un termine di attenuazione esponenziale 𝑒 −𝛼𝑥 : onda
    iniettata al tempo t=0 alla sezione x=0 raggiunge la
    generica sezione x con attenuazione che dipende dal
    rapporto tra resistività per unità di lunghezza r e
    l’impedenza caratteristica 𝑍0

  ❑ Visto che abbiamo assunto 𝑟 ≪ 𝜔𝑙 stiamo facendo un’analisi in frequenza valida per “alte“ frequenze.
      ❑ → questo approccio non descrive completamente la linea di trasmissione e non è sufficiente per
        calcolare la risposta dell’interconnessione ad un gradino di tensione
                                                                                                       10
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       11
                                                                             ELETTRONICI
                                                                                FREQUENCIES


❑ Tornando alla linea di lunghezza infinita con stimolo in ingresso dato da un gradino di potenziale, la tensione
  al tempo t e sezione x sarà data da:

                                                   𝑥                              0𝑦 ≤0
              𝑉 𝑥, 𝑡 = 𝑉0 𝑒 −𝛼𝑥 + 𝑓𝑠𝑙 𝑥, 𝑡 𝑢 𝑡 −                             𝑢 𝑦 ቊ
                                                   𝑣𝑙                             1𝑦 ≥0

                     = 𝑉0 𝑒 −𝛼𝑥 + 𝑓𝑠𝑙 𝑥, 𝑡 𝑢 𝑡 − 𝑡𝑓𝑙                        𝑓𝑠𝑙 𝑥, 𝑡 è una generica funzione lentamente
                                                                            variabile sulle scale temporali di un tempo di
                                                                            volo 𝑡𝑓𝑙 e tale che
                                                                                  lim 𝑒 −𝛼𝑥 + 𝑓𝑠𝑙 𝑥, 𝑡   →1
                                                                                  𝑡→∞



                                               𝑉 𝑥, 𝑡 è costituito da:

                                               ❑ una componente 𝑉0 𝑒 −𝛼𝑥 che raggiunge 𝑥 in un tempo 𝑡𝑓𝑙

                                               ❑ una componente lenta 𝑓𝑠𝑙 𝑥, 𝑡 che garantisce il raggiungimento
                                                 di 𝑉0 in un tempo sufficientemente lungo
                                                                                                                11




                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       12
                                                                             ELETTRONICI
                                                                                FREQUENCIES

                Linea con forti perdite e a basse perdite

               Fortemente dispersiva                                           Basse perdite
                      𝑒 −𝛼𝐿𝑒𝑛 < 0.08                                             𝑒 −𝛼𝐿𝑒𝑛 > 0.78
                →




                                                                            →




                     𝑟𝐿𝑒𝑛                                                       𝑟𝐿𝑒𝑛
                          > 2.5                                                      < 0.25
                     2𝑍0                                                        2𝑍0
                →




                                                                            →




                               𝑍0                                                          𝑍0
                     𝐿𝑒𝑛 > 5                                                       𝐿𝑒𝑛 <
                               𝑟                                                           2𝑟
              poco meno del 10% dell’onda                                quasi l’80% dell’onda iniettata
              iniettata raggiunge l’uscita                               raggiunge l’uscita della linea
              della linea in un tempo pari a                             in un tempo pari a 𝑡𝑓𝑙
              𝑡𝑓𝑙
                                                                                                                12
                                                           CIRCUITI
                                                      ELECTRONIC    E SISTEMI
                                                                 CICUITS FOR HIGH       13
                                                                               ELETTRONICI
                                                                                  FREQUENCIES

                                     Linea senza perdite
          𝑟𝐿𝑒𝑛                                                                                 𝑙
    se         ≪1        → linea senza perdite/linea di trasmissione                con 𝑍0 =
          2𝑍0                                                                                  𝑐

    L’equazione che descrive la linea di trasmissione sarà

                    𝜕 2 𝑉 𝑥, 𝑡   1 𝜕 2 𝑉 𝑥, 𝑡        equazione delle onde
                               =
                        𝜕𝑥 2     𝑣𝑙2 𝜕𝑡 2


                                                 𝑥                                    La tensione ad una sezione
                            𝑉𝑓 𝑥, 𝑡 = 𝑉 0, 𝑡 −                   onda progressiva     della linea è sempre la
                                                𝑣𝑙
    soluzioni generali                                                                sovrapposizione di un’onda
                                                 𝑥𝑟 − 𝑥          onda regressiva
                            𝑉𝑟 𝑥, 𝑡 = 𝑉 𝑥𝑟 , 𝑡 −                                      progressiva e una regressiva
                                                   𝑣𝑙                                 pesata con opportuni coefficienti
                                                𝑥𝑟 sezione della linea dove
                                                viene    iniettata    l’onda
                                                regressiva
                                                                                                               13




                                                           CIRCUITI
                                                      ELECTRONIC    E SISTEMI
                                                                 CICUITS FOR HIGH       14
                                                                               ELETTRONICI
                                                                                  FREQUENCIES


NOTA

❑ La tensione ad una certa sezione della linea di lunghezza finita si comporta si comporta come se la
  linea fosse infinita fino all’istante in cui arriva la prima onda riflessa da una terminazione → infatti
  l’onda elettromagnetica si propaga ad una velocità finita e non può «sapere» cosa c’è davanti a se;

❑ Le forme d’onda sulla linea dipenderanno dalle condizioni con cui la linea viene eccitata e dal modo in
  cui viene terminata la linea

❑ Deriviamo un modello che ci consenta di studiare linee di lunghezza finita con riflessioni




                                                                                                               14
                                                                 CIRCUITI
                                                            ELECTRONIC    E SISTEMI
                                                                       CICUITS FOR HIGH       15
                                                                                     ELETTRONICI
                                                                                        FREQUENCIES

                                     Linea pilotata da un driver
                 𝑅𝑠
                                                                                                              𝑍0
                                                                                      SORGENTE 𝑉𝑆 =               𝑉 = 𝑉𝑖
                                                                                                           𝑅𝑠 + 𝑍0 0

𝑉0                    𝑉𝑠                 𝑉𝑃                𝑉𝑡𝐿          𝑍𝐿                                    𝑍0
                                                                                      GENERICO      𝑉𝑃 =           2𝑉 = 𝑉𝑖
                                                                                       PUNTO
                                                                                                            𝑍0 + 𝑍0 𝑖

                                                                                                              𝑍𝐿
                                                                                                    𝑉𝑡𝐿 =          2𝑉
                                                                                      CARICO
                                                                                                            𝑍0 + 𝑍𝐿 𝑖
                           𝑅𝑠 𝑉               𝑍0     𝑉𝑃            𝑍0
                               𝑠                                        𝑉𝑡𝐿             Tensione al carico: è la somma tra
                                                                                        onda incidente 𝑉𝑖 e onda 𝑉𝑟𝐿 riflessa
           𝑉0              𝑍0      2𝑉𝑖                    2𝑉𝑖                           dal carico verso la linea
                                               𝑍0                            𝑍𝐿
                                                                                                 𝑉𝑡𝐿 = 𝑉𝑖 + 𝑉𝑟𝐿


                                                                                                                    15




                                                                 CIRCUITI
                                                            ELECTRONIC    E SISTEMI
                                                                       CICUITS FOR HIGH       16
                                                                                     ELETTRONICI
                                                                                        FREQUENCIES


                                                      𝑍𝐿               𝑍𝐿 − 𝑍0
     𝑉𝑡𝐿 = 𝑉𝑖 + 𝑉𝑟𝐿        →    𝑉𝑟𝐿 = 𝑉𝑡𝐿 − 𝑉𝑖 =
                                                    𝑍0 + 𝑍𝐿
                                                            2𝑉𝑖 − 𝑉𝑖 =         𝑉 = 𝜌𝐿 𝑉𝑖
                                                                       𝑍𝐿 + 𝑍0 𝑖
                                                                                                 𝜌𝐿 coefficiente dei
                                                                                                 riflessione al carico



                                                    𝑉𝑡𝐿 = 𝑉𝑖 + 𝑉𝑟𝐿 = 𝑉𝑖 1 + 𝜌𝐿


       ❑ Quando l’onda regressiva arriva alla sorgente, ci sarà un’altra riflessione
                                                                     𝑅𝑆 − 𝑍0
       ❑ Definiamo in coefficiente di riflessione alla sorgente 𝜌𝑆 = 𝑅 + 𝑍
                                                                             𝑆    0

         L’onda 𝑉𝑟𝑆 riflessa alla sorgente verso la linea e quella 𝑉𝑡𝑆 trasmessa dalla linea alla sorgente
         saranno:

            𝑉 = 𝜌𝑆 𝑉𝑖
           ቊ 𝑟𝑆
            𝑉𝑡𝑆 = 1 + 𝜌𝑆 𝑉𝑖
                                                                                                                    16
                                      CIRCUITI
                                 ELECTRONIC    E SISTEMI
                                            CICUITS FOR HIGH       17
                                                          ELETTRONICI
                                                             FREQUENCIES

                               Esempio
     𝑅𝑠 ≪ 𝑍0
                                                              𝑍𝐿 − 𝑍0
                                                       𝜌𝐿 =           → +1
                                                              𝑍𝐿 + 𝑍0
𝑉0                                   𝑍𝐿 ≫ 𝑍0
                                                              𝑅𝑆 − 𝑍0
                                                       𝜌𝑆 =           → −1
                                                              𝑅𝑆 + 𝑍0


                             ❑ Andamento oscillatorio al carico → indesiderato

                             ❑ Definiamo il 𝑡𝑠𝑡𝑙 il settling time come tempo necessario affinché la
                               tensione sul carico si mantenga entro un certo specificato intervallo
                               intorno al valore di regime (esempio 10%)

                             ❑ Un tempo 𝑡𝑠𝑡𝑙 maggiore del tempo di volo implica un ritardo non
                               ottimo per il circuito perchè maggiore di quello strettamente
                               indispensabile per la propagazione del segnale sulla linea

                                                                                        17




                                      CIRCUITI
                                 ELECTRONIC    E SISTEMI
                                            CICUITS FOR HIGH       18
                                                          ELETTRONICI
                                                             FREQUENCIES

                    Adattamento al carico
     𝑅𝑠 ≪ 𝑍0                                                  𝑍𝐿 − 𝑍0
                                                       𝜌𝐿 =           →0
                                                              𝑍𝐿 + 𝑍0
                                                              𝑅𝑆 − 𝑍0
𝑉0                                  𝑍𝐿 = 𝑍0            𝜌𝑆 =           → −1
                                                              𝑅𝑆 + 𝑍0


                                                    𝑉𝑡𝐿 𝑡 = 𝑡𝑓𝑙 = 𝑉𝑠 𝑡 = 0


                                  ❑ In un tempo di volo tutti i transitori sono esauriti e
                                    trasferiamo tutta la tensione al carico


               𝑡𝑠𝑡𝑙 = 1𝑡𝑓𝑙



                                                                                        18
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       19
                                                                            ELETTRONICI
                                                                               FREQUENCIES

                            Adattamento alla sorgente
         𝑅𝑠 = 𝑍0                                                                     𝑍𝐿 − 𝑍0
                                                                              𝜌𝐿 =           →1
                                                                                     𝑍𝐿 + 𝑍0
                                                                                     𝑅𝑆 − 𝑍0
𝑉0                                                     𝑍𝐿 ≫ 𝑍0                𝜌𝑆 =           →0
                                                                                     𝑅𝑆 + 𝑍0

                                                                  𝑉0
                                                          𝑉𝑆 0 =
                                                                   2
                                                          𝑉𝑡𝐿 𝑡 = 𝑡𝑓𝑙 = 𝑉𝑠 0         1 + 𝜌𝐿 = 𝑉0

                                                                                   𝑉0
                                                          𝑉𝑟𝐿 𝑡 = 𝑡𝑓𝑙 = 𝑉𝑠 0 𝜌𝐿 =
                                                                                    2
                                                                                  𝑉0
                                                          𝑉𝑡𝑆 𝑡 = 2𝑡𝑓𝑙   = 𝑉𝑠 0 +     1 + 𝜌𝑆 = 𝑉0
                                                                                  2
                           𝑡𝑠𝑡𝑙 = 1𝑡𝑓𝑙
                                                    ❑ In un tempo di volo tutti i transitori sono esauriti e
                                                      trasferiamo tutta la tensione al carico
                                                                                                        19




                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       20
                                                                            ELETTRONICI
                                                                               FREQUENCIES

                        Linea come semplice capacità
❑ Quando possiamo considerare la linea come semplice capacità?

     ▪ quando il tempo di salita e discesa del segnale in ingresso alla linea è grande rispetto a 𝑡𝑓𝑙

❑ Consideriamo un driver con 𝑡𝑟 il tempo di salita del segnale di ingresso alla linea pilotata dal driver

                                 𝐿𝑒𝑛                                     𝑡𝑟          𝑣𝑙 𝑡𝑟
             𝑡𝑟 > 2.5𝑡𝑓𝑙 = 2.5       = 2.5𝐿𝑒𝑛 𝑙𝑐       →     𝐿𝑒𝑛 <
                                                                     2.5 𝑙𝑐
                                                                                =
                                                                                     2.5
                                  𝑣𝑙




                                                                                                        20
                                                                         CIRCUITI
                                                                    ELECTRONIC    E SISTEMI
                                                                               CICUITS FOR HIGH       21
                                                                                             ELETTRONICI
                                                                                                FREQUENCIES

                     SORGENTE                            CARICO                          DIAGRAMMA A RETICOLO
                 𝑉𝑠0 0                                               0
                                            𝑉𝑠0
                                                                                                ❑ Al carico arriveranno contributi a
                       1                                             1    𝑉𝑡𝐿 𝑡𝑓𝑙 =               numeri dispari del tempo di volo,
                                          𝜌𝐿 𝑉𝑠0                                                  mentre alla sorgente a numeri pari
                                                                         𝑉𝑠0 1 + 𝜌𝐿
                                                                                                  del tempo di volo
    𝑉𝑡𝑆 2𝑡𝑓𝑙 =         2                                             2
   𝜌𝐿 𝑉𝑠0 1 + 𝜌𝑠                          𝜌𝑠 𝜌𝐿 𝑉𝑠0

                       3                                             3      𝑉𝑡𝐿 3𝑡𝑓𝑙 =
                                        𝜌𝑠 𝜌𝐿 2 𝑉𝑠0                      𝜌𝑠 𝜌𝐿 𝑉𝑠0 1 + 𝜌𝐿         𝑉𝑡𝐿 𝑛𝑡𝑓𝑙 e 𝑉𝑡𝑆 2𝑡𝑓𝑙 sono tensioni
                                                                                                  TRASMESSE al carico e sorgente
   𝑉𝑡𝑆 4𝑡𝑓𝑙 =                                                                                     rispettivamente. Non sono le
                       4                𝜌𝑠 2 𝜌𝐿 2 𝑉𝑠0                4                            tensioni assolute che ho in un
𝜌𝑠 𝜌𝐿 2 𝑉𝑠0 1 + 𝜌𝑠
                                                                                                  determinato istante al carico o
                                                                              𝑉𝑡𝐿 5𝑡𝑓𝑙 =          sorgente! (vedi prossima slide)
                       5                                             5
                                                                         𝜌𝑠 2 𝜌𝐿 2 𝑉𝑠0 1 + 𝜌𝐿

                     𝑡ൗ                                 𝑡ൗ                                                                 21
                       𝑡𝑓𝑙                                𝑡𝑓𝑙




                                                                         CIRCUITI
                                                                    ELECTRONIC    E SISTEMI
                                                                               CICUITS FOR HIGH       22
                                                                                             ELETTRONICI
                                                                                                FREQUENCIES


                                                        ∞

                     𝑉𝐿 𝑡 = 𝑉𝑡𝐿 𝑡𝑓𝑙 𝑢 𝑡 − 𝑡𝑓𝑙 + ෍ 𝑉𝑡𝐿 𝑡𝑓𝑙 + 2𝑛𝑡𝑓𝑙 𝑢 𝑡 − 𝑡𝑓𝑙 + 2𝑛𝑡𝑓𝑙
                                                        𝑛=1
                                                              ∞

                             = 1 + 𝜌𝐿 𝑉𝑠0 𝑢 𝑡 − 𝑡𝑓𝑙 + ෍ 1 + 𝜌𝐿              𝜌𝑆 𝜌𝐿 𝑛 𝑉𝑠0 𝑢 𝑡 − 𝑡𝑓𝑙 + 2𝑛𝑡𝑓𝑙
                                                              𝑛=1


                             = 1 + 𝜌𝐿 𝑉𝑠0 𝑢 𝑡 − 𝑡𝑓𝑙 + 1 + 𝜌𝐿 𝜌𝑆 𝜌𝐿 𝑉𝑠0 𝑢 𝑡 − 3𝑡𝑓𝑙 + 1 + 𝜌𝐿 𝜌𝑆 𝜌𝐿 2 𝑉𝑠0 𝑢 𝑡 − 5𝑡𝑓𝑙 + ⋯


                                           ∞

                      𝑉𝑆 𝑡 = 𝑉𝑆0 𝑢 𝑡 + ෍ 𝑉𝑡𝑆 2𝑛𝑡𝑓𝑙 𝑢 𝑡 − 2𝑛𝑡𝑓𝑙
                                          𝑛=1
                                           ∞

                              = 𝑉𝑆0 𝑢 𝑡 + ෍ 1 + 𝜌𝑆 𝜌𝑆 𝑛−1 𝜌𝐿 𝑛 𝑉𝑠0 𝑢 𝑡 − 2𝑛𝑡𝑓𝑙
                                          𝑛=1

 ❑ Notiamo come, per definizione, i termini 𝜌𝑆 e 𝜌𝐿 hanno modulo minore di 1 → elevandoli a potenza diventano
   sempre più piccoli → ho una serie convergente
 ❑ Per avere convergenza più rapida, uno dei due coefficienti di riflessione deve tendere a zero → caso limite si
   ha quando 𝜌𝐿 = 0 cioè non ho riflessione al carico                                                      22
                                CIRCUITI
                           ELECTRONIC    E SISTEMI
                                      CICUITS FOR HIGH       23
                                                    ELETTRONICI
                                                       FREQUENCIES




Driver troppo conduttivo                       Driver poco conduttivo
                                                                        23
