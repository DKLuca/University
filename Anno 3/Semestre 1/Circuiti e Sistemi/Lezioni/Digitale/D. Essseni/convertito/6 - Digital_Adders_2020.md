---
fonte: "6 - Digital_Adders_2020.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

A Generic Digital Processor


                                      MEM ORY
                       INPUT-OUTPUT




                                                 CONTROL




                                      DATAPATH




                                                                 2
© Digital
  EE141 Integrated Circuits2nd
                                                      Arithmetic Circuits
Building Blocks for Digital Architectures

             Arithmetic unit
             - Bit-sliced datapath (adder, multiplier, shifter, comparator, etc.)

             Memory
             - RAM, ROM, Buffers, Shift registers
             Control
             - Finite state machine (PLA, random logic.)
             - Counters
             Interconnect
             - Switches
             - Arbiters
             - Bus

                                                                                    3
© Digital
  EE141 Integrated Circuits2nd
                                                                       Arithmetic Circuits
Full-Adder
              A      B

 Cin           Full              Cout
              adder

                Sum




                                                   9
© Digital
  EE141 Integrated Circuits2nd
                                        Arithmetic Circuits
 The Binary Adder
                                  A   B

                          Cin      Full     Cout
                                  adder

                                   Sum


                        S = A ⊕ B ⊕ Ci

                           = ABC i + ABC i + ABCi + ABCi
                       C o = AB + BCi + ACi

                                                                     10
© Digital
  EE141 Integrated Circuits2nd
                                                           Arithmetic Circuits
Express Sum and Carry as a function of P, G, D

        Define 3 new variable which ONLY depend on A, B
        Generate (G) = AB
        Propagate (P) = A ⊕ B
        Delete = A B




        Can also derive expressions for S and Co based on D and P
         Note that we will be sometimes using an alternate definition for
         Propagate (P) = A + B
                                                                         11
© Digital
  EE141 Integrated Circuits2nd
                                                               Arithmetic Circuits
Complimentary Static CMOS Full Adder
                                                                         VDD

                       VDD
                                                       Ci       A         B

               A             B
                                                                               A

               B
                             Ci                                                B
                                                                                         VDD
               A
                                      X
                                                                               Ci

          Ci                      A                                                            S
                                                                                    Ci

      A            B              B         VDD
                                                  A         B       Ci              A


Co=AB+Ci(A+B)                                     Co                                B


S=ABCi+Co(A+B+Ci)
                                          28 Transistors
                                                                                                   12
© Digital
  EE141 Integrated Circuits2nd
                                                                                         Arithmetic Circuits
A Better Structure: The Mirror Adder
                   Co=1 se Generate=1
                                                                     S=ABCi+Co(A+B+Ci)
                   Co=0 se Kill=1                                           VDD
                   Co=Ci(A+B) altrimenti
                                   VDD                               VDD          A

                      A        B         B                   A   B     Ci         B
                                                 Kill
      "0"-Propagate                      A                                        Ci
                                                        Co
                          Ci                                                           S
                                         A                                        Ci
      "1"-Propagate                             Generate
                      A        B         B                   A   B     Ci         A

                                                                                  B
Al massimo 2 MOSFETs
in serie per il Co
                                             24 transistors
                                                                                                13
© Digital
  EE141 Integrated Circuits2nd
                                                                                      Arithmetic Circuits
      The Mirror Adder
    • The NMOS and PMOS chains are completely symmetrical.
      A maximum of two series transistors can be observed in the carry-
      generation circuitry.
    • When laying out the cell, the most critical issue is the minimization
      of the capacitance at node Co. The reduction of the diffusion
      capacitances is particularly important.
    • The capacitance at node Co is composed of four diffusion
      capacitances, two internal gate capacitances, and six gate
      capacitances in the connecting adder cell .
    • The transistors connected to Ci are placed closest to the output.
    • Only the transistors in the carry stage have to be optimized for
      optimal speed. All transistors in the sum stage can be minimal
      size.

                                                                        15
© Digital
  EE141 Integrated Circuits2nd
                                                              Arithmetic Circuits
Transmission Gate Full Adder
                                                                             G=AB
                                                               P equiv. Ci   P=A exor B
                                                           P
                                                                    VDD
                                                                             S = P exor Ci
                 VDD                              Ci
                                 P =A B+A B                                  Co = G + PCi
                                      A
                                                       P               S Sum Generation
             A       A                P           Ci

                                      A                P            VDD
                             B                B
                 VDD                              A
                                      P
                                                       P               Co Carry Generation
            Ci       Ci                           Ci                      Per P=0 si ha:
                                     A                                      A=B=0 -> Co=A=0=AB
                          Setup                            P                A=B=1 -> Co=A=1=AB
                                                                          Pertanto Co = AB + P Ci


                                                                                            19
© Digital
  EE141 Integrated Circuits2nd
                                                                                  Arithmetic Circuits
      The Ripple-Carry Adder
                      A0        B0              A1        B1          A2        B2          A3        B3


              Ci,0                     Co,0                    Co,1                  Co,2                  Co,3
                           FA                        FA                    FA                    FA
                                     (= Ci,1)


                           S0                        S1                    S2                    S3


                     Worst case delay linear with the number of bits
                                                     td = O(N)

                                                      tadder = (N-1)tcarry + tsum

                       Goal: Make the fastest possible carry path circuit

                                                                                                                       20
© Digital
  EE141 Integrated Circuits2nd
                                                                                                             Arithmetic Circuits
Inversion Property

                        A        B             A        B


               Ci           FA       Co   Ci       FA       Co


                            S                      S




                                                                           21
© Digital
  EE141 Integrated Circuits2nd
                                                                 Arithmetic Circuits
Minimize Critical Path by Reducing Inverting Stages

                                                         Even cell             Odd cell

            A0        B0           A1        B1          A2        B2          A3        B3


    Ci,0                   Co,0                   Co,1                  Co,2                  Co,3
                 FA                     FA                    FA                    FA



                 S0                     S1                    S2                    S3



                                  Exploit Inversion Property


                                                                                                     22
© Digital
  EE141 Integrated Circuits2nd
                                                                                          Arithmetic Circuits
Carry-Bypass Adder
                              P0    G1             P0    G1           P2    G2            P3    G3                 Also called
                                                                                                                   Carry-Skip
                     Ci,0                 C o,0               C o,1              Co,2                Co,3
                                 FA                 FA                 FA                  FA




                            P0 G1             P0    G1          P2     G2            P3    G3
                                                                                                     BP=P oP1 P2 P3
                  Ci,0                C o,0              Co,1                C o,2




                                                                                                     Multiplexer
                             FA                   FA                  FA                FA
                                                                                                                   Co,3




                            Idea: If (P0 and P1 and P2 and P3 = 1)
                            then Co3 = C0, else “kill” or “generate”.


                                                                                                                              30
© Digital
  EE141 Integrated Circuits2nd
                                                                                                                    Arithmetic Circuits
Carry-Bypass Adder (cont.)
          Bit 0–3                  Bit 4–7                Bit 8–11             Bit 12–15
          Setup        tsetup      Setup                   Setup                Setup
                                               tbypass


          Carry                     Carry                   Carry                Carry
       propagation               propagation             propagation          propagation




           Sum                      Sum                     Sum        tsum      Sum


           M bits



                    tadder = tsetup + Mtcarry
                                       tcarry + (N/M –1)tbypass + (M – 1)tcarry + tsum



                                                                                           31
© Digital
  EE141 Integrated Circuits2nd
                                                                               Arithmetic Circuits
Carry Ripple versus Carry Bypass

                     tp
                                        ripple adder




                                         bypass adder




                                 4..8         N
                                                                  32
© Digital
  EE141 Integrated Circuits2nd
                                                        Arithmetic Circuits
Carry-Select Adder
                                           Setup

                                             P,G

                 "0"             "0" Carry Propagation



                 "1"             "1" Carry Propagation



      Co,k-1                           Multiplexer                   C o,k+ 3

                                                      Carry Vector

                                     Sum Generation




                                                                                33
© Digital
  EE141 Integrated Circuits2nd
                                                                     Arithmetic Circuits
Carry Select Adder: Critical Path
             Bit 0–3                Bit 4–7                 Bit 8–11                Bit 12–15
             Setup                   Setup                   Setup                    Setup


   0        0-Carry       0         0-Carry       0         0-Carry        0         0-Carry


   1        1-Carry       1         1-Carry       1         1-Carry        1         1-Carry


           Multiplexer             Multiplexer             Multiplexer              Multiplexer
  Ci,0                    Co,3                    Co,7                    Co,11                     Co,15


         Sum Generation          Sum Generation          Sum Generation           Sum Generation
              S0–3                    S4–7                   S8–11                    S12–15




                                                                                                   34
© Digital
  EE141 Integrated Circuits2nd
                                                                                        Arithmetic Circuits
Linear Carry Select
                             Bit 0-3                  Bit 4-7                   Bit 8-11               Bit 12-15



                             Setup                      Setup                    Setup                  Setup

                                       (1)

                           "0" Carry                "0" Carry                "0" Carry               "0" Carry
               "0"                           "0"                      "0"                     "0"
                     (1)

                           "1" Carry                 "1" Carry                "1" Carry               "1" Carry
               "1"                           "1"                      "1"                     "1"
                     (5)       (5)                      (5)                      (5)                     (5)
                                             (6)                     (7)                     (8)
                           Multiplexer               Multiplexer              Multiplexer             Multiplexer
            Ci,0
                                                                                                               (9)

                     Sum Generation                Sum Generation           Sum Generation          Sum Generation

                             S0-3                       S 4 -7                   S8-11                   S 1 2-15 (10)



                                                                 M           N
                                                                             M



                                                                                                                               35
© Digital
  EE141 Integrated Circuits2nd
                                                                                                                     Arithmetic Circuits
Square Root Carry Select
                  Bit 0-1                  Bit 2-4                  Bit 5-8                Bit 9-13             Bit 14-19


                  Setup                      Setup                   Setup                   Setup
                            (1)

                 "0" Carry                "0" Carry               "0" Carry               "0" Carry
     "0"                           "0"                    "0"                     "0"
           (1)

                 "1" Carry                 "1" Carry              "1" Carry                "1" Carry
     "1"                          "1"                     "1"                     "1"
           (3)     (3)                       (4)                      (5)                      (6)                (7)
                                  (4)                     (5)                    (6)                      (7)
                 Multiplexer               Multiplexer            Multiplexer             Multiplexer           Mux
   Ci,0
                                                                                                                        (8)
           Sum Generation                Sum Generation         Sum Generation          Sum Generation          Sum

                  S0-1                        S2-4                   S5-8                     S9-13             S14-19 (9)




                                                                                                                        36
© Digital
  EE141 Integrated Circuits2nd
                                                                                                         Arithmetic Circuits
Adder Delays - Comparison
                                      50

                tp (in unit delays)
                                      40                      Ripple adder


                                      30

                                                        Linear select
                                      20


                                      10
                                                    Square root select

                                      0
                                           0   20        40              60
                                                    N

                                                                                        37
© Digital
  EE141 Integrated Circuits2nd
                                                                              Arithmetic Circuits
