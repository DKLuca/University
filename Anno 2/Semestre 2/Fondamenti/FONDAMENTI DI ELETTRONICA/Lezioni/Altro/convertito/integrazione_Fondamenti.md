---
fonte: "integrazione_Fondamenti.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Materiale integrative per il corso
 di Fondamenti di Elettronica
    Digitale, prof. P.Palestri
                        varie figure prese da
    http://icbook.eecs.berkeley.edu/resources/powerpoint-slides

"Adapted from Digital Integrated Circuits (2nd Edition): Jan M. Rabaey,
              Copyright 2003 Prentice Hall/Pearson."

                                                                          1
       Adders (1)
          A   B
              A   B
Cin        Full       Cout
      Cin adderFull          Cout
              adder
           Sum
               Sum


 S = A  B  Ci                            Generate (G) = AB
                                           Propagate (P) = A  B
      = ABC i + ABC i + ABCi + ABCi
                                      OR
 C o = AB + BC i + ACi
                                                                   2
                                                                                                                  carry ripple adder

                 Adders (2)                                                             A0        B0              A1        B1

                                                                                                                                 A
                                                                                                                                        A2

                                                                                                                                        B
                                                                                                                                                  B2          A3        B3


                                                                                 Ci,0                    Co,0                    Co,1                  Co,2                  Co,3
                                                                                             FA                        FA                    FA                    FA
                                                                                                          Cin
                                                                                                       (= Ci,1)                   Full                 Cout
                                                                 VDD
                                                                                                                                 adder
                 VDD                                                                         S0                        S1                    S2                    S3
                                               Ci       A         B
                                                                                                                                 Sum
         A             B
                                                                       A

         B
                                                                       B
                                                                                                        S = A  B  Ci
                       Ci
                                                                                  VDD
         A
                                X
                                                                       Ci

    Ci                      A                                                           S
                                                                                                            = ABC i + ABC i + ABCi + ABCi
                                                                            Ci

A            B              B       VDD
                                          A         B       Ci              A
                                                                                                       C o = AB + BC i + ACi
                                          Co                                B


                                                                                                                                                                        3
                                                                                                                                 Even cell             Odd cell

                                                                                   A0        B0            A1        B1          A2        B2          A3        B3

      Adders (3)                                                       Ci,0                       Co,0                    Co,1                  Co,2                  Co,3
                                                                                        FA                      FA                    FA                    FA



                                                                                        S0                      S1
                                                                                                                           A     B S                        S3
                                                                                                                                       2


                                                                      VDD                                 Cin               Full                Cout
                                                                                                                           adder
                             VDD                               VDD            A

                                                       A   B
                                                                                                                            Sum
                A        B         B                             Ci           B
                                           Kill
"0"-Propagate                      A                                          Ci
                                                  Co
                    Ci                                                             S
                                   A                                          Ci
                                                                                                         S = A  B  Ci
"1"-Propagate                             Generate
                A        B         B                   A   B     Ci           A                           = ABC i + ABC i + ABCi + ABCi
                                                                              B                      C o = AB + BC i + ACi

                                       24 transistors                                                                                                            4
     Adders (4)
                pass-transistors
                                            P
                                                VDD
     VDD                           Ci
                      A
                                        P         S Sum Generation
A      A              P            Ci                                   Propagate (P) = A  B

                      A                 P       VDD
              B               B
     VDD                           A
                      P
                                        P         Co Carry Generation
Ci     Ci                          Ci
                      A
            Setup                           P



                                                                                                5
 Adders (5)
                                                                          VDD
               Generate (G) = AB                                Pi
                          VDD                                         
     Pi                                                    Ci             Co
          Gi
                          Co                                         Gi
Ci

          Di
                                         Delete = A B                
     Pi



                                   Propagate (P) = A  B


                                                                                6
Adders (6)
                                Manchester carry chain

                                                               VDD
                 
           P0         P1             P2              P3
                                                               C3

    Ci,0
                G0         G1           G2                G3


                 




                     C0            C1               C2         C3
                                                                     7
         Adders (7)                                                                                VDD

                                                                                                                           G3

                                                                                                                           G2
  • carry lookAhead                                                                                                        G1

                                                                                                                           G0
       A0, B0    A1, B1                •••             AN-1, BN-1
                                                                         Ci,0
                                                                                                                           Co,3


                                                                          P0

                                                                          P1

                                                                          P2
Ci,0          P0 Ci,1        P1                                           P3
                                                  Ci, N-1       PN-1


         S0             S1             •••               SN-1
                                                                       C o k = Gk + Pk  Gk – 1 + P k – 1  + P1 G0 + P0 Ci 0  
        C o k = f A k B k Co k – 1  = Gk + P kCo k – 1

                                                                                                                                  8
Design styles: full custom

                    Transition to Automation and
                    Regular Structures




 Intel 4004 (‘71)


                                                   Intel 8486




                                                                9
Design styles: standard cells (1)
                                    example of cell: 3-input NAND cell
                                    (from ST Microelectronics)




                                                                     10
Design styles: standard cells (2)




  Initial transistor   Placed        Routed   Compacted   Finished
  geometries           transistors   cell     cell        cell
                                                                     11
     Design styles: PLA (programmable-logic-array)
                                                                  And-Plane              Or-Plane
                                          V DD                                                     GND


                         Product terms
                  x0x1
     AND           x2         OR
     plane                   plane




                            f0       f1

x0    x1     x2


                                                              x0 x0 x1 x1 x2 x2             f0 f1
                                                 Pull-up devices                  Pull-up devices
                                                                                                    12
                   Design styles: semi-custom
                                               Design Capture    Behavioral

                                                    HDL
                            Pre-Layout
                                                                 Structural
Design Iteration




                            Simulation
                                               Logic Synthesis



                                               Floorplanning
                            Post-Layout
                            Simulation           Placement       Physical

                          Circuit Extraction      Routing


                                                 Tape-out

                                                                              13
Design styles: late-binding


                  Array-based


   Pre-diffused                 Pre-wired
  (Gate Arrays)                 (FPGA's)




                                            14
Design styles: gate-array / sea-of-gates
                                                          polysilicon

                            VD D

                                                            metal
              rows of                                                   Uncommited
              uncommitted                                   possible
              cells         GND                             contact     Cell



                                   In 1 In 2   In 3 In4


              routing
              channel                                                   Committed
                                                                        Cell
                                                                        (4-input NOR)
                                                            Out




                                                                                        15
    Design styles: pre-wired arrays (1)
                                                  I5   I4   I3   I2   I1   I0   Programmable
                                                                                OR array
• Programming Technique
    Fuse-based (program-once)
    Non-volatile EPROM based
    RAM based
• Programmable Logic Style
    Array-Based
    Look-up Table

                M
                e                      In   Out
                                                  Programmable AND array

                                                                                 O 3O 2O 1O 0
                m
                                 Out   00    0
                o
                r                      01    1
                y                      10    1

                                       11    0

                                                                                                16
                      ln1 ln2
Design styles: pre-wired arrays (2)

              antifuse polysilicon        ONO dielectric




             n+ antifuse diffusion

                               2l
   Open by default, closed by applying current pulse

   One Time Programmable (OTP)

                                                           17
Design styles: Mesh interconnection




                                      18
   FPGA (1)
• example: ALTERA Cyclone
                            logic array block=10 logic elements




                                                       19
   FPGA (2)
• example: ALTERA Cyclone



              Logic element:




                               20
Scaling and Moore’s law (1)




                              21
Scaling and Moore’s law (2)

• 2014: 250x1018 transistors fabricated
• more than all transistors fabricated before 2010

                                                      1 acre =
• fabrication costs 1B$/acre                         4 046.85642 m2
• cost of the tools: 100 times higher over 35 years
   • but 100 times faster….




                                                                  22
Scaling and Moore’s law (3)

                              Static RAM




                                           23
Power/energy consumption (1)




                               24
Power/energy consumption (2)




                               25
Power/energy consumption (3)




                               26
Schmitt Trigger (1)
                                     Vou t                      V OH




              In         Out


                                             V OL



                                                    VM–   VM+      Vi n
• bistable circuit use to restore noisy signals


                                                                          27
Schmitt Trigger (2)




                      28
      Schmitt Trigger (3)
                                                    M2+M4 if “out”=‘0’
                                                    M2    if “out”=‘1’
               VDD



                                                         𝛽𝑢𝑝             𝛽𝑢𝑝
          M2         M4                           𝑉𝐷𝐷         − 𝑉𝑇            −1
                                                        𝛽𝑑𝑜𝑤𝑛           𝛽𝑑𝑜𝑤𝑛
Vin            X            Vout          𝑉𝐿𝑇 =
                                                                      𝛽𝑢𝑝
                                                            1+
                                                                     𝛽𝑑𝑜𝑤𝑛
          M1         M3             M1+M3 if “out”=‘1’
                                    M1    if “out”=‘0’                   Vou t                           V OH




                                   VLT(“out”=’1’) < VLT(“out”=’0’)
                                                                                 V OL



                                                                                        VM–        VM+      Vi n

                                                                                              29
 Pads (1)
Bonding Pad




              Out        100 mm


                                  PADS +
                                  bonding
                                  wires
   VDD
                    In   GND
                                            30
Pads (2): tri-state buffer
             V DD

                                            V DD
                                En

                                                   Out
        En
                                En
   In               Out
                          In

        En



                               Increased output drive
Pads (3)
• scalable pads (Infineon AP32146)




                                     32
 Example of Pads in ST microcontrollers (1)
• digital push-pull        • open drain




                                              33
 Example of Pads in ST microcontrollers (2)
• with analog
  multiplexer




                                              34
Microcontrollers (1)




thanks to N.Ponte      35
Microcontrollers (2)




                       thanks to N.Ponte
                       36
Microcontrollers (3)
       I/O of C8051F380 microcontroller




                                          37
Microcontrollers (4)


                       huge efforts to improve
                       energy efficiency




                                                 38
Microcontrollers (5)




                       39
 Package (1)
                                           • flip-chip with ball-grid-array
• lead frame
        Bonding wire


                       Chip
  L
                                Mounting
                                 cavity

                        Lead
              L´        frame




                       Pin



      >1nH

                                                                              40
  Package (2)


SMD: surface mount device




                            41
             • AN203 Silicon Labs
PCB design




                                    42
PCB design: decoupling (1)
      From:




                             PDN: power distribution network
                                                               43
PCB design: decoupling (2)




                             44
PCB design: decoupling (3)




                             to have 5% voltage drop



                                    Smith et al., IEEE
                                    TRANSACTIONS ON
                                    ADVANCED PACKAGING,
                                    VOL. 22, NO. 3, AUGUST
                                    1999


                                                         45
PCB design: decoupling (4)
  impedance vs. freq. of a single capacitor




           not only the capacitor itself,
           but also the trace inductance
                                              46
PCB design: decoupling (5)




                             47
     PCB design: decoupling (6)
                                                                 OR
Capacitors in parallel                  small cap. in parallel
                                                                 using low ESL capacitors
                                        better than big one




  MLCC: multi-layer-ceramic-capacitor                                                       48
