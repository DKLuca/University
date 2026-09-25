---
fonte: "chapter07_Elearn_2020.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Digital Integrated
                                   Circuits
                                   A Design Perspective
                                   Jan M. Rabaey
                                   Anantha Chandrakasan
                                   Borivoje Nikolic

                                   Designing Sequential
                                   Logic Circuits
                                            November 2002

© Digital Integrated Circuits2nd
                                                   Sequential Circuits
 Sequential Logic
              Inputs                                         Outputs
                                     COMBINATIONAL
                                         LOGIC

         Current State
                                                          Next state
                                         Registers
                                         Q      D


                                              CLK

                                   2 storage mechanisms
                                   • positive feedback
                                   • charge-based

© Digital Integrated Circuits2nd
                                                            Sequential Circuits
      Timing Definitions

         CLK
                                                              t   Register
                                   tsu   thold                    D        Q


            D                       DATA                                CLK
                                   STABLE                     t
                                            tc 2 q

            Q                                         DATA
                                                     STABLE   t




© Digital Integrated Circuits2nd
                                                                      Sequential Circuits
 Maximum Clock Frequency
                                         φ




                                       FF’s
                                   LOGIC                   Also:
                                                           tcdreg + tcdlogic > thold
                                   tp,comb
                                                           tcd: contamination delay =
                                                           minimum delay
                           tclk-Q + tp,comb + tsetup = T



© Digital Integrated Circuits2nd
                                                                         Sequential Circuits
      Naming Conventions

        In our text:
              a latch is level sensitive
              a register is edge-triggered
        There are many different naming
           conventions
              For instance, many books call edge-
               triggered elements flip-flops
              This leads to confusion however


© Digital Integrated Circuits2nd
                                                 Sequential Circuits
         Latches
              Positive Latch                                 Negative Latch


         In       D       Q        Out                  In      D         Q       Out
                      G                                               G

                       CLK                                             CLK

   clk                                   clk

    In                                    In

  Out                                    Out


          Out         Out                       Out          Out
         stable   follows In                   stable    follows In




© Digital Integrated Circuits2nd
                                                                      Sequential Circuits
      Latch versus Register
      Latch                               Register
         stores data when                      stores data when
         clock is low                          clock rises

                                   D Q              D Q

                                   Clk               Clk


          Clk                            Clk

           D                             D

           Q                             Q

© Digital Integrated Circuits2nd
                                                           Sequential Circuits
 Positive Feedback: Bi-Stability
                                                                                             Vi 1          V o1 = V i 2    V o2


                        1




                  V o1                                      Vi2
                                                                      1




                        o




                                                                      o




                                                                                                           V o2 = V i 1
                    V




                                                                  V




                                                                  5




                                                                      2




                                                                      i




                                                                  V




                                                     V i1                                           V o2

                                                 1
                                                        A
                                   V i 2 = V o1
                                                 o




                                             V




                                             5




                                                 2




                                             V
                                                 i




                                                                          C


                                                                                     B
                                                                              V i 1 = V o2

© Digital Integrated Circuits2nd
                                                                                                                    Sequential Circuits
  Meta-Stability
               A                                                 A
V i 2 5 V o1




                                                  V i 2 5 V o1
                         C                                           C




                                          B                                        B
                                   V i 1 5 V o2                             V i 1 5 V o2
                     d                                           d
               Gain should be larger than 1 in the transition region


© Digital Integrated Circuits2nd
                                                                     Sequential Circuits
      Mux-Based Latches
      Negative latch                   Positive latch
      (transparent when CLK= 0)        (transparent when CLK= 1)




                           1       Q                0            Q


           D               0             D          1


                    CLK                       CLK

        Q = Clk ⋅ Q + Clk ⋅ In               Q = Clk ⋅ Q + Clk ⋅ In

© Digital Integrated Circuits2nd
                                                           Sequential Circuits
        Mux-Based Latch
                                   CLK



                                               Q

                                         CLK

                       D



                                   CLK


© Digital Integrated Circuits2nd
                                               Sequential Circuits
      Mux-Based Latch
       CLK
                                     QM
                                          CLK

                                     QM

                                          CLK




                              CLK


                         NMOS only        Non-overlapping clocks



© Digital Integrated Circuits2nd
                                                      Sequential Circuits
        Writing into a Static Latch
     Use the clock as a decoupling signal,
     that distinguishes between the transparent and opaque states


                     CLK                       CLK

                                   Q     D                              D
                           CLK
                                               CLK
    D



                     CLK
                                          Forcing the state
        Converting into a MUX             (can implement as NMOS-only)


© Digital Integrated Circuits2nd
                                                              Sequential Circuits
       Master-Slave (Edge-Triggered)
       Register
                                   Slave
             Master                        CLK

                                    0      Q   D
               1                               QM
                                    1
                           QM
   D           0                               Q

                                   CLK
              CLK




    Two opposite latches trigger on edge
    Also called master-slave latch pair

© Digital Integrated Circuits2nd
                                                    Sequential Circuits
      Master-Slave Register

    Multiplexer-based latch pair




                   I2         T2   I3        I5   T4        I6        Q


                                        QM
          D        I1         T1             I4   T3


  CLK




© Digital Integrated Circuits2nd
                                                       Sequential Circuits
       Setup Time
              3.0                                                    3.0
                                   Q
              2.5                                                    2.5

              2.0                      QM                            2.0                 I 2 2 T2
              1.5                                                    1.5                              Q
     Volts




                                                            Volts
                           CLK                                                    CLK
                      D                                                      D
              1.0                                                    1.0
                                       I 2 2 T2                                             QM
              0.5                                                    0.5

              0.0                                                    0.0

             2 0.5                                                  2 0.5
                  0       0.2    0.4     0.6      0.8   1                0       0.2    0.4     0.6       0.8    1
                                 time (nsec)                                            time (nsec)
                            (a) Tsetup 5 0.21 nsec                                 (b) T setup 5 0.20 nsec



© Digital Integrated Circuits2nd
                                                                                                 Sequential Circuits
      Clk-Q Delay

                       2.5
                               CLK

                       1.5
              Volts




                               D
                                     tc 2 q(lh)                 tc 2 q(hl)
                                        Q
                       0.5


                      2 0.5
                           0          0.5         1       1.5       2        2.5
                                                  time, nsec


© Digital Integrated Circuits2nd
                                                                                   Sequential Circuits
      More Precise Setup Time
                     Clk

                                                                       t
                     D

                                                                       t
                     Q

                                                                       t
                                                      (a)


                                   1.05tC 2 Q
                                                            tC 2 Q



                                                tSu                  tD 2 C


                                                      tH
                                                      (b)

© Digital Integrated Circuits2nd
                                                                              Sequential Circuits
      Setup/Hold Time Illustrations
    Circuit before clock arrival (Setup-1 case)
                                        CN

                                   TG1
                                                            Inv2                 Clk-Q Delay
                                   D1         SM                         QM
               D

                       Inv1


                                         CP
                                                                                  TClk-Q


                                                              TSetup-1                                      Time

       Data                                              Clock
                          TSetup-1

                                                                          Time
                                                   t=0


© Digital Integrated Circuits2nd
                                                                                      Sequential Circuits
      Setup/Hold Time Illustrations
    Circuit before clock arrival (Setup-1 case)
                                         CN

                                   TG1
                                                            Inv2              Clk-Q Delay
                                   D1         SM                   QM
               D

                       Inv1


                                         CP
                                                                               TClk-Q


                                                                   TSetup-1                              Time


                   Data                                  Clock
                                        TSetup-1

                                                                     Time
                                                   t=0


© Digital Integrated Circuits2nd
                                                                                   Sequential Circuits
      Setup/Hold Time Illustrations
    Circuit before clock arrival (Setup-1 case)
                                        CN

                                   TG1
                                                            Inv2                   Clk-Q Delay
                                   D1         SM                   QM
               D

                       Inv1
                                                                                    TClk-Q

                                         CP


                                                                        TSetup-1                              Time


                       Data                              Clock
                                         TSetup-1

                                                                    Time
                                                   t=0


© Digital Integrated Circuits2nd
                                                                                        Sequential Circuits
      Setup/Hold Time Illustrations
    Circuit before clock arrival (Setup-1 case)
                                        CN

                                   TG1
                                                              Inv2                   Clk-Q Delay
                                   D1           SM                   QM               TClk-Q
               D

                       Inv1


                                         CP


                                                                          TSetup-1                             Time


                              Data                         Clock
                                              TSetup-1

                                                                      Time
                                                     t=0


© Digital Integrated Circuits2nd
                                                                                         Sequential Circuits
      Setup/Hold Time Illustrations
                          Hold-1 case
                                        CN

                                   TG1                                         Clk-Q Delay
                                                         Inv2
                                   D1           SM              QM
               D

                       Inv1

                                                0
                                         CP
                                                                      TClk-Q


                                                                                                  THold-1
                                                                                                            Time


           Clock                                        Data
                                              THold-1

                                                                     Time
                               t=0


© Digital Integrated Circuits2nd
                                                                                    Sequential Circuits
      Setup/Hold Time Illustrations
                          Hold-1 case
                                        CN

                                   TG1                                          Clk-Q Delay
                                                          Inv2
                                   D1           SM               QM
               D

                       Inv1

                                                0
                                         CP
                                                                       TClk-Q


                                                                                              THold-1
                                                                                                           Time


           Clock                                        Data
                                              THold-1

                                                                      Time
                               t=0


© Digital Integrated Circuits2nd
                                                                                     Sequential Circuits
      Setup/Hold Time Illustrations
                          Hold-1 case
                                        CN

                                   TG1                                       Clk-Q Delay
                                                       Inv2
                                   D1         SM              QM
               D

                       Inv1

                                              0
                                         CP                         TClk-Q


                                                                                       THold-1
                                                                                                        Time


           Clock                                    Data
                                          THold-1

                                                                   Time
                               t=0


© Digital Integrated Circuits2nd
                                                                                  Sequential Circuits
      Setup/Hold Time Illustrations
                              Hold-1 case
                                        CN

                                   TG1                                         Clk-Q Delay
                                                         Inv2
                                   D1         SM                QM
               D

                       Inv1                                           TClk-Q

                                              0
                                         CP


                                                                                   THold-1
                                                                                                           Time


           Clock                                  Data
                                        THold-1
                                                                     Time
                                t=0


© Digital Integrated Circuits2nd
                                                                                     Sequential Circuits
      Setup/Hold Time Illustrations
                          Hold-1 case
                                         CN

                                   TG1                                      Clk-Q Delay
                                                      Inv2         TClk-Q
                                   D1          SM            QM
               D

                       Inv1

                                               0
                                          CP


                                                                              THold-1
                                                                                                         Time


           Clock                               Data
                                        THold-1                                  ⇒
                                                                  Time
                               t=0


© Digital Integrated Circuits2nd
                                                                                   Sequential Circuits
       Reduced Clock Load
       Master-Slave Register

             CLK                         CLK


 D             T1                  I1    T2    I3                   Q

                                    I2          I4
             CLK                         CLK




© Digital Integrated Circuits2nd
                                                     Sequential Circuits
      Avoiding Clock Overlap
                    CLK                      X            CLK
                                                                                    Q
                             A
              D
                                                 B




                                   CLK                                 CLK
                                           (a) Schematic diagram


                                   CLK



                                   CLK
                                         (b) Overlapping clock pairs



© Digital Integrated Circuits2nd
                                                                             Sequential Circuits
       Cross-coupled NOR Pair
      NOR-based set-reset

                                                         S   R         Q       Q
  S
                           Q
                                   S   Q                 0   0         Q       Q
                                                         1   0         1       0
                                   R   Q
                                                         0   1         0       1
                           Q
  R                                                      1   1         0       0

                                           Forbidden State




© Digital Integrated Circuits2nd
                                                                 Sequential Circuits
      Cross-coupled NAND pair
        Cross-coupled NANDs
                                       S   R   Qn     Qn
          S                            0   0   N/A    N/A
                                   Q
                                       0   1    1      0
                                       1   0    0      1

                                   Q
                                       1   1   Qn-1   Qn-1
          R




© Digital Integrated Circuits2nd
                                                      Sequential Circuits
      Set-Reset NOR Latch
                                                 VDD


                                            M2         M4
                                                            Q
                                        Q


                             CLK       M6                   M8   CLK
                                            M1         M3

                                   S   M5                   M7   R




                              This is not used in datapaths any more,
                              but is a basic building memory cell

© Digital Integrated Circuits2nd
                                                                        Sequential Circuits
      Storage Mechanisms

                        CLK



                                    Q           CLK

                              CLK
                                        D                            Q
        D



                        CLK                     CLK



                     Static                 Dynamic (charge-based)


© Digital Integrated Circuits2nd
                                                           Sequential Circuits
  Making a Dynamic Latch Pseudo-Static

                                   CLK


                 D                       D



                                   CLK




© Digital Integrated Circuits2nd
                                             Sequential Circuits
    Dynamic Latches/Registers: C2MOS
                                         VDD                       VDD


                                         M2                        M6


                             CLK         M4                 CLK    M8
                                                  X
                    D                                                         Q
                                                      CL1                   CL2
                             CLK         M3                 CLK    M7


                                         M1                        M5




                                   Master Stage               Slave Stage

              “Keepers” can be added to make circuit pseudo-static

© Digital Integrated Circuits2nd
                                                                                  Sequential Circuits
      Insensitive to Clock-Overlap
                   VDD                 VDD               VDD                 VDD

                   M2                  M6                M2                  M6


             0     M4              0   M8
                         X                                     X
  D                                          Q   D                                   Q
                                                     1   M3           1      M7


                   M1                  M5                M1                  M5


                   (a) (0-0) overlap                     (b) (1-1) overlap




© Digital Integrated Circuits2nd
                                                                     Sequential Circuits
       Single-phase Latches: TSPC
                  VDD              VDD                    VDD         VDD




                                         Out

  In      CLK                CLK               In   CLK         CLK

                                                                               Out




             Double n-C2MOS                           Double p-C2MOS


© Digital Integrated Circuits2nd
                                                                      Sequential Circuits
      Including Logic in TSPC
                     VDD             VDD                VDD                    VDD

                                            In1                   In2
                     PUN
                                       Q                                             Q

     In      CLK               CLK                CLK                   CLK




                     PDN                      In1



                                              In2



          Example: logic inside the latch                     AND latch

© Digital Integrated Circuits2nd
                                                                          Sequential Circuits
      Precharged Register (TSPC)
                                   VDD         VDD             VDD


                                         CLK                         Q
                                   M3          M6              M9
                                                     Y
                                                                         Q
                    D       CLK            X             CLK
                                   M2          M5              M8



                                         CLK
                                   M1          M4              M7




                            p-C2MOS – double n-C2MOS


© Digital Integrated Circuits2nd
                                                                         Sequential Circuits
 Pipelining




                                                     REG
        REG



 a                                               a




                                                           REG




                                                                 REG




                                                                                REG
                                     REG
                               log         Out       CLK                log           Out
       CLK




                                                     REG
        REG




 b                                   CLK         b         CLK   CLK           CLK


       CLK                                           CLK


     Reference                                                         Pipelined




© Digital Integrated Circuits2nd
                                                                   Sequential Circuits
