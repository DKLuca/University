---
fonte: "testo_17_luglio.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Prova scritta di Fondamenti di Elettronica

                                                         17 luglio 2014

                                                          parte digitale

Nome: . . . . . . . . . . . . . . . .. . . . .Cognome: . . . . . . . . . . . . . . . . . . . . . .Matricola: . . . . . . . . . . . .
Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . ..= . . . . . . . . .
Sia VDD=2V e si assumano i seguenti parametri tecnologici per i MOSFET:
 Parametro                       n-MOSFET               p-MOSFET
 VTO [V]                                0.5                  -0.5
 ’ [A/V2]                            200                    100
  [V1/2]                                 0                      0
  [V-1]                                  0                      0
 LMIN [m]                            0.25                   0.25
 COX [fF/m2]                            10                     10
 CGSO [fF/m]                           1.0                    1.0


Si assuma per tutti i transistori L=LMIN e nel calcolo dei transitori si consideri la transizione
completata al 90% della escursione totale del segnale. Si trascuri il self-loading.
Si risponda ai seguenti quesiti:
     1) (6 punti) Si implementi la funzione logica F=AC+ĀB con un gate statico CMOS facendo uso
        di un invertitore sull’uscita ed assumendo che gli ingressi siano disponibili sia in forma vera
        che in forma negata.
     2) (8 punti) Si assuma che gli nMOS del gate CMOS abbiano Sn=1, mentre i pMOS Sp=2, e si
        dimensioni l’invertitore (mantenendo Sp,inv=Sn,inv) in modo da minimizzare il tempo di ritardo
        di caso peggiore quando l’invertitore pilota un carico CL=100fF. Si assuma che il carico del
        gate CMOS sia solamente la capacità di ingresso del invertitore.
     3) (8 punti) Si calcoli il tempo di ritardo complessivo (invertitore incluso) per ogni combinazione
        dei segnali in ingresso.
     4) (8 punti) Si calcoli la potenza dissipata sulla CL e sulla capacità di ingresso dell’invertitore
        assumendo di lavorare con una frequenza di clock di 300MHz con gli ingressi A e B che
        hanno entrambi eguale probabilità di essere ‘1’ o ‘0’ (cioè PA=PB=0.5) mentre l’ingresso C è
        a ‘1’ con il 30% di probabilità (PC=0.3).
