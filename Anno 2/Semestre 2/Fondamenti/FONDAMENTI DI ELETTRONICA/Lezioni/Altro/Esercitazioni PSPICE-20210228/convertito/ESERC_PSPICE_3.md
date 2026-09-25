---
fonte: "ESERC_PSPICE_3.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

ESERCITAZIONI DI LABORATORIO: SIMULATORE PSPICE

          TRANSITORI ED EFFETTI CAPACITIVI SU DIODI E BJT

                                       23/05/2016


1. Disegno del circuito elettrico di Fig.1 con l’editor SCHEMATICS.
2. Applicazione di un impulso rettangolare tramite il generatore VG e simulazione
   Transient. Analisi del transitorio di spegnimento del diodo e studio dell'effetto
   della capacita' non lineare in parallelo al diodo (definita tramite il Transit time: TT
   nel modello PSPICE). Es.: TT=10ns.
3. Calcolo del tempo di storage e verifica sul tracciato temporale. Effetto della
   capacita' di inversione sul transitorio.
4. Disegno di uno stadio invertente ad emettitore comune con l’editor
   SCHEMATICS, secondo lo schema elettrico di Fig.2.
5. Applicazione di un impulso rettangolare tramite il generatore Vin e simulazione
   Transient. Analisi del transitorio di accensione e spegnimento del transistore
   bipolare.
6. Applicazione di un impulso rettangolare e commutazione del transistore bipolare
   tra interdizione e zona lineare. Analisi dell'effetto della capacita' non lineare CBE
   del transistore bipolare (definita tramite il Transit time: TF nel modello PSPICE)
   sul transitorio di accensione e spegnimento. Es.: TF=0.3ns.
7. Applicazione di un impulso rettangolare e commutazione del transistore bipolare
   tra interdizione e saturazione. Analisi dell'effetto della capacita' non lineare CBC del
   transistore bipolare (definita tramite il Transit time: TR nel modello PSPICE) sul
   transitorio di accensione e spegnimento. Es.: TR=50ns.
8. Studio dell'evoluzione temporale di VCE, VBE, IB e IC


   Download di PSPICE student version: http://ingprj.diegm.uniud.it/labelettronica/


   In Fig.1 e Fig.2:

        Diodo: Dbreak
        Transitore bipolare: QbreakN
        Generatore di tensione V2: VSRC
        Generatori VG e Vin: VPULSE
Fig.1




Fig.2
