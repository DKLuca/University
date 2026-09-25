---
fonte: "9_Interconnessioni_24_25_lavagna_13112024.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       1
                                                                             ELETTRONICI
                                                                                FREQUENCIES

                            Interconnessioni a basse perdite

                  𝑟∆𝑥            𝑙∆𝑥



𝑉(𝑥, 𝑡)                                𝑐∆𝑥                  𝑉(𝑥 + ∆𝑥 , 𝑡)




Il sistema di equazioni che descrive il circuito RLC sarà
𝜕𝑉 𝑥, 𝑡                𝜕𝐼 𝑥, 𝑡
        = −𝑟𝐼 𝑥, 𝑡 − 𝑙
  𝜕𝑥                     𝜕𝑡                                   𝜕 2 𝑉 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡      𝜕 2 𝑉 𝑥, 𝑡
𝜕𝐼 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡                                                     = 𝑟𝑐         + 𝑙𝑐
        = −𝑐                                                      𝜕𝑥 2          𝜕𝑡             𝜕𝑡 2
  𝜕𝑥           𝜕𝑡                 ❑ Derivando rispetto a
                                    x la prima equazione
                                  ❑ Sostituendo nella
                                    seconda si ottiene
                                                                                                        1
                                   CIRCUITI
                              ELECTRONIC    E SISTEMI
                                         CICUITS FOR HIGH       2
                                                       ELETTRONICI
                                                          FREQUENCIES

  DIMOSTRAZIONE
            𝑟∆𝑥   𝑙∆𝑥



𝑉(𝑥, 𝑡)                 𝑐∆𝑥     𝑉(𝑥 + ∆𝑥 , 𝑡)




                                                                        2
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       3
                                                                             ELETTRONICI
                                                                                FREQUENCIES


                                           Interconnessioni rlc
Ora notiamo che nel caso particolare in cui 𝑟=0 si ha che:

 𝜕 2 𝑉 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡      𝜕 2 𝑉 𝑥, 𝑡           𝜕 2 𝑉 𝑥, 𝑡      𝜕 2 𝑉 𝑥, 𝑡
            = 𝑟𝑐         + 𝑙𝑐                                 = 𝑙𝑐
     𝜕𝑥 2          𝜕𝑡             𝜕𝑡 2                 𝜕𝑥 2            𝜕𝑡 2
                                           Questa equazione per linea non-dissipativa assomiglia all’equazione di
                                           propagazione di un’onda (equazione di d'Alembert):

                                                            1 𝜕 2 𝑢(𝒓, 𝑡)       caso 1D   𝜕 2 𝑢 𝑥, 𝑡   1 𝜕 2 𝑢(𝑥, 𝑡)
                                             ∇2 𝑢(𝒓, 𝑡) −                 =0                         − 2             =0
                                                            𝑣 2 𝜕𝑡 2                          𝜕𝑥 2    𝑣      𝜕𝑡 2

                                           dove 𝑢(𝑥, 𝑡) rappresenta l’intensità dell’onda nel punto 𝑥 e al tempo 𝑡 e
                                           con 𝑣 : velocità di propagazione dell’onda nel mezzo.


                                                                                         1
                                                                       E dunque:    𝑙𝑐 = 2
                                                                                        𝑣𝑙


                                                                                                               3
                                                                CIRCUITI
                                                           ELECTRONIC    E SISTEMI
                                                                      CICUITS FOR HIGH       4
                                                                                    ELETTRONICI
                                                                                       FREQUENCIES

                                  Interconnessioni a basse perdite
  Abbiamo visto come possiamo schematizzare un tratto ∆𝑥 di linea
            𝑟∆𝑥         𝑙∆𝑥                                                                               Φ
                                                        Sappiamo che l’induttanza è definita come rapporto 𝐵
                                                                                                           𝑖




                                                                                                →
𝑉𝑖𝑛                                                        𝑉𝑜𝑢𝑡          𝑙 sarà quindi definita in base al flusso di campo
                                   𝑐∆𝑥
                                                                           magnetico per unità di lunghezza della linea




                                                                                                →
                                                                       Questa definizione, che è corretta, risulta laboriosa
                                                                                        nel nostro caso


 Stimiamo 𝑙 sfruttando il fatto che: un conduttore immerso in un materiale isolante omogeneo con permettività
 dielettrica e magnetica pari a 𝜀𝑑𝑖 = 𝜀𝑟 𝜀0 , 𝜇𝑑𝑖 = 𝜇𝑟 𝜇0 ) si ha che
                                                                   1     𝜀𝑟 𝜇𝑟   𝜀𝑟
                                                            𝑙𝑐 =       =       ≈
                                                                   𝑣𝑙2      2
                                                                          𝑣𝑙0     2
                                                                                 𝑣𝑙0
      ❑ dove 𝑣𝑙 è la velocità della luce nel dielettrico
                                                                                                                       4
      ❑ dove 𝑣𝑙0 è la velocità della luce nel vuoto
                                                           CIRCUITI
                                                      ELECTRONIC    E SISTEMI
                                                                 CICUITS FOR HIGH       5
                                                                               ELETTRONICI
                                                                                  FREQUENCIES


                                                Alcuni esempi
       Linea coassiale                             Linea coplanare                               Linea bifilare

                     𝑟2                                          𝑟                                 𝑟              𝑟
                                                                                                        ℎ
                𝑟1                                           ℎ
                                                                                                         2𝜋𝜀
                                                                                               𝑐=
                                                                                                        −1 ℎ2 − 2𝑟
                                                    2𝜋𝜀                  𝜇        ℎ                cosh
       2𝜋𝜀                                                                     −1                            2𝑟 2
     𝑐= 𝑟                𝜇 𝑟2                𝑐=                      𝑙=    cosh
                     𝑙=   ln                             ℎ              2𝜋        𝑟                𝜇         ℎ2 − 2𝑟
       ln 𝑟2            2𝜋 𝑟1                     cosh−1 𝑟                                     𝑙=    cosh −1
           1                                                                                      2𝜋           2𝑟 2
           1                                              1                                       1
      𝑙𝑐 = 2 = 𝜀𝜇 = 𝜀𝑟 𝜇𝑟 𝜀0 𝜇0                    𝑙𝑐 =       = 𝜀𝜇 = 𝜀𝑟 𝜇𝑟 𝜀0 𝜇0             𝑙𝑐 = 2 = 𝜀𝜇 = 𝜀𝑟 𝜇𝑟 𝜀0 𝜇0
          𝑣𝑙                                              𝑣𝑙2                                     𝑣𝑙
                           1                                                1                                      1
                  = 𝜀𝑟 𝜇𝑟 2                                        = 𝜀𝑟 𝜇𝑟 2                               = 𝜀𝑟 𝜇𝑟 2
                          𝑣0                                               𝑣0                                     𝑣0

La velocità di propagazione di una onda in questi casi è pari alla velocità della luce nel mezzo che riempie la linea e
NON dipende dalle caratteristiche geometriche della linea!
                                                                                                                5
Si può dimostrare che lo stesso vale anche per linee non-distorcenti (𝑟𝑐 = 𝑔𝑙) o per segnali ad «alte frequenze»
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       6
                                                                             ELETTRONICI
                                                                                FREQUENCIES


                                                 Alcune note
Si può dimostrare che solamente nei casi di linea non dispersiva (𝑟 = 0) oppure non-distorcenti (𝑟𝑐 = 𝑔𝑙) per
segnali ad «alte frequenze» (𝑟 ≪ 𝜔𝑙) la velocità di propagazione di un segnale non dipende dalla sua pulsazione
𝜔. In termini generali, invece, la velocità di propagazione può dipendere dalla pulsazione del segnale
     → un segnale generico (che può essere scomposto nelle sue componenti armoniche mediante trasformata di
        Fourier) verrà tanto più distorto quanto è lunga la linea di trasmissione dato che le sue componenti spettrali
        viaggeranno a velocità diverse nella linea di trasmissione!




                                                                                                               6
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       7
                                                                            ELETTRONICI
                                                                               FREQUENCIES


Possiamo quindi calcolare il valore di induttanza per unità di lunghezza una volta nota la capacità per unità di
lunghezza come:


                                                  1 1    1 𝜀𝑟 𝜇𝑟 1 𝜀𝑟
                                             𝑙=        =      2 ≈ 𝑐 2
                                                  𝑐 𝑣𝑙2 𝑐 𝑣𝑙0      𝑣𝑙0




                                                                                                           7
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       8
                                                                           ELETTRONICI
                                                                              FREQUENCIES


 𝜕 2 𝑉 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡   1 𝜕 2 𝑉 𝑥, 𝑡
            = 𝑟𝑐         + 2                  E’ un’equazione di propagazione con attenuazione
     𝜕𝑥 2          𝜕𝑡     𝑣𝑙     𝜕𝑡 2


Assumiamo che la linea di trasmissione sia
connessa ad un generatore di tensione                                      L’unico parametro è x!
                                                         𝑉 𝑥, 𝑡 → 𝑉𝜔 𝑥
sinusoidale con pulsazione 𝜔 → passo al                ቊ                   Nel caso di scomposizione di un segnale
                                                         𝐼 𝑥, 𝑡 → 𝐼𝜔 𝑥
regime armonico introducendo i fasori                                      con Fourier, ∀𝜔 avrò un set di equazioni.
complessi 𝑉𝜔 𝑥 e 𝐼𝜔 𝑥


 𝜕𝑉 𝑥, 𝑡                𝜕𝐼 𝑥, 𝑡
         = −𝑟𝐼 𝑥, 𝑡 − 𝑙
   𝜕𝑥                     𝜕𝑡
 𝜕𝐼 𝑥, 𝑡      𝜕𝑉 𝑥, 𝑡
         = −𝑐                   Trasformo nel dominio delle
   𝜕𝑥           𝜕𝑡                      frequenze

                                                                   Equazione dei telegrafisti
                                                                    (con conduttanza g=0)

                                                                  Questa equazione va scritta
                                                                   per ogni pulsazione 𝜔 !!              8
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       9
                                                                           ELETTRONICI
                                                                              FREQUENCIES


Sfruttiamo il fatto che, per una generica linea RLC (anche con una eventuale conduttanza g in parallelo al
condensatore), si può dimostrare che per una linea infinitamente lunga (cioè: senza onde riflesse)

        𝑉𝜔 𝑥                                                                     𝑟 + 𝑗𝜔𝑙      𝑟 + 𝑗𝜔𝑙
             =𝑍 𝜔        impedenza generalizzata              dove     𝑍 𝜔 =             ≈
        𝐼𝜔 𝑥                                                                     𝑔 + 𝑗𝜔𝑐        𝑗𝜔𝑐
                         non dipende dalla sezione x!!

       e dove      𝑉𝜔 𝑥 = 𝑉𝜔 0 𝑒 − 𝑗𝜔𝑐 𝑟+𝑗𝜔𝑙 𝑥
                                        𝛾 𝜔 costante di propagazione

           Restringiamo l’analisi nel caso in cui 𝑟 ≪ 𝜔𝑙 (caso di basse perdite)

         In altre parole stiamo analizzando il comportamento alle alte frequenze (più alte di 𝑟/𝑙)


                         𝑗𝜔𝑙          𝑙   1                    In questo caso l’impedenza
                𝑍 𝜔 ≈        = 𝑍0 =     =    = 𝑣𝑙 𝑙            caratteristica è reale e non
                         𝑗𝜔𝑐          𝑐 𝑣𝑙 𝑐
                                                                      dipende da 𝝎
                                                                                                             9
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       10
                                                                             ELETTRONICI
                                                                                FREQUENCIES


In questo caso (cioè se 𝑟 ≪ 𝜔𝑙 ) la costante di propagazione diventa

                                                                          𝑟 𝑐
                                     𝛾 𝜔 =       𝑗𝜔𝑐 𝑟 + 𝑗𝜔𝑙 ≈ 𝑗𝜔 𝑙𝑐 +
                                                                          2 𝑙


                           1
                    𝑣𝑙 =
                           𝑙𝑐                           𝜔   𝑟
ricordando che                                 𝛾 𝜔 ≈𝑗     +
                           𝑙                            𝑣𝑙 2𝑍0
                    𝑍0 =
                           𝑐


                                                                    𝜔     𝑟
                                                   −𝛾 𝜔 𝑥         −𝑗𝑣 𝑥 −   𝑥
 e dunque il potenziale risulta   𝑉𝜔 𝑥    = 𝑉𝜔 0 𝑒        = 𝑉𝜔 0 𝑒 𝑙 𝑒 0 2𝑍



                                                         = 𝑉𝜔 0 𝑒 −𝑗𝜔𝑡𝑓𝑙 𝑒 −𝛼𝑥
  ❑ dove 𝑡𝑓𝑙 = 𝑥 Τ𝑣𝑙 è il tempo di volo
  ❑ dove 𝛼 = 𝑟Τ 2𝑍0 è la costante di attenuazione                                             10
                                                    CIRCUITI
                                               ELECTRONIC    E SISTEMI
                                                          CICUITS FOR HIGH       11
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
                                                                                                     11
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       12
                                                                              ELETTRONICI
                                                                                 FREQUENCIES


❑ Tornando alla linea di lunghezza infinita con stimolo in ingresso dato da un gradino di potenziale, la tensione
  al tempo t e sezione x sarà data da:

                                                    𝑥                          0𝑦 ≤0
              𝑉 𝑥, 𝑡   = 𝑉0 𝑒 −𝛼𝑥 + 𝑓𝑠𝑙 𝑥, 𝑡   𝑢 𝑡−                       𝑢 𝑦 ቊ
                                                    𝑣𝑙                         1𝑦 ≥0

                       = 𝑉0 𝑒 −𝛼𝑥 + 𝑓𝑠𝑙 𝑥, 𝑡 𝑢 𝑡 − 𝑡𝑓𝑙                    𝑓𝑠𝑙 𝑥, 𝑡 è una generica funzione lentamente
                                                                          variabile sulle scale temporali di un tempo di
                                                                          volo 𝑡𝑓𝑙 e tale che
                                                                               lim 𝑒 −𝛼𝑥 + 𝑓𝑠𝑙 𝑥, 𝑡   →1
                                                                               𝑡→∞



                                                𝑉 𝑥, 𝑡 è costituito da:

                                                ❑ una componente 𝑉0 𝑒 −𝛼𝑥 che raggiunge 𝑥 in un tempo 𝑡𝑓𝑙

                                                ❑ una componente lenta 𝑓𝑠𝑙 𝑥, 𝑡 che garantisce il raggiungimento
                                                  di 𝑉0 in un tempo sufficientemente lungo
                                                                                                              12
                                      CIRCUITI
                                 ELECTRONIC    E SISTEMI
                                            CICUITS FOR HIGH       13
                                                          ELETTRONICI
                                                             FREQUENCIES

 Linea con forti perdite e a basse perdite

 Fortemente dispersiva                              Basse perdite
        𝑒 −𝛼𝐿𝑒𝑛 < 0.08                                𝑒 −𝛼𝐿𝑒𝑛 > 0.78
           →




                                                           →
       𝑟𝐿𝑒𝑛                                          𝑟𝐿𝑒𝑛
            > 2.5                                         < 0.25
       2𝑍0                                           2𝑍0
           →




                                                           →
               𝑍0                                               𝑍0
       𝐿𝑒𝑛 > 5                                          𝐿𝑒𝑛 <
               𝑟                                                2𝑟
poco meno del 10% dell’onda                   quasi l’80% dell’onda iniettata
iniettata raggiunge l’uscita                  raggiunge l’uscita della linea
della linea in un tempo pari a                in un tempo pari a 𝑡𝑓𝑙
𝑡𝑓𝑙
                                                                                13
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       14
                                                                           ELETTRONICI
                                                                              FREQUENCIES

                                 Linea senza perdite
      𝑟𝐿𝑒𝑛                                                                                 𝑙
se         ≪1        → linea senza perdite/linea di trasmissione                con 𝑍0 =
      2𝑍0                                                                                  𝑐

L’equazione che descrive la linea di trasmissione sarà

                𝜕 2 𝑉 𝑥, 𝑡   1 𝜕 2 𝑉 𝑥, 𝑡        equazione delle onde
                           = 2
                    𝜕𝑥 2    𝑣𝑙     𝜕𝑡 2


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
                                                                                                           14
                                                     CIRCUITI
                                                ELECTRONIC    E SISTEMI
                                                           CICUITS FOR HIGH       15
                                                                         ELETTRONICI
                                                                            FREQUENCIES


NOTA

❑ La tensione ad una certa sezione della linea di lunghezza finita si comporta come se la linea fosse
  infinita fino all’istante in cui arriva la prima onda riflessa da una terminazione → infatti l’onda
  elettromagnetica si propaga ad una velocità finita e non può «sapere» cosa c’è davanti a se;

❑ Le forme d’onda sulla linea dipenderanno dalle condizioni con cui la linea viene eccitata e dal modo in
  cui viene terminata la linea

❑ Deriviamo un modello che ci consenta di studiare linee di lunghezza finita con riflessioni




                                                                                                        15
                                                         CIRCUITI
                                                    ELECTRONIC    E SISTEMI
                                                               CICUITS FOR HIGH       16
                                                                             ELETTRONICI
                                                                                FREQUENCIES

               Linea senza perdite pilotata da un driver
          𝑅𝑠
                                                                                                  𝑍0
                                                                          SORGENTE 𝑉𝑆 =               𝑉 = 𝑉𝑖
                                                                                               𝑅𝑠 + 𝑍0 0

𝑉0             𝑉𝑠                 𝑉𝑃               𝑉𝑡𝐿          𝑍𝐿                               𝑍0
                                                                          GENERICO      𝑉𝑃 =           2𝑉𝑖 = 𝑉𝑖
                                                                           PUNTO
                                                                                               𝑍0 + 𝑍0

                                                                                                𝑍𝐿
                                                                          CARICO        𝑉𝑡𝐿 =        2𝑉
                                                                                              𝑍0 + 𝑍𝐿 𝑖
                    𝑅𝑠 𝑉               𝑍0    𝑉𝑃            𝑍0
                        𝑠                                       𝑉𝑡𝐿         Tensione al carico: è la somma tra
                                                                            onda incidente 𝑉𝑖 e onda 𝑉𝑟𝐿 riflessa
     𝑉0             𝑍0      2𝑉𝑖                   2𝑉𝑖                       dal carico verso la linea
                                        𝑍0                           𝑍𝐿
                                                                                     𝑉𝑡𝐿 = 𝑉𝑖 + 𝑉𝑟𝐿


                                                                                                        16
                                                       CIRCUITI
                                                  ELECTRONIC    E SISTEMI
                                                             CICUITS FOR HIGH       17
                                                                           ELETTRONICI
                                                                              FREQUENCIES



𝑉𝑡𝐿 = 𝑉𝑖 + 𝑉𝑟𝐿   →     𝑉𝑟𝐿 = 𝑉𝑡𝐿 − 𝑉𝑖 =                                                  𝜌𝐿 coefficiente dei
                                                                                         riflessione al carico



                                          𝑉𝑡𝐿 = 𝑉𝑖 + 𝑉𝑟𝐿 =


  ❑ Quando l’onda regressiva arriva alla sorgente, ci sarà un’altra riflessione
                                                                𝑅𝑆 − 𝑍0
  ❑ Definiamo in coefficiente di riflessione alla sorgente 𝜌𝑆 = 𝑅 + 𝑍
                                                                 𝑆    0

    L’onda 𝑉𝑟𝑆 riflessa alla sorgente verso la linea e quella 𝑉𝑡𝑆 trasmessa dalla linea alla sorgente
    saranno:

       𝑉 = 𝜌𝑆 𝑉𝑖
      ቊ 𝑟𝑆
       𝑉𝑡𝑆 = 1 + 𝜌𝑆 𝑉𝑖
                                                                                                            17
                        CIRCUITI
                   ELECTRONIC    E SISTEMI
                              CICUITS FOR HIGH       18
                                            ELETTRONICI
                                               FREQUENCIES

                 Esempio
     𝑅𝑠 ≪ 𝑍0
                                            𝑍𝐿 − 𝑍0
                                       𝜌𝐿 =         →
                                            𝑍𝐿 + 𝑍0
𝑉0                     𝑍𝐿 ≫ 𝑍0
                                            𝑅𝑆 − 𝑍0
                                       𝜌𝑆 =         →
                                            𝑅𝑆 + 𝑍0


               ❑ Andamento oscillatorio al carico → indesiderato

               ❑ Definiamo il 𝑡𝑠𝑡𝑙 il settling time come tempo necessario affinché la
                 tensione sul carico si mantenga entro un certo specificato intervallo
                 intorno al valore di regime (esempio 10%)

               ❑ Un tempo 𝑡𝑠𝑡𝑙 maggiore del tempo di volo implica un ritardo non
                 ottimo per il circuito perchè maggiore di quello strettamente
                 indispensabile per la propagazione del segnale sulla linea

                                                                          18
                                  CIRCUITI
                             ELECTRONIC    E SISTEMI
                                        CICUITS FOR HIGH       19
                                                      ELETTRONICI
                                                         FREQUENCIES

                    Adattamento al carico
     𝑅𝑠 ≪ 𝑍0                                          𝑍𝐿 − 𝑍0
                                                 𝜌𝐿 =         →
                                                      𝑍𝐿 + 𝑍0
                                                      𝑅𝑆 − 𝑍0
𝑉0                             𝑍𝐿 = 𝑍0           𝜌𝑆 =         →
                                                      𝑅𝑆 + 𝑍0


                                              𝑉𝑡𝐿 𝑡 = 𝑡𝑓𝑙 = 𝑉𝑠 𝑡 = 0


                              ❑ In un tempo di volo tutti i transitori sono esauriti e
                                trasferiamo tutta la tensione al carico


               𝑡𝑠𝑡𝑙 = 1𝑡𝑓𝑙



                                                                                 19
                                  CIRCUITI
                             ELECTRONIC    E SISTEMI
                                        CICUITS FOR HIGH       20
                                                      ELETTRONICI
                                                         FREQUENCIES

               Adattamento alla sorgente
     𝑅𝑠 = 𝑍0                                           𝑍𝐿 − 𝑍0
                                                  𝜌𝐿 =         →
                                                       𝑍𝐿 + 𝑍0
                                                         𝑅𝑆 − 𝑍0
𝑉0                               𝑍𝐿 ≫ 𝑍0          𝜌𝑆 =           →
                                                         𝑅𝑆 + 𝑍0

                                            𝑉0
                                    𝑉𝑆 0 =
                                             2
                                    𝑉𝑡𝐿 𝑡 = 𝑡𝑓𝑙 = 𝑉𝑠 0    1 + 𝜌𝐿 = 𝑉0

                                                            𝑉0
                                    𝑉𝑟𝐿 𝑡 = 𝑡𝑓𝑙 = 𝑉𝑠 0 𝜌𝐿 =
                                                             2
                                                           𝑉0
                                    𝑉𝑡𝑆 𝑡 = 2𝑡𝑓𝑙 = 𝑉𝑠 0 +      1 + 𝜌𝑆 = 𝑉0
                                                           2
               𝑡𝑠𝑡𝑙 = 1𝑡𝑓𝑙
                              ❑ In un tempo di volo tutti i transitori sono esauriti e
                                trasferiamo tutta la tensione al carico
                                                                                  20
                                                     CIRCUITI
                                                ELECTRONIC    E SISTEMI
                                                           CICUITS FOR HIGH       21
                                                                         ELETTRONICI
                                                                            FREQUENCIES

                        Linea come semplice capacità
❑ Quando possiamo considerare la linea come semplice capacità?

    ▪ quando il tempo di salita e discesa del segnale in ingresso alla linea è grande rispetto a 𝑡𝑓𝑙

❑ Consideriamo un driver con 𝑡𝑟 il tempo di salita del segnale di ingresso alla linea pilotata dal driver

                              𝐿𝑒𝑛                                𝑡𝑟     𝑣𝑙 𝑡𝑟
            𝑡𝑟 > 2.5𝑡𝑓𝑙 = 2.5     = 2.5𝐿𝑒𝑛 𝑙𝑐      →     𝐿𝑒𝑛 <
                                                               2.5 𝑙𝑐
                                                                      =
                                                                        2.5
                               𝑣𝑙




                                                                                                 21
                                          CIRCUITI
                                     ELECTRONIC    E SISTEMI
                                                CICUITS FOR HIGH       22
                                                              ELETTRONICI
                                                                 FREQUENCIES

  SORGENTE                    CARICO                DIAGRAMMA A RETICOLO
𝑉𝑠0 0                                 0
                 𝑉𝑠0
                                                          ❑ Al carico arriveranno contributi a
    1                                 1                     numeri dispari del tempo di volo,
               𝜌𝐿 𝑉𝑠0                                       mentre alla sorgente a numeri pari
                                                            del tempo di volo
    2                                 2
               𝜌𝑠 𝜌𝐿 𝑉𝑠0

    3                                 3
             𝜌𝑠 𝜌𝐿 2 𝑉𝑠0                                     𝑉𝑡𝐿 𝑛𝑡𝑓𝑙 e 𝑉𝑡𝑆 2𝑡𝑓𝑙 sono tensioni
                                                             TRASMESSE al carico e sorgente
                                                             rispettivamente. Non sono le
    4        𝜌𝑠 2 𝜌𝐿 2 𝑉𝑠0            4                      tensioni assolute che ho in un
                                                             determinato istante al carico o
                                                             sorgente! (vedi prossima slide)
    5                                 5


  𝑡ൗ                         𝑡ൗ                                                      22
    𝑡𝑓𝑙                        𝑡𝑓𝑙
                                                           CIRCUITI
                                                      ELECTRONIC    E SISTEMI
                                                                 CICUITS FOR HIGH       23
                                                                               ELETTRONICI
                                                                                  FREQUENCIES


                                           ∞

               𝑉𝐿 𝑡 = 𝑉𝑡𝐿 𝑡𝑓𝑙 𝑢 𝑡 − 𝑡𝑓𝑙 + ෍ 𝑉𝑡𝐿 𝑡𝑓𝑙 + 2𝑛𝑡𝑓𝑙 𝑢 𝑡 − 𝑡𝑓𝑙 + 2𝑛𝑡𝑓𝑙
                                          𝑛=1
                                                ∞

                    = 1 + 𝜌𝐿 𝑉𝑠0 𝑢 𝑡 − 𝑡𝑓𝑙 + ෍ 1 + 𝜌𝐿       𝜌𝑆 𝜌𝐿 𝑛 𝑉𝑠0 𝑢 𝑡 − 𝑡𝑓𝑙 + 2𝑛𝑡𝑓𝑙
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
  ha quando 𝜌𝐿 = 0 cioè non ho riflessione al carico                                                      23
                                CIRCUITI
                           ELECTRONIC    E SISTEMI
                                      CICUITS FOR HIGH       24
                                                    ELETTRONICI
                                                       FREQUENCIES




Driver troppo conduttivo                       Driver poco conduttivo
                                                                        24
