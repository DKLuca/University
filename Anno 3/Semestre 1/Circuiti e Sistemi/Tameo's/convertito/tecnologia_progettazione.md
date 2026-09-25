---
fonte: "tecnologia_progettazione.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Corso di Laurea in Ingegneria Elettronica - Università degli Studi di Udine




        Tecnologia e Progettazione di
    MEMORIE NON VOLATILI
                                                 Agostino Pirovano
                                                             Roberto Bez
                                                     Alessandro Grossi
                                                         Giorgio Servalli

                                                           Process R&D

                                                                   Micron

                                         Agrate Brianza (Milan), Italy

                          ©2009 Micron Technologies, Inc. All rights reserved. Products are warranted only to meet Micron’s production data sheet specifications. Information, products, and/or specifications
                          are subject to change without notice. All information is provided on an “AS IS” basis without warranties of any kind. Dates are estimates only. Drawings are not to scale. Micron and
                          the Micron logo are trademarks of Micron Technology, Inc. All other trademarks are the property of their respective owners.

                                                                                                                                                |     ©2009 Micron Technology, Inc.                  |      1




                              Tecnologia e Progettazione di
                             MEMORIE NON VOLATILI                                                                                                                                 1

•   PANORAMICA SULLE MEMORIE NON VOLATILI

•   CELLA DI MEMORIA A FLOATING GATE

    ▶   PRINCIPI DI FUNZIONAMENTO

    ▶   COEFFICIENTI CAPACITIVI

    ▶   SCRITTURA DELLA CELLA A FLOATING GATE
          • cancellazione UV
          • scrittura per Fowler-Nordheim tunnelling
          • programmazione per Channel Hot Electrons



                                                                                                             Company Confidential               |     ©2009 Micron Technology, Inc.                  |      2




                                                                                                                                                                                                                  1
                              Tecnologia e Progettazione di
                             MEMORIE NON VOLATILI                                                          2
•   DISPOSITIVO FLASH NOR
    ▶   FUNZIONAMENTO DEL DISPOSITIVO
            • organizzazione della matrice di memoria NOR

            • lettura, programmazione e cancellazione

    ▶   AFFIDABILITA' DELLA MEMORIA
            • disturbi di programmazione e lettura

            • endurance e ritenzione

    ▶   TESTING E RESA
    ▶   DISPOSITIVI MULTILIVELLO
•   DISPOSITIVO FLASH NAND
    ▶   FUNZIONAMENTO DEL DISPOSITIVO
            • organizzazione della matrice di memoria NAND

            • lettura, programmazione e cancellazione

                                                            Company Confidential   |   ©2009 Micron Technology, Inc.   |   3




                              Tecnologia e Progettazione di
                             MEMORIE NON VOLATILI
                                                                                                              3
        •     PROBLEMI DI SCALABILITA’ DELLE MEMORIE FLASH

               ▶   Elementi attivi
               ▶   Elementi passivi


        •     ALTRE MEMORIE NON VOLATILI

               ▶   FERAM
               ▶   MRAM and STT-MRAM
               ▶   RRAM



                                                            Company Confidential   |   ©2009 Micron Technology, Inc.   |   4




                                                                                                                               2
                                      Tecnologia e Progettazione di
                                     MEMORIE NON VOLATILI                                                                     4

    • AN OUTLOOK INTO THE FUTURE
          ▶ Una lezione sullo scaling

          ▶ Memorie a cambiamento di fase (PCM)

          ▶ Possibili evolzioni delle memorie PCM

          ▶ Memorie a cross-point




                                                                               Company Confidential   |   ©2009 Micron Technology, Inc.   |   5




                                      Tecnologia e Progettazione di
                                     MEMORIE NON VOLATILI

                                                    glossario
•   Array efficiency: rapporto tra area della matrice di        •   Fowler-Nordheim tunneling: tunnel di elettroni attraverso
    memoria e area dell'intero chip                                 una barriera di potenziale triangolare, usatoo per la
•   Bit (binary digit): unità base di memoria, "1" o "0"            scrittura nelle EEPROM e nelle FLASH
•   BitLine: linea di interconnessione per le operazioni di     •   Hot electron injection: iniezione di elettroni caldi dal
    I/O della matrice di memoria                                    canale del transistore nella floating gate, oltre la barriera di
                                                                    potenziale dell'ossido
•   Byte: gruppo di bits che vengono letti simultaneamente
                                                                •   Memoria Non Volatile: memoria i cui dati sono mantenuti
•   Cancellazione: l'operazione di rimozione di elettroni           senza la necessità di una alimentazione esterna
    dalla floating gate
                                                                •   Memoria Volatile: memoria i cui dati sono mantenuti
•   Cella: il dispositivo a semiconduttore che immagazzina          mediante una alimentazione esterna e/o un continuo
    un bit (o più bit )                                             refresh
•   Control Gate: gate di controllo del transistore di          •   ONO (Ossido-Nitruro-Ossido): dielettrico utilizzato come
    memoria tramite accoppiamento capacitivo                        isolante tra control gate e floating gate
•   Disturbo: indesiderato cambiamento dello stato della        •   Ossido di tunnel : ossido di gate abbastanza sottile da
    memoria durante le operazioni di scrittura o lettura            permettere il Fowler - Nordheim tunneling
•   ECC (error correction code): tecnica per correggere         •   Programmazione: l'operazione di iniezione di elettroni
    errori in una memoria migliorando affidabilità e resa           nella floating gate
•   Endurance: numero di cicli di scrittura/cancellazione che   •   Ridondanza: tecnica di progettazione che migliora la resa
    una memoria garantisce                                          di un dispositivo mediante l'utilizzo di celle di scorta, che
•   Ferroelettrico: materiale con caratteristiche di                possono sostituire eventuali celle difettose
    polarizzazione elettrica permanenti, la cui polarità può    •   Ritenzione: capacità di mantenere la carica immagazzinata
    essere modificata mediante campo elettrico                      nella cella
•   Floating gate: gate in silicio policristallino              •   Scrittura: l'operazione generica di variazione dello stato
    completamente isolata mediante dielettrici                      della memoria (programmazione o cancellazione)



                                                                               Company Confidential   |   ©2009 Micron Technology, Inc.   |   6




                                                                                                                                                  3
            Le memorie a semiconduttore


     Memorie a semiconduttore

Memorie Volatili                        Memorie Non Volatili
                                                                                                            ENVM
SRAM                DRAM                            ROM              EPROM

 Memoria Volatile:         l’informazione rimane
                                                                OTP
                           memorizzata solo finché
                           il dispositivo è alimentato             EEPROM

 Memoria Non Volatile: l’informazione rimane                          FLASH
                       memorizzata anche se il
                       dispositivo non è alimentato




                                                          Company Confidential   |       ©2009 Micron Technology, Inc.   |   7




     Memorie: proprietà fondamentali

                                              ROM
                                                                                     ALTERABILITA’




                                               OTP
              RITENZIONE




                                           EPROM

                                           FLASH

                                          EEPROM

                                             DRAM

                                             SRAM

                                                          Company Confidential   |       ©2009 Micron Technology, Inc.   |   8




                                                                                                                                 4
Un esempio: l’iPod


            Cosa vediamo dall’esterno?


            •   L’estetica


            •   L’interfaccia:
                ▶     Input:
                         • Sensori tattili

                ▶     Output
                         • Display LCD
                         • Cuffie



                Company Confidential   |   ©2009 Micron Technology, Inc.   |   9




 Dentro l’iPod - 1

            Step-down switching regulator




            Audio CODEC




            USB power manager




                Company Confidential   |   ©2009 Micron Technology, Inc.   |   10




                                                                                    5
Dentro l’iPod - 2


           8Mb multi-purpose Flash NOR


            256Mb mobile DRAM




           ARM core DSP + Flash controller




                Company Confidential   |   ©2009 Micron Technology, Inc.   |   11




Dentro l’iPod - 3



         32Gb (2x) multi-level NAND Flash


                              or
            64Gb (dual-stacked)
            multi-level NAND Flash



               Power manager




                Company Confidential   |   ©2009 Micron Technology, Inc.   |   12




                                                                                    6
32Gb (2x) NAND Flash




              Company Confidential   |   ©2009 Micron Technology, Inc.   |   13




   8Gb NAND dice




              Company Confidential   |   ©2009 Micron Technology, Inc.   |   14




                                                                                  7
                               IC and memory markets




                                      15                                     Company Confidential    |   ©2009 Micron Technology, Inc.   |   15




                                           Memory market
                        100                                                                                 1000
    Total Volume (Eb)




                         10                                                                                 100
                                                                                                                       Price ($/Gb)




                          1                                                                                 10


                         0.1                                                                                1


                        0.01                                                                                0.1
                               2000        2002        2004          2006      2008                 2010

                                                              Year
                                             NAND Eb   DRAM Eb   NAND $/Gb   DRAM $/Gb



In the last years the production volume of DRAM and in particular of
NAND Flash increased exponentially with a clear cost reduction trend

                                                                             Company Confidential    |   ©2009 Micron Technology, Inc.   |   16




                                                                                                                                                  8
               NVM application boosting

  The continuous decrease of the cost/Gb has boosted the
   introduction of NVM in a wide spectrum of applications




                                       Company Confidential   |   ©2009 Micron Technology, Inc.   |   17




 Dal transistore alla cella di memoria


 soglia di un transistore
     MOS n-channel
  Vt = VFB +VS + 2 Φp +                 la tensione di soglia
  +
     1
    Cox
                (
        2εqNa 2 Φp +VS −VB     )     di un transistore dipende
                                        dalla carica presente
                                      tra la gate e il substrato
dipendenza della tensione
 di flat band dalla carica
   presente nell’ossido
                                       Vt = Vt Q=0 − k ⋅ Q
                      t
              Qf   1 ox x
                            ρ(x)dx
              Cox Cox ∫0 tox
VFB = ΦMS −      −




                                       Company Confidential   |   ©2009 Micron Technology, Inc.   |   18




                                                                                                           9
     La cella FLASH: sezione lungo L


                   isolamento della                                sezione al
                        floating gate                        microscopio elettronico
                                                                               150000:1
 ossido
 interpoly         control gate
                  control  gate          contatto
                       polySi n+
                      polySi  n+         al drain
 ossido            floating gate
                  floating  gate
 di tunnel             polySi n+
                      polySi  n+

     source n+                  drain n+
                   lunghezza
                   di canale L                                             L=0.28µm
                             substrato Si p-



                                                        Company Confidential    |   ©2009 Micron Technology, Inc.   |   19




                 Struttura a bande della cella


struttura del     y
transistore a
floating gate
                               z

                                                                                                       ∆E(Q)


                                                    3.2 eV                                            3.2 eV
                                    Ec                                    Ec
                  E
diagramma                           Ef                                    Ef
della struttura                     Ev                                    Ev
a bande                                             4.0 eV                                            4.0 eV
                               z


                                   stato cancellato                   stato programmato
                                          “1”                                 “0”


                                                        Company Confidential    |   ©2009 Micron Technology, Inc.   |   20




                                                                                                                             10
      La cella FLASH a floating gate
                                                                                          G

layout cella                                                                                                  FG
Flash NOR
                                                                        S                                          D



       ossido interpoly                                                     ossido interpoly                 ossido di tunnel
                                                contatto
                          control gate
                                                al drain                                       control gate
      ossido di tunnel
                          floating gate
                                                                                          floating gate
            source n+                      drain n+
                                                                             ossido di                           ossido di
                           lunghezza                                                          larghezza di       isolamento
                                                                             isolamento
                           di canale L                                                        canale W

                                          substrato p-                                                         substrato p-



            sezione lungo L                                                    sezione lungo W

                                                                        Company Confidential       |      ©2009 Micron Technology, Inc.   |   21




     La cella FLASH: sezione lungo W


                                                                                  sezione al
                                                  ossido di tunnel          microscopio elettronico
ossido interpoly                                                                                   200000:1



                          control gate
                floating gate
ossido di                                                  ossido di
isolamento                larghezza di                     isolamento                             W=0.16µm
                          canale W

                                                 Substrato Si p-




                                                                        Company Confidential       |      ©2009 Micron Technology, Inc.   |   22




                                                                                                                                                   11
Floating gate e rapporti capacitivi

                                           La cella di memoria a floating gate è
                                           schematizzabile come un circuito di 4
                                           condensatori in parallelo:


                VG                            ∑C ⋅ (V −V ) = Q
                                          i =S ,B ,D ,G
                                                       i   FG           i             FG

      C
                                                                                                ∑C
      G
                VFG                        Definiti la capacità totale: CTOT =                            i
                                                                                            i = S ,B , D,G

CS    CB                 CD
                                           e i rapporti capacitivi:              αi = Ci CTOT < 1
 VS                    VD
           VB
                                           la tensione di floating gate dipende dalle
                                           tensioni ai capi della cella:


                                                           QFG
                                             VFG =             + ∑ αi ⋅Vi
                                                           CTOT i =S ,B,D,G


                                                               Company Confidential    |   ©2009 Micron Technology, Inc.   |   23




 Corrente nella cella di memoria

 Corrente in un transistore MOS:

                                    [
                I Dtrans = βtrans ⋅ (VGtrans − VTtrans )⋅VD     ]

 Corrente in una cella a floating gate:

                                [
                I Dcell = βtrans ⋅ ( VFG − VTtrans )⋅VD =  ]
                                                  Q               
                = βtrans ⋅  αG ⋅VGcell + αD ⋅VD + FG − VTtrans  ⋅VD  =
                                                  CTOT            
                                         Q    V trans   α       
                = αG ⋅ βtrans ⋅ VGcell + FG − T  ⋅VD + D ⋅VD2 
                                         CG    αG       αG      


                                                               Company Confidential    |   ©2009 Micron Technology, Inc.   |   24




                                                                                                                                    12
               Soglia e guadagno della cella



Soglia della cella (Q=0):                                                                                     transistore             cella (Q=0)
                                                               trans                   120
                                                             V
VTcell               = VGcell                            =    T
                                                                                       100
         (QFG =0 )                    ( I D =0,VD ≅0 )        αG                        80




                                                                             ID (µA)
                                                                                        60
                                                                                        40
                                                                                        20
Guadagno della cella:                                                                        0
                                                                                        -20
            1 ∂I              cell
βcell =      ⋅                        = αG ⋅ βtrans
                              D                                                                  -1       0     1   2     3       4     5     6      7     8

           VD ∂V              G
                               cell
                                                                                                                         VG (V)




                                                                                                  Company Confidential       |   ©2009 Micron Technology, Inc.   |   25




                         Carica nella floating gate

 Soglia della cella:                                                                                  cella (Q=0)                    cella (Q<0)
                      trans
VTcell (QFG ) =
                  V    Q                       Q                                        70
                     T
                      − FG = VTcell           − FG
                   αG  CG           (QFG =0 )  CG                                       60
                                                                                        50
                                                                            ID (µA)




                                                                                        40
                                                                                        30
                                                                                        20
                                                                                        10                                        ∆VT
                                                                                         0


     ∆VTcell (QFG ) = −
                                                 QFG                                   -10
                                                                                             -1       0        1    2    3       4     5     6      7     8
                                                 CG                                                                     VG (V)




         QFG = −CG ⋅ ∆VTcell                                       VFG (QFG ) = αG ⋅ (VGcell − ∆VTcell ) + ∑ αi ⋅Vi
                                                                                                                                       i =S ,B,D




                                                                                                  Company Confidential       |   ©2009 Micron Technology, Inc.   |   26




                                                                                                                                                                          13
                   Calcolo dei rapporti capacitivi
                                                                 VG
                   tONO                                                                                      tONO
                        tox                            C
                                                       G                                                      tox
              LS           LB   LD
                                                                 VFG
                                                                                                   A/2        W         A/2
                       L                                                                                    W+A
                                              CS       CB                CD

                                               VS                      VD
  sezione cella lungo L                                     VB
                                                                                      sezione cella lungo W

In approssimazione di condensatori a piatti piani e paralleli:                                                            αG            αD
                 L ⋅ (W + A)                   C          1                                             L           -      ≅            ¯
CG = εONO ⋅ ε0 ⋅                          αG = G =
                      tONO                    CTOT      W tONO                                                           ≅
                                                   1 +    ⋅                                        LD           -                   -
                                                     W + A tox 
                                                                                                       W            -      ¯            -
                                                                   LS ,B,D
                                                                                                        A           -         -         ¯
                       LS ,B,D ⋅W                  C
                                          αS ,B,D = S ,B,D =         L
CS ,B,D = εox ⋅ ε0 ⋅
                            tox                    CTOT  W + A tox                                   tONO         -      ¯            -
                                                             1 +        ⋅ 
                                                                  W tONO                            tox          -         -         ¯




                                                                            Company Confidential   |    ©2009 Micron Technology, Inc.       |   27




                        La cella come elettrometro

La cella di memoria a floating gate è un elettrometro ad elevatissima risoluzione:
dati i parametri costruttivi di una cella in tecnologia 0.18µm

                                                                                        L ⋅ (W + A)
  L                W                 A     tONO                  CG = εONO ⋅ ε0 ⋅                   ≅ 0.3 fF
0.3µm        0.2µm              0.25µm    15nm
                                                                                             tONO

la variazione di carica pari a 1 elettrone (!) provoca una variazione di soglia della
cella pari a:
                                                    QFG 1.6 ⋅ 10−19 C
                                ∆VTcell (1 e) = −      =              ≅ 0.5 mV
                                                    CG    0.31 fF

Variazioni di carica pari a poche decine di elettroni nella cella di
memoria sono misurabili e possono avere un impatto significativo sui
dispositivi con memorie non volatili


                                                                            Company Confidential   |    ©2009 Micron Technology, Inc.       |   28




                                                                                                                                                     14
                Meccanismi di scrittura della cella

         I meccanismi fisici utilizzati per la scrittura* di una cella di memoria a floating
         gate sono i seguenti:


                                                            Fowler-
                                                            Fowler-                                      Channel
                   UV
                                                           Nordheim                                        Hot
                Radiation
                                                           tunneling                                     Electron
                 hν                                                                                          E

         E                                             E

                                        EB                   EB                                                         EB

                                                                                               n(E)
                      x                                       x                                                                               x




             *si definisce scrittura l'operazione generica di variazione dello stato della cella di memoria



                                                                                  Company Confidential   |    ©2009 Micron Technology, Inc.       |   29




                      Cancellazione per UV radiation
•   Per effetto fotoelettrico si fornisce ai
    portatori della floating gate energia                                     F        F
    sufficiente a superare la barriera di                                hν
                                                                                               ∆E(Q)
    potenziale dell’ossido
     ▶   L’eventuale carica intrappolata nella                                                3.2 eV                                  3.2 eV
                                                                   Ec                                    Ec
         floating gate genera il campo elettrico
         interno che causa la corrente netta con                   Ef                                    Ef
         la quale il sistema si porta all’equilibrio               Ev                                    Ev
         (potenziale elettrochimico costante,
                                                                                              4.0 eV                                  4.0 eV
         quindi nessuna carica nella floating
         gate)

•   L’irraggiamento UV è una operazione
                                                                        stato iniziale                           stato finale
    di reset
     ▶   Non è detto che alla condizione di
                                                                                                              ν > 7.7e14 Hz
                                                                   hν >EB = 3.2 eV
         neutralità corrisponda uno stato logico
         della memoria, ma l’operazione è detta
                                                                                                               λ < 380 nm
         cancellazione poiché non è selettiva



                                                                                  Company Confidential   |    ©2009 Micron Technology, Inc.       |   30




                                                                                                                                                           15
                 Fowler-Nordheim Tunneling

•   Applicando una differenza di potenziale              EB=3.2eV
    ∆V sufficentemente elevata tra le                                                                 q ⋅ Vox = q ⋅ ∆V − φs ≅ q ⋅ ∆V
    armature di un condensatore MOS e'                        E
    possibile piegare le bande in modo tale                   C
    da ottenere nell’ossido una barriera di                 EFm
    potenziale triangolare attraverso la quale
    la probabilita' di tunnelling e' diversa da               EV
    zero.                                                                                        3.2 eV                           q ⋅ ∆V

                                                                                                                     φs           E
•   Si ottiene cosi' una corrente di gate con la                                                                                  C
    quale e' possibile alterare lo stato di                                                                                        EFsn
    carica di una gate flottante e quindi
    scrivere una memoria non volatile                                                                                             EV
    (il meccanismo è bidirezionale).
                                                                                                 3.8 eV
•   Per limitare la caduta di potenziale φs sul
    silicio, la giunzione n* che costituisce uno
    dei due capi del condensatore deve
    essere molto drogata.                                      n+ poly ossido                         Silicio n


                                                                              -             +
                                                                                            ∆V


                                                                    Company Confidential                 |   ©2009 Micron Technology, Inc.    |   31




            Equazione di Fowler-Nordheim

       Il tunneling attraverso una barriera di                                10
                                                                                      -6



       potenziale triangolare può essere                                      10
                                                                                      -7



       calcolato mediante il metodo WKB:                                      10
                                                                                      -8
                                                                         IG




                                                                                      -9
                                                                              10



                                B 
                                                                                      -10
                                                                              10


          J FN = AFN ⋅ F ⋅ exp − FN 
                            2
                           ox
                                                                              10
                                                                                      -11

                                                                                       6          8           10           12           14

                                Fox                                                                         VG




                                                                                       -8
                                                                                 10

                                                                                       -9

                              e3 m0 1                                            10

                       AFN =    ⋅      ⋅
                             8πh moxeff EB
                                                                         2




                                                                                       -10
                                                                                 10
                                                                          I G /E OX




                                                                                       -11
                                                                                 10
          dove                                                                         -12
                                                                                 10
                                8π
                       BFN =        ⋅ 2 ⋅ moxeff ⋅ EB3                           10
                                                                                  0.050
                                                                                       -13

                                                                                                 0.075       0.100        0.125       0.150
                                3eh                                                                          1/EOX




                                                                    Company Confidential                 |   ©2009 Micron Technology, Inc.    |   32




                                                                                                                                                       16
           Cancellazione per FN tunneling

Il meccanismo di Fowler-Nordheim tunneling viene utilizzato per cancellare
una memoria Flash NOR, cioè per togliere elettroni dalla floating gate.
                                                                                                                   VG~-8V
Analisi della cancellazione FN a tensioni esterne costanti:

Campo                        VS − VFG (1 − αS ) ⋅VS − αG ⋅VG + αG ⋅ ∆VTcell                             VS~5V                     VD float
                     Fox =           =
elettrico                       tox                    tox
                                                                                                                      VB=0V
Corrente di                                  dQFG        d∆VTcell               dF
                     I FN = SSG ⋅ J FN = −        = CG ⋅          = CTOT ⋅ tox ⋅ ox
tunneling                                     dt           dt                    dt
FN
Equazione differenziale                                    dFox SSG ⋅ J FN     S ⋅A                 B 
  della cancellazione                                          =            = − SG FN ⋅ Fox2 ⋅ exp − FN 
                                                            dt   CTOT ⋅ tox    CTOT ⋅ tox           Fox 
   per tunneling FN
                             tox ⋅ BFN        S ⋅ A ⋅B
                                                                         ∆VTcell (t ) =
                                                           1                                          V0
                                αG
                                       = V0 ; SG FN FN =
                                                CTOT ⋅ tox
                                                                                                                     −V *
Soluzione          posti
                                                           t0                                       V0       t
                             1 − αS                                                       ln exp *          + 
                                    ⋅VS − VG = V *                                             V + ∆VT (0)  t0 
                                                                                                         cell
                               αG




                                                                               Company Confidential     |   ©2009 Micron Technology, Inc.   |   33




     Cancellazione FN di una Flash NOR

    I generazione                                    II generazione                                   III generazione
           VG=0V                                           VG~-8V                                               VG=-9V


  VS~12V              VD float                   IS=cost             VD float                         VS=VB                    VD float

             VB=0V                                          VB=0V                                             VB crescente


+ tensioni positive (semplicità                + correnti BBT ridotte                          + correnti BBT nulle
circuitale)                                    (alimentazione interna)                         (alimentazione interna)
                                               + campo elettrico sull’ossido                   + tensione VBS nulla (giunzione
– tensione VBS elevata                         costante nel tempo                              source abrupt)
(giunzione source graduale)                                                                    + campo elettrico sull’ossido
– correnti BBT elevate                         – tensione VBS elevata                          costante nel tempo
(alimentazione esterna)                        (giunzione source graduale)
– campo elettrico sull’ossido                  – tensioni negative                             – tensioni negative (complessità
decrescente nel tempo                          (complessità circuitale)                        circuitale)
                                                                                               – polarizzazione substrato
                                                                                               (processo “triplo well”)




                                                                               Company Confidential     |   ©2009 Micron Technology, Inc.   |   34




                                                                                                                                                     17
                              Channel Hot Electrons

 •       Gli elettroni che viaggiano dal source al drain                                                        C.H.E.
         guadagnano energia per effetto del campo                                                                                          E
         elettrico laterale e la perdono per interazioni con il                              EB-=3.2eV
         cristallo                                                                                             E
                                                                                                                C
 •       La distribuzione di energia degli elettroni n(E)                                                     φs
         presenta una coda di elettroni con energia molto                                                           EFsp
                  Channel Hot Electrons)
         elevata (Channel     Electrons , superiore alla          EB-=3.2eV                                   EV           n(E)

         barriera di potenziale dell’ossido, nei punti del           E
         canale dove il campo elettrico laterale è molto             C
         elevato                                                   EFm
                                                                                             EB+=3.8eV
                                                  giunzione         EV
                               VG=+9V
                                                   di drain
                                                    abrupt        EB+=3.8eV
                             Fox

         VS=0V                     Flaterale    VD=+5V
                                                                      n+ poly ossido              Silicio p


         VB=0V                                                                   +    -




                                                                           Company Confidential    |   ©2009 Micron Technology, Inc.   |       35




                     La cella come amperometro

 La cella di memoria a floating gate può essere utilizzata come un amperometro
 molto sensibile: dati i parametri costruttivi di una cella in tecnologia 0.18µm

                                                                                       L ⋅ (W + A)
     L               W             A            tONO              CG = εONO ⋅ ε0 ⋅                 ≅ 0.3 fF
0.3µm            0.2µm      0.25µm             15nm
                                                                                            tONO

 le curve di programmazione effettuate con un impulsatore standard permettono
 di rilevare indirettamente correnti di gate estremamente basse:

                                                       dQFG         d∆VTcell
                                               IG =         = −CG ⋅
                                                        dt            dt
 La variazione di soglia di 1 V in 1s (programmazione a bassi campi) corrisponde
 su questa cella ad una corrente media di gate pari a 0.3fA.




                                                                           Company Confidential    |   ©2009 Micron Technology, Inc.   |       36




                                                                                                                                                    18
     Moltiplicazione di elettroni e lacune
                             VG=+9V                                                        VG=+9V
                                                                                                              Li

                                   Fox                                                            Fox         Fox
    VS=0V                           M1      VD=+5V                         VS=0V
                                                                                                                 M1
                                                                                                                           VD=+5V


    VB=0V                                                                  VB=0V

  Iniezione di Hot Electrons prodotti da                                  Iniezione di Hot Holes prodotti da
  moltiplicazione per ionizzazione da impatto al drain                    moltiplicazione per ionizzazione da impatto al
                                                                          drain

                                   VG=+9V
                                             Li

                                     Fox     Fox
                 VS=0V                                    VD=+5V         Iniezione di Hot Electrons secondari
                                                     M1                  prodotti da moltiplicazione per ionizzazione
                                            M2                           secondaria da impatto nel substrato
                 VB=0V




                                                                               Company Confidential     |    ©2009 Micron Technology, Inc.   |   37




      Iniezione di carica: moltiplicazione

                                                                                         corrente
                                                                   elettroni
                                              elettroni                                   di gate
                                                                     caldi
                                                                                        secondaria
                                                             corrente
                                                             di canale
            elettroni                                       secondaria
                           MOLTIPLICAZIONE
               caldi          PRIMARIA
            di canale                                                                                                          corrente
                                                                                                            elettroni
                                                                                      elettroni                                 di gate
elettroni                                                                                                     caldi
                                                                                                                              secondaria
di canale
                                                                                                             corrente
                        corrente
                                                                                                             di canale
                         di gate
                                                                                                            secondaria
                        primaria                                      MOLTIPLICAZIONE
                                                          lacune
                                            lacune                      SECONDARIA
                                                           calde



            corrente                                       corrente
                                                                                                                      corrente
            di canale                                     di substrato                            lacune
                                                                                                                     di substrato
             primaria




                                                                               Company Confidential     |    ©2009 Micron Technology, Inc.   |   38




                                                                                                                                                      19
C.I.S.E.I.: programmazione con body

Quando l’efficienza di programmazione diventa bassa a causa del campo elettrico
sfavorevole nella regione di drain (VFG < VD), un significativo incremento della corrente di
gate si può ottenere polarizzando il substrato (operazione che richiede un processo con
“triplo well”);
l’aumento di efficienza di programmazione permette di ridurre la corrente assorbita dalla
cella
                                                                                                                 1E-03




                                                                                          G/IcanaleEff iciency
                 VG=+9V                                                                                                                       VD




                                                   Efficienza di programmazione
                             Li                                                                                  1E-04
                                                                                                                                                               VB=-1.5V
                      Fox                                                                                        1E-05
                              Fox
                                                                                                                 1E-06




                                                                                  Pr ograImming
 VS=0V                                    VD=+4V
                                    M1                                                                           1E-07
                             M2
                                                                                                                 1E-08
VB=-1V
                                                                                                                 1E-09                                            VB=0V
        C.I.S.E.I.                                                                                               1E-10
     Channel Induced                                                                                                  1.5             2.5              3.5          4.5            5.5
Secondary Electron Injection                                                                                                       Flo ating Gate Voltage [V]



                                                                                                                            Company Confidential   |    ©2009 Micron Technology, Inc.    |   39




                      Programmazione di Flash NOR


           I generazione                                                                                                         II generazione
                    VG=+9V                                                                                                                  VG~+8V


          VS=0V               VD=+5V                                                                                          Vs=0V                          VD=+4V


           VB=0V                                                                                                               VB=-1V                          C.H.E. +
                                  C.H.E.
                                                                                                                                                               C.I.S.E.I.

   + tensioni positive                                                                                               + correnti di programmazione ridotte
   (semplicità circuitale)                                                                                           (alto parallelismo)

   – correnti di programmazione elevate                                                                              – tensioni negative (complessità circuitale)
                                                                                                                     – polarizzazione substrato (triplo well)




                                                                                                                            Company Confidential   |    ©2009 Micron Technology, Inc.    |   40




                                                                                                                                                                                                  20
        Memoria Flash NOR: organizzazione

•   La funzione di un dispositivo                                         OUTPUT                                  OUTPUT
    di memoria è quella di                                                BUFFERS                                 SIGNALS

    conservare informazioni e       Y ADDRESS    INPUT                    SENSE
    renderle disponibili in modo     SIGNALS    BUFFERS                 AMPLIFIERS
    ordinato.
                                                 COLUMN                  COLUMN
•   In una memoria Flash a                      DECODERS                SELECTORS
    singolo livello i dati sono
    immagazzinati in forma
    digitale in celle di memoria,
                                                  ROW                     MEMORY
    disposte secondo un                         DECODERS                    CELL
    arrangiamento a matrice.                                               ARRAY
•   La capacità in bit della
    memoria è pari al numero di
    celle di memoria disponibili    X ADDRESS    INPUT
                                     SIGNALS    BUFFERS




                                                          Company Confidential            |    ©2009 Micron Technology, Inc.   |   41




                  Layout di un dispositivo Flash
                                                                    I/O pads
                                                                 pompe di carica
                                                 sense amplifiers                             micro          pompe
                                                                                                            di carica
                                                                            row decoder




                                                                                                   settore


           16Mbit Flash 3.0V
           Tecnologia 0.25µm
                                                 sense amplifiers                             sense amplifiers
           chip size=28 mm2
                                                                      I/O pads



                                                          Company Confidential            |    ©2009 Micron Technology, Inc.   |   42




                                                                                                                                        21
    Matrice di memoria Flash NOR
                                                         Bitlines
                                                    (drain delle celle)




Cella Flash NOR
     singola




                                                                                                           (source delle celle)
                               (gate delle celle)




                                                                                                                                  Sourcelines
                   Wordlines




                                                    Company Confidential   |   ©2009 Micron Technology, Inc.                      |         43




    Circuito della matrice Flash NOR

                                                           Bitlines



Cella Flash NOR
     singola

        G
                  Wordlines




                                                                                                                   Sourcelines




S
            D




                                                    Company Confidential   |   ©2009 Micron Technology, Inc.                      |         44




                                                                                                                                                 22
         Wordline di una matrice Flash




              dielettrico
                                        floating gate                             wordline
              interpoly
                                          (poly-Si)                               (poly-Si)
                (ONO)




                                                                                     isolamento
        canale
                                                                                        (SiO2)
     (area attiva)



                                                 Company Confidential   |   ©2009 Micron Technology, Inc.   |   45




               Bitline di una matrice Flash




                            wordline    Contatto di drain                   Metal 1
                            (poly-Si)         (W)                           (AlCu)


dielettrico
interpoly                                                                            dielettrico
  (ONO)                                                                              premetal
                                                                                      (BPSG)

                                                                                     dielettrico
 floating gate                                                                       premetal
   (poly-Si)                                                                           (SiO2)



                                                 Company Confidential   |   ©2009 Micron Technology, Inc.   |   46




                                                                                                                     23
                          Memoria Flash: lettura

                                                                    GND         GND        GND         1V         GND          GND




                                            GND
•   L’organizzazione a matrice del




                                                                                                                                     GND
    dispositivo Flash NOR




                                            GND
    permette di selezionare e




                                                                                                                                     GND
    leggere una singola cella
                                           5V




                                                                                                                                     GND
                                            GND
•   Per leggere una cella si alza la




                                                                                                                                     GND
    sua wordline a ~5V e la sua


                                            GND
    bitline a ~1V, con source e




                                                                                                                                     GND
    body a massa                            GND




                                                                                                                                     GND
                                                                                Company Confidential   |    ©2009 Micron Technology, Inc.   |   47




                             Lettura: read verify

             In base al funzionamento
             del circuito di sensing, si
             definiscono 1 le celle che                                                     tensione              read
             portano più corrente                                                           di lettura            verify
             della cella di read verify                           100
             alla tensione di lettura                              90
                                                  Id@Vd=1V (uA)




                                                                   80
                                                                   70                      1
                                                                   60
             Si definiscono 0 le celle                             50
                                                                   40
             che portano meno                                      30
                                                                                                                  0
                                                                   20
             corrente del read verify                              10
             alla tensione di lettura                               0
                                                                        0   1    2     3     4     5   6      7       8    9    10
                                                                                              Vg (V)
             Tempi di accesso
                Random: 50÷150ns
                Burst mode: 15÷30ns



                                                                                Company Confidential   |    ©2009 Micron Technology, Inc.   |   48




                                                                                                                                                     24
      Memoria Flash: programmazione

                                                     GND           GND       GND           5V          GND        GND


   L’organizzazione a matrice




                                   GND
   del dispositivo Flash NOR




                                                                                                                         GND
   permette di selezionare e




                                   GND
   programmare una




                                                                                                                         GND
   singola cella per C.H.E.
                                  9V




                                                                                                                         GND
   Per programmare una cella




                                   GND
   si alza la sua wordline a




                                                                                                                         GND
   ~9V e la sua bitline a


                                   GND
   ~5V, con source e body a




                                                                                                                         GND
   massa
                                   GND




                                                                                                                         GND
                                                                   Company Confidential     |   ©2009 Micron Technology, Inc.   |   49




     Programmazione: program verify
Ogni impulso di
programmazione (pochi µs)
è seguito da una verifica
della cella rispetto alla cella
                                                                                                            read program
di program verify
                                                                                                            verify verify
                                                         100
Tempi di program: ~10µs                                   90
                                         Id@Vd=1V (uA)




                                                          80
                                                          70
                                                          60
Una cella è programmata                                   50                                    ∆P
                                                          40
quando meno corrente del                                  30
program verify alla                                       20
                                                          10
                                                                                                             0
tensione di lettura                                        0
                                                               0   1     2     3     4      5      6    7     8    9    10
                                                                                          Vg (V)
Il margine di
programmazione ∆P serve
per l’affidabilità della cella
(ritenzione e disturbi)



                                                                   Company Confidential     |   ©2009 Micron Technology, Inc.   |   50




                                                                                                                                         25
      Memoria Flash: cancellazione

 L’organizzazione a                          FLOAT FLOAT FLOAT FLOAT FLOAT FLOAT
 matrice del dispositivo
 Flash NOR non                    -9V
 permette di cancellare
                                                                                                                           5V
 una singola cella
                                  -9V
                                                                                                                           5V
 La cancellazione viene           -9V
 esguita per Fowler
                                                                                                                           5V
 Nordheim tunneling su
 un intero blocco di celle        -9V
 (settore) portando tutte                                                                                                  5V
 le wordlines a ~-9V e            -9V
 tutte le sourcelines a                                                                                                    5V
 ~5V, con body a massa            -9V
 e drain floating                                                                                                          5V



                                                                  Company Confidential      |   ©2009 Micron Technology, Inc.   |   51




         Cancellazione: erase verify

Ogni impulso di
cancellazione (decine di ms)
è seguito da una verifica                                                                       erase read program
della cella rispetto alla cella                                                                 verify verify verify
di erase verify                                         100
                                                         90
                                        Id@Vd=1V (uA)




                                                         80
Una cella è cancellata                                   70                       1
                                                         60
quando più corrente dell’                                50                           ∆E
                                                         40
erase verify alla tensione di                            30
lettura                                                  20
                                                         10
                                                          0
                                                              0    1    2     3       4     5      6   7     8     9    10
Il margine di cancellazione
                                                                                          Vg (V)
∆E serve per l’affidabilità
della cella nel tempo
(ritenzione e disturbi)




                                                                  Company Confidential      |   ©2009 Micron Technology, Inc.   |   52




                                                                                                                                         26
                                                                                                    Celle deplete

La cancellazione per FN è funzione esponenziale                                                                                                               Read error: corrente
del campo elettrico sull’ossido di tunnel: piccole                                                                                                              letta sulla bitline erase read                                    program
differenze di campo (indotte da cariche nell’ossido                                                                                                           indirizzando la cella
                                                                                                                                                                  programmata       verify verify                                  verify
o dispersione di processo) causano sensibili
differenze nella velocità di cancellazione.                                                                                                                 100
Cancellando un settore Flash è normale ottenere                                                                                                              90




                                                                                                                                            Id@Vd=1V (uA)
una certa percentuale di celle deplete.                                                                                                                      80               cella
                                                                                                                                                             70
                                                                                                                                                             60              depleta
                                                                                                                                                             50
                                                                                                                                                             40                                            ∆I
            1,E+07
                                                                                                                                                             30                 ∆I                                   cella
            1,E+06                celle                                                                                                                      20
                                                                                                                                                             10                                                  programmata
            1,E+05 cancellate                                               celle                                                                             0
  cells #




            1,E+04                                                           UV                                                                                   0      1     2     3       4       5       6     7    8     9    10
            1,E+03                                                                                                                        leakage sulla bitline causato dalla Vg (V)
                                                                                                                                           cella depleta (corrente a Vg=0)
            1,E+02                                                                              celle
            1,E+01                                                                          programmate
            1,E+00                                                                                                                        La presenza di celle deplete su una bitline può
                           -2         -1        0       1       2       3       4       5       6       7       8       9       10        causare errori nella lettura delle altre celle della
   coda di                                      cell threshold voltage (V)                                                                bitline, poichè la cella depleta aggiunge un offset
                                                                                                                                          di corrente ∆I sulla bitline
celle deplete




                                                                                                                                                                      Company Confidential       |       ©2009 Micron Technology, Inc.     |   53




                             Soft-program delle celle deplete

  Per recuperare le celle deplete si ricorre alla
  soft-programmazione: le celle a bassa soglia                                                                                                                    GND          GND GND                    5V        GND GND
  vengono programmate selettivamente per
  C.H.E. con tensione di gate molto bassa, in
                                                                                                                                                GND




  modo da evitare che la loro soglia finale
                                                                                                                                                                                                                                         GND




  superi il valore di erase verify
                                                                                                                                                GND




                                                                                                                                                                                                                                         GND




                        1,E+07
                                          celle
                                   soft-programmate                                                                                        3V
                                                                                                                                                                                                                                         GND




                        1,E+06
                               celle            celle
                                                                                                                                                GND




                        1,E+05
                          cancellate             UV
            c e lls #




                                                                                                                                                                                                                                         GND




                        1,E+04

                        1,E+03
                                                                                                                                                GND




                        1,E+02
                                                                                                                                                                                                                                         GND




                                                                                                    celle
                        1,E+01
                                                                                                programmate
                                                                                                                                                GND




                        1,E+00
                                                                                                                                                                                                                                         GND




                                 -2        -1       0       1       2       3       4       5       6       7       8       9        10

     coda di                                                cell threshold voltage (V)
  celle deplete




                                                                                                                                                                      Company Confidential       |       ©2009 Micron Technology, Inc.     |   54




                                                                                                                                                                                                                                                    27
          Cancellazione: depletion verify


    Ogni impulso di                                                                             depletion erase read program
                                                                                                 verify verify verify verify
    softprogrammazione (pochi µs) è
    seguito da una verifica della cella                               100
                                                                       90                cella
    rispetto alla cella di depletion




                                                      Id@Vd=1V (uA)
                                                                       80               depleta
    verify                                                             70
                                                                       60
                                                                       50
                                                                                                1
                                                                       40
    Una cella è softprogrammata                                        30
                                                                       20
    quando più corrente del                                            10
                                                                        0
    depletion verify alla tensione di
                                                                            0      1      2    3       4       5    6     7   8     9    10
    lettura, ma porta comunque meno
                                                                                                           Vg (V)
    corrente dell’ erase verify




                                                                                Company Confidential       |   ©2009 Micron Technology, Inc.   |   55




Flash NOR: sequenza di cancellazione

           Erase Start
                                                                                       Depletion Verify

         Protected Sector       Y   Soft Program Pulse
                                                                                        Depleted bits               N
                N
                                                                                               Y
          Program All0
                                                 N                              Last Soft Program Pulse
                                                                                               Y
           Erase Pulse
                                                                                   Set Erase Fail Flag
           Erase Verify


          Erased Sector     Y
                N                                                           N            Last Sector
                                                                                               Y
                                                                                                                        Tempi di erase:
N        Last Erase Pulse       Y                                                                                         0.5÷1.5s
                                                                                         Erase End
                                                                                                                          per settore
                                        Next Sector




                                                                                Company Confidential       |   ©2009 Micron Technology, Inc.   |   56




                                                                                                                                                        28
       Affidabilità di una memoria Flash

• Disturbi
   ▶ disturbi in programmazione, disturbi in lettura


• Fast erasing bits

• Endurance
   ▶ Degrado in ciclatura, bit erratici


• Ritenzione
   ▶ leakage negli ossidi, contaminazione ionica, SILC




                                                      Company Confidential   |   ©2009 Micron Technology, Inc.   |     57




             Disturbi di programmazione

 Durante la programmazione della cella
                                                    GND    GND        GND        5V        GND        GND
 A, la cella B che condivide la stessa
 bitline e la cella C che sta sulla stessa
 wordline subiscono degli stress
                                              GND




                                                                                                                 GND




  B programmata:
                                              GND




   FN drain stress su ossido di tunnel               C                                 A
                                                                                                                 GND




   Hot Holes Injection
   T= Σ program celle della bitline
                                             9V
                                                                                                                 GND
                                              GND




  C programmata:
                                                                                                                 GND




   FN gate stress su ossido interpoly
                                              GND




   T= Σ program celle della wordline
                                                                                        B
                                                                                                                 GND
                                              GND




  C cancellata:
                                                                                                                 GND




   FN gate stress su ossido di tunnel
   T= Σ program celle della wordline



                                                      Company Confidential   |   ©2009 Micron Technology, Inc.   |     58




                                                                                                                            29
                                      Disturbi: campi elettrici
I campi elettrici sugli                                                    VG − VFG (1 − αG ) ⋅ VG + αG ⋅ ∆VT − α D ⋅ VD
ossidi attivi di una
                                                               FONO =              =
                                                                             tONO                    tONO
cella dipendono dalle
tensioni applicate e                                                       VFG − VD α G ⋅ (VG − ∆VT ) − (1 − α D ) ⋅ VD
                                                                   Fox =           =
dalla soglia della cella.                                                     tox                 tox

                    Disturbo di gate in programmazione                                            Disturbo di drain in programmazione
                               VG=9V, VD=0V                                                                 VG=0V, VD=5V

                   10                                                                             4
                             C
                                                                                                  2
                   8                                                                                            ONO
                                                                                                  0
                                                               C
      F (MV/cm )




                                                                                     F (MV/cm)
                   6                                                                              -2

                                                                                                  -4
                   4                                                                                        tunnel
                                                                                                  -6
                                                                                                                                                    B
                   2         ONO                                                                  -8
                                                                                                 -10
                                                        tunnel
                   0                                                                             -12
                        -4       -2   0      2      4      6       8                                   -4      -2     0        2        4       6       8
                                          DVt (V)                                                                         DVt (V)




                                                                                                  Company Confidential     |       ©2009 Micron Technology, Inc.   |     59




                                             Disturbi di lettura

Durante la lettura della cella D essa                                                GND                    GND      GND           1V        GND        GND
tende a programmarsi, mentre la
cella E che condivide la stessa
                                                                              GND




wordline subisce uno stress di gate
                                                                                                                                                                   GND
                                                                              GND




                                                                                                                                            D
                                                                                                                                                                   GND




 D cancellata:
  Channel Hot Electrons Injection                                           5V
                                                                                                                                                                   GND




  T= lifetime del dispositivo
                                                                              GND




                                                                                                 E
                                                                                                                                                                   GND
                                                                              GND




 E cancellata:
                                                                                                                                                                   GND




  FN gate stress su ossido di tunnel
                                                                              GND




  T= lifetime del dispositivo
                                                                                                                                                                   GND




                                                                                                  Company Confidential     |       ©2009 Micron Technology, Inc.   |     60




                                                                                                                                                                              30
                            Fast erasing bits

                                                                                      Durante le operazioni di scrittura per
                                                                                      Fowler-Nordheim tunneling si osservano
                                                                                      normalmente code nella distribuzione
                                                                                      delle celle (celle che si cancellano più
                                                                                      velocemente della media)


                                                                                                                                                   Poly-Si
                                                                                                                                                   floating gate


          Modelli fisici che spiegano
          l’aumento locale di campo elettrico:                                                                                         Source n+
             struttura a grani del poly
             cariche positive nell’ossido di
          tunnel

I bit più veloci vengono normalmente scartati poichè sono potenziali difetti in
ciclatura


                                                                                                           Company Confidential                     |    ©2009 Micron Technology, Inc.         |   61




                  Endurance di celle Flash

 Le Memorie Non Volatili hanno una specifica di endurance variabile tra 100 cicli
 (EPROM) e 106 cicli (EEPROM).
 Per una Flash la specifica tipica è di 105 cicli di scrittura e
 cancellazione.

    Durante la ciclatura di                                                Single cell                                                             Flash device
    una cella Flash si osserva                                                                                                        1,4                                        1,4

    tipicamente la chiusura                               8                                            8                                           program erase
                                  Threshold Voltage (V)




                                                                                                                                      1,2                                        1,2

    della finestra di
                                                                                                                   Writing time (s)




                                                                                                                                      1,0                                        1
                                                          6
                                                                  program                              6
    funzionamento, cioè il                                                                                                            0,8                                        0,8
                                                                                                           pippo




                                                                                                                                                                                       Pippo




    contemporaneo degrado                                 4
                                                                   erase
                                                                                                       4
                                                                                                                                      0,6                                        0,6


    delle prestazioni (salto di                                                                                                       0,4                                        0,4


    soglia della cella) in                                2                                            2                              0,2                                        0,2

                                                                                                                                      0,0                                        0
    programmazione C.H.E.                                     1      10       100   1,000   10,000 100,000                                  1      100          10.000      1.000.000
                                                                                                                                                   Number of Cycles
                                                                           Number of Cycles
    e in cancellazione FN




                                                                                                           Company Confidential                     |    ©2009 Micron Technology, Inc.         |   62




                                                                                                                                                                                                        31
                      Degrado in ciclatura

                                                                                                Poly-Si                      Poly-Si
     Il degrado delle prestazioni
                                                                                                floating gate                floating gate
     della cella Flash che si osserva
     in ciclatura è dovuto al
     progressivo aumento di
     cariche negative nell’ossido di                          Source n+                                                                    drain n+
     tunnel e all’interfaccia ossidi-
     silicio, sia al source che al
     drain.




                                                                                 Si osserva infatti che con il continuo
                                                                                 passaggio di cariche negative
                                                                                 nell’ossido la tensione necessaria a
                                                                                 sostenere un certo flusso di
                                                                                 corrente aumenta (FN Voltage
                                                                                 Shift)




                                                                                                      Company Confidential   |      ©2009 Micron Technology, Inc.   |   63




                                   Bit erratici
•   La fluttuazione delle cariche
    positive nell’ossido può
                                                                Cell threshold (V)




                                                                                     5
    causare il fenomeno dei bit                                                      4
                                                                                                 cycle 3
    erratici                                                                         3
                                                                                                 cycle 4
                                                                                     2           cycle 5
                                                                                     1
•   Un bit erratico si comporta                                                      0
                                                                                         1           10           100            1000         10000
    in maniera imprevedibile
    durante la ciclatura                                                                                    Erase time (ms)
                                                        3

                                                        2.5
                                        Erased Vt (V)




•   Il controllo della qualità                          2

                                                        1.5
    dell’ossido di tunnel e la                          1

    riduzione dell’iniezione di                         0.5

                                                        0
    cariche positive permette di                            0                            1000        2000       3000         4000          5000        6000

                                                                                                      Number of Cycles
    limitare il fenomeno



                                                                                                      Company Confidential   |      ©2009 Micron Technology, Inc.   |   64




                                                                                                                                                                             32
                             Ritenzione di carica

  Una cella Flash deve garantire il suo stato di carica per 10 anni.
  Data una cella con i seguenti parametri tecnologici:

                                                                                                            L ⋅ (W + A)
      L             W          A         tONO                CG = εONO ⋅ ε0 ⋅                                           ≅ 0.3 fF
   0.3µm       0.2µm         0.25µ      15nm
                                                                                                                 tONO
  Ipotizzando una cella con margini di programmazione e cancellazione pari a 1 V, la
                         m
  carica massima che può essere persa dalla floating gate in 10 anni è:

    QFG = −CG ⋅ ∆VTcell = −0.3fF ⋅1V = -0.3fC ≅ 2000 elettroni
  Questa perdita di carica equivale ad un leakage medio di
                   2000 elettroni                                                                         10−24 A
      Ileakage =                  ≅ 10−24 A                                        J leakage =                        ≅ 10−15 A 2
                     10 anni                                                                          0.3 µm ⋅ 0.2 µm          cm

Ci sono due meccanismi di perdita di carica:

leakage attraverso gli ossidi e contaminazione ionica

                                                                                           Company Confidential     |   ©2009 Micron Technology, Inc.   |   65




          Ritenzione: leakage sugli ossidi

                                                                                                Charge loss vs. time
    Perdita di carica intrinseca                                                           4
                                                                                                      temperature
    tutte le celle sono soggette a perdita di carica
                                                                   Threshold shift [ V ]




                                                                                           3
    attraverso gli ossidi attivi, per FN tunneling o
    conduzione attraverso trappole nell’ossido
                                                                                           2

                                                                                                                                      Ea~1.2 eV
                          E 
                                                                                           1


          I leakage ∝ exp − a                                                            0

                          kT                                                                 0.01   0.1    1        10       100      3 110
                                                                                                                                      110   4
                                                                                                                  Bake time [ hours ]




                                                                                                                    dipendenza dal         energia di
                                                ossido     meccanismo di leakage
    Perdita di carica                                                                                               campo elettrico        attivazione

    su single bit                                          FN tunneling attraverso
                                                                                                                     esponenziale          Ea~0.3 eV
                                                         barriera di potenziale ridotta
    difetti negli ossidi possono
                                                tunnel
    variare la ritenzione delle                          conduzione per impurezze o
    celle                                                                                                               lineare            Ea ~0.6 eV
                                                                                  difetti

                                                         conduzione per emissione da
                                                ONO                                                                  esponenziale          Ea >0.8eV
                                                            trappole nel dielettrico

                                                                                           Company Confidential     |   ©2009 Micron Technology, Inc.   |   66




                                                                                                                                                                 33
        Ritenzione: contaminazione ionica

• La contaminazione ionica è causata dalla presenza di
     cariche mobili nei dielettrici del dispositivo
     ▶ Sostanze introdotte durante la fabbricazione e non rimosse

     ▶ Sostanze che entrano nel circuito durante la vita del
         dispositivo per la scarsa efficacia della passivazione


• La contaminazione ionica provoca problemi di ritenzione
     poichè le cariche mobili influenzano elettrostaticamente il
     potenziale della floating gate


                                                      Company Confidential   |   ©2009 Micron Technology, Inc.   |   67




                             Ritenzione: SILC

 •    per cancellare una Flash con un tunnel
      oxide da 10 nm in 100 ms bisogna
      applicare uno stress di 1e-4 A/cm2 a una
      tensione di 10 V

 •    dopo l'applicazione dello stress, la corrente
      di leakage aumenta
      (Stress Induced Leakage Current)

 •    ll leakage anomalo nell’ossido di tunnel
      avviene attraverso le trappole create dal
      passaggio di carica, quindi dopo ciclatura

 •    con la tecnologia attuale, per garantire la
      ritenzione dopo ciclatura il minimo
      spessore dell’ossido di tunnel è 8 nm




                                                      Company Confidential   |   ©2009 Micron Technology, Inc.   |   68




                                                                                                                          34
                Testing memoria FLASH

    • Processo di costruzione del circuito
       ▶ Testing Parametrico di processo


       ▶ I EWS (Electric Wafer Sorting)
       ▶ II EWS


    • Assemblaggio
       ▶ Final Test
       ▶ Campionamento per valutazione affidabilistica




                                                Company Confidential   |   ©2009 Micron Technology, Inc.   |   69




                  Resa di un dispositivo

•   La RESA di un dispositivo su lotto è il rapporto tra i pezzi funzionanti e
    i pezzi disponibili

•   La resa dipende dalla difettosità del processo

•   Per migliorare la resa di un dispositivo ci sono 2 vie:
     ▶ Riduzione della difettosità del processo
     ▶ Introduzione di accorgimenti di design che permettono di
       aumentare la resa:
         • Ridondanza: celle aggiuntive utilizzabili come “scorta”, fissate a
           livello di EWS
         • Error Correction Codes: algoritmi in grado di riconoscere e
           riparare celle di memoria difettose durante la vita del
           dispositivo



                                                Company Confidential   |   ©2009 Micron Technology, Inc.   |   70




                                                                                                                    35
    Resa e ridondanza: analisi statistica

    •   Resa di un dispositivo in assenza di ridondanza:
          ▶   p: probabilità che una cella sia difettosa
                                                           Y0 = (1 − p)
                                                                                                                 1
                                                                                Nr⋅ Nc
          ▶   Nr: numero di righe della matrice                                          ⇒ p = 1 − Y0 Nr⋅Nc
          ▶   Nc: numero di colonne della matrice


    •   Resa di un dispositivo con Nrid colonne di ridondanza:
          ▶   p: probabilità che una cella sia difettosa
          ▶   qc: probabilità che una colonna non contenga bit difettosi
          ▶   pc: probabilità che una colonna contenga almeno un bit difettoso
          ▶   Nr: numero di righe della matrice
          ▶   Nc: numero di colonne della matrice
                                 Nrid  Nc                                                    
     qc = (1 − p )
                                                           Nrid  Nrid
                   Nr
                                                                   
                         YNrid = ∑   ⋅ pcm ⋅ qcNc−m ⋅ ∑         ⋅ qc j ⋅ pcNrid− j  
     pc = 1 − qc                 m=0  m                j =m  j                         

                                                             Company Confidential   |    ©2009 Micron Technology, Inc.   |   71




                        Error Correction Code
•   Gli Error Correction Codes sono sistemi basati sulla codificazione dei dati e su
    algoritmi in grado di riconoscere ed riparare automaticamente celle che cambiano
    stato logico (es. per problemi di ritenzione)
•   Codifica ECC
           • Quando vengono scritte in matrice le informazioni del cliente, l’algoritmo
              ECC provvede a scrivere altri bit aggiuntivi (bit di parità) accessibili solo
              al sistema
•   Decodifica ECC
           • Quando il cliente legge i dati della memoria, l’algoritmo ECC confronta i
              dati con le informazioni dei bit i parità e nel caso trovi differenze è in
              grado di fornire una risposta corretta riconoscendo i bit che hanno
              cambiato stato logico
           • Eventualmente la memoria può anche autocorreggersi, riprogrammando
              il dato inizialmente memorizzato sui bit difettosi



                                                             Company Confidential   |    ©2009 Micron Technology, Inc.   |   72




                                                                                                                                  36
                        ECC vs. Ridondanza

                     ECC                                   Ridondanza
•     correggono problemi di affidabilità            •   occupa poca area in matrice
      durante la vita del dispositivo                •   risolve alcuni tipi di difettosità delle
•     occupano area elevata in matrice                   celle di memoria

•     necessitano di circuiteria aggiuntiva          •   può essere utilizzata a livello di
      per la gestione degli algoritmi                    colonna, riga, settore

•     rallentano il tempo di accesso ai dati         •   viene fissata a livello di EWS, non può
                                                         essere modificata durante la vita del
                                    dispositivo
    ECC e Ridondanza vengono utilizzati insieme per aumentare
    sia la resa che l’affidabilità

                                                             Company Confidential   |   ©2009 Micron Technology, Inc.   |   73




                 Memorie Flash multilivello

                                                                  ∆VTcell (QFG ) = −
                                                                                                 QFG
    Partendo dalla relazione che lega la soglia di
    una cella alla carica nella floating gate                                                    CG
    si osserva come il transistore a floating gate non sia intrisecamente un oggetto digitale,
    ma sia piuttosto un elettrometro analogico.
    Perchè non sfruttare quindi queste caratteristiche per memorizzare all’interno di una
    sola cella di memoria floating gate un maggior numero di informazioni?


                                                              MULTI BIT CELL:
        SINGLE BIT CELL:
                                                                    1 cella
             1 cella
                                                                2n stati logici
          2 stati logici
                                                            (000 - 001 - 010 - 011
             (0 - 1)
                                                            100 - 101 - 110 - 111)

Con una memoria multilivello la densità della memoria aumenta e il
costo per bit si riduce (a pari complessità tecnologica!)


                                                             Company Confidential   |   ©2009 Micron Technology, Inc.   |   74




                                                                                                                                 37
        Memoria NOR multilivello (2bit/cell)

    Una memoria Flash NOR si presta naturalmente all’introduzione
    del concetto di multilivello:


                                1 bit/cell                                                                              2 bit/cell
                   1,E+07                                                                                  1,E+07
                   1,E+06
                                        1                    0                                             1,E+06
                                                                                                                             11          10 01                   00
                   1,E+05                                                                                  1,E+05
         cells #




                                                                                                 cells #
                   1,E+04                                                                                  1,E+04
                   1,E+03                                                                                  1,E+03
                   1,E+02                                                                                  1,E+02
                   1,E+01                                                                                  1,E+01
                   1,E+00                                                                                  1,E+00
                            0   1   2    3   4   5   6   7       8   9 10                                           0    1       2   3   4   5       6   7   8   9 10
                                 cell threshold voltage (V)                                                              cell threshold voltage (V)




                                                                                                                  Company Confidential       |       ©2009 Micron Technology, Inc.   |   75




         Lettura Flash multilivello (2bit/cell)
•   In analogia alla cella single bit, la
    lettura avviene confrontando la                                                                                          RV2 RV1 RV3
                                                                                             1,E+07
    corrente della cella con la corrente                                                                            11          10  01   00
                                                                                             1,E+06
    delle 3 celle di riferimento                                                             1,E+05
                                                                                   cells #




                              CORRENTE IREAD                                                 1,E+04

                            CELLA SELEZIONATA                                                1,E+03
                                                                                             1,E+02
                                                                                             1,E+01
                            N           IREAD>IRV1                   Y                       1,E+00
                                                                                                              0      1       2       3   4       5       6   7     8    9 10
                                                                                                                        cell threshold voltage (V)
    N       IREAD>IRV2                  Y            N           IREAD>IRV3    Y

                                                                                             •             Dovendo inserire più livelli di sensing,

    11                           10                  01                       00                           il tempo di accesso risulta in generale
                                                                                                           aumentato


                                                                                                                  Company Confidential       |       ©2009 Micron Technology, Inc.   |   76




                                                                                                                                                                                              38
       Programmazione Flash Multilivello

 •   La programazione per C.H.E di
     una Flash NOR Multilivello è
     particolarmente delicata poichè
     bisogna ottenere distribuzioni
     molto strette e valori di soglia
     molto controllati per gli stati 10
     e 01

 •   Programmando la cella con una
     successione di brevi impulsi con
     tensione di drain costante e
     tensione di gate crescente, la
     soglia della cella segue la
     tensione di gate

 •   Tra un impulso e il successivo
     una fase di verifica permette di
     fermare la programmazione al
     livello desiderato



                                          Company Confidential   |   ©2009 Micron Technology, Inc.   |   77




          Problemi delle Flash multilivello

• Complessità aggiuntiva nei circuiti di sensing

• Minor velocità di lettura e programmazione


• Minori margini sulle distribuzioni
     ▶ Maggior criticità delle dispersioni di processo

     ▶ Maggior sensibilità ai disturbi

     ▶ Minori margini sulla ritenzione

         • Necessità di algoritmi ECC



                                          Company Confidential   |   ©2009 Micron Technology, Inc.   |   78




                                                                                                              39
           NOR Flash: 180nm                              65nm

       λ: technology generation minimum size (i.e.: 180nm)
       Scaling rules for NOR Flash cells: area = ~ 10⋅λ2

      180nm NOR: 0.326um2                   65nm NOR: 0.042um2




                                           Company Confidential   |   ©2009 Micron Technology, Inc.   |   79




          X-direction: 180nm                             65nm

• Cell scaling along X direction: Shallow Trench Isolation (STI) and
  width must be reduced

      180nm NOR: 0.326um2                   65nm NOR: 0.042um2




                W=0.16µm                               W=0.05µm
                                                       X=0.146µm


            X=0.50µm




                                           Company Confidential   |   ©2009 Micron Technology, Inc.   |   80




                                                                                                               40
          Y-direction: 180nm                               65nm

•   Scaling along Y direction: cell length (L) must be reduced as well as
    contact sizes, distances between contacts and WL, and between
    sources
          180nm NOR: 0.326um2
                                                          65nm NOR: 0.042um2




                                                                    L=0.12µm
      L=0.28µm
                                                                    Y=0.29µm
        Y=0.65µm




                                             Company Confidential    |   ©2009 Micron Technology, Inc.   |   81




       NOR Flash scaling: an example




    16Mbit Flash 3.0V                    512Mbit Flash 1.8V
    Technology 250nm                  Technology 65nm 2bit/cell
    chip size=28 mm2                      chip size=29 mm2


                                             Company Confidential    |   ©2009 Micron Technology, Inc.   |   82




                                                                                                                  41
        La famiglia delle memorie FLASH


                             FLASH

                    NOR                            NAND                        AND

     Virtual                      Common       Standard                           ACEE
     Ground                        Ground       NAND

  AMG       Split      Standard    Source        DINOR                              AND
            Gate         NOR      Injection

                                                                                     HiC
     Poly-Poly   Merged
      Erase




                                              Company Confidential   |   ©2009 Micron Technology, Inc.   |   83




        Ideal Mass Storage Technology

• The larger capacity at the lower cost (per
  megabyte) with
  ▶ Strong Ruggedness

  ▶ Low Power Consumption

  ▶ Small Size

  ▶ Light Weight

  ▶ High Reliability

  ▶ Noise immunity

  ▶ Good Performances (High Program and Read Throughput)


                                              Company Confidential   |   ©2009 Micron Technology, Inc.   |   84




                                                                                                                  42
                                    NAND Flash



     y

         x
                              basic layout    y-pitch cross-section
                         Bit line

         Bit line sel.
                                     W .L.




         Bit line sel.
             Source

             array equivalent circuit         x-pitch cross-section


                                             Company Confidential   |   ©2009 Micron Technology, Inc.   |   85




             NAND Cell Cross-section




  y-pitch cross-section                       x-pitch cross-section

• Cell distance is 2F in both directions     4F2 cell size!
• Very simple cell structure     easier scaling

                                             Company Confidential   |   ©2009 Micron Technology, Inc.   |   86




                                                                                                                 43
   Matrice di memoria Flash NAND
                                                                  Bitlines




                                                                                                                    Bitline Select Transistor e Ground Select Transistor
Cella Flash NAND
      singola




                                                                                                                                                                           Select transistors
                   16 Wordlines
                                  (gate delle celle)




                                                             Company Confidential   |   ©2009 Micron Technology, Inc.                                                      |                87




 Organizzazione di una Flash NAND
                                                                    Bitlines



                                                       BSL


Cella Flash NAND
      singola

        G
                     16 Wordlines




                                                                                                                                          Select Transistors




   n+       n+


                                                       GSL




                                                             Company Confidential   |   ©2009 Micron Technology, Inc.                                                      |                88




                                                                                                                                                                                                 44
                                NAND Stacked Gate Flash

                                                                                            NAND cell
                                                                                               Tunnel oxide th.: 7-8nm
                                                                                               ONO EOT: 15nm
                                                                                               Cell gate length: 130nm
                                                                                               Cell size: 0.09um2




                                    CHARGE
                                    STORAGE
                                                                                            130nm Technology Node
Interpoly                           ELEMENT
                                                                Control Gate
dielectric      Control Gate
              Control Gate
                                    Tunnel                      Floating Gate
                Floating Gate
                                     oxide
     Source                       Drain
  Source                        Drain
              y-pitch                                          x-pitch



                                                                                 Company Confidential   |   ©2009 Micron Technology, Inc.   |   89




                                             Reading Operation



                                                                                NAND Flash
                  "1"                                    "0"
     Id
                                                                                  Read current: I=300-500nA
                                                                                  Random access: t=10-30us
                     ∆Vt = - Q / Cpp                                              Serial throughput: 10-30MB/s

                          Vread                    Vcg

"1"                      =>            Iread > 0
"0"                      =>           Iread = 0




                                                                                 Company Confidential   |   ©2009 Micron Technology, Inc.   |   90




                                                                                                                                                     45
                                                                   NAND: lettura
                                                                                                         GND       GND           GND       3V        GND        GND
                                 Celle                            Celle
               1,E+07
                               cancellate                     programmate                   4.5V
               1,E+06




                                                                                             4.5V
               1,E+05
    cells #




               1,E+04

               1,E+03




                                                                                             4.5V
               1,E+02

               1,E+01

               1,E+00
                        -5      -4    -3     -2     -1    0    1   2    3     4   5      GND
                                     cell threshold voltage (V)




                                                                                             4.5V
   Lettura cella NAND



                                                                                             4.5V
   Dato che tutte le celle non selezionate
   sono accese, indipendentemente dal
                                                                                             4.5V
   loro stato, sulla bitline selezionata
   passa corrente solo se la cella
   selezionata è cancellata.                                                                4.5V



                                                                                                          Company Confidential    |    ©2009 Micron Technology, Inc.   |   91




                   NAND Flash Writing Mechanism
                                Vwl>0                                                                                 Vwl                           18-20V
                                                                       • Programming:
                                                                            Fowler-Nordheim (FN)                      Vbody                              0V
                         Control Gate                                       electron tunneling current
                                                                            through the tunnel oxide to               tpulse                          300us
                         Floating Gate                                      the floating gate
              Source                              Drain                                                               Icurrent                           ~0
                              Vbody=0
                                                                                                                      Throughput                 7-10MB/s

Threshold voltage range (V): -5<Vt<3;                                                               Threshold voltage shift (V): ∆Vt>3

                                Vwl=0                              • Erasing:
                                                                            Fowler-Nordheim (FN)                       Vwl                                  0V
                                                                            electron tunneling current
                             Control Gate                                   through the tunnel oxide from              Vbody                           18-20V
                                                                            the floating gate to the silicon
                             Floating Gate                                  surface
                                                                                                                       tpulse                             2ms
               Source                             Drain

                               Vbody>0                                                                                 Icurrent                             ~0




                                                                                                          Company Confidential    |    ©2009 Micron Technology, Inc.   |   92




                                                                                                                                                                                46
                                      NAND: Program e Erase
               La programmazione di una Flash                                     La cancellazione di una Flash NAND
              NAND avviene per FN, polarizzando la                                    avviene per FN, polarizzando il
                 wordline a tensioni elevate con                                  substrato a tensioni elevate e tenendo
                       substrato a massa                                                tutte le wordlines a massa

                                 3V   3V   3V   0V 3V       3V                                   FLOAT FLOAT FLOAT FLOAT FLOAT FLOAT

                   3V                                                                FLOAT
                   10V 10V




                                                                                 GND
                                                                                 GND




                                                                                                                                               Body = 21V
               18V                                                               GND
                   10V 10V 10V




                                                                                 GND
                                                                                 GND
                                                                                 GND
                 GND                                                                 FLOAT




                                                                                          Company Confidential   |   ©2009 Micron Technology, Inc.          |   93




                  Performances: Data Throughput



                                                             NAND
               SEQUENTIAL                                    FLASH                             SEQUENTIAL
               PROGRAM                                                                         READ
               7MB/s Max                                                                       27MB/s Max

                    Direct Video
                     Recording
                                                             ERASE
                                                           64MB/s Max

                                                          1Gbit Chip Erase
                                                            in 2 seconds

Maximum throughput referred to NAND Family X16 with 2Kbytes Page Size w/o Host Overhead




                                                                                          Company Confidential   |   ©2009 Micron Technology, Inc.          |   94




                                                                                                                                                                     47
               NAND Multi-Level Concept

                                      Bit
                                 Distribution


            1bit/cell
                           “1”                                “0”


                                                                                      Voltage




                                      Bit
                                 Distribution



            2bit/cell
                           “11”                 “10”        “01”          “00”

                                                                                      Voltage




                                                   Company Confidential   |   ©2009 Micron Technology, Inc.   |   95




                NAND Flash Memory Product

120nm NAND Technology     90nm NAND Technology                      25nm NAND Technology
   0.062um2 Cell Size       0.038um2 Cell Size                        0.0034um2 Cell Size




512Mb NAND Flash Memory   1Gb NAND Flash Memory                    64Gb 3b/c NAND Flash Memory




                                                   Company Confidential   |   ©2009 Micron Technology, Inc.   |   96




                                                                                                                       48
 Confronto Flash NAND e Flash NOR

La cella NAND è più piccola
 ▶   Non è necessario il contatto tra i drain delle celle
 ▶   La lunghezza di canale è minore poichè non serve tensione elevata al drain
 ▶   Non c’è necessità di realizzare una giunzione graduale al source
La memoria NAND consuma meno corrente
 ▶   I meccanismi di scrittura per FN sono più efficienti del C.H.E.


Il tempo di accesso random di una NAND è molto più lento
 ▶   La lettura “in serie” riduce molto la corrente disponibile
La memoria NAND necessità di tensioni più elevate
 ▶   I meccanismi di scrittura FN richiedono forti campi elettrici
La memoria NAND è più sensibile ai disturbi di programmazione




                                                                  Company Confidential       |   ©2009 Micron Technology, Inc.   |   97




 NOR and NAND Stacked Gate Flash
                                                NOR                              NAND



              Cell size (F2)                      10                                     5
              Read access                     Random                              Serial
                                           (fast ~50ns)

              Progr. mech./                     CHE /                              FN /

              troughput                      0.5 MB/s                        8-10MB/s

              SEM
              Cross-section
              (BL direction)




                                                                  Company Confidential       |   ©2009 Micron Technology, Inc.   |   98




                                                                                                                                          49
        NOR-NAND Architecture Comparison

   •      Common Cell Architecture:
           ▶ Floating Gate Concept
           ▶ One-Transistor Stacked-Gate Cell

   •      Different Transistor Architecture:
           ▶ High Performance Logic in NOR:
                  • To speed the program/erase algorithm
                  • To get the fastest random access time
           ▶   Dedicated Logic in NAND, driven by the Cell Architecture
                  • To minimize the mask number
                  • To reduce the process cost

   •      Different Memory Reliability Requirement
           ▶ NOR, after Final Test, must be a perfect array (100% functionality)
           ▶ NAND is similar to a mass storage media (fault tolerant, like HD):
                  • ECC (64bit every 512)
                  • 98% array functionality (2% of bad blocks on field admitted)




                                                                          Company Confidential    |   ©2009 Micron Technology, Inc.   |   99




                               La cella EEPROM
                                          •    Sia la programamzione che la cancellazione avvengono per
                                               FN tunneling sulla regione del condensatore di tunnel

                EEPROM                    •    La lettura della cella avviene sul transistore di sensing

         Electrically Erasable            •    La memoria EEPROM è programmabile e
       and Programmable ROM                    cancellabile a livello di byte, grazie ai transistori di
                                               selezione
                                          •    Rispetto alla cella EPROM o FLASH, la cella EEPROM
                                               è molto più grande a causa del select transistor e della
                                               separazione tra la zona di scrittura e quella di lettura
                                                                                                                 ossido HV
                                                                 ossido interpoly
                                                                ossido di tunnel                 control gate
       Select Transistor
                                                                                                 floating gate

MOS tunnel capacitor
                                                                                                        lunghezza
       Sensing Region                         substrato p-                                              di canale L
                                                                                        MOS
                                                              Select                   Tunnel           Sensing
                                                             Transistor               capacitor          region


                                                                          Company Confidential    |   ©2009 Micron Technology, Inc.   |   100




                                                                                                                                                50
                                            Conclusions

• In the last decade the NVM market increased exponentially due to the
requirements of mobile applications and portable systems

• Floating gate concepts has been proven to be a very reliable mechanism
for Flash memory fabrication

• Flash memories are expected to be the mainstream NVM for the next
years

• NOR Flash is the preferred option for code storage due to their high
perormances

• NAND Flash is the preferred option for data storage dur to their very low
cost



                           December 11                                                                       Company Confidential               |     ©2009 Micron Technology, Inc.                  |    101




    Corso di Laurea in Ingegneria Elettronica - Università degli Studi di Udine




       Tecnologia e Progettazione di
     MEMORIE NON VOLATILI
                                                 Agostino Pirovano
                                                             Roberto Bez
                                                     Alessandro Grossi
                                                         Giorgio Servalli

                                                           Process R&D

                                                                   Micron

                                         Agrate Brianza (Milan), Italy

                          ©2009 Micron Technologies, Inc. All rights reserved. Products are warranted only to meet Micron’s production data sheet specifications. Information, products, and/or specifications
                          are subject to change without notice. All information is provided on an “AS IS” basis without warranties of any kind. Dates are estimates only. Drawings are not to scale. Micron and
                          the Micron logo are trademarks of Micron Technology, Inc. All other trademarks are the property of their respective owners.

                                                                                                                                                |     ©2009 Micron Technology, Inc.                  |    102




                                                                                                                                                                                                                  51
                     Tecnologia e Progettazione di
                    MEMORIE NON VOLATILI
                                                                                              3
•   PROBLEMI DI SCALABILITA’ DELLE MEMORIE FLASH

    ▶   Elementi attivi
    ▶   Elementi passivi


•   ALTRE MEMORIE NON VOLATILI

    ▶   FERAM
    ▶   MRAM
    ▶   RRAM



                                            Company Confidential   |   ©2009 Micron Technology, Inc.   |   103




                     Tecnologia e Progettazione di
                    MEMORIE NON VOLATILI                                                   4

• AN OUTLOOK INTO TE FUTURE
    ▶ Una lezione sullo scaling

    ▶ Memorie a cambiamento di fase (PCM)

    ▶ Possibili evolzioni delle memorie PCM

    ▶ Memorie a cross-point




                                            Company Confidential   |   ©2009 Micron Technology, Inc.   |   104




                                                                                                                 52
                                              Flash Cell Evolution

                   6
                  10                                                    •   Flash cell size reduction
                                                                            following the Moore’s law

                   5
                  10                                                    •   Cell basic structure
Cell Size [nm2]




                                                                            unchanged through the
                                                            2
                                                                            different generations
                   4
                  10                                      10F
                                  ?                       5F
                                                            2

                                                          NOR           •   Scaling beyond the 45 nm
                                                          NAND
                                                                            technology node for NOR
                   3
                  10
                        1
                       10                    10
                                               2                  3
                                                                 10         Flash and beyond 22nm for
                                   Technology Node F [nm]                   NAND Flash is still considered
                                                                            critical



                                                                             Company Confidential       |   ©2009 Micron Technology, Inc.   |   105




                                 Flash Cell Scaling Challenges

•                 Cell basic structure unchanged through the                                                    NAND Flash
                  different generations
•                 Cell area scaling through:
                                                                                              Y-pitch




                   ▶        Active device scaling (W/L)
                   ▶        Passive elements scaling
•                 Main scaling issues:
                   ▶        Number of stored electrons                                                              X-pitch
                   ▶        Cell proximity interference
                   ▶        Tunnel and interpoly dielectric thickness
                   ▶        Isolation spacing and WL voltage increase
                   ▶        Random Telegraph Noise
                   ▶        Trapping/detrapping, SILC
                   ▶        Retention after cycling



                                                                             Company Confidential       |   ©2009 Micron Technology, Inc.   |   106




                                                                                                                                                      53
                     Innovations in Flash Technology

    •    System management techniques
             ▶    Charge placement algorithms
             ▶    Error management techniques
             ▶
                                                                            P.Blomme et al., “A novel low voltage memory device with an
                  Multi-level memories                                        engineered SiO2/High-k tunneling barrier”, NVSMW 2003



    •    High-k dielectrics and “discrete-trap”                               High-K
                                                                             material
                                                                                 Interpoly
                                                                                                                               CHARGE
                                                                                                                               STORAGE
                                                                                                                               ELEMENT


                                                                            dielectrics
         memories                                                                dielectric           Control Gate
                                                                                                     Control   Gate
                                                                                                      Floating Gate
                                                                                                                               Tunnel
                                                                                                                               oxide

             ▶    Reduced oxide thickness                                              Source
                                                                                      Source                              Drain
                                                                                                                         Drain
                                                                                                     y-pitch
             ▶    Lower energy barrier height
             ▶    Improved reliability
    •    Fin-FET and 3D architectures
             ▶    Moves the scaling constraints along the                     Cell1                                   Cell 2


                  vertical dimension
                                                                                      Gate1                 Gate2
             ▶    Higher performance
                                                                                                Source

                                                                          A. Fazio, MRS Bulletin, Nov. 2004



                                                                  Company Confidential           |     ©2009 Micron Technology, Inc.      |   107




                   Technology Challenges for Scaling

•       Continuous technology innovations are required for Flash memories scaling
         ▶   Advanced lithography for high resolution
                 • Light wavelength reduction

                 • Methods to reduce diffraction effects must be introduced

         ▶   Thermal treatments reduction
         ▶   Self-aligned process schemes
                                                                              SELF-ALIGNED ISOLATION
                 CONVENTIONAL ISOLATION


                       S     X   W       X’



                           PITCH                                                                     PITCH




                                                                  Company Confidential           |     ©2009 Micron Technology, Inc.      |   108




                                                                                                                                                    54
    Flash Evolution: Nanocrystal and Charge-
              Trap (CT) Memories
•    Storing mechanism
      ▶   Electrons trapped into silicon
          nanocrystals or trapping centers that act
          as nano-floating gates
•    Writing mechanism
      ▶   FN or direct tunneling
      ▶   Channel hot electrons
•    Sensing mechanism
      ▶   Change in the threshold voltage
          of a MOSFET
•    Cell structure
      ▶   1 Transistor (Flash-like) structure

                                                              European Project ADAMANT

                                                       Company Confidential   |   ©2009 Micron Technology, Inc.   |   109




Nanocrystal and CT: Advantages and Issues
•    Main advantages
      ▶   Evolutionary with respect to FG memories
      ▶   Integration and full compatibility with
          conventional CMOS processes
      ▶   Robustness to parasitic FG cross-talk
          (interference coupling)
      ▶   Robustness to stress induced leakage
          current (SILC)
                                                          The distributed nature of charge
•    Main issues                                          storage makes it more robust

      ▶   Low threshold voltage shift (<3 V)              In a conventional NVM a weak
                                                          spot is fatal
      ▶   Retention and endurance characteristics to
          be deeper investigated                          Nanocrystal and CT cell allows
                                                          tunnel oxide scaling
      ▶   Difficult retention-programming trade-off
          for CT memories
      ▶   Scaling concerns related to nanocrystal
          distributions


                                                       Company Confidential   |   ©2009 Micron Technology, Inc.   |   110




                                                                                                                            55
      Samsung stacked NAND-concept
Samsung presented at IEDM 2006 a stacked NAND based on multi
silicon layers grown by epitaxy


                                   32 bit TANOS-NAND
                                  cell string with 63 nm
                                        dimension




    The integration scheme
   is based on mono crystal
         silicon epitaxy

                               Jung at al., IEDM 2006, pg. 37- 39



                                              Company Confidential   |   ©2009 Micron Technology, Inc.   |   111




        Toshiba 3D approach-concept
Toshiba presented at VLSI 2007 an interesting 90nm 3D approach
for Multi-layer TANOS-NAND technology




                                     Number of layers independent from
                                     critical steps


                              Tanaka at al., VLSI 2007, pg. 14-15




                                              Company Confidential   |   ©2009 Micron Technology, Inc.   |   112




                                                                                                                   56
          Toshiba 3D approach-concept
The proposed architecture is very challenging but the process is
really inexpensive
                                                Selector transistor and memory stack
                                                must be integrated separately (3
                                                critical mask for the NAND STRING
                                                and 1 critical mask for the routing).
                                                Due to the Overlay constraints the cell
                                                size is 6F2




 For stacked NAND (3 critical
 layers) the Cost per bit increases if
 more than 3 layers are stacked


                                                      Company Confidential   |   ©2009 Micron Technology, Inc.   |   113




            Hynix 3D floating-gate Flash

• A 3D vertical NAND Flash with floating gate




                              S. Whang et al., IEDM (2010)

                      December 11                     Company Confidential   |   ©2009 Micron Technology, Inc.   |   114




                                                                                                                           57
        3D NAND Status and Development

• 3D NAND Flash have several concerns

    ▶    All approaches have big process/fabrication issues

    ▶    More complicated P/E procedures (hole inlection, ...)

    ▶    Disturbs are increased due to shared electrodes


• It is a well-defined problem (in particular the FG
    approach) that can be effectivelly adressed by
    semicoductor industries


                                                Company Confidential   |   ©2009 Micron Technology, Inc.   |   115




                        Flash Limitations

•   Limited endurance (105 cycles)
•   Slow operations
     ▶   NOR slow write (~5-10µs/byte program, ~1 sec/Mbit erase)
     ▶   NAND slow random read (30µs)

•   Data flexibility
     ▶   NAND page program
     ▶   NAND and NOR sector erase

•   Cell scalability beyond 40 nm (in particular for NOR Flash)
•   Difficult process architecture with high-voltage devices for program
    and erase operation




                                                Company Confidential   |   ©2009 Micron Technology, Inc.   |   116




                                                                                                                     58
Key Requirements of an Alternative NVM
 •   Readiness for beyond leading edge technology node
 •   Scalability
 •   Cost structure
      ▶   MLC capable
      ▶   3D stackable
 •   Performance
      ▶   High Program and Read Throughput
      ▶   Low power
      ▶   Flexibility
 •   Reliability
      ▶   Non-volatility with long retention (e.g. > 10 years)
      ▶   Extended number of read cycles
      ▶   High program endurance




                                                         Company Confidential    |         ©2009 Micron Technology, Inc.   |   117




 Near-Term and Long-Term Alternatives
More than 35 NVM alternatives have been so far proposed…
                                                                            Polymer FeRAM
  FERAM                   PCM                                                                            Word line
                                                                                                 Word line

                                              PMC RRAM                          Bit line
                                                                                            Polymer Layer
                                                                                              Bit line          Bit line

                                                                                            Polymer Layer
                                                                                                    Word line




                                                                                                          CNT

                        MOx-RRAM          Polymer RRAM
  MRAM

                                                                                              Molecular




                                                         Company Confidential    |         ©2009 Micron Technology, Inc.   |   118




                                                                                                                                     59
                               NVM Categories
•   Electronic decoded, lithography dependent (Moore’s law follower)
     ▶   Transistor selected (like DRAM or Flash)
          •   Ferroelectric memory (FERAM)
          •   Magnetoresistive memory (MRAM and STT-MRAM)
          •   Resistive RAM (RRAM)
          •   Phase-Change Memory (PCM)

     ▶   Cross-point memories (Passive arrays)
          •   Ferroelectric polymers (PFRAM or TFEM)
          •   Organic charge-transfer complexes (conductive polymers)
          •   Resistive switching


•   Mechanical decoded, lithography independent (beyond Moore’s law)
     ▶   Probe storage (Seek and Scan, like Hard Disk or CD)
          •   Polymers
          •   Chalcogenide
          •   Ferroelectric



                                                             Company Confidential   |   ©2009 Micron Technology, Inc.   |   119




                Ferroelectric RAM (FeRAM)
•   Storing mechanism
     ▶ Permanent polarization of a ferroelectric
       material

•   Writing mechanism
    ▶ Electric field produced in the ferroelectric
      layer by the voltage applied to the
      capacitor plates

•   Sensing mechanism
     ▶ Displacement current associated to the
       polarization switch

•   Cell structure
     ▶ DRAM-like: 1 transistor, 1 capacitor
       (1T/1C)



                                                             Company Confidential   |   ©2009 Micron Technology, Inc.   |   120




                                                                                                                                  60
                        Ferroelectric Materials
•   Ferroelectric materials exhibit, over some range
    of temperature, a spontaneous electric
    polarization that can be oriented by application
    of an electric field

•   Main ferroelectric thin film materials
     ▶   PZT: Lead-Zirconate-Titanate PbZrxTi1-xO3
     ▶   SBT: Strontium-Bismuth-Tantalate Sr1-yBi2+xTa2O9
     ▶   BLT: La substituted-Bismuth-Titanate Bi4-xLaxTi3O12

•   Electrical characteristics
     ▶   High Pr value (10-30 µC/cm2)
     ▶   Switching voltage (~1.5-3 V)
     ▶   Reliability

•   Technological characteristics
     ▶   Formation temperature (usually higher than 600°C)
     ▶   Electrode interaction (Pr and integration issues)

•   MOCVD PZT dominates for scaled technologies



                                                               Company Confidential   |   ©2009 Micron Technology, Inc.   |   121




                          Operating Principles

         The basic memory element is a ferroelectric capacitor (FeCAP)
                                                                           Destructive read




                           Read out signal: Qs- Qns = 2Pr

                                                               Company Confidential   |   ©2009 Micron Technology, Inc.   |   122




                                                                                                                                    61
              FeCAP Architectures

   Offset              Stacked
                                                                 FeFET
  capacitor           capacitor




                                  Company Confidential   |   ©2009 Micron Technology, Inc.                                        |   123




         FeRAM Cell Architectures
 2T2C and 1T1C
                                                                                       Smaller cell size and better scalability



      cell
(DRAM architecture)


Chain-type FeRAM
   (NAND Flash
   architecture)


      FeFET
 (MOFET-like Flash
   architecture)




                                  Company Confidential   |   ©2009 Micron Technology, Inc.                                        |   124




                                                                                                                                            62
                      FeRAM Reliability

      Endurance
      (electrical            Retention loss                              Imprint
       fatigue)

      Polarization           Time dependent                         Shift of the
         loss                polarization loss                    hysteresis loop
      upon cycling




                                                  Company Confidential   |   ©2009 Micron Technology, Inc.   |   125




                        FeRAM Scaling
                    Planar FeCAP area scaling
Minimum capacitance for sensing:          30 fF
Operating voltage:                         1V

Minimum charge for sensing:              30 fC
Equivalent electron number:          200000
                                                                         2D FeCAP
Technology node:                          90 nm
FeCAP area:                        100 x 100 nm2
Pr:                                       20 µC/cm2

Available electron number:             25000




          3D approach necessary!
                                                                         3D FeCAP

                                                  Company Confidential   |   ©2009 Micron Technology, Inc.   |   126




                                                                                                                       63
               FeRAM: Advantages and Issues

   •     Main advantages                               •    Main issues


           ▶   Fast (<100ns) read and write                  ▶     Limited read endurance,
               operations with no intrinsic                        destructive read-out (apart
               limitation (<100ps)                                 FeFET)
           ▶   High write endurance (>1012)                  ▶     Difficult process integration
           ▶   Low voltage and low power                     ▶     Large cell size vs. Flash and
               operation                                           DRAM (>15F2)
                                                             ▶     Scaling limits and 3D capacitor
                                                                   required to go beyond the
                                                                   90nm technological node



                                                                    Company Confidential   |    ©2009 Micron Technology, Inc.   |   127




                      FeRAM Development Status
         Company         Fujitsu Matsushita                Samsung                         TI/Ramtron               Toshiba
           Source        IEDM’02    VLSI’04   VLSI’05      IEDM’05       IEDM’06               VLSI’03             ISSCC’06

   Technology Node
                            180      180       150           180             150                  130                   130
           [nm]

          Density           4Mb      1Mb       64Kb          2Mb            64Mb                 64Mb                 64Mb

              µm2-F2]
   Cell size [µ            1.3-40   2.4-74    0.27-12      0.48-15        0.34-15              0.54-32               0.61-36

                           0.49-               0.11-                        0.16-
              µm2-%]
  FeCAP size [µ                        -                   0.26-54%                            0.25-46%             0.2-32%
                           38%                 40%                          47%
                         MOCVD                MOCVD         MOCVD         MOCVD
        FE Material                  SBT                                                          PZT                   PZT
                            PZT                PZT           PZT             PZT

             µC/cm2]
        2Pr [µ              31         -        35            38              40                   24                    42

 Operation voltage [V]      1.8       2.7      <1.2          1.6              1.8                  1.3                  1.8

       Cycle time [ns]       -       2000        -            60             100                   35                    60


Low-density stand-alone (up to 4Mb) and embedded products on the market for a number
         of years in relaxed technologies (0.35 µm) from Fujitsu and Ramtron


                                                                    Company Confidential   |    ©2009 Micron Technology, Inc.   |   128




                                                                                                                                          64
         Magnetoresistive RAM (MRAM)

•   Storing mechanism
     ▶ Permanent magnetization of a
       ferromagnetic material in a Magnetic
       Tunnel Junction (MTJ)

•   Writing mechanism
    ▶ Magnetic field produced by the current
      flowing in the array bit and digit lines

•   Sensing mechanism
     ▶ Resistance change in the MTJ

•   Cell structure
     ▶ 1 transistor, 1 resistor (1T/1R)




                                               Company Confidential   |   ©2009 Micron Technology, Inc.   |   129




                        MTJ Principles
                                          • Magnetic Tunnel Junction
                                            constituted by a pinned
                                            magnetic layer, an insulator,
                                            and a free magnetic layer

                                          • Information stored in the
                                            magnetization direction
                                            (parallel or anti-parallel) of
                                            the free layer

                                          • Read out performed
                                            comparing to a reference
                                            resistance


                                               Company Confidential   |   ©2009 Micron Technology, Inc.   |   130




                                                                                                                    65
            MRAM Writing Principles

                       •   Writing mechanism
                            ▶ Vector sum of magnetic field
                               generated by Digit Line and Bit
                               Line current switch the MTJ free
                               layer (Stoner-Wohlfarth
                               switching)

                       •   Writing disturb
                            ▶ Selectivity is based on Astroid
                               diagram: half selected bits must
                               not switch

                       •   Writing current
                            ▶ Digit Line and Bit Line current
                               each ~ 5-10mA

                       •   Key issue
                            ▶ Complex bit shape and
                              uniformity



                                 Company Confidential   |   ©2009 Micron Technology, Inc.   |   131




            MRAM Cell Architectures


  Cross-point
  architecture

                                          N. Sakimura et al., ISSCC 2003




MOSFET-selected
  architecture


                              W. J. Gallagher, Taiwan NVM Workshop, 2005



                                 Company Confidential   |   ©2009 Micron Technology, Inc.   |   132




                                                                                                      66
                        Toggle MRAM
Savtchenko switching “Toggle”: antiparallel bilayer free layer oriented
45°° with respect to the write wires, written by rotating the magnetic
field




                                       M. Durlam et al., IEDM Tech. Dig., 2003

     Program disturb issue is resolved, but a larger programming current
                 is required (~7mA vs. ~4mA of SW MRAM)


                                                 Company Confidential   |   ©2009 Micron Technology, Inc.   |   133




                      MgO-based MTJ




  A larger Tunneling Magnetoresistance Ratio (TMR) can be achieved
     in MgO-based MTJ devices (up to 220% at room temperature)


                                      W. J. Gallagher, Taiwan NV Memory Workshop, 2005


                                                 Company Confidential   |   ©2009 Micron Technology, Inc.   |   134




                                                                                                                      67
               Interconnections Scheme




                                                        M. Durlan et al., IEDM Tech. Dig. 2003



                                                 Company Confidential    |   ©2009 Micron Technology, Inc.   |   135




                        MRAM Reliability

•   Electromigration of programming metal lines
    (~10 MA/cm2)                                                               M3
•   Tunnel barrier dielectric reliability                    MTJ
                                                                               M2
•   Back-end-of-line dielectric deposition and
    thermal budget

•   MTJ stack delamination                                              “Keeper” or “liner”

•   Front-end-of-line contamination due to new
    material integration                                                       M3

•   Soft error rate for thermally activated
                                                             MTJ
    random switching                                                           M2


                                                 Company Confidential    |   ©2009 Micron Technology, Inc.   |   136




                                                                                                                       68
                                MRAM Scaling
                                         Failure probability
                                      Eb +Eb
                                     − 1    2
                                 t
                                − e     kBT

                  P ( t ) = 1− e τ              ≤ 1ppm @85°C for 10 years

                                           Thermal stability

                Eb1 ∝ kV                             Higher k or larger volume V

                Eb2 ∝ AR −1                           Higher aspect ratio AR


                                          Power consumption

                Hwrite1 ∝ k
                                                      High programming current
                Hwrite2 ∝ AR −1


                                                               Company Confidential   |   ©2009 Micron Technology, Inc.   |   137




                                MRAM Scaling
•   Thermal stability

     ▶   Smaller cell volume implies a lower thermal stability
     ▶   Compromise between power consumption and thermal stability

•   Power consumption

     ▶   High power consumption as large magnetic fields required for switching
         (~4mA in standard MRAM and ~7mA for Toggle MRAM)
     ▶   Power consumption will increase upon scaling due to cell shape
         anisotropy

               1st generation not expected to be viable
                 beyond the 90 nm technology node


                                                               Company Confidential   |   ©2009 Micron Technology, Inc.   |   138




                                                                                                                                    69
                   MRAM: Advantages and Issues

 •     Main advantages                                •      Main issues


         ▶   Fast write (<100 ns)                            ▶   Difficult process integration
         ▶   High write endurance                            ▶   Large cell size vs. Flash and
         ▶   Low voltage write                                   DRAM
                                                             ▶   Large write current
                                                                 (> 10 mA/B)
                                                             ▶   Small read signal
                                                             ▶   Scaling limits




                                                                    Company Confidential   |   ©2009 Micron Technology, Inc.   |   139




                     MRAM Development Status
                                             Nec                                  IBM            Freescale
     Company         Motorola   Renessas              TSMC       Samsung                                                Hitachi
                                           Toshiba                            Infineon         STM Philips

                                                                  VLSI-         VLSI-
       Source        ISSCC’04   VLSI’04    IEDM’04 IEDM’04                                     VLSI-TSA’05            ISSCC’07
                                                                 TSA’05        TSA’05
Technology Node
                       180        130        130      180          240            180                 90                  200
        [nm]

      Density          4Mb        1Mb        1Mb      1Kb         64Kb           16Mb                4Kb                  2Mb

           µm2-F2]
Cell size [µ         1.55-48    0.81-48    0.1152-7 1.49-46         -          1.42-44            0.29-36              2.56-64

      Cell type      1T-1MTJ    1T-1MTJ     1MTJ     1T-2MTJ     1T-1MTJ      1T-1MTJ            1T-1MTJ               SP-MTJ

Current/bit [mA]        9          -          4        2.5          -               5                   -                  0.2

     Operation
                     1.8/3.3      1.2        1.5       1.8          -          1.8/2.5                  -                  1.8
     voltage [V]
 Cycle time [ns]        -          -         250       40           -              30                   -                 100



             Freescale Semiconductor Inc. started commercial shipment of
               4Mb MRAM (39F2 cell size, 35 ns cycle time) in July 2006


                                                                    Company Confidential   |   ©2009 Micron Technology, Inc.   |   140




                                                                                                                                         70
                MRAMs today
                          •   0.18 µm CMOS with 3 layers of
                              Al and 2 layers of Cu
                              interconnects
                          •   Cladded write lines
                          •   3.3 V supply voltage
                          •   Symmetrical 35 ns read and
                              write timing
                          •   Cell size = 1.55 µm2 (48 F2)
                          •   Die size 4.5 x 6.3 mm2
    4 Mb MRAM die,
Freescale, now Everspin
   (16 Mb available)

                                Company Confidential   |   ©2009 Micron Technology, Inc.   |   141




Thermal-Assisted MRAM (TA-MRAM)




                              R. Sousa et al., EPCOS 2006


                                Company Confidential   |   ©2009 Micron Technology, Inc.   |   142




                                                                                                     71
                     Spin Transfer Effect


•   Incoming electrons lose
    transverse component of spin in
    the ferromagnetic layer


•   Momentum conservation implies a
    torque applied by electron current


•   Over a threshold Jc, current can
    switch magnetization                            C. Chappert lecture (2008)




                                              Company Confidential   |   ©2009 Micron Technology, Inc.   |   143




           Spin transfer torque: write “0”




•   Two ferromagnetic layers separated by a non-magnetic metallic spacer
•   Fixed layer spin-polarizes the current
•   The torque switches the free layer magnetization

                                              Company Confidential   |   ©2009 Micron Technology, Inc.   |   144




                                                                                                                   72
                Spin transfer torque: write “1”




      •   Electrons injected from the free layer
      •   Spin-dependent scattering reflects electrons with spin opposite to fixed
          layer magnetization
      •   Torque exerted by reflected electrons
145                                                  Company Confidential   |   ©2009 Micron Technology, Inc.   |   145




                                STT MRAM cell




            • No digit line, no cladding ⇒ ideally, a 6F2 cell

            • Potentially scalable to 20 nm

                                                     Company Confidential   |   ©2009 Micron Technology, Inc.   |   146




                                                                                                                          73
SPRAM or STT-MRAM (Spin-transfer torque RAM)
•    Basic concept
      ▶ In a conventional MRAM, the parallel or
        anti-parallel configuration is formed by
        applying a cross-point synthetic field
        induced by a current passing through
        bit/word lines
      ▶ SPRAM uses the current-induced
        switching caused by spin-transfer
        torque

•    Advantages
      ▶ Cell size: 4F2, but limited by CMOS
        selector to 4F2
      ▶ Can mitigate some MRAM issues

•    Issues
      ▶ Self-read disturbance
      ▶ Writing time depends on the
        device area
      ▶ Integration                             K. Miura et al., VLSI Symp. on Tech. 2007


                                                              Company Confidential   |   ©2009 Micron Technology, Inc.   |   147




     Low-power and Embedded Applications

 •   FeRAM advantages                               •        MRAM advantages
      ▶   Fast (<100 ns) and low energy write                 ▶    Fast (<100 ns) read and write

      ▶   Low voltage and low power operation                 ▶    Very high write endurance
                                                              ▶    Low/mid voltage operation

 •   FeRAM Main issues
      ▶   Large cell size vs. Flash and DRAM        •        MRAM Main issues
      ▶   Scaling limits                                      ▶    Large cell size vs. Flash and DRAM
                                                              ▶    Scaling limits (better situation for STTMRAM)




 •   Small densities low voltage and low        •       Small densities embedded high
     power high performance (niche) market              performance market
      ▶   Contactless smartcards and ID tags             ▶     Micro and embedded applications

      ▶   Ultra low-power applications                   ▶     Portable and battery operated high
                                                               performance systems




                                                              Company Confidential   |   ©2009 Micron Technology, Inc.   |   148




                                                                                                                                   74
                           Resistive RAM (RRAM)
                                                                                 1.00


    •    Storing mechanism                                                       0.75

                                                                                 0.50
                                                                                                                                ON
                                                                                 0.25




                                                                 Current [mA]
            ▶   Resistive switching of a storage layer                          0.00
                                                                                              OFF                1m
                                                                                -0.25                           100µ
                                                                                                                                      ON
                                                                                                                 10µ



         Writing mechanism
                                                                                                                  1µ

    •                                                                           -0.50                           100n
                                                                                                                 10n                  OFF
                                                                                -0.75                                1n
                                                                                                                100p
                                                                                                                   0.0    0.1   0.2        0.3    0.4   0.5



            ▶
                                                                                -1.00
                Current or voltage-induced                                          -1.5    -1.0    -0.5       0.0        0.5               1.0          1.5

                conductance switching                                                                      Voltage [V]




    •    Sensing mechanism

            ▶   Resistance change

    •    Cell structure

            ▶   1 transistor, 1 resistor (1T/1R) or
                cross-point (1R)



                                                         Company Confidential                 |     ©2009 Micron Technology, Inc.                              |   149




                    RRAM Proposed Alternatives
•       Chalcogenide

        ▶   GST and other phase-change alloys
        ▶   AgGeSe, AgGeS, WO3 and SiO2 solid
            electrolyte

•       Binary oxide
        ▶   Nb2O5, Al2O3, Ta2O5, TiO2, ZrOx , CuxO                                  M. Kozicki, EPCOS 2006
            and NiO

•       Oxides with perovskite structure

        ▶   SrZrO3, doped- SrTiO3, Pb(ZrxTi1-x)O3
            and Pr0.7Ca0.3MnO3

•       Conductive polymers
        ▶   Bengala Rose, AlQ3Ag, Cu-TCNQ
                                                                                           A. Chen et al.,
                                                                                           IEDM Tech. Dig. 2005

                                                         Company Confidential                 |     ©2009 Micron Technology, Inc.                              |   150




                                                                                                                                                                         75
                     Resistive Oxides Memories
•    Basic concept
      ▶ Resistive switching in a binary oxide
        layer
      ▶ Can be coupled with an oxide based
        selecting diode

•    Advantages                                                     I. G. Baek et al., IEDM Tech. Dig. 2005
      ▶ Cell size: 4-8 F2/n
      ▶ Very low-cost solution
      ▶ Reasonably good endurance and
        performance

•    Issues
      ▶ Leakage current
      ▶ Programming current quite high
      ▶ Temperature stability
      ▶ Switching mechanism still controversial



                                                                     I. G. Baek et al., IEDM Tech. Dig. 2004

                                                                    Company Confidential   |   ©2009 Micron Technology, Inc.   |   151




           Programmable Metallization Cells
    Programmable metallization cell (PMC): a conductive filament of silver
    is created by diffusion into a chalcogenide (solid electrolyte) by
    applying an electric field


                                                       Oxidizable
                                                       electrode
Metallic electrodeposit
low resistance
                                         Ion current




                          M → M + + e-


Glassy electrolyte
high resistance       M + + e- → M

                                                       Inert
                                                       electrode




               M. Kozicki, EPCOS 2006                               M. Kund et al., IEDM Tech. Dig., 2005



                                                                    Company Confidential   |   ©2009 Micron Technology, Inc.   |   152




                                                                                                                                         76
                      Polymeric Memories
•   Basic concept
     ▶ Storage material located at the cross
       points
     ▶ Several polymers proposed for the
       storage element (Rose Bengal,
       Fluorescine-based polymer,DDQ, TAPA,
       Cu:TCNQ)
     ▶ Can be coupled with a polymeric
       selecting diode
                                                                   1.00

•   Advantages                                                     0.75

     ▶ Cell size: 4-8 F2/n                                         0.50
                                                                                                                       ON
     ▶ Very low-cost solution                                      0.25




                                                   Current [mA]
                                                                  0.00

•   Issues                                                        -0.25
                                                                                 OFF                   1m
                                                                                                      100µ
                                                                                                                            ON

     ▶ Leakage current
                                                                                                       10µ
                                                                                                          1µ
                                                                  -0.50
     ▶ Poor performance
                                                                                                      100n
                                                                                                      10n                   OFF
                                                                  -0.75                                   1n

     ▶ Integration and temperature stability                                                          100p
                                                                                                         0.0   0.1    0.2        0.3    0.4   0.5
                                                                  -1.00
                                                                      -1.5     -1.0      -0.5       0.0         0.5               1.0          1.5
                                                                                                Voltage [V]

                                                    A. Pirovano et al., Solid-State Electronics, 2005

                                                                  Company Confidential    |     ©2009 Micron Technology, Inc.                 |     153




            RRAM: Advantages and Issues

•   Main advantages                        •   Main issues


     ▶   Good read signal window               ▶   Low maturity, no multi-Mb test-
         (factor ten in resistance)                chip has been so far presented
     ▶   Medium/low voltage write              ▶   Difficult process integration (low
     ▶   Low programming current and               thermal budget required)
         energy                                ▶   Retention capabilities for 10years
     ▶   Cross-point solutions available           at 85°C must be demonstrated

     ▶   Good scalability




                                                                  Company Confidential    |     ©2009 Micron Technology, Inc.                 |     154




                                                                                                                                                          77
                         Key Learnings
  •    Opportunities exist in the NVM market for new memory concepts
       that can provide a competitive advantage, but...




                                              Company Confidential   |   ©2009 Micron Technology, Inc.   |   155




 Floating-Gate NVM (Successful) History
1967     First Floating Gate Structure
  1971       FAMOS

        1977     EPROM
            1980     EEPROM
                1985      1T EEPROM (Flash)
                     1988     NOR Flash
                         1989     NAND Flash
                             1995     MLC NOR
                                 2005     MLC NAND
                                      2010     Intel-Micron 64Gb MLC
                                               NAND in 25nm tech.


                                              Company Confidential   |   ©2009 Micron Technology, Inc.   |   156




                                                                                                                   78
                                NVM Market Timeline
• New memory technologies are                                                                                       Year of 1st            Memory
                                                                                                                    Shipment             Technology
  rare                                                                                                                 1969                    SRAM
                                                                                                                       1970                    DRAM
   ▶   SRAM, DRAM, EPROM are 30 years old                                                                              1971                   EPROM
       concepts                                                                                                        1988                 NOR Flash
                                                                                                                       1995              NAND Flash
   ▶   Evolutionary changes for NVM
                                                                                                                       1997                 MLC NOR
         •   EPROM            E2PROM                  Flash

   ▶   Even less innovation for volatile RAM                                                           1000
                                                                                                        900

• Displacement timeline for                                                                             800
                                                                                                        700                                       Flash




                                                                                        Revenue [M$]
  revenues cross-over                                                                                   600
                                                                                                        500
                                                                                                                      1st Flash
                                                                                                                      product
   ▶   5 years needed from first Flash product                                                          400          availability
                                                                                                        300
       availability in 1988 and the revenue                                                             200

       crossover with EPROM in 1992                                                                     100                                        EPROM
                                                                                                         0
                                                                                                         1987 1988 1989 1990 1991 1992 1993 1994 1995 1996
                                                                                                                                     Year

                                                                                                         Company Confidential   |   ©2009 Micron Technology, Inc.       |   157




                History of PCM Development
                S. Lai and T. Lowrey,                     F. Pellizzer et al.,              F. Pellizzer et al.,                            G. Servalli,
                     IEDM 2001                                VLSI 2004                         VLSI 2006                                   IEDM 2009
                                                               180nm                              90nm                                         45nm
                        180nm



  PCM
  cell



                                 M. Gill et al.,                G. Casagrande et al.,                                  Bedeschi et al.,              C. Villa et al.,
                                 ISSCC 2002                          VLSI 2004                                           ISSCC 2008                   ISSCC 2010
                                                                       180nm                                       90nm 128Mb (256Mb MLC)              45nm 1Gb
                                    180nm




  PCM array
    & chip



                  2001                             2003                          2005                         2007                   2009                        2011


                            Concept                                              Technology Validation                                   Manufacturing
                          Demonstration                                            Product Reliability

                                                                                                         Company Confidential   |   ©2009 Micron Technology, Inc.       |   158




                                                                                                                                                                                  79
                                 Key Learnings
  •      Opportunities exist in the NVM market for new memory concepts
         that can provide a competitive advantage, but...

  •      … disruptive innovation takes a lot of time!




                                                            Company Confidential   |   ©2009 Micron Technology, Inc.   |   159




          NOR Flash Technology Evolution
                                        CMOS Scaling path
         1992             1998               2002                2004                          2007




         0.8 µm          0.35 µm             180 nm           130 nm                           65 nm

• WSi2                • W contact plug • Si3N4 borderless   • Diff. Si3N4                 • 3 Cu metals
• Single Gate Oxide   • 2 Gate Oxides    contact              spacers

• Single Al Metal     • 2 Al/Cu Metal    • TiSi2            • CoSi2
                                         • Dual Poly CMOS
                                         • 3 Metal

Leverage on:
• Standard CMOS roadmap
• Specific technologies for Flash


                                                            Company Confidential   |   ©2009 Micron Technology, Inc.   |   160




                                                                                                                                 80
                       The MRAM lesson
•   Magnetic memory concepts dates back to the
    1955, with the introduction of the first magnetic
    core memory
•   In 1995 - Motorola initiates work on MRAM
    development
•   2003 - A 128 kbit MRAM chip was introduced,
    manufactured with a 180 nm lithographic process
•   2004 - MRAM becomes a standard product offering
    at Freescale Semiconductor                                                Freescale MRAM chip

•   2006 - Freescale Semiconductor begins marketing
    a 4-Mbit MRAM chip at 180nm
•   2007 - R&D moving to spin transfer torque
    MRAM (STT-MRAM)
                                                                              Fujitsu STT-MRAM chip


                                                   Company Confidential   |   ©2009 Micron Technology, Inc.   |   161




                           Key Learnings
    •   Opportunities exist in the NVM market for new memory concepts
        that can provide a competitive advantage, but...

    •   … disruptive innovation takes a lot of time!

    •   To be successful in the memory market, a new NVM concept must
        be scalable well beyond the actual leading-edge technology node




                                                   Company Confidential   |   ©2009 Micron Technology, Inc.   |   162




                                                                                                                        81
                   Chalcogenide Alloys
       Alloys with an element of the VI group of the periodic
       table, usually combined with IV and V group elements

  IVA VA      VIA VIIA

   C N         O F                • As2S3                     • As2Se3

  Si P         S Cl               • As2Te3                    • Sb2Te3

  Ge As Se Br                     • SnSb2Te4                  • Ge41Sb12Te41Se6

  Sn Sb Te I                      • GeTe                      • Ge2Sb2Te5 (GST)

  Pb Bi Po At                     • Ge1Sb4Te7


Chalcogenic elements

                                                Company Confidential   |   ©2009 Micron Technology, Inc.   |   163




            Chalcogenide Applications

                                                            Photoconductive
1970           Xerography                                      properties



                 DVD-RW
1990             CD-RW

                                                                   Reversible
                                                                  Phase-Change
2000            Memories

        OUM (Ovonic Universal Memory)
         PCM (Phase Change Memory)
          PRAM (Phase-change RAM)



                                                Company Confidential   |   ©2009 Micron Technology, Inc.   |   164




                                                                                                                     82
    Phase Change Memory: New Materials
          Certain alloys containing one or more group VI elements
          (Chalcogenides) exhibit reversible transition between the
                  disordered and ordered atomic structure




                                                Pseudo-binary (GeTe)x-
                                                (Sb2Te3)y compositions:

                                                – GeSb4Te7
                                                – GeSb2Te4
                                                – Ge2Sb2Te5




                                                 Company Confidential    |    ©2009 Micron Technology, Inc.      |   165




            Phase Change Memory (PCM)
                                                                         Amorphous Crystalline

•   Storing mechanism
     ▶   Amorphous/poly-crystal phase of chalcogenide
         alloy (Ge2Sb2Te5 – GST)                                        High resistivity Low resistivity



•   Writing mechanism                                                  Temperature

                                                                                  Reset (amorphization)
     ▶   Current-induced Joule effect                                    T
                                                                         m               Set (crystallization)
                                                                         Tx

•   Sensing mechanism                                                                           Time


     ▶   Resistance change of the GST

•   Cell structure                                                 I

     ▶   1 transistor, 1 resistor (1T/1R)
                                                                                    V



                                                 Company Confidential    |    ©2009 Micron Technology, Inc.      |   166




                                                                                                                           83
            PCM Storage Element

                     Top electrode


    Active region

          Resistor                       Crystalline
                                            GST


    Bottom electrode

                                Company Confidential   |   ©2009 Micron Technology, Inc.   |   167




             Sensing Mechanism


                                                              SET “1”
                                                              Crystal
I                                                          Low resistance




                                                           RESET “0”
              V                                        Amorphous High
                                                         resistance




                                Company Confidential   |   ©2009 Micron Technology, Inc.   |   168




                                                                                                     84
                Joule Heating

   Top electrode
                                                                              Temp C




              Crystalline
 Resistor        GST
 (Heater)
                             Simulation of temperature distribution
                                  during PCM programming
 Bottom electrode

                                  Company Confidential   |   ©2009 Micron Technology, Inc.   |   169




 PCM Operating Principles - Set to Reset


                          SET
Temperature

 Tm


                   Time
                          RESET


                                  Company Confidential   |   ©2009 Micron Technology, Inc.   |   170




                                                                                                       85
        PCM Operating Principles - Reset to Set


                                                    RESET
Temperature

               Tm
               Tx
                                                Time
                                                                        SET


                                                                                                     Company Confidential     |   ©2009 Micron Technology, Inc.    |    171




                         Fundamental Characteristics

                 Current-voltage curve                                                               Programming curve

                                                                                           6
               0.75                                                                       10
                        Crystal                                                                                     Crystal
                        Amorphous                                                                                   Amorphous
                                                 Reset
                                                                        Resisstance [Ω]




                                                                                           5
Current [mA]




               0.50                                                                       10
                                                                                                Read                        Set                   Reset
                                                          Temperature




                                                 Set                                       4
               0.25                                                                       10


                                    Vth
                                                 Read
                                                                                           3
               0.00                                                                       10
                  0.0       0.5           1.0           1.5                                    0.0   0.1      0.2       0.3       0.4       0.5       0.6         0.7
                             Voltage [V]                                                             Programming Current [mA]



                                                                                                     Company Confidential     |   ©2009 Micron Technology, Inc.    |    172




                                                                                                                                                                              86
                                      Basic Physical Mechanisms
                                                               0.75
                                                                         Crystal
                                                                         Amorphous




                                                Current [mA]
                                                               0.50




                                                               0.25


                                                                                         Vth
                                                               0.00
                                                                  0.0         0.5              1.0          1.5
                                                                               Voltage [V]

                                                                                         Joule Heating and Phase Change
                     Electronic Switching                                                        (Memory Effect)
                         (Reversible)


                                            +
                                + +    +    +
SHR recombination                                                       Impact
  through traps                                                       ionization

                                                                                                          Company Confidential   |   ©2009 Micron Technology, Inc.   |   173




                                            Reset Programming

                       6
                    2x10
                                 F. Ottogalli et al., ESSDERC 2004                                                                        treset
                       6
                     10
  Resistance [Ω ]




                                                                                                                  Vreset
                                                                                         VRESET
                       5
                                                                                         1.0 V
                     10                                                                  1.1 V
                                                                                         1.2 V
                       4
                    5x10
                           10    15    20       25                30     35         40    45         50
                                            Pulse Width [ns]

                            PCM cell can be reset in 10ns with a good reading window


                                                                                                          Company Confidential   |   ©2009 Micron Technology, Inc.   |   174




                                                                                                                                                                               87
                                                                                Set Pulse Width
                                                         F. Ottogalli et al., ESSDERC 2004
                                                 6
                                             10




                                                 5
                                             10
                           Resistance [Ω ]




                                                                                                                                                                             tset

                                                 4            10 µs
                                             10               250 ns
                                                              100 ns
                                                              40 ns
                                                              20 ns
                                                 3
                                             10
                                                     0        100      200    300      400      500                600
                                                                    Programming Current [µA]

                                                                           PCM cell can be set with 20ns pulses
                                                                          still maintaining a good reading window


                                                                                                                                          Company Confidential       |   ©2009 Micron Technology, Inc.    |    175




                                                                                       Endurance
                                                 F. Ottogalli et al., ESSDERC 2004                            F. Pellizzer et al., VLSI Symp. on Tech. 2003
                           12                                                                                                7
                          10                                                                                                10

                           11
                          10                                                  Experimental
Endurance [# of cycles]




                                                                                             -1.05                           6
                                                                              Best Fitting W                                10
                           10
                          10
                                                                                                          Resistance [Ω ]




                               9                                                                                             5
                                                                                                                            10                          RESET
                          10
                                                                                                                                                        SET
                               8
                          10
                                                                                                                             4
                                                                                                                            10
                               7
                          10

                               6                                                                                             3
                          10                                                                                                10
                                                                                                                                  0   1       2     3     4      5       6     7    8     9    10    11       12
                                             1            2            3        4         5           6
                                10                       10          10       10        10           10                          10 10 10 10 10 10 10 10 10 10 10 10 10
                                                          RESET Pulse Width W [ns]                                                                  Number of cycles [#]


                                      •           Reset operation has the strongest impact on endurance performance
                                      •           More than 1011 cycles have been demonstrated



                                                                                                                                          Company Confidential       |   ©2009 Micron Technology, Inc.    |    176




                                                                                                                                                                                                                     88
                                                                Data Retention
                         A. Pirovano et al., IEDM Tech. Dig. 2003                          M. Gill et al., ISSCC 2002
                              10
                             10
                                  9
                             10        10 years
                                  8
                             10
  Crystallization Time [s]




                                  7
                             10                                      110 °C
                                  6
                             10
                                  5
                             10
                                  4
                             10
                                  3
                             10
                                  2
                             10
                                  1
                             10
                                  20      22      24   26      28     30      32   34
                                                                -1
                                                       1/kBT [eV ]

 • The activation energy is 2.6 eV
                                                                                                               More than 300
 • 10 years at 110°
                  °C have been                                                                                 years at 85°
                                                                                                                          °C
   extrapolated


                                                                                        Company Confidential    |   ©2009 Micron Technology, Inc.   |   177




                                                       Multilevel Capabilities




S. Lai, IEDM Tech. Dig. 2003


                                                                                        Company Confidential    |   ©2009 Micron Technology, Inc.   |   178




                                                                                                                                                              89
                     PCM Cell Structure
    Cell Structure: 1 selector + 1 storage element



             Transistor                  Resistor:
             • BJT                       heater/material
             • MOSFET                    • Heater
             • Diode
                                              – Sub-litho contact
        Bit line              Bit line        – µTrench
                   Storage
                                              – Planar options
                   element
Word line            Word line           • Material
                                              – GST
                   Selector




                                           Company Confidential   |   ©2009 Micron Technology, Inc.   |   179




                   Program disturb issue




     The program operation induces unwanted heating on
       adjacent bits that may results in thermal disturb

                                           Company Confidential   |   ©2009 Micron Technology, Inc.   |   180




                                                                                                                90
                 Cross-talk results




                                       Company Confidential   |   ©2009 Micron Technology, Inc.   |   181




          Ultimate scalability of PCM




                                            D. Wright et al., EPCOS 2004




Device functionality demonstrated on
60 nm2 active area
Phase change mechanism appears
scalable to at least ~5nm                  C. Lam, SRC NVM Forum 2004


                                       Company Confidential   |   ©2009 Micron Technology, Inc.   |   182




                                                                                                            91
       Materials for Phase Change Memory
Many chalcogenide materials are available for use in solid state memories,
exploiting the experience of optical disk research
                                                  • But other requirements must be satisfied:

                        Ge or M (at %)                • Electronic switching capability with reasonable
                        0 100                           switching voltage
                   10       90
     GeSbTe(GST) 20          80      Doped SbTe       • Sufficiently low set resistance for reading
                30               70
                                                        performances
         GeTe 40                   60
                                         DVD+RW
              50                    50
   DVD+RAM
            60                        40
                                                      • Sufficiently low melting temperature for program
           70
                    225                 30              performances
         80                               20
        90           124
                             M-Sb2Te 10               • Stability under million of cycles
     100     147
                                       0
        0 10 20 30 40 50 60 70 80 90 100              • Higher crystallization temperature for better
    Te (at %)      Sb2Te3 Sb2Te       Sb (at %)         retention

  From optical disk experience Ge, Sb, Te, In, Si compounds are most
  suitable materials for employment in solid state devices


                                                                   Company Confidential   |   ©2009 Micron Technology, Inc.   |   183




                                           PCM yesterday

                                                        1970
                                                        Die:                122 mil X 131 mil
                                                        Capacity:           256 bits
                                                        Reset:              ~200 mA, < 25V, 5 µs
                                                        Set:                5 mA, ~ 25V, 10 ms
                                                        Read:               2.5 mA, < 5V


                                                        “Nonvolatile and Reprogrammable,
                                                        the Read-Mostly Memory is Here,”
                                                        R. G. Neale, D. L. Nelson, and
                                                        Gordon E. Moore, Electronics
                                                        (Sept. 1970) p. 56.




                                                                   Company Confidential   |   ©2009 Micron Technology, Inc.   |   184




                                                                                                                                        92
  90nm Technology - 128Mb “Alverstone” Product

                                        Process Architecture
                                        •   PCM cell
                                             ▶ Salicided minimum-size BJT selector
                                             ▶ Self-aligned “Wall” Structure
                                             ▶ 1 Base Contact / 1 Emitter
                                             ▶ 0.097 µm2 cell size

                                        •   CMOS architecture
                                             ▶   Single gate oxide (8 nm to manage
                                                 3V operation)
                                             ▶   Dual-flavor poly & CoSi2
                                        •   3 Cu levels for tight interconnects


                                                              Company Confidential   |   ©2009 Micron Technology, Inc.   |   185




             Omneo™ PCM Products Overview


Omneo P5Q PCM                                                                Omneo P8P PCM
• Single, dual, and quad I/O                                                 • High-performance parallel
  serial interface                                                               interface
• 128Mb density                                                              • 128Mb density
• 2.7 – 3.6V supply voltage                                                  • 2.7 – 3.6V supply voltage
• 66Mhz clock (50MHz in x4                                                   • 1.7 – 3.6V i/o voltage
  mode)                                                                      • 0.7 MB/s programming time
• SOIC-16 package                                                            • 56l TSOP; 64b Easy BGA
                                                                                 package options



                Omneo PCM Delivers Value to Embedded Applications
            • Byte alterable, No erase required, Over-write capability

            • 1M write cycles delivers 10X flash endurance capability



                                                              Company Confidential   |   ©2009 Micron Technology, Inc.   |   186




                                                                                                                                   93
                       PCM: Advantages and Issues

    •     Main advantages                                     •   Main issues
            ▶    Fast write (<100ns)                               ▶   Process integration for GST
            ▶    Good read signal window (factor                   ▶   Heater-GST interface
                 ten in resistance)                                    optimization
            ▶    Medium/low voltage write                          ▶   Writing current reduction
            ▶    Long endurance                                    ▶   Retention at very high
                                                                       temperature (150°C)
            ▶    Cell size comparable to Flash
                 and DRAM
            ▶    Good scalability

            ▶    MLC capabilities




                                                                        Company Confidential   |   ©2009 Micron Technology, Inc.   |   187




                                       PCM Active Material
Despite Ge2Sb2Te5 has been demonstrated a good material for PCM fabrication, many
other chalcogenide materials are available for use in solid state memories, exploiting
the experience of optical disk research
                                                      But other requirements must be satisfied:

                           Ge or M (at %)                 • Electronic switching capability with reasonable
                          0 100                             switching voltage
                       10     90
         GeSbTe(GST) 20         80     Doped SbTe         • Sufficiently low set resistance for reading
                    30            70
                                                            performances
          GeTe 40                  60
                                         DVD+RW
               50                   50
    DVD+RAM
             60                       40
                                                          • Sufficiently low melting temperature for
            70
                         225            30                  program performances
          80                              20
            90
                 147
                          124
                                M-Sb2Te  10               • Stability under million of cycles
         100                               0
            0 10 20 30 40 50 60 70 80 90 100              • Higher crystallization temperature for better
        Te (at %)      Sb2Te3 Sb2Te       Sb (at %)
                                                            retention



   From optical disk experience Ge, Sb, Te, In, Si compounds are most suitable
   materials for employment in solid state devices

                                                                        Company Confidential   |   ©2009 Micron Technology, Inc.   |   188




                                                                                                                                             94
                 Fast Crystallization Alloy




     M. Boniardi et al., IMW 2010

•   Decrease of the reset resistance with the increase in the Sb
    concentration
•   Convergence of the set level to the minimum set
•   Faster crystallization

                                                 Company Confidential   |   ©2009 Micron Technology, Inc.   |   189




               Higher-Temperature Alloy

                                       “N-doped GeTe as Performance Booster for
                                          Embedded Phase-Change Memories”
                                               A. Fantini et al., IEDM 2010




                                      “On Carbon doping to improve GeTe-based
                                       Phase-Change Memory data retention at
                                                 high temperature”
                                          G. Betti Beneventi et al., IMW 2010



                                    “Electrical Performances of Tellurium-rich Gex-Te1-x
                                                  Phase Change Memory”
                                               G. Navarro et al., IMW 2011



                                                 Company Confidential   |   ©2009 Micron Technology, Inc.   |   190




                                                                                                                      95
        3D Integration Cross-Point Memory

• Crossbar memory attracts great interests
  ▶   “simple” structure and minimum cell size (4F2)
         low cost
  ▶   suitable for 3D stacking    cell size (4/n)F2
  ▶   array over circuitry   better array efficiency


                                                                              Vprog
• The basic cell architecture requires a                 Vprog/2                              Vprog/2


  selector structure to be integrated in the
  BEOL                                                                                                          Vprog/2


  ▶   Parasitic paths exist through neighbouring cells
                                                                                                               0V
  ▶   Programming (and also reading) can perturb
      the array                                                                                                 Vprog/2




                                                              Company Confidential    |   ©2009 Micron Technology, Inc.   |   191




          A Wide Range of Material Choices


                                                         Selector device options
                                                       • Homojunctions                     polySi p/n
                                                         junctions
                                                       • Heterojunctions                     p-CuO/n-InZnO
                                                       • Schottky diode                   Ag/n-ZnO
                                                       • Chalcogenide Ovonic Threshold
   For the selector structure                            Switching (OTS) materials
                                                       • Mixed Ionic Electronic Conduction
      few concepts have been                             (MIEC) materials
   proposed so far, all in the
       “path finding” phase


                                                              Company Confidential    |   ©2009 Micron Technology, Inc.   |   192




                                                                                                                                    96
         Cross-Point Switch Requirements

• Very high forward bias current
     ▶   greater than the switching current

• Low reverse bias current
     ▶   Prevent loss of signal by cross talk
     ▶   Leakage may set the block size

• Composition compatible with memory material
• Low temperature process

• Bipolar operation is preferred




                                                Company Confidential   |   ©2009 Micron Technology, Inc.   |   193




                            Key Learnings
 •   Opportunities exist in the NVM market for new memory concepts
     that can provide a competitive advantage, but...

 •   … disruptive innovation takes a lot of time!

 •   To be successful in the memory market, a new NVM concept must
     be scalable well beyond the actual leading-edge technology node

 •   In the last ten years PCM has demonstrated to be able to follow
     the scaling rules and to have room for entering in the sub-10nm
     domain




                                                Company Confidential   |   ©2009 Micron Technology, Inc.   |   194




                                                                                                                     97
  Selectors and PCM Array Architectures
                          MOSFET                       BJT/Diode                                           OTS
                                                   Dedicated steps for the
   Process        No mask overhead for                                                      Dedicated steps in the
                                                       p-n-p junction
 Complexity               the selector                                                                     BEOL
                                                           integration

   Cell Size         Larger (~20F2)                    Smaller (~5F2)                       3D cross-point (~4F2/n)

Memory Array
                      Conventional                         Innovative                                Ground-breaking
Organization

                                                      High density/
 Application      Embedded memory                                                               Very high density
                                                    High Performance
                                BL                    WL


Schematic Cell                                                BL
                                                                                                BL
                    GND
  Structure                                                                                                   OTS
                              WL                                                                              OUM
Cross-section        n+                 n+   STI              p+
                                                             n-well
                                                                        n+                                     WL
                          p-substrate
                                                              p-substrate




                                                                     Company Confidential   |   ©2009 Micron Technology, Inc.   |   195




                  Embedded PCM (ePCM)


                                                                                                         IMW 2010




    R. Annunziata et al., IEDM 2009



                                                                     Company Confidential   |   ©2009 Micron Technology, Inc.   |   196




                                                                                                                                          98
                  Stand-Alone NVM TAM Expansion
     ($K)
30,000




                                                                                                                                  }
25,000


                                                                                                              Wireless                          Cost,
20,000
                                                                                                                                                Reliability, &
                                                                                                                                                Performance
                                                                                                                       SSD
15,000

                                                                                                     Industrial / CE




                                                                                                                                  }
10,000


                                                                                                                                                Cost, Cost
 5,000                                                          Bulk NAND
                                                                                                                                                & Cost!!!

       0
        2005      2006       2007       2008       2009          2010         2011      2012     2013         2014            2015

Source: iSuppli Application Market Forecast Tool , June 2010



                                                                                               Company Confidential      |    ©2009 Micron Technology, Inc.     |    197




            Phase Change Memory Key Attributes
 •          Non Volatility
 •          Flexibility
                                                        Attributes                   PCM        EEPROM                NOR              NAND              DRAM
             ▶   No Erase, Bit
                                                               Non-Volatile           Yes          Yes                 Yes               Yes                  No

                 alterable, Continuous                           Scaling         sub-2x nm         n.a.               3x nm             2x nm             3x nm


                 Writing                                       Granularity       Small/Byte    Small/Byte             Large             Large          Small/Byte

                                                                  Erase               No           No                  Yes               Yes                  No

 •          Lower power                                         Software             Easy         Easy           Moderate               Hard                  Easy

            consumption than RAM                                 Power               ~Flash      ~Flash           ~Flash               ~Flash                 High

                                                          Write Bandwidth            1- 15+       13-30               0.5-2              10+              100+
 •          Fast Writes                                                              MB/s         KB/s                MB/s              MB/s              MB/s

                                                           Read Latency          50 - 100 ns   200-200 ns        70-100 ns            15 - 50 us        20 - 80 ns
 •          Read bandwidth and
                                                               Endurance              106+       105 -106              105              104-5           Unlimited
            writing throughput
 •          eXecution in Place
 •          Extended endurance

                 PCM provides a new set of features combining
                        properties of NVMs with DRAM
                                                                                               Company Confidential      |    ©2009 Micron Technology, Inc.     |    198




                                                                                                                                                                           99
                  PCM Value Proposition




                                              Company Confidential   |   ©2009 Micron Technology, Inc.   |   199




                PCM – NOR Flash legacy

                             •   Replace NOR in embedded platforms
                                 ▶   PCM has an edge due to density,
                                     scalability, and write speed

                             •   45nm PCM - 1Gb “Bonelli” specifications
                                 ▶ NOR Flash legacy spec + bit alterability
                                 ▶ Chip area: 37.5 mm2
                                 ▶ Power supply range: 1.7V, 2.0V
                                 ▶ Temperature range: -40°C, +85°C

                             •   Measured performance
                                 ▶   Initial access speed: 85ns
                                 ▶   Max read throughput: 266MB/s
                                 ▶   Program throughput: 9MB/s
C.Villa et al., ISSCC 2010

                                              Company Confidential   |   ©2009 Micron Technology, Inc.   |   200




                                                                                                                   100
                                   PCM – LPDDR2
                                                •    Replace (a part of) DRAM
                                                      ▶   PCM has an edge on DRAM due to power
                                                          and scalability, but it is slower

                                                •    58nm PRAM - 1Gb LPDDR2 specifications
                                                      ▶ LPDDR2 interface
                                                      ▶ Chip area: 63.4 mm2
                                                      ▶ Power supply range: 1.8V, 1.2V
                                                      ▶ Temperature range: -25°C, +85°C

                                                •    Measured performance
                                                      ▶   Initial access speed: 76ns
                                                      ▶   IO speed: 800Mbps/pin
        H. Chung et al., ISSCC 2011                   ▶   Program throughput: 6.4MB/s


                                                                      Company Confidential   |   ©2009 Micron Technology, Inc.   |   201




              PCM Application Opportunities
  PCM feature can be exploited by all the memory system, especially the
  ones resulting from the convergence of consumer, computer and
  communication electronics

• Wireless System to store of XiP, semi-static data and files
   ▶ Bit alterability allows direct-write memory


• Solid State Storage Subsystem to store frequently accessed pages
  and elements easily managed when manipulated in place
    ▶    Caching with PCM will improve performance and reliability

• Computing Platforms taking advantage of non-volatility to reduce
  the power
    ▶    PCM offers endurance and write latency that are compelling for a number
         of novel solutions

 S.Eilert et al., “PCM: a new memory enables new memory usage models”, IMW, 2009



                                                                      Company Confidential   |   ©2009 Micron Technology, Inc.   |   202




                                                                                                                                           101
                          MLC Capability
                       “Write Strategies for 2 and 4-bit Multi-Level Phase-Change Memory”
                                            T. Nirschl et al., IEDM 2007




 “A Multi-Level-Cell Bipolar Selected Phase Change Memory”
               F. Bedeschi et al., ISSCC 2008




                                “Drift-Tolerant Multileve Phase Change Memory”
                                        N. Papandreou et al., IMW 2011




                                                      Company Confidential     |    ©2009 Micron Technology, Inc.         |        203




PCMS Memory Cell Cross-Bar Architecture
Ovonic Threshold Switch, OTS, is a two-terminal switch


                                                                                                       Colu
                                                                                                            mn


                                                                                                                        w
                                                                                                                     Ro

                                                                                                                               2
                                                                                                                          al
                                                                                                                     et                    y
                                                                                                Met                 M                  l
                                                                                                    al 1                            Po


                                                                             Si-S
                                                                                 ubs
                                                                                    t rat
                                                                                            e




                                                                             Intel-Numonyx, IEDM 2009

   Chalcogenide materials can be used both for the memory and for
   the selector (OTS) to form stackable cross point PCM (PCMS)
   • True high density cross-bar

   • Possible multilayer vertical stacking
                                                      Company Confidential     |    ©2009 Micron Technology, Inc.         |        204




                                                                                                                                               102
                                Key Learnings
        •     Opportunities exist in the NVM market for new memory concepts
              that can provide a competitive advantage, but...

        •     … disruptive innovation takes a lot of time!

        •     To be successful in the memory market, a new NVM concept must
              be scalable well beyond the actual leading-edge technology node

        •     In the last ten years PCM has demonstrated to be able to follow
              the scaling rules and to have room for entering in the sub-10nm
              domain

        •     Replacing an existing memory technology could be a very hard
              challenge, but the key features of PCM can be effectively exploited
              for improving existing applications

                                                      Company Confidential   |   ©2009 Micron Technology, Inc.   |   205




December 11




                                                                                                                           103
