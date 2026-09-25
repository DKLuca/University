---
fonte: "Simulatore SPICE.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Simulatore circuitale SPICE

                 Francesco Driussi

      Corso di Laurea in Ingegneria Elettronica
Dipartimento Politecnico di Ingegneria ed Architettura


             francesco.driussi@uniud.it
             www.diegm.uniud.it/driussi


                   Francesco Driussi – 2020
                                             Simulatori circuitali
• I simulatori circuitali sono programmi in grado di fare l’analisi a circuiti
  elettrici descritti tramite modelli matematici
• I simulatori circuitali sono basati sui metodi di analisi standard della teoria
  dei circuiti, in particolare il metodo della analisi nodale modificata (MNA) e
  della tabella sparsa (STA)
• La simulazione circuitale è essenziale per la progettazione di circuiti, in
  particolare se di dimensioni medie o grandi.
• Per mezzo degli strumenti di simulazione circuitale, infatti, è possibile
  progettare un circuito elettrico limitando al minimo indispensabile la
  realizzazione di prototipi.
• I simulatori circuitali più conosciuti sono quelli derivati da SPICE acronimo
  di Simulation Program with Integrated Circuit Emphasis.
                                                   Un po’ di storia
SPICE è stato sviluppato dall'Electronics Research Laboratory
dell'Università della California in Berkeley nel 1975
(dal team di Ron Rohrer, tra cui in particolare Larry Nagel e Donald
Peterson)
• Inizialmente sviluppato come un software open source primitivo
• SPICE fu subito largamente utilizzato e distribuito
• Si sono poi susseguite 3 versioni, delle quali l'ultima, SPICE3, risale al
  1985
• Successivamente sono stati sviluppati prodotti commerciali, tra i quali il
  più noto è PSPICE (sviluppato da MicroSim; successivamente acquistata
  da OrCAD)
• OrCAD a sua volta è stata in seguito acquistata da Cadence, la maggiore
  software house per programmi per lo sviluppo di tecnologia micro e nano-
  elettronica (detiene il 70% del mercato)
• Sono stati sviluppati anche spin-off accademici com XSPICE
                            Student version di PSPICE
PSPICE è disponibile in una student version gratuita scaricabile
dimostrando di essere uno studente iscritto ad una università.


https://www.orcad.com/pspice-free-trial


Ci sono anche altre versioni freeware, più o meno complete, a
seconda del sistema operativo utilizzato


Es.: ngspice, LTspice
                                     Struttura dei simulatori
Generalmente i simulatori sono composti da una suite che include diverse
componenti dell’ambiente di simulazione:
•   Editor di schematici: utile a disegnare il circuito e definire i
    componenti (si tratta essenzialmente di un CAD)
•   Generatore di NETLIST: una volta creato lo schema del circuito
    genera una netlist che descrive il circuito in forma testuale e ne fa il
    check elettrico. Eventuali errori di connessione sono segnalati
•   Simulatore SPICE: legge la netlist (dove trova la descrizione del
    circuito) ed esegue la simulazione elettrica richiesta:
     •   Simulazioni DC
     •   Simulazioni AC
     •   Simulazioni di transistorio
•   Programmi di visualizzazione dei risultati: consente di analizzare i
    risultati della simulazione e di creare grafici delle grandezze elettriche
    simulate
