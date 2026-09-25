---
fonte: "BAV99_SER.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

BAV99 series
                    High-speed switching diodes
                    Rev. 8 — 18 November 2010                                                    Product data sheet




1. Product profile

          1.1 General description
              High-speed switching diodes, encapsulated in small Surface-Mounted Device (SMD)
              plastic packages.

              Table 1.      Product overview
              Type number         Package                                     Configuration           Package
                                  NXP            JEITA         JEDEC                                  configuration

              BAV99               SOT23          -             TO-236AB       dual series             small
              BAV99S              SOT363         SC-88         -              quadruple; 2 series     very small
              BAV99W              SOT323         SC-70         -              dual series             very small


          1.2 Features and benefits
               High switching speed: trr ≤ 4 ns                     Low capacitance: Cd ≤ 1.5 pF
               Low leakage current                                  Reverse voltage: VR ≤ 100 V
               Small SMD plastic packages                           AEC-Q101 qualified


          1.3 Applications
               High-speed switching                                 Reverse polarity protection
               General-purpose switching


          1.4 Quick reference data
              Table 2.      Quick reference data
              Symbol          Parameter                   Conditions                  Min    Typ      Max     Unit
              Per diode
              IR              reverse current             VR = 80 V                   -      -        0.5     μA
              VR              reverse voltage                                         -      -        100     V
              trr             reverse recovery time                             [1]   -      -        4       ns

              [1]   When switched from IF = 10 mA to IR = 10 mA; RL = 100 Ω; measured at IR = 1 mA.
NXP Semiconductors                                                                                                                    BAV99 series
                                                                                                                              High-speed switching diodes



2. Pinning information
                     Table 3.      Pinning
                     Pin               Description                                                            Simplified outline              Graphic symbol
                     BAV99; BAV99W
                     1                 anode (diode 1)
                                                                                                                              3                               3
                     2                 cathode (diode 2)
                     3                 cathode (diode 1),
                                       anode (diode 2)
                                                                                                                      1                2
                                                                                                                                  006aaa144          1                 2
                                                                                                                                                                  006aaa763


                     BAV99S
                     1                 anode (diode 1)
                                                                                                                          6       5    4             6        5        4
                     2                 cathode (diode 2)
                     3                 cathode (diode 3),
                                       anode (diode 4)
                     4                 anode (diode 3)                                                                    1       2    3
                     5                 cathode (diode 4)                                                                                             1        2        3
                     6                 cathode (diode 1),                                                                                                         006aab101

                                       anode (diode 2)


3. Ordering information
                     Table 4.      Ordering information
                     Type number            Package
                                            Name                    Description                                                                               Version
                     BAV99                  -                       plastic surface-mounted package; 3 leads                                                  SOT23
                     BAV99S                 SC-88                   plastic surface-mounted package; 6 leads                                                  SOT363
                     BAV99W                 SC-70                   plastic surface-mounted package; 3 leads                                                  SOT323


4. Marking
                     Table 5.      Marking codes
                     Type number                                                                      Marking code[1]
                     BAV99                                                                            A7*
                     BAV99S                                                                           K1*
                     BAV99W                                                                           A7*

                     [1]   * = placeholder for manufacturing site code




BAV99_SER                                All information provided in this document is subject to legal disclaimers.                            © NXP B.V. 2010. All rights reserved.

Product data sheet                                   Rev. 8 — 18 November 2010                                                                                          2 of 14
NXP Semiconductors                                                                                                           BAV99 series
                                                                                                                        High-speed switching diodes



5. Limiting values
                     Table 6.   Limiting values
                     In accordance with the Absolute Maximum Rating System (IEC 60134).
                     Symbol            Parameter                                         Conditions                              Min    Max               Unit
                     Per diode
                     VRRM              repetitive peak reverse                                                                   -      100               V
                                       voltage
                     VR                reverse voltage                                                                           -      100               V
                     IF                forward current
                                          BAV99                                                                            [1]   -      215               mA
                                                                                                                           [2]   -      125               mA
                                          BAV99S                                                                           [1]   -      200               mA
                                          BAV99W                                                                           [1]   -      150               mA
                                                                                                                           [2]   -      130               mA
                     IFRM              repetitive peak forward                                                                   -      500               mA
                                       current
                     IFSM              non-repetitive peak                               square wave                       [3]

                                       forward current                                       tp = 1 μs                           -      4                 A
                                                                                             tp = 1 ms                           -      1                 A
                                                                                             tp = 1 s                            -      0.5               A
                     Ptot              total power dissipation                                                          [1][4]

                                          BAV99                                          Tamb ≤ 25 °C                            -      250               mW
                                          BAV99S                                         Tsp ≤ 85 °C                       [5]   -      250               mW
                                          BAV99W                                         Tamb ≤ 25 °C                            -      200               mW
                     Per device
                     Tj                junction temperature                                                                      -      150               °C
                     Tamb              ambient temperature                                                                       −65    +150              °C
                     Tstg              storage temperature                                                                       −65    +150              °C

                     [1]    Single diode loaded.
                     [2]    Double diode loaded.
                     [3]    Tj = 25 °C prior to surge.
                     [4]    Device mounted on an FR4 Printed-Circuit Board (PCB), single-sided copper, tin-plated and standard
                            footprint.
                     [5]    Soldering points at pins 2, 3, 5 and 6.




BAV99_SER                                  All information provided in this document is subject to legal disclaimers.                  © NXP B.V. 2010. All rights reserved.

Product data sheet                                     Rev. 8 — 18 November 2010                                                                                3 of 14
NXP Semiconductors                                                                                                          BAV99 series
                                                                                                                       High-speed switching diodes



6. Thermal characteristics
                     Table 7.      Thermal characteristics
                     Symbol           Parameter                                             Conditions                          Min   Typ           Max           Unit
                     Rth(j-a)         thermal resistance from                               in free air                [1][2]

                                      junction to ambient
                                         BAV99                                                                                  -     -             500           K/W
                                         BAV99W                                                                                 -     -             625           K/W
                     Rth(j-sp)        thermal resistance from
                                      junction to solder point
                                         BAV99                                                                                  -     -             360           K/W
                                         BAV99S                                                                           [3]   -     -             260           K/W
                                         BAV99W                                                                                 -     -             300           K/W

                     [1]   Single diode loaded.
                     [2]   Device mounted on an FR4 PCB, single-sided copper, tin-plated and standard footprint.
                     [3]   Soldering points at pins 2, 3, 5 and 6.


7. Characteristics
                     Table 8.   Characteristics
                     Tamb = 25 °C unless otherwise specified.
                     Symbol        Parameter                                     Conditions                                     Min   Typ           Max           Unit
                     Per diode
                     VF            forward voltage                               IF = 1 mA                                      -     -             715           mV
                                                                                 IF = 10 mA                                     -     -             855           mV
                                                                                 IF = 50 mA                                     -     -             1             V
                                                                                 IF = 150 mA                                    -     -             1.25          V
                     IR            reverse current                               VR = 25 V                                      -     -             30            nA
                                                                                 VR = 80 V                                      -     -             0.5           μA
                                                                                 VR = 25 V; Tj = 150 °C                         -     -             30            μA
                                                                                 VR = 80 V; Tj = 150 °C                         -     -             50            μA
                     Cd            diode capacitance                             f = 1 MHz; VR = 0 V                            -     -             1.5           pF
                     trr           reverse recovery time                                                                  [1]   -     -             4             ns
                     VFR           forward recovery voltage                                                               [2]   -     -             1.75          V

                     [1]   When switched from IF = 10 mA to IR = 10 mA; RL = 100 Ω; measured at IR = 1 mA.
                     [2]   When switched from IF = 10 mA; tr = 20 ns.




BAV99_SER                                 All information provided in this document is subject to legal disclaimers.                      © NXP B.V. 2010. All rights reserved.

Product data sheet                                    Rev. 8 — 18 November 2010                                                                                    4 of 14
NXP Semiconductors                                                                                                                                      BAV99 series
                                                                                                                                                    High-speed switching diodes




                                                                   006aab132                                                                                               006aab133
            103                                                                                                  102
                                                                                                                IR                                        (1)
       IF                                                                                                      (μA)
      (mA)                                                                                                         10

            102                                                                                                                                           (2)
                                                                                                                      1


                                                                                                                 10−1
            10
                                                                                                                                                          (3)
                                                                                                                 10−2


                                 (1)   (2)    (3)   (4)                                                          10−3
             1

                                                                                                                 10−4                                     (4)


        10−1                                                                                                     10−5
                  0    0.2   0.4        0.6         0.8   1.0       1.2    1.4                                            0            20          40           60     80            100
                                                                      VF (V)                                                                                                VR (V)


        (1) Tamb = 150 °C                                                                                        (1) Tamb = 150 °C
        (2) Tamb = 85 °C                                                                                         (2) Tamb = 85 °C
        (3) Tamb = 25 °C                                                                                         (3) Tamb = 25 °C
        (4) Tamb = −40 °C                                                                                        (4) Tamb = −40 °C
 Fig 1.           Forward current as a function of forward                                              Fig 2.            Reverse current as a function of reverse
                  voltage; typical values                                                                                 voltage; typical values

                                                                       mbg446                                                                                                mbg704
            0.8                                                                                                    102
        Cd
       (pF)                                                                                                    IFSM
                                                                                                                (A)
            0.6
                                                                                                                     10


            0.4


                                                                                                                      1

            0.2




              0                                                                                                  10−1
                  0          4                 8            12                 16                                         1                   10        102          103             104
                                                                   VR (V)                                                                                                  tp (μs)


                  f = 1 MHz; Tamb = 25 °C                                                                                 Based on square wave currents.
                                                                                                                          Tj = 25 °C; prior to surge
 Fig 3.           Diode capacitance as a function of reverse                                            Fig 4.            Non-repetitive peak forward current as a
                  voltage; typical values                                                                                 function of pulse duration; maximum values




BAV99_SER                                                        All information provided in this document is subject to legal disclaimers.                           © NXP B.V. 2010. All rights reserved.

Product data sheet                                                           Rev. 8 — 18 November 2010                                                                                         5 of 14
NXP Semiconductors                                                                                                                           BAV99 series
                                                                                                                                         High-speed switching diodes



8. Test information


                                                                                                  tr                 tp
                                                                                                                                         t
                                          D.U.T.
                                                                                                  10 %
            RS = 50 Ω
                                     IF                                                                                                      + IF                 trr
                                                           SAMPLING                                                                                                                t
                                                         OSCILLOSCOPE
        V = VR + IF × RS                                       Ri = 50 Ω
                                                                                                         90 %                                                                (1)
                                                                                       VR
                                                           mga881
                                                                                                              input signal                           output signal

        (1) IR = 1 mA
             Input signal: reverse pulse rise time tr = 0.6 ns; reverse voltage pulse duration tp = 100 ns; duty cycle δ = 0.05
             Oscilloscope: rise time tr = 0.35 ns
 Fig 5.      Reverse recovery time test circuit and waveforms

               I        1 kΩ        450 Ω
                                                                                   I                                                         V
                                                                                                    90 %

       RS = 50 Ω                            OSCILLOSCOPE                                                                                            VFR
                        D.U.T.
                                                   Ri = 50 Ω

                                                                                            10 %
                                                                                                                                     t                                             t
                                                                                             tr                tp

                                                                                                        input signal                                  output signal
                                                                                                                                                                           mga882


             Input signal: forward pulse rise time tr = 20 ns; forward current pulse duration tp ≥ 100 ns; duty cycle δ ≤ 0.005
 Fig 6.      Forward recovery voltage test circuit and waveforms


                        8.1 Quality information
                                 This product has been qualified in accordance with the Automotive Electronics Council
                                 (AEC) standard Q101 - Stress test qualification for discrete semiconductors, and is
                                 suitable for use in automotive applications.




BAV99_SER                                               All information provided in this document is subject to legal disclaimers.                        © NXP B.V. 2010. All rights reserved.

Product data sheet                                                  Rev. 8 — 18 November 2010                                                                                      6 of 14
NXP Semiconductors                                                                                                                            BAV99 series
                                                                                                                                          High-speed switching diodes



9. Package outline


                                                                                                                                    2.2                                 1.1
                          3.0                                  1.1                                                                  1.8                                 0.8
                          2.8                                  0.9

                                                                                                                             6            5    4         0.45
                                3                                                                                                                        0.15

                                                0.45
                                                0.15
     2.5 1.4                                                                                   2.2 1.35
     2.1 1.2                                                                                   2.0 1.15                      pin 1
                                                                                                                             index



                1                        2                                                                                   1            2    3
                                             0.48              0.15                                                                                0.3                  0.25
                                                                                                                             0.65                  0.2                  0.10
                                             0.38              0.09
                          1.9                                                                                                       1.3

       Dimensions in mm                                            04-11-04                    Dimensions in mm                                                                06-03-16


 Fig 7.     Package outline BAV99 (SOT23/TO-236AB)                                     Fig 8.           Package outline BAV99S (SOT363/SC-88)


                                                                         2.2                                          1.1
                                                                         1.8                                          0.8

                                                                                3                   0.45
                                                                                                    0.15



                                       2.2 1.35
                                       2.0 1.15




                                                          1                                2
                                                                                                0.4                    0.25
                                                                                                0.3                    0.10
                                                                         1.3

                                        Dimensions in mm                                                                         04-11-04


 Fig 9.     Package outline BAV99W (SOT323/SC-70)


10. Packing information
                          Table 9.    Packing methods
                          The indicated -xxx are the last three digits of the 12NC ordering code.[1]
                          Type number           Package               Description                                                                        Packing quantity
                                                                                                                                                         3000               10000
                          BAV99                 SOT23                 4 mm pitch, 8 mm tape and reel                                                     -215               -235
                          BAV99S                SOT363                4 mm pitch, 8 mm tape and reel; T1                                           [2]   -115               -135
                                                                      4 mm pitch, 8 mm tape and reel; T2                                           [3]   -125               -165
                          BAV99W                SOT323                4 mm pitch, 8 mm tape and reel                                                     -115               -135

                          [1]   For further information and the availability of packing methods, see Section 14.
                          [2]   T1: normal taping
                          [3]   T2: reverse taping


BAV99_SER                                       All information provided in this document is subject to legal disclaimers.                                 © NXP B.V. 2010. All rights reserved.

Product data sheet                                          Rev. 8 — 18 November 2010                                                                                               7 of 14
NXP Semiconductors                                                                                                                BAV99 series
                                                                                                                              High-speed switching diodes



11. Soldering

                                                                   3.3

                                                                   2.9

                                                                   1.9




                                                                                                                                                            solder lands


                                                                                                                                                            solder resist
                      3    1.7                                                                                       2

                                                                                                                                                            solder paste


                                  0.7                                                                       0.6                                             occupied area
                                 (3×)                                                                      (3×)
                                                                                                                                              Dimensions in mm

                                                                   0.5
                                                                  (3×)
                                                                   0.6
                                                                  (3×)

                                                                    1                                                                                                sot023_fr


                     Fig 10. Reflow soldering footprint BAV99 (SOT23/TO-236AB)

                                                                           2.2
                                                        1.2
                                                       (2×)




                                  1.4
                                 (2×)


                                                                                                                                                              solder lands


                     4.6   2.6                                                                                                                                solder resist


                                                                                                                                                              occupied area

                                                                                                                                               Dimensions in mm
                                 1.4




                                                                                                                         preferred transport direction during soldering

                                                                           2.8

                                                                           4.5                                                                                       sot023_fw


                     Fig 11. Wave soldering footprint BAV99 (SOT23/TO-236AB)




BAV99_SER                               All information provided in this document is subject to legal disclaimers.                               © NXP B.V. 2010. All rights reserved.

Product data sheet                                  Rev. 8 — 18 November 2010                                                                                             8 of 14
NXP Semiconductors                                                                                                     BAV99 series
                                                                                                                     High-speed switching diodes




                                                                          2.65




                                                                                                                                  solder lands
                            2.35 1.5     0.6 0.5                                                          0.4 (2×)
                                        (4×) (4×)                                                                                 solder resist


                                                                                                                                  solder paste

                                                               0.5                      0.6                                       occupied area
                                                              (4×)                     (2×)
                                                               0.6                                                       Dimensions in mm
                                                              (4×)
                                                                           1.8                                                            sot363_fr


                     Fig 12. Reflow soldering footprint BAV99S (SOT363/SC-88)




                                                                                                    1.5


                                                                                                                                            solder lands
                      4.5                                                                                  0.3 2.5
                                                                                                                                            solder resist


                                                                                                                                            occupied area
                                                                                                    1.5
                                                                                                                               Dimensions in mm


                                                                                                                                   preferred transport
                                       1.3                               1.3                                                   direction during soldering

                                                       2.45

                                                        5.3                                                                                         sot363_fw


                     Fig 13. Wave soldering footprint BAV99S (SOT363/SC-88)




BAV99_SER                              All information provided in this document is subject to legal disclaimers.                © NXP B.V. 2010. All rights reserved.

Product data sheet                                 Rev. 8 — 18 November 2010                                                                              9 of 14
NXP Semiconductors                                                                                                             BAV99 series
                                                                                                                             High-speed switching diodes




                                                                 2.65

                                                                 1.85

                                                                            1.325
                                                                                                                                           solder lands


                                                                            2                                                              solder resist

                                    0.6                   3                                                                                solder paste
                            2.35                                                                        1.3
                                   (3×)

                                                                                                 0.5                                       occupied area
                                                                            1
                                                                                                (3×)
                                                                                                                                  Dimensions in mm

                                                0.55
                                                (3×)                                                                                               sot323_fr


                     Fig 14. Reflow soldering footprint BAV99W (SOT323/SC-70)

                                                                    4.6

                                                                   2.575
                                              1.425
                                               (3×)
                                                                                                                                                     solder lands


                                                                                                                                                     solder resist


                                                                                                                                                     occupied area

                      3.65 2.1                                                                                         1.8              Dimensions in mm


                                                                                                                 09                        preferred transport
                                                                                                                (2×)                   direction during soldering


                                                                                                                                                            sot323_fw


                     Fig 15. Wave soldering footprint BAV99W (SOT323/SC-70)




BAV99_SER                                 All information provided in this document is subject to legal disclaimers.                      © NXP B.V. 2010. All rights reserved.

Product data sheet                                    Rev. 8 — 18 November 2010                                                                                  10 of 14
NXP Semiconductors                                                                                                        BAV99 series
                                                                                                                        High-speed switching diodes



12. Revision history
Table 10.   Revision history
Document ID               Release date             Data sheet status                                        Change notice    Supersedes
BAV99_SER_8               20101118                 Product data sheet                                       -                BAV99_SER_7
Modifications:                 • Section 4 “Marking”: marking placeholder explanation in table footer updated
                               • Section 5 “Limiting values”: Ptot condition for BAV99S corrected
                               • Section 13 “Legal information”: updated
BAV99_SER_7               20100414                 Product data sheet                                       -                BAV99_SER_6
BAV99_SER_6               20100310                 Product data sheet                                       -                BAV99_SER_5
BAV99_SER_5               20080820                 Product data sheet                                       -                BAV99_4
                                                                                                                             BAV99S_3
                                                                                                                             BAV99W_4
BAV99_4                   20011015                 Product specification                                    -                BAV99_3
BAV99S_3                  20010514                 Product specification                                   -                 BAV99S_N_2
BAV99W_4                  19990511                 Product specification                                   -                 BAV99W_3




BAV99_SER                                  All information provided in this document is subject to legal disclaimers.             © NXP B.V. 2010. All rights reserved.

Product data sheet                                     Rev. 8 — 18 November 2010                                                                         11 of 14
NXP Semiconductors                                                                                                                               BAV99 series
                                                                                                                                               High-speed switching diodes



13. Legal information

13.1 Data sheet status
Document status[1][2]                  Product status[3]                    Definition
Objective [short] data sheet           Development                          This document contains data from the objective specification for product development.
Preliminary [short] data sheet         Qualification                        This document contains data from the preliminary specification.
Product [short] data sheet             Production                           This document contains the product specification.

[1]   Please consult the most recently issued document before initiating or completing a design.
[2]   The term ‘short data sheet’ is explained in section “Definitions”.
[3]   The product status of device(s) described in this document may have changed since this document was published and may differ in case of multiple devices. The latest product status
      information is available on the Internet at URL http://www.nxp.com.



13.2 Definitions                                                                                           malfunction of an NXP Semiconductors product can reasonably be expected
                                                                                                           to result in personal injury, death or severe property or environmental
                                                                                                           damage. NXP Semiconductors accepts no liability for inclusion and/or use of
Draft — The document is a draft version only. The content is still under
                                                                                                           NXP Semiconductors products in such equipment or applications and
internal review and subject to formal approval, which may result in
                                                                                                           therefore such inclusion and/or use is at the customer’s own risk.
modifications or additions. NXP Semiconductors does not give any
representations or warranties as to the accuracy or completeness of                                        Applications — Applications that are described herein for any of these
information included herein and shall have no liability for the consequences of                            products are for illustrative purposes only. NXP Semiconductors makes no
use of such information.                                                                                   representation or warranty that such applications will be suitable for the
                                                                                                           specified use without further testing or modification.
Short data sheet — A short data sheet is an extract from a full data sheet
with the same product type number(s) and title. A short data sheet is intended                             Customers are responsible for the design and operation of their applications
for quick reference only and should not be relied upon to contain detailed and                             and products using NXP Semiconductors products, and NXP Semiconductors
full information. For detailed and full information see the relevant full data                             accepts no liability for any assistance with applications or customer product
sheet, which is available on request via the local NXP Semiconductors sales                                design. It is customer’s sole responsibility to determine whether the NXP
office. In case of any inconsistency or conflict with the short data sheet, the                            Semiconductors product is suitable and fit for the customer’s applications and
full data sheet shall prevail.                                                                             products planned, as well as for the planned application and use of
                                                                                                           customer’s third party customer(s). Customers should provide appropriate
Product specification — The information and data provided in a Product                                     design and operating safeguards to minimize the risks associated with their
data sheet shall define the specification of the product as agreed between                                 applications and products.
NXP Semiconductors and its customer, unless NXP Semiconductors and
customer have explicitly agreed otherwise in writing. In no event however,                                 NXP Semiconductors does not accept any liability related to any default,
shall an agreement be valid in which the NXP Semiconductors product is                                     damage, costs or problem which is based on any weakness or default in the
deemed to offer functions and qualities beyond those described in the                                      customer’s applications or products, or the application or use by customer’s
Product data sheet.                                                                                        third party customer(s). Customer is responsible for doing all necessary
                                                                                                           testing for the customer’s applications and products using NXP
                                                                                                           Semiconductors products in order to avoid a default of the applications and
13.3 Disclaimers                                                                                           the products or of the application or use by customer’s third party
                                                                                                           customer(s). NXP does not accept any liability in this respect.

Limited warranty and liability — Information in this document is believed to                               Limiting values — Stress above one or more limiting values (as defined in
be accurate and reliable. However, NXP Semiconductors does not give any                                    the Absolute Maximum Ratings System of IEC 60134) will cause permanent
representations or warranties, expressed or implied, as to the accuracy or                                 damage to the device. Limiting values are stress ratings only and (proper)
completeness of such information and shall have no liability for the                                       operation of the device at these or any other conditions above those given in
consequences of use of such information.                                                                   the Recommended operating conditions section (if present) or the
                                                                                                           Characteristics sections of this document is not warranted. Constant or
In no event shall NXP Semiconductors be liable for any indirect, incidental,
                                                                                                           repeated exposure to limiting values will permanently and irreversibly affect
punitive, special or consequential damages (including - without limitation - lost
                                                                                                           the quality and reliability of the device.
profits, lost savings, business interruption, costs related to the removal or
replacement of any products or rework charges) whether or not such                                         Terms and conditions of commercial sale — NXP Semiconductors
damages are based on tort (including negligence), warranty, breach of                                      products are sold subject to the general terms and conditions of commercial
contract or any other legal theory.                                                                        sale, as published at http://www.nxp.com/profile/terms, unless otherwise
Notwithstanding any damages that customer might incur for any reason                                       agreed in a valid written individual agreement. In case an individual
whatsoever, NXP Semiconductors’ aggregate and cumulative liability towards                                 agreement is concluded only the terms and conditions of the respective
customer for the products described herein shall be limited in accordance                                  agreement shall apply. NXP Semiconductors hereby expressly objects to
with the Terms and conditions of commercial sale of NXP Semiconductors.                                    applying the customer’s general terms and conditions with regard to the
                                                                                                           purchase of NXP Semiconductors products by customer.
Right to make changes — NXP Semiconductors reserves the right to make
changes to information published in this document, including without                                       No offer to sell or license — Nothing in this document may be interpreted or
limitation specifications and product descriptions, at any time and without                                construed as an offer to sell products that is open for acceptance or the grant,
notice. This document supersedes and replaces all information supplied prior                               conveyance or implication of any license under any copyrights, patents or
to the publication hereof.                                                                                 other industrial or intellectual property rights.

Suitability for use — NXP Semiconductors products are not designed,                                        Export control — This document as well as the item(s) described herein
authorized or warranted to be suitable for use in life support, life-critical or                           may be subject to export control regulations. Export might require a prior
safety-critical systems or equipment, nor in applications where failure or                                 authorization from national authorities.


BAV99_SER                                                         All information provided in this document is subject to legal disclaimers.                   © NXP B.V. 2010. All rights reserved.

Product data sheet                                                            Rev. 8 — 18 November 2010                                                                               12 of 14
NXP Semiconductors                                                                                                                     BAV99 series
                                                                                                                                     High-speed switching diodes


Quick reference data — The Quick reference data is an extract of the
product data given in the Limiting values and Characteristics sections of this
                                                                                                 13.4 Trademarks
document, and as such is not complete, exhaustive or legally binding.                            Notice: All referenced brands, product names, service names and trademarks
                                                                                                 are the property of their respective owners.



14. Contact information
For more information, please visit: http://www.nxp.com
For sales office addresses, please send an email to: salesaddresses@nxp.com




BAV99_SER                                               All information provided in this document is subject to legal disclaimers.               © NXP B.V. 2010. All rights reserved.

Product data sheet                                                  Rev. 8 — 18 November 2010                                                                           13 of 14
NXP Semiconductors                                                                                                         BAV99 series
                                                                                                                       High-speed switching diodes



15. Contents
1      Product profile . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.1      General description . . . . . . . . . . . . . . . . . . . . . 1
1.2      Features and benefits . . . . . . . . . . . . . . . . . . . . 1
1.3      Applications . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.4      Quick reference data . . . . . . . . . . . . . . . . . . . . 1
2      Pinning information . . . . . . . . . . . . . . . . . . . . . . 2
3      Ordering information . . . . . . . . . . . . . . . . . . . . . 2
4      Marking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
5      Limiting values. . . . . . . . . . . . . . . . . . . . . . . . . . 3
6      Thermal characteristics . . . . . . . . . . . . . . . . . . 4
7      Characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . 4
8      Test information . . . . . . . . . . . . . . . . . . . . . . . . . 6
8.1      Quality information . . . . . . . . . . . . . . . . . . . . . . 6
9      Package outline . . . . . . . . . . . . . . . . . . . . . . . . . 7
10     Packing information . . . . . . . . . . . . . . . . . . . . . 7
11     Soldering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
12     Revision history . . . . . . . . . . . . . . . . . . . . . . . . 11
13     Legal information. . . . . . . . . . . . . . . . . . . . . . . 12
13.1     Data sheet status . . . . . . . . . . . . . . . . . . . . . . 12
13.2     Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
13.3     Disclaimers . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
13.4     Trademarks. . . . . . . . . . . . . . . . . . . . . . . . . . . 13
14     Contact information. . . . . . . . . . . . . . . . . . . . . 13
15     Contents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14




                                                                                   Please be aware that important notices concerning this document and the product(s)
                                                                                   described herein, have been included in section ‘Legal information’.


                                                                                   © NXP B.V. 2010.                                             All rights reserved.
                                                                                   For more information, please visit: http://www.nxp.com
                                                                                   For sales office addresses, please send an email to: salesaddresses@nxp.com
                                                                                                                                        Date of release: 18 November 2010
                                                                                                                                         Document identifier: BAV99_SER
