---
fonte: "Testo230120_moretto.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Complementi di Circuiti e sistemi
                    elettronici
                                          Anno accademico 2019/2020


Prova scritta di Elettronica Analogica
                                                     23 Gennaio 2020

Considerando il circuito riportato in figura
                             5V

                     (2/1) (2/1)                         (8/1)        1
                                                                        𝜇 𝐶 = 50𝜇𝐴/𝑉 $
  (2/1)             M4        M3
                                               V2
                                                         M5           2 ! "#
 M7                                                                   1
                                                                        𝜇 𝐶 = 25𝜇𝐴/𝑉 $
                                                                      2 % "#

                     M1     M2
                                     C1
                                                R2
                                                                      𝑉&! = +𝑉&% + = 1𝑉
                                                         Vout
                    (2/1)   (2/1)
           Vin                            V1                          𝑟" = 10 𝑀Ω
                                                                 CL
                                           R1
                                                                      𝑅' = 5𝑘Ω
                              50uA         C1
                                                                      𝑅$ = 10𝑘Ω
                    0V

                                          V3                          𝐶' = 200𝑝F
  (2/1)                                                  M6

      M8                                                 (8/1)        𝐶( = 1𝑛F
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
    3. 𝐺)**+ (0) = −𝑔𝑚',- 4 -𝑟. / ∥ 𝑟. 0 0 = 2𝑘
    4.
                                                                        (1 + 𝑠𝜏𝑧1 )
                                 𝐺)**+ (𝑠) = 𝐺)**+ (0)
                                                              (1 + 𝑠𝜏𝑝1 )(1 + 𝑠𝜏𝑝2 )

                                                           𝑓%( = 26.5𝐻𝑧
                                                         𝑓%- = 63.69𝑘𝐻𝑧

                                                         𝑓.' = 159.15𝑘𝐻𝑧

                                               𝑓/ ≅ 𝑓%( 𝐺𝑙𝑜𝑜𝑝 (0) = 53𝑘𝐻𝑧
                                    1                    1                      1
    5. 𝜑0 ≅ 180° − tan−1 C1 ! D − tan−1 C1 ! D + tan−1 E1 ! F = 68.69°
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
                           𝒗𝒐𝒖𝒕 (𝒔)          𝒔𝑪𝟏 𝑹𝟐      𝟏 + 𝒔𝑪𝟏 (𝑹𝟏 + 𝑹𝟐 )
                                    =𝟏+               =
                            𝒗𝒊𝒏 (𝒔)       𝟏 + 𝒔𝑪𝟏 𝑹𝟏         𝟏 + 𝒔𝑪𝟏 𝑹𝟏
    3. Calcolare il guadagno d'anello in continua
       Considerando la polarizzazione abbiamo i seguenti valori di trasconduttanza di segnale
       trascurando l’effetto della modulazione di canale.
                   𝑔𝑚',$ ≅ 100𝜇𝐴/𝑉


                                 𝐺)**+ (0) = −𝑔𝑚',- 4 -𝑟. / ∥ 𝑟. 0 0 = 2𝑘

                                            F𝐺)**+ (0)F=> = 66𝑑𝑏

    4. Calcolare il guadagno d’anello in frequenza e tracciarne il diagramma asintotico e
       calcolare la frequenza di attraversamento dell’asse a 0db.
       Il guadagno d’anello ha 2 poli e 1 zero


                                                                 (1 + 𝑠𝜏𝑧1 )
                                 𝐺)**+ (𝑠) = 𝐺)**+ (0)
                                                           (1 + 𝑠𝜏𝑝1 )(1 + 𝑠𝜏𝑝2 )

         Le due costanti di tempo possono essere espresse come




Via delle Scienze, 206 – 33100 Udine
CF 80014550307 - P.IVA 01071600306 – IBAN IT65Z0200812310000040469457 – BIC swift UNCRITM1UN6
         Complementi di Circuiti e sistemi
                 elettronici
                                     Anno accademico 2019/2020

         Dove

                                               𝜏𝑝1 + 𝜏𝑝2 = 𝐶𝐿 𝑅′ 𝐿 + 𝐶1 𝑅′ 1
                                             I                1         1
                                              𝜔𝑝1 + 𝜔𝑝2 =          +
                                                           𝐶𝑐 𝑅 𝐿 𝐶1 𝑅′′ 1
                                                                ′′



         Dove

                                                𝑅6 ( ≅ J𝑟7 8 ∥ 𝑟7 9 L = 5𝑀Ω

                                       𝑅66 ( ≅ 𝑟7 8 ∥ 𝑟7 9 ∥ (𝑅' + 𝑅$ ) = 14.95𝐾Ω

                                       𝑅6' ≅ 𝑅' + 𝑅$ + J𝑟7 8 ∥ 𝑟7 9 L = 5.015𝑀Ω

                                                 𝑅66' ≅ 𝑅' + 𝑅$ = 15𝐾Ω


         Quindi i poli saranno
                                                       𝑓%( = 26.5𝐻𝑧
                                                     𝑓%- = 63.69𝑘𝐻𝑧


         Gli zeri possono essere calcolati considerando
                                                                   1
                                                       𝑠.' = −
                                                                 𝐶' 𝑅'
         Quindi
                                                     𝑓.' = 159.15𝑘𝐻𝑧

         L’attraversamento dell’asse a 0db sarà

                                               𝑓/ ≅ 𝑓%( 𝐺𝑙𝑜𝑜𝑝 (0) = 53𝑘𝐻𝑧




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
                                         𝑓/          𝑓/          𝑓/
                     𝜑0 ≅ 180° − tan−1 P Q − tan−1 P Q + tan−1 C D = 68.69°
                                        𝑓%'         𝑓%$         𝑓.'


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
