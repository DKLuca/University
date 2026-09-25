---
fonte: "3_Logical Effort_e_Interconnessioni_13102021_14102021.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       1
                                                                            ELETTRONICI
                                                                               FREQUENCIES

                                                   Summary
                              𝑅𝑡 𝐶𝑡                                                                       𝐶𝑂𝑈𝑇
𝑔: 𝐿𝑜𝑔𝑖𝑐𝑎𝑙 𝐸𝑓𝑓𝑜𝑟𝑡        𝑔=                               𝐻: 𝑃𝑎𝑡ℎ 𝐸𝑙𝑒𝑐𝑡𝑟𝑖𝑐𝑎𝑙 𝐸𝑓𝑓𝑜𝑟𝑡          𝐻 = ෑ 𝑟𝑖 =
                            𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉                                                                      𝐶𝐼𝑁
                                                                                                     𝑖
                              𝐶𝑂𝑈𝑇                                                               𝑁
ℎ: 𝐸𝑙𝑒𝑐𝑡𝑟𝑖𝑐𝑎𝑙 𝐸𝑓𝑓𝑜𝑟𝑡     ℎ=                                                                                  𝐶𝑂𝑈𝑇
                               𝐶𝑡                         𝐹: 𝑃𝑎𝑡ℎ 𝐸𝑓𝑓𝑜𝑟𝑡                    𝐹 = ෑ 𝑔𝑖 ℎ𝑖 = 𝐺𝐵
                                                                                                              𝐶𝐼𝑁
                              𝑅𝑡 𝐶𝑝𝑡                                                            𝑖=1
𝑝: 𝑃𝑎𝑟𝑎𝑠𝑖𝑡𝑖𝑐 𝐸𝑓𝑓𝑜𝑟𝑡      𝑝=
                            𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉                     መ 𝑆𝑡𝑎𝑔𝑒 𝐸𝑓𝑓𝑜𝑟𝑡 𝑜𝑡𝑡𝑖𝑚𝑜                            𝑁
                                                          𝑓:                                𝑓መ = 𝑔𝑖 𝑏𝑖 𝑟𝑖 = 𝐹
                                𝐶𝑖+1 + 𝐶𝑜𝑓𝑓−𝑝𝑎𝑡ℎ
𝑏: 𝐵𝑟𝑎𝑛𝑐ℎ𝑖𝑛𝑔 𝐸𝑓𝑓𝑜𝑟𝑡      𝑏𝑖 =
                                      𝐶𝑖+1
                                                          𝜌: 𝑆𝑡𝑎𝑔𝑒 𝐸𝑓𝑓𝑜𝑟𝑡 𝑜𝑡𝑡𝑖𝑚𝑜 ≅ 0,71𝑝𝐼𝑁𝑉 +2,82
𝐵: 𝑃𝑎𝑡ℎ 𝐵𝑟𝑎𝑛𝑐ℎ𝑖𝑛𝑔 𝐸𝑓𝑓𝑜𝑟𝑡 𝐵 = ෑ 𝑏𝑖
                                     𝑖


𝑃: 𝑃𝑎𝑡ℎ 𝑃𝑎𝑟𝑎𝑠𝑖𝑡𝑖𝑐 𝐸𝑓𝑓𝑜𝑟𝑡         𝑃 = ෍ 𝑝𝑖
                                         𝑖


𝐺: 𝑃𝑎𝑡ℎ 𝐿𝑜𝑔𝑖𝑐𝑎𝑙 𝐸𝑓𝑓𝑜𝑟𝑡           𝐺 = ෑ 𝑔𝑖
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




                        Ottimizzazione a numero             Ottimizzazione del ritardo
                             di stadi fissato                   aggiungendo, se
                                                              necessario, inveritori
                                                                                                            2
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       3
                                                                            ELETTRONICI
                                                                               FREQUENCIES

                      Ottimizzazione a numero di stadi fissato
CONDIZIONE DI OTTIMO: Lo stage effort di tutti gli stadi deve essere:



                                                       𝑁                                           𝐶𝑂𝑈𝑇
                                        𝑓መ = 𝑔𝑖 𝑏𝑖 𝑟𝑖 = 𝐹 = 𝑔𝑁 𝑟𝑁     ∀𝑗 ≠ 𝑁        con   𝐹 = 𝐺𝐵
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
❑ L’inserimento di invertitori non modifica il path effort F (perché 𝑔𝑖𝑛𝑣 = 1)                                            1              1
                                                                                                          𝑡𝑎𝑑 𝑁    ෡ 𝜌𝑠 + 𝑝
                                                                                                                  𝑠𝑁           𝜌𝑠 + 𝑝
                                                                                                       𝑟=       =           =𝑠
                                                                                                                   ෡ 𝜌+𝑝
         𝜌 ≅ 0,71𝑝𝐼𝑁𝑉 +2,82 calcoliamo ෡                                                                      ෡
                                                                                                          𝑡𝑎𝑑 𝑁    𝑁           𝜌+𝑝
❑ Noti ቊ                               𝑁 = 𝑙𝑛𝐹 Τ𝑙𝑛𝜌
           𝑝𝑎𝑡ℎ 𝑒𝑓𝑓𝑜𝑟𝑡 𝐹
                                                                                                                   𝑝𝐼𝑁𝑉 = 1       𝜌 = 3.59
                                                                                                           2
                                                     ෡ non sarà un numero intero → devo
                                                     𝑁                                                             𝑝𝐼𝑁𝑉 = 2       𝜌 = 4.32
                                                                                                               2
                                                     approssimarlo con un numero intero
                                                     (sempre meglio per eccesso)




                                                                                                       r
                                                          ora ci sono due strade

                                                                                                                              2      2
                                                                                                                          s

           ricalcolo lo stage effort ottimo con N                       assumo lo stage effort ottimo uguale
           intero                                                       a quello con 𝑁 ∈ ℛ cioè 𝑓መ = 𝜌 per gli
                                      𝑁                                 N-1 stadi. Ci sarà poi uno stadio con
                       𝑓መ = 𝑔𝑖 𝑏𝑖 𝑟𝑖 = 𝐹
                                                                        𝑓≠𝜌
                              𝑛1                                                           𝑛1
                 𝑁
         𝑡Ƹ𝑎𝑑 = 𝑁 𝐹 + ෍ 𝑝𝑖 + 𝑁 − 𝑛1 𝑝𝐼𝑁𝑉                           𝑡Ƹ𝑎𝑑 = 𝑁 − 1 𝜌 + 𝑓 + ෍ 𝑝𝑖 + 𝑁 − 𝑛1 𝑝𝐼𝑁𝑉
                              𝑖=1                                                          𝑖=1
        ❑ 𝑛1 = numero di stadi iniziali                                                                                       4
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
e 𝑝𝑖𝑛𝑣 basata sulla simulazione del comportamento                          𝑡𝑝,𝑖𝑛𝑣 = 𝑡𝑝0 𝑔ℎ + 𝑝𝑖𝑛𝑣
dell’invertitore al variare della capacità di carico (quindi
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
    a               a             a             a                   ❑ Capacità prodotte dai transistori variano con le
                                                                      tensioni

                                                                    ❑ Gate «a» sono quelli lungo i quali si propaga il
                                                                      ritardo
              b              b            b               b         ❑ Gate «b» forniscono (h-1) degli h gate di carico
                                                                      per i gate «a»
                                                                    ❑ I gate «c» servono a fare in modo che le uscite
                                                                      dei gate «b» non commutino troppo velocemente
          c              c            c               c               → la presenza di questi gate è necessaria per
                                                                      rallentare il transitorio all’uscita del gate «b» che
                                                                      per effetto Miller potrebbe comportare errori non
                                                                      trascurabili nella stima del ritardo


primi due stadi forniscono                    il quarto stadio
una pendenza «realistica» dei                 fornisce      una
fronti in ingresso al DUT                     capacità di carico
(Device Under Test)                           «realistica»     al
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


Modello nMOS       Modello pMOS                NMOS:            PMOS:
                                               L=0.35u,         L=0.35u,
+VTO=-0.4 [V]       +VTO=0.4 [V]
                                               W=0.35u,         W=0.7u,
+KP=200e-6 [A/V^2] +KP=400e-6 [A/V^2]
+GAMMA=0.5 [V^1/2] +GAMMA=0.5 [V^1/2]
+PHI=0.9 [V]        +PHI=0.9 [V]
+NSUB=6e17 [cm-3]   +NSUB=6e17 [cm-3]
+LAMBDA=0.05 [V^-1] +LAMBDA=0.05 [V^-1]
+TOX=4e-9 [m]       +TOX=4e-9 [m]                      𝑝𝑠
+CGSO=8e-10 [F/m]   +CGSO=8e-10 [F/m]
+CGDO=8e-10 [F/m]   +CGDO=8e-10 [F/m]
+CJ=2e-3[F/m^2]     +CJ=2e-3[F/m^2]                                           →       da
+PB=1 [V]           +PB=1 [V]                                                     simulazioni
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
                                               2𝐶𝑢++ + 2𝐻2 𝑂            2𝐶𝑢 𝑠 + 𝑂2 𝑔 + 4𝐻 +
                                                                                              18
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       19
                                                                           ELETTRONICI
                                                                              FREQUENCIES

                                          Interconnessioni

                                                               𝑉𝑂𝐿𝑚𝑎𝑥 =0.1𝑉𝐷𝐷                   𝑉𝑇
                                                                                  𝑑𝑉𝑜       2𝐹
                               Fino ad ora:                                                    𝑉𝐷𝐷
                                                     𝑡𝑓 = 𝐶𝑊        න                  = 𝐶𝑊 ′        = 𝐶𝑊 𝑅𝑖𝑛𝑣
                         interconnessione come                                  𝐼𝑀𝑛 𝑉𝑜     𝛽𝑛 𝑆𝑛 𝑉𝐷𝐷
                          capacità verso massa                     𝑉𝐷𝐷




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



       𝐼 𝑥      𝑟∆𝑥           𝑙∆𝑥                  𝐼 𝑥 + ∆𝑥



 𝑉 𝑥                             𝑐∆𝑥                  𝑔∆𝑥      𝑉 𝑥 + ∆𝑥



                                ∆𝑥




                                                                                            24
                                                            CIRCUITI
                                                       ELECTRONIC    E SISTEMI
                                                                  CICUITS FOR HIGH       25
                                                                                ELETTRONICI
                                                                                   FREQUENCIES

                                              Interconnessioni
Modello a parametri concentrati                                   Modello a parametri distribuiti
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

                                                                 𝑐  3 × 108
                                                               λ= =          = 1𝑚
                                                                 𝑓 300 × 106
                                                                                                              25
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       26
                                                                             ELETTRONICI
                                                                                FREQUENCIES

                                           Interconnessioni


❑ Ci sono linee che a causa della resistività del
  materiale e sezioni molto piccole → hanno                     Linee dispersive RC
  resistenza per unità di lunghezza molto alta
  che domina sulle componenti induttive



❑ Ci sono linee dove a causa dell’alta conducibilità
  e grande sezione → dominano effetti induttivi                 Linee senza perdite




                                                                                              26
                            CIRCUITI
                       ELECTRONIC    E SISTEMI
                                  CICUITS FOR HIGH       27
                                                ELETTRONICI
                                                   FREQUENCIES

                  Linee dispersive RC
𝑟∆𝑥   𝑙∆𝑥
                            𝑉𝑟 = 𝐼 𝑥 𝑟∆𝑥
                                        𝑑𝐼 𝑥
            𝑐∆𝑥              𝑉𝑙 = 𝑙∆𝑥
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
      Se 𝑉𝑙 ≪ 𝑉𝑟 :                    𝑙∆𝑥      ≪ 𝑟∆𝑥𝐼0             𝑙 ≪ 𝑟𝜏
                                             𝜏

      ❑ Se abbiamo a che fare con linee tanto resistive e poco induttive pilotate in un tempo sufficientemente alto
        → possiamo considerare soddisfatta 𝑙 ≪ 𝑟𝜏



      𝐼 𝑥        𝑟∆𝑥            𝐼 𝑥 + ∆𝑥
                                                                  𝑅𝑖𝑛𝑡 = 𝑟𝐿𝑒𝑛      resistenza della linea

𝑉 𝑥                    𝑐∆𝑥                   𝑉 𝑥 + ∆𝑥             𝐶𝑖𝑛𝑡 = 𝑐𝐿𝑒𝑛      capacità della linea




                        ∆𝑥


                                                                                                            28
                                 CIRCUITI
                            ELECTRONIC    E SISTEMI
                                       CICUITS FOR HIGH       29
                                                     ELETTRONICI
                                                        FREQUENCIES

          Capacità e Resistenza dell’interconnessione
                                    𝜀𝑑𝑖
                             𝐶𝑖𝑛𝑡 =     𝑊𝐿𝑒𝑛 = 𝑐𝑝𝑝 𝐿𝑒𝑛
                                    𝑡𝑑𝑖
                                                    𝑐𝑝𝑝 parallel plate capacitance
    𝐿𝑒𝑛

                                            𝜌        𝐿𝑒𝑛
𝐻                            𝑅𝑖𝑛𝑡 = 𝑟𝐿𝑒𝑛 =    𝐿 = 𝑅□
                                           𝐻𝑊 𝑒𝑛     𝑊
               𝑡𝑑𝑖                                  𝑅□ : resistenza per quadro: è la
          𝑊                                         resistenza di una linea quadrata con
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
                                                               diminuisce esponenzialmente                      𝑑
                                                                                                            −
                                                               allontanandosi dall’interfaccia   𝐽 = 𝐽0 𝑒       𝛿


                                                                                                  𝜌
 esempio                                                           spessore efficace    𝛿=
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
          𝑊   𝑡𝑑𝑖




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

𝐻                                           𝜀𝑑𝑖
                                      𝑐𝑝𝑝 =     𝑊
                                            𝑡𝑑𝑖
               𝑡𝑑𝑖                                          𝐶𝑖𝑛𝑡
                                                         𝑐=      = 𝑐𝑝𝑝 + 𝑐𝑓𝑟
                                                             𝐿

                                                                         𝑊       2𝜋
                                                                 = 𝜀𝑑𝑖      +
                                          2𝜋                             𝑡𝑑𝑖 𝑙𝑛 4𝑡𝑑𝑖 + 𝐻
                         𝑐𝑓𝑟 = 𝜀𝑑𝑖                                                 𝐻
                                           2𝑡𝑑𝑖 + 𝐻
𝐻                                  cosh−1
                                              𝐻
                     se 𝑡𝑑𝑖 >> 𝐻

        𝑡𝑑𝑖                              2𝜋
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
          𝑊       2𝜋               se W diminuisce, 𝑐 può essere dominata da 𝑐𝑓𝑟
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
    𝐿𝑒𝑛                                           𝜌        𝐿𝑒𝑛
                                   𝑅𝑖𝑛𝑡 = 𝑟𝐿𝑒𝑛 =    𝐿 = 𝑅□
                                                 𝐻𝑊 𝑒𝑛     𝑊

𝐻                                    𝑅□ : resistenza per quadro: è la resistenza di una
                                     linea quadrata con 𝑊 = 𝐿𝑒𝑛 , con resistività 𝜌 e
          𝑊      𝑡𝑑𝑖                 spessore 𝐻




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
      𝐼 𝑥      𝑟∆𝑥            𝐼 𝑥 + ∆𝑥                   𝑉 𝑥, 𝑡 = 𝑉 𝑥 + ∆𝑥, 𝑡 + 𝐼 𝑥, 𝑡 𝑟∆𝑥
                                                     ቐ                           𝜕𝑉 𝑥 + ∆𝑥, 𝑡
                                                      𝐼 𝑥, 𝑡 = 𝐼 𝑥 + ∆𝑥, 𝑡 + 𝑐∆𝑥
                                                                                       𝜕𝑡
𝑉 𝑥                  𝑐∆𝑥                 𝑉 𝑥 + ∆𝑥




                                                                            →
                                                          𝑉 𝑥 + ∆𝑥, 𝑡 − 𝑉 𝑥, 𝑡
                                                                               = −𝑟𝐼 𝑥, 𝑡
                                                                   ∆𝑥
                         ∆𝑥                            𝐼 𝑥 + ∆𝑥, 𝑡 − 𝐼 𝑥, 𝑡      𝜕𝑉 𝑥 + ∆𝑥, 𝑡
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
    𝜕𝑥                           ricaviamo         𝜕 2 𝑉 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡
 𝜕𝐼 𝑥, 𝑡       𝜕𝑉 𝑥, 𝑡                                        = 𝑟𝑐           Equazione di diffusione
          = −𝑐                                         𝜕𝑥 2          𝜕𝑡
   𝜕𝑥            𝜕𝑡
                                                   Analoga a quella della diffusione del calore.
𝑉𝑖𝑛              𝑉𝑜𝑢𝑡                              Usata per descrivere la variazione della concentrazione di
                                                   una certa quantità (es: materia, momento, energia) all’interno
                   simbolo per rete distribuita    di una specifica regione rispetto a variazioni spaziali e
                                                   temporali)



Per studiare questo sistema dobbiamo imporre dei vincoli:
❑ Condizione iniziale: Linea scarica   → 𝑉 𝑥, 0 = 0 ∀𝑥 > 0                     dobbiamo trovare
                                                                                                  𝑉 𝑥, 𝑡 𝑝𝑒𝑟 t>0
❑ Condizioni al contorno per x=0,L:               → 𝑉 0, 𝑡 = 𝑉𝑖𝑛 𝑡 ∀ 𝑡 > 0
                                                  → I 𝐿, 𝑡 = 0 ∀ 𝑡 > 0                                     39
                                                                   CIRCUITI
                                                              ELECTRONIC    E SISTEMI
                                                                         CICUITS FOR HIGH       40
                                                                                       ELETTRONICI
                                                                                          FREQUENCIES

                                Ritardo intrinseco dell’interconnessione
                                                                                                       notazione:
𝜕 2 𝑉 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡            Sfruttiamo la trasformata di Laplace                                   𝑉ෘ 𝑥, 𝑠 indica la trasformata di
           = 𝑟𝑐
    𝜕𝑥 2          𝜕𝑡                                                   𝜕 2 𝑉ෘ 𝑥, 𝑠                        Laplace di 𝑉 𝑥, 𝑡 . con 𝑠 ∈ ℂ
                                        𝑟𝑐 𝑠𝑉ෘ 𝑥, 𝑠 − 𝑉 𝑥, 0−        =
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

BC1:        𝑉 0, 𝑡 = 𝑉𝑖𝑛 𝑡 ∀𝑡 > 0

            𝐼ሙ 𝐿, 𝑠
BC2:                = 𝑌ෘ 𝐿, 𝑠   : ammettenza di un generico carico
            ෘ
            𝑉 𝐿, 𝑠

Applicando BC1 e BC2 scriviamo

𝑉ෘ 0, 𝑠 = 𝐴 𝑠 + 𝐵 𝑠
                                                          risolvendo per 𝐴 𝑠 e 𝐵 𝑠 e inserendo le soluzioni
              𝑠𝐶𝑖𝑛𝑡 𝐵 𝑠 𝑒 − 𝑟𝑐𝑠 − 𝐴 𝑠 𝑒 + 𝑟𝑐𝑠
𝑌ෘ 𝐿, 𝑠 =                                                 nell’espressione per il potenziale scriviamo
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
                        𝑁(𝑠)                   𝑠𝐶𝑖𝑛𝑡               𝑥                                   𝑥
   𝑉ෘ 𝑥, 𝑠 = 𝑉ේ
              𝑖𝑛 0, 𝑠          dove   𝑁 𝑠 =          cosh       1−       𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 + 𝑌 𝐿, 𝑠 sinh   1−     𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                        𝐷(𝑠)                   𝑅𝑖𝑛𝑡                𝐿                                   𝐿


                                               𝑠𝐶𝑖𝑛𝑡
                                      𝐷 𝑠 =          cosh       𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 + 𝑌 𝐿, 𝑠 sinh   𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                               𝑅𝑖𝑛𝑡

                                                 1
Nel caso specifico di input a gradino 𝑉ේ
                                       𝑖𝑛 0, 𝑠 =   e di ammettenza 𝑌 𝐿, 𝑠 = 0 (linea di lunghezza L
                                                          𝑠
senza carico connesso in x=L) e scriviamo
                                                                  𝑥
                                                     1 cosh     1−𝐿       𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                         𝑉ෘ 𝑥, 𝑠 =
                                                     𝑠        cosh   𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡

 E dunque, nel caso particolare di x = 𝐿:
                                                                     1
                                              𝑉ෘ 𝐿, 𝑠 =                                                      42
                                                          𝑠 cosh     𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       43
                                                                             ELETTRONICI
                                                                                FREQUENCIES


Ci sono delle soluzioni approssimate dell’equazione differenziale per x = 𝐿 come ad esempio:


                                               𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡                          𝑡 < 0.1𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                   𝑉0 𝑒𝑟𝑓𝑐
                     𝑉 𝐿𝑒𝑛 , 𝑡 =                  4𝑡
                                                   −2.536𝑡           −9.4641𝑡     𝑡 > 0.1𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                   𝑉0   1 − 1.366𝑒 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 + 0.366𝑒 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡


                  2 𝑥 −𝑦2
dove 𝑒𝑟𝑓𝑐 𝑥 = 1 −   න 𝑒   𝑑𝑦            error-function
                   𝜋 0                  complementare


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
           1 cosh        1−𝐿        𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                                                         ❑ polo semplice in 𝑠0 = 0
  𝑉 𝑥, 𝑠 =
           𝑠     cosh          𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡                                ❑ infiniti poli semplici (radici di cosh       𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 = 0)
                                                                             in 𝑠𝑘 = −𝑝𝑘 / 𝑅𝐶 per ogni intero 𝑘 ≥ 1

                                                                                       2𝑘 − 1 2 𝜋 2         𝑘≥1
                                                                               𝑝𝑘 =
 maggiori informazioni in:                                                                 4
 [Vasant B. Rao, "Delay Analysis of the Distributed RC                  I residui corrispondenti a ogni polo sono 𝜌0 = 1
 Line", 32nd Design Automation Conference, 1995]
                                                                                                    𝑥         𝜋
                                                                                     −4 cos 1 − 𝐿 2𝑘 − 1 2
                                                                        e 𝜌 (𝑥) =                                   per 𝑘 ≥ 1
                                                                             𝑘
                                                                                      2𝑘 − 1 𝜋 sin 2𝑘 − 1 𝜋Τ2
                                                                                                       soluzione nel dominio del tempo
                ∞                                        2 2                                      ∞
               4 sin 𝑘 − 1Τ2 𝜋 𝑥 Τ𝐿 − 2𝑘−1   𝜋 𝑡
𝑣 𝑥, 𝑡 = 1 − ෍                      𝑒 4𝑅   𝐶
                                        𝑖𝑛𝑡 𝑖𝑛𝑡                                      𝑣 𝑥, 𝑡 = 1 + ෍ 𝜌𝑘 𝑥 𝑒 𝑠𝑘 𝑡
                     2𝑘 − 1 𝜋
               𝑘=1                                                      𝜋                        𝑘=1
                                                           sin   2𝑘 − 1   = −1 𝑘+1                                              44
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
V0= 1;   % voltage step amplitude                                                               % transmission the line                                                                 end
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
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%               plot(t,OutputVoltage_Euler,'k','linewidth',2);
%            METHOD 1: fully numeric - BACKWARD EULER METHOD              %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
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




             31.4ns         82.5ns




Per una rete RC a parametri concentrati, il ritardo per un’escursione del segnale in uscita da   a9 %
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
                                                                 𝑉𝑜𝑢𝑡 = 𝑉0 1 − 𝑒         𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡


        𝑉0                           𝐶𝑖𝑛𝑡          𝑉𝑜𝑢𝑡                          se vogliamo 𝑉𝑜𝑢𝑡 =90%


                                                                 𝑡 = 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 ln 10 ≅ 2.3𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡


Per avere la stessa escursione di 𝑉𝑜𝑢𝑡 nel circuito a parametri concentrati, serve un tempo pari a

                                                       𝑡 = 2.3𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡


❑ La linea a parametri distribuiti è più veloce di quella a parametri concentrati!

E’ un risultato atteso visto che, preso un punto x tra e 𝐿𝑒𝑛 , se guardo verso la sorgente vedo una resistenza
< 𝑅𝑖𝑛𝑡 → questo vuol dire transitorio più veloce rispetto al circuito a parametri concentrati

                                                                                                         47
