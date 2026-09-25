---
fonte: "Opam_characteristics.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

UNIVERSITY OF UDINE

Department DIEG
Via delle scienze 206
33100 Udine (UD), Italy




                      CHARCATERISTICS OF
                      OPERATIONAL AMPLIFIERS
                      Assistant professor Stefano Saggini
                      Nome della conferenza o seminario
Different types of Operational
amplifiers
¨ Voltage mode operational amplifier
¨ Current feedback

¨ Norton operational amplifier
OPAMP general Characteristics
¨   Polarization and/or large signal
    ¤ Input common mode range ICMR
    ¤ Output voltage swing Voutmax Voutmin
    ¤ Maximum output current
    ¤ Input bias current
    ¤ Slew rate SR
¨   AC characteristics
    ¤   Input impedance
    ¤ DC Gain Av(0)
    ¤ Output impedance
    ¤ Gain band product
    ¤ CMRR
    ¤ PSRR
    ¤ Input equivalent noise
¨   Mismatch non idealities
    ¤   Input offset Voffset
    ¤   Input current mismatch
     Polarization and/or large signal
     ¨ Input common mode range ICMR
     ¨ Output voltage swing Voutmax Voutmin
         VinCM=(Vin++Vin-)/2
                                                             Vs+
     VinCMmin
                                                                                                Voutmax

                                       Vin+          +                   Iout
                                                                                 Vout
                                       Vin-           -
       VinCMmax
                                                                                                  Voutmin
                                                                   Vs-
Se VinCM è nel range (VinCMmin, VinCMmax ), se Vout è nel range (Voutmin, Voutmax ) e se la corrente di
uscita Iout è nel range (Ioutmin , Ioutmax ) dove Ioutmin è la massima corrente entrante (Massimo sinking) e
Ioutmax è la massima corrente uscente (Massimo sourcing).

L’amplificatore operazionale è polarizzato correttamente e può essere studiato con il suo modello di piccolo segnale.
AC linear model Small Signal
¨ Input impedance differential
¨ Output impedance

¨ Gain transfer function (GBWP)

¨ CMRR

¨ PSRR
Scheme

                  vSP

         2ZinCM

        vD
         2


                        ZinD    Z out

  vCM
        vD                                 ⎛                                     ⎞
                                                     vCM     vSP        vSM
         2                     vout = A(s) ⎜ v D +        +          +           ⎟
                                           ⎝       CMRR(s) PSRR p (s) PSRR m (s) ⎠
         2ZinCM




                  vSM
Gain transfer function
¨     Transfer function
       vOUT
            = AV (s)
        vD                                               AV (0)
                                        AV (s) =
                                                   (1+ sτ L )(1+ sτ H )



AV ( j2π f )                              GBWP = AV (0) f L
               db
                    AV (0)
                             db




                                                     fH

                                  fL   GBWP                        f
       Example CMRR
       ¨   Considering CMRR in the transfer function
                                                           Gideale
                                                                                1
           vOUT   G
                = ideale                     v +v                    vout 1+ 2CMRR
                                 vin − vout + in out = 0                 =
            v IN 1− Gloop
                      −1
                                             2CMRR                   vin        1
                                                                           1−
                                                                              2CMRR

                       ⎛                                             1           1
                             1 ⎞                    vout − vin 1+ 2CMRR
                    AV ⎜1+                                                              1
  vOUT   Gideale       ⎝ 2CMRR ⎠
                                ⎟                             =          −1 = CMRR ≅
       =         =                                     vin           1             1  CMRR
                                                                1−           1−
   v IN 1− Gloop
              −1         ⎛    1 ⎞                                  2CMRR        2CMRR
                   1+ AV ⎜1−      ⎟
                         ⎝ 2CMRR ⎠
                                                       Gloop

                      +
                                                                 +
v IN                                                                                  ⎛
                                                                          Gloop = −AV ⎜1−
                                                                                          1 ⎞
                                                                                              ⎟
                      -                                          -
                                                                                      ⎝ 2CMRR ⎠
Example PSRR
¨   Signal noise on vdd
                         vout   0      Gdirect   Gdirect     1
                              =      +         ≅         ≡
                  VDD    vSP 1− Gloop 1− Gloop
                                  −1
                                                  AV       PSRR+
            vSP


            +
                              VOut

            -


                        VSS
Equivalent circuit
¨   Equivalent circuit



                         +
           vSP
         PSRR+
                         -
          vSM
         PSRR−


          vCM
         CMRR
Effetto di offset e bias
¨   Circuito equivalente


               ibias

                                  +

     vOFFSET             Δibias

                                  -

                 ibias
Limitazioni di grande segnale
¨   Limitazione dovuta alla SR considerando un segnale
    sinusoidale di uscita di ampiezza A e frequenza ω


                 Aω < SR

¨   Limitazione dovuta alla Iout sulla massima derivata
    di uscita
                     I out
                Aω <
                     CL
