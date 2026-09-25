---
fonte: "7 - Design_Opamp.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

UNIVERSITY OF UDINE

Department DIEG
Via delle scienze 206
33100 Udine (UD), Italy




                      DESIGN OF OPAMPS
                      Assistant professor Stefano Saggini
                      Nome della conferenza o seminario
OPAMP general Specifications
¨   DC Gain Av(0)
    ¤ Also the (depend on the application) CMRR

¨ Gain band product
¨ Input offset Voffset

¨ Input common mode range ICMR

¨ Output capacitance CL

¨ Slew rate SR

¨ Output voltage swing Voutmax Voutmin

¨ Consumption Pdiss

¨ Input equivalent noise
Two stage OPAMP design Steps
¨ Depending on the                   Vdd

  ICMR spec choice of           M5          M6              M7

  the n-ch differential
  stage or the p-ch                                    Cc



¨ Determination of the
  Vov of M5 and M6 for    V-                      V+        Vout

  the Max ICMR                 M3           M4



¨ Determination of the                Id1                    Id2


  Vov of M1,2,3,4 Min          Vg    M1           Vg        M2


  ICMR                                      Vss
Two stage OPAMP design Steps
¨   The Input offset                    Vdd

    determine the                  M5          M6              M7


    dimension of the stage
                                                          Cc




                             V-                      V+        Vout
                                  M3           M4



                                         Id1                    Id2


                                  Vg    M1           Vg        M2


                                               Vss
Two stage OPAMP design Steps
¨ The Gain bandwidth                   Vdd

  product and the phase           M5          M6              M7


  margin in follower is a
                                                         Cc
  function of
¨ The slew rate is
                                                              Vout
  function of               V-
                                 M3           M4
                                                    V+




                                        Id1                    Id2


                                 Vg    M1           Vg        M2


                                              Vss
    Project of two stage OpAmp
    ¨    Determination of the capacitor Cc
        gm3, 4
GB @                                                       Considering the ratio
         CC                                                0.1
                         -1
p1 @
     æ ro 7 ro 2 ö          æ r r ö                        gm7 > 10 gm3, 4
     çç             ÷÷ gm7 çç o 6 o 4 ÷÷CC
      è ro 7 + ro 2 ø       è ro 6 + ro 4 ø
       - gm7
p2 @
        CL
     gm7                                                  p2 > 2.2 GB
z1 =
     CC
                                                          gm7       gm3, 4
                æ GB ö       -1 æ GB ö       -1 æ GB ö
                                                              > 2.2
60 < 180 - tan çç -1
                     ÷÷ - tan çç     ÷÷ - tan çç     ÷÷   CL         CC
                è p1 ø          è p2 ø          è z1 ø
                                                          CC > 0.22 C L
Project of two stage OpAmp
¨   Determination of gm3,4

              gm3,4 ≅ GB CC
¨   From slew rate can be determined the Id1

               I d1 = SRCc

¨   From the two information can be calculated the
    Vov3,4
                      2 ID   I d1
             Vov3,4 =      =
                      gm3,4 gm3,4
Project of two stage OpAmp
¨   Determination of the ratio of 3,4
                             !I $
                           2 # d1 &
               !W $          " 2 %
               # & =                  2
               " L %3,4 K ' (Vov *
                          n)     3,4 +




¨   As a function of the ICMR max the (W/L)5,6 is
    determined
                                     !I $
                                   2 # d1 &
          !W $                       " 2 %
          # & =                                       2
          " L %5,6 K ' )V −V (max) − V (max) +V (min)+
                     p * DD in        T5       T3    ,
  Project of two stage OpAmp
  ¨   As a function of the offset we will determines the
      values of Area
                                                       Minimum area required


                             $ '! σ $ ! σ I $2 *
                              2         2
          2
σ Vos = σ Vtp3,4
                    !V
                 + ## OV3,4 && )## Kp && + ## D && ,
                                )
                    " 2 % (" k p %3,4 " I D %5,6 +
                                                   ,                           W3,4,5,6

                            2           2

                                                                               L3,4,5,6
   !σ I $           ! σ $ ! 2σ        $
   ## D && =        # Kp & + # VTp5,6 &
                    # k & # V         &
    " I D %5,6      " p %5,6 " OV5,6 %
Project of two stage OpAmp
¨   As a function of the ICMR min the (W/L)1 is
    determined

          Vin min = Vov1 +Vov3,4 +VT max




              !W $
              # & =
                           ( )
                       2 I d1
                                2
              " L %1 K ' (Vov *
                       n)     1+
Project of two stage OpAmp
¨   Considering the trasconductance relation
                    gm7 > 10 gm3, 4

¨   Considering                       !W $      10 gm3,4
                                      # & >
                                      " L %7 K P Vov5,6
                                                   ! W $ ! W $ Id1
                                      Id7 = Id 2 = # & / # &
    Vov5,6 = Vov7                                  " L %7 " L %5,6 2

                                         ! W $ ! W $ Id 2
                                         # & =# &
                                         " L %2 " L %1 Id1
      Output stage
      ¨   Obviously a buffer output stage reduce Cc
                   Vdd

            Cgd
C’L                      1/gm                  C’L<CL
            Cgs            Vout

                                        Condition to be imposed
                            CL
           Vbias
                                              1       gmout
                                       p3 ≅         =       > 10GB
                                            RoutC L    CL
                   Vss
Output stage
¨   Output stage

                   Cc
                             Cc

                   1              1

                        CL
Inserting a zero on the loop transfer
function
¨   Inserting the zero in the transfer function


       Second Stage of the OpAmp

             R
                      Rd

       Cc                                    1
                                   z1 =
                                         (
                                        CC 1 gm − R   )
Inserting a zero on the loop transfer
function
¨   Controlling the right half-plane zero



                 gm2


                                                  1
                                       z1 = −
                          Cc
                                               (
                                              CC 1 gm2   )
Compensation that increase p2
¨   The feedback gain reduce the output impedance of
    the structure         VDD


                           Cc



                    M8     VB    VOUT




                                M7
Compensation that increase p2
¨   At high frequency
                   VDD


                      Cc
                                              −gm7 gm8 Rdstot
                                       p2 ≅
                                                   CL
        M8
                          VB    VOUT



                                        CL

                               M7
                 Rdstot
  PSRR: Substrate noise coupling
  ¨   Vdd and Gnd bounce
                                 DC-DC converter    Analog Circuit
           Logic circuit well    well     Vin


GND




      P+
              Nwell                 Nwell          Nwell




                          Psub
  PSRR: Substrate noise coupling Analysis

  ¨   For each point can be defined a T(s)
                      GND                                   T(s)
                      external                 Vin(s)                   Vdd(s)



                         MIM
             Vdd(s)      internal
                                    GND
GND                                                            Vin(s)
                                    internal
                                                   Source of Noise
      P+
             Nwell                                Nwell




                                    Psub
PSRR:Substrate noise coupling Analysis

¨   For each sensitive point and each noise source can
    be defined a T(s)


               T1P
    S1
                                              |T(ω)|

         T2P    P
    S2




                                                       ω
PSRR
¨   Definition

                              Vout   0        Gdirect   Gdirect     1
                 VDD               =       +          ≅         ≡
                              Vdd 1− Gloop
                                       −1
                                             1− Gloop    AV       PSRR+
                        Vdd
             +
                               VOut

             -


                       VSS
PSRR
¨   Calculation
                                      ro2          (1+ sτ z )
                       Gdiretto =
                                  (ro7 + ro2 ) (1+ sτ 1 )(1+ sτ 2 )

                  M7
                                       1        z1 =
                                                           ro2
                                                                   p
                                                       (ro7 + ro2 ) 1




M1                M2
                             z1   p1       p2
PSRR close loop
¨   Calculation close loop
                                   vdd 1− Gloop
                            PSRR =+
                                        =
              VDD                  vout   Gdirect

                                                             AV (0)                   A (0)
                                               PSRR+ (0) =          (g ds7 + g ds2 ) = V    (ro7 + ro2 )
                     Vdd                                      g ds7                    ro2

         +
                           VOut

          -


                    VSS


                                                                     GB        p2
PSRR
¨ Non Linear effect of the OpAmp as Asymmetrical
  slew rate can rectify the noise
¨ This effect are studied by AC simulations




            VDD




            VOut
Low Noise design
¨   The PMOS have about 2 to 5 less 1/f noise than n
    ¤ Design a PMOS input stage

¨   Make the first gain stage as high as possible
    ¤ Cascode structure to increase the low frequency gain of
      the opamp
P-ch Folded cascode input schematic

¨    Increase the Input common mode range
          Vdd               Vdd                             Vdd


                Iref              Iref                            I1std




                                                    I1std /2      I1std /2


4*(W/L)
                                                                                    I1std /2   I1std /2
                                (W/L)
4*(W/L)         VT+Vov
                                                                                       (W/L)*I1std /(2 Iref )
    Vov                                             I1std           I1std
                                                             Vov
                                                                             4*(W/L)*I1std / Iref
                       VT+Vov            VT+2*Vov


          Polarizzation
  Input rail to rail
                   Vdd



       IB1
                               GM


                         VB

                         OUT        Correction
INP
             INM
                   VB                            VICM



       IB2
                   Vss
             Output rail to rail

                      Vdd                                                         Vdd


                            I1std
                                             M7                           M8            M9        M12    M13

                                                                                                          OUT
        M1                               M2
    +                                          -
              I1std /2      I1std /2
                                                                                             CC     R
                                       Vpol2                              Vpol2
                                                    I1std /2   I1std /2
                                        M6                                M5


        M3                                 M4
Vpol1         I1std           I1std                Vpol1                                                 M14
                       Vov
                                                                                  M10              M11
Current feedback
                              Vdd


                                    (25/1)                      (25/1)
                100µ




                                             (10/1)


 In+                                            In-                                Vout
                           (25/1)                                             X1

       (10/1)
                                              (25/1)


                                                                      Ccomp


                 100µ
                                    (10/1)                      (10/1)

                               gnd

                 µnCox = 200µA/V2                      µpCox = 80µA/V2
                       VTn = 0.6V                       |VTp|= 0.6V
µ741
Input stage
              ¨   Input stage npn higher !
              ¨ Gain gm/4 of
                differential stage gain
                final gm/2
              ¨ Mirror with offset

                compensation
              ¨ Second stage npn higher
                performance
              ¨ Bias loop for first stage
Second stage
                               ¨ Darlinton Q15-Q19
                               ¨ Protection Q22 Q17

                               ¨ Q14 and Q20 class AB
                         Q14
                                 stage
                   Q17         ¨ Q16 vbe multiplier
             Q16
                                 (Vbe*(1+4.7/7.5))
       Q15
                         Q20
 Q22
             Q19
