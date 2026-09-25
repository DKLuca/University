---
fonte: "7_Interconnessioni_24_25_lavagna_25102024.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

CIRCUITI
     ELECTRONIC    E SISTEMI
                CICUITS FOR HIGH       1
                              ELETTRONICI
                                 FREQUENCIES




Interconnessioni



                                               1
                                                    CIRCUITI
                                               ELECTRONIC    E SISTEMI
                                                          CICUITS FOR HIGH       2
                                                                        ELETTRONICI
                                                                           FREQUENCIES

                                       Interconnessioni




❑ Non c’è abbastanza spazio sulla superficie del chip per
  creare le connessioni elettriche necessarie → si creano
  interconnessioni in direzione out-of-plane
❑ Circuiti integrati complessi possono avere fino a 10 o
  più layer di interconnessioni
                                                                                         2
         CIRCUITI
    ELECTRONIC    E SISTEMI
               CICUITS FOR HIGH       3
                             ELETTRONICI
                                FREQUENCIES

Interconnessioni




                                              3
     CIRCUITI
ELECTRONIC    E SISTEMI
           CICUITS FOR HIGH       4
                         ELETTRONICI
                            FREQUENCIES




                                          4
                 CIRCUITI
            ELECTRONIC    E SISTEMI
                       CICUITS FOR HIGH       5
                                     ELETTRONICI
                                        FREQUENCIES


Materiali




                                                      5
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       6
                                                                            ELETTRONICI
                                                                               FREQUENCIES

                     Materiali per realizzare interconnessioni
Per molti decenni: interconnessioni in alluminio
PRO:
❑ nonostante abbia conducibilità minore di Au e Cu, ha una
  minore resistenza di contatto con il silicio
                                                                     [from Microchip fabrication - Peter van Zant.]
❑ buona adesione su SiO2
❑ realizzabili mediante semplice evaporazione termica
  (melting point 660°C)
CONTRO:
❑ Se in contatto con Si, a 577°C si forma una miscela
  eutettica → può essere un problema ad esempio nel caso di
  shallow junctions
❑ Lo scaling dei transistori (e quindi delle interconnessioni) ha
  portato a problemi di elettromigrazione
   ▪ Per ridurre problemi di elettromigrazione
      ▪ → 0.5-4% Cu aggiunto ad Al
      ▪ ma per scaling molto spinto la resistività è troppo                                               6
          alta → si passa a Cu (late 1990s)
                                                      CIRCUITI
                                                 ELECTRONIC    E SISTEMI
                                                            CICUITS FOR HIGH       7
                                                                          ELETTRONICI
                                                                             FREQUENCIES

                      Materiali per realizzare interconnessioni
 Fino a circa 1990 si usava Al. All’incirca dalla generazione 180nm in poi, vista la necessità di fare
 interconnessioni più vicine e più piccole per far fronte a scaling transistori, si è passati al Cu (𝜌𝐶𝑢 < 𝜌𝐴𝑙 ).

❑ Gli atomi di Cu diffondono nel
   silicio  e    deteriorano   le
   proprietà dei MOSFET.
→ vengono introdotte diffusion
barriers (solitamente TiW or TiN
or TaN or metal silicides)

❑ Separazione netta, durante i
  processi produttivi dei transistori
  in: FEOL e BEOL per evitare
  contaminazioni.




                                                                                                         7
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       8
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




                 deposition rate ~Å/sec



                                                                         deposition rate ~nm/sec
                                                                                                               8
                                                    CIRCUITI
                                               ELECTRONIC    E SISTEMI
                                                          CICUITS FOR HIGH       9
                                                                        ELETTRONICI
                                                                           FREQUENCIES

                Tecniche per realizzare interconnessioni: CVD
Reazioni chimiche: es riduzione di esafluoruro di tungsteno
2WF6 + 3Si → 2W + 3SiF4
2WF6 + 3H2 → 2W + 6HF


      Tecniche per realizzare interconnessioni: Electroplating

                                                                  Utilizzato solitamente per
                                                                   interconnessioni in Cu


                                                                              yields
                                                              2𝐶𝑢++ + 2𝐻2 𝑂            2𝐶𝑢 𝑠 + 𝑂2 𝑔 + 4𝐻 +



                                                                                                  9
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       10
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

                                                                                                          10
         CIRCUITI
    ELECTRONIC    E SISTEMI
               CICUITS FOR HIGH       11
                             ELETTRONICI
                                FREQUENCIES

Interconnessioni




                                              11
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       12
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




                                                                                                             12
                                                     CIRCUITI
                                                ELECTRONIC    E SISTEMI
                                                           CICUITS FOR HIGH       13
                                                                         ELETTRONICI
                                                                            FREQUENCIES



        Due scenari

Interconnessioni locali
𝐿𝑒𝑛 è legata a distanza tra i gate → si riduce con
lo scaling della tecnologia

                                                      Parametro           Relazione           Int. Locale          Int. Globale
Interconnessioni globali                                 𝑊, 𝐻, 𝑡𝑑𝑖                                  1Τ𝑆                1Τ𝑆
Linee che si diramano lungo tutto il chip.                  𝐿𝑒𝑛                                     1Τ𝑆                𝑆𝑐ℎ
                                                            𝑅𝑖𝑛𝑡              𝜌
Con scaling della tecnologia i transistori sono                                  𝐿
sempre più piccoli e le dimensioni dei chip                                  𝐻𝑊 𝑒𝑛
                                                            𝐶𝑖𝑛𝑡            𝜀𝑑𝑖
sempre più grandi.                                                              𝑊𝐿𝑒𝑛
                                                                            𝑡𝑑𝑖
❑ L’area dei chip (𝐴𝑐ℎ ) è aumentata                         𝑡𝑤              𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
❑ In media 𝐿𝑚𝑎𝑥 ≅     𝐴𝑐ℎ /2                           𝑆 > 1 è il fattore di scaling dei transistori;                  13
                                                       𝑆𝑐ℎ > 1 è il fattore di scaling legato all’area del chip;
                                                            CIRCUITI
                                                       ELECTRONIC    E SISTEMI
                                                                  CICUITS FOR HIGH       14
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
                                                                                                              14
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       15
                                                                           ELETTRONICI
                                                                              FREQUENCIES


Ci occuperemo per semplicità di interconnessioni isolate → no cross talk



       𝐼 𝑥      𝑟∆𝑥           𝑙∆𝑥                  𝐼 𝑥 + ∆𝑥



 𝑉 𝑥                             𝑐∆𝑥                  𝑔∆𝑥      𝑉 𝑥 + ∆𝑥



                                ∆𝑥




                                                                                            15
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       16
                                                                             ELETTRONICI
                                                                                FREQUENCIES

                                           Interconnessioni


❑ Ci sono linee che a causa della resistività del
  materiale e sezioni molto piccole → hanno                     Linee dispersive RC
  resistenza per unità di lunghezza molto alta
  che domina sulle componenti induttive



❑ Ci sono linee dove a causa dell’alta conducibilità
  e grande sezione → dominano effetti induttivi                 Linee senza perdite




                                                                                              16
                            CIRCUITI
                       ELECTRONIC    E SISTEMI
                                  CICUITS FOR HIGH       17
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
                                      𝜏                                         17
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       18
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


                                                                                                            18
                                 CIRCUITI
                            ELECTRONIC    E SISTEMI
                                       CICUITS FOR HIGH       19
                                                     ELETTRONICI
                                                        FREQUENCIES

          Capacità e Resistenza dell’interconnessione
                                    𝜀𝑑𝑖
                             𝐶𝑖𝑛𝑡 =     𝑊𝐿𝑒𝑛 = 𝑐𝑝𝑝 𝐿𝑒𝑛
                                    𝑡𝑑𝑖
                                                    𝑐𝑝𝑝 parallel plate capacitance
    𝐿𝑒𝑛

                                     𝜌               𝐿𝑒𝑛
𝐻                            𝑅𝑖𝑛𝑡 =    𝐿 = 𝑟𝐿𝑒𝑛 = 𝑅□
                                    𝐻𝑊 𝑒𝑛            𝑊
               𝑡𝑑𝑖                                  𝑅□ : resistenza per quadro: è la
          𝑊                                         resistenza di una linea quadrata con
                                                    𝑊 = 𝐿𝑒𝑛 , con resistività 𝜌 e spessore
                                                    𝐻




                                                                                19
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       20
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
  𝜌𝐴𝑙 = 2.7 𝜇Ω𝑐𝑚
                        → 𝛿 = 2.6𝜇𝑚
  𝑓 = 1𝐺𝐻𝑧


 𝛿 grande rispetto alle dimensioni della sezione di una interconnessione
                         → possiamo trascurare effetto pelle
                                                                                                                    20
                                CIRCUITI
                           ELECTRONIC    E SISTEMI
                                      CICUITS FOR HIGH       21
                                                    ELETTRONICI
                                                       FREQUENCIES

              Resistenza dell’interconnessione
    𝐿𝑒𝑛                                           𝜌        𝐿𝑒𝑛
                                   𝑅𝑖𝑛𝑡 = 𝑟𝐿𝑒𝑛 =    𝐿 = 𝑅□
                                                 𝐻𝑊 𝑒𝑛     𝑊

𝐻                                    𝑅□ : resistenza per quadro: è la resistenza di una
                                     linea quadrata con 𝑊 = 𝐿𝑒𝑛 , con resistività 𝜌 e
          𝑊      𝑡𝑑𝑖                 spessore 𝐻




                                                                                 21
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       22
                                                                           ELETTRONICI
                                                                              FREQUENCIES

esempio
Supponiamo di avere una linea di clock in Al che si estende per 10cm, di larghezza 1μm, che giace sul primo layer di
metalizzazione.




                                                                                                          22
                                         CIRCUITI
                                    ELECTRONIC    E SISTEMI
                                               CICUITS FOR HIGH       23
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
                                                                              23
                                           CIRCUITI
                                      ELECTRONIC    E SISTEMI
                                                 CICUITS FOR HIGH       24
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
                                                                                    24
                                     CIRCUITI
                                ELECTRONIC    E SISTEMI
                                           CICUITS FOR HIGH       25
                                                         ELETTRONICI
                                                            FREQUENCIES

                    Capacità dell’interconnessione
          𝑊       2𝜋
𝑐 = 𝜀𝑑𝑖      +                     se W diminuisce, 𝑐 può essere dominata da 𝑐𝑓𝑟
          𝑡𝑑𝑖 𝑙𝑛 4𝑡𝑑𝑖 + 𝐻
                    𝐻




                                                          𝜀𝑑𝑖 = 𝜀𝑆𝑖𝑂2 = 3.9𝜀0



                                                                                   25
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       26
                                                                           ELETTRONICI
                                                                              FREQUENCIES

All’aumentare dello scaling, le interconnessioni saranno più vicine → ci sarà una capacità inter-wire: 𝑐𝑖𝑤




                                                                  supponiamo che 𝑊 ed 𝑆 diminuiscono
                                                                  mantenendo costante il rapporto 𝐻/𝑇𝑑𝑖




                                                                                                             26
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       27
                                                                           ELETTRONICI
                                                                              FREQUENCIES

esempio
Supponiamo di avere una linea di clock in Al che si estende per 10cm, di larghezza 1μm, che giace sul primo layer di
metalizzazione.




                                                               *



                                                 *per singolo lato




                                                                                                          27
                                             CIRCUITI
                                        ELECTRONIC    E SISTEMI
                                                   CICUITS FOR HIGH       28
                                                                 ELETTRONICI
                                                                    FREQUENCIES

                    Ritardo intrinseco dell’interconnessione
      𝐼 𝑥   𝑟∆𝑥         𝐼 𝑥 + ∆𝑥



𝑉 𝑥               𝑐∆𝑥              𝑉 𝑥 + ∆𝑥



                   ∆𝑥




                                                                                  28
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       29
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
                                                  → I 𝐿, 𝑡 = 0 ∀ 𝑡 > 0                                     29
                                                                   CIRCUITI
                                                              ELECTRONIC    E SISTEMI
                                                                         CICUITS FOR HIGH       30
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
                                                                                                                                30
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       31
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

 𝑉ෘ 0, 𝑠 = 𝑉ේ
            𝑖𝑛 𝑠 = 𝐴 𝑠 + 𝐵 𝑠
                                                          risolvendo per 𝐴 𝑠 e 𝐵 𝑠 e inserendo le soluzioni
              𝑠𝐶𝑖𝑛𝑡 𝐵 𝑠 𝑒 −𝐿 𝑟𝑐𝑠 − 𝐴 𝑠 𝑒 +𝐿 𝑟𝑐𝑠
𝑌ෘ 𝐿, 𝑠 =                                                 nell’espressione per il potenziale scriviamo
              𝑅𝑖𝑛𝑡 𝐵 𝑠 𝑒 −𝐿 𝑟𝑐𝑠 + 𝐴 𝑠 𝑒 +𝐿 𝑟𝑐𝑠
                                                                                          𝑁(𝑠)
                                                                        𝑉ෘ 𝑥, 𝑠 = 𝑉ේ
                                                                                   𝑖𝑛 𝑠
                                                                                          𝐷(𝑠)
                                                                                                          31
                                                    CIRCUITI
                                               ELECTRONIC    E SISTEMI
                                                          CICUITS FOR HIGH       32
                                                                        ELETTRONICI
                                                                           FREQUENCIES

                        Ritardo intrinseco dell’interconnessione
                     𝑁(𝑠)                   𝑠𝐶𝑖𝑛𝑡              𝑥                                        𝑥
   𝑉ෘ 𝑥, 𝑠 = 𝑉ේ
              𝑖𝑛 𝑠          dove   𝑁 𝑠 =          cosh      1−        𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 + 𝑌 𝐿, 𝑠 sinh       1−     𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                     𝐷(𝑠)                   𝑅𝑖𝑛𝑡               𝐿                                        𝐿


                                             𝑠𝐶𝑖𝑛𝑡
                                   𝐷 𝑠 =           cosh     𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 + 𝑌 𝐿, 𝑠 sinh    𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                             𝑅𝑖𝑛𝑡

                                              1
Nel caso specifico di input a gradino 𝑉ේ
                                       𝑖𝑛 𝑠 =   e di ammettenza ෙ𝑌 𝐿, 𝑠 = 0 (linea di lunghezza L
                                                  𝑠
senza carico connesso in x=L) scriviamo
                                                              𝑥
                                                 1 cosh     1−𝐿       𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                     𝑉ෘ 𝑥, 𝑠 =
                                                 𝑠        cosh    𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡

 E dunque, nel caso particolare di x = 𝐿:
                                                                 1
                                           𝑉ෘ 𝐿, 𝑠 =                                                          32
                                                       𝑠 cosh    𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                                                    CIRCUITI
                                                               ELECTRONIC    E SISTEMI
                                                                          CICUITS FOR HIGH       33
                                                                                        ELETTRONICI
                                                                                           FREQUENCIES

                              Ritardo intrinseco dell’interconnessione
Soluzione più generale ∀𝑥 con input a gradino
                                                                         Si nota la presenza di:
                         𝑥
            1 cosh   1 −   𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                         𝐿                                               ❑ polo semplice in 𝑠0 = 0
  𝑉ෘ 𝑥, 𝑠 =
            𝑠     cosh 𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡                                        ❑ infiniti poli semplici (radici di cosh 𝑠𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 = 0)
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
                                                           sin   2𝑘 − 1   = −1 𝑘+1                                              33
                                                                        2
                                                           CIRCUITI
                                                      ELECTRONIC    E SISTEMI
                                                                 CICUITS FOR HIGH       34
                                                                               ELETTRONICI
                                                                                  FREQUENCIES


Ci sono delle soluzioni approssimate dell’equazione differenziale per x = 𝐿 come ad esempio:


                                              𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡                         𝑡 < 0.1𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                𝑉0 𝑒𝑟𝑓𝑐
                     𝑉 𝐿, 𝑡 =                    4𝑡
                                                  −2.536𝑡          −9.4641𝑡     𝑡 > 0.1𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                 𝑉0     1 − 1.366𝑒 𝑖𝑛𝑡 𝑖𝑛𝑡 + 0.366𝑒 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                                  𝑅   𝐶




                  2 𝑥 −𝑦2
dove 𝑒𝑟𝑓𝑐 𝑥 = 1 −   න 𝑒   𝑑𝑦             error-function
                   𝜋 0                   complementare


per avere un’escursione del 90% ad una distanza 𝐿𝑒𝑛 dall’inizio
delle linea dove viene applicato il gradino di tensione, deve
passare un tempo pari a


                        𝑡 = 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                                                                                   34
                                                    CIRCUITI
                                               ELECTRONIC    E SISTEMI
                                                          CICUITS FOR HIGH       35
                                                                        ELETTRONICI
                                                                           FREQUENCIES


                                                                 90% → 1.0𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 = 82.5𝑛𝑠




                                                                 50% → 0.38𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 = 31.4𝑛𝑠




             31.4ns         82.5ns




Per una rete RC a parametri concentrati, il ritardo per un’escursione del segnale in uscita da 0 a 90%
                                         non vale 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                                                                                         35
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       36
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

E’ un risultato atteso visto che, preso un punto x tra 0 e 𝐿𝑒𝑛 , se guardo verso la sorgente vedo una resistenza
< 𝑅𝑖𝑛𝑡 → questo vuol dire transitorio più veloce rispetto al circuito a parametri concentrati

                                                                                                          36
                                                     CIRCUITI
                                                ELECTRONIC    E SISTEMI
                                                           CICUITS FOR HIGH       37
                                                                         ELETTRONICI
                                                                            FREQUENCIES

                              Modelli a parametri concentrati
Posso rappresentare una linea distribuita con una opportuna successione di celle a parametri
concentrati con struttura a L, T o π
       𝑅                                       𝑅/2         𝑅/2


                  𝐶                                        𝐶/2        𝐶/2


              𝑅                                      𝑅/2                    𝑅/2



       𝐶/2              𝐶/2             𝐶/4                𝐶/4           𝐶/4              𝐶/4


       𝑅/2        𝑅/2                          𝑅/4          𝑅/4    𝑅/4         𝑅/4


                  𝐶                             𝐶/2                𝐶/2
                                                                                                37
                                                           CIRCUITI
                                                      ELECTRONIC    E SISTEMI
                                                                 CICUITS FOR HIGH       38
                                                                               ELETTRONICI
                                                                                  FREQUENCIES

Indipendentemente dal tipo di rete utilizzata (L, T o π) dovrà risultare

                                  Le       rappresentazioni       circuitali      delle
      𝑁                           interconnessioni viste ora (L, T o π), sono utili per
     ෍ 𝑅𝑖 = 𝑅𝑖𝑛𝑡 = 𝑟𝐿𝑒𝑛           determinare in modo analitico le costanti di tempo
                                  dominanti delle reti di resistenze e capacita →
     𝑖=1
      𝑁                           formule di Elmore
     ෍ 𝐶𝑖 = 𝐶𝑖𝑛𝑡 = 𝑐𝐿𝑒𝑛           Consentono di calcolare la costante di tempo al
                                  prim’ordine (o, similmente il primo momento
      𝑖=1
                                  della     risposta    impulsiva)       →     è
                                  un’approssimazione della costante di tempo
                                  reale.
            𝑅1          𝑅2               𝑅3                   𝑅𝑛−1             𝑅𝑛



                 𝐶1          𝐶2               𝐶3                 𝐶𝑛−1               𝐶𝑛




                                                                                                38
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       39
                                                                              ELETTRONICI
                                                                                 FREQUENCIES


         𝑅1           𝑅2        𝑉2                                           𝑅𝑛
                                     𝑅3                    𝑅𝑛−1


              𝐶1           𝐶2             𝐶3                  𝐶𝑛−1                𝐶𝑛



per il nodo 2:
            𝑑𝑉2 𝑉1 − 𝑉2 𝑉3 − 𝑉2           per trovare 𝑉1 e 𝑉3 devo ripetere la stessa procedura
        𝐶      =       +
            𝑑𝑡    𝑅2      𝑅3




                                                                     →
                                          trovo tante equazioni differenziali quando sono i nodi




                                                                     →
                                                          complicato da risolvere

                                               𝑁                         𝑁
→ Formule di Elmore: consentono
di calcolare, in un dato nodo, la         𝜏𝑖 = ෍ 𝐶𝑘 𝑅𝑘𝑖    con 𝑅𝑘𝑖 = ෍ 𝑅𝑗 ∈ [𝑝𝑒𝑟𝑐𝑜𝑟𝑠𝑖 𝑠 → 𝑖 ˄𝑝𝑒𝑟𝑐𝑜𝑟𝑠𝑖 𝑠 → 𝑘 ]
costante di tempo dominante come               𝑘=1                    𝑗 =1
                                                                                                       39
                                              CIRCUITI
                                         ELECTRONIC    E SISTEMI
                                                    CICUITS FOR HIGH       40
                                                                  ELETTRONICI
                                                                     FREQUENCIES
                                        𝑁                    𝑁
                         𝑅3
                                   𝜏𝑖 = ෍ 𝐶𝑘 𝑅𝑘𝑖   con 𝑅𝑘𝑖 = ෍ 𝑅𝑗 ∈ [𝑝𝑒𝑟𝑐𝑜𝑟𝑠𝑖 𝑠 → 𝑖 ˄𝑝𝑒𝑟𝑐𝑜𝑟𝑠𝑖 𝑠 → 𝑘 ]
                                       𝑘=1                  𝑘=1
                          𝐶3
A     𝑅1       𝑅2


       𝐶1           𝐶2
                         𝑅4
                               B

                          𝐶4




    𝜏𝐴→𝐵
    = 𝐶1 𝑅1
    + 𝐶2 𝑅1 + 𝑅2
    + 𝐶3 𝑅1 + 𝑅2
    + 𝐶4 𝑅1 + 𝑅2 + 𝑅4


                                                                                            40
                                            CIRCUITI
                                       ELECTRONIC    E SISTEMI
                                                  CICUITS FOR HIGH       41
                                                                ELETTRONICI
                                                                   FREQUENCIES

A    𝑅1        𝑅2        B   𝑅3        𝑅4



          𝐶1        𝐶2            𝐶3        𝐶4




𝜏𝐴→𝐵
= 𝐶1 𝑅1
+ 𝐶2 𝑅1 + 𝑅2
+ 𝐶3 𝑅1 + 𝑅2
+ 𝐶4 𝑅1 + 𝑅2




                                                                                 41
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       42
                                                                            ELETTRONICI
                                                                               FREQUENCIES


Nel caso di assenza di diramazioni
                                                    𝑁      𝑘           𝑁       𝑁

                                             𝜏0→𝑁 = ෍ 𝐶𝑘 ෍ 𝑅𝑗 = ෍ 𝑅𝑘 ෍ 𝐶𝑗
                                                   𝑘=1     𝑗=1       𝑘=1    𝑗=𝑘

 Sfruttando la rappresentazione a parametri concentrati con
 schema a L, di una linea a parametri distribuiti, avremo
         𝑅𝑖𝑛𝑡
    𝑅𝑖 =          ∀𝑖 ∈ 1, … , 𝑁                                  𝑁         𝑘              𝑁
          𝑁                                                 1                 1
         𝐶𝑖𝑛𝑡                                        𝜏0→𝑁 = 2 ෍ 𝐶𝑖𝑛𝑡 ෍ 𝑅𝑖𝑛𝑡 = 2 ෍ 𝐶𝑖𝑛𝑡 𝑘 𝑅𝑖𝑛𝑡
    𝐶𝑖 =          ∀𝑖 ∈ 1, … , 𝑁         e dunque           𝑁                 𝑁
          𝑁                                                      𝑘=1       𝑗=1           𝑘=1
                                                                                               𝑁
                                                                                       𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
        𝑅𝑖𝑛𝑡 /N       𝑅𝑖𝑛𝑡 /N     𝑅𝑖𝑛𝑡 /N        𝑅𝑖𝑛𝑡 /N                           =             ෍𝑘
  IN                                                           OUT                       𝑁2
                                                                                               𝑘=1
                                                                                               𝑁(𝑁 + 1)
                                                                                   = 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
        𝐶𝑖𝑛𝑡 /𝑁        𝐶𝑖𝑛𝑡 /𝑁     𝐶𝑖𝑛𝑡 /𝑁       𝐶𝑖𝑛𝑡 /𝑁                                         2𝑁 2


                                                                                                          42
                                                     CIRCUITI
                                                ELECTRONIC    E SISTEMI
                                                           CICUITS FOR HIGH       43
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




                                                                                              43
