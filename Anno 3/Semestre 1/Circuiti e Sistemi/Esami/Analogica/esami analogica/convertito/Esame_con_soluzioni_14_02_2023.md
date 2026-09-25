---
fonte: "Esame_con_soluzioni_14_02_2023.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Complementi di Circuiti e sistemi
                   elettronici
                                             Anno accademico 2022/2023


Prova scritta di Elettronica Analogica
                                                14 Febbraio 2023
Considerando il circuito riportato in figura
                                                                                                                        1
                                                                                                                          𝜇 𝐶 = 50𝜇𝐴/𝑉 $
                                                                                                                        2 ! "#
                                                                             5V
                                                                                                                        1
                                                       (4/1)                        (4/1)        (8/1)                    𝜇 𝐶 = 25𝜇𝐴/𝑉 $
                                                           M3                    M4              M5              50uA   2 % "#
                                R1
                                                         V2                 V3                                          𝑉&! = +𝑉&% + = 1𝑉
                                                                                        Cc                       Vout
                   R1            5V                             M1          M2
                            -         Vout        V-           (2/1)        (2/1)           V+
                                                                                                 V4
                                                                                                         (8/1)          𝑟" = 1 𝑀Ω
                            +
               C                                                       V1                                        M6
 Vin
                        R       -5V                                                                                     𝑅' = 200𝑘Ω
                                                                              50uA                    50uA
                                                                                                                        𝑅 = 100𝑘Ω
                                                               -5V

                                                                                                                        𝐶 = 20𝑛F
                            a)                                                          b)
                                                                                                                        𝐶( = 20𝑝F


       1. (Punti 6) Calcolare l’espressione del guadagno ideale di segnale tra Vo(s) e Vin(s).
       2. (Punti 6) Calcolare tutte le tensioni (V1, V2, V3, V4, V5 e Vo) e tutte le correnti di
          polarizzazione dello schema considerando Vin=0V.
       3. (Punti 8) Calcolare il guadagno d’anello in continua.
       4. (Punti 10) Calcolare il guadagno d’anello in frequenza, tracciarne il diagramma
          asintotico, calcolare la frequenza di attraversamento dell’asse a 0db e il margine di
          fase.
       5. (Punti 3) Tracciare il diagramma asintotico del modulo del guadagno reale.




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                       Anno accademico 2022/2023


                                               Soluzioni
         𝒗𝒐𝒖𝒕 (𝒔)   𝟏&𝒔𝑪𝑹
    1.   𝒗𝒊𝒏 (𝒔)
                  = 𝟏)𝒔𝑪𝑹
    2. ID1= ID2=25uA
       V1=-1.5V
       V2= 3.5V
       |Vgs5|=|Vgs3,4|=1.5V
       V3=V2=3.5V
       |Vgs6|=1.5V
       V4=-1.5V

                                                           𝑅1
    3.   𝐺*++, (0) = −𝑔𝑚1,2 '𝑟0 4 ∥ 𝑟0 2 ( 𝑔𝑚5 𝑟0 5               1    = −4.94𝑘
                                                        2 𝑅1 +
                                                                 𝑔𝑚6
               34         7&
    4.   𝑓2 = $56&,(          &     = 393𝐾𝐻𝑧
                    ) $ 7& 8 *+
                                ,
                                                         𝑓2          𝑓2
                                     𝜑4 ≅ 180° − tan−1 B C − tan−1 D E = 76°
                                                        𝑓%'         𝑓9$
    5.


                              𝒗𝒐𝒖𝒕 (𝒔) 𝟏 − 𝒔𝑪𝑹 𝑮𝒍𝒐𝒐𝒑 (𝒔)        𝑮𝒅𝒊𝒓 (𝒔)
                                      =                      +
                              𝒗𝒊𝒏 (𝒔)   𝟏 + 𝒔𝑪𝑹 𝟏 − 𝑮𝒍𝒐𝒐𝒑 (𝒔) 𝟏 − 𝑮𝒍𝒐𝒐𝒑 (𝒔)




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2022/2023




                                       Svolgimento
    1. Calcolare l’espressione del guadagno ideale di segnale tra Vout(s) e Vin(s) .
       Il generatore di segnale può essere sdoppiato in due generatori distinti non collegati
       fra loro, uno connesso alla resistenza R1 e l’altro alla capacità C.
       Il guadagno dello schema può essere calcolato sovrapponendo gli effetti
                                             𝒗𝒐𝒖𝒕 (𝒔) 𝟏 − 𝒔𝑪𝑹
                                                     =
                                             𝒗𝒊𝒏 (𝒔)   𝟏 + 𝒔𝑪𝑹


    2. Calcolare tutte le tensioni (V1, V2, V3, V4, V5 e Vo) e tutte le correnti di
       polarizzazione dello schema considerando Vin=2.5V.

         Le correnti di polarizzazione si divideranno
         ID1= ID2=25uA
         La tensione V+ = V- sarà pari a 0.
         Quindi la tensione V1 e V2 si potranno esprimere come
         V1=- Vgs1,2=-1.5V
         V2= 5- |Vgs3,4|=3.5V
         In uscita invece le tensioni saranno
         |Vgs5|=|Vgs3,4|=1.5V
         V3=V2=3.5V
         |Vgs6|=1.5V
         V4=0-|Vgs6|=-1.5V


    3. Calcolare il guadagno d’anello in continua.
       Considerando la polarizzazione abbiamo i seguenti valori di trasconduttanza
       trascurando l’effetto della modulazione di canale.
                  𝑔𝑚',$ ≅ 100𝜇𝐴/𝑉

                  𝑔𝑚:,; ≅ 200𝜇𝐴/𝑉

         Lo schema può essere tagliato in corrispondenza dell’ingresso invertente come
         riportato in figura.




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2022/2023

                                                                             𝑅1
                         𝐺*++, (0) = −𝑔𝑚1,2 '𝑟0 4 ∥ 𝑟0 2 ( 𝑔𝑚5 𝑟0 5                1
                                                                                        = −4.94𝑘
                                                                        2 𝑅1 +
                                                                                  𝑔𝑚6

                                          :𝐺*++, (0):89 = 73.87𝑑𝑏




                   (4/1)                        (4/1)                (8/1)
                                                                                                R1
                        M3                   M4                     M5
                                                                                                     Gloop Vtest

                      V2                V3                                       R1
                                                      Cc
              V-             M1         M2
                           (2/1)        (2/1)           V+                    (8/1)

Vtest                              V1                                                      M6



                                                             R
                                           C

    4. Calcolare il guadagno d’anello in frequenza e tracciarne il diagramma asintotico e
       calcolare la frequenza di attraversamento dell’asse a 0db.
       Il guadagno d’anello ha 2 poli e 2 zeri dato che la funzione di trasferimento per 𝜔 → ∞
       tende ad un valore diverso da 0. La tensione della capacità C rappresenta una variabile
       di stato non raggiungibile e il suo polo si semplifica con lo zero
                                                          (1 + 𝑠𝜏𝑧1 )(1 − 𝑠𝜏𝑧2 )
                               𝐺*++, (𝑠) = 𝐺*++, (0)
                                                         '1 + 𝑠𝜏𝑝1 ( (1 + 𝑠𝜏𝑝2 )

         Le due costanti di tempo possono essere espresse come




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2022/2023

                                    ⎧𝜏𝑝1 = 𝐶1 G'1 + 𝑔𝑚5 𝑟0 5 ('𝑟0 4 ∥ 𝑟0 2 ( + 𝑟0 5 H
                                    ⎪                        𝐶    1
                                                         𝜏𝑧2 =
                                    ⎨                         𝑔𝑚5
                                    ⎪
                                    ⎩                 𝜏𝑝2 = 𝜏𝑧1 = 𝐶𝑅



         Quindi il polo sarà alla frequenza
                                                       𝑓%' = 78𝐻𝑧
                                                    𝑓%$ = 𝑓9' = 79𝐻𝑧


         E lo zero destro è una configurazione

                                                              𝑔𝑚:
                                                       𝑠9' =
                                                               𝐶(
                                                     𝑓9$ = 1.59𝑀𝐻𝑧

         L’attraversamento dell’asse a 0db sarà

                                                𝑔𝑚',$     𝑅'
                                         𝑓2 =                    = 393𝐾𝐻𝑧
                                                2𝜋𝐶( 2 𝑅 + 1
                                                        '    𝑔𝑚;



                                                          𝑓2             𝑓2
                               𝜑4 ≅ 180° − tan−1 B           C − tan−1 D E = 76°
                                                         𝑓%'            𝑓9$



                                   "$%%! !




                                                                             !&'
                                                           X
                                                           0
                                                          !!" !!'       !#
                                                          !!'
                                                          !&"




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2022/2023


    5. Tracciare il diagramma asintotico del modulo del guadagno reale.

         Il generatore di segnale può essere sdoppiato in due generatori distinti non collegati
         fra loro, uno connesso alla resistenza R1 e l’altro alla capacità C.
         Il guadagno dello schema può essere calcolato sovrapponendo gli effetti.
            𝒗𝒐𝒖𝒕 (𝒔)          𝟏           𝑮𝒅𝒊𝒓 (𝒔)      𝒔𝑪𝑹         𝟐
                     =−                +             +
            𝒗𝒊𝒏 (𝒔)     𝟏 − 𝑮𝒍𝒐𝒐𝒑 (𝒔)&𝟏 𝟏 − 𝑮𝒍𝒐𝒐𝒑 (𝒔) 𝟏 + 𝒔𝑪𝑹 𝟏 − 𝑮𝒍𝒐𝒐𝒑 (𝒔)&𝟏

         Quindi


                          𝒗𝒐𝒖𝒕 (𝒔) 𝟏 − 𝒔𝑪𝑹 𝑮𝒍𝒐𝒐𝒑 (𝒔)        𝑮𝒅𝒊𝒓 (𝒔)
                                  =                      +
                          𝒗𝒊𝒏 (𝒔)   𝟏 + 𝒔𝑪𝑹 𝟏 − 𝑮𝒍𝒐𝒐𝒑 (𝒔) 𝟏 − 𝑮𝒍𝒐𝒐𝒑 (𝒔)

         Dove
                                                           1
                                                          𝑔𝑚6
                                            𝑮𝒅𝒊𝒓 =               1
                                                                      = 0.0123
                                                     2 𝑅1 +
                                                                𝑔𝑚6
         Quindi
                                   𝑔𝑚1,2       𝑅1
                                   𝑔𝑚5               1
                                 2 𝑅1 +
                𝒗𝒐𝒖𝒕 (𝒔)                𝑔𝑚6                              𝑮𝒅𝒊𝒓
          𝐥𝐢𝐦 M         M=    𝑔𝑚                           +        𝑔𝑚                      = 𝟎. 𝟑𝟒𝟒𝟐
          𝝎→< 𝒗𝒊𝒏 (𝒔)           1,2     𝑅1                                       𝑅1
                           𝟏−         𝑔𝑚5             1         𝟏 − 𝑔𝑚1,2              1
                                            2 𝑅1 +                     5    2 𝑅1 +
                                                     𝑔𝑚6                              𝑔𝑚6



                                $&'% #
                                 $!( #       !!" " !)&&* "


                                             !!" "
                                                           #%

                                                                !#$ "




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
