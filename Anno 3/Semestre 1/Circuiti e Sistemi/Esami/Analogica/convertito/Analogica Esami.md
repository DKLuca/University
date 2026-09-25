---
fonte: "Analogica Esami.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

OneNote                                    https://euc-onenote.officeapps.live.com/o/onenoteframe.aspx?ui=it%2D...



          Esercizio tema d'esame 1
          martedì 17 novembre 2020 21:29




          Testo230…




1 of 4                                                                                          16/09/2021, 19:11
            Complementi di Circuiti e sistemi
                    elettronici
                                          Anno accademico 2019/2020


Prova scritta di Elettronica Analogica
                                                     23 Gennaio 2020

Considerando il circuito riportato in figura
                             5V

                     (2/1) (2/1)                         (8/1)        1
                                                                        # $ = 50#(/* $
  (2/1)             M4        M3
                                               V2
                                                         M5           2 ! "#
 M7                                                                   1
                                                                        # $ = 25#(/* $
                                                                      2 % "#

                     M1     M2
                                     C1
                                                R2
                                                                      *&! = +*&% + = 1*
                                                         Vout
                    (2/1)   (2/1)
           Vin                            V1                          ," = 10 .Ω
                                                                 CL
                                           R1
                                                                      0' = 51Ω
                              50uA         C1
                                                                      0$ = 101Ω
                    0V

                                          V3                          $' = 2002F
  (2/1)                                                  M6

      M8                                                 (8/1)        $( = 14F
                    0V




       1. (Punti 6) Calcolare tutte le tensioni (V1, V2, V3 e Vout) e tutte le correnti di polarizzazione
          dello schema considerando Vin=2.5V.
       2. (Punti 6) Calcolare l’espressione del guadagno ideale di segnale tra Vout(s) e Vin(s)
       3. (Punti 10) Calcolare il guadagno d’anello in continua.
       4. (Punti 8) Calcolare il guadagno d’anello in frequenza, tracciarne il diagramma
          asintotico e calcolare la frequenza di attraversamento dell’asse a 0db.
       5. (Punti 3) Valutare il margine di fase del guadagno d’anello e tracciare il diagramma
          asintotico di bode del guadagno reale.




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2019/2020


                                             Soluzioni
    1. V2=5V-|Vgs5|=5V-1.7V=3.29V
       V3= Vgs6=1.5 V
       ID5= -1/2upCox(W/L)5(Vov5)2=-100uA
       ID6= 1/2upCox(W/L)6(Vov6)2=100uA
       Vout= V1=2.5V
       ID1= ID2=25uA
       V1=2.5V- Vgs1,2=1V
       V2= 5- |Vgs3,4|=3.5V
       |Vgs5|=|Vgs3,4|=1.5V
       V3=V2=3.5V
       |Vgs6|=1.5V
       V4=2.5V-|Vgs6|=3.5V

         !!"# (#)     #% &    '(#%& (&& (&' )
    2.            =1+ & ' =
          !$% (#)    '(#%& &&   '(#%& &&
    3. $)**+ (0) = −)*',- 4 -.. / ∥ .. 0 0 = 22
    4.
                                                                        (1 + 78)1 )
                                 $)**+ (3) = $)**+ (0)
                                                              (1 + 78+1 )(1 + 78+2 )

                                                           :%( = 26.5=>
                                                         :%- = 63.691=>

                                                         :.' = 159.151=>

                                               :/ ≅ :%( $1223 (0) = 53267
                                    1                    1                      1
    5. B0 ≅ 180° − tan−1 C1 ! D − tan−1 C1 ! D + tan−1 E1 ! F = 68.69°
                                    "#                   "$                         %#




                                         '())" ! '+, !



                                                                               '+, !


                                                              !$

                                                                       !"%
                                               X              o    X      o
                                                                          X
                                               !"#                            !&#


                                                                                         '- !




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2019/2020


                                       Svolgimento
    1. Calcolare tutte le tensioni (V1, V2, V3 e Vout) e tutte le correnti di polarizzazione
       dello schema considerando Vin=2.5V.
       Lo schema è retroazionato negativemente, quindi si può calcolare le condizioni di
       polarizzazione considerando V1= 2.5V.
       Di conseguenza la corrente ID1= ID2=25uA
       V2=5V-|Vgs5|=5V-1.7V=3.29V
       V3= Vgs6=1.5 V
       ID5= -1/2upCox(W/L)5(Vov5)2=-100uA
       ID6= 1/2upCox(W/L)6(Vov6)2=100uA
       Vout= V1=2.5V
    2. Calcolare l’espressione del guadagno ideale di segnale tra vout(s) e vin(s)
       Lo schema è retroazionato negativemente, considerando l’amplificatore avere un
       guadagno molto alto a tutte le frequenze la funzione di trasferimento vout(s) e vin(s)
       tende ad essere come la seguente.
                           A678 (B)          BD; E<      C + BD; (E; + E< )
                                    =C+               =
                            A9: (B)       C + BD; E;         C + BD; E;
    3. Calcolare il guadagno d'anello in continua
       Considerando la polarizzazione abbiamo i seguenti valori di trasconduttanza di segnale
       trascurando l’effetto della modulazione di canale.
                   GH',$ ≅ 100#(/*


                                 $)**+ (0) = −)*',- 4 -.. / ∥ .. 0 0 = 22

                                            F$)**+ (0)F=> = 66GH

    4. Calcolare il guadagno d’anello in frequenza e tracciarne il diagramma asintotico e
       calcolare la frequenza di attraversamento dell’asse a 0db.
       Il guadagno d’anello ha 2 poli e 1 zero


                                                                 (1 + 78)1 )
                                 $)**+ (3) = $)**+ (0)
                                                           (1 + 78+1 )(1 + 78+2 )

         Le due costanti di tempo possono essere espresse come




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2019/2020

         Dove

                                               8+1 + 8+2 = $3 0′ 3 + $1 0′ 1
                                             I                1         1
                                              I+1 + I+2 =          +
                                                           $5 0 3 $1 0′′ 1
                                                                ′′



         Dove

                                                06 ( ≅ J,7 8 ∥ ,7 9 L = 5.Ω

                                       066 ( ≅ ,7 8 ∥ ,7 9 ∥ (0' + 0$ ) = 14.95NΩ

                                       06' ≅ 0' + 0$ + J,7 8 ∥ ,7 9 L = 5.015.Ω

                                                 066' ≅ 0' + 0$ = 15NΩ


         Quindi i poli saranno
                                                       :%( = 26.5=>
                                                     :%- = 63.691=>


         Gli zeri possono essere calcolati considerando
                                                                   1
                                                       7.' = −
                                                                 $' 0'
         Quindi
                                                     :.' = 159.151=>

         L’attraversamento dell’asse a 0db sarà

                                               :/ ≅ :%( $1223 (0) = 53267




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2019/2020

                                                %&''" !




                                                                 !$

                                                                      !"(
                                                     X                 X o
                                                     !"#                     !)#




    5. Valutare il margine di fase del guadagno d’anello e tracciare il digramma asintotico di
       bode del guadagno reale.
                                         :/          :/          :/
                     B0 ≅ 180° − tan−1 P Q − tan−1 P Q + tan−1 C D = 68.69°
                                        :%'         :%$         :.'


                                   '())" ! '+, !



                                                                             '+, !


                                                            !$

                                                                  !"%
                                          X                 o X      o
                                                                     X
                                          !"#                            !&#


                                                                                     '- !




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
           Complementi di Circuiti e sistemi
                   elettronici
                                       Anno accademico 2018/2019


Prova scritta di Elettronica Analogica
                                              21 gennaio 2019

Considerando il circuito riportato in figura

                   5V                                 5V
                                                                              1
                                                M6                              # % = 30#+/- .
                                                                              2 $ &'
                             60uA             (4/1)                3V
                                                                              1
                        Va                                                      # % = 30#+/- .
                                                                              2 0 &'

            M1           M2           Vin+2.5V              Vout              -1$ = 2-10 2 = 1-
 Vm
           (4/1)         (4/1)                                                3& = 1 4Ω         per M1,2,3,4
                                                                   R1
                                         Cc                                   3& = 250 7Ω       per M5,6
            Vb                   Vc
                                                                              89 = 1007Ω
                                                M5
      M3                         M4                                           8. = 47Ω
                                                                   R2
   (1/1)                         (1/1)                     C1                 %9 = 10;F
                                              (4/1)                           %= = 100>F




      1. (Punti 8) Calcolare tutte le tensioni (Va,Vb,Vc,Vm e Vout) e tutte le correnti di
         polarizzazione dello schema.
      2. (Punti 4) Calcolare l’espressione del guadagno ideale di segnale tra vout(s) e vin(s) .
      3. (Punti 8) Calcolare il guadagno d’anello in continua e la resistenza di uscita ad anello
         chiuso.
      4. (Punti 5) Tracciare il diagramma asintotico del guadagno d’anello in frequenza e
         calcolare la frequenza di attraversamento dell’asse a 0db e il margine di fase.
      5. (Punti 3) Tracciare il diagramma asintotico del modulo del guadagno reale.




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
           Complementi di Circuiti e sistemi
                   elettronici
                                       Anno accademico 2018/2019


Prova scritta di Elettronica Analogica
                                              21 gennaio 2019

Considerando il circuito riportato in figura

                   5V                                 5V
                                                                              1
                                                M6                              # % = 30#+/- .
                                                                              2 $ &'
                             60uA             (4/1)                3V
                                                                              1
                        Va                                                      # % = 30#+/- .
                                                                              2 0 &'

            M1           M2           Vin+2.5V              Vout              -1$ = 2-10 2 = 1-
 Vm
           (4/1)         (4/1)                                                3& = 1 4Ω         per M1,2,3,4
                                                                   R1
                                         Cc                                   3& = 250 7Ω       per M5,6
            Vb                   Vc
                                                                              89 = 1007Ω
                                                M5
      M3                         M4                                           8. = 47Ω
                                                                   R2
   (1/1)                         (1/1)                     C1                 %9 = 10;F
                                              (4/1)                           %= = 100>F




      1. (Punti 8) Calcolare tutte le tensioni (Va,Vb,Vc,Vm e Vout) e tutte le correnti di
         polarizzazione dello schema.
      2. (Punti 4) Calcolare l’espressione del guadagno ideale di segnale tra vout(s) e vin(s) .
      3. (Punti 8) Calcolare il guadagno d’anello in continua e la resistenza di uscita ad anello
         chiuso.
      4. (Punti 5) Tracciare il diagramma asintotico del guadagno d’anello in frequenza e
         calcolare la frequenza di attraversamento dell’asse a 0db e il margine di fase.
      5. (Punti 3) Tracciare il diagramma asintotico del modulo del guadagno reale.




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2018/2019


                                             Soluzioni
    1.
         ID1= ID2=-30uA
         Va=2.5V+|Vgs1,2|=4V
         Vb= Vgs3,4=2V
         ID6=-1/2upCox(W/L)6(Vov6)2=-120uA
         Vc= Vgs5=2V
    2.

         ?&@A (C)       C%9 89     1 + C%9 (89 + 8. )
                  =1+            =
         ?E$ (C)      1 + C%9 8.      1 + C%9 8.

    3.   GH&&0 (0) = −JK1,2 M30 2 ∥ 30 4 O JK5 M30 6 ∥ 30 5 O = −1800
                         8&@A TS           M 30 6 ∥ 30 5 O
         8&@A RS =                    =                       = 69.4Ω
                      1 − GUVV>(0)        1 − GUVV>(0)
                                   (1+CYZ1 )(1−CYZ2 )
    4.   GH&&0 (C) = GH&&0 (0)
                                   (1+CY>1 )(1+CY>2 )
                                                                                        '())" !
         [0S = 41.31\Z
         [0] = 363\Z
         [^9 = 47\Z
         [^. = 3827\Z                                                                                    !&

              JK9,. 8.                                                                       X      X o             o
         [A ≅               = 7.347\Z                                                        !"#   !"$ !%#    !%$
              2` %= 8. + 89




    5.
                                                 '())" ! '+, !




                                                                         '+, !



                                                        X o X o              o
                                                        !"# !"$ !%# !&     !%$
                                                                                 '- !




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2018/2019


                                             Soluzioni
    1.
         ID1= ID2=-30uA
         Va=2.5V+|Vgs1,2|=4V
         Vb= Vgs3,4=2V
         ID6=-1/2upCox(W/L)6(Vov6)2=-120uA
         Vc= Vgs5=2V
    2.

         ?&@A (C)       C%9 89     1 + C%9 (89 + 8. )
                  =1+            =
         ?E$ (C)      1 + C%9 8.      1 + C%9 8.

    3.   GH&&0 (0) = −JK1,2 M30 2 ∥ 30 4 O JK5 M30 6 ∥ 30 5 O = −1800
                         8&@A TS           M 30 6 ∥ 30 5 O
         8&@A RS =                    =                       = 69.4Ω
                      1 − GUVV>(0)        1 − GUVV>(0)
                                   (1+CYZ1 )(1−CYZ2 )
    4.   GH&&0 (C) = GH&&0 (0)
                                   (1+CY>1 )(1+CY>2 )
                                                                                        '())" !
         [0S = 41.31\Z
         [0] = 363\Z
         [^9 = 47\Z
         [^. = 3827\Z                                                                                    !&

              JK9,. 8.                                                                       X      X o             o
         [A ≅               = 7.347\Z                                                        !"#   !"$ !%#    !%$
              2` %= 8. + 89




    5.
                                                 '())" ! '+, !




                                                                         '+, !



                                                        X o X o              o
                                                        !"# !"$ !%# !&     !%$
                                                                                 '- !




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                       Anno accademico 2018/2019


                                           Svolgimento
    1. Calcolare tutte le tensioni (Va,Vb,Vc,Vm e Vout) e tutte le correnti di “drain” di
       polarizzazione dello schema
       Lo schema è retroazionato negativemente, quindi si può calcolare le condizioni di
       polarizzazione considerando Vm= 2.5V.
       Di conseguenza la corrente ID1= ID2=-30uA
       Va=2.5V+|Vgs1,2|=4V
       Vb= Vgs3,4=2V
       ID6=-1/2upCox(W/L)6(Vov6)2=-120uA
       Vc= Vgs5=2V
    2. Calcolare l’espressione del guadagno ideale di segnale tra vout(s) e vin(s)
       Lo schema è retroazionato negativemente, considerando l’amplificatore avere un
       guadagno molto alto a tutte le frequenze la funzione di trasferimento vout(s) e vin(s)
       tende ad essere come la seguente.
                           bcde (f)          fji ki       i + fji (ki + kl )
                                    = i+                =
                            bgh (f)        i + fji kl         i + fji kl
    3. Calcolare il guadagno d'anello in continua e la resistenza di uscita ad anello chiuso
       Considerando la polarizzazione abbiamo i seguenti valori di trasconduttanza
       trascurando l’effetto della modulazione di canale.
                   JK9,. ≅ 120#+/-

                    JKm ≅ 240#+/-

         Lo schema può essere tagliato in corrispondenza dell’ingresso inverterntente come
         riportato in figura

                                                                                 ro6
                                                           va

                                                    M1      M2                            vout

                                                   (4/1)    (4/1)
                                   vtest                                                         R1
                                                    vb              vc      Cc
                                                                                                      Gloop vtest
                                                                                   M5
                                            M3                      M4                           R2
                                           (1/1)                    (1/1)                C1
                                                                                 (4/1)




                        GH&&0 (0) = −JK1,2 M30 2 ∥ 30 4 O JK5 M30 6 ∥ 30 5 O = −1800




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2018/2019

                                            2GH&&0 (0)2        ≅ 65.1pq
                                                          no

Essendo il nodo di uscita un nodo della retroazione la resistenza di uscita ad anello chiuso può essere
espressa come

                                            8&@A TS            M 30 6 ∥ 30 5 O
                             8&@A RS =                    =                      = 69.4Ω
                                         1 − GUVV>(0)          1 − GUVV>(0)



    4. Tracciare il diagramma asintotico del guadagno d’anello in frequenza e calcolare la
       frequenza di attraversamento dell’asse a 0db e il margine di fase
       Il guadagno d’anello ha 2 poli (due capacità indipendenti) e 2 zeri dato che la funzione
       di trasferimento per r → ∞ non tende a 0.
                                                           (1 + CYZ1 )(1 − CYZ2 )
                                 GH&&0 (C) = GH&&0 (0)
                                                           (1 + CY>1 )(1 + CY>2 )


         Adottando il metodo delle costanti di tempo per calcolare il valore dei poli otteniamo

         Dove

                                               Y>1 + Y>2 = %v 8′ % + %1 8′ 1
                                             u                1         1
                                              r>1 + r>2 =          +
                                                           %v 8 % %1 8′′ 1
                                                                ′′



         Dove

                        8x R ≅ M3y . ∥ 3y z O {1 + JKm M3y | ∥ 3y m O} + M3y | ∥ 3y m O = 15.624Ω


          8xx R ≅ M3y . ∥ 3y z O {1 + JKm M3y | ∥ 3y m ∥ (89 + 8. )O} + M3y | ∥ 3y m ∥ (89 + 8. )O = 7.374Ω

         Che possono essere calcolate anche usando il teorema di Miller.

                                         8x9 = 89 + 8. + M3y | ∥ 3y m O = 2297Ω

                                   8xx9 = 89 + 8. + M3y | ∥ 3y m ∥ 1/ JKm O = 1087Ω




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2018/2019

         Quindi i poli saranno
                                                             [0S = 41.31\Z
                                                              [0] = 363\Z


         Gli zeri possono essere calcolati considerando
                                                                            1
                                                             C^9 = −
                                                                          %9 8.

                                                                          JKm
                                                              C^. =
                                                                           %=

         Quindi
                                                              [^9 = 47\Z

                                                             [^. = 3827\Z



                                                '())" !




                                                                     !&

                                                       X       X o                   o
                                                       !"#    !"$ !%#          !%$




         La frequenza di taglio può essere determinata dal diagramma di bode asintotico o
         considerando il circuito equivalente [^9 ≤ [ ≤ [^. .

                                                                               ro6
                                                               va

                                                        M1      M2                        vout


                                        vtest                                                    R1
                                                        vb           vc   Cc
                                                                                                      Gloop vtest
                                                                                M5
                                                  M3                 M4                          R2
                                                                                         C1




         Il guadagno d’anello per [^9 ≤ [ ≤ [^. tende ad essere




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2018/2019
                                                               JK1,2     82
                                              2GH&&0 (r)2 ≈
                                                                r %v 82 + 81

         Quindi si può stimare la frequenza di taglio

                                                    JK9,. 8.
                                             [A ≅                 = 7.347\Z
                                                    2` %= 8. + 89

         Il margine di fase può essere calcolato

                                    [A          [A          [A          [A
                €Å ≅ 180° − tan−1 Ü á − tan−1 Ü á + tan−1 à â − tan−1 à â = 63.4°
                                   [09         [0.         [^9         [^.

    5. Tracciare il diagramma asintotico del modulo del guadagno reale


                                          '())" ! '+, !




                                                                    '+, !



                                                X o X o                  o
                                                !"# !"$ !%# !&         !%$
                                                                               '- !




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
            Complementi di Circuiti e sistemi
                    elettronici
                                            Anno accademico 2019/2020


Prova scritta di Elettronica Analogica
                                                18 Giugno 2020

Considerando il circuito riportato in figura
                                                                          Vdd                            Vdd        1
                                                                                                                      ) ! = 60)+/- )
                                                                                                                    2 & '(
                                                              60uA                              60uA
                                                                                                                    1
 Vdd = 5V   (100/1)                     Vo                                                                            ) ! = 30)+/- )
                                                                             Va                                     2 * '(
                                                                   M1           M2                             Vg
                 M6                                    Vin1                                  Vin2                   -+& = /-+* / = 1-
                                       R2                         (4/1)         (4/1)
                                                                                                                    0' = 1 1Ω
                      +                           RL               Vb                   Vc
                                        Co
                      -                                                                             M5              3, = 505Ω
                                                                        M3   M4
                          1.2 V        R1
                                                          (1/1)                         (1/1)              (4/1)    3) = 87.55Ω

                                                                                                                    !' = 50)F

                                                                                                                    3- = 500Ω
                                  a)                                                 b)


     1. (Punti 6) Calcolare il valore della tensione Vo nello schema (a) di figura considerando
        ideale l’amplificatore operazionale.
     2. (Punti 4) Calcolare tutte le tensioni (Vin1, Vin2, Va, Vb, Vc, Vg e Vo) e tutte le correnti di
        polarizzazione dello schema.
     3. (Punti 8) Calcolare il guadagno d’anello in continua.
     4. (Punti 8) Calcolare il guadagno d’anello in frequenza considerando !!" $% = 20&' ,
        tracciarne il diagramma asintotico e valutare la frequenza di attraversamento dell’asse
        a 0db.
     5. (Punti 4) Valutare il margine di fase del guadagno d’anello
     6. (Punti 3) Cambia il guadagno d’anello se Vdd è uguale a 4V?




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2019/2020


                                            Soluzioni
    1. !! = #. #!
    2. Va= 2.7V
       Vb= 1.7V
       Vc= 1.5V
       Vo = 3.3 V
       Vg=2.52 V

                                                                  (.! ∥(." 0.# )) ."
    3. %"##$ (0) = −*+%,' -.( ) ∥ .( ' 0 *+* .( * *++                                  = 23.3K
                                                                       ." 0.#
    4.
                                                                      1
                                 %"##$ (4) = %"##$ (0)
                                                           (1 + $%!1 )(1 + $%!2 )

                                                         '*, = 6.3,-
                                                        '*) = 7.80,-


                                           '1 ≅ C/%2334 D'*) E/ '*) = 348,-


                                    3               3
    5. 92 ≅ 180° − tan−1 I3 ! J − tan−1 I3 ! J = 12.9°
                                    "#               "$




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2019/2020




                                       Svolgimento
    1. Calcolare il valore della tensione Vo nello schema (a) di figura considerando ideale
       l’amplificatore operazionale. Lo schema è retroazionato negativamente, considerando
       l’amplificatore avere un guadagno molto alto a tutte le frequenze la tensione di uscita
       può essere espressa come
                                           $" + $#
                                    !! = =          @ !$%& = '. '!
                                              $"

    2. Calcolare tutte le tensioni (Vin1, Vin2, Va, Vb, Vc, Vg e Vo) e tutte le correnti di
       polarizzazione dello schema.
       Lo schema è retroazionato negativamente, quindi si può calcolare le condizioni di
       polarizzazione considerando V+= 1.2V.
       Di conseguenza la corrente ID1= ID2=30uA
       Vgs1,2= 1.5V quindi
       Va= 1.5V + 1.2V= 2.7 V
       Vb=Vgs3,4= 1.7 V
       Mentre
       Vc= Vgs5=1.5V
       Considerando che Vo = 3.3V
       IDM6 ≅ 6.6mA,
       |Vgs6|= 2.48 V
       Vg=2.52 V

    3. Calcolare il guadagno d'anello in continua
       Considerando la polarizzazione abbiamo i seguenti valori di trasconduttanza di segnale
       trascurando l’effetto della modulazione di canale.
                                   ;<,,) ≅ 120)+/-

                                   ;<5 ≅ 240)+/-

                                    ;<% ≅ 8.9<+/-


                                                                   (5= ∥ (5% + 5' )) 5%
           )"##$ (0) = −./%,' -2( ) ∥ 2( ' 0 ./* 2( * ./+                               = -23.3K
                                                                         5% + 5'




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2019/2020

                                            C)"##$ (0)C>? = 87 =>

    4. Calcolare il guadagno d’anello in frequenza e tracciarne il diagramma asintotico e
       calcolare la frequenza di attraversamento dell’asse a 0db.
       Il guadagno d’anello ha 2 poli


                                                                      1
                                 )"##$ (?) = )"##$ (0)
                                                           (1 + AB01 )(1 + AB02 )

         Le due costanti di tempo possono essere espresse come

         Dove
                                                       B*, = !' 36'

                                            36' ≅ 54 ∥ (51 + 52 ) ≅ 500Ω



                                               B*) = !!" $% 07$5 = 20B?

         Quindi

                                                        D*, = 6.3EF
                                                       D*) = 7.85EF


         Essendo

                                                    D*, )7889 (0) > D*)

         L’attraversamento dell’asse a 0db sarà a 40db per decade quindi avremo

                                             D*, )7889 (0) = D*) /)7889 DD*) E/

                                                   /)7889 DD*) E/ = 18.8

         Considerando l’attraversamento a 40db/dec


                                           D1 ≅ C/)7889 DD*) E/ D*) = 34JEF




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2019/2020



                                                   "$%%! !




                                                         X            X
                                                        !!"          !!&    !#


5. Valutare il margine di fase del guadagno d’anello
                                                  D1          D1
                              K2 ≅ 180° − tan−1 N O − tan−1 N O = 12.9°
                                                 D*,         D*)
6.   Cambia il guadagno d'anello se Vdd è uguale a 4V?

Si, il guadagno cambia perché M6 non opera più in saturazione ma opera in zona triodo. In
queste condizioni si aggiunge in parallelo al nodo di uscita anche la conduttanza ;8"$%
riducendo il guadagno d’anello.




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
           Complementi di Circuiti e sistemi
                   elettronici
                                          Anno accademico 2018/2019


Prova scritta di Elettronica Analogica
                                                 17 giugno 2019

Considerando il circuito riportato in figura

     5V                  5V                           5V                    5V            5V   5V
                                                                                                               1
                                                                                                                 # % = 50#+/- .
                                                 M5                          M6      Cc                        2 $ &'
                                   60uA          (1/1)                      (1/1)                   Iout
           Iin                                                                                                 1
                              Va                                                                                 # % = 30#+/- .
                                                                                                               2 0 &'
                                                                       Ve                           M7 (4/1)
                  M1           M2
          Vi                                                    1.5V                                           -2$ = 3-20 3 = 1-
                 (4/1)         (4/1)             (1/1)                       (1/1)
                                                                                                      Vo       4& = 1 5Ω
                  Vb                                       M3          M4
                                                                                                               78 = 109Ω
                               Vc
R1                                                                                                             7. = 19Ω
                                                                                                      R2
                       40uA               40uA
                                                                                                               %: = 100;F




     1. (Punti 6) Calcolare l’espressione del guadagno ideale di segnale tra Iout(s) e Iin(s) .
     2. (Punti 6) Calcolare tutte le tensioni (Va,Vb,Vc,Vm e Vout) e tutte le correnti di
        polarizzazione dello schema considerando Iin=10µA
     3. (Punti 8) Calcolare il guadagno d’anello in continua
     4. (Punti 5) Tracciare il diagramma asintotico del guadagno d’anello in frequenza e
        calcolare la frequenza di attraversamento dell’asse a 0db
     5. (Punti 7) Tracciare il diagramma asintotico del modulo del guadagno reale.




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2018/2019




                                             Soluzioni
         =>?@ (B)   E
    1.            = EF = FH
          ==D (B)    G


    2. In ingresso ci sarà
       Vi=100m
       Considerando lo stadio differenziale circa in equilibrio avremo
       ID1= ID2=-30uA
       di conseguenza
       Va=Vi+|Vgs1,2|=1.6V
       Considerando il resto dello schema in equilibrio
       ID3= ID4=10uA e
       ID5= ID6=-10uA.
       Vi= Vo=100mV quindi avremo IR2=100uA= ID7
       Ve=0.1V+Vgs7=1.8V
       Vb= Vc=1.5- Vgs3,4=0.052V
                                        72
    3. IJ&&0 (0) = −LM1,2 O40 6 ∥ 4R4 T        = −25.85
                                         ⁄    72 +1 LM7

                                         4Z[ = 4\ . + 4\ ] O1 + 4\ . LM]T = 46.75



    4.   e5

                 %&''" !                                  %&''" ! %)* !




                                                                               %)* !
                                !$


                      X                                           X
                      !"#                                        !"#      !$
                                                                                       %+ !




                                                  LM8,.     7.
                                           ^_ ≅                    = 42def
                                                  2a %b 7. + 1⁄LMc




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2018/2019


                                       Svolgimento
    1. Calcolare l’espressione del guadagno ideale di segnale tra Iout(s) e Iin(s) .
       Lo schema è retroazionato negativemente con una struttura serie-serie, si trova che la
       tensione Vo ai capi della resistenza R2 viene eguagliata alla caduta sulla resistenza R1.
       Quindi il guadagno ideale sarà
                                          =>?@ (B) EF
                                                   =    = FH
                                           ==D (B)   EG

    2. Calcolare tutte le tensioni (Va,Vb,Vc,Vm e Vout) e tutte le correnti di polarizzazione
       dello schema considerando Iin=10µA.
       In ingresso ci sarà
       Vi=100m
       Considerando lo stadio differenziale circa in equilibrio avremo
       ID1= ID2=-30uA
       di conseguenza
       Va=Vi+|Vgs1,2|=1.6V
       Considerando il resto dello schema in equilibrio
       ID3= ID4=10uA e
       ID5= ID6=-10uA.
       Vi= Vo=100mV quindi avremo IR2=100uA= ID7
       Ve=0.1V+Vgs7=1.8V
       Vb= Vc=1.5- Vgs3,4=0.052V

    3. Calcolare il guadagno d'anello in continua
       Considerando la polarizzazione abbiamo i seguenti valori di trasconduttanza
       trascurando l’effetto della modulazione di canale.
                   LM8,. ≅ 120#+/-

                  LMg,] ≅ 44.7#+/-

                    LMc ≅ 282#+/-

         Lo schema può essere tagliato in corrispondenza dell’ingresso invertente come
         riportato in figura.




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                      Anno accademico 2018/2019

                                                        M5                     M6     Cc
                                                       (1/1)                  (1/1)

                 vtest
                                                                                                 M7 (4/1)
                              M1        M2
                             (4/1)      (4/1)           (1/1)                 (1/1)
                                                                                                       Gloop vtest
                                                                M3       M4


                R1                                                                                R2




                                                                             72
                          IJ&&0 (0) = −LM1,2 O40 6 ∥ 4R4 T                                 = −25.85
                                                                      72 + 1⁄LM7

                                     4Z[ = 4\ . + 4\ ] O1 + 4\ . LM]T = 46.75Ω

                                                3IJ&&0 (0)3         ≅ 28.3jk
                                                               hi




    4. Tracciare il diagramma asintotico del guadagno d’anello in frequenza e calcolare la
       frequenza di attraversamento dell’asse a 0db e il margine di fase
       Il guadagno d’anello ha 1 polo e nessuno zero dato che la funzione di trasferimento
       per l → ∞ tende a 0.
                                                                              1
                                        IJ&&0 (o) = IJ&&0 (0)
                                                                        (1 + op;1 )


                                                  p08 = %: q4\ . ∥ 4Z[ r = 97.9#o

                                                         ^08 = 1.62def


                     Il guadagno d’anello per ^08 ≤ ^ tende ad essere

                                                                     LM1,2          72
                                                3IJ&&0 (l)3 ≈
                                                                     l %v 72 + 1⁄LM7




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2018/2019

                                                   LM8,.     7.
                                           ^_ ≅                     = 42def
                                                   2a %b 7. + 1⁄LMc




                                             %&''" !




                                                                  !$


                                                   X
                                                   !"#



    5. Tracciare il diagramma asintotico del modulo del guadagno reale




                                   %&''" ! %)* !




                                                                       %)* !



                                              X
                                             !"#             !$
                                                                                 %+ !




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
          Complementi di Circuiti e sistemi
                  elettronici
                                          Anno accademico 2018/2019


Prova scritta di Elettronica Analogica
                                                   15 luglio 2019

Considerando il circuito riportato in figura

                               5V                                     1
                                                                        # % = 50#+/- .
                                                                      2 $ &'
          R1                                      R2            C1
                         M1      M2                                   1
                                                                        # % = 25#+/- .
                       (4/1)    (4/1)                           V2    2 / &'
 V1
                                                                      -0$ = 1-0/ 1 = 1-

                                                                      2& = 10 4Ω
                           2.5V
                 M3                        M4           R3            67 = 108Ω
                (8/1)                    (8/1)
         Iin                                      Cc                  6. = 18Ω
                                                        Vout
                                    VC                                69 = 108Ω

                                                                      %7 = 100:F
                  M5                     M6            M7
                                                                      %< = 10:F
               (4/1)                      (4/1)         (8/1)




      1. (Punti 6) Calcolare l’espressione del guadagno ideale di segnale tra Vout(s) e Iin(s).
      2. (Punti 6) Calcolare tutte le tensioni (V1, V2, Vc e Vout) e tutte le correnti di polarizzazione
         dello schema considerando Iin=10µA.
      3. (Punti 8) Calcolare il guadagno d’anello in continua.
      4. (Punti 7) Tracciare il diagramma asintotico del guadagno d’anello in frequenza e
         calcolare la frequenza di attraversamento dell’asse a 0db e il margine di fase.
      5. (Punti 6) Tracciare il diagramma asintotico del modulo del guadagno reale.




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                                  Anno accademico 2018/2019




                                                                Soluzioni
         !"#$ (&)      , J,            , ,
    1.            = −,- ., 0 L- + &3- , .J,0 O
          (() (&)         0            .    0
    2. V1= 5V-100mV = 4.9V = V2
       Considerando lo stadio differenziale circa in equilibrio avremo
       ID1= ID2=- ID3=- ID4
       Vgs1,2+| Vgs3,4 |=2.4V
       ID1= 8u A
       IR2= IR1 R1/ R2=100 u A
       Vo= V2 – IR2 R3 = 3.9V
                                          T
          5PQR = 50 + S W UV
                           1                              = 1.55
                                L O            D F
                                      X Y 2 E GH

         Vc= Vgs7=1.5V
                               PQ1,2,3,4
    3.   K_&&/ (0) = −                         eV0 6 ∥ VY4 i PQ7 \2 = −106
                                      2
                  1              PQn
         Vkl =       + Vm n o1 +     p ≅ 20eΩ
                 PQ.             PQ.
                                                 y                    y                    y
    4. gs ≅ 180° − tan−1 oy z p − tan−1 oy z p − tan−1 Ly z O = 88°
                                                  {|                  {V                   }|
              PQ7,.,9,n \.
         st ≅                = 57.8yz{
               4w FÅ \. + \9

    5.

               %&''" ! %)* !                                               %&''" !




                                  %)* !                                               !$

                                                                                           !"(
                                                                                X           X o
                                                                                !"#               !)#

                                              !", !-,    !-#
                      X                         Xo      o
                     !"#         !$


                                                               %+ !




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                       Anno accademico 2018/2019




                                            Svolgimento
    1. Calcolare l’espressione del guadagno ideale di segnale tra Vout(s) e Iin(s) .
       Lo schema è retroazionato negativemente con una struttura serie-parallelo, si trova
       che la tensione V2 ai capi della resistenza R2 viene eguagliata alla caduta sulla
       resistenza R1.
       Quindi il guadagno ideale sarà
             !"#$ (&)              ,. (&3- ,0 + -)            ,. + ,0               ,. ,0
                      = −,- o- +                     p = −,-            o- + &3-          p
                 (
              (() &)                       ,0                    ,0               ,. + ,0

    2. Calcolare tutte le tensioni (V1,V2,Vc e Vout) e tutte le correnti di polarizzazione dello
       schema considerando Iin=10µA.
       In ingresso ci sarà
       V1= 5V-100mV = 4.9V = V2
       Considerando lo stadio differenziale circa in equilibrio avremo
       ID1= ID2=- ID3=- ID4
       Inoltre possiamo calcolare
       Vgs1,2+| Vgs3,4 |=2.4V
       Mettendo sistema le precedenti equazioni otteniamo
       ID1= 8u A
       Considerando il resto dello schema
       IR2= IR1 R1/ R2=100 u A
       Quindi Vo= V2 – IR2 R3 = 3.9V ed infine
                                  T
          5PQR = 50 + S W UV
                           1                = 1.55
                            L O       D F
                              X Y 2 E GH

         Vc= Vgs7=1.5V

    3. Calcolare il guadagno d'anello in continua e la resistenza di uscita ad anello chiuso
       Considerando la polarizzazione abbiamo i seguenti valori di trasconduttanza
       trascurando l’effetto della modulazione di canale.
                  PQ7,.,9,n ≅ 80D|/5

                    PQR ≅ 400D|/5




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2018/2019

         Lo schema può essere tagliato in corrispondenza dell’ingresso invertente come
         riportato in figura.


                                              PQ1,2,3,4
                            K_&&/ (0) = −                 eV0 6 ∥ VY4 i PQ7 \2 = −106
                                                 2
                                             1              PQn
                                    Vkl =       + Vm n o1 +     p ≅ 20eΩ
                                            PQ.             PQ.

                                            1K_&&/ (0)1        ≅ 40.56•‚
                                                          ÖÜ




    4. Tracciare il diagramma asintotico del guadagno d’anello in frequenza e calcolare la
       frequenza di attraversamento dell’asse a 0db e il margine di fase
       Il guadagno d’anello ha 2 polo e 1 zero dato che la funzione di trasferimento per ƒ →
       ∞ tende a 0.
                                                                    (1 − †‡{1 )
                                 K_&&/ (†) = K_&&/ (0)
                                                               (1 + †‡ˆ1 )(1 + †‡ˆ2 )

         Le due capacità C1 e Cc sono indipendenti e interagenti

                                                ‡ˆ1 + ‡ˆ2 = FŠ \′ F + F1 \′ 1
                                              é                1         1
                                               ƒˆ1 + ƒˆ2 =          +
                                                            FŠ \ F F1 \′′ 1
                                                                 ′′



         Dove

                            \ë < ≅ eVm í ∥ Vkl i(1 + PQR (\. + \9 )) + (\. + \9 ) = 36eΩ

                                   \ëë < ≅ eVm í ∥ Vkl i(1 + PQR \9 ) + \9 = 9.3eΩ

         Che possono essere calcolate anche usando il teorema di Miller.

                                                     \ë7 ≅ \. = 1•Ω

                                          \ëë7 = \. ∥ (\9 + 1/ PQR) = 926Ω




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2018/2019


         Quindi i poli saranno
                                                       s/î = 442z{
                                                     s/ï = 1.72ez{

         Lo zero destro è una configurazione

                                                              PQR
                                                        †ñ7 =
                                                               FÅ
                                                      sñ7 = 6.3ez{


                   Il guadagno d’anello per s/7 ≤ s tende ad essere




                                                              PQ1,2,3,4    \2
                                            1K_&&/ (ƒ)1 ≈
                                                              2 ƒ FŠ \2 + \3

                                                  PQ7,.,9,n \.
                                           st ≅                  = 57.8yz{
                                                   4w FÅ \. + \9




                                             st          st          st
                         gs ≅ 180° − tan−1 ô ö − tan−1 ô ö − tan−1 o p = 88°
                                            s/7         s/.         sñ7




    5. Tracciare il diagramma asintotico del modulo del guadagno reale




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2018/2019

                                               %&''" !




                                                                    !$

                                                                         !"(
                                                    X                     X o
                                                    !"#                         !)#




         Questo è lo zero del guadagno ideale
                                                          sñ. = 1.75ez{

                                            %&''" ! %)* !




                                                                %)* !




                                                                          !", !-,      !-#
                                                    X                       Xo        o
                                                   !"#         !$

                                                                                             %+ !




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
            Complementi di Circuiti e sistemi
                    elettronici
                                           Anno accademico 2020/2021


Prova scritta di Elettronica Analogica
                                                      14 Giugno 2021


                                                                                          3.3V

                                          3.3V                             3.3V
                                                                                                       1
                                                                                                         ! " = 100!'/) )
                                                  40uA                             80uA                2 & '(
   3.3V                                                                                      Iout
                                             Va                                                        1
                                                                                                         ! " = 20!'/) )
                                  M1             M2                           Vd              (20/1)   2 * '(
           Iin                                                                                M6
                                 (20/1)          (20/1)                                                )+& = *)+* * = 0.6)
                                                                                                 Ve
          (4/1)                   Vb                      Vc    Cc
                                                                                                       -' = 1 /Ω
                                                                      M5          10X(4/1)
                           M3                             M4
                                                                                                       ),-./ = 0.74)
 M8                                                                                          M7
                        (10/1)                                                                         "0 = 2034
                                            (10/1)               (40/1)




      1. (Punti 3) Calcolare l’espressione del guadagno ideale di segnale tra Iout(s) e Iin(s) nello
         schema riportato in figura.
      2. (Punti 5) Calcolare tutte le tensioni (Va, Vb, Vc, Vd e Ve) e tutte le correnti di
         polarizzazione, considerando Iin=10µA.
      3. (Punti 7) Calcolare il guadagno d’anello in continua
                                                                                                 "
      4. (Punti 4) Considerando i parametri di “matching” per la tensione di soglia " ($! ) =
                                                                                                                             √$%
                                             !                 &(()          *
            e per il coefficiente ' = " !# "$%                  (
                                                                      =             pari a (( = 10+$ ∙ -+ e . = 10% ∙ -+),
                                                                           √$%
         valutare la varianza della corrente di uscita.
      5. (Punti 7) Calcolare l il guadagno d’anello in frequenza, tracciarne il diagramma
         asintotico e calcolare la frequenza di attraversamento dell’asse a 0db.
      6. (Punti 7) Calcolare l’impedenza di uscita nel terminale in cui è connesso il diodo




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                        Anno accademico 2020/2021


                                                   Soluzioni
         +!"# (,)
    1.    +$% (,)
                  = 10
    2. Va=1.57V, Vb=0.74V,Vb= Vc, Vd= 1.581V e Ve=0.758V.
       ID1,2,3,4=20µA, ID5=80µA, ID6,7=100µA e ID8=10µA
                                                               67 (4& ||4& )
    3. 0-../ (0) = −561,2 230 1 ∥ 30 2 5 565 30 3 67 676 (4' ||4( ) = −10.365 k
                                                                     6   &'   &(

                                                   :   2    &(() 2
    4. " 2 (;.89 ) = < =+2 " 2 ($! ) + !"#
                                       ;
                                           ? ( @
         =+ = 126µ C/$
         Quindi
                                                       " (;.89 ) = 2.14 µ C
                                       (1+9:"1 )
    5. 0-../ (F) = 0-../ (0) <
                                       1+9:$1 =
         f;< ≅ 13.9Hz
         f=< = 9.096 MHz
                                                                   gm<,)
                                                             ω> ≅
                                                                     C?
                                                           f> ≅ 1.4483MHz

                                   f>
         φ@ ≅ 180° − 90° − tan−1 D E = 81°
                                  f=<

    6. FAB+ (F) ≅ (3@6 + 3@7 )(1 − 0NOOP ∗ (F))
                                                                                   566 30 C 30 D
                  0NOOP ∗ (0) = −(1 + 561,2 230 1 ∥ 30 2 5 565 30 3 )                              = −46.33 /
                                                                                   30 C + 30 D
                                                              561,2 566 30 C 30 D
                          lim 0-../ ∗ (UI) ≅ −(1 −                 )              = 375.8
                          D→∞                                 565 30 C + 30 D




                 "$%& !
                             92TΩ




                                                   753 MΩ
                                  X
                                 !!"         !#




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021




                                       Svolgimento
    1. Calcolare l’espressione del guadagno ideale di segnale tra Iout(s) e Iin(s) nello
       schema.
       Lo schema ha una retroazione negativa che porta i transistori M8 e M7 a lavorare con la
       stessa Vds, avendo anche la stessa Vgs si può concludere che

                                                      VEFG (W)
                                                               = XY
                                                       VHI (W)

    2. Calcolare tutte le tensioni (Va, Vb, Vc, Vd e Ve) e tutte le correnti di polarizzazione
       considerando Iin=10µA.
       La Vgs8= Vgs7 =0.758V, e considerando l’effetto della retroazione avremo che Ve=0.758V.
       Considerando i transistori in saturazione, la corrente nei rami del primo stadio M1 e M2
       sarà di 20µA. Di conseguenza |Vgs1,2|= 0.82V con Va=1.57V, Vgs3,4= 0.74V con Vb=0.74V.
       Considerando M5 in saturazione la sua corrente sarà di 80µA e quindi la sua Vgs5= 0.74V
       e quindi Vb= Vc. IDM7 sarà uguale a 100µA avendo la stessa Vgs di M8 e Vgs6 sarà di =0.823V.
       Quindi Vd=Ve+0.823=1.581V.


    3. Calcolare il guadagno d'anello in continua
       Considerando la polarizzazione abbiamo i seguenti valori di trasconduttanza di segnale
       trascurando l’effetto della modulazione di canale.
                                   56<,) ≅ 182!'/)

                                   56G ≅ 1143!'/)

                                  56H ≅ 894.5!'/)

         Non scorrendo corrente nel ramo di Vtest lo schema può essere semplificato come in
         figura :
                                                                 566 (30 ||30 C )
                                                                          D
             0-../ (0) = −561,2 230 1 ∥ 30 2 5 565 30 3                                = −103.65 k
                                                              1 + 566 (30 D ||30 C )

                                           [0-../ (0)[JK = 100\]




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                       Anno accademico 2020/2021




                                                                                     Vd            (10/1)
                                              M1           M2
                                                                                                   M6
                                             (20/1)        (20/1)
                         Vtest
                                              Vb                    Vc    Cc                        Gloop Vtest

                                                                               M5         (40/1)
                                       M3                           M4
                                                                                                   M7
                                    (10/1)                          (10/1)          (40/1)




                                                                                                                   M
    4. Considerando i parametri di “matching” per la tensione di soglia ^ (_L ) =                                       e per
                                                                                                                  √NO
                                   I                  P(Q)            R
         il coefficiente ` = J KK LLM                  Q
                                                               =             pari a (a = XYb_ ∙ cb e d = e % ∙ cb),
                                                                    √NO
         valutare la varianza della corrente di uscita
                                                        T)*+ S       P(Q) S
         ^S (fEFG ) = g hbS ^S (_L ) +                     U
                                                                    ? Q @
         hb = Xijµ k/_
         Quindi
         ^ (fEFG ) = i. Xl µ k

    5. Calcolare il guadagno d’anello in frequenza e tracciarne il diagramma asintotico e
       calcolare la frequenza di attraversamento dell’asse a 0db.

         Il guadagno d’anello ha un polo e uno zero in entrambi i casi
                                                                               (1 + NON1 )
                                            0-../ (F) = 0-../ (0)
                                                                               21 + NOO1 5

         Il polo della capacità Cc sarà

                                 PP = Q30 4 ∥ 30 2 R 56G 30 5 + 30 5 = 572.5 nΩ

         Quindi il polo sarà alla frequenza

                                                                    S*< ≅ 13.9TU




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021


         Nel caso dello schema riconosciamo una configurazione che genera uno zero destro di
         pulsazione paria a U< .

                                                       U< = 56G /"PP

                                                       SQ< = 9.096 /TU

         Infatti, Considerando I → ∞, il nostro guadagno d’anello tenderà a
                                                                     561,2
                                            lim 0-../ (UI) ≅
                                           D→∞                       565



                                             "$%%! !




                                                                X            0
                                                               !!"      !#       !&"

                                          ∠ "$%%! !
                                                        180°


                                                                      90°




                                             SS
         XR ≅ 180° − 90° − p(q−1 D              E = 81°
                                            SQ<
                                                               56<,)
                                                         IS ≅
                                                                 "P
                                                       SS ≅ 1.4483/TU

    6. Calcolare la resistenza di uscita dello schema
       Trasformando il transistore che si trova su M6 nel suo equivalente thevenin creiamo
       uno schema con retroazione di tipo serie sull’uscita. Questa trasformazione non
       cambia il guadagno d’anello che rimane quello precedentemente valutato e permette
       una valutazione immediata dell’impedenza che viene moltiplicata dalla retroazione.

         FAB+ (F) ≅ (3@6 + 3@7 )(1 − 0NOOP ∗ (F))




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
              Complementi di Circuiti e sistemi
                      elettronici
                                                        Anno accademico 2020/2021


Prova scritta di Elettronica Analogica
                                                              27 Gennaio 2021

                                                                            1.65 V+ VIN
                                                                                          +          Vout        1
                                                                                                                   # $ = 100#'/) $
                                                                                           -                     2 ! "#
                  3.3 V                                                                        R2
                                                                                                                 1
              (2/1)        (2/1)                                                                                   # $ = 20#'/) $
                                                                                                                 2 % "#
        M3                          M4
                                                (2/1)              (16/1)                      C1
                                                                                                            CL   )&! = *)&% * = 0.6)
        Vb                                              M5         M8                     R1

               M1            M2
                                                                              1.65 V
                                                                                                                 -" = 1 /Ω
                                                                   Vout                        (a)
 Vin1        (10/1)        (10/1)        Vin2
                                                                            1.65 V+ VIN
                                                                                           -         Vout
                                                                                                                 $' = 101F
                      Va                                      Vc
                                                         M6        (16/1)
                                                                    M7
                                                                                           +                     $( = 10013
                                                (2/1)
                                                                                               R2
                             20uA
                                                                                                                 4' = 105Ω
                                                                                          R1 (b)                 4$ = 1005Ω
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
                                  ()' *' *&
         !!"# (#)   (%& &%' )('&        )
                                 *' +*&
    2.   !$% (#)
                  =     %' ('&#(' %& )
    3. Va=0.95, Vb=2.2V, Vc=0.82V e Vo = 1.65 V
                           )*1,2 8 ,-, - ∥-, . ∥(// &/0 )0//
    4. ")**+ (0) = −                   // &/0
                                                                = −13.11
                                        (1+/0$1 )
    5.   ")**+ (*) = ")**+ (0) ,1+/0 0,1+/0 0
                                          %1         %2



         6%' ≅ 17.68 5:;
         6%$ ≅ 1.93/:;
         61' = 160>:;




            "$%%! !




                                                                   !#
                                     X          0           X
                                    !!"        !'"        !!&

                             63          63          63
         ?2 ≅ 180° − ./0−1 @ A + ./0−1 B C − ./0−1 @ A = 114°
                            6%'         61'         6%$




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
                                                                     5' 58
                        3345 (4) 3345 (4) (58 + 5' ) (6 + 47' 5' + 58 )
                                 =          =
                         367 (4)    367 (4)       5'        (6 + 47' 58 )

    3. Calcolare tutte le tensioni (Va, Vb, Vc e Vo) e tutte le correnti di polarizzazione dello
       schema considerando Vin=0 A.
        Considerando i transistori in saturazione, la corrente nei rami del primo stadio è da
       10uA. Di conseguenza Vgs1,2= 0.7V con Va=0.95, |Vgs3|= 1.1V con Vb=2.2V ed essendo la
       corrente riflessa dallo specchio M4, M5 abbiamo Vgs6= Vc=0.82V. Nello stadio di uscita
       avremo Vo= 1.65V e la corrente dell’ultimo stadio M8 / M7 sarà di 80 uA.

    4. Calcolare il guadagno d'anello in continua
       Considerando la polarizzazione abbiamo i seguenti valori di trasconduttanza di segnale
       trascurando l’effetto della modulazione di canale.
                                   DE',$ ≅ 200#'/)


                                       DE1,2 8 899 : ∥ 99 ; ∥ (;< + ;= )<;<
                     ")**+ (0) = −                                               = −13.11
                                                       ;< +;=

                                          =")**+ (0)=>? = 22.35AB




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021

    5. Calcolare il guadagno d’anello in frequenza e tracciarne il diagramma asintotico e
       calcolare la frequenza di attraversamento dell’asse a 0db.
       Il guadagno d’anello ha 2 poli e 1 zeri


                                                                 (1 + GH61 )
                                ")**+ (*) = ")**+ (0)
                                                            81 + GH71 <81 + GH72 <

         Le capacità C1 e CL sono interagenti e si può usare il metodo delle costanti di tempo.

                                          H71 + H72 = $1 4′ 1 + $9 4′ 9
                                        C                1         1
                                         I71 + I72 =          +
                                                      $1 4 1 $9 4′′ 9
                                                           ′′


         Dove
                                    4:' = 4$ ||(4' + 90 7 ∥ 90 8 ) = 83.6>Ω


                                                   4::' = 4$ ||4' = 9>Ω

         e
                                    4: ( = (90 ∥ 90 8 )||(4' + 4$ ) = 90>Ω
                                               7


                                            4:: ( = (90 ∥ 90 8 )|| 4' = 9.8>Ω
                                                        7
         Quindi i poli saranno
                                                     6%' ≅ 17.68 5:;
                                                      6%$ ≅ 1.93/:;



         lo zero può essere calcolato considerando

                                                    H1' = $' 4$ = 1#G

                                                      61' = 160>:;


         Essendo

                                            *"CDDE M6%$ N* ≅ 6%' *"CDDE (0)*/61'




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021

         L’attraversamento dell’asse a 0db sarà a 20db per decade quindi avremo

                                           63 ≅ *"CDDE M6%$ N* 6%$ = 2.88/:;



            "$%%! !




                                                              !#
                                    X        0        X
                                   !!"     !'"      !!&

                                         63          63          63
                     ?2 ≅ 180° − ./0−1 @ A + ./0−1 B C − ./0−1 @ A = 114°
                                        6%'         61'         6%$

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

                                   )3;< ≅ (3.3) − 1. PQR) 4' /( 4' + 4$ ) = 150E)

                                    )3;= ≅ (−1. PQR) 4' /( 4' + 4$ ) = −150E)

         A causa del guadagno limitato dell’amplificatore |)>ℎ+,− | < 150E) .




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
             Complementi di Circuiti e sistemi
                     elettronici
                                                                     Anno accademico 2020/2021


Prova scritta di Elettronica Analogica
                                                                          22 settembre 2021

                                                                                                                                1
                                                                                                                                  # $ = 100#'/) $
                                                                                                                                2 ! "#
                   5V               5V                 5V
                                                                                                                                1
                           (50/1)                           (100/1)                                                               # $ = 20#'/) $
                                                        M9                                                                      2 % "#
                        40uA
                                                  Va
                                                             Vc                                                     R1
                                                                                                                                )&! = *)&% * = 0.6)
                                                                          (50/1)
                                                                                           5V
              M1                     M3
                                                        M5           M8         3.4V
                                                                                                M9
                                                                                                                    -
                                                                                                                         Vout
                                                                                                                                -" = 1 /Ω
          (10/1)                                        (10/1)             Ve
                          (10/1)                                                            (10/1)            R2    +
                        IN-                 IN+                                 C
                                                                                                     OUT
                                                                                                                                $ = 10012
                                                        M6           M7                                       Vin
                                      M4                                        1.6V
 2.5V         M2
                                     (50/1)
                                                       (50/1)
                                                                     Vd   (10/1)                                                3' = 5056
                               Vb                                                   40uA                   2.5V
          (50/1)
                                                                                                                                3$ = 1056
                        40uA                                M10

                                         (10/1)             (20/1)



Considerando il circuito di figura

        1. (Punti 4) Calcolare l’espressione del guadagno ideale di segnale tra Vin(s) e Vout(s).
        2. (Punti 7) Calcolare tutte le tensioni (Va, Vb, Vc, Vd, Ve e OUT) e tutte le correnti di
           polarizzazione, quando Vin è pari a 0.
        3. (Punti 8) Calcolare il guadagno d’anello in continua
        4. (Punti 7) Calcolare l il guadagno d’anello in frequenza, tracciarne il diagramma
           asintotico e calcolare la frequenza di attraversamento dell’asse a 0db.
        5. (Punti 7) Calcolare il guadagno reale tra Vin(s) e Vout(s).




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021




                                                 Soluzioni
         !!"#(#)
    1.   !$% (#)
                 = −#
    2. Considerando i transistori in saturazione, la corrente nei rami del primo stadio M1 e M2
       sarà di 40µA. Di conseguenza |Vgs1|= 0.8V, e anche |Vgs2|= 0.8V, con Va=3.3V e Vb=1.7V.
       Considerando M9 in saturazione la sua corrente sarà di 80µA con Vgs5= 0.8V. La tensione
       di uscita dell’amplificatore operazionale sarà di 2.5V e Ve=3.3V. Infine abbiamo
       Vc=4.4+|Vgs8|= 4.2V e Vd=1.6-|Vgs7|= 0.8V.
                                    (                +2      * (,& (,& ()+1)-,& )
    3. $%&&' (0) ≅ -                                                                = −6.6 k
                         (/()++1 +(/(* ())||+2 (/(* ())++2            2
                                        1
    4. $%&&' (,) = $%&&' (0) .1+12 /
                                            #1



    5.
            ""#! !
             "$% !          14db




                                   X
                                  !!
                                                          -45.7db




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021




                                       Svolgimento
    1. Calcolare l’espressione del guadagno ideale di segnale tra Vin(s) e Vout(s).
       Lo schema ha una retroazione negativa che farà eguagliare i due ingressi
       dell’amplificatore di tipo current- feedback. L’amplificazione complessiva sarà

                                                      -012 (.)
                                                               = −#
                                                      -34 (.)

    2. Calcolare tutte le tensioni (Va, Vb, Vc, Vd, Ve e OUT) e tutte le correnti di
       polarizzazione, quando Vin è pari a 0.
       Considerando i transistori in saturazione, la corrente nei rami del primo stadio M1 e M2
       sarà di 40µA. Di conseguenza |Vgs1|= 0.8V, e anche |Vgs2|= 0.8V, con Va=3.3V e Vb=1.7V.
       Considerando M9 in saturazione la sua corrente sarà di 80µA con Vgs5= 0.8V. La tensione
       di uscita dell’amplificatore operazionale sarà di 2.5V e Ve=3.3V. Infine abbiamo
       Vc=4.4+|Vgs8|= 4.2V e Vd=1.6-|Vgs7|= 0.8V.


    3. Calcolare il guadagno d'anello in continua
       Considerando la polarizzazione abbiamo i seguenti valori di trasconduttanza di segnale
       trascurando l’effetto della modulazione di canale. Per tutti i transistori vale:
                                    9: ≅ 400#'/)

         Aprendo l’anello sul gate di M9 abbiamo:
         Non scorrendo corrente nel ramo di Vtest lo schema può essere semplificato come in
         figura :
                               1                   32      2 (25 (25 9: + 1) + 25 )
    $%&&' (0) ≅ -                                                                   = −6.6 k
                    1/9: + 31 + 1/(2 9:)||32 1/(2 9:) + 32             2

                                            4$%&&' (0)467 = 7667




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                      Anno accademico 2020/2021

            (50/1)                          (100/1)
                                        M9


                                Va


                                                   M8
                      M3                                                           M9
                                                               Gloop Vtest
           (10/1)                                                                 (10/1)
                                                           C                               R1

                                                  M7
                      M4
                     (50/1)                 (50/1)
                                                                                                R2
              Vb


                                            M10

                       (10/1)           (20/1)


    4. Calcolare il guadagno d’anello in frequenza e tracciarne il diagramma asintotico e
       calcolare la frequenza di attraversamento dell’asse a 0db.

         Il guadagno d’anello ha un polo e uno zero in entrambi i casi
                                                                             1
                                       $%&&' (,) = $%&&' (0)
                                                                   81 + ?@31 9

         Il polo della capacità C sarà
                                            (20 (20 9: + 1) + 20 )
                                     34 =                          = 201 :Ω
                                                      2
         Quindi il polo sarà alla frequenza

                                                          B%' ≅ 7.9EF


                                                  B5 ≅ B%' $9::; (0) = 52.6kEF




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021


             "$%%! !




                                      X
                                     !!"           !#


    5.   Calcolare il guadagno reale tra Vin(s) e Vout(s).
         Considerando la relazione del guadagno reale
                              <:<= (,)     $>@ (,)         $@>A (,)
                                       =               +
                              <>? (,) H1 − $9::; (,) J K1 − $9::; (,)L
                                                    6'



         In questo caso abbiamo

                                                  $B6 (,) = -5
         e


                                      1/(2 9:)||(32 + 1/ 9:)       1/ 9:
                       $6B, (,) ≅                                            = 0.0052
                                    1/(2 9:)||(32 + 1/ 9:) + 31 (32 + 1/ 9:)

         Considerando i valori precedentemente calcolati di $%&&' (,) abbiamo
                                    ""#! !
                                     "$% !          14db




                                                           X
                                                          !!
                                                                                 -45.7db




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
            Complementi di Circuiti e sistemi
                    elettronici
                                        Anno accademico 2018/2019


Prova scritta di Elettronica Analogica
                                               26 febbraio 2019

Considerando il circuito riportato in figura
                                                                                            1
                                                                                              # % = 100#*/, -
                                             3.3V                                           2 $ &'

                                 M2     M3                                                  1
                                                                                              # % = 25#*/, -
                                                           Cc                               2 / &'
                       (16/1)                  (16/1)
                                                                                            ,1$ = 2,1/ 2 = 0.5,
                                                                        M4
                        Va                           Vc                 (4/1)      25µA     4& = 2 5Ω
                       M1
                                (1/1)                     R2            vout                78 = 109Ω
                1.5V
                                Vb                   M6                                     7- = 1009Ω
                                                                M5              M7
       R1
                                             (4/1)              (4/1)           (4/1)
                                                                                            %: = 100;F
                    25µA
0.5V+vin




    1. (Punti 8) Calcolare tutte le tensioni (Va,Vb,Vc e Vout), tutte le correnti di polarizzazione
       dello schema e lo stato di polarizzazione dei transistori.
    2. (Punti 4) Calcolare l’espressione del guadagno ideale di segnale tra vout(s) e vin(s) .
    3. (Punti 8) Calcolare il guadagno d’anello in frequenza e la frequenza di attraversamento
       dell’asse a 0db.
    4. (Punti 6) Tracciare il diagramma asintotico del modulo del guadagno reale.
    5. (Punti 4) Considerando di connettere al nodo Vout una capacità CL connessa a massa,
       calcolare il massimo valore di CL che garantisca un margine di fase superiore a 80°.




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                       Anno accademico 2018/2019


                                                  Soluzioni
    1.
         Vgs1=1V
         IR1=0
         Vb=0.5V
         Va=2.55V
         ID2= ID3=-25uA
         Vout=0.5V
         Vc= Vout +Vgs4=0.5V+0.75V =1.25V
    2.

         =&>? (A)    78
                  =−
         =C$ (A)     7-

                                       GH ∥ GH                        GH T ∥GH N            QS
         EF&&/ (0) = − (8⁄LM PQ PQI ∥8⁄LM
                                       K
                                          )∥G
                                                                                                       = −4.52
                               N   R     S        S   H T ∥GH N QR PQS ∥8⁄LMS P GH T ∥GH N QS P8⁄LMS

                                         1
         EF&&/ (A) = EF&&/ (0) (1+AW )
                                             ;1


         W/8 = X4Y Z ∥ 4Y [ \%]


                E`aa; (0)
         ^? ≅             = 7.279de
                 2b W/8


    3.   Ef (A) = −EF&&/ (A) ECg (A)

                                  1⁄hi4                        1⁄hi1
         EgCG ≅                                                                = 0.0249
                   71 + X72 + 1⁄hi4 \ ∥ 1⁄hi1 72 + 1⁄hi4




                                                          |Emn |^?
                                                  ^k8 ≅              = 35de
                                                           Enm4




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2018/2019

                                     &'((" ! &*+ !




                                                              &*+ !

                                                                   &, !
                                                                          !$#
                                                X        X            o
                                          !"#            !%                     &+*, !




                                           1
    4. EF&&/ (A) = EF&&/ (0)
                                   (1+AW;1 )(1+AW;2 )
         W/8 = X4Y Z ∥ 4Y [ \%]
         W/- ≅ X(7- + 78 ∥ 1⁄hi8 ) ∥ 1⁄hip \%q

                                                      ^?          ^?
                                  rM = 180° − tan−1 x y − tan−1 x y > 80°
                                                     ^/8         ^/-

                                                              ^?
                                                ^/- >                     ≅ 17.79de
                                                        tan (42°)


                                1
         %q <                                      = 1.9|}
                2bX(7- + 78 ∥ 1⁄hi8 ) ∥ 1⁄hip \^/-




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2018/2019


                                         Svolgimento
    1. Calcolare tutte le tensioni (Va,Vb,Vc e Vout), tutte le correnti di polarizzazione dello
       schema e lo stato di polarizzazione dei transistori.
       Lo schema è retroazionato negativamente, il nodo Vc è in equilibrio se la corrente di
       M1 è pari a 25uA.
       Di conseguenza la corrente ID2= ID3=-25uA e, trascurando l’effetto di modulazione del
       canale possiamo calcolare:
       Vgs1=1V
       IR1=0
       Vb=0.5V
       Va=2.55V
       ID2= ID3=-25uA
       Vout=0.5V
       Vc= Vout +Vgs4=0.5V+0.75V =1.25V


    2. Calcolare l’espressione del guadagno ideale di segnale tra vout(s) e vin(s)
       Lo schema è retroazionato negativamente, considerando l’amplificatore avere un
       guadagno molto alto a tutte le frequenze la funzione di trasferimento vout(s) e vin(s)
       tende ad essere come la seguente.
                                           =&>? (A)     78
                                                    =−
                                            =C$ (A)     7-
    3. Calcolare il guadagno d'anello in frequenza e la frequenza di attraversamento
       dell'asse a 0db.
       Considerando la polarizzazione abbiamo i seguenti valori di trasconduttanza
       (trascurando l’effetto della modulazione di canale).
                    hi8 ≅ 100#*/,

                    hip ≅ 200#*/,

         Lo schema può essere tagliato in corrispondenza della corrente generata da M1
         trascurando l’effetto della resistenza ro1. In alternativa, se si volesse tener conto anche
         della resistenza ro1 , si potrebbe interrompere l’anello in corrispondenza della tensione
         di gate di M4 dopo la capacità Cc.
                                     GH I ∥ GH K                    GH T ∥GH N           QS
         EF&&/ (0) = − (8⁄                                                                         = −4.52
                            LMN PQR PQS ∥8⁄LMS )∥GH T ∥GH N QR PQS ∥8⁄LMS P GH T ∥GH N QS P8⁄LMS




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2018/2019


                                                         M2      M3
                                                                                     Cc
                                             (16/1)                       (16/1)

                                                                                          M4
                                          ITEST
                                                                                          (4/1)

                                       GLOOPITEST          M1                       R2



                                                                              ro6         ro5

                                           R1




         Che potrebbe anche essere semplificata come
                                                   40 3 ∥ 40 6                 71
                   EF&&/ (0) ≅ −
                                  X1⁄hi4 + 72 + 71 ∥ 1⁄hi1 \ ∥ 40 5 ∥ 40 4 71 + 1⁄hi1



                                            2EF&&/ (0)2              ≅ 13.2 n€
                                                                g•




                                          %&''" !




                                                                     !$


                                                  X
                                                  !"#




                                                        E`aa; (0)
                                            ^? ≅                  = 7.279de
                                                         2b W/8




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2018/2019

    4. Tracciare il diagramma asintotico del modulo del guadagno reale
       Lo schema ha un guadagno diretto che diventa dominante per • → ∞.
                          1⁄hi4               1⁄hi1
       EgCG ≅                                         = 0.0249
              71 + X72 + 1⁄hi4 \ ∥ 1⁄hi1 72 + 1⁄hi4



         Quindi avremo uno zero destro sul guadagno ideale circa


                                                    |Emn (0)|^?
                                           ^k8 ≅                     = 35de
                                                         Enm4




                                         &'((" ! &*+ !




                                                                     &*+ !

                                                                       &, !
                                                                                 !$#
                                                    X           X            o
                                              !"#               !%                         &+*, !




         Per l’esattezza, considerando che il guadagno d’anello è piuttosto basso, il valore di
         guadagno reale in continua risulta essere.

                                                              −10
                                       EGÑfF (0) =                      = −8.18
                                                         1 − E`aa;(0)Ö8


    5. Considerando di connettere al nodo Vout una capacità CL connessa a massa,
       calcolare il massimo valore di CL che garantisca un margine di fase superiore a 60°.
       Con l’inserimento della capacità di uscita il guadagno d’anello sarà
                                                                                       1
                                      EF&&/ (A) = EF&&/ (0)
                                                                     (1 + AW;1 )(1 + AW;2 )
         W/8 = X4Y Z ∥ 4Y [ \%]
         W/- ≅ X(7- + 78 ∥ 1⁄hi8 ) ∥ 1⁄hip \%q




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2018/2019


         Considerando che il margine di fase richiesto è superiore a 45° il secondo polo cadrà a
         frequenza superiore rispetto alla frequenza dell’attraversamento.

                                                      ^?          ^?
                                  rM = 180° − tan−1 x y − tan−1 x y > 80°
                                                     ^/8         ^/-

                                                          ^?
                                              ^/- >               ≅ 17.79de
                                                      tan (42°)


                                1
         %q <                                      = 1.9|}
                2bX(7- + 78 ∥ 1⁄hi8 ) ∥ 1⁄hip \^/-




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
                  Complementi di Circuiti e sistemi
                          elettronici
                                                                       Anno accademico 2020/2021


Prova scritta di Elettronica Analogica
                                                                              22 Febbraio 2021


                     3.3V                             3.3V                                                 3.3V                           3.3V
                                                                                                                                                                             1
                                                                                                                                                                               # $ = 100#'/) $
                             40uA                             80uA                                                 40uA                           80uA                       2 ! "#
                                                                       3.3V                                                                                3.3V
                        Va                                                                                    Va
                                                                                                                                                                             1
                                                                         (10/1)                                                                              (10/1)            # $ = 20#'/) $
                                                                                                                                                                             2 % "#
             M1             M2          Vin+1.65V        Vd                                        M1             M2         Vin+1.65V       Vd
                                                                         M6                                                                                  M6
            (20/1)          (20/1)                                                                (20/1)          (20/1)

             Vb                        Vc   Cc                                    Vout
                                                                                                   Vb                      Vc   Cc                                    Vout   )&! = *)&% * = 0.6)
                                                 M5           (40/1)                                                                 M5           (40/1)
     M3                                M4                                                  M3                              M4                                                -" = 1 /Ω
                                                         VBias           M7                                                                                  M7
   (10/1)                            (10/1)             (40/1)                           (10/1)                            (10/1)           (40/1)                           )'()* = 0.74)

                                                                                                                                                                             $+ = 2034
                                 (a)                                                                                   (b)


     1. (Punti 3) Calcolare l’espressione del guadagno ideale di segnale tra vout(s) e vin(s) dello
        schema (a) e dello schema (b).
     2. (Punti 4) Calcolare tutte le tensioni (Va, Vb, Vc, Vd e Vout) e tutte le correnti di
        polarizzazione dello schema (a) e (b) considerando Vin=0 V.
     3. (Punti 7) Calcolare il guadagno d’anello in continua per i due schemi
     4. (Punti 10) Calcolare il guadagno d’anello in frequenza, tracciarne il diagramma
        asintotico, calcolare la frequenza di attraversamento dell’asse a 0db e valutarne il
        margine di fase per lo schema di figura (a) e per lo schema di figura (b).
     5. (Punti 3) Tracciare il diagramma del guadagno reale in frequenza per i due schemi.
     6. (Punti 6) Tracciare la risposta di Vout nel tempo ad un gradino di tensione in ingresso
        ampio 500mV per lo schema di figura (a) e (b).




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                       Anno accademico 2020/2021




                                                    Soluzioni
         !!"# (#)
    1.   !$% (#)
                  ="
    2. Va=2.47V, Vb=0.74V,Vb= Vc, Vo=1.65V e Vgs8= 0.88V quindi Vd= 2.53V in entrambe gli
       schemi.
                                                                 126 (-& ||-& ( )
    3. #%&&'( (0) = −561,2 ()) * ∥ )) + + 565 )) , /0 12 (-' ||- ) = −10.365 k
                                                                        6   &'       &(

               #%&&'1 (0) = −561,2 ()) *
                                                              566 ()) 2 ||)) 3 )                                           1
                                     ∥ )) + + 3 565 )) ,                                         + 567 ()) 2 ||)) 3 ||           )6
                                                           1 + 566 ()) 2 ||)) 3 )                                          566
                                     = −103.83 k

                                      (1+67"1 )
    4.   #%&&' (8) = #%&&' (0) 4
                                      1+67$1 5

                                                                      "$%%! !



         7%8 ≅ 13.9;<
         798 = 9.096 /;<
                                                                                            X               0
                                                                                           !!"         !#       !&"

                                                                  ∠ "$%%! !
                                                                                 180°

                                                                                                                Caso (b)
                                                                                                     90°

                                                                                                                Caso (a)
                                    7<
         =:; ≅ 180° − 90° − <=>−1 > ? = 81°
                                   798
                                    7<
         =:' ≅ 180° − 90° + <=>−1 > ? = 98°
                                   798


                 "%&&! !     "'( !
                                                                  Vin         SR
                                                      2.15V
                                                                                   VoutB

                                                                        VoutA
                                                      1.65V
                        X                 0
                       !!"       !#           !$"
                                                                 t0
                                                                                                 t




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021


                                       Svolgimento
    1. Calcolare l’espressione del guadagno ideale di segnale tra vout(s) e vin(s) dello
       schema di figura (a) e (b)
       Lo schema è retroazionato negativamente, considerando l’amplificatore avere un
       guadagno molto alto a tutte le frequenze la funzione di trasferimento Vout(s) e Vin(s)
       tende ad essere come la seguente nei due casi:
                                      ?89: (@) ?89: (@)
                                               =         ="
                                       ?;< (@)   ?;< (@)


    2. Calcolare tutte le tensioni (Va, Vb, Vc, Vd e Vout) e tutte le correnti di polarizzazione
       dello schema (a) e (b) considerando Vin=0 V.

         Considerando i transistori in saturazione, la corrente nei rami del primo stadio sarà di
         20µA. Di conseguenza |Vgs1,2|= 0.82V con Va=2.47V, Vgs3,4= 0.74V con Vb=0.74V.
         Considerando M5 in saturazione la sua corrente sarà di 80µA e quindi la sua Vgs5= 0.74V
         e quindi Vb= Vc. Il transistore M7 ha la stessa di polarizzazione nei due schemi e quindi
         IDM7=80µA in entrambe i casi. Infine, Vo=1.65V e Vgs8= 0.88V quindi Vd= 2.53V in
         entrambe gli schemi.

    3. Calcolare il guadagno d'anello in continua
       Considerando la polarizzazione abbiamo i seguenti valori di trasconduttanza di segnale
       trascurando l’effetto della modulazione di canale.
                                   568,$ ≅ 182#'/)

                                  56=,> ≅ 1143#'/)

                                  56? ≅ 571.5#'/)

         Per lo schema di figura (a):
                                                                  566 ()) ||)) 3 )
                                                                          2
            #%&&'( (0) = −561,2 ()) * ∥ )) + + 565 )) ,                                 = −103.65 k
                                                               1 + 566 ()) 2 ||)) 3 )

                                          A#%&&'( (0)A        = 100BC
                                                         =1

         Per lo schema di figura (b)




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
              Complementi di Circuiti e sistemi
                      elettronici
                                                      Anno accademico 2020/2021

                                                                                      566 ()) 2 ||)) 3 )                                                1
        #%&&'1 (0) = −561,2 ()) * ∥ )) + + 3 565 )) ,                                                             + 567 ()) 2 ||)) 3 ||                       )6
                                                                                    1 + 566 ()) 2 ||)) 3 )                                              566
                                = −103.83 k

                                                               A#%&&'1 (0)A=1 = 100BC

             La differenza del guadagno in continua dei due schemi è praticamente trascurabile.



                                                                     (10/1)                                                               Vd                (10/1)
                     M1      M2                        Vd                                                M1      M2
                                                                     M6                                                                                     M6
                    (20/1)   (20/1)                                                                     (20/1)   (20/1)
Vtest                                                                                 Vtest
                     Vb               Vc   Cc                         Gloop Vtest                        Vb               Vc   Cc                             Gloop Vtest
                                                            (40/1)                                                                  M5         (40/1)
                                                 M5
             M3                       M4                                                         M3                       M4
                                                                     M7                                                                                  M7
           (10/1)                     (10/1)          (40/1)                                   (10/1)                     (10/1)         (40/1)




        4. Calcolare il guadagno d’anello in frequenza e tracciarne il diagramma asintotico e
           calcolare la frequenza di attraversamento dell’asse a 0db.

              Il guadagno d’anello ha un polo e uno zero in entrambi i casi
                                                                                              (1 + CD@1 )
                                                       #%&&' (8) = #%&&' (0)
                                                                                              (1 + CDA1 +

             Il polo della capacità Cc non dipende dalla configurazione perché non cambia la
             resistenza vista a suoi capi

                                               EB = F)0 4 ∥ )0 2 G 56= )0 5 + )0 5 = 572.5 FΩ

             Quindi il polo sarà alla frequenza

                                                                              7%8 ≅ 13.9;<

              Per quanto riguarda lo zero le due configurazioni hanno molte differenze.
              Nel caso dello schema di figura (a) riconosciamo una configurazione che genera uno zero destro
              di pulsazione paria a <8 .

                                                                              <8 = 56= /$BB




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021

                                                       798 = 9.096 /;<

         Infatti, Considerando H → ∞, il nostro guadagno d’anello tenderà a
                                                                    561,2
                                           lim #%&&'( (KH) ≅
                                           C→∞                      565

         Nel caso dello schema di figura (b) la configurazione notevole non genera lo stesso zero per il
         guadagno d’anello perché ci sono due percorsi di segnali che da KB raggiungono l’uscita e la loro
         combinazione determinerà il comportamento ad alta frequenza.
         Considerando H → ∞, il nostro guadagno d’anello non è nullo anche nel caso (b), per
         l’esattezza


                                         561,2  566 ()) 2 ||)) 3 )   567     561,2
                  lim #%&&'1 (KH) ≅          3                     −     6≅−
                 C→∞                      565 1 + 566 ()) ||)) 3 )   566     565
                                                           2

         In entrambe i casi abbiamo quindi uno zero alla frequenza 798 ma con contributo di fase
         opposto. Pe entrambe gli schemi abbiamo circa

                                                               568,$
                                                         H< ≅
                                                                 $B
                                                       7< ≅ 1.4483/;<


                                             "$%%! !




                                                               X            0
                                                              !!"     !#        !&"

                                           ∠ "$%%! !
                                                       180°

                                                                                Caso (b)
                                                                    90°

                                                                                Caso (a)




                                    7<
         =:; ≅ 180° − 90° − <=>−1 > ? = 81°
                                   798
                                    7<
         =:' ≅ 180° − 90° + <=>−1 > ? = 98°
                                   798




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021

    5. Tracciare il digramma asintotico di bode del guadagno reale.

         Il circuito di figura non ha un trasferimento diretto




                                          "%&&! !        "'( !




                                                 X                      0
                                                !!"            !#           !$"



    6. Tracciare la risposta di Vout nel tempo ad un gradino di tensione in ingresso ampio
       500mV
       Gli schemi (a) e (b) hanno lo stesso slew-rate perché in caso di saturazione del primo
       stadio abbiamo approssimativamente la stessa dinamica del nodo “d”.

                                              LE = 40#'/$B = 2/) /CMN

         Il guadagno reale precedentemente calcolato presenta un polo alla frequenza 7< e uno
         zero positivo o negativo alla frequenza 798 rispettivamente per il caso (a) e per il caso (b).
         Il modulo del guadagno ad alta frequenza sarà


                                                            561,2
                                        lim |#- (KH)| ≅             = 0.16
                                       C→∞                  565

         Se non ci fossero limitazioni di slew-rate per OFG la derivata della tensione di uscita sarebbe

                                          500N (1 + 0.16)
                              L&BĊ E ≅           $H
                                                                 = 5.278FL/8PQ
                                                 561,2




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021

                                          500N (1 − 0.16)
                              L&BĊ F ≅           $H
                                                                     = 3.822FL/8PQ
                                                 561,2

Quindi durante il transitorio la pendenza iniziale sarà limitata dallo slew rate




                                                      Vin       SR
                                       2.15V
                                                                     VoutB

                                                            VoutA
                                       1.65V


                                                    t0
                                                                             t




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
              Complementi di Circuiti e sistemi
                      elettronici
                                     Anno accademico 2019/2020


Prova scritta di Elettronica Analogica
                                              17 Febbraio 2020

Considerando il circuito riportato in figura
                                                                                                                      1
                                                             5V                              12V        12V             # $ = 60#(/* $
                                                                                                                      2 ! "#
                                               60uA                                120uA                      120uA   1
                                                                                                                        # $ = 30#(/* $
                                                                  Va
                                                                                                                      2 % "#

                                                   M1              M2                              Vd                 *&! = ,*&% , = 1*
                                       Vin1                                     Vin2
  C1          R2                                  (4/1)            (4/1)                                      Vo
                                                                                                                      -" = 1 /Ω
                        +   Vo                                                     Cc
                                                   Vb                      Vc                             M6
                        -                                                                                             1' = 503Ω
       Iout                                                                             M5                (4/1)
                                                        M3        M4
 Vin          R1
                                          (1/1)                            (1/1)               (4/1)                  1$ = 503Ω

                                                                                                                      $( = 1004F

                                                                                                                      $' = 16F
                   a)                                                   b)




        1. (Punti 6) Calcolare l’espressione del guadagno ideale di segnale tra iout(s) e vin(s) nello
           schema (a) di figura
        2. (Punti 2) Considerando l’amplificatore operazionale realizzato con lo schema di figura
           (b) definire quali tra Vin1 e Vin2 corrispondono agli ingressi V+ e V-.
        3. (Punti 4) Calcolare tutte le tensioni (Vin1, Vin2, Vb, Vc, Vd e Vo) e tutte le correnti di
           polarizzazione dello schema considerando Vin=2.5V.
        4. (Punti 10) Calcolare il guadagno d’anello in continua.
        5. (Punti 8) Calcolare il guadagno d’anello in frequenza, tracciarne il diagramma
           asintotico e calcolare la frequenza di attraversamento dell’asse a 0db.
        6. (Punti 2) Valutare il margine di fase del guadagno d’anello
        7. (Punti 3) Tracciare il diagramma asintotico di bode del guadagno reale.




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2019/2020


                                            Soluzioni
         !!"# (#)  #& '
    1.            = '& '
         %$% (#)      &
    2. Vin2 corrisponde all’ingresso non invertente V+ dell’amplificatore e Vin1 all’ingresso
       invertente.
    3. Va= 4V
       Vb= 1.7V
       Vc= Vgs5=1.7V
       Vo = 5 V
       Vd=3.24 V

                                                                    1(
    4. "())* (0) = −'(+,- *+. / ∥ +. - - '(0 +. 0                                  = 9.7K
                                                           1( 21) 2+⁄34*
    5.
                                                                    (1 + 9:)1 )
                                 "())* (2) = "())* (0)
                                                           (1 + 9:+1 )(1 + 9:+2 )

                                                         <%' = 9.1?@
                                                        <%$ = 31.43?@

                                                     <-' = 545.93?@


                                          <. ≅ C,"6778 D<%$ E, <%$ = 52.6F?@
                                    0               0                    0
    6. G/ ≅ 180° − tan−1 H0 ! I − tan−1 H0 ! I − tan−1 J0 ! K = 25.3°
                                    "#               "$                     %#



                                                               !"            !#$
                                            X              X                 o


                                                                    %*+ !             %, !

                                                                                                   -.6




                                                                                   %&''( ! %*+ !




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2019/2020




                                       Svolgimento
    1. Calcolare l’espressione del guadagno ideale di segnale tra iout(s) e vin(s) nello schema
       (a) di figura
       Lo schema è retroazionato negativamente, considerando l’amplificatore avere un
       guadagno molto alto a tutte le frequenze la funzione di trasferimento Iout(s) e vin(s)
       tende ad essere come la seguente.
                                             =;<= (>) >@? A@
                                                     =
                                             ?!> (>)     A?
    2. Considerando l’amplificatore operazionale realizzato con lo schema di figura (b)
       definire quali tra Vin1 e Vin2 corrispondono agli ingressi V+ e V-.
        Vin2 corrisponde all’ingresso non invertente V+ dell’amplificatore e Vin1 all’ingresso
       invertente.
    3. Calcolare tutte le tensioni (Vin1, Vin2, Vb, Vc e Vout) e tutte le correnti di
       polarizzazione dello schema considerando Vin=2.5V.
       Lo schema è retroazionato negativamente, quindi si può calcolare le condizioni di
       polarizzazione considerando V-= 2.5V.
       Di conseguenza la corrente ID1= ID2=30uA
       Vgs1,2= 1.5V quindi
       Va= 1.5V + 2.5V= 4V
       Vb=Vgs3,4= 1.7V
       Mentre
       Vc= Vgs5=1.7V
       Considerando che Vo = 2 Vin
       Ir1,2 = 50 uA, quindi
       Vo = 5 V e che Vgs6= 1.76 V
       Vd=3.24 V
    4. Calcolare il guadagno d'anello in continua
       Considerando la polarizzazione abbiamo i seguenti valori di trasconduttanza di segnale
       trascurando l’effetto della modulazione di canale.




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2019/2020

                                   MN',$ ≅ 120#(/*

                                   MN6 ≅ 343#(/*

                                   MN8 ≅ 184#(/*



                                                                         B+
                 "())* (0) = −'(+,- *+. / ∥ +. - - '(0 +. 0                       = 9.7K
                                                                  B+ + B- + 1⁄'(A

                                           E"())* (0)EBC = 79.7 FG

    5. Calcolare il guadagno d’anello in frequenza e tracciarne il diagramma asintotico e
       calcolare la frequenza di attraversamento dell’asse a 0db.
       Il guadagno d’anello ha 2 poli e 1 zero


                                                                 (1 + 9:)1 )
                                 "())* (2) = "())* (0)
                                                           (1 + 9:+1 )(1 + 9:+2 )

         Le due costanti di tempo possono essere espresse come

         Dove
                                                       :%' = $( 1123

                                  1123 ≅ D-4 $ ∥ -4 5 ED1 + MN6 -4 6 E + -4 6 = 173/Ω



                                             :%$ = $' (1⁄'(6 ∥ (1' + 1$ ))

         Dove

                                                       <%' = 9.1?@
                                                      <%$ = 31.43?@


         Gli zeri possono essere calcolati considerando
                                                  :-' = $( ⁄'(5




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2019/2020
                                                                  '(5
                                                          9-' =
                                                                  $(
         Quindi
                                                       <-' = 545.93?@

         Essendo

                                                      <%' "6778 (0) > <%$

         L’attraversamento dell’asse a 0db sarà a 40db per decade quindi avremo

                                             <%' "6778 (0) = <%$ ,"6778 D<%$ E,

                                                      ,"6778 D<%$ E, = 2.81

         Considerando l’attraversamento a 40db/dec


                                          <. ≅ C,"6778 D<%$ E, <%$ = 52.6F?@




                                            %&''" !




                                                                              !)#
                                                 X                       X    o
                                                !"#                !"(
                                                                         !$




    6. Valutare il margine di fase del guadagno d’anello e tracciare il digramma asintotico di
       bode del guadagno reale.
                                          <.          <.          <.
                      G/ ≅ 180° − tan−1 R S − tan−1 R S − tan−1 H I = 25.3°
                                         <%'         <%$         <-'




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2019/2020


    Il circuito ha anche un guadagno diretto che vale
                                                             1
                                  "BFG (2) = −
                                                 1⁄2I+ + (1⁄'(A ∥ (11 + 12 ))

    Per frequenze J > <9

                                                 "BFG (2) ≅ −'(A

                                                       !"             !#$
                              X                    X                  o


                                                             %*+ !              %, !

                                                                                                -.6




                                                                            %&''( ! %*+ !




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
            Complementi di Circuiti e sistemi
                    elettronici
                                          Anno accademico 2020/2021


Prova scritta di Elettronica Analogica
                                                         26 luglio 2021

                                                                                                        1
                                                                                                          # $ = 100#'/) $
                                                                                    3.3V                2 ! "#
                                                                                                        1
                                             3.3V                           3.3V            Ib            # $ = 20#'/) $
                                                                   80uA                                 2 % "#
               +
 Vout
           A           R
                                                     40uA                                               )&! = *)&% * = 0.6)
                                                Va
               -
                                     M1                                        Vd      (80/1)           -" = 1 /Ω
                                                    M2
                                                                                       M6
                                    (10/1)          (10/1)                                              1' = 102Ω
                                                                                      Ve
                                     Vb                      Vc   Cc
                                                                                           IRM          ' = 10
               1.65V                                                   M5                        RM
                              M3                             M4                             RM          $( = 2034
                                                                                                  Vin
                           (10/1)
                                               (10/1)              (40/1)                               1 = 502Ω



Il circuito in figura rappresenta una possibile realizzazione di un preamplificatore connesso al
sensore magnetico della testina di un hard disk. RM rappresenta il sensore magneto-resistivo
che cambia la resistenza in base alla campo presente in prossimità della testina.

        1. (Punti 4) Calcolare l’espressione del guadagno ideale di segnale tra Ib(s) e IRM(s) nello
           schema riportato in figura.
        2. (Punti 7) Calcolare tutte le tensioni (Va, Vb, Vc, Vd e Ve) e tutte le correnti di
           polarizzazione, considerando Ib=100µA.
        3. (Punti 8) Calcolare il guadagno d’anello in continua
        4. (Punti 7) Calcolare l il guadagno d’anello in frequenza, tracciarne il diagramma
           asintotico e calcolare la frequenza di attraversamento dell’asse a 0db.
        5. (Punti 7) Considerando una variazione di resistenza Δ"! pari al 10% valutare il segnale
           equivalente Vin riportato nello schema e valutare la funzione di trasferimento in
           frequenza Vout(s) e Vin (s)




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021


                                               Soluzioni
         "!" ($)
    1.    "# ($)
                 =1
    2. Va=1.57V, Vb=0.74V,Vb= Vc, Vd= 1.581V e Ve=0.758V.
       ID1,2,3,4=20µA, ID5=80µA, ID6,7=100µA e ID8=10µA
                                                            ./ (-$ ||-$ )
    3. %&''( (0) = −671,2 *+) * ∥ +) + - 675 +) , /0 ./6 (-% ||-& ) = −10.365 k
                                                                6   $%   $&
                                   (1+12"1 )
    4. %&''( (4) = %&''( (0) 11+12 2
                                        $1
         f34 ≅ 13.9Hz
         f54 = 9.096 MHz
                                                             gm4,$
                                                        ω6 ≅
                                                               C7
                                                     f6 ≅ 1.4483MHz

                                   f6
         φ8 ≅ 180° − 90° − tan−1 F G = 81°
                                  f54

    5. H9:& (4) ≅ (+56 + +57 )(1 − %=>>? ∗ (4))
                                                                               676 +) 8 +) 9
                  %=>>? ∗ (0) = −(1 + 671,2 *+) * ∥ +) + - 675 +) , )                          = −46.33 /
                                                                               +) 8 + +) 9
                                                          671,2 676 +) 8 +) 9
                         lim %&''( ∗ (DK) ≅ −(1 −              )              = 375.8
                         <→∞                              675 +) 8 + +) 9




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021




                                       Svolgimento
    1. Calcolare l’espressione del guadagno ideale di segnale tra Iout(s) e Iin(s) nello
       schema.
       Lo schema ha una retroazione negativa che porta il transistore M6 ad avere una corrente
       di drain pari E: .

                                                       F;< (G)
                                                               =H
                                                        F= (G)

    2. Calcolare tutte le tensioni (Va, Vb, Vc, Vd e Ve) e tutte le correnti di polarizzazione
       considerando Ib=100µA.
       Considerando i transistori in saturazione, la corrente nei rami del primo stadio M1 e M2
       sarà di 20µA. Di conseguenza |Vgs1,2|= 0.91V con Va=2.56V, Vgs3,4= 0.74V con Vb=0.74V.
       Considerando M5 in saturazione la sua corrente sarà di 80µA e quindi la sua Vgs5= 0.74V.
       IDM6 sarà uguale a 100µA Vgs6 sarà di =0.711V.
       Quindi Vd=Ve+0.711=1.711V.


    3. Calcolare il guadagno d'anello in continua
       Considerando la polarizzazione abbiamo i seguenti valori di trasconduttanza di segnale
       trascurando l’effetto della modulazione di canale.
                                   674,$ ≅ 126#'/)

                                   67@ ≅ 1143#'/)

                                   67A ≅ 1789#'/)

         Non scorrendo corrente nel ramo di Vtest lo schema può essere semplificato come in
         figura :
                                                                        R
                 %&''( (0) ≅ −671,2 *+) * ∥ +) + - 675 +) ,                       = −340.65 k
                                                                 1/ 676 + 1?

                                           L%&''( (0)L>? = 110MN




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021




    4. Calcolare il guadagno d’anello in frequenza e tracciarne il diagramma asintotico e
       calcolare la frequenza di attraversamento dell’asse a 0db.

         Il guadagno d’anello ha un polo e uno zero in entrambi i casi
                                                                 (1 + NOB1 )
                                      %&''( (4) = %&''( (0)
                                                                *1 + NOC1 -

         Il polo della capacità Cc sarà

                              1D = P+0 4 ∥ +0 2 Q 67@ +0 5 + +0 5 = 572.5 QΩ

         Quindi il polo sarà alla frequenza

                                                       R%4 ≅ 13.9ST

         Nel caso dello schema riconosciamo una configurazione che genera uno zero destro di
         pulsazione paria a T4 .

                                                      T4 = 67@ /$DD

                                                     RE4 = 9.096 /ST

         Infatti, Considerando K → ∞, il nostro guadagno d’anello tenderà a
                                                    671,2         R
                               lim %&''( (DK) ≅                             = 0.54
                              <→∞                    675 1/ 676 + 1?




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021

                                             "$%%! !




                                                               X           0
                                                              !!"     !#       !&"

                                          ∠ "$%%! !
                                                       180°


                                                                    90°




                                             RG
         WF ≅ 180° − 90° − STU−1 F              G = 62°
                                            RE4
                                                      674,$    R
                                                 KG ≅
                                                       $D 1/ 67A + 1'

                                                       RG ≅ 4.75/ST

    5. Considerando una variazione di resistenza VW< pari al 10% valutare il segnale
       equivalente Vin riportato nello schema e valutare la funzione di trasferimento in
       frequenza Vout(s) e Vin (s)
                                          )H! = XW< Y=
       Cosiderando la relazione del guadagno reale
                              Z5DE (4)     %FH (4)         %HFK (4)
                                       =               +
                              ZFG (4) P1 − %I55J (4) Q Y1 − %I55J (4)Z
                                                    I4



         In questo caso abbiamo

                                                   %"> (4) = 0
         e


                                                                    [R
                                                %>"- (4) =
                                                              1/ 676 + 1?

         Considerando i valori precedentemente calcolati di %&''( (4) abbiamo




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021

                                 "$%& !
                                  "'( !                                        40db




                                                   -77db

                                                            X
                                                           !!"           !#




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
              Complementi di Circuiti e sistemi
                      elettronici
                                                  Anno accademico 2021/2022


Prova scritta di Elettronica Analogica
                                                         23 Febbraio 2022
                                                                                                                                1
                                                                                                                                  # $ = 100#'/) $
                                                                               5V               5V                              2 ! "#
                                                                        M3                       M4                             1
                                                                                                                                  # $ = 20#'/) $
                                                        5V
                                                                    (16/1)                       (16/1)        5V
                                                                                                                                2 % "#
                                                                                                                     80uA
                                                 40uA
                                                                                                                                )&! = *)&% * = 0.6)
                                                                          M5                     M6
                               R2                                                                (16/1)                   OUT

              R1                                 M1     Va   M2
                                                                    (16/1)
                                                                                                                                -" = 1 /Ω
                                                                                                          Cc         CL
                           -             INa                      INb               Vb

                           +
                                    Vo
                                         (4/1)                    (4/1)
                                                                                                                                $' = 2012
                                                                                                                M10
                   2.5 V                                                  M7             2V      M8              (4/1)
Vin                                                                  (1/5)                       (1/5)                          $( = 1012
      2.5 V                                                                                                         (4/1)
                                                                                                                    M9          3) = 104Ω
                                                                  40uA                   40uA

                                                                                                                                3$ = 1004Ω
                    a)                                                                   b)




Considerando il circuito di figura

       1. (Punti 6) Calcolare l’espressione del guadagno ideale di segnale tra Vin(s) e Vout(s) dello
          schema di figura a) e indicare quali morsetti (INa e INb) dello schema di figura b)
          corrispondono al morsetto invertente e non invertente.
       2. (Punti 7) Calcolare tutte le tensioni (Va, Vb e OUT) e tutte le correnti di polarizzazione,
          quando Vin è pari a 0V.
       3. (Punti 7) Calcolare il guadagno d’anello in continua
       4. (Punti 7) Calcolare l il guadagno d’anello in frequenza, tracciarne il diagramma
          asintotico, calcolare la frequenza di attraversamento dell’asse a 0db e il margine di
          fase.
       5. (Punti 6) Calcolare il guadagno reale tra Vin(s) e Vout(s).




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
              Complementi di Circuiti e sistemi
                      elettronici
                                                  Anno accademico 2021/2022


Prova scritta di Elettronica Analogica
                                                         23 Febbraio 2022
                                                                                                                                1
                                                                                                                                  # $ = 100#'/) $
                                                                               5V               5V                              2 ! "#
                                                                        M3                       M4                             1
                                                                                                                                  # $ = 20#'/) $
                                                        5V
                                                                    (16/1)                       (16/1)        5V
                                                                                                                                2 % "#
                                                                                                                     80uA
                                                 40uA
                                                                                                                                )&! = *)&% * = 0.6)
                                                                          M5                     M6
                               R2                                                                (16/1)                   OUT

              R1                                 M1     Va   M2
                                                                    (16/1)
                                                                                                                                -" = 1 /Ω
                                                                                                          Cc         CL
                           -             INa                      INb               Vb

                           +
                                    Vo
                                         (4/1)                    (4/1)
                                                                                                                                $' = 2012
                                                                                                                M10
                   2.5 V                                                  M7             2V      M8              (4/1)
Vin                                                                  (1/5)                       (1/5)                          $( = 1012
      2.5 V                                                                                                         (4/1)
                                                                                                                    M9          3) = 104Ω
                                                                  40uA                   40uA

                                                                                                                                3$ = 1004Ω
                    a)                                                                   b)




Considerando il circuito di figura

       1. (Punti 6) Calcolare l’espressione del guadagno ideale di segnale tra Vin(s) e Vout(s) dello
          schema di figura a) e indicare quali morsetti (INa e INb) dello schema di figura b)
          corrispondono al morsetto invertente e non invertente.
       2. (Punti 7) Calcolare tutte le tensioni (Va, Vb e OUT) e tutte le correnti di polarizzazione,
          quando Vin è pari a 0V.
       3. (Punti 7) Calcolare il guadagno d’anello in continua
       4. (Punti 7) Calcolare l il guadagno d’anello in frequenza, tracciarne il diagramma
          asintotico, calcolare la frequenza di attraversamento dell’asse a 0db e il margine di
          fase.
       5. (Punti 6) Calcolare il guadagno reale tra Vin(s) e Vout(s).




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
             Complementi di Circuiti e sistemi
                     elettronici
                                     Anno accademico 2019/2020


Prova scritta di Elettronica Analogica
                                             21 Luglio 2020

Considerando il circuito riportato in figura

                                                         Vdd = 5V

                                                                                                1
               M1                                                                                 # $ = 60#(/* $
                              60uA                                            M7                2 ! "#
                                                         M6
                          (1/1)                  (4/1)                        (4/1)             1
       Iin                                                                                        # $ = 30#(/* $
                                                                                      Vo        2 % "#
                                                               Cc                               *&! = ,*&% , = 1*
                                   M2            M3
                                                                             M5                 -" = 1 /Ω
              60uA
                                                                 (1/1)                          $ = 101F
                                 (1/1)          (1/1)
                                                                                                $' = 10034
                                                                      Gnd
                                                                                                5( = 507Ω
                                     C
                                               R1


    1. (Punti 6) Calcolare tutte le tensioni e tutte le correnti di polarizzazione dello schema
       considerando l’ingresso Iin pari a 0.
    2. (Punti 4) Calcolare l’espressione del guadagno ideale di segnale tra Vout(s) e Iin(s)
    3. (Punti 8) Calcolare il guadagno d’anello in continua.
    4. (Punti 8) Calcolare il guadagno d’anello in frequenza, tracciarne il diagramma
       asintotico e calcolare la frequenza di attraversamento dell’asse a 0db.
    5. (Punti 4) Valutare il margine di fase del guadagno d’anello
    6. (Punti 4) Valutare la resistenza di uscita ad anello chiuso




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2019/2020


                                              Soluzioni
    1. Vgs1,2,3,5= 2V e |Vgs6,7|= 1.7 V e quindi Vo=4V
    2. !!""# (0) = −'()$ +% & ∥ +% $ + ()' +% ' ()( +% & ∥ +% $ . = −7260

                                   (1−,- )(1+,- )                    (1−,- )
    3.   !!""# (2) = !!""# (0) (1+,- !1)(1+,-!2 ) = !!""# (0) (1+,-!1 )
                                         $1        $2                       $1



                                                               8%( = 269:
                                                              80( = 23/9:


                     "%&&! !




                                              !$

                            X                              o
                            !!"                         !#"




                                    2                    2
    4. ;1 ≅ 180° − tan−1 <2 % = − tan−1 >2 % ? = 89°
                                    &'                   ('
                     -! " ∥-! #
    5. ;"+, = /01!""#(%) = 34.7Ω




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2019/2020




                                       Svolgimento
    1. Calcolare tutte le tensioni e tutte le correnti di polarizzazione dello schema
       considerando l’ingresso Iin pari a 0. Lo schema è retroazionato negativamente,
       considerando l’amplificatore avere un guadagno molto alto a tutte le frequenze, tutti i
       dispositivi finiranno per portare una corrente di drain pari a ID=60uA. Quindi le tensioni
       saranno
       Vgs1,2,3,5= 2V e |Vgs6,7|= 1.7 V e quindi Vo=4V

    2. Calcolare l’espressione del guadagno ideale di segnale tra Vout(s) e Iin(s).

                                                @456 (A)       C9
                                                         =−
                                                 B78 (A)    D + AEC9

    3. Calcolare il guadagno d'anello in continua
       Considerando la polarizzazione abbiamo i seguenti valori di trasconduttanza di segnale
       trascurando l’effetto della modulazione di canale.
                             @A(,$,4,5 = @A ≅ 120#(/*


                !!""# (0) = −'()$ +% & ∥ +% $ + ()' +% ' ()( +% & ∥ +% $ . = −7260

                                           F!!""# (0)F:; = 77.2 GH




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2019/2020


    4. Calcolare il guadagno d’anello in frequenza e tracciarne il diagramma asintotico e
       calcolare la frequenza di attraversamento dell’asse a 0db.

                                       M1
                                                                          M6               M7
                                                (1/1)             (4/1)                    (4/1)
                             Vtest                                                                 Vo
                                                                               Cc
                                                         M2       M3
                                                                                          M5

                                                        (1/1)    (1/1)          (1/1)

                                         Gloop vtest

                                                           C
                                                                 R1

         Il guadagno d’anello ha 2 poli e 2 zeri in cui lo zero della capacità C coincide con il polo.
                                             (1 − EF61 )(1 + EF62 )                     (1 − EF61 )
                   !!""# (2) = !!""# (0)                                 = !!""# (0)
                                             (1 + EF81 )(1 + EF82 )                     (1 + EF81 )

         La costante di tempo della capacità Cc può essere espressa come:
                                                         F%( = $' 59:;'

                59:;' ≅ 1/()1 + (()5 /()1 + ()2 /()1 ()3 +0 2 + 1)(+0 7 ∥ +0 5 ) ≅ 61JΩ

         Quindi

                                                           8%( = 269:

         Per frequenza che tende all’infinito il nostro schema continua ad avere un guadagno diverso da
         zero quindi abbiamo uno zero. Lo schema può essere semplificato considerando che la
         struttura M2, M3, M6 e M7 ha come azione quella di potenziare la trasconduttanza del
         transistore M5 di un fattore (1 + () +0 ).
         Quindi

                                              E0( = () (1 + () +0 )/($' )

                                                          80( = 23/9:




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2019/2020



         L’attraversamento dell’asse a 0db sarà a 20db per decade

                                              8< = 8%( !ABBC (0) = 188KLM


                                                          8< < 80(



                                         "%&&! !




                                                                !$

                                              X                          o
                                              !!"                     !#"




    5. Valutare il margine di fase del guadagno d’anello
                                                    8<          8<
                                ;1 ≅ 180° − tan−1 J K − tan−1 < = = 89°
                                                   8%(         80(
    6. Resistenza and anello chiuso
                                                     ND E ∥ ND F
                                        C456 =                   = TU. VΩ
                                                   D + OPQQR(S)




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
           Complementi di Circuiti e sistemi
                   elettronici
                                                      Anno accademico 2020/2021


Prova scritta di Elettronica Analogica
                                                                  10 Maggio 2021


                  2.5V                                2.5V

                    M10                          M5          M6                                              1
                                                                                                               # $ = 100#'/) $
        VB2        (100/0.5)       (50/0.5)                       (50/0.5)                                   2 ! "#
                     Va                                                                                      1
                                                                                                               # $ = 20#'/) $
           M1            M2                      Vc
                                                                                                             2 % "#
 V+      (50/0.5) (50/0.5)         V-
                                                                                        2.5V
                                                                                                             )&! = *)&% * = 0.5)
                                                                             Vin   +
                                                                   Vout
                                                                                               Vout          -" = 1 /Ω
           M4             M3                                                       -
         (20/1)          (20/1)
                                                                                                             )'( = 0.6)
                    Vb                           Vd                                                   Cout   )'$ = 1.9)
                     M9
                                                                  M8
        VB1         (40/1)
                                          M7
                                                                                                             $")* = 10034
                                        (20/1)                    (20/1)


                                  a)                                                   b)



      1. (Punti 3) Calcolare l’espressione del guadagno ideale di segnale tra vout(s) e vin(s) dello
         schema riportato in figura (b).
      2. (Punti 8) Considerando lo schema dell’amplificatore operazionale “rail to rail” riportato
         in figura (a), calcolare tutte le tensioni (Va, Vb, Vc, Vd e Vout) e tutte le correnti di
         polarizzazione dello schema (a) e (b) considerando Vin =1.25 V e Vin=0.2 V.
      3. (Punti 7) Calcolare il guadagno d’anello in continua considerando Vin =1.25 V e Vin=0.2V.
      4. (Punti 9) Calcolare il guadagno d’anello in frequenza, tracciarne il diagramma asintotico,
         calcolare la frequenza di attraversamento dell’asse a 0db considerando Vin=0.2 V e Vin
         =1.25 V.
      5. (Punti 6) Tracciare la risposta di Vout nel tempo ad un gradino di tensione in ingresso
         ampio 300m con Vin =1.25 V.




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
           Complementi di Circuiti e sistemi
                   elettronici
                                                      Anno accademico 2020/2021


Prova scritta di Elettronica Analogica
                                                                  10 Maggio 2021


                  2.5V                                2.5V

                    M10                          M5          M6                                              1
                                                                                                               # $ = 100#'/) $
        VB2        (100/0.5)       (50/0.5)                       (50/0.5)                                   2 ! "#
                     Va                                                                                      1
                                                                                                               # $ = 20#'/) $
           M1            M2                      Vc
                                                                                                             2 % "#
 V+      (50/0.5) (50/0.5)         V-
                                                                                        2.5V
                                                                                                             )&! = *)&% * = 0.5)
                                                                             Vin   +
                                                                   Vout
                                                                                               Vout          -" = 1 /Ω
           M4             M3                                                       -
         (20/1)          (20/1)
                                                                                                             )'( = 0.6)
                    Vb                           Vd                                                   Cout   )'$ = 1.9)
                     M9
                                                                  M8
        VB1         (40/1)
                                          M7
                                                                                                             $")* = 10034
                                        (20/1)                    (20/1)


                                  a)                                                   b)



      1. (Punti 3) Calcolare l’espressione del guadagno ideale di segnale tra vout(s) e vin(s) dello
         schema riportato in figura (b).
      2. (Punti 8) Considerando lo schema dell’amplificatore operazionale “rail to rail” riportato
         in figura (a), calcolare tutte le tensioni (Va, Vb, Vc, Vd e Vout) e tutte le correnti di
         polarizzazione dello schema (a) e (b) considerando Vin =1.25 V e Vin=0.2 V.
      3. (Punti 7) Calcolare il guadagno d’anello in continua considerando Vin =1.25 V e Vin=0.2V.
      4. (Punti 9) Calcolare il guadagno d’anello in frequenza, tracciarne il diagramma asintotico,
         calcolare la frequenza di attraversamento dell’asse a 0db considerando Vin=0.2 V e Vin
         =1.25 V.
      5. (Punti 6) Tracciare la risposta di Vout nel tempo ad un gradino di tensione in ingresso
         ampio 300m con Vin =1.25 V.




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                                   Anno accademico 2020/2021




                                                           Soluzioni
         !!"# (#)
    1.   !$% (#)
                  ="
    2. Con Vin=1.25V ID10 = 40µA. Di conseguenza |Vgs1,2|= 0.6V con Va=1.85V, Vgs3,4= 0.6V con
       Vb=0.65V. In queste condizioni entrambe i dispositivi M9 e M10 saranno in saturazione,
       quindi Vc=0.6V e Vd=1.9V. Considerando Vin=0.2V, ID10 = 40µA, invece la corrente di M9
       verrà annullata perché M4 e M3 sono in interdizione. Pertanto, Va=0V, Vb=0.8V, Vc=2.5V
       e Vd=0.6V.
    3. #%&&' (0) = −(561,2 + 564,3 )(*( ) ∥ *( * ∥ *( + ∥ *( , ) = −200
                                                                  -#%&&' (0)--. = 4612
         e per Vin=0.2V il risultato complessivo non cambia
                                   #%&&' (0) = −561,2 (*( * ∥ *( , ) = −200
                                                                  -#%&&' (0)--. = 4612


                                      /&''( (()
    4.   #%&&' (3) = 01+12 1
                                              !1



            "$%%! !




                              X
                             !!"         !#

          ∠ "$%%! !
                      180°


                                       90°




    5.

                         Vin          SR1                   Vin           SR2
           1.55V                                    0.5V


                               Vout                               VoutA
          1.25V                                     0.2V


                        t0                                 t0
                                               t                                t




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021


                                       Svolgimento
    1. Calcolare l’espressione del guadagno ideale di segnale tra vout(s) e vin(s) dello
       schema riportato in figura (b).
       Lo schema è retroazionato negativamente, considerando l’amplificatore avere un
       guadagno molto alto a tutte le frequenze la funzione di trasferimento Vout(s) e Vin(s)
       tende ad essere come la seguente nei due casi:
                                       4234 (5) 4234 (5)
                                               =         ="
                                       456 (5)   456 (5)


    2. Considerando lo schema dell’amplificatore operazionale “rail to rail” riportato in
       figura (a), calcolare tutte le tensioni (Va, Vb, Vc, Vd e Vout) e tutte le correnti di
       polarizzazione dello schema (a) e (b) considerando Vin =1.25 V e Vin=0.2 V.

         Con Vin=1.25V Considerando i transistori in saturazione, la corrente dei transistori M9 e
         M10 stadio sarà di 40µA. Di conseguenza |Vgs1,2|= 0.6V con Va=1.85V, Vgs3,4= 0.6V con
         Vb=0.65V. In queste condizioni entrambe i dispositivi M9 e M10 saranno in saturazione,
         quindi Vc=0.6V e Vd=1.9V. Considerando Vin=0.2V, la corrente di M10 rimarrà di 40µA,
         invece la corrente di M9 verrà annullata perché M4 e M3 sono in interdizione. Pertanto,
         Va=0V, Vb=0.8V, Vc=2.5V e Vd=0.6V.

    3. Calcolare il guadagno d'anello in continua
       Considerando la polarizzazione abbiamo i seguenti valori di trasconduttanza di segnale
       trascurando l’effetto della modulazione di canale.
                                   56(,$ ≅ 400#'/)

                                   563,4 ≅ 400#'/)

         Abbiamo per Vin=1.25V

                    #%&&' (0) = −(561,2 + 564,3 )(*( ) ∥ *( * ∥ *( + ∥ *( , ) = −200

                                            -#%&&' (0)-       = 4612
                                                         -.

         e per Vin=0.2V il risultato complessivo non cambia

                                  #%&&' (0) = −561,2 (*( * ∥ *( , ) = −200




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021

                                            -#%&&' (0)--. = 4612



    4. Calcolare il guadagno d’anello in frequenza, tracciarne il diagramma asintotico,
       calcolare la frequenza di attraversamento dell’asse a 0db considerando Vin=0.2 V e
       Vin =1.25 V.
       Il guadagno d’anello ha solo un polo in entrambi i casi
                                                           #%&&' (0)
                                            #%&&' (3) =
                                                           (1 + :;51 )

         Il polo della capacità dipende dallo stato di polarizzazione perché cambia la
         resistenza vista a suoi capi. Pertanto, per Vin=1.25V abbiamo
                                   <6 = *0 6 ∥ *0 2 ∥ *0 3 ∥ *0 8 = 2507 Ω

         quindi il polo sarà alla frequenza

                                                        =% ≅ 6.36?@A

         Invece, per Vin=0.2V abbiamo

                                          <6 = *0 2 ∥ *0 8 = 5007 Ω

         quindi il polo sarà alla frequenza

                                                        =% ≅ 3.18?@A

         Valutando l’attraversamento dell’asse a 0 db abbiamo per Vin=1.25V
                                             56(,$ + 564,3
                                       =* ≅                 = 636?@A
                                                 2 C $")*

         Invece, nel caso con Vin=0.2 V avremo

                                                      56(,$
                                                 =* ≅        = 1.2/@A
                                                    2 C $")*
         Il margine di fase è circa in enrtambi i casi
         D7 ≅ 180° − 90° = 90°




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2020/2021


                                       "$%%! !




                                                              X
                                                             !!"        !#

                                    ∠ "$%%! !
                                                    180°


                                                                     90°




    5. Tracciare la risposta di Vout nel tempo ad un gradino di tensione in ingresso ampio
       300m con Vin =1.25 V e Vin =0.2 V.



                                                "$%%! !      "&' !




                                                        X
                                                       !!"         !#




         Lo schema ha un’intrinseca limitazione di slew rate dovuta alla massima corrente di
         uscita. Nel caso con Vin=1.25V abbiamo

                                            E<1 = 80#'/$")* = 0.8/) /:FG

         In questo caso il guadagno reale sarà




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                         Anno accademico 2020/2021

                                                >&<= (3)      1
                                                         =
                                                >>? (3)    1 + 3@
         Considerando che


                                                     Δ B>?
                                                           > E<
                                                       @
         Nel caso con Vin=0.2V abbiamo
                                              E<2 = 40#'/$")* = 0.4/) /:FG




         Quindi durante il transitorio la pendenza iniziale sarà limitata dalla saturazione della corrente di
         uscita




                           Vin          SR1                                Vin           SR2
            1.55V                                            0.5V


                                 Vout                                            VoutA
           1.25V                                             0.2V


                         t0                                              t0
                                                 t                                              t




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
                                                                                                                          www.uniud.it
 UNIVERSITÀ                          Dipartimento Politecnico
                                     di ingegneria e architettura
 DEGLI STUDI
 DI UDINE
 hic sunt futura




             Complementi di Circuiti e sistemi
                                                   elettronici
                                         Anno accademico 2022/2023



Prova scritta di Elettronica Analogica
                                                   17 Gennaio 2023

                                                                            5V



                                                                   (8/1) Ms           Mio (/1)
                                                                                                   z4ox      100uA/V2
                                                         5V
                                                                       V
                                                                                                   1
                                                  40uA             (8/1)Mr            Ma (8/1)     4pox40uA/V2

                    W                                                  Va

                                         Np
                                                  Mi          M2
                                                                                         out       Vrn7 = 0.6V
                                                                                                   T1M
C                             Vout        (2/1)
                                                                   (5/1) Me      YMs(5/1)          C   4nF
 Vn 1
                  2.5V
                                                         VD                                        C    400pF
                                                                   (10/1) Ma           Ma (1a/1)
                                                                                                   R=1MA


                         a)                                                      b)



Considerando il circuito di acquisizione di un sensore piezoelettrico riportato in figura,
rispondere ai seguenti quesiti.

        1.   (Punti 6) Calcolare 'espressione del guadagno ideale di segnale tra Vinls) e Vout(s) dello
           schema di figura (a)
        2. (Punti 7) Considerando che lo schema dell'amplificatore di figura (b), calcolare tutte le
           tensioni e le correnti dello schema quando Va è uguale a 0.
           (Punti 8) Tracciare il diagramma asintotico del guadagno d'anello in frequenza e
           calcolare la frequenza di attraversamento dell'asse a Odb e il margine di fase.
        4. (Punti 7) Tracciare il diagramma asintotico del modulo del guadagno reale.
        5.   (Punti 5) Stimare la risposta ad un gradino di tensione in ingresso pari a 100mV




                                                                                                                        SA9TEA
Via delle Scienze, 206-33100 Udine
CF 80014550307 - P.VA 01071600306 1BAN IT65Z0200812310000040469457 BIC swift UNCRITM1UNG                          ONV GL
