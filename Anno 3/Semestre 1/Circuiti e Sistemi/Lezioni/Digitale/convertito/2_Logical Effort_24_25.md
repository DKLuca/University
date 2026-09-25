---
fonte: "2_Logical Effort_24_25.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       1
                                                                            ELETTRONICI
                                                                               FREQUENCIES

                                             Summary
              𝑅𝑡 𝐶𝑡     𝐶𝑂𝑈𝑇       𝑅𝑡 𝐶𝑝𝑡▪ 𝑡𝑝0 è il ritardo di un inverter connesso ad un carico pari alla sua
 𝑡𝑝 = 𝑡𝑝0                      +
            𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉    𝐶𝑡      𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉 capacità di ingresso (senza parassiti né capacità esterne)
                                         ▪ 𝑔 e 𝑝: fissata topologia e vincoli su dimensionamenti relativi di
                                           nMOS e pMOS che garantiscono 𝑡𝑓 = 𝑡𝑟 (di caso peggiore) →
            LOGICAL ELECTRICAL PARASITIC   dipendono dalla tecnologia (𝛽𝑛′ , 𝑉𝑇 , 𝑉𝐷𝐷 , da come definisco
            EFFORT    EFFORT    EFFORT
                                           l’esaurimento di un transitorio) e non dai dimensionamenti
              g         h         p        assoluti
                                         ▪ L’electrical effort (h) dipende dal dimensionamento attraverso 𝐶𝑡


             𝑡𝑝 = 𝑡𝑝0 𝑔ℎ + 𝑝

Equazione fondamentale per il metodo del logical
effort che mostra linearità del ritardo con 𝐶𝑂𝑈𝑇


                                                                                                      1
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       2
                                                                             ELETTRONICI
                                                                                FREQUENCIES


                                     Calcolo del logical effort g
                                                      𝑅𝑡 𝐶𝑡
                                                 𝑔=
                                                    𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉

Dunque si può dire che:
                                         cioè g è il rapporto 𝐶𝑡 su 𝐶𝐼𝑁𝑉 se dimensiono il gate affinché abbia la
         𝐶𝑡
     𝑔=          se       𝑅𝑡 =𝑅𝐼𝑁𝑉       stessa resistenza equivalente dell’inverter di riferimento → cioè se eroga
        𝐶𝐼𝑁𝑉                             la stessa corrente di uscita dell’inverter di riferimento


oppure:

         𝑅𝑡                               cioè g è il rapporto 𝑅𝑡 su 𝑅𝐼𝑁𝑉 se dimensiono il gate affinché abbia la
     𝑔=          se       𝐶𝑡 =𝐶𝐼𝑁𝑉        stessa capacità di ingresso dell’inverter di riferimento
        𝑅𝐼𝑁𝑉


                                     (è possibile calcolare 𝒈 in entrambi i modi)                           2
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       3
                                                                             ELETTRONICI
                                                                                FREQUENCIES

ESEMPIO: Gate NAND con fan-in=«n»

metodo 1) Usiamo definizione di g che richiede di uguagliare le correnti di uscita del
gate NAND con quelle dell’invertitore di riferimento con dimensionamento 𝑆𝐼𝑁𝑉

                                                    𝐶𝑡,𝑁𝐴𝑁𝐷 𝑛 + 𝜀
                                            𝑔𝑁𝐴𝑁𝐷 =        =
                                                     𝐶𝐼𝑁𝑉    1+𝜀
DIMOSTRAZIONE




                                                                                              3
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       4
                                                                              ELETTRONICI
                                                                                 FREQUENCIES


                                                      𝐶𝑡,𝑁𝐴𝑁𝐷 𝑛 + 𝜀
                                        𝑔𝑁𝐴𝑁𝐷 =              =
                                                       𝐶𝐼𝑁𝑉    1+𝜀

Si nota che g-NAND:
❑ Non dipende da dimensionamenti assoluti → perciò neanche dal dimensionamento dell’inverter di riferimento
                                             ′
                                            𝛽𝑛
❑ Dipende dalla tecnologia attraverso 𝜀 =    ൗ𝛽′
                                                 𝑝

❑ Dal fan-in attraverso «n»




                                                                                                     4
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       5
                                                                            ELETTRONICI
                                                                               FREQUENCIES

ESEMPIO: Gate NAND con fan-in=«n»

 metodo 2) Usiamo definizione di g che richiede di uguagliare la capacità di ingresso del gate con quella
 dell’inverter di riferimento

                                                        𝑅𝑡   𝑛+𝜀
                                            𝑔𝑁𝐴𝑁𝐷 =        =
                                                       𝑅𝐼𝑁𝑉 1 + 𝜀
 DIMOSTRAZIONE




                                                                                                            5
     CIRCUITI
ELECTRONIC    E SISTEMI
           CICUITS FOR HIGH       6
                         ELETTRONICI
                            FREQUENCIES




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

LOGICAL EFFORT: NAND vs NOR


                                        NAND
                                        N

                                       𝛽′𝑛
                                    𝜀=     =2
                                       𝛽′𝑝
                  Logical ffort g




                                                     an n                                 8
                                           CIRCUITI
                                      ELECTRONIC    E SISTEMI
                                                 CICUITS FOR HIGH       9
                                                               ELETTRONICI
                                                                  FREQUENCIES

ESEMPIO: Gate XOR a 2 ingressi

                                 𝑔𝑋𝑂𝑅 = 2

  DIMOSTRAZIONE




                                                                                9
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       10
                                                                            ELETTRONICI
                                                                               FREQUENCIES


                                           Parasitic Effort p
  ’ il contributo al ritardo di un gate dovuto a capacità parassita sul nodo di uscita prodotta dai transistori dello
stesso gate
Abbiamo già visto che p non dipende dai dimensionamenti assoluti dunque:
❑ tutti i gate con medesima topologia e stessi vincoli sui dimensionamenti di nMOS e pMOS hanno stesso
  valore di p

              Calcolo di p:

                                                      𝑅𝑡 𝐶𝑝𝑡
                                                 𝑝=
                                                    𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉

                        𝐶𝑝𝑡                                     𝑅𝑡
                    𝑝=            se   𝑅𝑡 =𝑅𝐼𝑁𝑉             𝑝=            se    𝐶𝑝𝑡 =𝐶𝐼𝑁𝑉
                       𝐶𝐼𝑁𝑉                                    𝑅𝐼𝑁𝑉

                                                                                                             10
             In entrambi i casi dobbiamo tenere conto della capacità parassita sul nodo di uscita
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       11
                                                                           ELETTRONICI
                                                                              FREQUENCIES

            Quali sono le capacità che contribuiscono a p?


❑ Capacità parassite CGDp
❑ Capacità di canale 𝐶𝐺𝐷𝐶
❑ Capacità di giunzione 𝐶𝐷𝐵



Trascureremo il contributo 𝐶𝐺𝐷𝐶 (capacità di canale) ai fini di:
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


Analizziamo il caso più semplice: il calcolo di p dell’invertitore
→ infatti per definizione in quel caso si ha che 𝑅𝑡 =𝑅𝐼𝑁𝑉




                  𝑆𝐼𝑁𝑉 1 + 𝜀 𝐶𝑝1   𝐶𝑝1 𝐿𝑀𝐼𝑁 2𝐶𝐺𝑆0 + 𝐿𝑆 𝐶𝑗0 𝐾𝑒𝑞
           𝑝𝐼𝑁𝑉 =                =    = 2
                  𝑆𝐼𝑁𝑉 1 + 𝜀 𝐶𝑀1 𝐶𝑀1    𝐿𝑀𝐼𝑁 𝐶𝑜𝑥 + 2𝐿𝑀𝐼𝑁 𝐶𝐺𝑆0




                                                                                  13
                                                      CIRCUITI
                                                 ELECTRONIC    E SISTEMI
                                                            CICUITS FOR HIGH       14
                                                                          ELETTRONICI
                                                                             FREQUENCIES


Generalizzando al caso di gate CMOS diversi dall’invertitore, imponendo Rt = RINV
                                                         𝑛𝑝
                                                       σ𝑖=1 𝑆𝑖 𝐶𝑝1
                                        𝑝𝐺𝐴𝑇𝐸 =
                                                    𝑆𝐼𝑁𝑉 1 + 𝜀 𝐶𝑀1

                                                       𝑛𝑝
                                                      σ𝑖=1 𝑆𝑖
                                                =                 𝑝𝐼𝑁𝑉
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


Calcolo del parasitic effort in NORn


                      DD

               (1)


               (2)




               (n)


(1)      (2)                 (n)



                                                                                 16
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       17
                                                                              ELETTRONICI
                                                                                 FREQUENCIES

𝑝𝑁𝐴𝑁𝐷 e 𝑝𝑁𝑂𝑅 aumentano linearmente con il fan-in

❑ attraverso simulazioni si vede che l’aumento è più che lineare con il fan-in
    ❑ Infatti un ruolo importante è dato anche dalle capacità parassite sui nodi interni delle reti di pull-up e pull-
       down
    ❑ n questi calcoli analitici si trascura anche il fatto che la conduzione nei transistori dipende dall’effetto
       body (per cui la tensione di soglia cambia quando 𝑉𝑆 ≠ 𝑉𝐵 )
❑ in aggiunta al punto precedente, per il calcolo del parasitic effort si dovrebbe anche tenere in considerazione
  l’ordine di commutazione dei M S T che costituiscono il gate:



                                                                                CL




                                                                                                               17
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       18
                                                                           ELETTRONICI
                                                                              FREQUENCIES

Ottenere formule analitiche compatte per il parasitic effort p è complicato. C’è però da dire che la procedura di
minimizzazione del ritardo in presenza di una serie di gate non coinvolgerà il parasitic effort dei gate




                                                                                                          18
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       19
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




                                                                                                              19
