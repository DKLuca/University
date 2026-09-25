---
fonte: "ESERC_PSPICE_2.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

ESERCITAZIONI DI LABORATORIO: SIMULATORE PSPICE

           ANALISI DI PICCOLO SEGNALE E FUNZIONI DI RETE

                                        02/05/2016


1. Disegno di uno stadio amplificatore a doppio carico con l’editor SCHEMATICS,
   secondo lo schema elettrico di Fig.1. Modifica del modello del bipolare con
   l'inserimento della tensione di Early (VAF nel modello PSPICE)
2. Simulazione DC sweep, analisi della caratteristica di uscita (Vo vs. Vin ) e scelta del
   punto di polarizzazione.
3. Simulazione Bias Point Details ed analisi del punto di lavoro. Calcolo dei
   parametri del circuito equivalente ai piccoli segnali del transistore bipolare (rbe, rce).
4. Simulazione AC sweep ed estrazione delle funzioni di rete (resistenza di ingresso,
   resitenza di uscita, amplificazione di tensione). Confronto del valore estratto con i
   valori calcolati attraverso i parametri del circuito equivalente.
5. Inserimento di un carico disaccoppiato attraverso il condensatore C, secondo lo
   schema elettrico di Fig.2.
6. Verifica del punto di polarizzazione.
7. Estrazione dell'amplificazione di tensione e confronto del valore estratto con quello
   calcolato attraverso i parametri del circuito equivalente.




   Download di PSPICE student version: http://ingprj.diegm.uniud.it/labelettronica/


   In Fig.1 e Fig.2:

        Transitore bipolare: QbreakN
        Generatori di tensione Vin e Valim: VSRC
Fig.1
Fig.2
