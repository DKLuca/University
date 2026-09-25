---
fonte: "1 - Introduzione.pdf"
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
¨   Discussing example related
    ¤ Analog processing



    Sensors                                 Acquisition system

Input Signals                               Output Signals

                   Modification
                   • Linear or non linear
Example of design: LiFi
¨   Specification




            TX            RX
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
      ¨   High level                    CK

                                                  n
         Signal
                                                           Logic             Digital
    Dependent on light                 ADC
                                                        elaboration          output
        intensity



                                      All in µC
                                      Or 2 different integrated circuits


                                                                 LSB=FS/2n
At transistor level this connection
isn’t necessarily banal

                                       TCK
TODIODE CIRCUITS   the VOUT is given as VOUT = IP × RL. An output voltage
AMENTAL PHOTODIODE CIRCUITS
                   proportional to thethe VOUT is
                                        amount  ofgiven as Vlight
                                                   incident       = Iobtained.
                                                              OUT is P × RL. An output voltage

                   Example of sensor: Photodiode
  e fundamental photodiode
 es 1 and 2 show the fundamentalThe

  ure 1 transforms a photo-
                                                 photodiode
                                               VCC {proportionalThe
                                                                    proportional
                                                     proportional region           to the amount
                                                                            is expanded
                                                                         proportional
                                                                     region:  VOUT < (V
                                                                                             by theofamount
                                                                                         region+ is
                                                                                                        incidentoflight is obtained.
                                                                                                     expanded by the amount of
                                                                                           OC VCC)}. On the
                                                                    VCC {proportional region: VOUT < (VOC + VCC)}. On the
circuit shown in Figure 1 transforms           other   hand, application
                                                    a photo-                 of reverse bias to the photo-
  odiode without bias into a                                        other hand, application of reverse bias to the photo-
  produced by a photodiode without             diode
                                                  bias causes
                                                        into a the dark current (Id) to increase, leaving
  age (V OUT ) is given as                                          diode causes the dark current (Id) to increase, leaving
e. The output voltage (V OUT ) ais voltage         given as of Id × RL when the light is interrupted,          and
en
  1P × RL. It is more
      V OUT   <  V OC
                       Sensor photodiode
  or less proportional to the
                     ¨. It can
                             or less proportional
                                  also
                                                        to the
                                               this point
                                                                    a voltage of Id × RL when the light is interrupted, and
                                                            should be  noted
                                                                    this point in designing
                                                                                should   be     the in
                                                                                            noted    circuit.
                                                                                                       designing the circuit.
  of incident light when VOUT < VOC. It can also
  lly relative
pressed          to the amount
             logarithmically         of to the Figure
                                 relative          amount 2of(B) shows     the 2operating
                                                                       Figure      (B) showspoint     for a loadpoint for a load
                                                                                                 the operating
near
   lightVwhen
          OC. (V VOC   is the open-            resistor RL with reverse
                                                                    resistorbias  applied   to the  photodiode.
                  OUT is near VOC. (VOC is the open-                          RL with  reverse   bias  applied to the photodiode.
  iode).
    voltage of a photodiode).                      Features of a circuit  used with
                     Proportional to                                   Features   of a acircuit
                                                                                          reverse-biased
                                                                                                used with apho-
                                                                                                              reverse-biased pho-
erating    point
 e 1 (B) shows thefor  a load   resis-
                        operating     point fortodiode    are:
                                                a load resis-       todiode are:
 fwithout
                     The
     bias toapplication
                           amount
              the photodiode.
                                       of                                                           Large signal model
                           of bias to the photodiode.
                                               • High-speed response
                     Incident light                                 • High-speed response
  in  which    the  photodiode       is
 e 2 shows a circuit in which the photodiode is
                                               • Wide-proportional-range         of output
                                                                    • Wide-proportional-range         of output
a photocurrent
-biased               (IP) a
             by VCC and     isphotocurrent
                               trans-           (IP) is trans-
e.ntoAlso   in this voltage.
       an output    arrangement,                   Therefore, this circuit
                               Also in this arrangement,                     is generally
                                                                       Therefore,           used.
                                                                                    this circuit  is generally used.

                   Large signal analysis
                           IP
                                                               EV1 < EV2 < EV3             EV1 < EV2 < EV3        Small signal model
   IP                                                                                         I
                                                                  I                                           V
                                                                                       V

                                                         EV1                     EV1                          1/gm
              E
            RL V        VOUT
                                      RL        VOUT
                                                                                 EV2
                                                                                                                            CD
                                                         EV2                                                                           RL
                                                                                 EV3
                                                         EV3                                             RL
                                                                             RL                   VOUT
                                                                      VOUT

                                (A)                                                               (B)
                                                                            EV1 < EV2 < EV3                                              V
            IP
                                                                                    I
                                                                                                     EV1 V



                   Example Photodiode
                 EV                           RL      VOUT          EV1
                                                                                                     EV2
EV                         RL          VOUT
                                                                    EV2
                                                                                                     EV3
                                                                                                                                 RL
                                                                    EV3                                              VOUT
                                                                                                     RL
                                                                                        VOUT

                    ¨
                   (A)
                           Polarized inverse
                                       (A)
                                                                                         (B)
                                                                                                                     (B)
                                                                                                                       Small signal model OP1-16
                                                                                                                                OP1-16
                            Figure 1. Fundamental Circuit of Photodiode (Without Bias)
     Figure 1. Fundamental Circuit of Photodiode (Without Bias)

                                 VCC
             VCC
                                                                                                    EV1 < EV2 < EV3
                                                                   EV1 < EV2 < EV3
                                         IP                                                           VCC        I
                      IP
     EV
                           EV                                        VCC        I
                                                                                                V
                                                                                                                            V                 CD
                                                                                        EV1
                                                             EV1

                                                                                        EV2
                                                             EV2

           RL               VOUTRL             VOUT          EV3                        EV3


                                                                          VOUT                             VOUT
                                                                                                                                         RL
                                                                                               RL                          RL



             (A)                 (A)                                      (B)                              (B)
                                                                                                                                OP1-17             OP1-17

          Figure 2. Fundamental  Circuit of Photodiode
                      Figure 2. Fundamental             (With
                                               Circuit of     Bias)
                                                          Photodiode (With Bias)
Basic ADC
¨   ADC conversion two types
            Vin not differential

                                   n   Vin input conversion range
                       ADC             From a Vin MIN to a Vin MAX with n bit
Vin
                                        Zin             Input impedance


            Vin differential           Each input has a dynamic range
                                       from a VP,M MIN to a VP.M MAX
     VinP                          n
    Vin               ADC              The difference Vin = Vin P - Vin M
     VinM                              is converted From a Vin MIN to a Vin MAX
                                       with n bit
