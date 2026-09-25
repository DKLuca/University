---
fonte: "Memorie_SRAM_DRAM_2020.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Digital Integrated
                                   Circuits
                                   A Design Perspective
                                   Jan M. Rabaey
                                   Anantha Chandrakasan
                                   Borivoje Nikolic

                                   Semiconductor
                                   Memories
                                          December 20, 2002

© Digital Integrated Circuits2nd                          Memories
   Chapter Overview

       Memory Classification
       Memory Architectures
       The Memory Core
       Periphery
       Reliability
       Case Studies

© Digital Integrated Circuits2nd   Memories
Semiconductor Memory Classification

                                                Non-Volatile
                 Read-Write Memory              Read-Write     Read-Only Memory
                                                 Memory

             Random            Non-Random         EPROM         Mask-Programmed
              Access             Access
                                                  E2PROM       Programmable (PROM)

              SRAM                 FIFO            FLASH

               DRAM                LIFO
                               Shift Register
                                   CAM



© Digital Integrated Circuits2nd                                              Memories
      Memory Timing: Definitions
                             Read cycle


   READ

                                                           Write cycle
                      Read access         Read access
  WRITE

                                                         Write access
                                            Data valid


   DATA


                                                                Data written



© Digital Integrated Circuits2nd                                        Memories
      Memory Architecture: Decoders
                                                  M bits                                                                    M bits

                                       S0                                                                           S0
                                                  Word 0                                                                    Word 0
                                       S1
                                                  Word 1                A0                                                  Word 1
                                       S2                     Storage                                                                    Storage
                                                  Word 2                A1                                                  Word 2
                                                              cell                                                                       cell
                  w   o   r   d   s




                                                                        AK-1
              N




                                                                                       D   e   c   o   d   e   r




                                      SN – 2
                                                Word N – 2                                                                Word N – 2
                                      SN – 1
                                                Word N – 1                                                                Word N – 1


                                                                          K = log2 N
                                               Input-Output                                                              Input-Output
                                                  (M bits)                                                                  (M bits)

       Intuitive architecture for N x M memory                          Decoder reduces the number of select signals
               Too many select signals:
              N words == N select signals
                                                                                                                   K = log2N

© Digital Integrated Circuits2nd                                                                                                        Memories
      Array-Structured Memory Architecture
                 Problem: ASPECT RATIO or HEIGHT >> WIDTH
                                                2L 2 K      Bit line
                                                                                 Storage cell
                    AK




                                  Row Decoder
                    A K1 1                                                      Word line


                    AL2 1



                                                                            M.2K
                                                                                            Amplify swing to
                                                   Sense amplifiers / Drivers               rail-to-rail amplitude

                             A0
                                                         Column decoder                     Selects appropriate
                             A K2 1                                                         word


                                                          Input-Output
                                                             (M bits)


© Digital Integrated Circuits2nd                                                                                  Memories
      Hierarchical Memory Architecture
                           Block 0                  Block i                               Block P 2 1

        Row
        address


        Column
        address
        Block
        address



                                                                                 Global data bus
             Control               Block selector                Global
             circuitry                                        amplifier/driver


                                                                    I/O
          Advantages:
          1. Shorter wires within blocks
          2. Block address activates only 1 block => power savings
© Digital Integrated Circuits2nd                                                                   Memories
    Block Diagram of 4 Mbit SRAM
                                         Clock                 Z-address           X-address
                                        generator               buffer              buffer

                                                      Predecoder and block selector
                                                             Bit line load
                                                                                                           o
                                                                                                           l
                                                                                                           yB
                                                                                                            ra
                                                                                                             A
                                                                                                             K
                                                                                                             8
                                                                                                             2
                                                                                                             1
                                                                                                             ck0




                                                                                        ro
                                                                                         g
                                                                                         u
                                                                                         lS
                                                                                          a
                                                                                          b
                                                                                          c
                                                                                          e
                                                                                          d
                                                                                          w




                                            ro
                                             g
                                             u
                                             lS
                                              a
                                              b
                                              c
                                              e
                                              d
                                              w




                                                                   o
                                                                   G
                                                                   c
                                                                   e
                                                                   d
                                                                   lrw
                                                                     a
                                                                     b




                         o
                         l
                         B
                         0
                         ck3




                   o
                   l
                   B
                   1
                   ck3




                                                                                                     o
                                                                                                     l
                                                                                                     B
                                                                                                     ck1




                                                             Transfer gate
                                                            Column decoder                                         e
                                                                                                                   d
                                                                                                                   lrw
                                                                                                                     ca
                                                                                                                      o
                                                                                                                      L




                                                     Sense amplifier and write driver


                               CS, WE              I/O           x1/x4         Y-address       X-address
                               buffer             buffer       controller       buffer          buffer




© Digital Integrated Circuits2nd                              [Hirose90]                                                  Memories
    Contents-Addressable Memory
                                                                                                                                                                                           Data (64 bits)




                     I/O Buffers



                                                                                                                 Commands
                              I   /   O   B   u   f   f   e   r   s




                                                                         I   /   O   B   u   f   f   e   r   s




                                                                                                                                                                                                                                                                                                                                         Comparand

                                                                                                                       C   o   m   m   a   n   d   s
                                                                                                                                                       C   o   m   m   a   n   d   s




                                                                                                                                                                                                                                                                                                                                           Mask




                                                                                                                                                                                                              Address Decoder




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Priority Encoder
                                                                                                                                                                                                                                                                                                                                                                2 Validity Bits
                                                                                                                                                                                                                                                                                                                                      CAM Array
                                                                      Control Logic                                                                                                    R/W Address (9 bits)                                                                                                                          9
                                                                                                                                                                                                                                                                                                                                    2 words 3 64 bits
                                                                                                                                                                                                                                                                                                                                                                     V   a   l   i   d   i   t   y       B       i       t       s




                                                                                                                                                                                                                                                                                                                                                        9




                                                                                                                                                                                                                                                                                                                                                                9
                                                                                                                                                                                                                                                                                                                                                                 2




                                                                                                                                                                                                                                                                                                                                                                                                                                                                         P   r   i   o   r   i   t   y   E   n   c   o   d   e   r




                                                                                                                                                                                                                                                                                                                                                                                                             V       a       l       i   d   i   t   y   B   i   t   s




                                                                                                                                                                                                                                                                            A   d   d   r   e   s   s   D   e   c   o   d   e   r




                                                                                                                                                                                                                                                                                                                                                            9




                                                                                                                                                                                                                                                                                                                                                                                                     2




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      P   r   i   o   r   i   t   y   E   n   c   o   d   e   r




                                                                                                                                                                                                                    A   d   d   r   e   s   s   D   e   c   o   d   e   r




© Digital Integrated Circuits2nd                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Memories
Read-Write Memories (RAM)
             STATIC (SRAM)
                      Data stored as long as supply is applied
                      Large (6 transistors/cell)
                      Fast
                      Differential


            DYNAMIC (DRAM)
                     Periodic refresh required
                     Small (1-3 transistors/cell)
                     Slower
                     Single Ended

© Digital Integrated Circuits2nd                                 Memories
      6-transistor CMOS SRAM Cell

                                        WL

                                        V DD
                                   M2          M4
                                                Q
                           M5       Q               M6


                                   M1          M3


                      BL                             BL




© Digital Integrated Circuits2nd                          Memories
      CMOS SRAM Analysis (Read)
                                                           WL

                                        V DD
                              BL                      M4
                                                                 BL
                                        Q= 0
                                               Q= 1         M6
                                   M5

                       V DD             M1     V DD                   V DD

                Cbit                                                         Cbit


     Kn,M5=Cox Mobn S5
      Kn,M1=Cox Mobn S1                                    S1



      CR=S1/S5




© Digital Integrated Circuits2nd                                                    Memories
      CMOS SRAM Analysis (Read)
                                                                                                1.2

                     Voltage Rise (V)                                                            1
                                                                                                0.8
                                                                                                0.6
                                                                                                0.4
                                                                                                0.2
                                        V   o   l   t   a   g   e   r   i   s   e   [   V   ]




                                                                                                 0
                                                                                                      0   0.5    1 1.2 1.5 2      2.5   3
                                                                                                                Cell Ratio (CR)



© Digital Integrated Circuits2nd                                                                                                            Memories
      CMOS SRAM Analysis (Write)
                                                                  WL
                                               V DD
                                                             M4

                                        Q= 0                           M6
                                   M5                        Q= 1

                                          M1
                                                      V DD
Kn,M6=Cox Mobn S6            BL = 1                                         BL = 0
Kp,M4=Cox Mobp S4
PR=S4/S6




© Digital Integrated Circuits2nd                                                     Memories
      CMOS SRAM Analysis (Write)




© Digital Integrated Circuits2nd   Memories
    6T-SRAM — Layout
                                                               VDD
                                       M2             M4




                                   Q                       Q
                                            M1   M3


                                                               GND
                                       M5             M6       WL


                                        BL        BL


© Digital Integrated Circuits2nd                                     Memories
    Resistance-load SRAM Cell
                                                              WL
                                              V DD
                                         RL               RL

                                    Q                     Q
                               M3                                  M4

                      BL                M1           M2                 BL




                      Static power dissipation -- Want R L large
                      Bit lines precharged to V DD to address t p problem


© Digital Integrated Circuits2nd                                             Memories
      SRAM Characteristics




© Digital Integrated Circuits2nd   Memories
      Sense Amplifiers
                                                  make ∆ V as small
                              C ⋅ ∆V              as possible
                         tp = ----------------
                                Iav

                          large                  small

    Idea: Use Sense Amplifer

                small
                transition                          s.a.


                                        input                output


© Digital Integrated Circuits2nd                                      Memories
      Differential Sense Amplifier
                                   V DD


                            M3            M4
                                               y        Out


             bit           M1             M2   bit



                      SE           M5


                                                     Directly applicable to
                                                     SRAMs

© Digital Integrated Circuits2nd                                   Memories
      Differential Sensing ― SRAM
           V DD                     V DD
                         PC



         BL                              BL             V DD                    V DD
                         EQ
                                              y M3              M4                         2y

        WL i
                                              x      M1    M2        2x   x                     2x

                                                   SE     M5                              SE


                                                           SE
                     SRAM cell i

                                              V DD
                        Diff.
                      x Sense 2x                                                       Output
                        Amp                    y


                                                   SE
                          Output
               (a) SRAM sensing scheme             (b) two stage differential amplifier


© Digital Integrated Circuits2nd                                                                Memories
     Sense Amplifier (and Waveforms)
                                                                       Address
     I /O                I /O

                                                                          ATD
                 SEQ                         Block
                                             select    ATD
                                      BS                                  BEQ

                                                                           Vdd
    SA      BS            SA                                       I/O Lines
                                           SEQ                            GND

                                                                           SEQ
                                                      SEQ
                   SEQ          SEQ                                       Vdd
                                       DATA                          SA, SA
                                                             Dei         GND

                                                                         DATA
                 BS

                                                                       Data-cut


© Digital Integrated Circuits2nd                                                  Memories
      Data Retention in SRAM
                                   1.30u

                                   1.10u
                                                                   0.13 mm CMOS
                                   900n

                                   700n
                  Ileakage



                                   500n                       Factor 7
                       (   A   )




                                   300n                           0.18 mm CMOS

                                   100n

                                       0.00   .600         1.20          1.80

                                                     VDD

         SRAM leakage increases with technology scaling

© Digital Integrated Circuits2nd                                                  Memories
      Suppressing Leakage in SRAM
                   V DD
                            low-threshold transistor           V DD   V DDL
      sleep
                                   V DD,int            sleep
                                                                              V DD,int

 SRAM             SRAM             SRAM
  cell             cell             cell               SRAM      SRAM         SRAM
                                                        cell      cell         cell

                                   V SS,int
          sleep




Inserting Extra Resistance                         Reducing the supply voltage


© Digital Integrated Circuits2nd                                              Memories
      3-Transistor DRAM Cell
            BL 1                             BL 2

      WWL

      RWL                                           WWL

                                        M3          RWL

                    M1      X                       X                     V DD 2 V T
                                   M2
                                                                 V DD
                       CS                           BL 1

                                                    BL 2    V DD 2 V T          DV




                         No constraints on device ratios
                         Reads are non-destructive
                         Value stored at node X when writing a “1” = VWWL-VTn


© Digital Integrated Circuits2nd                                            Memories
     3T-DRAM — Layout
                                   BL2   BL1        GND


                           RWL
                                               M3

                                               M2



                           WWL
                                    M1




© Digital Integrated Circuits2nd                          Memories
      1-Transistor DRAM Cell
                      BL
         WL                                                           Write 1              Read 1
                                                       WL

                           M1
                                                       X GND                  V DD 2 V T
                                      CS
                                                                       V DD
                                                       BL
                                                            V DD /2                               V /2
                                                                                           sensing DD
         CBL




          Write: C S is charged or discharged by asserting WL and BL.
          Read: Charge redistribution takes places between bit line and storage capacitance
                                                                        CS
                                   ∆V = VBL – V PRE = V BIT – V PRE ------------
                                                                    C S + CBL

                           Voltage swing is small; typically around 250 mV.


© Digital Integrated Circuits2nd                                                                     Memories
DRAM Cell Observations
 1T DRAM requires a sense amplifier for each bit line,
due to charge redistribution read-out.
 DRAM memory cells are single ended in contrast to
SRAM cells.
The read-out of the 1T DRAM cell is destructive; read and
refresh operations are necessary for correct operation.
 Unlike 3T cell, 1T cell requires presence of an extra
capacitance that must be explicitly included in the design.
 When writing a “1” into a DRAM cell, a threshold voltage
is lost. This charge loss can be circumvented by
bootstrapping the word lines to a higher value than VDD



© Digital Integrated Circuits2nd                    Memories
     1-T DRAM Cell
                                                                                 Capacitor


                                                                                       M 1 word
                                                                                       line
 Metal word line
                                                 SiO2
                              Poly
           n+          n+                     Field Oxide   Diffused
                                                            bit line
                            Inversion layer
                Poly
                            induced by                                         Polysilicon
                                                                 Polysilicon
                            plate bias                             gate        plate

             Cross-section                                              Layout

                             Uses Polysilicon-Diffusion Capacitance
                                          Expensive in Area

© Digital Integrated Circuits2nd                                                  Memories
SEM of poly-diffusion capacitor 1T-DRAM




© Digital Integrated Circuits2nd          Memories
  Advanced 1T DRAM Cells
                                                              Word line
                                                                                Cell plate    Capacitor dielectric layer
                                                      Insulating Layer




      Cell Plate Si


                                                               Transfer gate                   Isolation
                                     Refilling Poly
Capacitor Insulator                                                            Storage electrode


Storage Node Poly
                                     Si Substrate
   2nd Field Oxide




                 Trench Cell                                 Stacked-capacitor Cell
  © Digital Integrated Circuits2nd                                                                     Memories
      Single-to-Differential Conversion

                     WL
        BL                                      2x
                                    x
                                        Diff.
                                                     1
                                                     +
               Cell                     S.A.               V ref
                                                     -
                                                     2


                                           Output


                        How to make a good Vref?


© Digital Integrated Circuits2nd                         Memories
      Latch-Based Sense Amplifier (DRAM)
                                               EQ
                                   BL               BL
                                             VDD

                                        SE




                                        SE




       Initialized in its meta-stable point with EQ
       Once adequate voltage gap created, sense amp enabled with SE
       Positive feedback quickly forces output to a stable operating point.

© Digital Integrated Circuits2nd                                              Memories
     Open bitline architecture with
     dummy cells
                                             EQ


           L              L1       L0        V DD   R0    R1             L
                                        SE

                 BLL                                           BLR


               …                                                    …
   CS              CS       CS                           CS    CS             CS
                                        SE

 Dummy cell                                                             Dummy cell




© Digital Integrated Circuits2nd                                        Memories
     Sense Amp Operation

            V BL                                             V(1)


                     V PRE
                                         DV(1)


                                                             V(0)
                                       Sense amp activated          t
                                   Word line activated



© Digital Integrated Circuits2nd                                        Memories
     DRAM Read Process with Dummy Cell
             3                                                                           3




             2                                                                           2

                     V
                                          BL                                     V
                                                                                                                  BL

             1                                                                           1
                                           BL                                                                              BL



             0                                                                           0
                 0           1                 2           3                                 0       1                 2        3
                                 t (ns)                                                                  t (ns)

                             reading 0                                                               reading 1
                                                   3
                                                           EQ     WL


                                                   2
                         V




                                                                                SE

                                                   1



                                                   0
                                                       0          1                  2           3
                                                                       t (ns)

                                                                control signals
© Digital Integrated Circuits2nd                                                                                                Memories
    Periphery

     Decoders
     Sense Amplifiers
     Input/Output Buffers
     Control / Timing Circuitry



© Digital Integrated Circuits2nd   Memories
      Row Decoders
                Collection of 2M complex logic gates
                Organized in regular and dense fashion

                                   (N)AND Decoder




                                   NOR Decoder




© Digital Integrated Circuits2nd                         Memories
      Hierarchical Decoders
       Multi-stage implementation improves performance
                                                                                 •••




                                                                                        WL 1




                                                                                        WL 0



              A 0A 1 A 0A 1 A 0A 1 A 0A 1   A 2A 3 A 2A 3 A 2A 3 A 2A 3



                                                                          •••
                                                                                NAND decoder using
                                                                                2-input pre-decoders
             A1 A0      A0        A1        A3 A2     A2        A3




© Digital Integrated Circuits2nd                                                               Memories
      Dynamic Decoders
Precharge devices        GND             GND                                     VDD


                                                                                            WL3
                                                                                 VDD
                                                    WL 3

                                                                                            WL 2
                                                    WL 2                         VDD

                                                    WL 1
                                                                                            WL 1
                                                                                 V DD
                                                    WL 0
                                                                                            WL 0

  VDD φ             A0         A0   A1         A1
                                                             A0   A0   A1   A1          φ



   2-input NOR decoder                                     2-input NAND decoder



© Digital Integrated Circuits2nd                                                        Memories
      4-input pass-transistor based column
      decoder            BL BL  BL BL                                                                       0   1       2   3


                                                                                                       S0
                     A0
                                                                                                       S1

                                                                                                       S2

                     A1                                                                                S3
                                   2   -   i   n   p   u   t   N   O   R   d   e   c   o   d   e   r




                                                                                                                    D

   Advantages: speed (tpd does not add to overall memory access time)
      Only one extra transistor in signal path
   Disadvantage: Large transistor count


© Digital Integrated Circuits2nd                                                                                                Memories
     4-to-1 tree based column decoder
                                   BL 0 BL 1 BL 2 BL 3

                              A0

                              A0

                              A1

                              A1




                                              D
            Number of devices drastically reduced
            Delay increases quadratically with # of sections; prohibitive for large decoders
            Solutions: buffers
                       progressive sizing
                       combination of tree and pass transistor approaches

© Digital Integrated Circuits2nd                                                 Memories
     Voltage Regulator

             VDD

                                   Mdrive
    VREF                                VDL
                                                Equivalent Model
              Vbias
                                              VREF
                                                     -
                                                     -
                                                              Mdrive
                                                     +
                                                     +



                                                              VDL

© Digital Integrated Circuits2nd                          Memories
      Charge Pump                                   CLK



                                   V DD
                                                                   2V DD -2 V T
                                                          VB
                                    M1
        CLK               A        B
                                                                        - VT
                                                                   V DD 2
                                                                   0V
                           Cpump
                                      M2
                                           V load
                              Cload                       V load

                                                                   0VDD
                                                                     V - 2VT




© Digital Integrated Circuits2nd                                        Memories
      Sensing Parameters in DRAM
                                           1000
                                                                     C D(1F)
                                                                         f
                                                       V smax (mv)

                                                                          Q S(1C)
                                                                              f
                           s   m   a   x




                                           100
                       V




                       ,
                                                                C S(1F)
                                                                    f
                           D   D




                       V




                       ,




                           S




                       C




                       ,




                           S
                                            10
                       Q




                                                                                    V DD (V)
                       ,




                           D




                       C




                                                  QS 5= C S V DD / 2
                                                  V smax 5
                                                         = Q S / (C S 1+ C D )

                                                  4K     64K     1M 16M 256M 4G                64G
                                                       Memory Capacity (bits        / chip)

© Digital Integrated Circuits2nd                               From [Itoh01]                         Memories
    Semiconductor Memory Trends
    (updated)




© Digital Integrated Circuits2nd   From [Itoh01]   Memories
      Trends in Memory Cell Area




© Digital Integrated Circuits2nd   From [Itoh01]   Memories
