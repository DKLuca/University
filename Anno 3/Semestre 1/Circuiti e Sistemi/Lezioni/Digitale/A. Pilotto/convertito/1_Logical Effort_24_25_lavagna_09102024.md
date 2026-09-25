---
fonte: "1_Logical Effort_24_25_lavagna_09102024.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       1
                                                                            ELETTRONICI
                                                                               FREQUENCIES




Alessandro Pilotto
alessandro.pilotto@uniud.it

Ufficio: A1 51 (primo piano, zona ex-biblioteca)
Lab:     B1 25 (primo piano)

24 CFU (da inizio ottobre a metà novembre)
• Metodologia del Logical Effort
• Interconnessioni

Materiale didattico su elearning

Ricevimento su appuntamento

NanoElectronic DEvices and Circuits
nanoelectronics.uniud.it

                                                                                             1
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       2
                                                                           ELETTRONICI
                                                                              FREQUENCIES


                            Metodologia del Logical Effort
❑ Data una funzione logica i chip designer si devono chiedere quale sia la miglior topologia del circuito →
  qui ci occuperemo solamente di gate logici realizzati in tecnologia CMOS
❑ Scelta la topologia bisogna dimensionare i transistori (che dimensioni fisiche devono avere? Transistori
  con area molto grande avranno correnti di output grandi, ma anche capacità di ingresso grandi!)

❑ Come possiamo minimizzare il
  ritardo di un segnale che attraversa
  i gate logici?




                                                                                                          2
                                                     CIRCUITI
                                                ELECTRONIC    E SISTEMI
                                                           CICUITS FOR HIGH       3
                                                                         ELETTRONICI
                                                                            FREQUENCIES


                          Metodologia del Logical Effort
→ La metodologia del Logical Effort consente di dare una prima risposta a queste domande in modo
  sistematico attraverso dei modelli algebrici relativamente semplici e compatti
→ È un buon punto di partenza per valutare differenti tipi di chip design evitando approcci molto dispendiosi in
  termini di tempo e risorse
→ Ulteriori e più approfondite analisi del funzionamento dei circuiti devono essere svolte tramite tool TCAD




                                                                                                         3
                         CIRCUITI
                    ELECTRONIC    E SISTEMI
                               CICUITS FOR HIGH       4
                                             ELETTRONICI
                                                FREQUENCIES


            Invertitore CMOS
     ❑ Assumeremo caratteristiche statiche simmetriche (per massimizzare i
       margini di rumore)



VO




                ▪ Per massimizzare NMH voglio VIHmin piccolo
                ▪ Per massimizzare NML voglio VILmax grande

                                     → VLT=VDD/2                    4
                          CIRCUITI
                     ELECTRONIC    E SISTEMI
                                CICUITS FOR HIGH       5
                                              ELETTRONICI
                                                 FREQUENCIES




Dobbiamo determinare le condizioni che portano a VLT=VDD/2     5
                                                 CIRCUITI
                                            ELECTRONIC    E SISTEMI
                                                       CICUITS FOR HIGH       6
                                                                     ELETTRONICI
                                                                        FREQUENCIES


                                       𝑉 = 𝑉𝑇𝑝 = 𝑉𝑇
❑ Affinché VLT=VDD/2 dobbiamo avere   ൝ 𝑇𝑛              allora                    𝑆   𝛽 ′
                                           𝛽𝑛 = 𝛽𝑝               𝑆𝑛 𝛽𝑛′ = 𝑆𝑝 𝛽𝑝′ → 𝑝 = 𝑛
                                                                                        ′
                                                                                𝑆𝑛    𝛽𝑝
DIMOSTRAZIONE

                                                                               𝛼            𝜀




                                                                                                6
                                                                              CIRCUITI
                                                                         ELECTRONIC    E SISTEMI
                                                                                    CICUITS FOR HIGH       7
                                                                                                  ELETTRONICI
                                                                                                     FREQUENCIES
                      conducibilità intrinseca

                           𝑊 ′
❑ sappiamo che 𝛽𝑛 =         𝛽             con             𝛽𝑛′ = 𝜇𝑛 𝐶𝑜𝑥
                           𝐿 𝑛
         dimensionamento   𝑆𝑛




                                                                                                                                       [ J.A del Alamo, Nature, vol 479, p.317, 2011]
                                                     TEM image                   TEM image




                                        [Sangya D. et al., Scientific Reports,   [B. Mereu et al., Appl. Phys. A 80, 253–257 (2005)]                                    7
                                        vol.7, n°8257 (2017) ]
                      CIRCUITI
                 ELECTRONIC    E SISTEMI
                            CICUITS FOR HIGH       8
                                          ELETTRONICI
                                             FREQUENCIES


Capacità di ingresso di un invertitore CMOS
                La capacità di ingresso CINV
                dell’inverter CMOS sarà data dalla
                somma delle capacità di gate, date da:

                ❑ capacità intrinseche di canale
                ❑ capacità parassite


                              𝐶𝐺𝐴𝑇𝐸 ≅ 𝑊𝐿𝐶𝑂𝑋 + 𝑊𝐶𝐺𝑆0 +𝑊𝐶𝐺𝐷0

                                                         2𝑊𝐶𝐺𝑆0




                                                                  8
                                                 CIRCUITI
                                            ELECTRONIC    E SISTEMI
                                                       CICUITS FOR HIGH       9
                                                                     ELETTRONICI
                                                                        FREQUENCIES

Dunque, per un invertitore CMOS:   𝐶𝐼𝑁𝑉 ≅ 𝐶𝑝𝑀𝑂𝑆 + 𝐶𝑛𝑀𝑂𝑆

                                       ≅ 𝑆𝑛 1 + 𝛼 𝐶𝑀1

DIMOSTRAZIONE




                                                                                      9
                                                    CIRCUITI
                                               ELECTRONIC    E SISTEMI
                                                          CICUITS FOR HIGH       10
                                                                        ELETTRONICI
                                                                           FREQUENCIES


Calcoliamo il tempo di commutazione dell’invertitore definito come:
tempo necessario affinché a fronte di una commutazione istantanea della tensione di ingresso (da 0V a VDD, o
viceversa), il nodo di uscita compia un’escursione del 90%.
Assumiamo anche che:
❑ Il carico sia un condensatore a capacità costante
❑ Per semplificare i calcoli trascuriamo l’effetto di modulazione della lunghezza di canale (λ=0)




              𝑡𝑓 =tempo di discesa: affinché l’uscita passi da VDD al valore VOLmax=0.1VDD
                                                                𝑉𝑂𝐿𝑚𝑎𝑥                  𝑉𝐷𝐷
                                                                          𝑑𝑉𝑂              𝑑𝑉𝑂
                                                     𝑡𝑓 = −𝐶𝐿 න                = 𝐶𝐿     න
                           n                                             𝐼𝑛𝑀𝑂𝑆            𝐼𝑛𝑀𝑂𝑆
                                                                𝑉𝐷𝐷                   𝑉𝑂𝐿𝑚𝑎𝑥

                                                                    𝑉𝑇
                                                               2𝐹
                                                                   𝑉𝐷𝐷
                                                        = 𝐶𝐿
                                                                𝛽𝑛 𝑉𝐷𝐷

                                                                                                   10
                                                      CIRCUITI
                                                 ELECTRONIC    E SISTEMI
                                                            CICUITS FOR HIGH       11
                                                                          ELETTRONICI
                                                                             FREQUENCIES



     𝑡𝑟 + 𝑡𝑓       1  1   1    𝑉𝑇    2𝐶𝐿      𝑉𝑇                    NOTA:
𝑡𝑝 =         = 𝐶𝐿       +   𝐹     =        𝐹                         ’uguaglianza è valida perché il gate è
        2         𝑉𝐷𝐷 𝛽𝑛 𝛽𝑝   𝑉𝐷𝐷   𝛽𝑛 𝑉𝐷𝐷   𝑉𝐷𝐷
                                                                    simmetrico (α = Sp/Sn = β’n/β’p = ε)!



Definiamo la resistenza equivalente (del pull-down) dell’invertitore come:
                                                        Dipende da parametri tecnologici e dimensionamenti:
              2      𝑉𝑇
    𝑅𝐼𝑁𝑉 =        𝐹                                     ❑ conducibilità intrinseca 𝛽𝑛′
           𝛽𝑛 𝑉𝐷𝐷   𝑉𝐷𝐷                                 ❑ tensione di soglia 𝑉𝑇
                                                        ❑ tensione di alimentazione 𝑉𝐷𝐷
             2   1       𝑉𝑇                             ❑ dimensionamenti 𝑆𝑛
          =      ′    𝐹
            𝑉𝐷𝐷 𝛽𝑛 𝑆𝑛   𝑉𝐷𝐷                             ❑ come definiamo esaurimento transitorio


La simmetria del gate impone che la resistenza equivalente del pull-up sia identica a quella del pull-down!


                                                                                                         11
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       12
                                                                            ELETTRONICI
                                                                               FREQUENCIES

dunque      𝑡𝑝 = 𝑅𝐼𝑁𝑉 𝐶𝐿

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


ntroduciamo un po’ di simbologia:

𝐶𝑡 : capacità di ingresso del generico gate logico
𝐶𝑝𝑡 :capacità parassita al nodo di uscita prodotto dai transistori del gate che
sto considerando a causa di: capacità di giunzione 𝐶𝐷𝐵 e 𝐶𝐺𝐷
𝐶𝑂𝑈𝑇 : capacità di uscita dovuta solamente ai gate connessi a valle del gate
logico in esame (non comprende capacità di uscita del gate in esame!)




                Il generico ritardo diventa: 𝑡𝑝 = 𝑅𝑡 𝐶𝑂𝑈𝑇 + 𝑅𝑡 𝐶𝑝𝑡


                                                =


                                                =
                                                                                               15
                       CIRCUITI
                  ELECTRONIC    E SISTEMI
                             CICUITS FOR HIGH       16
                                           ELETTRONICI
                                              FREQUENCIES




             𝑅𝑡 𝐶𝑡     𝐶𝑂𝑈𝑇       𝑅𝑡 𝐶𝑝𝑡
𝑡𝑝 = 𝑡𝑝0                      +
           𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉    𝐶𝑡      𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉

           LOGICAL ELECTRICAL PARASITIC
           EFFORT    EFFORT    EFFORT
              g         h           p


            𝑡𝑝 = 𝑡𝑝0 𝑔ℎ + 𝑝
                                                     CIRCUITI
                                                ELECTRONIC    E SISTEMI
                                                           CICUITS FOR HIGH       17
                                                                         ELETTRONICI
                                                                            FREQUENCIES




                                        𝑡𝑝 = 𝑡𝑝0 𝑔ℎ + 𝑝
NOTE:
❑ 𝐶𝑡 è ∝ dimensionamento 𝑆𝑛,𝑒𝑞 ( o 𝑆𝑝,𝑒𝑞 )                  𝑅𝑡 𝐶𝑡 non dipende dal dimensionamento assoluto
❑ 𝑅𝑡 è ∝−1 dimensionamento 𝑆𝑛,𝑒𝑞 ( o                        Lo stesso vale per il termine 𝑅𝑡 𝐶𝑝𝑡
  𝑆𝑝,𝑒𝑞 )



❑ Ne deriva che logical effort (g) e parasitic effort (p) non dipendono dal dimensionamento assoluto dei
  transistori (al limite da quello relativo che consente di avere tempi di ritardo di caso peggiore di salita e
  di discesa uguali)
❑ ’electrical effort (h) dipende dal dimensionamento attraverso 𝐶𝑡
❑ 𝑡𝑝0 è un ritardo di riferimento in relazione al quale possiamo definire un ritardo normalizzato del gate che
  stiamo considerando

                                                                                                         17
                                                   CIRCUITI
                                              ELECTRONIC    E SISTEMI
                                                         CICUITS FOR HIGH       18
                                                                       ELETTRONICI
                                                                          FREQUENCIES

        Capacità parassita al nodo di uscita di un invertitore
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




                  𝐶𝑒𝑞,𝐺𝐷 = 2 𝑊𝑛 𝐶𝐺𝑆0 + 𝑊𝑝 𝐶𝐺𝑆0 +
                           1
                         + 𝑊𝑛 𝐿𝑛 + 𝑊𝑝 𝐿𝑝 𝐶𝑜𝑥 𝑅𝐷𝐷
       𝐶𝑒𝑞,𝐺𝐷              2




                  𝐶𝑒𝑞,𝐷𝐵 = 𝐾𝑒𝑞 𝑊𝐿𝑆 𝐶𝑗0
      𝐶𝑒𝑞,𝐷𝐵




                                             19
                                                  CIRCUITI
                                             ELECTRONIC    E SISTEMI
                                                        CICUITS FOR HIGH       20
                                                                      ELETTRONICI
                                                                         FREQUENCIES


              𝐶𝑝𝐼𝑁𝑉 = 𝐶𝑒𝑞,𝐺𝐷 + 𝐶𝑒𝑞,𝐷𝐵,𝑛 + 𝐶𝑒𝑞,𝐷𝐵,𝑝
                                                1
                    = 2 𝑊𝑛 𝐶𝐺𝑆0 + 𝑊𝑝 𝐶𝐺𝑆0 +         𝑊𝑛 𝐿𝑛 + 𝑊𝑝 𝐿𝑝 𝐶𝑜𝑥 𝑅𝐷𝐷 + 𝐾𝑒𝑞 𝑊𝑛 + 𝑊𝑝 𝐿𝑆 𝐶𝑗0
                                                2


❑ assumendo che 𝐿𝑛 = 𝐿𝑝 = 𝐿𝑚𝑖𝑛
❑ raccogliamo 𝑊 Τ𝐿
❑ sapendo che 𝑆𝑛 = 𝑊𝑛 Τ𝐿 e 𝑆𝑝 = 𝑊𝑝 Τ𝐿
❑ e che 𝑆𝑝 = 𝛼𝑆𝑛

                                             1              2+𝐾
               𝐶𝑝𝐼𝑁𝑉 = 𝑆𝑛 1 + 𝛼   2𝐶𝐺𝑆0     + 𝐶𝑜𝑥 𝑅𝐷𝐷          𝑒𝑞 𝐿𝑆,𝐷 𝐶𝑗0
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
❑   e l’uscita è 1(0) la rete di pull-down(pull-up) è spenta → VOL=0V e VOH=VDD
❑ In condizioni stazionarie solo la rete di pull-up (-down) è accesa/spenta (spenta/accesa) → consumo di
  potenza nulla in condizioni stazionarie
❑ Funzioni logiche sono «calcolate» sia da reti di pull-up che di pull-down → gate CMOS con N ingressi
  richiede solitamente 2N MOSFETS
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

              de Morgan              step 1) imporre simmetria 𝑡𝑓 = 𝑡𝑟 di caso
𝐹 𝐴, 𝐵 = 𝐴𝐵               𝐴ҧ + 𝐵ത
                                     peggiore
                                         ricordiamo che:
                                         ▪ se trascuriamo effetto body (𝛾 = 0)
                                         ▪ se trascuriamo l’effetto di modulazione della
                                             lunghezza di canale (λ = 0)




                                                                                                       1
                                                                                           𝑆𝑒𝑞 =
                                                                                                   1ൗ + 1ൗ
                                                                                                     𝑆1   𝑆2




                                                                   𝜀
                                                          𝑆𝑝,𝑁𝐴𝑁𝐷 = 𝑆𝑛,𝑁𝐴𝑁𝐷
                                                                   2
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
❑ ’electrical effort h è inversamente proporzionale a 𝐾𝑠𝑐




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
