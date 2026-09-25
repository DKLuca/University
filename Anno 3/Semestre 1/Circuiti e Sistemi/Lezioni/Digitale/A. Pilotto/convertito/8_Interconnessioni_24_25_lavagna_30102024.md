---
fonte: "8_Interconnessioni_24_25_lavagna_30102024.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       1
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
   trascurarle
 ❑ l’interconnessione viene schematizzata mediante parametri concentrati 𝐶𝑖𝑛𝑡 e 𝑅𝑖𝑛𝑡
                                                                                                             1
                                                      CIRCUITI
                                                 ELECTRONIC    E SISTEMI
                                                            CICUITS FOR HIGH       2
                                                                          ELETTRONICI
                                                                             FREQUENCIES


      𝑉𝐼𝐼         𝑅𝑖𝑛𝑡   𝑉𝑂𝐼
                                           Rispetto ai casi già studiati in precedenza, ora tra transistore e
            𝐼𝐷𝑆                            capacità di uscita è presente la resistenza 𝑅𝑖𝑛𝑡




                                                                            →
𝑉𝑖𝑛
                               𝐶𝑖𝑛𝑡   𝐶𝐿
                                            ci sono due potenziali incogniti 𝑉𝑂𝐼 e 𝑉𝐼𝐼

                                           Le espressioni per la corrente in regime di saturazione e di triodo
                                           sono note → potremmo calcolare analiticamente il ritardo.




                                                                             →
                                           Otterremmo espressioni complicate → per ovviare a questo
                                           problema semplifichiamo la relazione tra tensione e corrente del
                                           transistore




                                                                                                          2
                                                      CIRCUITI
                                                 ELECTRONIC    E SISTEMI
                                                            CICUITS FOR HIGH       3
                                                                          ELETTRONICI
                                                                             FREQUENCIES

                                        𝑅𝑖𝑛𝑡                                𝐼𝐷𝑆


                                  𝐼𝐷𝑆                                   𝐼𝑑𝑟
                  𝑉𝑖𝑛
                                               𝐶𝑖𝑛𝑡      𝐶𝐿

                                                                                       𝑅𝑑𝑟 −1


                                                                                                     𝑉𝐷𝑆
             saturazione                                  triodo                            𝑉𝑥
           𝑅𝑖𝑛𝑡                                               𝑅𝑖𝑛𝑡



𝐼𝑑𝑟                𝐶𝑖𝑛𝑡      𝐶𝐿                   𝑅𝑑𝑟                𝐶𝑖𝑛𝑡         𝐶𝐿



      Tempo di scarica: T1                              Tempo di scarica: T2
                                                                                                 3
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       4
                                                                           ELETTRONICI
                                                                              FREQUENCIES

                                                                           𝑉𝐼𝐼         𝑅𝑖𝑛𝑡   𝑉𝑂𝐼
 approssimazioni
                                                𝑉𝐷𝑆                              𝐼𝐷𝑆
 1) 𝑉𝐷𝑆 < 𝑉𝑥 , cioè in regione triodo:    𝐼𝐷𝑆 =
                                                                 𝑉𝑖𝑛
                                                𝑅𝑑𝑟
                                                                                                    𝐶𝑖𝑛𝑡   𝐶𝐿
 2) 𝑉𝐷𝑆 > 𝑉𝑥 , cioè in regione di saturazione     𝐼𝐷𝑆 = 𝐼𝑑𝑟


 𝐼𝐷𝑆                                              Assumiamo come condizione iniziale che la linea sia carica
                                                                  𝑉𝐼𝐼 𝑡 = 0 = 𝑉𝑂𝐼 𝑡 = 0 = 𝑉𝐷𝐷
𝐼𝑑𝑟
                                                 FASE 1: nMOS in saturazione → scarica a corrente costante
                                                                          𝐼𝐷𝑆 = 𝐼𝑑𝑟 = 𝑐𝑜𝑛𝑠𝑡

        𝑅𝑑𝑟 −1                                          equazione che governa la scarica è:

                                         𝑉𝐷𝑆                       𝑉𝑂𝐼 𝑡 =
             𝑉𝑥

                                               𝑉𝑂𝐼 𝑡 diminuisce linearmente finchè 𝑉𝐼𝐼 = 𝑉𝑥 per 𝑡 = 𝑡1      4
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       5
                                                                              ELETTRONICI
                                                                                 FREQUENCIES


Quando 𝑉𝐼𝐼 = 𝑉𝑥 cioè quando 𝑉𝐼𝐼 = 𝑉𝑂𝐼 − 𝑅𝑖𝑛𝑡 𝐼𝑑𝑟 = 𝑉𝑥


                                     𝐼𝑑𝑟
                            𝑉𝐷𝐷 −          𝑡 − 𝑅𝑖𝑛𝑡 𝐼𝑑𝑟 = 𝑉𝑥     dalla quale ricaviamo il tempo 𝑡1
                                  𝐶𝐿 + 𝐶𝑖𝑛𝑡 1

                                                               𝑡1 =

         𝑉𝐼𝐼         𝑅𝑖𝑛𝑡    𝑉𝑂𝐼
                                                          se 𝑅𝑖𝑛𝑡 è tale per cui 𝑅𝑖𝑛𝑡 𝐼𝑑𝑟 > 𝑉𝐷𝐷 − 𝑉𝑥 vuol dire che il
               𝐼𝐷𝑆
                                                          transitorio in cui l’nMOS è in saturazione non esiste
𝑉𝑖𝑛                                                       → in altre parole il transistore parte in regione triodo
                                   𝐶𝑖𝑛𝑡    𝐶𝐿

                                                         Tensione al nodo 𝑂𝐼 al tempo 𝑡1 :
                                                                       𝑉𝑂𝐼 𝑡1 = 𝑉𝑥 + 𝑅𝑖𝑛𝑡 𝐼𝑑𝑟



                                                                                                                 5
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       6
                                                                            ELETTRONICI
                                                                               FREQUENCIES

FASE 2: l’nMOS è in triodo e secondo l’approssimazione precedente, lo possiamo vedere come fosse una
resistenza di valore 𝑅𝑑𝑟

  𝑉𝐼𝐼        𝑅𝑖𝑛𝑡         𝐼𝐶
                                                                                         𝑑𝑉𝑂𝐼
                                           𝑅𝑡𝑜𝑡 = 𝑅𝑑𝑟 + 𝑅𝑖𝑛𝑡                 𝐼𝐶 = 𝐶𝑡𝑜𝑡
                                                                                          𝑑𝑡
        𝐼𝑅          𝑉𝑂𝐼                                                      𝐼𝑅 = −𝐼𝐶
                                           𝐶𝑡𝑜𝑡 = 𝐶𝑖𝑛𝑡 + 𝐶𝐿
                                                                                  𝑉𝐼𝐼   𝑉𝑂𝐼
𝑅𝑑𝑟                            𝐶𝑖𝑛𝑡   𝐶𝐿                                    𝐼𝑅 =      =
                                                                                 𝑅𝑑𝑟 𝑅𝑡𝑜𝑡




                                                                                                6
                                                           CIRCUITI
                                                      ELECTRONIC    E SISTEMI
                                                                 CICUITS FOR HIGH       7
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

       𝑠𝑒 𝑡1 → 0                                         𝑇90% ≈ 2.3 𝑅𝑖𝑛𝑡 + 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 + 𝐶𝐿
     ቊ
      𝑠𝑒 𝑉𝑥 + 𝑅𝑖𝑛𝑡 𝐼𝑑𝑟 ≈ 𝑉𝐷𝐷
                                                                                                        7
                                                      CIRCUITI
                                                 ELECTRONIC    E SISTEMI
                                                            CICUITS FOR HIGH       8
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
                                                                                                          8
                                                  CIRCUITI
                                             ELECTRONIC    E SISTEMI
                                                        CICUITS FOR HIGH       9
                                                                      ELETTRONICI
                                                                         FREQUENCIES

                                             Riepilogo
                                        𝑉𝐷𝐷 − 𝑉𝑥                                𝑉𝑥 + 𝑅𝑖𝑛𝑡 𝐼𝑑𝑟
      𝑇90% = 𝑇1 + 𝑇2 = 𝐶𝑖𝑛𝑡 + 𝐶𝐿 𝑅𝑖𝑛𝑡             − 1 + 𝑅𝑖𝑛𝑡 + 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 + 𝐶𝐿 ln
                                         𝑅𝑖𝑛𝑡 𝐼𝑑𝑟                                  0.1𝑉𝐷𝐷


              𝑅𝑖𝑛𝑡                                             𝑠𝑒 𝑡1 → 0
                                                             ቊ
                                                              𝑠𝑒 𝑉𝑥 + 𝑅𝑖𝑛𝑡 𝐼𝑑𝑟 ≈ 𝑉𝐷𝐷
        𝐼𝐷𝑆
𝑉𝑖𝑛                                            𝑇90% ≈ 2.3 𝑅𝑖𝑛𝑡 + 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 + 𝐶𝐿
                        𝐶𝑖𝑛𝑡      𝐶𝐿
                                               𝑇90% = 2.3 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 + 2.3 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 + 𝑅𝑖𝑛𝑡 𝐶𝐿 + 𝑅𝑑𝑟 𝐶𝐿

                                                            In modo empirico 2.3 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 → 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡


                                                  𝑇90% = 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 + 2.3 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 + 𝑅𝑖𝑛𝑡 𝐶𝐿 + 𝑅𝑑𝑟 𝐶𝐿

                                                            se 𝐶𝐿 ≪ 𝐶𝑖𝑛𝑡

                dipende dal quadrato della
                                                 𝑇90% ≈ 𝑟𝑐𝐿𝑒𝑛 2 + 2.3𝑅𝑑𝑟 𝑐𝐿𝑒𝑛                            9
                   lunghezza della linea!
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       10
                                                                            ELETTRONICI
                                                                               FREQUENCIES


Nel caso in cui 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 ≪ 2.3𝑅𝑑𝑟 𝐶𝑖𝑛𝑡                                       𝑇90% ≈ 𝑟𝑐𝐿𝑒𝑛 2 + 2.3𝑅𝑑𝑟 𝑐𝐿𝑒𝑛




                                                                                           →
Allora 𝑇90% è molto simile a quello di un driver caricato con capacità 𝐶𝑖𝑛𝑡       𝑇90% ≈ 2.3𝑅𝑑𝑟 𝑐𝐿𝑒𝑛




                                                                                                       10
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       11
                                                                           ELETTRONICI
                                                                              FREQUENCIES


                  Interconnessione RC come semplice capacità 𝐶𝑖𝑛𝑡
Quando possiamo considerare l’interconnessione RC come semplice capacità 𝐶𝑖𝑛𝑡 ?


riconsideriamo:    𝑇90% ≈ 𝑟𝑐𝐿𝑒𝑛 2 + 2.3𝑅𝑑𝑟 𝑐𝐿𝑒𝑛

                  se, ad esempio, 2.3𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 > 10𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡

                            𝑅𝑖𝑛𝑡             𝑅𝑑𝑟        se questa condizione è verificata allora possiamo
                   𝑅𝑑𝑟 > 10      → 𝐿𝑒𝑛 < 2.3            considerare la linea puramente capacitiva e trascurare
                            2.3              10𝑟
                                                        gli effetti resistivi della linea


                                                𝑅𝑑𝑟      allora dobbiamo tenere in considerazione della
                         se invece    𝐿𝑒𝑛 > 2.3
                                                10𝑟      natura distribuita della rete RC



                                                                                                        11
                                                             CIRCUITI
                                                        ELECTRONIC    E SISTEMI
                                                                   CICUITS FOR HIGH       12
                                                                                 ELETTRONICI
                                                                                    FREQUENCIES

                          Determinazione dei parametri del driver
sappiamo che la corrente di saturazione vale

                   𝛽𝑛
    𝐼𝑠𝑎𝑡 = 𝐼𝑑𝑟 =      𝑉𝐷𝐷 − 𝑉𝑇 2     dove per semplicità trascuriamo il termine 1 + λ𝑉𝐷𝑠
                   2

per quanto riguarda il termine 𝑅𝑑𝑟 e 𝑉𝑥 ricordiamo che in regione triodo

                                     𝛽𝑛
                               𝐼𝐷𝑆 =    2 𝑉𝐺𝑆 − 𝑉𝑇 𝑉𝐷𝑆 − 𝑉𝐷𝑆 2              dove anche in questo caso trascuriamo la modulazione della
                                     2                                      lunghezza di canale λ


                                   𝐼𝐷𝑆 è funzione quadratica di 𝑉𝐷𝑆 !




                        La determinazione di 𝑅𝑑𝑟 e 𝑉𝑥 può avvenire in due modi diversi
                                                                                                                           12
                                                    CIRCUITI
                                               ELECTRONIC    E SISTEMI
                                                          CICUITS FOR HIGH       13
                                                                        ELETTRONICI
                                                                           FREQUENCIES

                           Determinazione dei parametri del driver
 𝐼𝐷𝑆
                                   Metodo 1) Estrapoliamo la relazione 𝐼𝐷𝑆 - 𝑉𝐷𝑆 sulla base del tratto lineare
                                             nell’intorno di 𝑉𝐷𝑆 = 0
𝐼𝑑𝑟
                                              𝜕𝐼𝐷𝑆
                                                   ቤ           =
                                              𝜕𝑉𝐷𝑆 𝑉
                                                       𝐷𝑆 =0



                                                  𝑅𝑑𝑟 =                          e      𝑉𝑥 = 𝑅𝑑𝑟 𝐼𝑑𝑟
                                  𝑉𝐷𝑆
        𝑉𝑥(1) 𝑉𝐷𝐷 − 𝑉𝑇 = 𝑉𝑥(2)
                                              stiamo sovrastimando 𝐼𝐷𝑆         in regione triodo e quindi
                                              sottostimando il ritardo
 Metodo 2)
        𝑉𝑥(2)
  𝑅𝑑𝑟 =       =
         𝐼𝑑𝑟


      stiamo sottostimando 𝐼𝐷𝑆   in regione triodo e quindi                                             13
      sovrastimando il ritardo
                                                      CIRCUITI
                                                 ELECTRONIC    E SISTEMI
                                                            CICUITS FOR HIGH       14
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


                                                                                                           14
               CIRCUITI
          ELECTRONIC    E SISTEMI
                     CICUITS FOR HIGH       15
                                   ELETTRONICI
                                      FREQUENCIES

esempio




                                                    15
                                                      CIRCUITI
                                                 ELECTRONIC    E SISTEMI
                                                            CICUITS FOR HIGH       16
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




                                                                                                     16
                                                             CIRCUITI
                                                        ELECTRONIC    E SISTEMI
                                                                   CICUITS FOR HIGH       17
                                                                                 ELETTRONICI
                                                                                    FREQUENCIES


        Partizionamento di interconnessioni – ripetitori ad area minima

 Se il termine 2.3𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 < 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 il ritardo è dominato fortemente dall’interconnessione e l’unico modo per
 ridurre il ritardo è attraverso un partizionamento della linea con l’inserimento di opportuni driver (ripetitori)

      𝑅𝑑𝑟      𝑅𝑖𝑛𝑡 /𝑘         𝑅𝑑𝑟      𝑅𝑖𝑛𝑡 /𝑘         𝑅𝑑𝑟       𝑅𝑖𝑛𝑡 /𝑘    𝑅𝑑𝑟       𝑅𝑖𝑛𝑡 /𝑘         𝑅𝑑𝑟
𝑉𝑖𝑛


            𝐶𝑖𝑛𝑡 /𝑘                  𝐶𝑖𝑛𝑡 /𝑘                  𝐶𝑖𝑛𝑡 /𝑘               𝐶𝑖𝑛𝑡 /𝑘                       𝐶𝐿
                         𝐶𝑑𝑟                      𝐶𝑑𝑟                                            𝐶𝑑𝑟



                               𝑇90% ≈ 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡 + 2.3 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 + 𝑅𝑖𝑛𝑡 𝐶𝐿 + 𝑅𝑑𝑟 𝐶𝐿




                                                                                                             17
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       18
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

                                                                                             18
                           𝑅𝑑𝑟 𝐶𝑖𝑛𝑡   𝑅𝑖𝑛𝑡 𝐶𝑑𝑟
                                                      CIRCUITI
                                                 ELECTRONIC    E SISTEMI
                                                            CICUITS FOR HIGH       19
                                                                          ELETTRONICI
                                                                             FREQUENCIES


      Partizionamento di interconnessioni – ripetitori ad area minima

                               𝑇90% = 2.3 𝑅𝑑𝑟 𝑐𝐿𝑒𝑛 + 𝑟𝐿𝑒𝑛 𝐶𝑑𝑟 + 2𝐿𝑒𝑛 2.3𝑅𝑑𝑟 𝐶𝑑𝑟 𝑟𝑐


❑ Notiamo come il ritardo dipende linearmente e non più quadraticamente da 𝐿𝑒𝑛
❑ I termini 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 e 𝑅𝑖𝑛𝑡 𝐶𝑑𝑟 non vengono modificati dall’ottimizzazione
❑ Il k non sarà un numero intero → vale quanto detto nel caso di uso della metodologia del logical effort
❑ Quando devo aspettarmi un netto miglioramento rispetto al caso di interconnessione non partizionata?




                                                                                                        19
               CIRCUITI
          ELECTRONIC    E SISTEMI
                     CICUITS FOR HIGH       20
                                   ELETTRONICI
                                      FREQUENCIES

esempio




                                                    20
                                                                    CIRCUITI
                                                               ELECTRONIC    E SISTEMI
                                                                          CICUITS FOR HIGH       21
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




                                                                                                                              21
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       22
                                                                             ELETTRONICI
                                                                                FREQUENCIES

                            Dimensionamento ottimo dei ripetitori

In questo caso i parametri di progetto sono:
❑k
                                        sappiamo che avrò    𝑅𝑑𝑟
❑ Il dimensionamento h dei driver                                  𝑟𝑎𝑝𝑝𝑟𝑒𝑠𝑒𝑛𝑡𝑎 𝑙𝑎 𝑛𝑢𝑜𝑣𝑎 𝑅𝑑𝑟
                                                            ቐ ℎ
                                                             𝐶𝑑𝑟 ℎ 𝑟𝑎𝑝𝑝𝑟𝑒𝑠𝑒𝑛𝑡𝑎 𝑙𝑎 𝑛𝑢𝑜𝑣𝑎 𝐶𝑑𝑟
  Similmente al caso precedente

                   𝑇90% =




  Cerchiamo la condizione di ottimo rispetto al dimensionamento del driver h
                                                       𝑑𝑇90%
                                                             =0
                                                        𝑑ℎ
                                                                                              22
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       23
                                                                            ELETTRONICI
                                                                               FREQUENCIES

                           Dimensionamento ottimo dei ripetitori



𝑑𝑇90%                         𝑑𝑇90%    𝑅𝑑𝑟 𝑐𝐿𝑒𝑛
      =0                            =−          + 𝑟𝐿𝑒𝑛 𝐶𝑑𝑟 = 0
 𝑑ℎ                            𝑑ℎ        ℎ2




                                                                  Notiamo che i termini che dipendono da
                                         𝑅𝑑𝑟 𝑐     𝑅𝑑𝑟 𝐶𝑖𝑛𝑡
                                ℎ𝑜𝑡𝑡 =         =                  k non dipendono da h → quindi 𝑘𝑜𝑡𝑡 è
                                         𝑟𝐶𝑑𝑟      𝑅𝑖𝑛𝑡 𝐶𝑑𝑟       quello trovato in precedenza


Sostituendo le espressioni di ℎ e 𝑘 nell’espressione di 𝑇90% troviamo:

                                     𝑇90% = 2 2.3 + 2.3 𝐿𝑒𝑛 𝑅𝑑𝑟 𝐶𝑑𝑟 𝑟𝑐

                                                                                                      23
                                           𝑇90% ≈ 7.6𝐿𝑒𝑛 𝑅𝑑𝑟 𝐶𝑑𝑟 𝑟𝑐
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       24
                                                                              ELETTRONICI
                                                                                 FREQUENCIES


   𝑇90% = 2.3 𝑅𝑑𝑟 𝑐𝐿𝑒𝑛 + 𝑟𝐿𝑒𝑛 𝐶𝑑𝑟 + 2𝐿𝑒𝑛 2.3𝑅𝑑𝑟 𝐶𝑑𝑟 𝑟𝑐        → ottimizzando numero di tratti di linea k e con dim.min.


   𝑇90% = 7.6𝐿𝑒𝑛 𝑅𝑑𝑟 𝐶𝑑𝑟 𝑟𝑐       → ottimizzando numero di tratti di linea k e il dimensionamento dei driver h



 La seconda espressione mostra che il miglioramento di 𝑇90% è rilevante quando i ritardi 𝑅𝑑𝑟 𝑐𝐿𝑒𝑛 e 𝑟𝐿𝑒𝑛 𝐶𝑑𝑟
 sono molto diversi

          𝑅𝑑𝑟 𝑐       𝑅𝑑𝑟 𝐶𝑖𝑛𝑡       se 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 ≪ 𝑅𝑖𝑛𝑡 𝐶𝑑𝑟                   Contraddice l’ipotesi alla base del
 ℎ𝑜𝑡𝑡 =         =                                                 ℎ≪1         dimensionamento degli stadi con h>1
          𝑟𝐶𝑑𝑟        𝑅𝑖𝑛𝑡 𝐶𝑑𝑟
                                                                              che vorrebbe far diminuire la
                                                                              resistenza      dei     driver    a
 In particolare il miglioramento di 𝑇90% è rilevante quando                   dimensionamento minimo

𝑅𝑑𝑟 𝑐𝐿𝑒𝑛 ≫ 𝑟𝐿𝑒𝑛 𝐶𝑑𝑟
൝                                           si verifica quando 𝑅𝑑𝑟 𝑐 ≫ 𝑟𝐶𝑑𝑟
 𝑅𝑑𝑟 𝑐𝐿𝑒𝑛 ≫ 𝐿𝑒𝑛 2.3𝑅𝑑𝑟 𝐶𝑑𝑟 𝑟𝑐

          2.3 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡 𝑅𝑖𝑛𝑡 𝐶𝑑𝑟                                                                              24
                                                                              CIRCUITI
                                                                         ELECTRONIC    E SISTEMI
                                                                                    CICUITS FOR HIGH       25
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
            𝑇90% ≈ 7.6𝐿𝑒𝑛 𝑅𝑑𝑟 𝐶𝑑𝑟 𝑟𝑐                                    𝑘𝑜𝑡𝑡 =                          ℎ𝑜𝑡𝑡 =             =                                   25
                                                                                    2.3𝑅𝑑𝑟 𝐶𝑑𝑟                       𝑟𝐶𝑑𝑟            𝑅𝑖𝑛𝑡 𝐶𝑑𝑟
               CIRCUITI
          ELECTRONIC    E SISTEMI
                     CICUITS FOR HIGH       26
                                   ELETTRONICI
                                      FREQUENCIES

esempio




                                                    26
                                                               CIRCUITI
                                                          ELECTRONIC    E SISTEMI
                                                                     CICUITS FOR HIGH       27
                                                                                   ELETTRONICI
                                                                                      FREQUENCIES

                                                  Ripetitori in cascata
Se possiamo considerare l’interconnessione come una pura capacità 𝐶𝑖𝑛𝑡 = 𝑐𝐿𝑒𝑛
Usiamo quanto già appreso in precedenza

            𝑅𝑑𝑟                    𝑅𝑑𝑟 /𝑓            𝑅𝑑𝑟 /𝑓 2                 𝑅𝑑𝑟 /𝑓 (𝑛−1) 𝑅
     𝑉𝑖𝑛                                                                                    𝑖𝑛𝑡
                                                                                 (𝑛−1)
             1                     𝑓                 𝑓2                        𝑓
                                                                                       𝐶𝑖𝑛𝑡
                     𝑓𝐶𝑑𝑟               𝑓 2 𝐶𝑑𝑟                 𝑓 (𝑛−1) 𝐶𝑑𝑟                          𝐶𝐿




 In questo caso i parametri di progetto sono:
 ❑ Il numero 𝑛 degli invertitori
 ❑ Il fattore 𝑓 di aumento progressivo dei dimensionamenti → step-up ratio

 Si nota come i primi 𝑛 − 1 stadi abbiano come carico la capacità di ingresso dello stadio che segue → dunque il
 loro ritardo sarà 2.3𝑓𝑅𝑑𝑟 𝐶𝑑𝑟
                                                                                                          27
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       28
                                                                              ELETTRONICI
                                                                                 FREQUENCIES

L’ultimo invertitore che è connesso direttamente all’interconnessione avrà un ritardo dato da:

                                                                                                            𝑅𝑑𝑟
 se 𝐶𝐿 ≪ 𝐶𝑖𝑛𝑡 allora:     𝑇90% ≈ 𝑟𝑐𝐿𝑒𝑛 2 + 2.3𝑅𝑑𝑟 𝑐𝐿𝑒𝑛                              𝑇90% = 𝑟𝑐𝐿𝑒𝑛 2 + 2.3             𝑐𝐿𝑒𝑛
                                                                                                           𝑓 (𝑛−1)


E dunque il ritardo complessivo sarà dato da

                                                                       𝑅𝑑𝑟
                                 𝑇90% = 2.3 𝑛 − 1 𝑓𝑅𝑑𝑟 𝐶𝑑𝑟 + 2.3                𝐶𝑖𝑛𝑡 + 𝑅𝑖𝑛𝑡 𝐶𝑖𝑛𝑡
                                                                      𝑓 (𝑛−1)

                                                                          𝑅𝑑𝑟                  2
                                 𝑇90% = 2.3 𝑛 − 1 𝑓𝑅𝑑𝑟 𝐶𝑑𝑟 + 2.3          (𝑛−1)
                                                                                𝑐𝐿 𝑒𝑛 + 𝑟𝑐𝐿 𝑒𝑛
                                                                      𝑓

Il valore ottimo si ottiene annullando le derivate rispetto a 𝑛 e 𝑓

   𝑑𝑇90%                 ln 𝑓
         = 0 → 𝐶𝑑𝑟 − 𝑐𝐿𝑒𝑛 𝑛 = 0                                       𝐶𝑖𝑛𝑡      𝑐𝐿𝑒𝑛
     𝑑𝑛                   𝑓                                  𝑛 = ln        = ln
                                                         ൞            𝐶𝑑𝑟       𝐶𝑑𝑟
   𝑑𝑇90%            𝑐𝐿𝑒𝑛
         = 0 → 𝐶𝑑𝑟 − 𝑛 = 0                                             𝑓=𝑒
    𝑑𝑓               𝑓                                                                                                      28
                                                             CIRCUITI
                                                        ELECTRONIC    E SISTEMI
                                                                   CICUITS FOR HIGH       29
                                                                                 ELETTRONICI
                                                                                    FREQUENCIES


             2        𝑅𝑑𝑟                                                                         𝑐𝐿𝑒𝑛
𝑇90% = 𝑟𝑐𝐿𝑒𝑛 + 2.3             𝑐𝐿𝑒𝑛   sostituendo risultati trovati
                     𝑓 (𝑛−1)                                              𝑇90% = 2.3𝑒𝑅𝑑𝑟 𝐶𝑑𝑟 ln        + 𝑟𝑐𝐿𝑒𝑛 2
                                             in precedenza                                         𝐶𝑑𝑟

                                                                                                  da confrontare con

 Si vede come l’approccio che prevede una cascata di invertitori:                𝑇90% ≈ 2.3𝑅𝑑𝑟 𝑐𝐿𝑒𝑛 + 𝑟𝑐𝐿𝑒𝑛 2

 ❑ riduce drasticamente il termine legato al driver 𝑅𝑑𝑟 𝐶𝑖𝑛𝑡
 ❑ non modifica il ritardo intrinseco della linea 𝑟𝑐𝐿𝑒𝑛 2 (che dipende quadraticamente dalla lunghezza della linea)


  L’utilità di questo approccio sarà efficacie nel caso in cui 2.3𝑅𝑑𝑟 𝑐𝐿𝑒𝑛 ≫ 𝑟𝑐𝐿𝑒𝑛 2




                                                                                                                29
               CIRCUITI
          ELECTRONIC    E SISTEMI
                     CICUITS FOR HIGH       30
                                   ELETTRONICI
                                      FREQUENCIES

esempio




                                                    30
                                                     CIRCUITI
                                                ELECTRONIC    E SISTEMI
                                                           CICUITS FOR HIGH       31
                                                                         ELETTRONICI
                                                                            FREQUENCIES

                                         Alcuni risultati
𝑇90% di una linea RC in Al (𝜌𝐴𝑙 = 3𝜇Ω𝑐𝑚), 𝑐 = 3𝑝𝐹/𝑐𝑚, DRIVER: 𝑅𝑑𝑟 = 10𝑘Ω, 𝐶𝑑𝑟 = 3𝑓𝐹
                                       (𝑟 = 300Ω𝑐𝑚)                                   (𝑟 = 18750Ω𝑐𝑚)




❑ Resistività r bassa → ritardo caso singolo buffer è lineare (non dominato da 𝑟𝑐𝐿𝑒𝑛 2 )
❑ Pilotaggio con driver ripetuti a dimensionamento minimo è poco efficace
❑ Con driver ottimizzati, essendo 𝑅𝑑𝑟 𝑐 ≫ 𝑟𝐶𝑑𝑟 , 𝑇90% è molto minore                               31
                                                                 CIRCUITI
                                                            ELECTRONIC    E SISTEMI
                                                                       CICUITS FOR HIGH       32
                                                                                     ELETTRONICI
                                                                                        FREQUENCIES

                                                   Alcuni risultati
𝑇90% di una linea RC in polySi (𝜌𝑝𝑜𝑙𝑦𝑆𝑖 = 1000𝜇Ω𝑐𝑚), 𝑐 = 3𝑝𝐹/𝑐𝑚, DRIVER: 𝑅𝑑𝑟 = 10𝑘Ω, 𝐶𝑑𝑟 = 3𝑓𝐹

                                              (𝑟 = 100𝑘Ω𝑐𝑚)                                                 (𝑟 = 625𝑘Ω𝑐𝑚)




        ❑ Ritardo intrinseco della linea dominante per lunghezze di circa 103 𝜇𝑚 → infatti il ritardo con singolo driver aumenta in
          modo quadratic con 𝐿𝑒𝑛
        ❑ Pilotaggio con cascata di driver risulta poco efficace vista l’importanza del ritardo intrinseco
        ❑ 𝑅𝑑𝑟 𝑐 paragonabile a 𝑟𝐶𝑑𝑟 → l’ottimizzazione dei dimensionamento dei ripetitori non produce un grande miglioramento 32
          rispetto al ripetitore minimo
                                                                     CIRCUITI
                                                                ELECTRONIC    E SISTEMI
                                                                           CICUITS FOR HIGH       33
                                                                                         ELETTRONICI
                                                                                            FREQUENCIES

                                                       Alcuni risultati
𝑇90% di una linea in Tungsten silicide (𝜌𝑊𝑆𝑖2 = 130𝜇Ω𝑐𝑚), 𝑐 = 3𝑝𝐹/𝑐𝑚, DRIVER: 𝑅𝑑𝑟 = 10𝑘Ω, 𝐶𝑑𝑟 = 3𝑓𝐹


                                                  (𝑟 = 13𝑘Ω𝑐𝑚)                                                      (𝑟 = 81.25𝑘Ω𝑐𝑚)




        ❑ Resistività intermedia tra polisilicio e alluminio → proprietà dei ritardi intermedia rispetto ai due casi precedenti
                                                                                                                                  33
