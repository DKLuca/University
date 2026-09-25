---
fonte: "4b - Feedbacksystem_ita_2.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

UNIVERSITY OF UDINE

Department DIEG
Via delle scienze 206
33100 Udine (UD), Italy




                      FEEDBACK SYSTEM 2
                      Associate professor Stefano Saggini
                      Lezione di complementi di elettronica
     Retroazione serie serie
     ¨    Accesso ad un ramo della circuito retroazionato
          l’uscita è su un ramo della retrazione
         Effetto della
         retroazione negativa
                                                Transconductance
Intervento

                                Rα
dell’ingresso

                         RS
                                               RL
                 vS
                                                iL Segnale di uscita
                                Rβ
Retroazione serie serie
¨   Calcolo del risultato
               ⎡ R          ⎡ α                                 ⎤
                     0 ⎤ ⎢ r11  + r11
                                   β
                                      + RS      r12
                                                 α
                                                    + r12
                                                       β
                                                                ⎥
Rγ = Rα + Rβ + ⎢ S       ⎥=
               ⎢ 0
               ⎣     RL ⎥⎦ ⎢ r α21 + r 21
                                       β
                                             r α22 + r 22
                                                       β
                                                          + RL ⎥⎦
                            ⎣

                                         ⎡ v ⎤      ⎡ i ⎤
                                         ⎢ S ⎥ = Rγ ⎢ 1 ⎥
         i1                  i2          ⎢⎣ 0 ⎥⎦    ⎢ i ⎥
                                                    ⎣ 2 ⎦
    vs
                 Rγ
                                             ⎡ v ⎤ ⎡ i ⎤
                                         Rγ−1⎢ S ⎥ = ⎢ 1 ⎥
                                             ⎢⎣ 0 ⎥⎦ ⎢⎣ i2 ⎥⎦
Retroazione serie serie
¨   Soluzione
                    ⎡ α
              1 ⎢ r 22 + r 22 + RL
                             β
                                      (
                                     − r12
                                        α
                                           + r12
                                              β
                                                   ) ⎤⎥⎡⎢ v ⎤⎥ = ⎡⎢ i ⎤⎥
                                                          S         1
                    ⎢                               ⎥
           det(Rγ ) ⎢ − r α + r β
                       (        )    r11
                                      α
                                         + r11
                                            β
                                               + rS ⎥⎢⎣ 0 ⎥⎦ ⎢⎣ i2 ⎥⎦
                          21    21
                    ⎣                               ⎦


¨   Analisi del primo trasferimento                               Termine dominante GD
                                                                    Termine parassita GP



               =
                   (       )
            i2 − r 21 + r 21
                  α       β

                             =
                                −r α21
                                       +
                                            β
                                         −r 21
            vS   det Rγ        det Rγ det Rγ
      Trasferimento
                                                         Termine
      ¨    Trasferimento                                 dominante GD
                                                                                                                 Termine parassita GP


                                        =
                                               (
                                     i2 − r 21 + r 21
                                           α       β

                                                      =
                                                         −r α21)+
                                                                     β
                                                                  −r 21
                                     vS   det Rγ        det Rγ det Rγ

                                                                                                                                    ⎡ R    ≅0 ⎤
                                                Gideale   Gdiretto
                                      Greale =       −1
                                                        +                                                                      Rα = ⎢ in
                                                                                                                                    ⎢ R
                                                                                                                                                 ⎥
                                               1 − Gloop 1 − Gloop                                                                  ⎣      Rout ⎥⎦



                                                              −R                                            1             1
Gideale = lim GD = lim                                                                           =                   ≅
        R→−∞           R→−∞
                              (r + r + R ) (r + r + R ) − (r + r ) ( R + r ) (r + r )
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
                                                                                            β
                                                                                            21
                                                                                                       α
                                                                                                       12
                                                                                                                β
                                                                                                                12
                                                                                                                         r12
                                                                                                                          β




                                               1                                              1
  GD = Gideale                                                                  = Gideale
                 1+
                        β
                         (
                      r 21 r12
                            α
                               + r12
                                  β
                                    ) (
                                     − r11
                                        α
                                           + r11
                                              β
                                                  )(
                                                 + RS r α22 + r 22
                                                                β
                                                                   + RL     )               1− Gloop
                                                                                                −1



                                       (r + r ) r
                                          α
                                          12
                                                   β
                                                   12
                                                        α
                                                        21
Gideale nel circuito
                                               i2

                                                              i2
                   v1 = 0                           Gideale =
  RS
                   i1 = 0                                     vS
                            v2 non vincolata
                            i2 non vincolata

                                                    RL
 vs

             r11
              β
                            r12
                             β
                                i2
Gloop nel circuito
                                                       r α22

                                   r α21i1

                      r11
                       α

    RS




                                      Rβ

         Gloop =
                                      (
                                   − r12
                                      α
                                         + r12
                                            β
                                               )
                                               r α21
                     β
                      (
                   r 21 r12
                         α     β
                                ) (
                            + r12 − r11
                                     α
                                        + r11
                                           β
                                                   )(
                                              + RS r α22 + r 22
                                                             β
                                                                + RL   )
Analisi del secondo termine
¨   Analisi del secondo termine
                            Guadagno diretto

                                      r 21
                                        β
                                                                          1
      GP =     β
                (
             r 21 r12
                   α
                      + r12
                         β
                            ) (
                            − r11
                               α
                                  + r11
                                     β
                                        + RS    )(   r α22 + r 22
                                                               β
                                                                  + RL 1− Gloop
                                                                    )

                                             r 21
                                               β
        Gdiretto =     β
                        (
                     r 21 r12
                           α     β
                                  ) (
                              + r12 − r11
                                       α
                                          + r11
                                             β
                                                         )(
                                                + RS r α22 + r 22
                                                               β
                                                                  + RL    )

                                                1
                            GP = Gdiretto
                                             1− Gloop
Gdiretto nel circuito
                               i2
                                                    i2
                                         Gdiretto =
                                                    vS
                 r11α   r22α
   RS


                                    RL
  vs

                    Rβ
Analisi del secondo trasferimento
¨   Impedenza di ingresso
                            ⎡ α                                           ⎤
                      1 ⎢ r 22 + r 22 + RL
                                     β
                                                             (
                                                           − r12
                                                              α
                                                                 + r12
                                                                    β
                                                                         )          ⎡
                                                                          ⎥⎡ vS ⎤ ⎢ i1 ⎥
                                                                                          ⎤
                            ⎢                                             ⎥⎢     ⎥=
                   det(Rγ ) ⎢ − r α + r β
                                      (           )        r11 + r11 + RS ⎥⎢⎣ 0 ⎥⎦ ⎢⎣ i2 ⎥⎦
                                                            α     β
                                  21    21
                            ⎣                                             ⎦

          i1
             =
               (
               r α22 + r 22
                         β
                            + RL )
                                 = α
                                                        r α22 + r 22
                                                                  β
                                                                     + RL
          vS         det Rγ               (
                                   r11 + r11
                                          β
                                                             )(
                                             + RS r α22 + r 22
                                                             β
                                                               + RL − r12 α
                                                                            + r12
                                                                               β
                                                                                  ) (
                                                                                  r α21 + r 21
                                                                                            β
                                                                                              )(             )
                         r α22 + r 22
                                   β
                                      + RL                                                         1
GIN =
        (r + r + R ) (r + r + R ) − (r + r ) r 1−
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
                                                                  21                         (r + r ) r
                                                                                              α
                                                                                              12
                                                                                                        β
                                                                                                        12
                                                                                                             α
                                                                                                             21

                                                                         (r + r + R ) (r + r + R ) − (r + r ) r
                                                                             α
                                                                             11
                                                                                  β
                                                                                  11     S
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



  Conduttanza anello aperto
                                                                                 1
                                                             GIN = GINOL
                                                                              1− Gloop
  Ganello aperto nel circuito
                  i1                 i2

        i1
GINOL =                r11α   r22α
        vS
             RS


                                          RL
         vs

                          Rβ
Retroazione parallelo serie
¨   Accesso ad un nodo del circuito retroazionato
    l’uscita è su un ramo della retrazione

                                               Amplificazione di
    is       GS
                      Hαʹ
                                               corrente




                                          RL


                                         iL Segnale di uscita
                       H βʹ
       Retroazione parallelo parallelo
       ¨   Calcolo del risultato
                        ⎡ G          ⎡                                       ⎤
                              0 ⎤ ⎢ hʹ11α + hʹ11β + GS        hʹ12α + hʹ12β  ⎥
     Hγʹ = Hαʹ + H βʹ + ⎢ S       ⎥=
                        ⎢ 0
                        ⎣     RL ⎥⎦ ⎢ hʹ21α + hʹ21β        hα22 + h 22
                                                                    β
                                                                       + RL ⎥⎦
                                     ⎣
                                                    ⎡ i ⎤       ⎡ v ⎤
                                                    ⎢ S ⎥ = Hγʹ ⎢ 1 ⎥
                                           i2       ⎢⎣ 0 ⎥⎦     ⎢ i ⎥
                                                                ⎣ 2 ⎦
is           v1          Hγʹ
                                                               ⎡ i ⎤ ⎡ v ⎤
                                                         H ʹγ−1⎢ S ⎥ = ⎢ 1 ⎥
                                                               ⎢⎣ 0 ⎥⎦ ⎢⎣ i2 ⎥⎦
Retroazione parallelo serie
¨   Soluzione
                     ⎡ α
             1 ⎢ hʹ22 + hʹ22 + RL
                             β
                                                  (
                                                − hʹ12α + hʹ12β   ) ⎤⎥⎡⎢ i ⎤⎥ = ⎡⎢ v ⎤⎥
                                                                         S         1
                     ⎢                                             ⎥
          det( Hγʹ ) ⎢ − hʹα + hʹβ
                           (           )        hʹ11α + hʹ11β + GS ⎥⎢⎣ 0 ⎥⎦ ⎢⎣ i2 ⎥⎦
                          21    21
                     ⎣                                             ⎦


¨   Analisi del primo trasferimento                                             Termine dominante AID



                                                                             Termine parassita AIP
              =
                  (
           i2 − hʹ + hʹ
                       α
                      21
                                β
                               21   ) = −hʹ + −hʹ
                                            α
                                           21
                                                           β
                                                          21
           iS   det Hγʹ               det Hγʹ         det Hγʹ
Trasferimento
                                               Termine
¨   Trasferimento                              dominante AID
                                                                                                    Termine parassita AIP


                             =
                                     (
                          i2 − hʹ21 + hʹ21
                                  α      β

                                           =
                                                   )
                                              −hʹ21α
                                                     +
                                                       −hʹ21β
                          iS   det Hγʹ       det Hγʹ det Hγʹ

                                                                                                                ⎡ 1                       ⎤
                                     Gideale   Gdiretto                                                         ⎢                   ≅0 ⎥
                           Greale =       −1
                                             +                                                             Hα = ⎢
                                                                                                            ʹ       Rin
                                                                                                                                          ⎥
                                    1 − Gloop 1 − Gloop                                                         ⎢ AV                Rout ⎥⎦
                                                                                                                ⎣

                                                                 −AV                                           1             1
Gideale = lim AID = lim                                                                              =                  ≅
        AV →−∞       AV →−∞
                              (hʹ + hʹ + G ) (hʹ + hʹ + R ) − (hʹ + hʹ ) ( A + hʹ ) (hʹ + hʹ )
                                 α
                                11
                                          β
                                         11    S
                                                        α
                                                       22
                                                                 β
                                                                22     L
                                                                             α
                                                                            12
                                                                                  β
                                                                                 12   V
                                                                                                β
                                                                                               21
                                                                                                           α
                                                                                                          12
                                                                                                                    β
                                                                                                                   12
                                                                                                                            hʹ12β


                                                            1                                               1
      GD = Gideale                                                                            = Gideale
                     1+
                               (              ) (              )(
                          hʹ21β hʹ12α + hʹ12β − hʹ11α + hʹ11β + GS hʹ22α + hʹ22β + RL     )               1− Gloop
                                                                                                              −1



                                                 (hʹ + hʹ ) hʹ
                                                        α
                                                       12
                                                                  β
                                                                 12
                                                                        α
                                                                       21
Gideale nel circuito
         v1                                   i2

                                                              i2
  iS
        GS            v1 = 0
                      i1 = 0
                                                    Gideale =
                                                              iS
                           v2 non vincolata
                           i2 non vincolata


                                                   RL


              hʹ11β     hʹ12βi2
Gloop nel circuito
                                                             h22
                                                              ʹα



       GS                h11ʹα




                                                                                   RL


                                           H βʹ

       Gloop =
                                       (            )
                                     − hʹ12α + hʹ12β hʹ21α

                     (           ) (                    )(
                 hʹ21β hʹ12α + hʹ12β − hʹ11α + hʹ11β + GS hʹ22α + hʹ22β + RL   )
Analisi del secondo termine
¨   Analisi del secondo termine
                               Guadagno diretto

                                           hʹ21β                                    1
      AIP =
                  (            ) (
              hʹ21β hʹ12α + hʹ12β − hʹ11α + hʹ11β + GS   )(   hʹ22α + hʹ22β + RL 1− Gloop
                                                                              )

                                                   hʹ21β
        Gdiretto =
                          (           ) (                        )(
                      hʹ21β hʹ12α + hʹ12β − hʹ11α + hʹ11β + GS hʹ22α + hʹ22β + RL   )

                                                       1
                                GP = Gdiretto
                                                    1− Gloop
Gdiretto nel circuito
                                i2
                                                     i
                                          Gdiretto = 2
                                                    iS
    iS    GS      h11ʹα   h22
                           ʹα




                                     RL


                     H βʹ
   Analisi del secondo trasferimento
   ¨     Impedenza di ingresso
                                     ⎡ α
                             1 ⎢ hʹ22 + hʹ22 + RL
                                             β
                                                              (
                                                         − hʹ12α + hʹ12β   ) ⎤⎥⎡⎢ i ⎤⎥ = ⎡⎢ v ⎤⎥
                                                                                    S           1
                                     ⎢                                      ⎥
                          det( Hγʹ ) ⎢ − hʹα + hʹβ
                                            (        )   hʹ11α + hʹ11β + GS ⎥⎢⎣ 0 ⎥⎦ ⎢⎣ i2 ⎥⎦
                                          21    21
                                     ⎣                                      ⎦


                  =
                      (
               v1 hʹ22 + hʹ22 + RL
                          α     β

                                   = α
                                        )                   hʹ22α + hʹ22β + RL
               iS      det Hγʹ                  (             )(                   ) (               )(
                                    hʹ11 + hʹ11β + GS hʹ22α + hʹ22β + RL − hʹ12α + hʹ12β hʹ21α + hʹ21β                  )

                              hʹ22α + hʹ22β + RL                                                         1
RIN =
        (hʹ + hʹ + G ) (hʹ + hʹ + R ) − (hʹ + hʹ ) hʹ 1−
           α
          11
                  β
                 11       S
                                α
                               22
                                       β
                                      22        L
                                                     α
                                                    12
                                                          β
                                                         12
                                                                    β
                                                                   21                          (hʹ + hʹ ) hʹ
                                                                                                     α
                                                                                                    12
                                                                                                               β
                                                                                                              12
                                                                                                                    α
                                                                                                                   21

                                                                        (hʹ + hʹ + G ) (hʹ + hʹ + R ) − (hʹ + hʹ ) hʹ
                                                                            α
                                                                           11
                                                                                    β
                                                                                   11      S
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
Ganello aperto nel circuito
       v          v1                 i2
RINOL = 1
       iS

        iS   GS        h11ʹα   h22
                                ʹα




                                          RL


                          H βʹ
Retroazione serie parallelo
¨    Accesso ad un nodo del circuito retroazionato
     l’uscita è su un ramo della retrazione
                                               Segnale di uscita
                                          vL

                                     GL

    RS                 Hαʹʹ                     Amplificazione di
                                                tensione



    vS



                        H βʹʹ
     Retroazione parallelo parallelo
     ¨   Calcolo del risultato
                      ⎡ R          ⎡                                             ⎤
                            0 ⎤ ⎢ hʹʹ11α + hʹʹ11β + RS        hʹʹ12α + hʹʹ12β    ⎥
Hγʹʹ = Hαʹʹ + H βʹʹ + ⎢ S       ⎥=
                      ⎢ 0
                      ⎣     GL ⎥⎦ ⎢ hʹʹ21α + hʹʹ21β        hʹʹ22α + hʹʹ22β + GL ⎥⎦
                                   ⎣
                                                         ⎡ v ⎤       ⎡ i ⎤
               i1                              v2        ⎢ S ⎥ = Hγʹʹ⎢ 1 ⎥
                                                         ⎢⎣ 0 ⎥⎦     ⎢ v ⎥
                                                                     ⎣ 2 ⎦
vS
                            Hγʹ
                                                                 ⎡ v ⎤ ⎡ i ⎤
                                                         H ʹʹγ −1⎢ S ⎥ = ⎢ 1 ⎥
                                                                 ⎢⎣ 0 ⎥⎦ ⎢⎣ v2 ⎥⎦
Retroazione parallelo serie
¨   Soluzione
                     ⎡ α
             1 ⎢ hʹʹ22 + hʹʹ22 + GL
                               β
                                               (             ) ⎤⎥⎡⎢ v ⎤⎥ = ⎡⎢ i ⎤⎥
                                             − hʹʹ12α + hʹʹ12β
                                                                    S         1
                     ⎢                                            ⎥
          det( Hγʹʹ) ⎢ − hʹʹα + hʹʹβ
                            (            )   hʹʹ11α + hʹʹ11β + RS ⎥⎢⎣ 0 ⎥⎦ ⎢⎣ v2 ⎥⎦
                          21     21
                     ⎣                                            ⎦


¨   Analisi del primo trasferimento                                        Termine dominante AVD



                                                                        Termine parassita AVP
               =
                   (
            v2 − hʹʹ + hʹʹ
                        α
                       21
                           =
                                 β
                              −hʹʹ21α
                                21   )+
                                        −hʹʹ21β
            vS   det Hγʹʹ    det Hγʹʹ det Hγʹʹ
Trasferimento
                                                Termine
¨   Trasferimento                               dominante AVD
                                                                                                          Termine parassita AVP


                            =
                                      (
                         v2 − hʹʹ21 + hʹʹ21
                                  α       β

                                            =
                                                   )
                                               −hʹʹ21α
                                                       +
                                                         −hʹʹ21β
                         vS   det Hγʹʹ        det Hγʹʹ det Hγʹʹ

                                                                                                                        ⎡ R                      ⎤
                                      Gideale   Gdiretto                                                                ⎢ in
                                                                                                                                         ≅0
                                                                                                                                                 ⎥
                            Greale =          +                                                                  Hαʹʹ = ⎢
                                           −1
                                     1 − Gloop 1 − Gloop                                                                  A              1       ⎥
                                                                                                                        ⎢ I
                                                                                                                        ⎣                  Rout ⎥⎦


                                                                  −AI                                                1           1
Gideale = lim AVD = lim                                                                                 =                   ≅
        AI →−∞        AI →−∞
                               (hʹʹ + hʹʹ + R ) (hʹʹ + hʹʹ + G ) − (hʹʹ + hʹʹ ) ( A + hʹʹ ) (hʹʹ + hʹʹ )
                                  α
                                 11
                                           β
                                          11   S
                                                        α
                                                       22
                                                                  β
                                                                 22     L
                                                                              α
                                                                             12
                                                                                    β
                                                                                   12      I
                                                                                                      β
                                                                                                     21
                                                                                                                 α
                                                                                                                12
                                                                                                                          β
                                                                                                                         12
                                                                                                                                hʹʹ12β


                                                             1                                                    1
      AVD = Gideale                                                                                 = Gideale
                      1+
                                 (             ) (                 )(
                           hʹʹ21β hʹʹ12α + hʹʹ12β − hʹʹ11α + hʹʹ11β + RS hʹʹ22α + hʹʹ22β + GL   )               1− Gloop
                                                                                                                    −1



                                                  (hʹʹ + hʹʹ ) hʹʹ
                                                         α
                                                        12
                                                                   β
                                                                  12
                                                                         α
                                                                        21
Gideale nel circuito
                                      v2

                v1 = 0
                                             GL
                i1 = 0
  RS               v2 non vincolata
                   i2 non vincolata




  vS


                    hʹʹ12β v2                        v2
                                           Gideale =
                                                     vS
Gloop nel circuito

                                                                       h22
                                                                        ʹʹα
                            h11ʹʹα                                                      GL
    RS




                                                H βʹʹ

         Gloop =
                                            (             )
                                         − hʹʹ12α + hʹʹ12β hʹʹ21α

                       (             ) (                       )(
                   hʹʹ21β hʹʹ12α + hʹʹ12β − hʹʹ11α + hʹʹ11β + RS hʹʹ22α + hʹʹ22β + GL   )
Analisi del secondo termine
¨   Analisi del secondo termine
                                 Guadagno diretto

                                               hʹʹ21β                                      1
      AVP =
                   (             ) (
              hʹʹ21β hʹʹ12α + hʹʹ12β − hʹʹ11α + hʹʹ11β + RS   )(   hʹʹ22α + hʹʹ22β + GL 1− Gloop
                                                                                    )

                                                        hʹʹ21β
        Gdiretto =
                           (             ) (                           )(
                       hʹʹ21β hʹʹ12α + hʹʹ12β − hʹʹ11α + hʹʹ11β + RS hʹʹ22α + hʹʹ22β + GL   )

                                                           1
                                AVP = Gdiretto
                                                        1− Gloop
Gdiretto nel circuito

                                 v2
                                                      v2
                                           Gdiretto =
                 h11ʹʹα   h22
                           ʹʹα        GL              vS
   RS



  vs


                    H βʹʹ
  Analisi del secondo trasferimento
  ¨     Impedenza di ingresso
                                        ⎡ α
                                1 ⎢ hʹʹ22 + hʹʹ22 + GL
                                                  β
                                                                        (           ) ⎤⎥⎡⎢ v ⎤⎥ = ⎡⎢ i ⎤⎥
                                                                    − hʹʹ12α + hʹʹ12β
                                                                                                 S          1
                                        ⎢                                                ⎥
                             det( Hγʹʹ) ⎢ − hʹʹα + hʹʹβ
                                                  (            )    hʹʹ11α + hʹʹ11β + RS ⎥⎢⎣ 0 ⎥⎦ ⎢⎣ v2 ⎥⎦
                                             21     21
                                        ⎣                                                ⎦


           i1
              =
                 (
                hʹʹ22 + hʹʹ22 + GL
                     α         β

                                   = α
                                        )                      hʹʹ22α + hʹʹ22β + GL
           vS         det Hγʹʹ                (                    )(                      ) (             )(
                                    hʹʹ11 + hʹʹ11β + RS hʹʹ22α + hʹʹ22β + GL − hʹʹ12α + hʹʹ12β hʹʹ21α + hʹʹ21β            )
                               hʹʹ22α + hʹʹ22β + GL                                                             1
GIN =
        (hʹʹ + hʹʹ + R ) (hʹʹ + hʹʹ + G ) − (hʹʹ + hʹʹ ) hʹʹ 1−
           α
          11
                 β
                11       S
                                 α
                                22
                                         β
                                        22            L
                                                           α
                                                          12
                                                                    β
                                                                   12
                                                                             β
                                                                            21                           (hʹʹ + hʹʹ ) hʹʹ
                                                                                                            α
                                                                                                           12
                                                                                                                      β
                                                                                                                     12
                                                                                                                           α
                                                                                                                          21

                                                                                 (hʹʹ + hʹʹ + R ) (hʹʹ + hʹʹ + G ) − (hʹʹ + hʹʹ ) hʹʹ
                                                                                     α
                                                                                    11
                                                                                             β
                                                                                            11       S
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



   Conduttanza anello aperto
                                                                                           1
                                                                    GIN = GINOL
                                                                                        1− Gloop
  GIN ad anello aperto nel circuito
                  i1

        i1
GINOL =
        vS             h11ʹʹα   h22
                                 ʹʹα   GL
             RS



         vs


                           H βʹʹ
Generazione delle varie combinazioni
sullo stesso circuito
        +               +

        -               -




                      INPUT PARALLEL
      INPUT SERIES



        +               +

        -               -          RL




     OUTPUT     RL     OUTPUT
     PARALLEL          SERIES
