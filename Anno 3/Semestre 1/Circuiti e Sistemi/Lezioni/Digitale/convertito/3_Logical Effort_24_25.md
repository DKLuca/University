---
fonte: "3_Logical Effort_24_25.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

CIRCUITI
                                   ELECTRONIC    E SISTEMI
                                              CICUITS FOR HIGH       1
                                                            ELETTRONICI
                                                               FREQUENCIES


       INV   NAND        NOR
              𝑛+𝜀       1 + 𝑛𝜀
  𝑔     1
              1+𝜀        1+𝜀

  𝑝   𝑝𝑖𝑛𝑣   𝑛 ∙ 𝑝𝑖𝑛𝑣   𝑛 ∙ 𝑝𝑖𝑛𝑣


𝑡𝑝 = 𝑡𝑝0 𝑔ℎ + 𝑝                                                        𝜀=2
                                                                       𝑛=2
                                                                      𝑝𝑖𝑛𝑣 = 1




                                                                                 1
                                            CIRCUITI
                                       ELECTRONIC    E SISTEMI
                                                  CICUITS FOR HIGH       2
                                                                ELETTRONICI
                                                                   FREQUENCIES

                       Ritardo di due gate in cascata
         Gate 1          Gate 2
                                                 Vogliamo minimizzare il tempo di propagazione del
                                                 segnale attraverso la cascata di 2 gate.
                                                 Assumiamo che siano note:
                                                 • Le topologie dei gate (quindi g1, g2, p1, p2);
                                                 • CIN1 (quindi Sn1) e COUT.

                                                 h1 non è fissato e varia con CIN2.



𝑡𝑝 = 𝑡𝑝0 𝑔1 ℎ1 + 𝑝1 + 𝑡𝑝0 𝑔2 ℎ2 + 𝑝2             𝑝1 + 𝑝2 = 𝑃 (PATH PARASITIC EFFORT)




                                                                                          2
                         CIRCUITI
                    ELECTRONIC    E SISTEMI
                               CICUITS FOR HIGH       3
                                             ELETTRONICI
                                                FREQUENCIES

         Ritardo di due gate in cascata
Gate 1    Gate 2
                                PATH ELECTRICAL EFFORT (H):
                                            𝐶𝐼𝑁2 𝐶𝑂𝑈𝑇 𝐶𝑂𝑈𝑇
                                𝐻 = ℎ1 ℎ2 =           =
                                            𝐶𝐼𝑁1 𝐶𝐼𝑁2   𝐶𝐼𝑁1

                                STAGE EFFORT (f):
                                𝑓𝑖 = 𝑔𝑖 ℎ𝑖




                                                              3
                                   CIRCUITI
                              ELECTRONIC    E SISTEMI
                                         CICUITS FOR HIGH       4
                                                       ELETTRONICI
                                                          FREQUENCIES

Minimizzazione del ritardo:




                                                                        4
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       5
                                                                              ELETTRONICI
                                                                                 FREQUENCIES


Il ritardo ottimo si ottiene quando entrambi i gate hanno lo stesso stage effort f = gh.
NOTA: due gate con lo stesso f non hanno necessariamente lo stesso tp.

Introduciamo le quantità:

         PATH LOGICAL EFFORT: 𝐺 = 𝑔1𝑔2

                                                                 𝐶
         PATH EFFORT:                    𝐹 = 𝑔1 ℎ1 𝑔2 ℎ2 = 𝑔1 𝑔2 𝑂𝑈𝑇
                                                                 𝐶𝐼𝑁1



Quindi:
𝜕𝑡𝑝              𝐻
    = 𝑡𝑝0 𝑔1 − 𝑔2 2 = 0 → 𝑔1 ℎ1 = 𝑔2 ℎ2 = 𝑓መ                       𝑡ෝ𝑝 = 𝑡𝑝0 𝑔1 ℎ1 + 𝑔2 ℎ2 + 𝑃 = 𝑡𝑝0 (2𝑓መ + 𝑃)
𝜕ℎ1              ℎ1
                                                                                        𝐶𝑂𝑈𝑇
Segue che:                                                              = 𝑡𝑝0 2 𝑔1 𝑔2        +𝑃
                                                                                        𝐶𝐼𝑁1
                                𝐶𝑂𝑈𝑇          𝐶𝑂𝑈𝑇
𝑓መ 2 = 𝐹 → 𝑓መ = 𝐹 =     𝑔1 𝑔2        =    𝐺
                                𝐶𝐼𝑁1          𝐶𝐼𝑁1

                                                                                                            5
                                           CIRCUITI
                                      ELECTRONIC    E SISTEMI
                                                 CICUITS FOR HIGH       6
                                                               ELETTRONICI
                                                                  FREQUENCIES

Determinazione dei dimensionamenti:




                                                                                6
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       7
                                                                             ELETTRONICI
                                                                                FREQUENCIES

Caso semplice di: serie di due invertitori. Determinare ρ



                       𝜀𝑆1                 𝜌𝜀𝑆1


                     𝑆1                  𝜌𝑆1




                                                                                              7
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       8
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
                        stadio i                                                 𝐶𝑖        𝐶𝑖+1
                                       stadio i+1

                                                                                 𝑟𝑖       𝑏𝑖 : 𝑏𝑟𝑎𝑛𝑐ℎ𝑖𝑛𝑔 𝑒𝑓𝑓𝑜𝑟𝑡

  In relazione al percorso di segnale complessivo definiamo il Path Branching Effort B
                                                                𝑁

                                                          𝐵 = ෑ 𝑏𝑖
                                                                                                                  8
                                                               𝑖=1
                                                           CIRCUITI
                                                      ELECTRONIC    E SISTEMI
                                                                 CICUITS FOR HIGH       9
                                                                               ELETTRONICI
                                                                                  FREQUENCIES

Il path electrical effort H diventa:
        𝑁
          𝐶2 𝐶3    𝐶𝑂𝑈𝑇 𝐶𝑂𝑈𝑇
𝐻 = ෑ 𝑟𝑖 = × × ⋯ ×     =
          𝐶1 𝐶2     𝐶𝑛   𝐶1
       𝑖=1

Dunque lo stage effort f del generico gate diventa

                                                  𝑓 = 𝑔𝑖 ℎ𝑖 = 𝑔𝑖 𝑟𝑖 𝑏𝑖
E quindi il path effort F nel caso di diramazioni diventa

                                       𝑁              𝑁                      𝑁
                                                                             𝐶𝑂𝑈𝑇
                               𝐹 = ෑ 𝑔𝑖 ℎ𝑖 = ෑ 𝑔𝑖 𝑟𝑖 𝑏𝑖 = 𝐺𝐵 ෑ 𝑟𝑖 = 𝐺𝐵𝐻 = 𝐺𝐵
                                                                              𝐶𝐼𝑁
                                       𝑖=1           𝑖=1                    𝑖=1
                                       Equazione per il path effort F alla base dell’ottimizzazione
                                                               del ritardo

                                                                                                      9
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       10
                                                                            ELETTRONICI
                                                                               FREQUENCIES

                                                   Summary
                                  𝑅𝑡 𝐶𝑡                                                             𝐶𝑂𝑈𝑇
𝑔: 𝐿𝑜𝑔𝑖𝑐𝑎𝑙 𝐸𝑓𝑓𝑜𝑟𝑡        𝑔=                               𝐻: 𝑃𝑎𝑡ℎ 𝐸𝑙𝑒𝑐𝑡𝑟𝑖𝑐𝑎𝑙 𝐸𝑓𝑓𝑜𝑟𝑡    𝐻 = ෑ 𝑟𝑖 =
                                𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉                                                            𝐶𝐼𝑁
                                                                                              𝑖
                              𝐶𝑂𝑈𝑇                                                        𝑁
ℎ: 𝐸𝑙𝑒𝑐𝑡𝑟𝑖𝑐𝑎𝑙 𝐸𝑓𝑓𝑜𝑟𝑡     ℎ=                                                                            𝐶𝑂𝑈𝑇
                               𝐶𝑡                         𝐹: 𝑃𝑎𝑡ℎ 𝐸𝑓𝑓𝑜𝑟𝑡              𝐹 = ෑ 𝑔𝑖 ℎ𝑖 = 𝐺𝐵
                                                                                                        𝐶𝐼𝑁
                              𝑅𝑡 𝐶𝑝𝑡                                                      𝑖=1
𝑝: 𝑃𝑎𝑟𝑎𝑠𝑖𝑡𝑖𝑐 𝐸𝑓𝑓𝑜𝑟𝑡      𝑝=
                            𝑅𝐼𝑁𝑉 𝐶𝐼𝑁𝑉
                                𝐶𝑖+1 + 𝐶𝑜𝑓𝑓−𝑝𝑎𝑡ℎ
𝑏: 𝐵𝑟𝑎𝑛𝑐ℎ𝑖𝑛𝑔 𝐸𝑓𝑓𝑜𝑟𝑡      𝑏𝑖 =
                                      𝐶𝑖+1

𝐵: 𝑃𝑎𝑡ℎ 𝐵𝑟𝑎𝑛𝑐ℎ𝑖𝑛𝑔 𝐸𝑓𝑓𝑜𝑟𝑡 𝐵 = ෑ 𝑏𝑖
                                     𝑖


𝑃: 𝑃𝑎𝑡ℎ 𝑃𝑎𝑟𝑎𝑠𝑖𝑡𝑖𝑐 𝐸𝑓𝑓𝑜𝑟𝑡          𝑃 = ෍ 𝑝𝑖
                                         𝑖


𝐺: 𝑃𝑎𝑡ℎ 𝐿𝑜𝑔𝑖𝑐𝑎𝑙 𝐸𝑓𝑓𝑜𝑟𝑡            𝐺 = ෑ 𝑔𝑖
                                                                                                      10
                                         𝑖
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       11
                                                                              ELETTRONICI
                                                                                 FREQUENCIES


In un problema di ottimizzazione:
❑ 𝐶𝑂𝑈𝑇 e 𝐶𝐼𝑁 sono dati noti
❑ La conoscenza della tipologia di gate logico implica la conoscenza di 𝑔𝑖 e 𝑝𝑖
❑ La topologia del circuito consente di determinare 𝑏𝑖



L’ottimizzazione consiste nell’opportuno dimensionamento degli stadi al fine di partizionare il ritardo in modo da
minimizzarlo



                                    Ottimizzo il ritardo a numero di stadi fissato
            Due
            casi
                                    Il numero di stadi è un parametro
                                    dell’ottimizzazione

                                                                                                            11
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       12
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
                                             𝑁                        𝑁

                                    𝑡𝑎𝑑 = ෍ 𝑔𝑖 𝑏𝑖 𝑟𝑖 + 𝑝𝑖 = ෍ 𝑔𝑖 𝑏𝑖 𝑟𝑖 + 𝑃
                                            𝑖=1                      𝑖=1
                                     𝑁
                      𝐶𝑂𝑈𝑇
Ricordiamo che     𝐻=      = ෑ 𝑟𝑖
                       𝐶𝐼𝑁                                                                  12
                                    𝑖=1
                                                 CIRCUITI
                                            ELECTRONIC    E SISTEMI
                                                       CICUITS FOR HIGH       13
                                                                     ELETTRONICI
                                                                        FREQUENCIES


    𝑁
                              𝐻
𝐻 = ෑ 𝑟𝑖             𝑟𝑁 =
                            ς𝑁−1
                             𝑖=1 𝑟𝑖
    𝑖=1
                𝑁                     𝑁                    𝑁−1
                                                                               𝐻
          𝑡𝑎𝑑 = ෍ 𝑔𝑖 ℎ𝑖 + 𝑝𝑖 = ෍ 𝑔𝑖 𝑏𝑖 𝑟𝑖 + 𝑃 = ෍ 𝑔𝑖 𝑟𝑖 𝑏𝑖 + 𝑔𝑁              𝑁−1    +𝑃
                                                                            ς𝑖=1 𝑟𝑖
               𝑖=1                    𝑖=1                   𝑖=1




                                                                                         13
                                                  CIRCUITI
                                             ELECTRONIC    E SISTEMI
                                                        CICUITS FOR HIGH       14
                                                                      ELETTRONICI
                                                                         FREQUENCIES
                                𝑁−1
                                                    𝐻
Minimizziamo il ritardo   𝑡𝑎𝑑 = ෍ 𝑔𝑖 𝑟𝑖 𝑏𝑖 + 𝑔𝑁    𝑁−1    +𝑃
                                                  ς𝑖=1 𝑟𝑖
                                𝑖=1

   𝜕𝑡𝑎𝑑
        อ       =0
    𝜕𝑟𝑗
          𝑗≠𝑁




                                                                                       14
                                                           CIRCUITI
                                                      ELECTRONIC    E SISTEMI
                                                                 CICUITS FOR HIGH       15
                                                                               ELETTRONICI
                                                                                  FREQUENCIES

                    Come utilizzare il metodo di ottimizzazione
❑ Sono noti 𝑏 e 𝑔 di ogni stadio, 𝐶𝑂𝑈𝑇 e 𝐶𝐼𝑁 → e dunque 𝐹 e 𝑓መ
❑ Partiamo dall’ultimo stadio visto che 𝐶𝑂𝑈𝑇 = 𝐶𝑖+1
❑ Se conosciamo: 𝑏𝑖 , 𝑔𝑖 , 𝐶𝑖+1 , 𝑓መ possiamo calcolare la capacità di
                                                                                                        CN
                                                                                               CN-1
  ingresso dello stadio i-esimo dato che                                  𝐶𝑖+1
                                                      መ
                                                     𝑓 = 𝑔𝑖 𝑏𝑖 𝑟𝑖 = 𝑔𝑖 𝑏𝑖
                                                                           𝐶𝑖
                                                                                        𝑔𝑖 𝑏𝑖 𝐶𝑖+1
❑ In particolare per l’ultimo stadio: 𝑏𝑁 = 1, e quindi 𝐶𝑁 = 𝑔𝑁 𝐶𝑂𝑈𝑇 Τ𝑓መ          𝐶𝑖 =
                                                                                            𝑓መ
                                                                                        𝑔𝑖−1 𝑏𝑖−1 𝐶𝑖
❑ Nota 𝐶𝑖 ho la 𝐶𝑂𝑈𝑇 dello stadio 𝑖 − 1 → Proseguo a ritroso!                    𝐶𝑖−1 =
                                                                                             𝑓መ


❑ Ci fermiamo dimensionando il secondo stadio visto che il primo stadio ha dimensionamento fissato (𝐶𝐼𝑁 è nota,
  è una specifica di progetto)
    ❑ Come double-check si può verificare che 𝐶1 = 𝐶𝐼𝑁 (se 𝐶1 calcolata corrisponde a quella data dal
      problema)
                                                                                                        15
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       16
                                                                           ELETTRONICI
                                                                              FREQUENCIES

Esempio: calcolare 𝑡ෝ𝑝 e corrispondente dimensionamento dei gate
ε=2

                                   z

             x

                                   z
        Cx




                                   z


                                              = 4.5Cx




                                                                                            16
                                                                 CIRCUITI
                                                            ELECTRONIC    E SISTEMI
                                                                       CICUITS FOR HIGH       17
                                                                                     ELETTRONICI
                                                                                        FREQUENCIES

                                                        Alcune note
                                                            𝜕𝑏𝑖
❑ Nella derivazione del modello si è assunto che                =0   cioè che 𝑏𝑖 non dipende dai dimensionamenti
                                                            𝜕𝑟𝑖
                                𝑁−1
 𝜕𝑡𝑎𝑑                                               𝐻
      อ         = 0 con   𝑡𝑎𝑑 = ෍ 𝑔𝑖 𝑟𝑖 𝑏𝑖 + 𝑔𝑁             +𝑃
  𝜕𝑟𝑗                                             ς𝑁−1
                                                   𝑖=1 𝑟𝑖
          𝑗≠𝑁                   𝑖=1


                      𝐶𝑖+1 + 𝐶𝑜𝑓𝑓−𝑝𝑎𝑡ℎ
  ricordiamo che 𝑏𝑖 =
                            𝐶𝑖+1
❑ 𝐶𝑖+1 = 𝐶𝑜𝑛−𝑝𝑎𝑡ℎ è proporzionale al dimensionamento 𝑖 + 1

❑ Affinchè 𝑏𝑖 non dipenda dal dimensionamento, anche 𝐶𝑜𝑓𝑓−𝑝𝑎𝑡ℎ deve                    stadio i       stadio i+1
  essere proporzionale al dimensionamento dello stadio i+1

❑ Se però 𝐶𝑜𝑓𝑓−𝑝𝑎𝑡ℎ è data:
     ❑ capacità di un’interconnessione                                  𝑏𝑖 dipenderà dal dimensionamento e
                                                                        l’equazione di ottimo sarà diversa da
     ❑ capacità di ingresso di un gate a dimensionato fissato           quella calcolata                           17
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       18
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
                                                                    𝑁
❑ Sappiamo già che dati N stadi, il ritardo minimo si ha quando 𝑓መ = 𝐹 (di ogni stadio) e dunque

                   𝑛1
            𝑁
    𝑡Ƹ𝑎𝑑 = 𝑁 𝐹 + ෍ 𝑝𝑖 + 𝑁 − 𝑛1 𝑝𝐼𝑁𝑉
                   𝑖=1
                                                                                                   18
                                           CIRCUITI
                                      ELECTRONIC    E SISTEMI
                                                 CICUITS FOR HIGH       19
                                                               ELETTRONICI
                                                                  FREQUENCIES

             𝜕𝑡Ƹ𝑎𝑑
Calcoliamo           assumendo 𝑁𝜖 ℝ
              𝜕𝑁




                                                                                19
                                           CIRCUITI
                                      ELECTRONIC    E SISTEMI
                                                 CICUITS FOR HIGH       20
                                                               ELETTRONICI
                                                                  FREQUENCIES

             𝜕𝑡Ƹ𝑎𝑑
Calcoliamo           assumendo 𝑁𝜖 ℝ
              𝜕𝑁
                                          %%%% Matlab %%%%
                                          Pinv=0:0.1:5;
                                          rho_guess=exp(1);
                                          for i=1:numel(Pinv)
                                              fun = @(rho) rho*(1-log(rho))+Pinv(i)
                                              rho(i) = fsolve(fun,rho_guess)
       𝜌 ≅ 0,71𝑝𝐼𝑁𝑉 +2,82                 end
                                          figure(1)
                                          plot(Pinv,rho,'b','linewidth',3);
                                          shg
                                          ylabel('\rho')
                                          xlabel('p_{inv}');
                                          hold on
                                          plot(Pinv,0.71*Pinv+2.82,'r--','linewidth',3);
                                          legend('\rho esatta','\rho approx.')
                                          set(gca,'FontSize',16);




                                                                                           20
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       21
                                                                             ELETTRONICI
                                                                                FREQUENCIES

                                   ❑ 𝜌 ci dice qual è lo stage effort ottimo da usare nei circuiti della nostra
   𝜌 1 − 𝑙𝑛𝜌 + 𝑝𝐼𝑁𝑉 = 0              tecnologia per avere il ritardo ottimo (che è caratteristico della tecnologia
                                     (attraverso 𝑝𝐼𝑁𝑉 ) e non dipende dal circuito in esame)
                                   ❑ mentre 𝑓መ è lo stage effort ottimo di un dato circuito dove sono noti path
    𝜌 ≅ 0,71𝑝𝐼𝑁𝑉 +2,82               effort e numero di stadi con numero di stadi fissato

                                                                     ෡ necessario affinché lo stage effort di tutti
❑ dato un circuito con path effort F trovo il numero di stadi ottimo 𝑁
  gli stadi sia pari a 𝜌


                             calcoliamo      ln 𝐹
❑ Noti 𝜌 e 𝑝𝑎𝑡ℎ 𝑒𝑓𝑓𝑜𝑟𝑡 𝐹                  ෡=
                                          𝑁
                                             ln 𝜌

                                                                                𝑛1

❑ Il ritardo sarà dunque dato da             ෡ 𝑁෡ 𝐹 + 𝑁
                                      Ƹ𝑡𝑎𝑑 = 𝑁        ෡ − 𝑛1 𝑝𝐼𝑁𝑉 + ෍ 𝑝𝑖
                                                                                𝑖=1


                                                                                                              21
                                      CIRCUITI
                                 ELECTRONIC    E SISTEMI
                                            CICUITS FOR HIGH       22
                                                          ELETTRONICI
                                                             FREQUENCIES

ESEMPIO: buffer di invertitori




                                                                           22
                                                     CIRCUITI
                                                ELECTRONIC    E SISTEMI
                                                           CICUITS FOR HIGH       23
                                                                         ELETTRONICI
                                                                            FREQUENCIES

                                            Alcune note
❑ Supponiamo che inizialmente il circuito abbia un numero di stadi 𝑛1 e di ottenere un numero ottimo di
        ෡ > 𝑛1
  stadi 𝑁

                     ෡ − 𝑛1 = 𝑛2 invertitori (ma se 𝑁
❑ Dovremo aggiungere 𝑁                              ෡ ∈ℝ lo sarà anche 𝑛2 )

❑ 𝑛2 dovrà essere un numero intero! Dobbiamo capire come scegliere 𝑛2

                                                 Soluzione 1
❑ Se usiamo 𝑁  ෡ calcolato mediante 𝑁    ෡ = 𝑙𝑛𝐹 Τ𝑙𝑛𝜌 , sappiamo che lo stage effort ottimo è 𝜌 ma se
  approssimiamo 𝑁 ෡ con un numero intero, dobbiamo ricalcolare lo stage effort ottimo 𝑓መ = 𝑁 𝐹 sul numero di
  stadi che abbiamo deciso di utilizzare
    ❑ Possiamo dimensionare tutti gli stadi in modo tale che abbiano lo stesso stage effort pari a quello
      ricalcolato a valle della scelta di 𝑁 intero
                                                 Soluzione 2
❑ Usiamo lo stage effort calcolato mediante 𝜌 ≅ 0,71𝑝𝐼𝑁𝑉 +2,82. In questo modo però non possiamo imporre
  lo stesso stage effort 𝑓መ = 𝜌 in tutti gli stadi. Infatti il primo stadio avrà uno stage effort diverso
                                                                                                      23
                                            CIRCUITI
                                       ELECTRONIC    E SISTEMI
                                                  CICUITS FOR HIGH       24
                                                                ELETTRONICI
                                                                   FREQUENCIES

ESEMPIO di ottimizzazione di ritardi
                                         • Calcoliamo 𝜌 ≅ 0,71𝑝𝐼𝑁𝑉 +2,82
                                         • Calcoliamo F
                                         • Supponiamo 𝑁 ෡ = 3.23 e scegliamo N = 3




 stadio 1     stadio 2     stadio 3




                                                                                     24
                                            CIRCUITI
                                       ELECTRONIC    E SISTEMI
                                                  CICUITS FOR HIGH       25
                                                                ELETTRONICI
                                                                   FREQUENCIES

ESEMPIO di ottimizzazione di ritardi
                                         • Calcoliamo 𝜌 ≅ 0,71𝑝𝐼𝑁𝑉 +2,82
                                         • Calcoliamo F
                                         • Supponiamo 𝑁 ෡ = 3.23 e scegliamo N = 3




 stadio 1     stadio 2     stadio 3




                                                                                     25
