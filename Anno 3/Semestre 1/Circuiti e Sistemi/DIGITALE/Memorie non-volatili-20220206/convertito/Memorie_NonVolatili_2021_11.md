---
fonte: "Memorie_NonVolatili_2021_11.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Read-Only Memory Cells
 BL not isolated
                             BL                  BL                 BL
 from WL                                   VDD
           WL
                                   WL                 WL
      1


                             BL                  BL                 BL

           WL                      WL
                                                      WL
      0
                                                              GND


                Diode ROM               MOS ROM 1          MOS ROM 2



© Digital Integrated Circuits2nd                                  Memories
      MOS OR ROM
                                                                     Data stored at
                                   BL[0]   BL[1]    BL[2]    BL[3]
                                                                     address 0,1,2,3 ?

                   WL[0]
                                                                      V DD
                   WL[1]


                   WL[2]
                                                                      V DD

                   WL[3]


                    V bias

                                           Pull-down loads


© Digital Integrated Circuits2nd                                             Memories
      MOS NOR ROM                               Data stored at
                                                address 0,1,2,3 ?
                                                                     V DD
                                                                 Pull-up devices


             WL[0]

                                                                     GND
             WL [1]


             WL [2]

                                                                     GND
             WL [3]



                             BL [0]   BL [1]   BL [2]   BL [3]


© Digital Integrated Circuits2nd                                               Memories
MOS NOR ROM Layout                 A large part of the cell
Cell (11λ x 7λ)                    is devoted to contacts
                                   to bitline and GND

                                   Programmming using
                                   the Contact Layer Only



                                          Polysilicon

                                          Metal1

                                          Diffusion

                                          Metal1 on Diffusion



© Digital Integrated Circuits2nd                      Memories
      MOS NAND ROM
                                                    Data stored at
                                                    address 0,1,2,3 ?

                                                                    V DD
                                                             Pull-up devices

                                   BL [0]   BL[1]   BL[2]   BL[3]

            WL [0]


            WL [1]


            WL [2]

                                                                    Transistors that are not
            WL [3]                                                  present cannot be switched
                                                                    OFF, namely they cannot be
                                                                    selected
         All word lines high by default with exception of selected row

© Digital Integrated Circuits2nd                                               Memories
      MOS NAND ROM Layout
                                     Cell (8λ x 7λ)

                                     Programmming using
                                     the Metal-1 Layer Only

                                   No contact to VDD or GND necessary;
                                   drastically reduced cell size
                                   Loss in performance compared to NOR ROM



                                                      Polysilicon

                                                      Diffusion

                                                      Metal1 on Diffusion



© Digital Integrated Circuits2nd                                  Memories
      NAND ROM Layout
Cell (5λ x 6λ)

                                          Programmming using
                                          Implants Only




                                                Polysilicon

                                                Threshold-altering
 n-type implant turns the device into a         implant
 depletion transistor that is always ON         Metal1 on Diffusion
 regardless of the word line voltage

© Digital Integrated Circuits2nd                       Memories
      Equivalent Transient Model for MOS NOR ROM
                Model for NOR ROM                         V DD



                                                                   BL
                                                  rword
                                     WL                          Cbit

                                          cword




       Word line parasitics
             Wire capacitance and gate capacitance
             Wire resistance (polysilicon)
       Bit line parasitics
             Resistance not dominant (metal)
             Drain and Gate-Drain capacitance

© Digital Integrated Circuits2nd                                        Memories
     Equivalent Transient Model for MOS NAND ROM

                                                                    V DD
                  Model for NAND ROM
                                                                                  BL

                                                                                  CL
                                                                r bit

                                                                           cbit
                                                       r word
                                             WL

                                               cword




       Word line parasitics
             Similar to NOR ROM
       Bit line parasitics
             Resistance of cascaded transistors dominates
             Drain/Source and complete gate capacitance


© Digital Integrated Circuits2nd                                                  Memories
   Decreasing Word Line Delay
                     Driver
               WL                         Polysilicon word line



                                          Metal word line

                          (a) Driving the word line from both sides

                                                                    Metal bypass




               WL      K cells                                    Polysilicon word line

                                   (b) Using a metal bypass

                                      (c) Use silicides

© Digital Integrated Circuits2nd                                                          Memories
      Precharged MOS NOR ROM
                     f pre                                            V DD

                                                                 Precharge devices


                 WL [0]

                                                                      GND
                 WL [1]



                 WL [2]
                                                                      GND
                 WL [3]



                             BL [0]   BL [1]   BL [2]   BL [3]


          PMOS precharge device can be made as large as necessary,
          but clock driver becomes harder to design.

© Digital Integrated Circuits2nd                                                     Memories
      Non-Volatile Memories
      The Floating-gate transistor (FAMOS)

               Floating gate               Gate
                                                                      D
      Source                                        Drain

                                            tox              G

                                            tox
                                                                      S
              n+                       p          n+_
                           Substrate


                   Device cross-section                     Schematic symbol




© Digital Integrated Circuits2nd                                      Memories
      Floating-Gate Transistor Programming

                20 V                            0V                           5V



             10 V     5V    20 V                 -5V      0V                - 2.5 V     5V


       S                      D         S                 D          S                  D


      Hot-carrier injection        Removing programming            Programming results in
                                   voltage leaves charge trapped      higher V T .




© Digital Integrated Circuits2nd                                                  Memories
      A “Programmable-Threshold” Transistor

                 ID                “ 0” -state   “ 1” -state


                                     “ ON ”

                                          DV T




                                    “ OFF”
                                   V WL                        V GS



© Digital Integrated Circuits2nd                                      Memories
      FLOTOX EEPROM
      Floating gate                      Gate                         I

  Source                                             Drain

                           20–30 nm                           -10 V              V GD

                                                                          10 V

          n1                                    n1
                          Substrate
                             p
                                      10 nm

                                                             Fowler-Nordheim
               FLOTOX transistor
                                                             I-V characteristic




© Digital Integrated Circuits2nd                                            Memories
      EEPROM Cell
                                   BL


           WL
                                        Absolute threshold control
                                        is hard
          VDD                           Unprogrammed transistor
                                        might be depletion
                                        Ö 2 transistor cell




© Digital Integrated Circuits2nd                            Memories
      Flash EEPROM

                                    Control gate
                                                       Floating gate

            erasure                                    Thin tunneling oxide

          n 1+ source                              n 1+ drain
                                   programming
                                     p-substrate


       Many other options …


© Digital Integrated Circuits2nd                                         Memories
Cross-sections of NVM cells




                  Flash                             EPROM
© Digital Integrated Circuits2nd   Courtesy Intel       Memories
  Basic Operations in a NOR Flash Memory―
  Erase

                  cell                           array
                                          BL 0           BL 1
                         G
        12 V
                                   0V                           WL 0
            S                  D
                                   12 V

                                   0V                           WL 1


                                          open           open


© Digital Integrated Circuits2nd                                Memories
  Basic Operations in a NOR Flash Memory―
  Write
                  12 V                    BL 0   BL 1
                     G
                             6V
                                   12 V                 WL 0
          S                  D
                                   0V

                                   0V                   WL 1


                                          6V     0V



© Digital Integrated Circuits2nd                         Memories
  Basic Operations in a NOR Flash Memory―
  Read
                                             BL 0   BL 1
                     5V
                       G
                                   1V
                                        5V                 WL 0
             S                     D
                                        0V

                                        0V                 WL 1


                                             1V     0V




© Digital Integrated Circuits2nd                           Memories
      NAND Flash Memory
        Word line(poly)




                     Unit Cell                                 Gate
                                                              ONO


                                                      Gate            FG
                                                      Oxide




          Source line
          (Diff. Layer)


© Digital Integrated Circuits2nd   Courtesy Toshiba                   Memories
      NAND Flash Memory
                       Select transistor         Word lines



            Active area

                          STI



                    Bit line contact               Source line contact


© Digital Integrated Circuits2nd       Courtesy Toshiba              Memories
    Characteristics of State-of-the-art NVM




© Digital Integrated Circuits2nd        Memories
