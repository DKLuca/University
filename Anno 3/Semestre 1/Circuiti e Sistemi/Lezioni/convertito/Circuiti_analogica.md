---
fonte: "Circuiti_analogica.pdf"
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
                      1 lezione




    Books
    ¨   Teoria
        ¤ Microelettronica
           n Autori Richard c. Jaeger travis n.blalock
           n Mc GrawHill
Books
¨   Eserciziari
    ¤ Circuiti analogici
        n Autore F. Zappa
        n Progetto Leonardo
    ¤ Esercizi di progettazione elettronica
        n Autori Andrea Bonfanti
        n Società editrice Esculapio




Program
¨   Introduction
    ¤   Introduction analog design
    ¤   Analog components
¨   Simple stages amplifier
    ¤   Frequency analysis method
¨   Feedback loop
    ¤   Analysis method
¨   Operational amplifier
    ¤   Introduction
    ¤   First stage
        n   Differential Stage
        n   Current mirros
    ¤   Second stage
        n   miller/ahuja compensation
    ¤   Output stages
¨   Non linear circuits
    ¤   Bistable circuits and Oscillators
Introduzione Segnali
Segnale analogico e digitale
¨ Segnale è considerato qualsiasi valore misurabile di
  tensione, corrente o carica che descrive lo stato di un
  sistema o una grandezza fisica
    ¤ Segnale analogico è definito in un continuo di valori di ampiezza
      e di tempo
    ¤ Segnale analogico campionato è definito in un continuo di valori
      di ampiezza e in un insieme discreto di valori di tempo
    ¤ Segnale digitale è definito in un insieme di valori discreti di tempo
      e di ampiezza




Introduzione Progetto e Analisi
Progetto e analisi
¨ Analisi è il processo estrae da uno schema circuitale le sue
  proprietà
    ¤ Il risultato è unico
    ¤ È realizzabile attraverso metodologie che possono essere
      automatizzate
¨   Progetto è il processo che parte dalle proprietà che sono
    definite come specifiche e termina con una soluzione
    circuitale
    ¤ Il risultato non è unico è necessario introdurre delle cifre di merito
      per misurare le prestazioni
    ¤ Il processo è automatizzabile solo parzialmente
Introduzione Organizzazione gerarchica del
progetto
Ogni prodotto o componente è descritto da due
  e schemi:
¨ Schema funzionale: descrizione che contiene le
  informazioni mirate allutilizzo del componente
  (data-sheet, manuale della tecnologia)
¨ Schema di realizzazione: descrizione che contiene
  le informazioni su come è costruito il componente
  basata su descrizioni funzionali dei componenti a
  livello gerarchico inferiore




Esempio
Introduzione
Organizzazione gerarchica del progetto

         Prodotti               Attività             Figure professionali         Aziende

        Product level

                           Product level design         Designer Product




                                                                            company
                                                                             Product
         board level

                          Application level design      Circuit Designer

          IC level

                              IC level design            Chip architect




                                                                                            company
                                                                                            Fab-less
                                                                            Semiconductor
        Circuit level




                                                                              company
                          Transistor level design         IC designer

    Technological level

                          Technologic level design         Tecnologo

       Physical level




Example of design
¨    Discussing example related
     ¤ Analog processing



      Sensors                                               Acquisition system

Input Signals                                                Output Signals

                            Modification
                            • Linear or non linear
 Example of design: LiFi
 ¨   Specification




                   TX                                               RX




 Design of TX
 ¨   High level
                        CK

            n
Digital                         !"#$
input               DAC                LED driving               Light intensity




                                                     At transistor level this connection
 All in µC                                           isn’t necessarily banal
 Or 2 different integrated circuits

          !"#$ = &' () 2+) + (- 2+- + ⋯ + (/ 2+/

                Dove (0 ∈ 0,1
        Design of RX
        ¨   High level                                      CK

                                                                      n
         Signal
                                                                               Logic                Digital
    Dependent on light                                     ADC
                                                                            elaboration             output
        intensity



                                                          All in µC
                                                          Or 2 different integrated circuits


                                                                                     LSB=FS/2n
At transistor level this connection
isn’t necessarily banal

                                                           TCK




        Example of sensor: Photodiode
        ¨   Sensor photodiode

        Proportional to
        The amount of                                                       Large signal model
        Incident light



        Large signal analysis
              IP
                                             EV1 < EV2 < EV3                       Small signal model
                                                I
                                                                  V

                                       EV1                                      1/gm
   EV                    RL     VOUT                                                           CD
                                       EV2                                                              RL
                                       EV3
                                                             RL
                                                    VOUT

                   (A)
                                                    (B)
Example Photodiode
¨   Polarized inverse                                                    Small signal model



            VCC

                                         EV1 < EV2 < EV3
                  IP
                                           VCC    I
    EV
                                                            V
                                                                                         CD
                                  EV1

                                  EV2

         RL            VOUT       EV3


                                               VOUT
                                                                                   RL
                                                           RL




Basic ADC
¨   ADC conversion two types
                  Vin not differential

                                           n               Vin input conversion range
                              ADC                          From a Vin MIN to a Vin MAX with n bit
Vin
                                                                Zin         Input impedance


                   Vin differential                        Each input has a dynamic range
                                                           from a VP,M MIN to a VP.M MAX
     VinP                                  n
    Vin                       ADC                          The difference Vin = Vin P - Vin M
     VinM                                                  is converted From a Vin MIN to a Vin MAX
                                                           with n bit
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
          C    bulk                                                          bulk
                       VnB                   IC=IE a
                                   B                          ro                        InC          P   N+     N+
                                                a /gm
B
                             InB                                                                                N-
                                              Cp IE                                                      Psub
          E
                                                              E
        Small signal
                                                                       Approfondimento
            I
        gm = C                                                               Noise parameters
            VT
            V                                                                I nC = 2qI C
        ro = E
            IC                                                               I nB = 2qI B
               β
        α=                                                                VnB = 4kTRb
              1+ β




    Our design first example
    ¨   Example of RX circuit with bipolar transistor


                                                             VCC                              VCC


                                                                                  VBE
                                       IP               RL          RBE


                                                             VOUT                       Tr1


                                                     Tr1                                      VOUT
                                       VBE                                   IP



                        RBE                                                              RL
    MOS model and description
    ¨   Different types of MOS available from the
        technology
                                          Single well

                  Source Gate Drain               Source Gate Drain
                    P+                P+           N+              N+
                            N-
                                                        Psub

                                           Triple well
                  Source Gate Drain               Source Gate Drain
                   P+                P+            N+              N+
                                                           P-
                            N-

                                                   Psub




    MOS SOA consideration
    ¨   Voltage
                                                 Low voltage Diodes
                                                                                    Triple well
    Single well


          D                      SD                                     D               SD

G                  B    G                    B                 G            B   G                 B



          S                      S                                      S             DS
                                 D



These Diodes in many can have high BD voltage
    MOS Description
    ¨   MOS static model SPICE LEVEL I
 TRIODE

               W⎡                ⎛ V ⎞⎤
I D = µo Cox      ⎢(VGS −VTH ) − ⎜ DS ⎟⎥VDS         (VGS −VTH ) ≥ 0              (VGD −VTH ) ≥ 0
               L ⎢⎣              ⎝ 2 ⎠⎥⎦

 SATURATION
                 W          2
  I D = µo Cox
                 2L
                    (              )(
                    VGS −VTH 1+ λ VDS          ) (V −V ) ≥ 0
                                                         GS       TH
                                                                                 (VGD −VTH ) < 0


 OFF STATE
 ID ≅ 0                                 (VGS −VTH ) < 0                      (VGD −VTH ) < 0

VTH =VTHO + γ    ( 2 Φ +V − 2 Φ )
                        F     SB        F




  MOS Capacitors (AC)
                                                                         Mask L
  ¨   MOS dynamic model SPICE LEVEL I
                                                                             G         C1
                                                         C3
C1 = C3 ≅ ( LD ) Cox Weff = (CGXO) Weff
                                                                                  C2        Mask W
C2 = ( L − 2 LD ) Weff Cox
                                                    C5
 2C5 = CGBO( Leff )                                                     C4
                                                                   B
                                                              Cut Off    Saturation    Linear
                                             C 2+ 2 C5
                    Mask L                                                   CGS
                                            C1+ 2/3 C2
                                            C1+ 1/2 C2
               LD

                                                                             CGD
                                               C1, C 3                                  CGB
Mask W
                                                2 C5
                    L(Leff)
                                                                        VT         vDS+VT   VGS
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
g mbs = −        =− D       = gm                                     = η gm
            ∂VSB   ∂VT ∂VSB      2 2Φ +V            F          SB                 L’impedenza di ingresso
                                                                                  del dispositivo è
               ∂I D   λID                                                         rigorosamente un circuito
g ds = g o =        =
               ∂VSD 1+ λVDS
                                   (
                            ≅ λ I D λ ↓ L↑      )
                                                                                  aperto in Continua!!!!!!!!!!!!!
                                                                                                     D
                                             D C
                                                   db
                                    Cgd                                                Cgd                  Cdb
        D
                                                        InD
                                    gm vgs
                               G                    gmbs vbs        go   B    G         I=IS1             I=IS2    B
G                B                                                                                                     InD
                                                                                                ro
                                                                                        1/gm             1/gmbs

                                    Cgs
        S                                    S Csb                                    Cgs IS1            IS2 Csb

                                                                                                     S
                                       Cgb
                                                                                                Cgb




    Under threshold MOS current

                           v
         W      GS

    iD ≅ I DO e n
         L
    1< n < 3                       Process parameters
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
in2 = ⎢                +            ⎥ Δf             (A2)
      ⎣      3           2 f COX L2 ⎦


Reported at the input

         in2    ⎡ 8k (1 + η )       KF I D    ⎤
en2 =        2
               =⎢             +               ⎥ Δf    (V2)
        gm      ⎣ 3 gm          2 f COX WLK ' ⎦
Matching between two devices
¨   Considering two equal devices of area A on the same
    wafer characterized by the Parameter P (example the
    resistance, capacitor or the threshold voltage ecc..)
                Devices 1                   Devices 2
                                   D



    Area A
¨ P1 and P2 are two random variables
¨ The mean value of P on the wafer depend on process variation

¨ The difference ΔP=P1-P2 is Gaussian distributed with a variance

                                       Experimentally determined
          2       AP2
         σ (ΔP) =     + S 2P D 2
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

ΔP = P1 − P2                             Used for VT
ΔP 200 (P1 − P2 )                        Used for K
   =
 P   P1 + P2
              α         ΔP    β
σ (ΔP) =           σ(      )=                 Standard deviation
              WL         P    WL

                                                                   Mask L
              D                     D

        G          (DID/ID) ID G
                                                    Mask W
  DVT

              S                     S

                                                               M1       M2
              M1                    M2




 Recommended layout
 ¨   Centroid                      D2              D1


                                          B
                           G2                           G1
 Schematico
                                          S




  Layout
    Examples for voltage dividers
    ¨   Voltage references

               Vbg                           M
                                    VA =        V
                                           N + M bg
                      M
                          VA
                     N         Approfondimento

                               Calcolando la varianza della tensione otteniamo
                                                                 Scala con l’area
                                 σ VA       M    σR 1
                                      =
                                 VA     (N + M )N R 2




UNIVERSITY OF UDINE

Department DIEG
Via delle scienze 206
33100 Udine (UD), Italy




                      ANALISI IN FREQUENZA
                      Stefano Saggini
                      Complementi di circuiti e sistemi
Introduction
¨   Calculus of
    ¤ Voltage or current gain
    ¤ Impedance or transimpedance

    ¤ Conductance or transconductance

                            C1           Ck

          Vin(s)   Iin(s)                          Iout(s)   Vout(s)


                              Network




                            Ck+1              Cn




Soluzione del problema
¨ Calcolo della funzione di trasferimento tramite la
  soluzione del circuito lineare ottenuto sostituendo
  alle capacità la loro impedenza ZCk=1/(s Ck)
¨ Tecnica semplificata che cerca di determinare la

  funzione di trasferimento attraverso le proprietà.
                                   NZ


                   Y (s)
                                   ∏ (1+ sτ )      zi
                         = G(0) Ni=1
                   U (s)           P

                                   ∏ (1+ sτ )      pj
                                   j=1
  Determinazione di NP
  ¨      Nel caso ci siano solo capacità nello schema il
         numero di poli è dato dal numero di capacità
         indipendenti (le loro tensioni non sono vincolate da
         generatori di tensioni pilotati e ne da equazioni di
         maglia con altre capacità)
                                                 C1           Ck

                      Vin(s)     Iin(s)                                 Iout(s) Vout(s)


                                                    Network




                                                 Ck+1              Cn




  Determinazione di NZ
  ¨      Se per s è∞ il trasferimento è ≠ da 0 allora
         NZ=NP

                      x      Tensione sulle capacità
                      C1          Ck                                         ⎧ x! = x A + B u
         u                                                y                  ⎨
Vin(s)       Iin(s)                            Iout(s)   Vout(s)             ⎩y = x C + D u

                          Network                                         Y (s)
                                                                                = C(sI − A)−1 B + D
                                                                          X (s)


                      Ck+1                Cn
     Cancellazione poli zeri
     ¨        Caso di non osservabilità delle variabili di stato
         Considerando la funzione Zin                              C
         la capacità C è non osservabile

                              Zin




     ¨        Caso di non raggiungibilità delle variabili di stato
                   R1
                                       Considerando la funzione amplificazione di tensione
                                       Av c’è solo una variabile di stato e se
                              C2                      C2 R1        La variabile è osservabile ma non
         C1
Vin(s)            R2                                    =          raggiungibile
                                    Vout(s)           C1 R2




     Determinazione di alcuni zeri
     ¨        Certe configurazioni circuitali portano sempre degli
              zeri
 Vin(s)       Iin(s)                                                   Iout(s)   Vout(s)

                                                  R
                         Network                         Network                           τ z = RC
                                                  C

                                              R
   Vin(s)       Iin(s)                                                 Iout(s)   Vout(s)


                                                         Network                           τ z = RC
                         Network          C
Capacità interagenti
¨   Le capacità Ci e Cj sono interagenti se la tensione
    VCi influenza la corrente di carica ICj e viceversa.

⎧ x! = x A + B u                   Esempio
⎨
⎩y = x C + D u                     C 1 e C2
                                                            C2
In altre parole i termini          Non sono interagenti


aij ≠ 0        e        a ji ≠ 0


                                                       C1




Proprietà
¨   I poli delle capacità non interagenti possono essere
    calcolate indipendentemente l’una dall’altra.


                                              τ p1 = R1C1
                             R2    C2

                                              τ p2 = R2C2


           Iin(s) R
                    1
                              C1
 Metodo delle costanti di tempo
 ¨   Considerando una rete con capacità indipendenti e
     interagenti
                         NP         NP

                        ∑τ = ∑ RʹC
                               pi         i        i
                         i=1        i=1
                         NP         NP
                                              1
                        ∑ω = ∑ RʹʹC
                               pi
                         i=1        i=1       i        i

  Dove τi (ωi =1/τi) sono le costanti di tempo della rete e Ri’ sono le
  resistenze calcolate ai morsetti di connessione delle capacità Ci con le
  altre capacità scollegate e Ri’’ sono le resistenze calcolate ai morsetti
  di connessione delle capacità Ci con le atre capacità cortocircuitate




Miller Theorem
The impedance Z(s) connected between V1 e V2 can be
  substituted with two impedances:
¨ Z'(s) connected between V1 and ground

¨ Z"(s) connected between V2 and ground

                                                              Z(s)
                   Z (s)
     Z ʹ( s ) =
                 1 − K (s)
                  K (s)Z (s)                      V1         K(s)            V2
     Z ʹʹ( s ) =
                  1 − K (s)
                 V (s)
     K (s) = 2
                 V1 ( s )                         V1 Z’(s)   K(s)    Z’’(s   V2
                                                                     )
UNIVERSITY OF UDINE

Department DIEG
Via delle scienze 206
33100 Udine (UD), Italy




                      FEEDBACK SYSTEM 1
                      Associate professor Stefano Saggini
                      Lezione di complementi di elettronica




    Sommario
    ¨   Introduzione ai sistemi mutistadio
        ¤ Rappresentazione come doppi bipoli

    ¨   Introduzione ai circuiti retroazionati
        ¤ Calcolo del guadagno d’anello

        ¤ Calcolo del guadagno ideale
        ¤ Calcolo del guadagno diretto

        ¤ Calcolo del guadagno reale
     Amplificatore multistadio
     ¨   Sistema multistadio
         ¤ Il Guadagno tra vout e vs dipende da I valori di RL e Rg




                                                      vout



Rg                                                                         RL
vs




     Descrizione dell’amplificatore
     ¨   Circuito lineare per la descrizione dell’amplificatore
                                     Questa rappresentazione è più adatta per il
                                     calcolo dell’effettivo guadagno:
                                      Doppio bipolo tripolare.
                                        vin

                                              iin                   Rout
     Questa rappresentazione non è
     sufficiente                              Rin                   Av vin
                                                                    oppure
                                                                     R iin
                α
                                        vin

                                                iin
                                                                   Rout
                                              Rin                   G vin
                                                                     AI Iin
     Amplificatore differenziale
     ¨   Il segnale di ingresso differenziale in tensione

                                                             v DIF = v+ − v−
                V+
                          +              Vout                        v+ + v−
                                                             vCM =
                     V-                                                 2
                          -

                                                                  AD
                                                           CMRR =
                              Guadagno indesiderato               ACM

     vOUT = AD v DIF + ACM vCM




     Rappresentazione matematica
     ¨   Rappresentazione matematica

                                                            ⎡ v ⎤     ⎡ i ⎤
           i1                              i2               ⎢    ⎥ = R⎢ 1 ⎥
v1
                          R                           v2
                                                               1
                                                            ⎢ v ⎥     ⎢ i ⎥
                                                            ⎣ 2 ⎦     ⎣ 2 ⎦


               ⎡ r r ⎤ ⎡ R                                 ≅0 ⎤
           R = ⎢ 11 12 ⎥ = ⎢ in                                  ⎥
               ⎢ r r ⎥ ⎢ R                                 Rout ⎥⎦
               ⎣ 21 22 ⎦ ⎣
     Rappresentazione matematica
     ¨   Rappresentazione matematica

                                             ⎡ i ⎤     ⎡ v ⎤
                                             ⎢    ⎥ = G⎢ 1 ⎥
v1
          i1
                     G          i2
                                      v2
                                                1
                                             ⎢ i ⎥     ⎢ v ⎥
                                             ⎣ 2 ⎦     ⎣ 2 ⎦


                                  ⎡ 1                ⎤
                   ⎡ g                        ≅0
                          g12 ⎤ ⎢     Rin            ⎥
               G = ⎢ 11         ⎥=⎢                  ⎥
                   ⎢ g    g 22 ⎥⎦ ⎢ G        1       ⎥
                   ⎣ 21           ⎢⎣           Rout ⎥⎦




     Rappresentazione matematica
     ¨   Rappresentazione matematica

                                            ⎡ i ⎤       ⎡ v ⎤
                                            ⎢    ⎥ = H ʹ⎢ 1 ⎥
v1
          i1
                     Hʹ         i2
                                      v2
                                               1
                                            ⎢ v ⎥       ⎢ i ⎥
                                            ⎣ 2 ⎦       ⎣ 2 ⎦



                     ⎡ hʹ hʹ ⎤ ⎡ 1          ≅0 ⎥
                                                  ⎤
                                 ⎢
               H ʹ = ⎢ 11 12 ⎥ = ⎢ Rin
                                                  ⎥
                     ⎢ hʹ hʹ ⎥
                     ⎣ 21 22 ⎦ ⎢⎣ AV        Rout ⎥⎦
     Rappresentazione matematica
     ¨   Rappresentazione matematica

                                                  ⎡ v ⎤        ⎡ i ⎤
                                                  ⎢    ⎥ = H ʹʹ⎢ 1 ⎥
v1
           i1
                     H ʹʹ            i2
                                          v2
                                                     1
                                                  ⎢ i ⎥        ⎢ v ⎥
                                                  ⎣ 2 ⎦        ⎣ 2 ⎦


               ⎡ hʹʹ hʹʹ ⎤ ⎡ Rin               ≅0      ⎤
               ⎢  11  12 ⎥ ⎢                           ⎥
            ʹʹ
           H =            =
               ⎢ hʹʹ hʹʹ ⎥ ⎢ AI                1       ⎥
               ⎣ 21 22 ⎦ ⎢⎣                      Rout ⎥⎦




     Circuiti retroazionati
     ¨   La retroazione:
         ¤ Stabilizza il guadagno rispetto alle caratteristiche
           parametriche dei componenti perché dipende dai
           compenti passivi
           n Migliora la linearità
 Teoria dei circuiti reazionati
Differenze tra lo schema di reazione ideale e il circuito con retroazione:
¨ Ogni blocco dello schema a blocchi ha una direzione e un trasferimento che
   non dipende dai blocchi a cui è collegato, lo schema elettrico non è sempre
   direzionale e il trasferimento dipende dagli elementi a cui è connesso
¨ I segnali dello schema elettrico possono essere di tensione o di corrente

¨ Non c’è una equivalenza netta tra lo schema a blocchi e lo schema circuitale
   c’ è solo una similitudine, infatti il trasferimento complessivo non è ricavabile in
   modo immediato dal trasferimento degli schemi a blocchi.




                  α                   VI(t)                                       VO(t)
                                                             α
I(t)                      O(t)
                                           II(t)                              IO(t)
                                                              β
                  β




 Individuazione delle reazioni in uno
 schema
Per l’analisi della reazione è fondamentale individuare il
  blocco α e β:
¨ Per l’individuazione della direzione dell’anello è
  necessario seguire la direzione dei componenti direzionali
  di cui è composto lo schema

              C                        D

                                                             +
       B                    G
                                                              -
              E                        S
         Reazione serie e parallelo
     ¨     The type of feedback (Voltage or current) depend on the
           connection          Serr
                             +      α
                                                Sin                                        Sout
                                                                             β
                                                                                  Input current connected in parallel, the error is a current.
Input parallel the error is the current out is the voltage
                                                                                  Output in series the output is the current.


   iIN                    α                    vout                                      iIN                         α                   iOUT

                           β                                                                                         β
                                                                                 Input in series the error is the voltage, out in parallel the voltage is
Input in series the error is the voltage, out in series the current is the
                                                                                 the output.
output.


                           α               iOUT                                                                   α                   vout
   v IN                                                                                  v IN
                           β                                                                                      β




         Retroazione parallelo parallelo
         ¨    Accesso ad un nodo della circuito retroazionato
              l’uscita è su un nodo della retrazione
             Effetto della
             retroazione negativa                                                                                     Transresistance



                                 is                GS
                                                                       Gα                                  GL             vL


             Intervento
             dell’ingresso

                                                                      Gβ
      Retroazione parallelo parallelo
      ¨   Calcolo del risultato
                    ⎡ G                  ⎡ α                                                        ⎤
                                  0 ⎤ ⎢ g 11     β
                                             + g 11 + GS                                  α
                                                                                        g 12     β
                                                                                             + g 12 ⎥
     Gγ = Gα + Gβ + ⎢ S               ⎥=
                    ⎢ 0
                    ⎣             GL ⎥⎦ ⎢ g α21 + g 21
                                                    β
                                                                                  g 22 + g 22 + GL ⎥⎦
                                                                                    α      β
                                         ⎣
                                                                           ⎡ i ⎤        ⎡ v ⎤
                                                                           ⎢  S  ⎥ = Gγ ⎢ 1 ⎥
                                                                           ⎢⎣ 0 ⎥⎦      ⎢ v ⎥
                                                                                        ⎣ 2 ⎦
is          v1            Gγ                                     v2

                                                                             ⎡ i ⎤ ⎡ v ⎤
                                                                           G ⎢ S ⎥=⎢ 1 ⎥
                                                                            −1
                                                                            γ
                                                                             ⎢⎣ 0 ⎥⎦ ⎢⎣ v2 ⎥⎦




      Retroazione parallelo parallelo
      ¨   Soluzione
                          ⎡ α      β
                    1 ⎢ g 22 + g 22 + GL         (  α
                                                − g 12     β
                                                       + g 12   ) ⎤⎥⎡⎢ i ⎤⎥ = ⎡⎢ v ⎤⎥
                                                                       S         1
                          ⎢                                     ⎥
                             (
                 det(Gγ ) ⎢ − g α + g β  )       α
                                               g 11     β
                                                    + g 11 + GS ⎥⎣⎢ 0 ⎥⎦ ⎢⎣ v2 ⎥⎦
                          ⎣     21    21
                                                                ⎦


      ¨   Analisi del primo trasferimento                                     Termine dominante RD
                   v − ( g + g ) −g
                             α      β           α         β
                     2       21     21−g        21        21                     Termine parassita RP
                    =           =   +
                    iS      detGγ            detGγ   detGγ
Analisi del primo termine RD
¨      Analisi del termine RD

                                                                           Guadagno di andata
                                                   −g α21
         RD =
                (g + g + G )(g + g + G ) − (g + g )(g + g )
                        α
                        11
                              β
                              11    S
                                             α
                                             22
                                                  β
                                                  22        L
                                                                      α
                                                                      12
                                                                              β
                                                                              12
                                                                                          α
                                                                                          21
                                                                                               β
                                                                                               21




                                                                                                                           Gideale
                                                       −G                                                    1                  1
lim RD = lim                                                                                        =                      ≅
G→−∞         G→−∞
                    (     α
                        g 11     β
                             + g 11     )(
                                    + GS g α22 + g 22
                                                   β           α
                                                                ) (
                                                      + GL − g 12     β
                                                                  + g 12       β
                                                                         G + g 21  )(           ) (        α
                                                                                                         g 12     β
                                                                                                              + g 12   )         β
                                                                                                                               g 12



                                  ⎡ 1                          ⎤
                                  ⎢                    ≅0      ⎥
                                      Rin
                             Gα = ⎢                            ⎥
                                  ⎢ G                  1       ⎥
                                  ⎢⎣                     Rout ⎥⎦




Gideale nel circuito

                                                                                                        v2


        is                     GS                        v1 = 0
                                                         i1 = 0

                                                                       v2 non vincolata
                                                                       i2 non vincolata




                                                                                                                                      v2
                                                                                                        Gideale =
                                                                                                                                      iS
Dimostrazione

                                                                                                               v2


    iS                     GS                             v1 = 0
                                                          i1 = 0

                                                                         v2 non vincolata
                                                                         i2 non vincolata



                                                                                                                                  is
                                                                                                                     v2 =          β
                                                                                                                                 g 12




Analisi del primo termine RD
                          1                                             1
         RD =
                (g + g ) (g + g ) − (g + g + G )(g + g + G )
                     α
                     12
                                β
                                12
                                      α
                                      21
                                                β
                                                21
                                                              α
                                                              11
                                                                        β
                                                                        11            S
                                                                                                α
                                                                                                22
                                                                                                          β
                                                                                                          22   L

                            g             (g + g ) g
                                           α
                                           21
                                                                                 α
                                                                                 12
                                                                                           β
                                                                                           12
                                                                                                     α
                                                                                                     21




                                                              1                                                                   1
 RD = Gideale                                                                                                       = Gideale
                1+
                     g    β
                          21   (g + g ) − (g + g + G )(g + g + G )
                                 α
                                 12
                                       β
                                       12
                                                         α
                                                         11
                                                                   β
                                                                   11        S
                                                                                           α
                                                                                           22
                                                                                                      β
                                                                                                      22       L
                                                                                                                                    −1
                                                                                                                                1− Gloop

                                           (g + g ) g    α
                                                         12
                                                                   β
                                                                   12
                                                                             α
                                                                             21




 Gloop =
                                                    α
                                                     (
                                                − g 12     β
                                                       + g 12 g α21          )
              β
            g 21   α
                 g 12(    β
                      + g 12     α
                             − g 11    ) (
                                        β
                                    + g 11 + GS g α22 + g 22
                                                          β
                                                             + GL                         )(                             )
Gloop nel circuito
                                                                            α                             α
                                                                           g11                          g 22
                    GS                                                                                                                  GL




                                                                                Gβ

         Gloop =
                                                                      (
                                                                      α
                                                                  − g 12     β
                                                                         + g 12 g α21             )
                           β
                         g 21   α
                                 (
                              g 12     β
                                   + g 12     α
                                          − g 11     β
                                                 + g 11      ) (
                                                        + GS g α22 + g 22
                                                                       β
                                                                          + GL                         )(                              )




Dimostrazione
                                                                                           v1
                                                              Gloop = −g α21
                                                                                          itest
                                         ⎡ 0 ⎤ ⎡ gα + g β + G                                           α
                                                                                                      g 12     β
                                                                                                           + g 12
                                                                                                                     ⎤⎡      ⎤
                                         ⎢        ⎥ = ⎢ 11 11   S                                                    ⎥⎢ v1 ⎥
                                            i
                                         ⎢⎣ test ⎥⎦   ⎢      β
                                                           g 21                                   g α22 + g 22
                                                                                                            β
                                                                                                               + GL ⎥⎦⎢⎣ v2 ⎥⎦
                                                      ⎣

                                                                   ⎡ α
                                         1
                                                                              β
                                                                   ⎢ g 22 + g 22 + GL                               ( α
                                                                                                                  − g 12     β
                                                                                                                         + g 12   ) ⎤⎥⎡⎢ 0 ⎤⎥ = ⎡⎢ v ⎤⎥
                                                                                                                                                   1
                                                                β ⎢                                                           ⎥
  (     α
      g 11     β
           + g 11 + GS   )(   g α22 + g 22
                                        β
                                                    )
                                                    β
                                           + GL − g 21   α
                                                       g 12   (
                                                            + g 12 ⎢⎣
                                                                               β
                                                                           −g 21 )                                g + g + GS ⎥⎦⎢⎣ itest ⎥⎦ ⎢⎣ v2 ⎥⎦
                                                                                                                   α
                                                                                                                   11
                                                                                                                             β
                                                                                                                             11




                                  v1 =
                                                                          α
                                                                           (
                                                                      − g 12     β
                                                                             + g 12 itest )
                                             (g + g + G )(g + g + G ) − g (g + g )
                                               α
                                               11
                                                        β
                                                        11        S
                                                                           α
                                                                           22
                                                                                     β
                                                                                     22       L
                                                                                                       β
                                                                                                       21
                                                                                                             α
                                                                                                             12
                                                                                                                        β
                                                                                                                        12




                Gloop =
                                                                      (
                                                                      α
                                                                  − g 12     β
                                                                         + g 12 g α21     )
                                g   β
                                    21   (g + g ) − (g + g + G )(g + g + G )
                                              α
                                              12
                                                        β
                                                        12
                                                                          α
                                                                          11
                                                                                     β
                                                                                     11       S
                                                                                                        α
                                                                                                        22
                                                                                                                  β
                                                                                                                  22          L
 Analisi del secondo termine RP
 ¨     Analisi del termine RP
                                                                       β
                                                                                                Guadagno parassita
                                                                    −g 21
         RP =
                 (g + g + G )(g + g + G ) − (g + g )(g + g )
                      α
                      11
                                 β
                                 11         S
                                                      α
                                                      22
                                                                β
                                                                22          L
                                                                                           α
                                                                                           12
                                                                                                     β
                                                                                                     12
                                                                                                                α
                                                                                                                21
                                                                                                                           β
                                                                                                                           21




                                                                              β
                                                                            g 21
        RP =
                (g + g ) g + (g + g ) g (g + g + G )(g + g + G )
                     α
                     12
                                β
                                12
                                       α
                                       21
                                                      α
                                                      12
                                                               β
                                                               12
                                                                          β
                                                                          21
                                                                             −
                                                                                      α
                                                                                      11
                                                                                                β
                                                                                                11         S
                                                                                                                     α
                                                                                                                     22
                                                                                                                                   β
                                                                                                                                   22    L




                                              β
                                            g 21                                                                                                  1
RP =
       ( g + g ) g − ( g + g + G ) ( g + g + G ) 1+
         α
         12
                β
                12
                           β
                           21
                                      α
                                      11
                                                 β
                                                 11        S
                                                                     α
                                                                     22
                                                                                 β
                                                                                 22         L                           (g + g ) g           α
                                                                                                                                             12
                                                                                                                                                      β
                                                                                                                                                      12
                                                                                                                                                           α
                                                                                                                                                           21

                                                                                                          (g + g ) g − (g + g + G )(g + g + G )
                                                                                                               α
                                                                                                               12
                                                                                                                          β
                                                                                                                          12
                                                                                                                                    β
                                                                                                                                    21
                                                                                                                                             α
                                                                                                                                             11
                                                                                                                                                      β
                                                                                                                                                      11   S
                                                                                                                                                                α
                                                                                                                                                                22
                                                                                                                                                                     β
                                                                                                                                                                     22   L




 Analisi del secondo termine
 ¨     Analisi del secondo termine
                                                     Guadagno diretto
                                                                       β
                                                                     g 21                                     1
              RP =
                     g    β
                          21   (g + g ) − (g + g + G )(
                                 α
                                 12
                                                β
                                                12
                                                               α
                                                               11
                                                                          β
                                                                          11           S
                                                                                                 α
                                                                                                g + g + GL
                                                                                                 22
                                                                                                           1− Gβ
                                                                                                                loop
                                                                                                               22              )

                                                                                     β
                                                                                   g 21
               Gdiretto =          β
                                 g 21  (α
                                      g 12     β
                                           + g 12     α
                                                  − g 11     β
                                                         + g 11) (
                                                                + GS g α22 + g 22
                                                                               β
                                                                                  + GL                )(                                 )

                                                                             1
                                           RP = Gdiretto
                                                                          1− Gloop
   Gdiretto nel circuito

             v2                                                                                                          v2
Gdiretto =                                                                  α                           α
             iS                                                         g   11
                                                                                                    g   22
                                               GS
                      iS                                                                                                                    GL




                                                                         Gβ




   Dimostrazione
                                                                                           v2
                                                                      Gdiretto =
                                                                                           iS
                                              ⎡ i ⎤ ⎡ gα + g β + G                                    α
                                                                                                    g 12     β
                                                                                                         + g 12
                                                                                                               ⎤⎡      ⎤
                                              ⎢ S ⎥ = ⎢ 11 11     S                                            ⎥⎢ v1 ⎥
                                              ⎢⎣ 0 ⎥⎦ ⎢      β
                                                           g 21                             g α22 + g 22
                                                                                                      β
                                                                                                         + GL ⎥⎦⎢⎣ v2 ⎥⎦
                                                      ⎣
                                                                              ⎡ α
                                                1
                                                                                         β
                                                                              ⎢ g 22 + g 22 + GL                        (  α
                                                                                                                       − g 12     β
                                                                                                                              + g 12   ) ⎤⎥⎡⎢ i ⎤⎥ = ⎡⎢ v ⎤⎥
                                                                                                                                              S         1
                                                                           β ⎢                                                     ⎥
             (     α
                 g 11     β
                      + g 11 + GS   )(   g α22 + g 22
                                                   β
                                                         )     β
                                                      + GL − g 21 ( α
                                                                  g 12 + g 12 ⎢⎣  )       β
                                                                                      −g 21                            g + g + GS ⎥⎦⎢⎣ 0 ⎥⎦ ⎢⎣ v2 ⎥⎦
                                                                                                                        α
                                                                                                                        11
                                                                                                                              β
                                                                                                                              11



                                                                                    β
                                                                                 −g 21iS
                                            v2 =
                                                   (g + g + G )(g + g + G ) − g (g + g )
                                                    α
                                                    11
                                                             β
                                                             11   S
                                                                         α
                                                                         22
                                                                                      β
                                                                                      22        L
                                                                                                             β
                                                                                                             21
                                                                                                                  α
                                                                                                                  12
                                                                                                                         β
                                                                                                                         12



                                                                β
                      v2                                      g 21
                         = Gdiretto = β α
                      is                           β
                                                    (
                                     g 21 g 12 + g 12     α
                                                      − g 11     β
                                                             + g 11   ) (
                                                                    + GS g α22 + g 22
                                                                                   β
                                                                                      + GL                   )(                        )
   Analisi del secondo trasferimento
   ¨     Impedenza di ingresso
                              ⎡ α      β
                        1 ⎢ g 22 + g 22 + GL              ( α
                                                        − g 12     β
                                                               + g 12   ) ⎤⎥⎡⎢ i ⎤⎥ = ⎡⎢ v ⎤⎥
                                                                                  S            1
                              ⎢                                          ⎥
                                       (
                     det(Gγ ) ⎢ − g α + g β        )      α
                                                        g 11     β
                                                             + g 11 + GS ⎥⎢⎣ 0 ⎥⎦ ⎢⎣ v2 ⎥⎦
                              ⎣     21    21
                                                                         ⎦

           v1
              =
                (
                g α22 + g 22
                          β
                             + GL)= α
                                                          g α22 + g 22
                                                                    β
                                                                       + GL
           iS         detGγ                ( β         α
                                                         )(    β
                                    g 11 + g 11 + GS g 22 + g 22 + GL − g 12α
                                                                               ) (β
                                                                              + g 12 g α21 + g 21
                                                                                               β
                                                                                                    )(              )
                          g α22 + g 22
                                    β
                                       + GL                                                               1
RIN =
        ( g + g + G ) ( g + g + G ) − ( g + g ) g 1−
          α
          11
               β
               11     S
                           α
                           22
                                  β
                                  22           L
                                                   α
                                                   12
                                                          β
                                                          12
                                                                 β
                                                                 21                                (g + g ) g
                                                                                                     α
                                                                                                     12
                                                                                                               β
                                                                                                               12
                                                                                                                    α
                                                                                                                    21

                                                                        (g + g + G )(g + g + G ) − (g + g ) g
                                                                          α
                                                                          11
                                                                                      β
                                                                                      11   S
                                                                                                    α
                                                                                                    22
                                                                                                              β
                                                                                                              22    L
                                                                                                                         α
                                                                                                                         12
                                                                                                                              β
                                                                                                                              12
                                                                                                                                   β
                                                                                                                                   21


         Resistenza anello aperto
                                                                                1
                                                               RIN = RINOL
                                                                             1− Gloop




   Ranello aperto nel circuito
       v                               v1
RINOL = 1
       iS                                                  α
                                                          g11                α
                                                                           g 22
                                     GS
                is                                                                                                  GL




                                                              Gβ
 Dimostrazione
                                                               v
                                                          RIN = 1
                                                               iS
                            ⎡ i ⎤ ⎡ gα + g β + G                               α
                                                                             g 12     β
                                                                                  + g 12
                                                                                            ⎤⎡      ⎤
                            ⎢ S ⎥ = ⎢ 11 11     S                                           ⎥⎢ v1 ⎥
                            ⎢⎣ 0 ⎥⎦ ⎢      β
                                         g 21                            g α22 + g 22
                                                                                   β
                                                                                      + GL ⎥⎦⎢⎣ v2 ⎥⎦
                                    ⎣
                                                          ⎡ α
                             1
                                                                     β
                                                          ⎢ g 22 + g 22 + GL                        (
                                                                                                    α
                                                                                                − g 12     β
                                                                                                       + g 12   ) ⎤⎥⎡⎢ i ⎤⎥ = ⎡⎢ v ⎤⎥
                                                                                                                       S         1
                                                       β ⎢                                                       ⎥
     (g + g + G )(
      α
      11
           β
           11   S
                     g α22 + g 22
                               β
                                        )  β
                                  + GL − g 21   α
                                                 (
                                              g 12 + g 12 ⎢⎣     )    β
                                                                  −g 21                          α
                                                                                               g 11     β
                                                                                                    + g 11 + GS ⎥⎦⎣⎢ 0 ⎥⎦ ⎢⎣ v2 ⎥⎦



                     v1 =
                                       (g + g + G )i α
                                                     22
                                                            β
                                                            22       L   S


                            (g + g + G )(g + g + G ) − g (g + g )
                             α
                             11
                                   β
                                   11       S
                                                     α
                                                     22
                                                            β
                                                            22       L
                                                                                 β
                                                                                 21
                                                                                      α
                                                                                      12
                                                                                               β
                                                                                               12




       v1
          = RINOL = α
                                     g α22 + g 22
                                               β
                                                 (+ GL                       )
       is             (      β         α      β
                                                )(        β
                    g 11 + g 11 + GS g 22 + g 22 + GL − g 21   α
                                                             g 12     β
                                                                  + g 12     )             (            )




Trasferimento reale
Il trasferimento reale si può scomporre nei seguenti contributi
    di calcolo più immediato


               Gideale   Gdiretto
     Greale =       −1
                       +
              1 − Gloop 1 − Gloop
     Greale: Guadagno reale del trasferimento reazionato
     Gloop:Guadagno d’anello del circuito retroazionato
     Gideale: Guadagno reale del trasferimento se il G è infinito
     Gdiretto: Guadagno reale del trasferimento se il G è nullo
Calcolo del guadagno d’anello
¨   Il guadagno d’anello è il meccanismo che permette di ottenere il guadagno ideale
¨   Il calcolo del guadagno d’anello si ottiene spezzando l’anello in un punto “comodo” e
    calcolando il trasferimento sul circuito ottenuto ai capi del punto di rottura nella
    direzione dell’anello
¨   Si sopprimono gli ingressi (si aprono i generatori di corrente e si cortocircuitano quelli di
    tensione)
¨   Il calcolo si può anche realizzare in simulazione
¨   Questo calcolo è semplice da fare perché lo schema è direzionale



                                     R                  VAC=1           RC >> τ dello schema
                                             VC
      Vin                    Vin      C                  VC               Vout




                              T(s)




 Calcolo del guadagno d’anello

Il punto di rottura più comodo è l’ingresso o l’uscita di
   una generatore comandato ideale altrimenti è
   necessario ricostruire le impedenze modificate dalla
   rottura

                                                          Gloop Itest         Itest
                           α                                            α




                             β                                           β
Calcolo del guadagno ideale
¨   Il guadagno ideale è un trasferimento che si ottiene
    facendo tendere a zero la variabile di ingresso della del
    circuito con retroazione, ovvero l’ingresso del blocco α sia
    essa corrente che tensione




Calcolo del guadagno diretto
Questo calcolo si ottiene annullando il guadagno del blocco α e
  calcolando il trasferimento tra ingresso ed uscita:
¨ Questo calcolo può essere realizzato in simulazione inserendo il

  blocco senza generatore di tensione AC utilizzato per il calcolo del
  guadagno d’anello connesso in modo da non perturbare il
  trasferimento diretto del segnale. Il generatore AC necessario per la
  valutazione di questo trasferimento va inserito all’ingresso del
  circuito.
Singolarità del guadagno reale
¨ I poli del guadagno reale sono le soluzioni
  dell’equazione:      1 − Gloop = 0
¨ Tutti i poli del guadagno ideale sono degli zeri del
  guadagno d’anello (non vale il viceversa)
¨ Il guadagno d’anello e il guadagno diretto hanno gli

  stessi poli




 Rappresentazione del guadagno reale

 ¨   Rappresentazione del guadagno reale in
     frequenza:
                                       Greale ≅ Gideale
                − Gloop Gideale        Gloop >> 1
     Greale ≅
                  1 − Gloop
                                      Greale ≅ −GidealeGloop
     − Gloop Gideale
                                       Gloop << 1
                       Gideale
                                  Il modulo del guadagno reale si
       Greale                     traccia tracciando la minima curva tra
                                  il guadagno ideale e il prodotto del
                                  guadagno d’anello per il guadagno
                                  ideale
UNIVERSITY OF UDINE

Department DIEG
Via delle scienze 206
33100 Udine (UD), Italy




                         FEEDBACK SYSTEM 2
                         Associate professor Stefano Saggini
                         Lezione di complementi di elettronica




     Retroazione serie serie
     ¨    Accesso ad un ramo della circuito retroazionato
          l’uscita è su un ramo della retrazione
         Effetto della
         retroazione negativa
                                                                 Transconductance
Intervento
dell’ingresso

                         RS
                                          Rα
                                                                 RL
                 vS
                                                                 iL Segnale di uscita
                                           Rβ
Retroazione serie serie
¨   Calcolo del risultato
               ⎡ R                   ⎡ α                                                     ⎤
                              0 ⎤ ⎢ r11     β
                                         + r11 + RS                            α
                                                                              r12    β
                                                                                  + r12      ⎥
Rγ = Rα + Rβ + ⎢ S                ⎥=
               ⎢ 0
               ⎣              RL ⎥⎦ ⎢ r α21 + r 21
                                                β
                                                                           r 22 + r 22 + RL ⎥⎦
                                                                            α       β
                                     ⎣

                                                                  ⎡ v ⎤      ⎡ i ⎤
                                                                  ⎢ S ⎥ = Rγ ⎢ 1 ⎥
         i1                                  i2                   ⎢⎣ 0 ⎥⎦    ⎢ i ⎥
                                                                             ⎣ 2 ⎦
    vs
                          Rγ
                                                                     ⎡ v ⎤ ⎡ i ⎤
                                                                   R ⎢ S ⎥=⎢ 1 ⎥
                                                                     −1
                                                                     γ
                                                                     ⎢⎣ 0 ⎥⎦ ⎢⎣ i2 ⎥⎦




Retroazione serie serie
¨   Soluzione
                       ⎡ α      β
                 1 ⎢ r 22 + r 22 + RL    ( α
                                        − r12    β
                                              + r12   ) ⎤⎥⎡⎢ v ⎤⎥ = ⎡⎢ i ⎤⎥
                                                             S         1
                       ⎢                               ⎥
                          (        )
              det(Rγ ) ⎢ − r α + r β     α
                                        r11    β
                                            + r11 + rS ⎥⎣⎢ 0 ⎦⎥ ⎢⎣ i2 ⎥⎦
                       ⎣     21    21
                                                       ⎦


¨   Analisi del primo trasferimento                                  Termine dominante GD
                                                                       Termine parassita GP



                  =
                     α
                      (      β
                              )
               i2 − r 21 + r 21
                                =
                                   −r α21
                                          +
                                               β
                                            −r 21
               vS   det Rγ        det Rγ det Rγ
      Trasferimento
                                                             Termine
      ¨    Trasferimento                                     dominante GD
                                                                                                                         Termine parassita GP


                                            =
                                                   (    α
                                         i2 − r 21 + r 21
                                                          =
                                                                 β
                                                             −r α21
                                                                    +
                                                                     )   β
                                                                      −r 21
                                         vS   det Rγ        det Rγ det Rγ

                                                                                                                                               ⎡ R    ≅0 ⎤
                                                   G           Gdiretto
                                          Greale = ideale   +                                                                             Rα = ⎢ in         ⎥
                                                        −1
                                                  1 − Gloop   1 − Gloop                                                                        ⎢ R    Rout ⎥⎦
                                                                                                                                               ⎣



                                                                 −R                                                1                 1
Gideale = lim GD = lim                                                                                     =                    ≅
        R→−∞           R→−∞
                              (    α
                                  r11    β
                                      + r11       )(
                                            + RS r α22 + r 22
                                                           β          α
                                                              + RL − r12  ) (
                                                                            β
                                                                         + r12       β
                                                                               R + r 21      )(           ) (    α
                                                                                                                r12    β
                                                                                                                    + r12   )        β
                                                                                                                                    r12


                                                  1                                                       1
  GD = Gideale                                                                              = Gideale
                 1+
                        β
                         (
                      r 21  α
                           r12    β
                               + r12   ) (
                                        α
                                     − r11    β
                                           + r11      )(
                                                 + RS r α22 + r 22
                                                                β
                                                                   + RL                 )                   −1
                                                                                                        1− Gloop

                                          ( rα
                                              +
                                             12
                                                r ) r  β
                                                       12
                                                            α
                                                            21




      Gideale nel circuito
                                                                                                                    i2

                                                                                                                                                    i
                                                                         v1 = 0                                                           Gideale = 2
            RS
                                                                         i1 = 0                                                                    vS
                                                                                  v2 non vincolata
                                                                                  i2 non vincolata

                                                                                                                                          RL
          vs

                                                             β
                                                            r11                    β
                                                                                  r12 i2
Gloop nel circuito
                                                                                        r α22

                                                            r α21i1
                                           α
                                          r11
       RS




                                                                  Rβ

                      Gloop =
                                                              (α
                                                            − r12    β
                                                                  + r12 r α21   )
                                 r   β
                                     21   (r + r ) − (r + r + R ) (r + r + R )
                                            α
                                            12
                                                     β
                                                     12
                                                               α
                                                               11
                                                                       β
                                                                       11           S
                                                                                          α
                                                                                          22
                                                                                                β
                                                                                                22   L




Analisi del secondo termine
¨   Analisi del secondo termine
                                     Guadagno diretto
                                                       β
                                                     r 21                         1
      GP =
             r   β
                 21   (r + r ) − (r + r + R ) (
                       α
                       12
                                β
                                12
                                                α
                                                11
                                                      β
                                                      11      S
                                                                      α
                                                                    r + r + RL
                                                                      22
                                                                                β
                                                                               1−
                                                                                22
                                                                                  G loop    )
                                                              β
                                                            r 21
        Gdiretto =        β
                        r 21( α
                             r12    β
                                 + r12    α
                                       − r11    ) (
                                                β
                                             + r11 + RS r α22 + r 22
                                                                  β
                                                                     + RL  )(                    )

                                                               1
                                 GP = Gdiretto
                                                            1− Gloop
Gdiretto nel circuito
                                                                                                 i2
                                                                                                                                             i
                                                                                                                                  Gdiretto = 2
                                                                                                                                            vS
                                                        r11α             r22α
             RS


                                                                                                                             RL
        vs

                                                           Rβ




Analisi del secondo trasferimento
¨   Impedenza di ingresso
                                ⎡ α      β
                          1 ⎢ r 22 + r 22 + RL             (
                                                           α
                                                        − r12    β
                                                              + r12         ) ⎤⎥⎡⎢ v ⎤⎥ = ⎡⎢ i ⎤⎥
                                                                                      S           1
                                ⎢                                  ⎥
                                          (
                       det(Rγ ) ⎢ − r α + r β       )   r + r + RS ⎥⎢⎣ 0 ⎥⎦ ⎢⎣ i2 ⎥⎦
                                                         α          β
                                ⎣     21    21           11
                                                                   ⎦11




             i1
                =
                   (
                  r α22 + r 22
                            β
                               + RL   )
                                    = α
                                                          r α22 + r 22
                                                                    β
                                                                       + RL
             vS         det Rγ               β
                                              (       α
                                                           )(  β
                                      r11 + r11 + RS r 22 + r 22 + RL − r12 α    β
                                                                              + r12   ) (
                                                                                    r α21 + r 21
                                                                                              β
                                                                                                           )(                )
                              r α22 + r 22
                                        β
                                           + RL                                                                 1
GIN =
        (    11   11     )(
            r + r + RS r α22 + r 22
             α    β              β          α
                                    + RL − r12    ) (
                                                  β
                                               + r12   β
                                                     r 21       )        1−
                                                                                                      (    α
                                                                                                          r12    β
                                                                                                              + r12 r α21)
                                                                                (r + r + R ) (r + r + R ) − (r + r ) r
                                                                                 α
                                                                                 11
                                                                                      β
                                                                                      11     S
                                                                                                      α
                                                                                                      22
                                                                                                                    β
                                                                                                                    22       L
                                                                                                                                  α
                                                                                                                                  12
                                                                                                                                       β
                                                                                                                                       12
                                                                                                                                            β
                                                                                                                                            21



  Conduttanza anello aperto
                                                                                     1
                                                               GIN = GINOL
                                                                                  1− Gloop
  Ganello aperto nel circuito
                      i1                  i2

        i
GINOL = 1                   r11α   r22α
       vS
            RS


                                                     RL
           vs

                               Rβ




  Retroazione parallelo serie
  ¨   Accesso ad un nodo del circuito retroazionato
      l’uscita è su un ramo della retrazione

                                                    Amplificazione di
      is         GS                                 corrente
                           Hαʹ
                                               RL


                                               iL Segnale di uscita
                           H βʹ
       Retroazione parallelo parallelo
       ¨   Calcolo del risultato
                        ⎡ G                       ⎡ α                                                        ⎤
                                           0 ⎤ ⎢ h11ʹ + hʹ11β + GS                                  ʹα + h12
                                                                                                   h12    ʹβ ⎥
     Hγʹ = Hαʹ + H βʹ + ⎢ S                    ⎥=
                        ⎢ 0
                        ⎣                  RL ⎥⎦ ⎢ hʹ21α + hʹ21β                           h 22 + h 22 + RL ⎥⎦
                                                                                            α       β
                                                  ⎣
                                                                                      ⎡ i ⎤         ⎡ v ⎤
                                                                                      ⎢  S  ⎥ = Hγʹ ⎢ 1 ⎥
                                                                   i2                 ⎢⎣ 0 ⎥⎦       ⎢ i ⎥
                                                                                                    ⎣ 2 ⎦
is           v1                  Hγʹ
                                                                                           ⎡ i ⎤ ⎡ v ⎤
                                                                                        Hʹ ⎢ S ⎥ = ⎢ 1 ⎥
                                                                                            γ
                                                                                             −1

                                                                                           ⎢⎣ 0 ⎥⎦ ⎢⎣ i2 ⎥⎦




       Retroazione parallelo serie
       ¨   Soluzione
                             ⎡ α     β
                     1 ⎢ hʹ22 + hʹ22 + RL                  (
                                                         − hʹ12α + hʹ12β   ) ⎤⎥⎡⎢ i ⎤⎥ = ⎡⎢ v ⎤⎥
                                                                                  S         1
                             ⎢                                              ⎥
                                     (
                  det( Hγʹ ) ⎢ − hʹα + hʹβ      )        hʹ11α + hʹ11β + GS ⎥⎣⎢ 0 ⎥⎦ ⎢⎣ i2 ⎥⎦
                             ⎣    21    21
                                                                            ⎦


       ¨   Analisi del primo trasferimento                                               Termine dominante AID



                                                                                      Termine parassita AIP
                    i2
                       =
                             (
                           − hʹ21α + hʹ21β   ) = −hʹ + −hʹ
                                                     α
                                                    21
                                                                    β
                                                                   21
                    iS           det Hγʹ       det Hγʹ         det Hγʹ
Trasferimento
                                                Termine
¨   Trasferimento                               dominante AID
                                                                                                              Termine parassita AIP


                             =
                                     (
                          i2 − hʹ21 + hʹ21
                                           α

                                           =
                                              −hʹ21α
                                                    β

                                                     +
                                                        )
                                                       −hʹ21β
                          iS   det Hγʹ       det Hγʹ det Hγʹ

                                                                                                                           ⎡ 1                      ⎤
                                    G           Gdiretto                                                                   ⎢                  ≅0 ⎥
                           Greale = ideale
                                         −1
                                             +                                                                       Hαʹ = ⎢   Rin
                                                                                                                                                    ⎥
                                   1 − Gloop   1 − Gloop                                                                   ⎢ AV               Rout ⎥⎦
                                                                                                                           ⎣

                                                                       −AV                                               1             1
Gideale = lim AID = lim                                                                                        =                  ≅
          AV →−∞     AV →−∞
                              (hʹ + hʹ + G ) (hʹ + hʹ + R ) − (hʹ + hʹ ) ( A + hʹ ) (hʹ + hʹ )
                                 α
                                11
                                          β
                                         11     S
                                                             α
                                                            22
                                                                       β
                                                                      22     L
                                                                                       α
                                                                                      12
                                                                                            β
                                                                                           12   V
                                                                                                          β
                                                                                                         21
                                                                                                                     α
                                                                                                                    12
                                                                                                                              β
                                                                                                                             12
                                                                                                                                      hʹ12β


                                                                  1                                                   1
      GD = Gideale                                                                                      = Gideale
                     1+
                               (
                          hʹ21β hʹ12α + h12    ) (
                                         ʹβ − h11
                                               ʹα + h11          )(
                                                     ʹβ + GS hʹ22α + hʹ22β + RL                     )                   −1
                                                                                                                    1− Gloop

                                                  ( hʹ + hʹ )α
                                                            12
                                                              hʹ        β
                                                                       12
                                                                              α
                                                                             21




Gideale nel circuito
                              v1                                                                        i2

                                                                                                                                            i
     iS
                           GS                                    v1 = 0
                                                                 i1 = 0
                                                                                                                                  Gideale = 2
                                                                                                                                           iS
                                                                       v2 non vincolata
                                                                       i2 non vincolata


                                                                                                                              RL


                                   hʹ11β                           hʹ12βi2
Gloop nel circuito
                                                                                                ʹα
                                                                                               h22



                    GS                     h11ʹα




                                                                                                               RL


                                                                      H βʹ

                    Gloop =
                                                                 (
                                                              − hʹ12α + hʹ12β hʹ21α  )
                                  21   (    12
                                                       β
                                                      12   ) (
                                 hʹ hʹ + hʹ − hʹ + hʹ + GS hʹ22α + hʹ22β + RL
                                   β         α                    α
                                                                 11
                                                                            β
                                                                           11                 )(           )




Analisi del secondo termine
¨   Analisi del secondo termine
                                      Guadagno diretto

                                                      hʹ21β                               1
      AIP =     β
                    (    α        β
                                      ) (
              hʹ hʹ + hʹ − hʹ + hʹ + GS
               21       12       12
                                                  α
                                                 11
                                                         β
                                                        11           )(     α
                                                                          hʹ + hʹ + RL
                                                                           22
                                                                                       1− β
                                                                                          G
                                                                                         22 loop   )

                                                              hʹ21β
        Gdiretto =
                             (                   ) (                            )(
                        hʹ21β hʹ12α + hʹ12β − hʹ11α + hʹ11β + GS hʹ22α + hʹ22β + RL                    )

                                                                    1
                                      GP = Gdiretto
                                                                 1− Gloop
   Gdiretto nel circuito
                                                                                                           i2
                                                                                                                                                       i
                                                                                                                                            Gdiretto = 2
                                                                                                                                                      iS
                    iS                         GS                       h11ʹα          ʹα
                                                                                      h22




                                                                                                                                       RL


                                                                            H βʹ




   Analisi del secondo trasferimento
   ¨        Impedenza di ingresso
                                        ⎡ α     β
                                1 ⎢ hʹ22 + hʹ22 + RL                    (ʹα + hʹ12β
                                                                      − h12           ) ⎤⎥⎡⎢ i ⎤⎥ = ⎡⎢ v ⎤⎥
                                                                                                S               1
                                        ⎢                                          ⎥
                                                    (
                             det( Hγʹ ) ⎢ − hʹα + hʹβ             )   hʹ + hʹ + GS ⎥⎢⎣ 0 ⎥⎦ ⎢⎣ i2 ⎥⎦
                                                                        α        β
                                        ⎣    21    21                  11       11
                                                                                   ⎦

                         (   α
                 v1 hʹ22 + hʹ22 + RL
                    =                = α
                                        β
                                                )             hʹ22α + hʹ22β + RL
                 iS      det Hγʹ                        (              )(
                                      hʹ11 + hʹ11β + GS hʹ22α + hʹ22β + RL − h12               ) (
                                                                                 ʹα + hʹ12β hʹ21α + hʹ21β            )(                )

                                      hʹ22α + hʹ22β + RL                                                              1
RIN =
        (                        )(
            hʹ11α + hʹ11β + GS hʹ22α + hʹ22β + RL − h12     ) (
                                                     ʹα + h12
                                                           ʹβ hʹ21β    )        1−
                                                                                                            (                  )
                                                                                                                hʹ12α + hʹ12β hʹ21α

                                                                                     (hʹ + hʹ + G ) (hʹ + hʹ + R ) − (hʹ + hʹ ) hʹ
                                                                                        α
                                                                                       11
                                                                                                β
                                                                                               11      S
                                                                                                                 α
                                                                                                                22
                                                                                                                           β
                                                                                                                          22       L
                                                                                                                                             α
                                                                                                                                            12
                                                                                                                                                  β
                                                                                                                                                 12
                                                                                                                                                       β
                                                                                                                                                      21


    Resistenza anello aperto
                                                                                               1
                                                                        RIN = RINOL
                                                                                            1− Gloop
Ganello aperto nel circuito
       v             v1                   i2
RINOL = 1
       iS

         iS     GS          h11ʹα    ʹα
                                    h22




                                                       RL


                               H βʹ




Retroazione serie parallelo
¨    Accesso ad un nodo del circuito retroazionato
     l’uscita è su un ramo della retrazione
                                                    Segnale di uscita
                                               vL

                                          GL

    RS                    Hαʹʹ                       Amplificazione di
                                                     tensione



    vS



                          H βʹʹ
     Retroazione parallelo parallelo
     ¨   Calcolo del risultato
                      ⎡ R                       ⎡ α                                                           ⎤
                                         0 ⎤ ⎢ h11ʹʹ + hʹʹ11β + RS                               ʹʹα + hʹʹ12β
                                                                                                h12           ⎥
Hγʹʹ = Hαʹʹ + H βʹʹ + ⎢ S                    ⎥=
                      ⎢ 0
                      ⎣                  GL ⎥⎦ ⎢ hʹʹ21α + hʹʹ21β                          hʹʹ22 + hʹʹ22 + GL ⎥⎦
                                                                                              α       β
                                                ⎣
                                                                                      ⎡ v ⎤         ⎡ i ⎤
               i1                                                            v2       ⎢   S ⎥ = Hγʹʹ⎢ 1 ⎥
                                                                                      ⎢⎣ 0 ⎥⎦       ⎢ v ⎥
                                                                                                    ⎣ 2 ⎦
vS
                                         Hγʹ
                                                                                             ⎡ v ⎤ ⎡ i ⎤
                                                                                       H ʹʹγ ⎢ S ⎥ = ⎢ 1 ⎥
                                                                                               −1

                                                                                             ⎢⎣ 0 ⎥⎦ ⎢⎣ v2 ⎥⎦




     Retroazione parallelo serie
     ¨   Soluzione
                          ⎡ α       β
                  1 ⎢ hʹʹ22 + hʹʹ22 + GL                     (
                                                           − hʹʹ12α + h12
                                                                       ʹʹβ) ⎤⎥⎡⎢ v ⎤⎥ = ⎡⎢ i ⎤⎥
                                                                                  S        1
                          ⎢                                                 ⎥
                                     (
               det( Hγʹʹ) ⎢ − hʹʹα + hʹʹβ         )    hʹʹ11α + hʹʹ11β + RS ⎥⎣⎢ 0 ⎦⎥ ⎢⎣ v2 ⎥⎦
                          ⎣    21     21
                                                                            ⎦


     ¨   Analisi del primo trasferimento                                                Termine dominante AVD



                                                                                      Termine parassita AVP
                    v2
                       =
                             (
                           − hʹʹ21α + hʹʹ21β   ) = −hʹʹ + −hʹʹ
                                                       α
                                                      21
                                                                      β
                                                                     21
                    vS           det Hγʹʹ         det Hγʹʹ det Hγʹʹ
Trasferimento
                                                Termine
¨   Trasferimento                               dominante AVD
                                                                                                                  Termine parassita AVP


                            =
                                      (
                         v2 − hʹʹ21 + hʹʹ21
                                           α

                                            =
                                                    β
                                               −hʹʹ21α
                                                       +
                                                        )−hʹʹ21β
                         vS   det Hγʹʹ        det Hγʹʹ det Hγʹʹ

                                                                                                                                ⎡ R                ≅0      ⎤
                                     G           Gdiretto                                                                       ⎢ in                       ⎥
                            Greale = ideale
                                          −1
                                              +                                                                          Hαʹʹ = ⎢                          ⎥
                                    1 − Gloop   1 − Gloop                                                                         A                1
                                                                                                                                ⎢ I                  Rout ⎥⎦
                                                                                                                                ⎣

                                                                       −AI                                                   1             1
Gideale = lim AVD = lim                                                                                           =                   ≅
          AI →−∞      AI →−∞
                               (hʹʹ + hʹʹ + R ) (hʹʹ + hʹʹ + G ) − (hʹʹ + hʹʹ ) ( A + hʹʹ ) (hʹʹ + hʹʹ )
                                  α
                                 11
                                           β
                                          11    S
                                                             α
                                                            22
                                                                       β
                                                                      22       L
                                                                                         α
                                                                                        12
                                                                                                β
                                                                                               12   I
                                                                                                              β
                                                                                                             21
                                                                                                                         α
                                                                                                                        12
                                                                                                                                  β
                                                                                                                                 12
                                                                                                                                          hʹʹ12β


                                                                  1                                                       1
      AVD = Gideale                                                                                         = Gideale
                      1+
                                 (
                           hʹʹ21β hʹʹ12α + h12 ) (
                                            ʹʹβ − h11
                                                   ʹʹα + h11        )(
                                                          ʹʹβ + RS hʹʹ22α + hʹʹ22β + GL                 )                   −1
                                                                                                                        1− Gloop

                                                  ( hʹʹ + hʹʹ )
                                                              α
                                                             12
                                                                hʹʹ     β
                                                                       12
                                                                                α
                                                                               21




Gideale nel circuito
                                                                                                              v2

                                                                      v1 = 0
                                                                                                                                      GL
                                                                      i1 = 0
     RS                                                                     v2 non vincolata
                                                                            i2 non vincolata




     vS


                                                                            hʹʹ12β v2                                                      v2
                                                                                                                                 Gideale =
                                                                                                                                           vS
Gloop nel circuito

                                                                                              ʹʹα
                                                                                             h22
                                             α
                                           hʹʹ                                                      GL
                                            11
        RS




                                                                   H βʹʹ

              Gloop =
                                                               (
                                                              ʹʹα + hʹʹ12β hʹʹ21α
                                                           − h12                    )
                                       (
                                 hʹʹ21β hʹʹ12α + h12 ) (
                                                  ʹʹβ − hʹʹ11α + h11                    )(
                                                                  ʹʹβ + RS hʹʹ22α + hʹʹ22β + GL     )




Analisi del secondo termine
¨   Analisi del secondo termine
                                    Guadagno diretto

                                                 hʹʹ21β                               1
      AVP =     β
                    (    α         β
                                    ) (
              hʹʹ hʹʹ + hʹʹ − hʹʹ + hʹʹ + RS
               21       12        12
                                             α
                                            11
                                                    β
                                                   11          )(     α         β
                                                                    hʹʹ + hʹʹ + GL
                                                                     22        22
                                                                                   1− G  )
                                                                                        loop




                                                          hʹʹ21β
        Gdiretto =
                             (              ) (
                        hʹʹ21β hʹʹ12α + hʹʹ12β − h11                      )(
                                                  ʹʹα + hʹʹ11β + RS hʹʹ22α + hʹʹ22β + GL     )

                                                             1
                                   AVP = Gdiretto
                                                          1− Gloop
  Gdiretto nel circuito

                                                                                                           v2
                                                                                                                                                      v2
                                                                     α             α
                                                                                                                                         Gdiretto =
                                                                   hʹʹ
                                                                    11
                                                                                 hʹʹ
                                                                                  22
                                                                                                                                    GL                vS
               RS



             vs


                                                                     H βʹʹ




  Analisi del secondo trasferimento
  ¨     Impedenza di ingresso
                                        ⎡ α       β
                                1 ⎢ hʹʹ22 + hʹʹ22 + GL                       (
                                                                            ʹʹα + h12
                                                                         − h12     ʹʹβ   ) ⎤⎥⎡⎢ v ⎤⎥ = ⎡⎢ i ⎤⎥
                                                                                                   S              1
                                        ⎢                                               ⎥
                                                     (
                             det( Hγʹʹ) ⎢ − hʹʹα + hʹʹβ        )         hʹʹ + hʹʹ + RS ⎥⎢⎣ 0 ⎥⎦ ⎢⎣ v2 ⎥⎦
                                                                           α      β
                                        ⎣    21     21                    11     11
                                                                                        ⎦


              i1
                 =
                     (   α        β
                   hʹʹ22 + hʹʹ22 + GL
                                      = α
                                           )                    hʹʹ22α + hʹʹ22β + GL
              vS         det Hγʹʹ                (                   )(
                                        ʹʹ + hʹʹ11β + RS hʹʹ22α + hʹʹ22β + GL − hʹʹ12α + h12
                                       h11                                                   ) (
                                                                                          ʹʹβ hʹʹ21α + hʹʹ21β     )(                )
                                  hʹʹ22α + hʹʹ22β + GL                                                                 1
GIN =
        (     α
             11
                     β
                    11       )(
            hʹʹ + hʹʹ + RS hʹʹ22α + hʹʹ22β + GL − h12    ) (
                                                   ʹʹα + hʹʹ12β hʹʹ21β   )       1−
                                                                                                            (                   )
                                                                                                                hʹʹ12α + hʹʹ12β hʹʹ21α

                                                                                      (hʹʹ + hʹʹ + R ) (hʹʹ + hʹʹ + G ) − (hʹʹ + hʹʹ ) hʹʹ
                                                                                         α
                                                                                        11
                                                                                               β
                                                                                              11       S
                                                                                                                 α
                                                                                                                22
                                                                                                                            β
                                                                                                                           22       L
                                                                                                                                          α
                                                                                                                                         12
                                                                                                                                                β
                                                                                                                                               12
                                                                                                                                                       β
                                                                                                                                                      21



   Conduttanza anello aperto
                                                                                            1
                                                                     GIN = GINOL
                                                                                         1− Gloop
  GIN ad anello aperto nel circuito
                            i1

        i
GINOL = 1
       vS                             h11ʹʹα    ʹʹα
                                               h22               GL
            RS



        vs


                                          H βʹʹ




  Generazione delle varie combinazioni
  sullo stesso circuito
                    +                                   +

                    -                                   -




                                                      INPUT PARALLEL
                  INPUT SERIES



                    +                                   +

                    -                                   -          RL




                 OUTPUT          RL                    OUTPUT
                 PARALLEL                              SERIES
UNIVERSITY OF UDINE

Department DIEG
Via delle scienze 206
33100 Udine (UD), Italy




                      CHARCATERISTICS OF
                      OPERATIONAL AMPLIFIERS
                      Assistant professor Stefano Saggini
                      Nome della conferenza o seminario




    Different types of Operational
    amplifiers
    ¨ Voltage mode operational amplifier
    ¨ Current feedback

    ¨ Norton operational amplifier
     OPAMP general Characteristics
     ¨    Polarization and/or large signal
          ¤ Input common mode range ICMR
          ¤  Output voltage swing Voutmax Voutmin
          ¤ Maximum output current
          ¤ Input bias current
          ¤ Slew rate SR
     ¨    AC characteristics
          ¤   Input impedance
          ¤ DC Gain Av(0)
          ¤ Output impedance
          ¤ Gain band product
          ¤ CMRR
          ¤ PSRR
          ¤ Input equivalent noise
     ¨    Mismatch non idealities
          ¤   Input offset Voffset
          ¤   Input current mismatch




     Polarization and/or large signal
     ¨ Input common mode range ICMR
     ¨ Output voltage swing Voutmax Voutmin
         VinCM=(Vin++Vin-)/2
                                                             Vs+
     VinCMmin
                                                                                                Voutmax

                                       Vin+          +                   Iout
                                                                                 Vout
                                       Vin-           -
         VinCMmax
                                                                                                  Voutmin
                                                                   Vs-
Se VinCM è nel range (VinCMmin, VinCMmax ), se Vout è nel range (Voutmin, Voutmax ) e se la corrente di
uscita Iout è nel range (Ioutmin , Ioutmax ) dove Ioutmin è la massima corrente entrante (Massimo sinking) e
Ioutmax è la massima corrente uscente (Massimo sourcing).

L’amplificatore operazionale è polarizzato correttamente e può essere studiato con il suo modello di piccolo segnale.
AC linear model Small Signal
¨ Input impedance differential
¨ Output impedance

¨ Gain transfer function (GBWP)

¨ CMRR

¨ PSRR




Scheme

                    vSP

           2ZinCM

           vD
            2


                           ZinD    Z out

    vCM
           vD                                 ⎛                                         ⎞
                                                        vCM       vSP          vSM
            2                     vout = A(s) ⎜ v D +         +      p
                                                                           +      m
                                                                                        ⎟
                                              ⎝       CMRR(s)   PSRR   (s)   PSRR   (s) ⎠
           2ZinCM




                    vSM
       Gain transfer function
       ¨     Transfer function
              vOUT
                   = AV (s)
               vD                                                  AV (0)
                                                  AV (s) =
                                                             (1+ sτ L )(1+ sτ H )



       AV ( j2π f )                                 GBWP = AV (0) f L
                      db
                           AV (0)
                                    db




                                                               fH

                                         fL     GBWP                         f




       Example CMRR
       ¨     Considering CMRR in the transfer function
                                                                             Gideale
                                                                                                   1
             vOUT   G
                  = ideale                                v +v                          vout 1+ 2CMRR
                        −1                    vin − vout + in out = 0                       =
              v IN 1− Gloop                               2CMRR                         vin        1
                                                                                              1−
                                                                                                 2CMRR

                       ⎛                                                              1            1
                             1 ⎞                                     vout − vin 1+ 2CMRR
                    AV ⎜1+      ⎟                                                                CMRR       1
  vOUT   Gideale       ⎝ 2CMRR ⎠                                               =          −1 =          ≅
       =         =                                                      vin           1              1    CMRR
                         ⎛                                                       1−            1−
              −1
   v IN 1− Gloop              1 ⎞                                                   2CMRR         2CMRR
                   1+ AV ⎜1−      ⎟
                         ⎝ 2CMRR ⎠
                                                                          Gloop

                              +
                                                                                    +
v IN                                                                                                     ⎛   1 ⎞
                                                                                             Gloop = −AV ⎜1−     ⎟
                              -                                                     -
                                                                                                         ⎝ 2CMRR ⎠
Example PSRR
¨   Signal noise on vdd
                              vout   0      Gdirect   Gdirect     1
                                   =      +         ≅         ≡
                       VDD             −1
                              vSP 1− Gloop 1− Gloop    AV       PSRR+
                 vSP


                 +
                                   VOut

                 -


                             VSS




Equivalent circuit
¨   Equivalent circuit



                                   +
           vSP
         PSRR+
                                   -
          vSM
         PSRR−


          vCM
         CMRR
Effetto di offset e bias
¨   Circuito equivalente


                ibias

                                   +

      vOFFSET             Δibias

                                   -

                  ibias




Limitazioni di grande segnale
¨   Limitazione dovuta alla SR considerando un segnale
    sinusoidale di uscita di ampiezza A e frequenza ω


                          Aω < SR

¨   Limitazione dovuta alla Iout sulla massima derivata
    di uscita
                     I
                Aω < out
                     CL
UNIVERSITY OF UDINE

Department DIEG
Via delle scienze 206
33100 Udine (UD), Italy




                      BASIC ANALOG STAGES
                      Associate professor Stefano Saggini
                      Lezione di circuiti e sistemi elettronici




    Stadi differenziali
                                 +Va             +Va


                            RL                          RL

                                                        Vout




                                                RE


                                          -Va
Stadi differenziali
                   +Va         +Va


              RL                     RL
                                                                gm     IR
                                                       Ad =        RL = L
                                     Vout                        2     2VT


       Vd/2                                -Vd/2


                                          Considerando IRL=Va

                                                          Va
                               RE                  Ad =
                                                          2VT

                         -Va




Stadi differenziali
                   +Va         +Va

                                                                    RL              RL
                                     RL            Acm = −                    ≅−
              RL                                             2R + 1
                                                                E
                                                                                   2RE
                                                                         gm
                                     Vout
                                                               IRL    V
                                                    Acm ≅ −        = − L = −1
                                                              2IRE    VRE
       Vcm                                 Vcm




                                                                         Va
                               RE                            CMRR =
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



                                           vD        ⎛    RS      ⎞
                              iD =                   ⎜⎜1−         ⎟
                                     ro +1 gm / / RS ⎝ 1 gm + RS ⎟⎠
           RS




Generatori di corrente
      rD                                  rD
                                                         Approccio retroazione serie-serie


                                               r0

                                                           rD = ROL (1− Gloop)
                          ro vS gm
 VB                                                                      ⎛ gmr R ⎞
                r0                                         = (RS + ro ) ⎜⎜1+    o S
                                                                                      ⎟
                                                                         ⎝   RS + ro ⎟⎠
                               vS
                                                    RS



           RS
                                                                        (
                                                          rD = RS + ro 1+ gm RS     )
     Guadagno stadi elementari con ro

                                                          v DS
           RD
                                         iDS = vGS gm +
                      iDS                                  ro
                 vD
                                                          RS + RD
                                    iDS = vGS gm − iDS
                                                             ro
                            r0

          vGSgm
vG
                 vS                          vGS            vGS
                                 iDS =               =
                                          1 RS + RD
                                            +           1 ⎛ RS + RD ⎞
            RS                                            ⎜1+       ⎟
                                         gm    ro gm   gm ⎝     ro ⎠




     Guadagno stadi elementari con ro

                                     vD          −RD
           RD                           =
                      iDS            vG    1 ⎛ RS + RD ⎞
                                             ⎜1+       ⎟+ R
                 vD                       gm ⎝     ro ⎠ S


                            r0           vS          RS
                                            =
                                         vG    1 ⎛ RS + RD ⎞
          vGSgm                                  ⎜1+       ⎟+ R
vG                                            gm ⎝    ro ⎠ S
                 vS

            RS
  Guadagno stadi elementari con ro

                RD
                                  V0




                                                           RS
                                       r0        vo = iS          RD
                                                         RS + Rin

                 Rin
        iS                        RS




  Guadagno stadi elementari con ro

                                                  RD
                             vS
               Rin


                                            r0
             ro vS gm                       RD   Retroazione negativa (analogamente a
   vS                   r0
                                                 prima può essere interpretata utilizzando
                                                 il modello con i generatori di corrente
                                                 come retroazione positiva minore di 1)


           ro + RD   r + RD
Rin =              = o                           Ovviamente tende a 1/gm se ro è molto
        1− Gloop(0) 1+ gmro                      alta e maggiore di RD.
   Guadagno stadi elementari con ro

             RD                                   RS
                                      vo = iS            RD
                          V0                    RS + Rin


                               r0                 RS
                                    vo = iS               RD
                                                   r + RD
                                              RS + o
                                                  1+ gmro
             Rin
        iS                RS




UNIVERSITY OF UDINE

Department DIEG
Via delle scienze 206
33100 Udine (UD), Italy




                      CURRENT MIRRORS
  Current Mirrors

                                                            Rin=gm1gm2/(gm1+gm2)
 Small signal consideration
                                                            Rout=ro4 (1+gm4 ro3)+ro3
             Rin=1/gm1                                      Vmin= Vgs3 +Vov4
             Rout=ro2
                                                                           2
                                                            σ ID      ! σ $ ! 2σ $ 2
             Vmin= Vov2                                           =   # Kp & + ## VT
                                                                                     &&
                                                            I REF     # k &
                                                                      " p % " VOV %
Considering equal the two drain voltage              Vdd

                             2
              σ ID      ! σ $ ! 2σ $2                IIn                        Iout
                    =   # Kp & + ## VT &&
              I REF     # k &
                        " p % " VOV %
       Vdd


     IIn                          Iout                                                 M4
                                               M1


  M1                                     M2                                            M3
                                               M2




  Current Mirror

Rin≅ gm2gm3/(gm3+gm2)
Rout≅ ro3 (1+ro1gm3) with (gm1 equal to gm2)
Vmin= Vgs2+ Vov3
                                                           Vdd


                                                            IIn
Considering equal the two drain voltage


                         2
 σ ID         ! σ $ ! 2σ $2                                                            M3
       =      # Kp & + ## VT &&
 I REF        # k &
              " p % " VOV %
                                                M1                                 M2
   Current Mirror

Rin=1/gm4
Rout≅gm3 ro3 ro2gm1 ro1                                        Vdd
Vmin= Vov3 +Vgs1
                                                                Ireg              Iout




Considering equal the two drain voltage
                                                  Vdd

                                                                                         M3
                2
 σ ID     ! σ $ ! 2σ $2                            IIn
       = ## Kp && + ## VT &&
 I REF    " k p % " VOV %                                 M1


                                          M4                                        M2




   Current Steering DAC

                                                         P$matrix$
                                           ……..$

                                           ……..$


BIASN$
                                                               Out$P$
            DAC$$$BIAS$               SWITCH$                           Output current
                                      MATRIX$                  Out$N$




                                                         N$matrix$
                                           ……..$

                                               ……..$
   Current Steering DAC
                          VddA     VddD

               B<0:4>                  Bias_n
    Binary
               B<0:4>                     Outpos
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
    M1a                                     M1b                 M2
                            1


                                 M2         M1a             2          M1b


¨         Input Dynamic
     ¤      ICMR
     1.     Vincm (min)= Vov1+Vov2 + VTn (for n MOS) Vss for (for p MOS)
     2.      Vincm (max)= Vdd-Vov1-Vov2 - |VTp | (for p MOS) Vdd for (for n MOS)

¨         Trasconduttance :
                                      gm = K1 I D2
¨         Precision
                                               ⎞ ⎡⎛ σ ⎞           2⎤
                                                  2         2
                                       ⎛V                     ⎛σ ⎞ ⎥      Specchio
             σ Vos = σ      2
                                    + ⎜⎜ OV1,2
                                               ⎟⎟   ⎢⎜ Kp
                                                          ⎟     I
                            Vt1,2                   ⎢⎜    ⎟ +⎜ ⎟ ⎥
                                       ⎝ 2 ⎠ ⎣⎝ k p ⎠a,b ⎝ I ⎠ ⎦




Inverter current source
                            Vdd


                 Vbias
                                                      Ouput signal range
                                                      Voutmax=Vdd-Vovp
                                      Vd
                                           Vout       Voutmin= Vovn
                                                      Input dynamics
                      Vg                              Vinmin≅ Vinmax ≅ Vovn+VT


                           Gnd



¨    To increase the dynamics
     ¤ Increase W/L of nch and pch (decrease Vov)
     ¤ Reduce the current
  Inverter current source Tf
                                                                                                         C gd
                                                                                                  1− s
                                                                                                  gm
                             T (s) = −gm Rd Rg 2
                                                   (                                              ) (                                          )
                                              s RgC gs Rd C gd + RgC gs Rd Cd + RgC gd Rd Cd + s RgC gs + RgC gd Rd gm + RgC gd + Rd C gd + Rd Cd +1
               Rd
                        Cd


                      Vd   Output
            Cgd                                             1
Input                                      p1 ≅ −
                                                       gm C gd Rg Rd
                                                                                    |T(s)|
 Ig           Vg
                                                                gm C gd
               Cgs                         p2 ≅ −
         Rg
                                                       C gd (C gs + Cd ) + C gsCd
                                                  gm
                                           z1 =                                                           p1 p2 z1
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
                                                   (                                              ) (                                          )
                                              s RgC gs Rd C gd + RgC gs Rd Cd + RgC gd Rd Cd + s RgC gs + RgC gd Rd gm + RgC gd + Rd C gd + Rd Cd +1
               Rd
                        Cd


                      Vd   Output                                                                 1
            Cgd
Input                                                                               p1 ≅ −
 Ig           Vg                                                                             gm C gd Rg Rd
         Rg
               Cgs                                                                                         gm C gd
                                                                                    p2 ≅ −
                                                                                             C gd (C gs + Cd ) + C gsCd
                                                                                           gm
                                                                                    z1 =
                                                                                           C gd
                     Adding a capacitor on Ccg
                      |T(s)|



                                                              z1
UNIVERSITY OF UDINE

Department DIEG
Via delle scienze 206
33100 Udine (UD), Italy




                      DESIGN OF OPAMPS
                      Assistant professor Stefano Saggini
                      Nome della conferenza o seminario




    OPAMP general Specifications
    ¨   DC Gain Av(0)
        ¤ Also the (depend on the application) CMRR

    ¨ Gain band product
    ¨ Input offset Voffset

    ¨ Input common mode range ICMR

    ¨ Output capacitance CL

    ¨ Slew rate SR

    ¨ Output voltage swing Voutmax Voutmin

    ¨ Consumption Pdiss

    ¨ Input equivalent noise
Two stage OPAMP design Steps
¨ Depending on the                      Vdd

  ICMR spec choice of              M5          M6              M7

  the n-ch differential
  stage or the p-ch                                       Cc



¨ Determination of the
  Vov of M5 and M6 for       V-                      V+        Vout

  the Max ICMR                    M3           M4



¨ Determination of the                   Id1                    Id2


  Vov of M1,2,3,4 Min             Vg    M1           Vg        M2


  ICMR                                         Vss




Two stage OPAMP design Steps
¨   The Input offset                    Vdd

    determine the                  M5          M6              M7


    dimension of the stage
                                                          Cc




                             V-                      V+        Vout
                                  M3           M4



                                         Id1                    Id2


                                  Vg    M1           Vg        M2


                                               Vss
    Two stage OPAMP design Steps
    ¨ The Gain bandwidth                                                    Vdd

      product and the phase                                            M5          M6              M7


      margin in follower is a
                                                                                              Cc
      function of
    ¨ The slew rate is
                                                                                                   Vout
      function of                                                V-
                                                                      M3           M4
                                                                                         V+




                                                                             Id1                    Id2


                                                                      Vg    M1           Vg        M2


                                                                                   Vss




    Project of two stage OpAmp
    ¨    Determination of the capacitor Cc
        gm3, 4
GB @                                                                         Considering the ratio
          CC                                                                 0.1
                           -1
p1 @
       æ ro 7 ro 2 ö          æ r r ö                                        gm7 > 10 gm3, 4
       çç             ÷÷ gm7 çç o 6 o 4 ÷÷CC
        è ro 7 + ro 2 ø       è ro 6 + ro 4 ø
       - gm7
p2 @
        CL
       gm7                                                                  p2 > 2.2 GB
z1 =
       CC
                                                                            gm7      gm
                   æ GB ö            æ GB ö            æ GB ö                   > 2.2 3, 4
60 < 180 - tan -1 çç    ÷÷ - tan -1 çç    ÷÷ - tan -1 çç    ÷÷              CL        CC
                   è p1 ø            è p2 ø            è z1 ø
                                                                            CC > 0.22 C L
Project of two stage OpAmp
¨   Determination of gm3,4

                gm3,4 ≅ GB CC
¨   From slew rate can be determined the Id1

                 I d1 = SRCc

¨   From the two information can be calculated the
    Vov3,4
                         2 ID   I
              Vov3,4 =        = d1
                         gm3,4 gm3,4




Project of two stage OpAmp
¨   Determination of the ratio of 3,4
                             !I $
                           2 # d1 &
               !W $          " 2 %
               # & =                  2
               " L %3,4 K ' (Vov *
                          n)     3,4 +




¨   As a function of the ICMR max the (W/L)5,6 is
    determined
                                     !I $
                                   2 # d1 &
          !W $                       " 2 %
          # & =                                       2
          " L %5,6 K ' )V −V (max) − V (max) +V (min)+
                     p * DD in        T5       T3    ,
 Project of two stage OpAmp
 ¨   As a function of the offset we will determines the
     values of Area
                                                          Minimum area required


                                $ '! σ $ ! σ I $2 *
                                  2         2
                        !V
σ Vos = σ   2
            Vtp3,4
                     + ##
                        "
                          OV3,4

                           2
                                && #)   Kp
                                           & +# D & ,
                                    )# k & #" I &% ,
                                 % (" p %3,4
                                                                                  W3,4,5,6
                                                D 5,6
                                                      +


                                2           2
  !σ I $                ! σ $ ! 2σ        $
  ## D && =
   " I D %5,6
                        #  Kp
                              & #
                        # k & +# V
                                   VTp5,6

                        " p %5,6 " OV5,6 %
                                          &
                                          &                                       L3,4,5,6




 Project of two stage OpAmp
 ¨   As a function of the ICMR min the (W/L)1 is
     determined

                         Vin min = Vov1 +Vov3,4 +VT max




                                    !W $
                                    # & =
                                             2 I d1   ( )
                                                      2
                                    " L %1 K ' (Vov *
                                             n)     1+
      Project of two stage OpAmp
      ¨   Considering the trasconductance relation
                           gm7 > 10 gm3, 4

      ¨   Considering                        !W $      10 gm3,4
                                             # & >
                                             " L %7 K P Vov5,6
                                                          ! W $ ! W $ Id1
                                             Id7 = Id 2 = # & / # &
          Vov5,6 = Vov7                                   " L %7 " L %5,6 2

                                                ! W $ ! W $ Id 2
                                                # & =# &
                                                " L %2 " L %1 Id1




      Output stage
      ¨   Obviously a buffer output stage reduce Cc
                   Vdd

            Cgd
C’L                      1/gm                              C’L<CL
            Cgs            Vout

                                                  Condition to be imposed
                            CL
           Vbias
                                                          1       gmout
                                                 p3 ≅           =       > 10GB
                                                        RoutC L    CL
                   Vss
Output stage
¨   Output stage

                           Cc
                                                      Cc

                           1                                  1

                                CL




Inserting a zero on the loop transfer
function
¨   Inserting the zero in the transfer function


       Second Stage of the OpAmp

             R
                      Rd

       Cc                                        1
                                     z1 =
                                              (
                                            CC 1 gm − R   )
Inserting a zero on the loop transfer
function
¨   Controlling the right half-plane zero



                 gm2


                                                        1
                                           z1 = −
                            Cc
                                                      (
                                                    CC 1 gm2   )




Compensation that increase p2
¨   The feedback gain reduce the output impedance of
    the structure         VDD


                                 Cc



                       M8        VB    VOUT




                                      M7
  Compensation that increase p2
  ¨   At high frequency
                            VDD


                                Cc
                                                            −gm7 gm8 Rdstot
                                                     p2 ≅
                                                                 CL
           M8
                                   VB         VOUT



                                                      CL

                                            M7
                          Rdstot




  PSRR: Substrate noise coupling
  ¨   Vdd and Gnd bounce
                                        DC-DC converter                 Analog Circuit
           Logic circuit well           well     Vin


GND




      P+
                Nwell                      Nwell                     Nwell




                          Psub
  PSRR: Substrate noise coupling Analysis

  ¨   For each point can be defined a T(s)
                          GND                                   T(s)
                          external                 Vin(s)                   Vdd(s)



                             MIM
              Vdd(s)         internal
                                        GND
GND                                                                Vin(s)
                                        internal
                                                       Source of Noise
      P+
                  Nwell                               Nwell




                                        Psub




  PSRR:Substrate noise coupling Analysis

  ¨   For each sensitive point and each noise source can
      be defined a T(s)


                    T1P
       S1
                                                                       |T(ω)|

            T2P       P
       S2




                                                                                ω
PSRR
¨   Definition

                               Vout   0      G       G           1
                  VDD               =   −1
                                           + direct ≅ direct ≡
                               Vdd 1− Gloop 1− Gloop  AV       PSRR+
                         Vdd
             +
                                VOut

             -


                        VSS




PSRR
¨   Calculation
                                                            ro2          (1+ sτ z )
                                           Gdiretto =
                                                        (ro7 + ro2 ) (1+ sτ 1 )(1+ sτ 2 )

                                M7
                                                             1        z1 =
                                                                                 ro2
                                                                                         p
                                                                             (ro7 + ro2 ) 1




M1                               M2
                                                 z1     p1       p2
PSRR close loop
¨   Calculation close loop
                                       vdd 1− Gloop
                             PSRR+ =        =
              VDD                      vout   Gdirect

                                                                 AV (0)                   A (0)
                                                   PSRR+ (0) =          (g ds7 + g ds2 ) = V    (ro7 + ro2 )
                      Vdd                                         g ds7                    ro2

         +
                            VOut

          -


                    VSS


                                                                         GB        p2




PSRR
¨ Non Linear effect of the OpAmp as Asymmetrical
  slew rate can rectify the noise
¨ This effect are studied by AC simulations




                    VDD




                    VOut
Low Noise design
¨    The PMOS have about 2 to 5 less 1/f noise than n
     ¤ Design a PMOS input stage

¨    Make the first gain stage as high as possible
     ¤ Cascode structure to increase the low frequency gain of
          the opamp




P-ch Folded cascode input schematic

¨    Increase the Input common mode range
          Vdd               Vdd                             Vdd


                Iref              Iref                            I1std




                                                    I1std /2      I1std /2


4*(W/L)
                                                                                    I1std /2   I1std /2
                                (W/L)
4*(W/L)         VT+Vov
                                                                                       (W/L)*I1std /(2 Iref )
    Vov                                             I1std           I1std
                                                             Vov
                                                                             4*(W/L)*I1std / Iref
                       VT+Vov            VT+2*Vov


          Polarizzation
             Input rail to rail
                                                               Vdd



                             IB1
                                                                                   GM


                                                                          VB

                                                                          OUT                  Correction
        INP
                                                   INM
                                                               VB                                            VICM



                            IB2
                                                               Vss




             Output rail to rail

                      Vdd                                                               Vdd


                            I1std
                                             M7                            M8                 M9            M12     M13

                                                                                                                     OUT
        M1                               M2
    +                                          -
              I1std /2      I1std /2
                                                                                                    CC        R
                                       Vpol2                               Vpol2
                                                    I1std /2   I1std /2
                                        M6                                 M5


        M3                                 M4
Vpol1         I1std           I1std                Vpol1                                                            M14
                       Vov
                                                                                        M10                  M11
Current feedback
                              Vdd


                                    (25/1)                      (25/1)
                100µ




                                             (10/1)


 In+                                            In-                                Vout
                           (25/1)                                             X1

       (10/1)
                                              (25/1)


                                                                      Ccomp


                 100µ
                                    (10/1)                      (10/1)

                               gnd

                 µnCox = 200µA/V2                      µpCox = 80µA/V2
                       VTn = 0.6V                       |VTp|= 0.6V




µ741
Input stage
                               ¨   Input stage npn higher !
                               ¨ Gain gm/4 of
                                 differential stage gain
                                 final gm/2
                               ¨ Mirror with offset

                                 compensation
                               ¨ Second stage npn higher
                                 performance
                               ¨ Bias loop for first stage




Second stage
                               ¨ Darlinton Q15-Q19
                               ¨ Protection Q22 Q17

                               ¨ Q14 and Q20 class AB
                         Q14
                                 stage
                   Q17         ¨ Q16 vbe multiplier
             Q16
                                 (Vbe*(1+4.7/7.5))
       Q15
                         Q20
 Q22
             Q19
