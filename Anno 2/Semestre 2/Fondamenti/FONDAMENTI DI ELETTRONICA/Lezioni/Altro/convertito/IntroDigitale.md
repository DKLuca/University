---
fonte: "IntroDigitale.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Introduzione al corso
«Fondamenti di elettronica
        digitale»
       AA 2015/16
           Pierpaolo Palestri
  Dipartimento di Ingegneria Elettrica
        Gestionale e Meccanica
 Corso di Studi in Ingegneria Elettronica
     Dove troviamo i circuiti integrati ?
• dappertutto ! In telefoni, tablet, PC, elettrodomestici,
  automobile…
• esempio:
   iPhone 3G




                                                             2
    Dove troviamo i circuiti integrati ?




Apple watch

                                           3
Cosa c’è dentro le “scatoline nere”?
                                           fili ultra-sottili che
                                           contattano il chip



                            singolo chip

wafer di silicio




                   chip “impachettato” e
                   saldato sulla “board”
                                                             4
Il “mattoncino utilizzato”: il transistor
                   Transistore MOS




                Transistore bipolare




                                            5
Come è fatto un transistor MOS ?

              transistor
              Metallo/Ossido/Semiconduttore ad
              effetto di campo


    D                   D
                              interruttore
G                G            controllato


    S                  S
                                             6
Elettronica analogica
           /
 elettronica digitale

          tutti i segnali sono in realtà
          analogici

          l’elettronica digitale associa
          significati a fasce di valori

          segnali binari: ‘0’ e ‘1’


                                           7
BJT/MOSFET vs. analogico/digitale

              Circuiti       Circuiti
              analogici      digitali
     BJT      Corso del      obsoleti
              prof.Driussi
     MOSFET                  NOI SIAMO
                             QUA




                                         8
Quanti transistori stanno in un chip ?




• dei miliardi ! Ed il numero cresce esponenzialmente
  da 40 anni !                                     9
Quanti transistori stanno in un chip ?




  1o IC (1961)


                                     x86 (‘90)
                 intel 4004 (1971)
                 2300 transistors
                                                 NVIDIA’s Kepler GK110 (2013)
                                                  7,080,000,000 transistors




                                                                       10
     Quanto costa un transistor ?




• oggigiorno 5 milioni di transistori costano
  come un ettogrammo di riso
                                                11
                Come funziona un transistor ?
  • applicando una tensione sul gate si crea un canale tra
    source e drain
                       VG<VT                           VG>VT
elettrone                         ossido




    source                drain              source          drain

                   D
                                      IDS   OFF   ON

            G           IDS
            VGS
                                                       VGS
                  S                          VT                      12
    Cosa realizziamo coi transistor ?
 • funzioni logiche che vengono combinate insieme
   per creare sistemi molto complessi

esempio: funzione NAND,           esempio: sommatore a
OUT=1 se A=0 e B=0                1bit con riporto


                  tensione
                  applicata VDD




                                                         13
 Perchè riusciamo a mettere sempre
  più transistor nei circuiti integrati ?




• perchè li facciamo sempre più piccoli;
  lunghezze da 10m a 20nm in 40 anni      14
       Ci sono vantaggi oltre alla
        maggiore integrazione ?
                                                LG W


                                                           EOT




                                                𝑊 1
                                   corrente          𝑉𝐷𝐷 − 𝑉𝑇 2
                                                𝐿 𝐸𝑂𝑇

                                             1
                                   clock       𝑉 − 𝑉𝑇
                                             𝐿2 𝐷𝐷
• transistor sempre più veloci !                           15
 Quanto è complicato fare transistor
       sempre più piccoli ?

                                          LG


                                                       EOT




        2002    2006    2010

• diventa sempre più difficile ridurre le dimensioni
                                                        16
   Quanto è complicato fare transistor
         sempre più piccoli ?
• occorre complicare enormemente i processi tecnologici, per
  esempio usando molti materiali nuovi




                                                           17
   Quanto è complicato fare transistor
         sempre più piccoli ?
• architetture di transistore sempre più complicate; esempio:
  FinFET (Intel, 2011)




 • costo di una nuova FAB  10B$
                                                                18
    Quanto è complicato fare transistor
          sempre più piccoli ?
• processi complicati anche per interconnettere i miliardi di
  transistor




 • costo di una nuova FAB  10B$
                                                                19
    Quanto è complicato fare transistor
          sempre più piccoli ?
• già oggi siamo vicini alla saturazione della riduzione delle
  dimensioni del transistor (LG) ma miglioriamo la densità
  complessiva (half-pitch)


                                  half-pitch
       nanometri




                           node


                   LG



                                                                 20
Dimensioni dei wafer di silicio




                                  21
    Chi produce i chip ?




TSMC (solo foundry): 14.7B$ in 2011
                                      22
Chi produce i chip ?




                       23
Suddivisione per prodotti



                      il nostro corso




                                        24
 Quanta Potenza consuma un chip ?
                              𝑊𝐿       2
• singolo transistor: 𝑃1𝑡𝑟 ∝      𝑓𝑐𝑘 𝑉𝐷𝐷
                              𝐸𝑂𝑇
                      𝑃𝑐ℎ𝑖𝑝    1       2
• Potenza per area:         ∝     𝑓𝑐𝑘 𝑉𝐷𝐷
                        𝐴     𝐸𝑂𝑇



                                     I trend di incremento di
                                     frequenza di clock fck
                                     degli anni ‘90 sono
                                     diventati improponibili
                                     negli anni 2000

                                                                25
Quanta Potenza consuma un chip ?
• senza ridurre VDD non si può aumentare fCK !
                   𝑃𝑐ℎ𝑖𝑝    1       2
                         ∝     𝑓𝑐𝑘 𝑉𝐷𝐷
                     𝐴     𝐸𝑂𝑇
           VDD ed fCK quasi ferme dal 2002 ad oggi




                                                     26
 Perchè la tensione di alimentazione
         non si può ridurre ?
• per ridurre VDD bisogna ridurre anche VT
                    𝑊 1
       corrente          𝑉𝐷𝐷 − 𝑉𝑇 2
                    𝐿 𝐸𝑂𝑇
           IDS   OFF     ON
                                       scala log



                                  VGS
                    VT

• ridurre VT aumenta esponenzialmente
  il consumo dei transistori spenti !
                                                   27
Perchè la tensione di alimentazione
        non si può ridurre ?
• variabilità ! I transistor non sono tutti uguali 
  dispersione statistica




• Per VT bassa, si rischia che una % non piccolo di transistori
  sia sempre accesa (o sempre spenta)
                                                                  28
Ci sono soluzioni per aumentare le
          performance ?
• Si ! Usare processor con più di un “core”
                                        densità e performance
                                        complessive migliorano



                                         Potenza, clock e
                                         performance
                                         singolo core
                                         sono “fermi”




                                                        29
      Quanto è importante il consumo di
          energia dell’elettronica ?




                                          10% of the global energy consumption is due to
                                          electronic devices, mostly for ICT and CE.
In 2007 the energy supply of ICT produced CO2-output
at level of 25% of worldwide cars                                                      30
  Quanto è importante il consumo di
      energia dell’elettronica ?
                        • Potenza dissipata dai data centers: 
                          30GW (circa 10GW solo negli USA)
                        • 50% per il cooling
                        • una ricerca su google richiede 1kJ
                        • circa 100k ricerche per secondo
                        • una e.mail di 1M=19g di CO2=1Km
batteria AA (stilo)      in auto 190 miliardi di e.mail al
2Ah1.5V= 11 kJ           giorno

                        • consumo medio di uno smart-phone
                          50mW (0.2kJ in 1h)         31
Quanto è importante il consumo di
    energia dell’elettronica ?
                        • una %
                          significativa
                          di consumo è
                          dovuta a
                          dispositivi in
                          stand-by




                                       32
Che soluzioni si stanno studiando ?
• dispositivi con pendenza da spenti molto maggiore del MOSFET




                                               riduco VDD a parità di
                                               corrente di transistor
                                               spento




                                                                   33
  Che soluzioni si stanno studiando ?
 transistor “lunghi”                    transistor “corti”
             𝑊 1                                         𝑊
corrente          𝑉𝐷𝐷 − 𝑉𝑇 2      corrente       𝑣𝑥       𝑉 − 𝑉𝑇
             𝐿 𝐸𝑂𝑇                                      𝐸𝑂𝑇 𝐷𝐷
         1                                        𝑣𝑥
 clock  2 𝑉𝐷𝐷 − 𝑉𝑇                     clock 
         𝐿                                        𝐿


• Usare materiali con vx maggiore del
  silicio per ridurre VDD senza dover
  ridurre VT !
• esempio: vx(Si)107cm/s 
  vx(In0.53Ga0.47As)3107cm/s

                                                                     34
La nano-elettronica sono solo
     microprocessori ?

                 No !
                 • telecomunicazioni
                 • controllo di Potenza
                 • sensori
                 • memorie
                 • …..


                                          35
La nano-elettronica sono solo
     microprocessori ?

                cellulare fine anni ’90
                10chip + 100 passivi


                                          chip RF del
                                          iPhone 3G




                                               36
 Vantaggi dell’elaborazione digitale
• maggiore immunità ai disturbi
• minore impatto delle variazioni delle
  caratteristiche dei componenti (per esempio
  effetti della temperatura)
• precisione= n. di bit, non precisione nelle
  grandezze elettriche
• modularità:
  – progettare i diversi blocchi separatamente
  – riutilizzo dei blocchi
  – automatizzazione con strumenti TCAD
  – riduzione del time-to-market
                                                 37
                 I livelli di astrazione



livello “gate”

                                           livello layout




                      livello transistor
                      (schematico)



                                                            38
Esempio di standard cell




      XOR a 2 ingressi

                           39
            Esempi di Floor-plan




Micro controllore       IC per Wi-fi




                                       40
Design flow dei circuiti digitali




                                    41
Costo del design




                   42
Tempi di design




                  43
       Programma del corso
• Figure di merito dei gate digitali
• il transistore MOS
• scaling della tecnologia CMOS
• caratteristiche statiche e dinamiche dei
  gate logici CMOS
• logiche statiche, logiche a pass-
  transistors, logiche dinamiche


                                             44
         Cosa impareremo ?
• modello del transistore MOS per risolvere
  circuiti con tale componente
• come interconnetere dei MOSFET per
  realizzare semplici porte logiche
• come dimensionare i transistori per
  definire
  – le caratteristiche ingresso/uscita
  – la temporizzazione (ritardo, tempo di salita)
  – la potenza dissipata

                                                    45
Libro di testo

       D.Esseni
       Circuiti Digitali Integrati CMOS




                                          46
