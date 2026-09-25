---
fonte: "ESERC_PSPICE_1.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

ESERCITAZIONI DI LABORATORIO: SIMULATORE PSPICE

                              TRANSISTORE BIPOLARE

                                       18/04/2016


1. Disegno di uno stadio invertente ad emettitore comune con l’editor SCHEMATICS,
   secondo lo schema elettrico di Fig.1.
2. Simulazione DC sweep ed analisi della tensione di uscita Vout al variare della
   tensione di ingresso Vin (Vin = 0 ÷ 3 V ).Verifica della caratteristica invertente dello
   stadio amplificatore. Studio dell’influenza della resistenza di carico RC sulla
   caratteristica Vin - Vout . (Vdd = 3.0 V)
3. Simulazione del circuito nelle varie regioni di funzionamento del transistore
   bipolare (Interdizione, regione lineare, saturazione) e visualizzazione Bias Point
   Details. Analisi dell’influenza sulle correnti del circuito dei parametri del modello
   del bipolare (es.: βF (BF nel modello di PSPICE)).
4. Simulazione DC sweep e visualizzazione del gummel plot (IC, IB vs. VBE) del
   transistore bipolare. Calcolo e visualizzazione su PROBE dell’ hFE al variare di IC.
5. Disegno di uno specchio di corrente a transistori bipolari con l’editor
   SCHEMATICS, secondo lo schema elettrico di Fig.2.
6. Visualizzazione delle correnti nel circuito (Bias Point Detail) e verifica delle
   caratteristiche dello specchio di corrente. Analisi dell’influenza dei parametri del
   transistore bipolare (es: βF (BF in PSPICE) e Early voltage (VAF in PSPICE)) sul
   funzionamento del circuito.
7. Modifica dello specchio di corrente secondo lo schema di Fig.3.
8. Verifica del miglioramento delle caratteristiche del circuito.


   Download di PSPICE student version: http://ingprj.diegm.uniud.it/labelettronica/


   In Fig.1, Fig.2 e Fig.3:

        Transitore bipolare: QbreakN
        Generatori di tensione V1 e V2: VSRC
Fig.1
Fig.2




Fig.3
