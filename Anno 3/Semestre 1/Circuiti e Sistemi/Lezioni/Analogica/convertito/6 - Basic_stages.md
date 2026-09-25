---
fonte: "6 - Basic_stages.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

UNIVERSITY OF UDINE

Department DIEG
Via delle scienze 206
33100 Udine (UD), Italy




                      BASIC ANALOG STAGES
                      Associate professor Stefano Saggini
                      Lezione di circuiti e sistemi elettronici
Stadi differenziali
                +Va         +Va


           RL                     RL

                                  Vout




                            RE


                      -Va
Stadi differenziali
                   +Va         +Va


              RL                     RL
                                                              gm     IR
                                                      Ad =       RL = L
                                     Vout                      2     2VT


       Vd/2                                -Vd/2


                                          Considerando IRL=Va

                                                        Va
                               RE                  Ad =
                                                        2VT

                         -Va
Stadi differenziali
                  +Va         +Va

                                                            RL                RL
                                    RL         Acm = −                  ≅−
             RL                                          2RE + 1             2RE
                                                                   gm
                                    Vout
                                                           IRL    V
                                                Acm ≅ −        = − L = −1
                                                          2IRE    VRE
       Vcm                               Vcm




                                                                   Va
                              RE                         CMRR =
                                                                   VT

                                                Prestazioni limitate!
                        -Va
Generatori di corrente
      rD                    Positive loop approach

                          r +1 gm / / RS ro +1 gm / / RS
                     rD = o             =                = ro (RS gm +1) + RS
                            1− Gloop            RS
                                          1−
                                             1 gm + RS


 VB             r0      Open loop approach (forzo in tensione con VD)



                                         vD        ⎛    RS     ⎞
                              iD =                 ⎜⎜1−        ⎟⎟
                                   ro +1 gm / / RS ⎝ 1 gm + RS ⎠
           RS
Generatori di corrente
      rD                        rD
                                               Approccio retroazione serie-serie


                                     r0

                                                 rD = ROL (1− Gloop)
                     ro vS gm
 VB                                                            ⎛ gmr R ⎞
                r0                               = (RS + ro ) ⎜⎜1+    o S
                                                                           ⎟⎟
                                                               ⎝   RS + ro ⎠
                          vS
                                          RS



           RS
                                                              (
                                                rD = RS + ro 1+ gm RS     )
     Guadagno stadi elementari con ro

                                                     v DS
           RD
                                      iDS = vGS gm +
                      iDS                             ro
                 vD
                                                      RS + RD
                                   iDS = vGS gm − iDS
                                                         ro
                            r0

          vGSgm
vG
                 vS                        vGS            vGS
                                 iDS =             =
                                        1 RS + RD     1 ⎛ R +R ⎞
            RS                            +             ⎜1+ S    D
                                                                   ⎟
                                       gm    ro gm   gm ⎝     ro ⎠
     Guadagno stadi elementari con ro

                                 vD          −RD
           RD                       =
                      iDS        vG    1 ⎛ RS + RD ⎞
                                         ⎜1+       ⎟ + RS
                 vD                   gm ⎝     ro ⎠


                            r0    vS          RS
                                     =
                                  vG    1 ⎛ RS + RD ⎞
          vGSgm                           ⎜1+       ⎟ + RS
vG                                     gm ⎝    ro ⎠
                 vS

            RS
Guadagno stadi elementari con ro

      RD
            V0




                                RS
                 r0   vo = iS          RD
                              RS + Rin

      Rin
 iS         RS
  Guadagno stadi elementari con ro

                                   RD
                        vS
          Rin


                             r0
        ro vS gm             RD   Retroazione negativa (analogamente a
   vS              r0
                                  prima può essere interpretata utilizzando
                                  il modello con i generatori di corrente
                                  come retroazione positiva minore di 1)


         ro + RD   ro + RD
Rin =            =                Ovviamente tende a 1/gm se ro è molto
      1− Gloop(0) 1+ gmro         alta e maggiore di RD.
Guadagno stadi elementari con ro

      RD                          RS
                        vo = iS          RD
            V0                  RS + Rin


                 r0                RS
                      vo = iS               RD
                                    ro + RD
                              RS +
                                   1+ gmro
      Rin
 iS         RS
UNIVERSITY OF UDINE

Department DIEG
Via delle scienze 206
33100 Udine (UD), Italy




                      CURRENT MIRRORS
 Current Mirrors

                                                        Rin=gm1gm2/(gm1+gm2)
Small signal consideration
                                                        Rout=ro4 (1+gm4 ro3)+ro3
            Rin=1/gm1                                   Vmin= Vgs3 +Vov4
            Rout=ro2
                                                                        2
                                                        σ ID     ! σ $ ! 2σ $2
            Vmin= Vov2                                        = ## Kp && + ##   VT
                                                                                   &&
                                                        I REF       k
                                                                 " p %      " VOV %
Considering equal the two drain voltage           Vdd

                            2
             σ ID      ! σ $ ! 2σ $ 2             IIn                        Iout
                   =   # Kp & + ## VT &&
             I REF     # k &
                       " p % " VOV %
      Vdd


    IIn                          Iout                                               M4
                                             M1


 M1                                     M2                                          M3
                                             M2
  Current Mirror

Rin≅ gm2gm3/(gm3+gm2)

Rout≅ ro3 (1+ro1gm3) with (gm1 equal to gm2)

Vmin= Vgs2+ Vov3
                                                    Vdd


                                                     IIn
Considering equal the two drain voltage


                   2          2
 σ ID     ! σ Kp $    ! 2σ  $                              M3
       = ##      & + ## VT &&
 I REF           &
          " p % " VOV %
             k
                                               M1          M2
   Current Mirror

Rin=1/gm4
Rout≅gm3 ro3 ro2gm1 ro1                                    Vdd
Vmin= Vov3 +Vgs1
                                                           Ireg   Iout




Considering equal the two drain voltage
                                               Vdd

                                                                         M3
                 2             2
           ! σ $ ! 2σ $                         IIn
 σ ID
       =   # Kp & + ## VT &&
 I REF     # k &
           " p % " VOV %                              M1


                                          M4                        M2
  Current Steering DAC

                                   P$matrix$
                           ……..$

                           ……..$


BIASN$
                                         Out$P$
         DAC$$$BIAS$   SWITCH$                    Output current
                       MATRIX$           Out$N$




                                   N$matrix$
                           ……..$

                           ……..$
  Current Steering DAC
                      VddA     VddD

             B<0:4>                Bias_n
  Binary
             B<0:4>                   Outpos
              En
                             DAC
             T<0:6>
                                      Outneg
Thermometric T<0:6>
                CK
                      VssA     VssD
UNIVERSITY OF UDINE

Department DIEG
Via delle scienze 206
33100 Udine (UD), Italy




                      SECOND STAGE
                      Assistant professor Stefano Saggini
                      Nome della conferenza o seminario
Differential stage
    M1a                             M1b                   M2
                        1


                            M2      M1a               2           M1b


¨         Input Dynamic
     ¤      ICMR
     1.     Vincm (min)= Vov1+Vov2 + VTn (for n MOS) Vss for (for p MOS)
     2.      Vincm (max)= Vdd-Vov1-Vov2 - |VTp | (for p MOS) Vdd for (for n MOS)

¨         Trasconduttance :
                                 gm = K1 I D2
¨         Precision
                                         ⎞ ⎡⎛ σ ⎞            2⎤
                                          2         2
                                ⎛V                     ⎛ σ ⎞        Specchio
                       2
             σ Vos = σ Vt1,2 + ⎜⎜ OV1,2 ⎟⎟ ⎢⎜⎜ Kp ⎟⎟ + ⎜ I ⎟ ⎥
                                            ⎢                 ⎥
                                ⎝ 2 ⎠ ⎣⎝ k p ⎠a,b ⎝ I ⎠ ⎦
Inverter current source
                    Vdd


           Vbias
                                      Ouput signal range
                                      Voutmax=Vdd-Vovp
                          Vd
                               Vout   Voutmin= Vovn
                                      Input dynamics
             Vg                       Vinmin≅ Vinmax ≅ Vovn+VT


                   Gnd



¨   To increase the dynamics
    ¤ Increase W/L of nch and pch (decrease Vov)
    ¤ Reduce the current
  Inverter current source Tf
                                                                                                  C gd
                                                                                           1− s
                                                                                                gm
                           T (s) = −gm Rd Rg 2
                                                 (                                         ) (                                               )
                                            s RgC gs Rd C gd + RgC gs Rd Cd + RgC gd Rd Cd + s RgC gs + RgC gd Rd gm + RgC gd + Rd C gd + Rd Cd +1
               Rd
                      Cd


                     Vd   Output
            Cgd                                            1
Input                                    p1 ≅ −
                                                     gm C gd Rg Rd
                                                                                  |T(s)|
 Ig           Vg
                                                               gm C gd
               Cgs                       p2 ≅ −
         Rg
                                                     C gd (C gs + Cd ) + C gsCd
                                                gm
                                         z1 =                                                      p1 p2 z1
                                                C gd



  ¨     The dominant pole p1 can be calculated by using miller theorem
  ¨     To increase the performance
        ¤ Increase W/L of nch increase gm and Cgd
        ¤ Increase the current (increase of gm)
  Pole splitting
                                                                                                   C gd
                                                                                            1− s
                                                                                                 gm
                            T (s) = −gm Rd Rg 2
                                                 (                                        ) (                                                 )
                                             s RgC gs Rd C gd + RgC gs Rd Cd + RgC gd Rd Cd + s RgC gs + RgC gd Rd gm + RgC gd + Rd C gd + Rd Cd +1
              Rd
                       Cd


                     Vd   Output                                                               1
Input
         Cgd
                                                                           p1 ≅ −
 Ig          Vg                                                                       gm C gd Rg Rd
        Rg
              Cgs                                                                                    gm C gd
                                                                           p2 ≅ −
                                                                                      C gd (C gs + Cd ) + C gsCd
                                                                                  gm
                                                                           z1 =
                                                                                  C gd
                    Adding a capacitor on Ccg
                     |T(s)|



                                                        z1
