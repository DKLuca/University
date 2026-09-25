---
fonte: "soluzione_16072018.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                                         16 luglio 2018 parte digitale
1)   Si tratta di una porta logica np-CMOS (dettà anche NORA). Il primo stadio (blocco n) implementa
     la funzione X1=𝐴𝐵 ̅̅̅̅ . Il blocco p fa l’OR dei sui ingressi nerati, quindi F=AB+C.
2)   Il caso peggiore lo si ha quando C=0 e quindi il pMOS controllato da X1 carica CL una volta che X1
     è andato basso (con A=B=1). Questa prima operazione vede 3 nMOS in serie, mentre nel 2° stadio
     abbiamo 2 pMOS in serie. Il ritardo complessivo vale quindi:
             2𝐶𝑥1                      2𝐶𝐿                   2𝐶𝑚1 𝑆𝑥                    2𝐶𝐿
     𝑡𝑝 =       1    𝐹(𝑉𝑇 /𝑉𝑑𝑑 ) +        1    𝐹(𝑉𝑇 /𝑉𝑑𝑑 ) =     1    𝐹(𝑉𝑇 /𝑉𝑑𝑑 ) +              𝐹(𝑉𝑇 /𝑉𝑑𝑑 )
            𝛽′𝑛 3𝑉𝐷𝐷               𝛽′𝑝 𝑆𝑥 2𝑉𝐷𝐷               𝛽′𝑛 3𝑉𝐷𝐷               𝛽′𝑝 𝑆𝑥 12𝑉𝐷𝐷

     dove 𝐶𝑚1 = (𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 + 2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 ) = 1𝑓𝐹 e F=2.2.
     La minimizzazione fornisce

                                                         2𝐶𝐿 𝛽′𝑛/ 𝛽′𝑝
                                                𝑆𝑥 = √                  =11.5
                                                              3𝐶𝑚1

     Segue che 𝐶𝑋1 = 𝑆𝑥 𝐶𝑚1 = 11.5𝑓𝐹
3)   Nel caso in cui F=0, il tempo di valutazione è nullo, dato che iniziamo la fase di valutazione col nodo
     F già a massa.
     Il caso C=0 e A=B=1 è quello di caso peggiore visto sopra, in cui:
                                  2𝐶𝑚1 𝑆𝑥                            2𝐶𝐿
                         𝑡𝑣𝑎𝑙 =               𝐹(𝑉𝑇 /𝑉𝑑𝑑 ) +                   𝐹(𝑉𝑇 /𝑉𝑑𝑑 )=509ps
                                  𝛽′𝑛 13𝑉𝐷𝐷                    𝛽′𝑝 𝑆𝑥 12𝑉𝐷𝐷

     Quando invece A o B (o entrambi) sono a 0 e C=1, abbiamo solo il blocco p che lavora e carica CL
          con 2 pMOS in serie:
                                                    2𝐶
                                      𝑡𝑣𝑎𝑙 = 𝛽′ 𝑆 1𝐿𝑉         𝐹(𝑉𝑇 /𝑉𝑑𝑑 )=254ps
                                                  𝑝 𝑥 2 𝐷𝐷


     Il caso A=B=C=1 è più subdolo: quando il nodo X1 è stato scaricato, CL viene caricata dalla
           combinazione di tutti e 3 i pMOS del pull-up del blocco p. Però all’inizio lavora solo quello
           comandato da 𝐶̅ , che ci mette un tempo pari alla scarica di CL del caso sopra. E’ quindi
           ragionevole assumere 𝑡𝑣𝑎𝑙 =254ps anche in questo caso
4)   La pre-carica di CX1 tramite un pMOS con Sp=1 richiede un tempo
                                                         2𝐶
                                    𝑡𝑝𝑟𝑒−𝑐𝑎𝑟𝑖𝑐𝑎 = 𝛽′ 𝑉𝑋1 𝐹(𝑉𝑇 /𝑉𝑑𝑑 )=170ps
                                                         𝑝 𝐷𝐷


     Mentre la pre-scarica di CL tramite un nMOS con Sn=1 richiede:
                                                         2𝐶
                                   𝑡𝑝𝑟𝑒−𝑠𝑐𝑎𝑟𝑖𝑐𝑎 = 𝛽′ 𝑉𝐿 𝐹(𝑉𝑇 /𝑉𝑑𝑑 )=735ps
                                                          𝑛 𝐷𝐷

5)   Spendiamo energia per caricare sia CL che CX1. CL viene caricata ogni volta che F=1 a seguito della
     scarica nella fase si pre-scarica. CX1 viene caricata nella fase di pre-carica se era stata scaricate nella
     precedente fase di valutazione (cioè se A=B=1) La potenza dissipata vale quindi
                                                2                2
                                       𝑃𝑑 = 𝐶𝐿 𝑉𝐷𝐷 𝑓𝑐𝑘 𝑃𝐹 + 𝐶𝑋1 𝑉𝐷𝐷 𝑓𝑐𝑘 𝑃𝐴 𝑃𝐵 = 52.3𝜇𝑊
     essendo PF=5/8 e PAPB=1/4.
