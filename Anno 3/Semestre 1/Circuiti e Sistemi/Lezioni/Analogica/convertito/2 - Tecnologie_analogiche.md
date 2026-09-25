---
fonte: "2 - Tecnologie_analogiche.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

UNIVERSITY OF UDINE

Department DPIA
Via delle scienze 206
33100 Udine (UD), Italy




                      CIRCUITI E SISTEMI
                      ELETTRONICI
                      Stefano Saggini
                      2 lezione Tecnologie analogiche
Different Type of MOS available in the
technology
¨   Core MOS (minimum )
    ¤ Small minimum dimension L or W
    ¤ small maximum Vgs, Vgd and Vd
    ¤ Can be version Low VTH or Zero VTH

¨   I/O MOS (in general defined By the Vdd)
    ¤ Higher minimum dimension L or W
    ¤ Higher maximum Vgs, Vgd and Vd

¨   High Voltage LDMOS
    ¤ Fixed L dimension
    ¤ High Vds voltage
    BJT
                                               C
                                       Cµ
                                                    Cdbulk
                                                                                B   E      C
       C    bulk                                             bulk
                    VnB             IC=IE a
                                B              ro                   InC         P   N+     N+
                                       a /gm
B
                          InB                                                              N-
                                     Cp IE                                          Psub
       E
                                               E
     Small signal
                                                       Approfondimento
         I
     gm = C                                                  Noise parameters
         VT
         V                                                   I nC = 2qI C
     ro = E
         IC                                                  I nB = 2qI B
            β
     α=                                                  VnB = 4kTRb
           1+ β
s                                                                        Photodiode/Phototransistor . . .

                       Our design first example
e time is inversely proportional to the          In the circuit of Figure 4 (A), the output (VOUT ) is
 age and is expressed as follows:             given as:
                                                VOUT = IP × R1 + IB × R1 + VBE
        1
 R ) – --
       n
        -              ¨    Example of    RX
                                       This       circuit
                                             arrangement
                                    tively fast response.
                                                             with
                                                          provides    bipolar
                                                                   a large output and transistor
                                                                                      rela-

 pacitance of the photodiode                     The circuit of Figure 4 (B) has an additional transis-
tor                                           tor (Tr2) to provide a larger output current.
potential (0.5 V - 0.9 V)
bias voltage (negative value)                                             VCC                          VCC


                                                                                           VBE
                                                        IP          RL          RBE
RENT AMPLIFIER CIRCUIT
TRANSISTOR OF                                                            VOUT                    Tr1
 E
    4 show photocurrent amplifiers using                                                               VOUT
                                                                   Tr1
                                                       VBE                            IP
 wn in Figure 3 are most basic combina-
 ode and an amplifying transistor. In the
Figure 3 (A), the photocurrent produced
                                               RBE                                                RL
e causes the transistor (Tr1) to decrease
 from high to low. In the arrangement of
 e photocurrent causes the V OUT to
w to high. Resistor RBE in the circuit is
 ressing the influence of dard current (Id)
 meet the following conditions:                              (A)                           (B)
                                                                                                       OP1-18

                                                     Figure 3. Photocurrent Amplifier Circuit
MOS model and description
¨   Different types of MOS available from the
    technology
                           Single well

         Source Gate Drain        Source Gate Drain
           P+         P+             N+          N+
                 N-
                                         Psub

                             Triple well
         Source Gate Drain        Source Gate Drain
          P+          P+             N+          N+
                                            P-
                N-

                                    Psub
    MOS SOA consideration
    ¨   Voltage
                                   Low voltage Diodes
                                                            Triple well
    Single well


          D               SD                   D                SD

G                 B   G        B          G         B   G                 B



          S               S                    S              DS
                          D



These Diodes in many can have high BD voltage
    MOS Description
    ¨   MOS static model SPICE LEVEL I
 TRIODE

            W⎡              ⎛ V ⎞⎤
I D = µo Cox ⎢(VGS −VTH ) − ⎜ DS ⎟⎥VDS         (VGS −VTH ) ≥ 0    (VGD −VTH ) ≥ 0
            L ⎢⎣            ⎝ 2 ⎠⎥⎦

 SATURATION
               W          2
  I D = µo Cox
               2L
                  (            )(
                  VGS −VTH 1+ λ VDS        ) (V −V ) ≥ 0
                                                 GS   TH
                                                                 (VGD −VTH ) < 0


 OFF STATE
 ID ≅ 0                             (VGS −VTH ) < 0              (VGD −VTH ) < 0

VTH =VTHO + γ   ( 2 Φ +V − 2 Φ )
                      F   SB        F
  MOS Capacitors (AC)
                                                            Mask L
  ¨   MOS dynamic model SPICE LEVEL I
                                                                G        C1
                                                C3
C1 = C3 ≅ ( LD ) Cox Weff = (CGXO) Weff
                                                                    C2        Mask W
C2 = ( L − 2 LD ) Weff Cox
                                          C5
2C5 = CGBO( Leff )                                    B
                                                           C4
                                                 Cut Off    Saturation   Linear
                                  C 2+ 2 C 5
                 Mask L                                         CGS
                                  C1+ 2/3 C2
                                  C1+ 1/2 C2
            LD

                                                                CGD
                                     C 1, C 3                             CGB
Mask W
                                      2 C5
                 L(Leff)
                                                           VT       vDS+VT    VGS
Short channel effects SCE
¨  Output resistance decreases due to channel length
  modulation.
¨ VT becomes more dependent on Leff and VD.

¨ Ioff and subthreshold slope increase; susceptibility to punch-
  through increases.
¨ Vertical and lateral fields increase.

¨ Mobility degrades; velocity saturates; hot-carrier effects
  become more important.
¨ Overlap and fringe capacitances become a larger fraction
  of gate capacitance.
¨ Extrinsic resistance becomes a larger fraction of source-to-
  drain resistance.
¨ Flicker noise and mismatch increase
Saturation velocity
¨   When the E field reach a critical value the carrier
    reach the saturation velocity
                                  Leff
                           τ≈
                                  vsat

¨   Hence the current became
                                         Average inversion charge for unit area

                 Weff Leff Q
          ID ≈                 ≈ Weff Cox (VGS −VT ) vsat
                     τ
     Small signal model in Saturation
           ∂I D
    gm =        = (2 K ʹW L) I D (1+ λ VDS ) = (2 K ʹW L) I D
           ∂VGS
            ∂I D   ∂I ∂VT            γ
g mbs = −        =− D       = gm                                    = η gm
            ∂VSB   ∂VT ∂VSB      2 2Φ +V           F          SB                 L’impedenza di ingresso
                                                                                 del dispositivo è
               ∂I D   λID                                                        rigorosamente un circuito
g ds = g o =        =
               ∂VSD 1+ λVDS
                                   (
                            ≅ λ I D λ ↓ L↑     )
                                                                                 aperto in Continua!!!!!!!!!!!!!
                                                                                                    D
                                            D C
                                                  db
                                   Cgd                                                Cgd                  Cdb
        D
                                                       InD
                                   gm vgs
                             G                     gmbs vbs        go   B    G         I=IS1             I=IS2    B
G                B                                                                                                    InD
                                                                                               ro
                                                                                       1/gm             1/gmbs

                                   Cgs
        S                                   S Csb                                    Cgs IS1            IS2 Csb

                                                                                                    S
                                       Cgb
                                                                                               Cgb
Under threshold MOS current

              vGS
     W
iD ≅ I DO e    n
     L
1< n < 3            Process parameters
I DO
Temperature dependence
Temperature

VTH (T ) =VTH (To ) + TCV (T − To )
 ln(K (T )) = ln(K (To )) + BEX (ln(T ) − ln(To ))

TCV ≅ -1.5 [ mV/K ]
BEX ≅ -1.76

In saturation the temperature effect depends on Vov.
For low overdrive voltage the current increase with the
temperature with high overdrive is the contrary
Noise generator
Drain current noise generator

      ⎡ 8kg m (1 + η )     KF I D ⎤
in2 = ⎢                +          2 ⎥
                                      Δf     (A2)
      ⎣      3           2 f COX L ⎦


Reported at the input

 2  in2 ⎡ 8k (1 + η )       KF I D    ⎤
e = 2 =⎢
 n                    +               ⎥ Δf    (V2)
   gm   ⎣   3  g m      2 f COX WLK ' ⎦
Matching between two devices
¨   Considering two equal devices of area A on the same
    wafer characterized by the Parameter P (example the
    resistance, capacitor or the threshold voltage ecc..)
                 Devices 1                Devices 2
                                 D



    Area A
¨ P1 and P2 are two random variables
¨ The mean value of P on the wafer depend on process variation

¨ The difference ΔP=P1-P2 is Gaussian distributed with a variance

                       2             Experimentally determined
             2    A
         σ (ΔP) =   + S 2P D 2
                       P
                  A
Matching between two devices
¨   In the technology manual is reported
    ¤ Absolute variation between parameters

         ΔP = P1 − P2
      n Used for VT of MOS

    ¤ Relative variation

                 (
        ΔP 200 P1 − P2
           =
                        )
         P      P1 + P2
      n Used for K of MOS, Resistance and capacitors

¨   Only the coefficient related to the Area A
 Matching between two MOS

ΔP = P1 − P2                          Used for VT
ΔP 200 (P1 − P2 )                     Used for K
   =
 P   P1 + P2
            α         ΔP    β
σ (ΔP) =         σ(      )=              Standard deviation
            WL         P    WL

                                                              Mask L
            D                    D

        G        (DID/ID) ID G
                                               Mask W
  DVT

            S                    S

                                                          M1       M2
            M1                   M2
Recommended layout
¨   Centroid        D2       D1


                         B
               G2                 G1
Schematico
                         S




Layout
Examples for voltage dividers
    +

    -


¨   Voltage references

        Vbg                        M
                            VA =      Vbg
                                 N +M
              M
                  VA
              N        Approfondimento

                       Calcolando la varianza della tensione otteniamo
                                                         Scala con l’area
                         σ VA       M    σR 1
                              =
                         VA     (N + M )N R 2
