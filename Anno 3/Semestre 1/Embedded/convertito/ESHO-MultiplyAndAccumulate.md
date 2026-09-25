---
fonte: "ESHO-MultiplyAndAccumulate.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Multiply and ACcumulate (MAC)
Digital Signal Processing
Digital Signal Processing/Processor - DSP
The same acronym, DSP, refers both to the application domain and to the circuits
for its elaboration.
As a ma er of facts, all DSP applications ( lters, transformations, convolutions, ...)
are obtained executing the sum of products:
                                      N

                                      ∑ xk yk
                                    k=1
For example, the Fourier Transform:
                                          N
                                                - i kh xk
                               Fh = ∑ fk e
                                      k=1
               tt
Complex Sum and Product
As it is known, in the complex number domain the sum and product operator act to
the complex numbers, say x = xr + i xi as follows:

s = x + y = (xr + yr) + i (xi + yi)

p = x × y = (xr yr − xi yi) + i (xr yi − xi yr)
Single Cycle MAC



   x         x
             x
                   _
                       +
                                         p
                   +   +
    y        x
             x


                           accumulator
Pipelined MAC



   x              x
                  x              _              +
                                                              p
   y              x
                  x
                                 +              +



        input         pipeline       pipeline   accumulator
       register       register       register
     RTL Structural View

          xr           x
                                          +
                                                            sr
                           _            ovf   clr

          xi           x
                                              s
                                              r     over    ovf
                               clear                  ow
          yr           x                      s     logic
                                              r
                           +           ov
                                          f
                                                            si
          yi           x
                                          +
                                              clr
fl
Fixed-point Representation


      bit index   15   14 13 12    11   10   9   8    7   6   5    4   3    2   1    0




     bit weight   -20 2-1 2-2 2-3 2-4 2-5 2-6 2-7 2-8 2-9 2-10 2-11 2-12 2-13 2-14 2-15
Data Formats of the Datapath
                   point position
        (sign bit not accounted for below)


                     15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

   WI       .        s Input; Range: [ -1, 1 [ ; zero digits above the point.
                 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

  WPP     s .            Partial products; Range: [ -1, 1 ] ; one digit above the point.

             32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

  WPC   s   .            Complex products; Range: [ -2, 2 ] ; two digits above the point.

             19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

   WT   s   .             Truncation; Range: [ -2, 2 ] ; two digits above the point.

        21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

   WA s     .             Accumulator; Range: [ -16, 16 ] ; four digits above the point.
                     15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

   WO      s.             Output; Range: [ -1, 1 [ ; zero digits above the point.
     MAC RTL Structural View


          xrI                              accr
                    mxryr
     xr         x           prr
                                                            +
                                                                sar
                                                                              accr
                                                                                             sr
                                      pr          pra
                                  _                      ovf          clr
          xiI               pii
                    mxiyi
     xi         x                                   ovfsr             s     ovfr
                                                                      r              over    ovf
                    mxiyr
                                           clear                                       ow
     yr   yrI   x           pir                     ovfsi             s              logic
                                      pi          pia                 r     ovfi
                                  +                     ov
                            pri                            f    sai
                                                                                             si
     yi   yiI   x
                    mxryi                                   +
                                                                      clr
                                                                              acci
                                           acci
fl
Binary Multiplication
                                         A3      A2     A1     A0
                                         B3      B2     B1     B0
                                       A3 Bo   A2 B0   A1 B0   A0 B0
                              A3 B1    A2 B1   A1 B1   A0 B1
                     A3 B2   A2 B2    A1 B2    A0 B2
             A3 B3   A2 B3   A 1 B3   A0 B3

        S7    S6      S5      S4       S3      S2      S1      S0
Binary Multiplication - Block #1
                                                      A

                         A       B                        B
                                          A       B

            B       AB
                             B                O




                A                A
                    SO


                                     SO
Binary Multiplication - Block #2
                                        SI                           A

                    SI    A       B                                      B
                                                         A       B

            B        AB
                              B             A
                                                             O

                                       CO       HA   B
                                            S
                A                 A
                 CO SO

                                  CO   SO
Binary Multiplication - Block #3
                                           SI                            A CI

                    SI    A CI       B                                          B
                                                             A       B

            B        AB
                                 B             A
                                                                 O
                                                        B
                                          CO       FA   CI
                                               S
                A                    A
                 CO SO

                                     CO   SO
Binary Multiplication - Block #4
                                      A                 B

                 SI    B
                                          A        B
                                CO   CO       FA   CI   CI
            CO    FA       CI             S




                 SO


                                     SO
Binary Multiplication - Block #5
                                 A                B

                 SI    B
                                     A        B
                           CO   CO       HA
            CO    HA                 S




                 SO


                                SO
Binary Multiplier - Version #1
                                                                                                                 A3               A2               A1          A0

           B0
                                                                                                      A3 Bo            A2 Bo             A1 Bo          A0 Bo
                                                                                         A3                S03   A2         S02   A1         S01   A0    S00


            B1
                                                                             A3 B1                   A2 B1              A1 B1           A0 B1
                                                                A3         C14     S14   A2         C13    S13   A1   C12   S12   A0   C11   S11


            B2
                                                     A3 B2                  A2 B2                    A1 B2             A0 B2
                                        A3         C25    S25   A2         C24     S24   A1         C23    S23   A0   C22   S22

            B3
                             A3 B3                  A2 B3                    A1 B3                   A0 B3
                       C36   S36             C35    S35              C34     S34              C33    S33




          ovf     HA               FA                     FA                       HA



                 P7          P6                      P5                      P4                       P3               P2                P1             P0
Binary Multiplier - Version #2
                                                                                                                   A3               A2               A1          A0

           B0
                                                                                                        A3 Bo            A2 Bo             A1 Bo          A0 Bo
                                                                                          A3                 S03   A2         S02   A1         S01   A0    S00


            B1
                                                                              A3 B1                    A2 B1              A1 B1           A0 B1
                                                                 A3         C14     S14   A2          C13    S13   A1   C12   S12   A0   C11   S11


            B2
                                                      A3 B2                  A2 B2                     A1 B2             A0 B2
                                         A3         C25    S25   A2         C24     S24   A1          C23    S23   A0   C22   S22

            B3
                 '0'
                              A3 B3                  A2 B3                    A1 B3                    A0 B3
                        C36   S36             C35    S35              C34     S34              C33     S33



                                                                                                     '0'
          ovf      FA               FA                     FA                       FA



                 P7           P6                      P5                      P4                        P3               P2                P1             P0
Binary Multiplier - Version #3
                                                                                                                   A3                A2                A1                A0

           B0
                                                                                                           A3 Bo              A2 Bo             A1 Bo             A0 Bo
                                                                                          A3         '0'     S03   A2   '0'    S02   A1   '0'    S01   A0   '0'    S00


            B1
                                                                              A3 B1                    A2 B1                  A1 B1         A0 B1
                                                                 A3         C14     S14   A2          C13    S13   A1    C12   S12   A0   C11    S11


            B2
                                                      A3 B2                  A2 B2                         A1 B2              A0 B2
                                         A3         C25    S25   A2         C24     S24   A1          C23    S23   A0    C22   S22

            B3
                 '0'
                              A3 B3                  A2 B3                    A1 B3                    A0 B3
                        C36   S36             C35    S35              C34     S34              C33     S33



                                                                                                     '0'
          ovf      FA               FA                     FA                       FA



                 P7           P6                      P5                      P4                           P3                 P2                P1                P0
Binary Multiplier - Version #4
                                                                                                           '0'     A3           '0'     A2           '0'     A1         '0'     A0
                                                                                                                        '0'                  '0'                  '0'            '0'

           B0
                                                                                                       A3 Bo                  A2 Bo                A1 Bo                A0 Bo
                                                                                          A3         C03    S03    A2     C02     S02   A1     C01     S01   A0     C00   S00


            B1
                                                                              A3 B1                   A2 B1                   A1 B1                A0 B1
                                                                 A3         C14     S14   A2         C13    S13    A1     C12     S12   A0     C11     S11


            B2
                                                      A3 B2                  A2 B2                    A1 B2                   A0 B2
                                         A3         C25    S25   A2         C24     S24   A1         C23     S23   A0     C22     S22

            B3
                 '0'          A3 B3                  A2 B3                    A1 B3                   A0 B3
                        C36   S36             C35    S35              C34     S34              C33    S33


                                                                                                     '0'
          ovf      FA               FA                     FA                       FA



                 P7           P6                      P5                      P4                       P3                     P2                   P1                   P0
Binary Multiplier - Version #5
                                                                                          '0'     A3           '0'     A2           '0'     A1         '0'     A0
                                                                                                       '0'                  '0'                  '0'            '0'

           B0
                                                                                      A3 Bo                  A2 Bo                A1 Bo                A0 Bo
                                                                     C33     A3     C03    S03    A2     C02     S02   A1     C01     S01   A0     C00   S00


           B1
                                                                A3 B1                A2 B1                   A1 B1                A0 B1
                                                 C34    A3    C14      S14   A2     C13    S13    A1     C12     S12   A0     C11     S11


           B2
                                            A3 B2              A2 B2                 A1 B2                   A0 B2
                             C35   A3     C25     S25   A2    C24     S24    A1     C23     S23   A0     C22     S22

           B3
                           A3 B3           A2 B3                A1 B3                A0 B3
                     C36   S36      C35    S35          C34    S34            C33    S33




                P7         P6               P5                  P4                    P3                     P2                   P1                   P0
END
