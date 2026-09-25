---
fonte: "Testo270121️_moretto.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Complementi di Circuiti e sistemi
                      elettronici
                                                        Anno accademico 2020/2021


Prova scritta di Elettronica Analogica
                                                              27 Gennaio 2021

                                                                            1.65 V+ VIN
                                                                                          +          Vout        1
                                                                                                                   𝜇 𝐶 = 100𝜇𝐴/𝑉 $
                                                                                           -                     2 ! "#
                  3.3 V                                                                        R2
                                                                                                                 1
              (2/1)        (2/1)                                                                                   𝜇 𝐶 = 20𝜇𝐴/𝑉 $
                                                                                                                 2 % "#
        M3                          M4
                                                (2/1)              (16/1)                      C1
                                                                                                            CL   𝑉&! = *𝑉&% * = 0.6𝑉
        Vb                                              M5         M8                     R1

               M1            M2
                                                                              1.65 V
                                                                                                                 𝑟" = 1 𝑀Ω
                                                                   Vout                        (a)
 Vin1        (10/1)        (10/1)        Vin2
                                                                            1.65 V+ VIN
                                                                                           -         Vout
                                                                                                                 𝐶' = 10𝑝F
                      Va                                      Vc
                                                         M6        (16/1)
                                                                    M7
                                                                                           +                     𝐶( = 100𝑝𝐹
                                                (2/1)
                                                                                               R2
                             20uA
                                                                                                                 𝑅' = 10𝐾Ω
                                                                                          R1 (b)                 𝑅$ = 100𝐾Ω
                                                                               1.65 V


        1. (Punti 3) Considerando lo schema di sinistra definire quale dei due terminali Vin1 e Vin2
           rappresenta il terminale di ingresso positivo V+ e negativo V- dell’amplificatore
        Considerando lo schema di figura (a):
        2. (Punti 6) Calcolare l’espressione del guadagno ideale di segnale tra vout(s) e vin(s) nello
           schema di figura (a)
        3. (Punti 2) Calcolare tutte le tensioni (Va, Vb e Vout) e tutte le correnti di polarizzazione
           dello schema considerando Vin=0 V.
        4. (Punti 9) Calcolare il guadagno d’anello in continua
        5. (Punti 7) Calcolare il guadagno d’anello in frequenza, tracciarne il diagramma asintotico
           e calcolare la frequenza di attraversamento dell’asse a 0db e valutarne il margine di fase
        6. (Punti 3) Tracciare il diagramma del guadagno reale in frequenza
        Considerando lo schema di figura (b) a retroazione positiva
        7. (Punti 3) tracciare la caratteristica ingresso uscita (Vin, Vout)




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                      Anno accademico 2020/2021




                                               Soluzioni
    1. Vin1 corrisponde all’ingresso non invertente V+ dell’amplificatore e Vin2 all’ingresso
       invertente V-.
                                  𝒔𝑪𝟏 𝑹𝟏 𝑹𝟐
         𝒗𝒐𝒖𝒕 (𝒔)   (𝑹𝟐 &𝑹𝟏 )(𝟏&        )
                                 𝑹𝟏 +𝑹𝟐
    2.   𝒗𝒊𝒏 (𝒔)
                  =     𝑹𝟏 (𝟏&𝒔𝑪𝟏 𝑹𝟐 )
    3. Va=0.95, Vb=2.2V, Vc=0.82V e Vo = 1.65 V
                           𝑔𝑚1,2 8 ,-, - ∥-, . ∥(// &/0 )0//
    4. 𝐺)**+ (0) = −                   // &/0
                                                                = −13.11
                                        (1+𝑠𝜏𝑧1 )
    5.   𝐺)**+ (𝑠) = 𝐺)**+ (0) ,1+𝑠𝜏 0,1+𝑠𝜏 0
                                          𝑝1         𝑝2



         𝑓%' ≅ 17.68 𝐾𝐻𝑧
         𝑓%$ ≅ 1.93𝑀𝐻𝑧
         𝑓1' = 160𝑘𝐻𝑧




            "$%%! !




                                                                   !#
                                     X          0           X
                                    !!"        !'"        !!&

                             𝑓3          𝑓3          𝑓3
         𝜑2 ≅ 180° − 𝑡𝑎𝑛−1 @ A + 𝑡𝑎𝑛−1 B C − 𝑡𝑎𝑛−1 @ A = 114°
                            𝑓%'         𝑓1'         𝑓%$




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                         Anno accademico 2020/2021



    6.



                       "$%%! !   "&' !




           "*+ !




                                                   "&' !
                            X      0X        X0
                           !!"     !)"    !!( !#



    7.




                                                    !#$%

                                          3.3V




                                         "%)*              "&ℎ+                        !!"




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021


                                       Svolgimento
    1. Considerando lo schema di sinistra definire quale dei due terminali Vin1 e Vin2
       rappresenta il terminale positivo V+ e il terminale V- dell’amplificatore
       Vin1 corrisponde all’ingresso non invertente V+ dell’amplificatore e Vin2 all’ingresso
       invertente V-.




    2. Calcolare l’espressione del guadagno ideale di segnale tra vo(s) e vin(s) nello schema
       di figura (a).
       Lo schema è retroazionato negativamente, considerando l’amplificatore avere un
       guadagno molto alto a tutte le frequenze la funzione di trasferimento Vout(s) e Vin(s)
       tende ad essere come la seguente:
                                                                     𝑹𝟏 𝑹𝟐
                        𝒗𝒐𝒖𝒕 (𝒔) 𝒗𝒐𝒖𝒕 (𝒔) (𝑹𝟐 + 𝑹𝟏 ) (𝟏 + 𝒔𝑪𝟏 𝑹𝟏 + 𝑹𝟐 )
                                 =          =
                         𝒗𝒊𝒏 (𝒔)    𝒗𝒊𝒏 (𝒔)       𝑹𝟏        (𝟏 + 𝒔𝑪𝟏 𝑹𝟐 )

    3. Calcolare tutte le tensioni (Va, Vb, Vc e Vo) e tutte le correnti di polarizzazione dello
       schema considerando Vin=0 A.
        Considerando i transistori in saturazione, la corrente nei rami del primo stadio è da
       10uA. Di conseguenza Vgs1,2= 0.7V con Va=0.95, |Vgs3|= 1.1V con Vb=2.2V ed essendo la
       corrente riflessa dallo specchio M4, M5 abbiamo Vgs6= Vc=0.82V. Nello stadio di uscita
       avremo Vo= 1.65V e la corrente dell’ultimo stadio M8 / M7 sarà di 80 uA.

    4. Calcolare il guadagno d'anello in continua
       Considerando la polarizzazione abbiamo i seguenti valori di trasconduttanza di segnale
       trascurando l’effetto della modulazione di canale.
                                   𝑔𝑚',$ ≅ 200𝜇𝐴/𝑉


                                       𝑔𝑚1,2 8 8𝑟9 : ∥ 𝑟9 ; ∥ (𝑅< + 𝑅= )<𝑅<
                     𝐺)**+ (0) = −                                               = −13.11
                                                       𝑅< +𝑅=

                                          =𝐺)**+ (0)=>? = 22.35𝑑𝐵




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021

    5. Calcolare il guadagno d’anello in frequenza e tracciarne il diagramma asintotico e
       calcolare la frequenza di attraversamento dell’asse a 0db.
       Il guadagno d’anello ha 2 poli e 1 zeri


                                                                 (1 + 𝑠𝜏𝑧1 )
                                𝐺)**+ (𝑠) = 𝐺)**+ (0)
                                                            81 + 𝑠𝜏𝑝1 <81 + 𝑠𝜏𝑝2 <

         Le capacità C1 e CL sono interagenti e si può usare il metodo delle costanti di tempo.

                                          𝜏𝑝1 + 𝜏𝑝2 = 𝐶1 𝑅′ 1 + 𝐶𝐿 𝑅′ 𝐿
                                        C                1         1
                                         𝜔𝑝1 + 𝜔𝑝2 =          +
                                                      𝐶1 𝑅 1 𝐶𝐿 𝑅′′ 𝐿
                                                           ′′


         Dove
                                    𝑅:' = 𝑅$ ||(𝑅' + 𝑟0 7 ∥ 𝑟0 8 ) = 83.6𝑘Ω


                                                   𝑅::' = 𝑅$ ||𝑅' = 9𝑘Ω

         e
                                    𝑅: ( = (𝑟0 ∥ 𝑟0 8 )||(𝑅' + 𝑅$ ) = 90𝑘Ω
                                               7


                                            𝑅:: ( = (𝑟0 ∥ 𝑟0 8 )|| 𝑅' = 9.8𝑘Ω
                                                        7
         Quindi i poli saranno
                                                     𝑓%' ≅ 17.68 𝐾𝐻𝑧
                                                      𝑓%$ ≅ 1.93𝑀𝐻𝑧



         lo zero può essere calcolato considerando

                                                    𝜏1' = 𝐶' 𝑅$ = 1𝜇𝑠

                                                      𝑓1' = 160𝑘𝐻𝑧


         Essendo

                                            *𝐺𝑙𝑜𝑜𝑝 M𝑓%$ N* ≅ 𝑓%' *𝐺𝑙𝑜𝑜𝑝 (0)*/𝑓1'




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021

         L’attraversamento dell’asse a 0db sarà a 20db per decade quindi avremo

                                           𝑓3 ≅ *𝐺𝑙𝑜𝑜𝑝 M𝑓%$ N* 𝑓%$ = 2.88𝑀𝐻𝑧



            "$%%! !




                                                              !#
                                    X        0        X
                                   !!"     !'"      !!&

                                         𝑓3          𝑓3          𝑓3
                     𝜑2 ≅ 180° − 𝑡𝑎𝑛−1 @ A + 𝑡𝑎𝑛−1 B C − 𝑡𝑎𝑛−1 @ A = 114°
                                        𝑓%'         𝑓1'         𝑓%$

    Ovviamente questo risultato è ottenuto considerando il diagramma asintotico e, dato che
    le singolarità sono vicine all’attraversamento, l’approssimazione non molto vicina alla
    realtà.

    6.    Tracciare il digramma asintotico di bode del guadagno reale.

         Il circuito di figura non ha un trasferimento diretto




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021




                                          "$%%! !    "&' !




                           "*+ !




                                                                        "&' !
                                                X       0X       X0
                                               !!"      !)"   !!( !#




    7. Considerando lo schema di figura (b) a retroazione positiva tracciare la caratteristica
       ingresso uscita (Vin, Vout).
       Lo schema di figura (b) ha una retroazione positiva e quindi il punto di equilibrio in cui
       V+ e V- hanno un valore di tensione quasi identico non è più stabile. In queste condizioni
       si può considerare lo stadio differenziale in ingresso completamente sbilanciato in una
       direzione o nell’altra dipendentemente da Vin o dallo stato precedente. Se lo stadio è
       sbilanciato i transitori M8 e M7 sono in zona triodo (considerandoli in saturazione la
       corrente uscente o entrante sarebbe di 160uA incompatibile con la resistenza R1+R2
       connessa in uscita e la tensione di alimentazione di 3.3V). Approssimando la tensione di
       uscita a 3.3V o 0V e considerando il guadagno dell’amplificatore alto le soglie rispetto a
       Vin possono essere approssimate a:

                                   𝑉3;< ≅ (3.3𝑉 − 1. 𝟔𝟓𝑽) 𝑅' /( 𝑅' + 𝑅$ ) = 150𝑚𝑉

                                    𝑉3;= ≅ (−1. 𝟔𝟓𝑽) 𝑅' /( 𝑅' + 𝑅$ ) = −150𝑚𝑉

         A causa del guadagno limitato dell’amplificatore |𝑉𝑡ℎ+,− | < 150𝑚𝑉 .




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021


                                                !#$%

                                       3.3V




                                    "%)*             "&ℎ+                              !!"




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
