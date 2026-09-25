---
fonte: "1_introduzioneFondElettronica.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Fondamenti di Elettronica
          Analogica e Digitale

               Prof. Francesco Driussi

      Corso di Laurea in Ingegneria Elettronica
Dipartimento Politecnico di Ingegneria ed Architettura

             francesco.driussi@uniud.it
                 elearning.uniud.it/
             www.diegm.uniud.it/driussi
                   Francesco Driussi – 2024
          Cos’è l’elettronica?
Difficile rispondere in breve.
Siamo circondati dall’elettronica…
                                   Applicazioni dell’elettronica
Le applicazioni dei sistemi elettronici sono praticamente infinite:
•   microelettronica
•   informatica
•   telecomunicazioni
•   sensoristica
•   robotica e automazioni industriali
•   automotive e trasporti
•   domotica
•   diagnostica e clinica medica
•   smart health
•   gestione dell’energia
•   visione artificiale
•   fisica sperimentale e delle particelle
•   aerospazio
•   intelligenza artificiale
•   …
Nuovi ambiti e applicazioni sono costantemente contaminati
dall’elettronica à qual è il comune denominatore?
                                   Sistema elettronico

Formato da molti componenti attivi e passivi che ne definiscono
la/le funzione/i



   iPhone 3G
                                   Sistema elettronico

Formato da molti componenti attivi e passivi che ne definiscono
la/le funzione/i



   iPhone 8
                                          Sistema elettronico

Formato da molti componenti attivi e passivi che ne definiscono
la/le funzione/i
                     Componenti elettronici sempre più
                     - compatti
                     - complessi

   iPhone 15         Il sistema elettronico aumenta le sue prestazioni in termini di
                     - velocità
                     - efficienza energetica
                     - funzionalità
                                   Sistema elettronico

Formato da molti componenti attivi e passivi che ne definiscono
la/le funzione/i




Apple watch
                                                           Definizioni
• Sistemi elettronici à Acquisizione, trasporto, elaborazione di
 segnali elettrici (+ pilotare attuatori)
• Segnale elettrico à Grandezza elettrica che porta
  informazione
Es.: Temperatura (grandezza non elettrica) à sensore di temperatura à segnale
     elettrico che porta l’informazione riguardante la temperatura à circuito
     elettronico che in base all’informazione esegue operazioni (attua)

Gran parte dei circuiti elettronici si basa su dispositivi a semiconduttore

Il corso di Fondamenti di Elettronica introdurrà dispositivi, circuiti
e sistemi a semiconduttore che elaborano segnali elettrici di
natura diversa
Elettronica Analogica       à Segnali analogici
Elettronica Digitale        à Segnali digitali
                               Francesco Driussi - 2024
                      Elettronica Analogica e Digitale
• Segnali analogici à segnali elettrici tempo-varianti che
  assumono una gamma continua di valori
• Segnali digitali à segnali elettrici che assumono solo valori
  discreti

Convertitori A/D e D/A consentono la conversione da segnali analogici a
digitali e viceversa


Elettronica Analogica genera, trasforma, elabora segnali elettrici tempo-
                      varianti e continui (segnali in natura sono continui)
Esempio: segnale sinusoidale à circuito elettronico analogico (AMPLIFICATORE)
         à aumento dell’ampiezza del segnale


Forte legame tra elettronica analogica e sensoristica à interfaccia verso il
mondo esterno che è ANALOGICO !!
                         Elettronica Analogica e Digitale
Elettronica Digitale elabora segnali elettrici a valori discreti
à Tipicamente, rappresentazione binaria dell’informazione (0,1; bit)
(non sempre è così; es.: memorie non volatili, segnali su più livelli discreti per
codificare un numero maggiore di bit)

In elettronica digitale i segnali elaborati sono tipicamente segnali di tensione

Segnali continui per natura à generazione segnale digitale?
          à Fasce di valori associate a significati logici (es.: «0» e «1» logici)


                                                           V(t) > VH : ”1” logico
                                                           V(t) < VL : ”0” logico

                                                           VL < V(t) < VH :
                                                           logicamente indefinito
                                                           à V(t) non deve cadere mai
                                                           in questo range; solo durante
                                                           le transizioni !!
                Elettronica Analogica vs. Digitale
Vantaggi dell’elaborazione digitale:
• maggiore immunità ai disturbi
• minore impatto delle variazioni delle caratteristiche dei
  componenti (per esempio effetti della temperatura, invecchiamento)
• precisione = n. di bit, non precisione sulle grandezze elettriche
• modularità:
   – progettare i diversi blocchi separatamente
   – riutilizzo dei blocchi
   – progettazione automatica con strumenti TCAD, VHDL
   – riduzione del time-to-market

Vantaggi dell’elaborazione analogica à il mondo è «analogico» !
   L’interazione da e verso l’esterno è necessaria
                                           Programma del corso
• Introduzione ai semiconduttori
• Dispositivi elettronici
   - Diodo a giunzione p-n
   - Transistore bipolare (BJT)
   - Transistore ad effetto di campo (MOSFET)
• Elettronica analogica
   - Amplificatori con BJT
   - Amplificatori con MOSFET
   - Analisi statica dei circuiti e studio del punto di lavoro
   - Linearizzazione sistemi elettronici
   - Analisi di piccolo segnale
• Elettronica digitale
   - Figure di merito dei gate digitali
   - Scaling della tecnologia CMOS
   - Caratteristiche statiche e dinamiche dei gate logici CMOS
   - Porte logiche statiche, logiche a pass-transistor, porte logiche dinamiche
                                               Cosa si impara …
• Modelli matematici per la descrizione dei componenti a
  semiconduttore (diodi, transistori bipolari, transistori
  MOSFET)
• Utilizzo dei modelli per analizzare i circuiti con i dispositivi a
  semiconduttore
• Utilizzo dei transistor per la progettazione di
   • semplici amplificatori (analogica)
   • semplici porte logiche (digitale)
• Dimensionamento dei componenti elettronici per definire la
  specifiche di funzionamento dei circuiti analogici e digitali




                          Francesco Driussi - 2024
                                                    Requisiti
• Elettrotecnica di base
   - Leggi di Kirchhoff
• Soluzione di circuiti elettrici lineari
   - Dominio del tempo
   - Dominio della frequenza
   - Trasformate di Laplace e Fourier
   - Funzione di trasferimento
• Diagrammi di Bode




                         Francesco Driussi - 2024
                                                            Modalità d’esame
Esame scritto à Diviso in 2 parti (tot. 3.5 ore):
• Prima: studio di un circuito elettronico analogico (2 ore)
• Dopo: studio di circuiti elettronici digitale (1.5 ore)
Durante la prova scritta non è consentito l'uso di alcun libro e/o supporto didattico. E' consentita la
sola consultazione di un formulario (unico foglio formato A4), in cui lo studente ha facoltà di
includere tutte le equazioni che ritiene utili per lo svolgimento dell'esame.

IL SUPERAMENTO PARZIALE DI UNA SOLA DELLE DUE PROVE SARA’ MEMORIZZATO DAL
DOCENTE E LO STUDENTE AVRA’ LA FACOLTA’ DI SOSTENERE LA SOLA PROVA SCRITTA
MANCANTE NEGLI APPELLI SUCCESSIVI.

Tale superamento di una sola prova, però, verrà memorizzato PER NON PIU’ DI UN ANNO
ACCADEMICO, TRASCORSO IL QUALE LO STUDENTE DOVRA’ RIFARE ENTRAMBE LE
PROVE SCRITTE

Esame orale: si accede solo dopo il superamento di entrambi gli scritti e deve
essere sostenuta preferibilmente nella sessione in cui lo studente ha passato gli scritti
• Domande teoriche sull’analisi dei dispositivi e circuiti elettronici
                                 Supporti alla didattica

Ricevimento previo contatto e.mail: francesco.driussi@uniud.it
Il materiale didattico è disponibile su elearning.uniud.it
Es: testi d’esame appelli passati con soluzione degli esercizi

LIBRI
Elettronica Analogica
• Richard Jaeger, “Microelettronica”, Mc Graw Hill
• Jacob Millmann, “Elettronica di Millmann”, Mc Graw Hill
• P. Calzolari, S. Graffi, “Elementi di Elettronica”, Zanichelli
Elettronica Digitale
• David Esseni, “Fondamenti di circuiti integrati CMOS”, SGE
Ogni testo di elettronica di base può essere valido.
                           Dispositivi a semiconduttore
Gran parte dei circuiti elettronici si basa su dispositivi a semiconduttore
Fondamentali per lo sviluppo e la proliferazione dell’elettronica nell’ultimo
mezzo secolo:
  • minimo ingombro
  • basso consumo
  • ottima affidabilità
  • possibilità di realizzare dispositivi diversi su un unico substrato
  à CIRCUITI INTEGRATI
Intero sistema elettronico su un unico chip:
•   microcontrollori
•   banchi di memorie (volatili e non volatili)
•   sensori integrati
•   trasmettitori/ricevitori per telecomunicazioni (wired e wireless)
•   Display e touch screen
• …
                                              Circuiti integrati
                                                   fili conduttori
                                                   ultra-sottili che
                                                   contattano il chip



                               singolo chip

wafer (substrato) di silicio



         chip “impacchettato” e saldato
         sulla scheda che realizza il
         sistema elettronico completo
                    Il componente fondamentale
Il TRANSISTORE è il blocco fondamentale (“mattoncino”) per
costruire ogni circuito elettronico

   Transistore MOSFET




   Transistore bipolare
                Tecnologia micro e nano elettronica
Negli anni la tecnologia dei semiconduttori ha conosciuto enormi progressi
à ha permesso di fabbricare dispositivi sempre più piccoli e performanti




Il transistor è sempre più piccolo à lunghezze da 10µm a 10nm in 50 anni !
                          Miniaturizzazione e complessità
 La miniaturizzazione («scaling») dei transistor ha consentito di
 aumentare la complessità dei circuiti e abbattere il loro costo




Il transistor è sempre più piccolo à posso realizzarne sempre di più all’interno del chip
           Quanti transistori in un singolo chip?
La miniaturizzazione («scaling») dei transistor ha consentito di
aumentare la complessità dei circuiti e abbattere il loro costo




• Oggigiorno un chip è composto da miliardi di transistori !
• Il loro numero cresce esponenzialmente da 50 anni !
               Quanti transistori in un singolo chip?

                                            intel
                                            i386 (1985)
                                            275000
                                            transistor

1o IC (1961)

                  intel 4004 (1971)
                  2300 transistors



                      intel                NVIDIA’s Kepler
                      pentium               GK110 (2013)
                      (1993)               7,080,000,000
                      3100000                transistors
                      transistor
                           Costo per singolo transistor
• Lo «scaling» e il conseguente aumento del numero di componenti
  nei chip ha permesso di abbattere il costo di fabbricazione del
  singolo transistore
• Oggi 5 milioni di transistori costano meno di un ettogrammo di riso
                      Dimensioni dei wafer di silicio
• I miglioramenti tecnologici hanno consentito di aumentare
  anche le dimensioni dei wafer di silicio
• Molti più chip in un singolo wafer à riduzione del costo del
  singolo chip
                  Complessità e funzioni nei chip
Più transistori nei chip ha consentito di aumentarne la
complessità e di introdurre nuove potenzialità e funzioni



                                    cellulare fine anni ’90
                                    ~10chip + ~100 passivi


                                                            chip RF
                                                            del iPhone
                                                            3G
                                 Performance dei transistor
Lo «scaling» ha migliorato anche la velocità di componenti e circuiti integrati
à transistor sempre più veloci !!                          LG W


                                                                           EOT




                                                              𝑊 1
                                                corrente µ          𝑉!! − 𝑉" #
                                                              𝐿 𝐸𝑂𝑇
                                                              1
                                         frequenza di clock µ ) 𝑉** − 𝑉+
                                                             𝐿
                                       Ultimamente la frequenza di clock non
                                       aumenta più à molto difficile fare
                                       transitor più piccoli e problemi legati
                                       alla potenza dissipata
                                         Limiti allo scaling

                                                      LG


                                                             EOT




          2002      2006     2010
Diventa sempre più difficile ridurre le dimensioni:
• dei costi legati allo sviluppo della tecnologia
• decadimento delle prestazioni dei transitor ultra-corti basati
  su materiali e strutture standard/classiche
                      Introduzione di nuovi materiali
Processi tecnologici enormemente più complessi:
à utilizzo di molti materiali nuovi per la microelettronica
                   Sviluppo di strutture alternative
Architetture di transistore sempre più complicate
à esempio: FinFET (Intel, 2011)




Esplosione dei costi per la fabbricazione:
à costo di una nuova FAB ~ 10B$
                                    Costi di fabbricazione
Processi di fabbricazione complicati anche per interconnettere i
miliardi di transistor à forti sviluppo e costi per le interconnessioni




 Esplosione dei costi per la fabbricazione:
 à costo di una nuova FAB ~ 10B$
                                       Densità complessiva
Già oggi siamo alla saturazione della riduzione delle
dimensioni del transistor (LG) ma miglioriamo la densità
complessiva (half-pitch) à più transistor per singolo chip !




                                 half-pitch
      nanometri




                          node


                  LG
                 Ulteriori booster per l’alta densità

• Secondo le previsioni più
  recenti lo scaling                             previsioni 2016
  geometrico potrebbe
  fermarsi entro poco
• Prossime generazioni di      previsioni 2013
  chip:
à integrazione verticale
                              Limiti legati alla potenza
                               𝑊𝐿       )
• Singolo transistor:   𝑃,-. ∝     𝑓/0 𝑉**
                               𝐸𝑂𝑇

                        𝑃/123    1       )
• Potenza per area:           ∝     𝑓/0 𝑉**
                          𝐴     𝐸𝑂𝑇



                                        I trend di incremento
                                        di frequenza di clock
                                        fck degli anni ‘90 sono
                                        diventati improponibili
                                        negli anni 2000
                             Tensioni di alimentazione
• Senza ridurre VDD non si può aumentare fCK !
• Lo si è fatto in passato, ora non si riesce più !
                𝑃/123    1       )
                      ∝     𝑓/0 𝑉**
                  𝐴     𝐸𝑂𝑇
        VDD ed fCK quasi ferme dal 2002 ad oggi
                               Soluzioni alternative
E’ possible continuare ad aumentare le performance? Si !
Strategie alternative: parallelizzazione
à usare processori con più di un “core”

                                          densità e performance
                                          complessive migliorano


                                           Potenza, clock e
                                           performance del
                                           singolo “core”
                                           sono “fermi”
                Problema dell’energia in elettronica




                           10% of the global energy consumption is due to
                           electronic devices, mostly for ICT and CE.

In 2007 the energy supply of ICT produced
CO2-output at level of 25% of worldwide cars
                Problema dell’energia in elettronica

                            • Potenza dissipata dai data centers:
                              ~30GW (circa 10GW solo negli USA)
                            • 50% per il raffreddamento
                            • una ricerca su google richiede ~1kJ
                            • circa 100k ricerche per secondo
                            • una e.mail di 1 MB = 19 g di CO2 = 1 km
                              in autoà 190 miliardi di e.mail al giorno
                            • consumo medio di uno smart-phone
                              ~50mW (~0.2kJ in 1h)
 batteria AA (stilo) ~      • in Europa si stima che il 10% dei consumi
 2Ah×1.5V= 11 kJ              di energia elettrica nelle case e uffici è
                              dovuta a dispositivi in stand-by !!

Ricerca di dispositivi, sistemi e tecnologie più energeticamente efficienti
Mercato dei semiconduttori
                      Mercato dei semiconduttori




Il mercato dei semiconduttori nel 2022 ha fatturato 600 B$
                Mercato dei semiconduttori




TSMC (solo produzione di chip): 70 B$ in 2023
Mercato dei semiconduttori
             Circuiti integrati Digitali e Analogici




  Micro controllore                     IC per Wi-fi
     (DIGITALE)                       (ANALOGICO)


Le strategie di progetto sono ben specifiche e molto differenti
Costo del design
Tempi di design




            45
                                  Cos’è un transistor?


                             Esempio:
                             à MOS-FET
                             • Metallo/Ossido/Semiconduttore
                             • Transistor ad effetto di campo
                             à Trans-resistore

                                         Attraverso la tensione
      D                                  VGS, si modula la
                IDS   OFF   ON
                                         corrente sul terminale
G         IDS                            di DRAIN (IDS)
                                         à Effetto VALVOLA
VGS
                                   VGS   (elettronica analogica)
      S                VT
                 Cos’è un transistor?


            Esempio:
            à MOS-FET
            • Metallo/Ossido/Semiconduttore
            • Transistor ad effetto di campo


                  Estremizzazione dell’effetto
    D        D    valvola à interruttore
                  controllato in tensione
G       G         Bassa VGS à inter. OFF
                  Alta VGS à interruttore ON
    S             (elettronica digitale)
            S
