---
fonte: "4a - Feedbacksystem_ita_1.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

UNIVERSITY OF UDINE

Department DIEG
Via delle scienze 206
33100 Udine (UD), Italy




                      FEEDBACK SYSTEM 1
                      Associate professor Stefano Saggini
                      Lezione di complementi di elettronica
Sommario
¨   Introduzione ai sistemi mutistadio
    ¤ Rappresentazione come doppi bipoli

¨   Introduzione ai circuiti retroazionati
    ¤ Calcolo del guadagno d’anello

    ¤ Calcolo del guadagno ideale
    ¤ Calcolo del guadagno diretto

    ¤ Calcolo del guadagno reale
     Amplificatore multistadio
     ¨   Sistema multistadio
         ¤ Il Guadagno tra vout e vs dipende da I valori di RL e Rg




                                                 vout



Rg                                                             RL
vs
Descrizione dell’amplificatore
¨   Circuito lineare per la descrizione dell’amplificatore
                                Questa rappresentazione è più adatta per il
                                calcolo dell’effettivo guadagno:
                                 Doppio bipolo tripolare.
                                   vin

                                         iin                   Rout
Questa rappresentazione non è
sufficiente                              Rin                   Av vin
                                                               oppure
                                                                R iin
           α
                                   vin

                                           iin
                                                              Rout
                                         Rin                   G vin
                                                                AI Iin
Amplificatore differenziale
¨   Il segnale di ingresso differenziale in tensione

                                              v DIF = v+ − v−
       V+
                 +              Vout                v+ + v−
                                              vCM =
            V-                                         2
                 -

                                                    AD
                                             CMRR =
                     Guadagno indesiderato          ACM

vOUT = AD v DIF + ACM vCM
     Rappresentazione matematica
     ¨   Rappresentazione matematica

                                         ⎡ v ⎤    ⎡ i ⎤
v1
          i1
                   R         i2
                                   v2    ⎢ 1 ⎥ = R⎢ 1 ⎥
                                         ⎢ v ⎥    ⎢ i ⎥
                                         ⎣  2 ⎦   ⎣ 2 ⎦


              ⎡ r r ⎤ ⎡ R               ≅0    ⎤
              ⎢  11 12 ⎥ ⎢ in                 ⎥
           R=           =
              ⎢ r r ⎥ ⎢ R               Rout ⎥⎦
              ⎣ 21 22 ⎦ ⎣
     Rappresentazione matematica
     ¨   Rappresentazione matematica

                                             ⎡ i ⎤    ⎡ v ⎤
v1
          i1
                     G           i2
                                       v2    ⎢ 1 ⎥ = G⎢ 1 ⎥
                                             ⎢ i ⎥    ⎢ v ⎥
                                             ⎣  2 ⎦   ⎣ 2 ⎦


                                   ⎡ 1               ⎤
                  ⎡ g            ⎤ ⎢         ≅0 ⎥
                           g12         Rin
               G= ⎢   11         ⎥=⎢                 ⎥
                  ⎢ g      g 22 ⎥⎦ ⎢ G       1       ⎥
                  ⎣ 21             ⎢⎣          Rout ⎥⎦
     Rappresentazione matematica
     ¨   Rappresentazione matematica

                                        ⎡ i ⎤      ⎡ v ⎤
v1
          i1
                    Hʹ        i2
                                   v2   ⎢ 1 ⎥ = H ʹ⎢ 1 ⎥
                                        ⎢ v ⎥      ⎢ i ⎥
                                        ⎣  2 ⎦     ⎣ 2 ⎦



                    ⎡ hʹ hʹ ⎤ ⎡ 1       ≅0 ⎥
                                              ⎤
                                ⎢ Rin
               Hʹ = ⎢  11 12 ⎥=
                    ⎢ hʹ hʹ ⎥ ⎢               ⎥
                    ⎣ 21 22 ⎦ ⎢⎣ AV     Rout ⎥⎦
     Rappresentazione matematica
     ¨   Rappresentazione matematica

                                             ⎡ v ⎤       ⎡ i ⎤
v1
          i1
                  H ʹʹ       i2
                                     v2      ⎢ 1 ⎥ = H ʹʹ⎢ 1 ⎥
                                             ⎢ i ⎥       ⎢ v ⎥
                                             ⎣  2 ⎦      ⎣ 2 ⎦


                 ⎡ hʹʹ hʹʹ ⎤ ⎡ Rin        ≅0      ⎤
                              ⎢                   ⎥
          H ʹʹ = ⎢  11  12 ⎥=
                                          1
                 ⎢ hʹʹ hʹʹ ⎥ ⎢ AI                 ⎥
                 ⎣ 21 22 ⎦ ⎢⎣               Rout ⎥⎦
Circuiti retroazionati
¨   La retroazione:
    ¤ Stabilizza il guadagno rispetto alle caratteristiche
      parametriche dei componenti perché dipende dai
      compenti passivi
      n Migliora la linearità
 Teoria dei circuiti reazionati
Differenze tra lo schema di reazione ideale e il circuito con retroazione:
¨ Ogni blocco dello schema a blocchi ha una direzione e un trasferimento che
   non dipende dai blocchi a cui è collegato, lo schema elettrico non è sempre
   direzionale e il trasferimento dipende dagli elementi a cui è connesso
¨ I segnali dello schema elettrico possono essere di tensione o di corrente

¨ Non c’è una equivalenza netta tra lo schema a blocchi e lo schema circuitale
   c’ è solo una similitudine, infatti il trasferimento complessivo non è ricavabile in
   modo immediato dal trasferimento degli schemi a blocchi.




                 α                    VI(t)                                       VO(t)
                                                             α
I(t)                      O(t)
                                          II(t)                               IO(t)
                                                              β
                 β
 Individuazione delle reazioni in uno
 schema
Per l’analisi della reazione è fondamentale individuare il
  blocco α e β:
¨ Per l’individuazione della direzione dell’anello è
  necessario seguire la direzione dei componenti direzionali
  di cui è composto lo schema

          C                D

                                          +
   B               G
                                          -
          E                S
         Reazione serie e parallelo
     ¨     The type of feedback (Voltage or current) depend on the
           connection          Serr
                             +      α
                                                Sin                                        Sout
                                                                             β
                                                                                  Input current connected in parallel, the error is a current.
Input parallel the error is the current out is the voltage
                                                                                  Output in series the output is the current.


   iIN                    α                    vout                                      iIN                         α                   iOUT

                           β                                                                                         β
                                                                                 Input in series the error is the voltage, out in parallel the voltage is
Input in series the error is the voltage, out in series the current is the
                                                                                 the output.
output.


                           α               iOUT                                                                   α                   vout
   v IN                                                                                  v IN
                           β                                                                                      β
Retroazione parallelo parallelo
¨    Accesso ad un nodo della circuito retroazionato
     l’uscita è su un nodo della retrazione
    Effetto della
    retroazione negativa                     Transresistance



               is          GS
                                Gα      GL     vL


    Intervento
    dell’ingresso

                                Gβ
      Retroazione parallelo parallelo
      ¨   Calcolo del risultato
                    ⎡ G          ⎡ α                                  ⎤
                          0 ⎤ ⎢ g 11 + g 11
                                         β
                                            + GS      g 12
                                                        α
                                                           + g 12
                                                               β
                                                                      ⎥
     Gγ = Gα + Gβ + ⎢ S       ⎥=
                    ⎢ 0
                    ⎣     GL ⎥⎦ ⎢ g α21 + g 21
                                            β
                                                   g α22 + g 22
                                                             β
                                                                + GL ⎥⎦
                                 ⎣
                                              ⎡ i ⎤      ⎡ v ⎤
                                              ⎢ S ⎥ = Gγ ⎢ 1 ⎥
                                              ⎢⎣ 0 ⎥⎦    ⎢ v ⎥
                                                         ⎣ 2 ⎦
is          v1       Gγ                  v2

                                                   ⎡ i ⎤ ⎡ v ⎤
                                              G γ−1⎢ S ⎥ = ⎢ 1 ⎥
                                                   ⎢⎣ 0 ⎥⎦ ⎢⎣ v2 ⎥⎦
Retroazione parallelo parallelo
¨   Soluzione
                   ⎡ α
             1 ⎢ g 22 + g 22 + GL
                            β
                                          (
                                         − g 12
                                             α
                                                + g 12
                                                    β
                                                         ) ⎤⎥⎡⎢ i ⎤⎥ = ⎡⎢ v ⎤⎥
                                                                S         1
                   ⎢                                     ⎥
          det(Gγ ) ⎢ − g α + g β
                      (           )     g 11
                                          α
                                             + g 11
                                                 β
                                                    + GS ⎥⎢⎣ 0 ⎥⎦ ⎢⎣ v2 ⎥⎦
                         21    21
                   ⎣                                     ⎦


¨   Analisi del primo trasferimento                                    Termine dominante RD
             v − ( g + g ) −g
                      α      β           α         β
              2
              =
                      21
                          =
                             21
                              +
                                −g       21        21                    Termine parassita RP
             iS      detGγ            detGγ   detGγ
Analisi del primo termine RD
¨      Analisi del termine RD

                                                   α
                                                                   Guadagno di andata
                                             −g
        RD =                                       21

               (g + g + G )(g + g + G ) − (g + g )(g + g )
                 α
                 11
                        β
                        11    S
                                      α
                                      22
                                            β
                                            22        L
                                                              α
                                                              12
                                                                     β
                                                                     12
                                                                           α
                                                                           21
                                                                                β
                                                                                21




                                                                                                       Gideale
                                                 −G                                           1             1
lim RD = lim                                                                         =                 ≅
G→−∞     G→−∞
                ( g + g + G ) ( g + g + G ) − ( g + g ) (G + g ) ( g + g )
                  α
                  11
                         β
                         11       S
                                       α
                                       22
                                             β
                                             22           L
                                                               α
                                                               12
                                                                      β
                                                                      12
                                                                                β
                                                                                21
                                                                                         α
                                                                                         12
                                                                                                  β
                                                                                                  12
                                                                                                           g 12
                                                                                                             β




                            ⎡ 1                          ⎤
                            ⎢                    ≅0      ⎥
                                Rin
                       Gα = ⎢                            ⎥
                            ⎢ G                  1       ⎥
                            ⎢⎣                     Rout ⎥⎦
Gideale nel circuito

                                            v2


  is    GS      v1 = 0
                i1 = 0

                         v2 non vincolata
                         i2 non vincolata




                                                      v2
                                            Gideale =
                                                      iS
Dimostrazione

                                            v2


  iS   GS       v1 = 0
                i1 = 0

                         v2 non vincolata
                         i2 non vincolata



                                                      is
                                                 v2 = β
                                                     g 12
Analisi del primo termine RD
                          1                                              1
         RD =
                (g + g ) (g + g ) − (g + g + G )(g + g + G )
                     α
                     12
                                  β
                                  12
                                       α
                                       21
                                                 β
                                                 21
                                                               α
                                                               11
                                                                         β
                                                                         11            S
                                                                                                α
                                                                                                22
                                                                                                          β
                                                                                                          22   L

                            g             (g + g ) g
                                            α
                                            21
                                                                                  α
                                                                                  12
                                                                                            β
                                                                                            12
                                                                                                     α
                                                                                                     21




                                                               1                                                                 1
 RD = Gideale                                                                                                      = Gideale
                1+
                     g 21
                       β
                          g 12
                            α
                              (+ g 12
                                   β
                                      − g 11
                                          α
                                            ) (
                                             + g 11
                                                 β
                                                          )(
                                                    + GS g α22 + g 22
                                                                   β
                                                                      + GL                                     )               1− Gloop
                                                                                                                                   −1



                                               (g + g ) g α
                                                          12
                                                                    β
                                                                    12
                                                                              α
                                                                              21




 Gloop =
                                                     α
                                                      (
                                                 − g 12 + g 12
                                                            β
                                                               g α21          )
            g 21
              β
                 g 12
                   α
                     (+ g 12
                          β
                             − g 11
                                 α
                                        ) (
                                    + g 11
                                        β
                                           + GS g α22 + g 22
                                                          β
                                                             + GL                          )(                           )
Gloop nel circuito
                                     g11
                                      α
                                                 g 22
                                                   α


         GS                                                          GL




                                      Gβ

   Gloop =
                                 (
                               − g 12
                                   α
                                      + g 12
                                          β
                                            )g α21
               β
                (
             g 21 g 12
                    α
                           ) (
                       + g 12
                           β
                              − g 11
                                  α
                                     + g 11
                                         β
                                                )(
                                            + GS g α22 + g 22
                                                           β
                                                              + GL   )
Dimostrazione
                                                                         v1
                                              Gloop = −g α21
                                                                        itest
                         ⎡ 0 ⎤ ⎡ gα + g β + G                                        g 12
                                                                                       α
                                                                                          + g 12
                                                                                              β    ⎤⎡
                                                                                                       v   ⎤
                         ⎢         ⎥ = ⎢ 11 11   S                                                 ⎥⎢ 1 ⎥
                         ⎢⎣ itest ⎥⎦ ⎢      g 21
                                              β
                                                                                g α22 + g 22
                                                                                          β
                                                                                             + GL ⎥⎦⎢⎣ v2 ⎥⎦
                                       ⎣

                                                       ⎡ α
                          1                            ⎢ g 22 + g 22 + GL
                                                                  β
                                                                                                   (
                                                                                                − g 12
                                                                                                    α
                                                                                                       + g 12
                                                                                                           β
                                                                                                                ) ⎤⎥⎡⎢ 0 ⎤⎥ = ⎡⎢ v ⎤⎥
                                                                                                                                  1
                                                    β ⎢                                                           ⎥
 (g + g + G )(    g α22 + g 22      )
                               + GL − g 21    (
                                           g 12 + g 12         )                                            + GS ⎥⎦⎢⎣ itest ⎥⎦ ⎢⎣ v2 ⎥⎦
  α    β                    β           β    α
  11   11     S                                        ⎢⎣
                                                                   β
                                                               −g 21                            g 11
                                                                                                  α
                                                                                                     + g 11
                                                                                                         β




                       v1 =
                                                          (
                                                      − g 12
                                                          α
                                                             + g 12
                                                                 β
                                                                        )
                                                                    itest

                              (g + g + G )(g + g + G ) − g (g + g )
                               α
                               11
                                        β
                                        11        S
                                                          α
                                                          22
                                                                   β
                                                                   22       L
                                                                                      β
                                                                                      21
                                                                                           α
                                                                                           12
                                                                                                       β
                                                                                                       12




            Gloop =
                                                      (
                                                  − g 12
                                                      α
                                                         + g 12
                                                             β
                                                                g α21   )
                      g 21
                        β
                          (g 12
                             α
                                + g 12
                                    β
                                       − g 11
                                           α
                                             ) (
                                              + g 11
                                                  β
                                                     + GS g α22 + g 22
                                                                    β
                                                                       + GL     )(                          )
 Analisi del secondo termine RP
 ¨     Analisi del termine RP
                                                                        β
                                                                                              Guadagno parassita
                                                                   −g
         RP =                                                           21

                (g + g + G )(g + g + G ) − (g + g )(g + g )
                      α
                      11
                                 β
                                 11         S
                                                     α
                                                     22
                                                              β
                                                              22          L
                                                                                         α
                                                                                         12
                                                                                                   β
                                                                                                   12
                                                                                                             α
                                                                                                             21
                                                                                                                        β
                                                                                                                        21




                                                                          g 21
                                                                            β
        RP =
               (g + g ) g + (g + g ) g (g + g + G )(g + g + G )
                     α
                     12
                                β
                                12
                                       α
                                       21
                                                     α
                                                     12
                                                              β
                                                              12
                                                                        β
                                                                        21
                                                                           −
                                                                                    α
                                                                                    11
                                                                                              β
                                                                                              11        S
                                                                                                                  α
                                                                                                                  22
                                                                                                                             β
                                                                                                                             22    L




                                            g 21
                                              β
                                                                                                                                            1
RP =
       ( g + g ) g − ( g + g + G ) ( g + g + G ) 1+
         α
         12
                β
                12
                           β
                           21
                                      α
                                      11
                                                β
                                                11        S
                                                                   α
                                                                   22
                                                                               β
                                                                               22         L                           (g + g ) g       α
                                                                                                                                       12
                                                                                                                                                β
                                                                                                                                                12
                                                                                                                                                     α
                                                                                                                                                     21

                                                                                                        (g + g ) g − (g + g + G )(g + g + G )
                                                                                                            α
                                                                                                            12
                                                                                                                       β
                                                                                                                       12
                                                                                                                              β
                                                                                                                              21
                                                                                                                                       α
                                                                                                                                       11
                                                                                                                                                β
                                                                                                                                                11   S
                                                                                                                                                          α
                                                                                                                                                          22
                                                                                                                                                               β
                                                                                                                                                               22   L
Analisi del secondo termine
¨   Analisi del secondo termine
                            Guadagno diretto

                                      g 21
                                        β
                                                                            1
     RP =     β
               (
            g 21 g 12
                   α
                      + g 12
                          β
                            ) (
                             − g 11
                                 α
                                    + g 11
                                        β
                                           + GS   )(   g α22 + g 22
                                                                 β
                                                                    + GL 1− Gloop
                                                                      )

                                             g 21
                                               β
       Gdiretto =     β
                       (
                    g 21 g 12
                           α
                                  ) (
                              + g 12
                                  β
                                     − g 11
                                         α
                                            + g 11
                                                β
                                                          )(
                                                   + GS g α22 + g 22
                                                                  β
                                                                     + GL    )

                                           1
                        RP = Gdiretto
                                        1− Gloop
   Gdiretto nel circuito

          v                           v2
Gdiretto = 2
          iS             g11
                          α
                               g 22
                                 α

                    GS
               iS                          GL




                          Gβ
Dimostrazione
                                                                  v2
                                                Gdiretto =
                                                                  iS
                        ⎡ i ⎤ ⎡ gα + g β + G                               g 12 + g 12
                                                                                      ⎤⎡      ⎤
                                                                                      ⎥⎢ v1 ⎥
                                                                             α      β
                        ⎢ S ⎥ = ⎢ 11 11     S

                        ⎢⎣ 0 ⎥⎦ ⎢    g β
                                                                   g α22 + g 22
                                                                             β
                                                                                + GL ⎥⎦⎢⎣ v2 ⎥⎦
                                ⎣      21


                                                        ⎡ α
                          1                             ⎢ g 22 + g 22 + GL
                                                                   β
                                                                                           (
                                                                                         − g 12
                                                                                             α
                                                                                                + g 12
                                                                                                    β
                                                                                                         ) ⎤⎥⎡⎢ i ⎤⎥ = ⎡⎢ v ⎤⎥
                                                                                                                S         1
                                                     β ⎢                                                   ⎥
  (g + g + G )(
   α
   11
         β
         11    S
                   g α22 + g 22
                             β
                                   )
                                + GL − g 21
                                         β
                                            (
                                            g 12
                                              α
                                                 + g 12  )
                                                        ⎢⎣
                                                                    β
                                                                −g 21                    g 11
                                                                                           α
                                                                                              + g 11
                                                                                                  β
                                                                                                     + GS ⎥⎦⎢⎣ 0 ⎥⎦ ⎢⎣ v2 ⎥⎦


                                                           β
                                                        −g 21iS
                      v2 =
                             (g + g + G )(g + g + G ) − g (g + g )
                              α
                              11
                                       β
                                       11   S
                                                   α
                                                   22
                                                             β
                                                             22        L
                                                                               β
                                                                               21
                                                                                    α
                                                                                    12
                                                                                            β
                                                                                            12




        v2                                      g 21
                                                  β
           = Gdiretto = β α
        is                    (
                       g 21 g 12 + g 12
                                     β
                                        − g 11
                                            α
                                                ) (
                                               + g 11
                                                   β
                                                      + GS g α22 + g 22
                                                                     β
                                                                        + GL   )(                        )
   Analisi del secondo trasferimento
   ¨     Impedenza di ingresso
                              ⎡ α                                        ⎤
                        1 ⎢ g 22 + g 22 + GL
                                       β
                                                          (
                                                        − g 12
                                                            α
                                                               + g 12
                                                                   β
                                                                        )          ⎡
                                                                         ⎥⎡ iS ⎤ ⎢ v1 ⎥
                                                                                         ⎤
                              ⎢                                          ⎥⎢     ⎥=
                     det(Gγ ) ⎢ − g α + g β
                                       (           )    g 11 + g 11 + GS ⎥⎢⎣ 0 ⎥⎦ ⎢⎣ v2 ⎥⎦
                                                          α      β
                                    21    21
                              ⎣                                          ⎦

           v1
              =
                (
                g α22 + g 22
                          β
                             + GL)= α
                                                           g α22 + g 22
                                                                     β
                                                                        + GL
           iS         detGγ                (
                                    g 11 + g 11
                                             β
                                                         )(
                                                + GS g α22 + g 22
                                                                β
                                                                  + GL − g 12α
                                                                                 ) (
                                                                               + g 12
                                                                                   β
                                                                                             )(
                                                                                      g α21 + g 21
                                                                                                β
                                                                                                             )
                          g α22 + g 22
                                    β
                                       + GL                                                        1
RIN =
        ( g + g + G ) ( g + g + G ) − ( g + g ) g 1−
          α
          11
               β
               11     S
                           α
                           22
                                  β
                                  22           L
                                                   α
                                                   12
                                                          β
                                                          12
                                                                 β
                                                                 21                         (g + g ) g
                                                                                              α
                                                                                              12
                                                                                                        β
                                                                                                        12
                                                                                                             α
                                                                                                             21

                                                                        (g + g + G )(g + g + G ) − (g + g ) g
                                                                            α
                                                                            11
                                                                                  β
                                                                                  11    S
                                                                                             α
                                                                                             22
                                                                                                       β
                                                                                                       22    L
                                                                                                                  α
                                                                                                                  12
                                                                                                                       β
                                                                                                                       12
                                                                                                                            β
                                                                                                                            21


         Resistenza anello aperto
                                                                                1
                                                               RIN = RINOL
                                                                             1− Gloop
  Ranello aperto nel circuito
       v         v1
RINOL = 1
       iS             g11
                       α
                            g 22
                              α

                 GS
            is                     GL




                       Gβ
Dimostrazione
                                                            v
                                                       RIN = 1
                                                            iS
                       ⎡ i ⎤ ⎡ gα + g β + G                               g 12 + g 12
                                                                                         ⎤⎡      ⎤
                                                                                         ⎥⎢ v1 ⎥
                                                                            α      β
                       ⎢ S ⎥ = ⎢ 11 11     S

                       ⎢⎣ 0 ⎥⎦ ⎢    g β
                                                                      g α22 + g 22
                                                                                β
                                                                                   + GL ⎥⎦⎢⎣ v2 ⎥⎦
                               ⎣      21


                                                       ⎡ α
                         1                             ⎢ g 22 + g 22 + GL
                                                                  β
                                                                                                 (
                                                                                             − g 12
                                                                                                 α
                                                                                                    + g 12
                                                                                                        β
                                                                                                             ) ⎤⎥⎡⎢ i ⎤⎥ = ⎡⎢ v ⎤⎥
                                                                                                                    S         1
                                                    β ⎢                                                       ⎥
  (g + g + G )(
   α
   11
        β
        11   S
                  g α22 + g 22
                            β
                                     )
                               + GL − g 21
                                        β    α
                                              (
                                           g 12 + g 12 ⎢⎣     )    β
                                                               −g 21                        g 11
                                                                                              α
                                                                                                 + g 11
                                                                                                     β
                                                                                                        + GS ⎥⎦⎢⎣ 0 ⎥⎦ ⎢⎣ v2 ⎥⎦



                  v =
                                 (g + g + G )i    α
                                                  22
                                                         β
                                                         22       L   S
                   1
                      (g + g + G )(g + g + G ) − g (g + g )
                          α
                          11
                                β
                                11       S
                                                  α
                                                  22
                                                         β
                                                         22       L
                                                                              β
                                                                              21
                                                                                   α
                                                                                   12
                                                                                            β
                                                                                            12




    v1
       = RINOL = α
                                  g α22 + g 22
                                            β
                                              (+ GL                       )
    is             (
                 g 11 + g 11
                          β                 β
                                             )(
                             + GS g α22 + g 22 + GL − g 21
                                                        β
                                                           g 12
                                                             α
                                                                + g 12
                                                                    β
                                                                          )             (            )
Trasferimento reale
Il trasferimento reale si può scomporre nei seguenti contributi
    di calcolo più immediato


               Gideale   Gdiretto
     Greale =       −1
                       +
              1 − Gloop 1 − Gloop
     Greale: Guadagno reale del trasferimento reazionato
     Gloop:Guadagno d’anello del circuito retroazionato
     Gideale: Guadagno reale del trasferimento se il G è infinito
     Gdiretto: Guadagno reale del trasferimento se il G è nullo
Calcolo del guadagno d’anello
¨   Il guadagno d’anello è il meccanismo che permette di ottenere il guadagno ideale
¨   Il calcolo del guadagno d’anello si ottiene spezzando l’anello in un punto “comodo” e
    calcolando il trasferimento sul circuito ottenuto ai capi del punto di rottura nella
    direzione dell’anello
¨   Si sopprimono gli ingressi (si aprono i generatori di corrente e si cortocircuitano quelli di
    tensione)
¨   Il calcolo si può anche realizzare in simulazione
¨   Questo calcolo è semplice da fare perché lo schema è direzionale



                                     R                  VAC=1          RC >> τ dello schema
                                             VC
      Vin                    Vin      C                  VC               Vout




                              T(s)
 Calcolo del guadagno d’anello

Il punto di rottura più comodo è l’ingresso o l’uscita di
   una generatore comandato ideale altrimenti è
   necessario ricostruire le impedenze modificate dalla
   rottura

                                  Gloop Itest       Itest
                α                               α




                 β                              β
Calcolo del guadagno ideale
¨   Il guadagno ideale è un trasferimento che si ottiene
    facendo tendere a zero la variabile di ingresso della del
    circuito con retroazione, ovvero l’ingresso del blocco α sia
    essa corrente che tensione
Calcolo del guadagno diretto
Questo calcolo si ottiene annullando il guadagno del blocco α e
  calcolando il trasferimento tra ingresso ed uscita:
¨ Questo calcolo può essere realizzato in simulazione inserendo il

  blocco senza generatore di tensione AC utilizzato per il calcolo del
  guadagno d’anello connesso in modo da non perturbare il
  trasferimento diretto del segnale. Il generatore AC necessario per la
  valutazione di questo trasferimento va inserito all’ingresso del
  circuito.
Singolarità del guadagno reale
¨ I poli del guadagno reale sono le soluzioni
  dell’equazione:      1 − Gloop = 0
¨ Tutti i poli del guadagno ideale sono degli zeri del
  guadagno d’anello (non vale il viceversa)
¨ Il guadagno d’anello e il guadagno diretto hanno gli

  stessi poli
Rappresentazione del guadagno reale

¨   Rappresentazione del guadagno reale in
    frequenza:
                                      Greale ≅ Gideale
               − Gloop Gideale        Gloop >> 1
    Greale ≅
                 1 − Gloop
                                     Greale ≅ −GidealeGloop
    − Gloop Gideale
                                      Gloop << 1
                      Gideale
                                 Il modulo del guadagno reale si
      Greale                     traccia tracciando la minima curva tra
                                 il guadagno ideale e il prodotto del
                                 guadagno d’anello per il guadagno
                                 ideale
