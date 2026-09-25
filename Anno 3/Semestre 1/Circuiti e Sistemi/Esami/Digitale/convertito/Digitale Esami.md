---
fonte: "Digitale Esami.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Cognome e Nome
                     Matricola
                       Data                          16 Luglio 2008

                 Prova Scritta di Complementi di Elettronica Digitale
                                    16 Luglio 2008
Sia VDD =1.8V e si assumano i seguenti parametri tecnologici per i MOSFET:

                                Parametro       n-MOSFET       p-MOSFET
                                  VT O [V]         0.35           -0.35
                                β ! [µA/V2 ]       270             150
                                LM IN [µm]         0.18            0.18
                               Cox [fF/µm2 ]        13              13
                               CGS0 [fF/µm]        0.6              0.6
                               CJ0 [fF/µm2 ]       3.2              3.2
                                      Keq          0.75            0.75

Se non diversamente specificato si assuma per tutti i transistori L=LM IN e nel calcolo dei
transitori si consideri la transizione completata al 90% della escursione totale del segnale.
                                                 VDD                                 VDD

                          φ                                      φ
                 IN                   N1           N2                    N3


                         φ                                        φ

La figura mostra un circuito di campionamento. Sia i pass-transistor complementari che gli invertitori
hanno dimensionamento Sn =1 ed Sp = ε=βn! /βp! .

  1) (4 Punti). Si indichi, motivando brevemente la risposta, se il circuito è un latch (che campiona a
     livello) oppure un registro (che campiona a fronte). Si specifichi inoltre il livello o il fronte a cui
     avviene il campionamento.
2) (12 Punti). Si calcoli la resistenza equivalente Req dei pass-transistor valutandola nel caso in cui le
   tensioni ai capi del pass-transistor stesso sono VP 1 =0V e VP 2 =VDD . Si determini inoltre il valore
   delle capacità C1 , C2 e C3 ai nodi interni N 1, N 2 ed N 3 del circuito, considerando ad ogni nodo:
   (a) le capacità parassite gate-drain CGD,p e quelle delle giunzioni CSB (o CDB ) dei transistori MOS
   che sono connessi al nodo stesso; (b) le capacità di ingresso degli eventuali invertitori connessi al
   nodo medesimo. Per le capacità delle giunzioni si assuma LSD =2LM IN .
   Si identifichi nel circuito il ritardo che corrisponde al tempo tSU di set-up dell’ingresso e se ne calcoli
   il valore numerico.




3) (6 Punti). Si supponga che il dato IN sia rimasto IN =1 per il tempo tSU prima dell’evento di
   campionamento. Supponiamo inoltre che all’atto del campionamento avvenga una sovrapposizione
   temporanea delle fasi di clock (φ, φ)=(1, 1) e che durante tale sovrapposizione il dato in ingresso
   IN si porti a zero.
   Si calcoli la durata minima t1,1 della sovrapposizione che produce il campionamento sbagliato del
   valore di ingresso IN =0.
                Cognome e Nome
                   Matricola
                     Data                              20 Settembre 2010

                 Prova Scritta di Complementi di Elettronica Digitale
                                  20 Settembre 2010
Sia VDD =1.5V e si assumano i seguenti parametri tecnologici per i MOSFET:

                                   Parametro       n-MOSFET        p-MOSFET
                                     VT O [V]         0.35            -0.35
                                   β ! [µA/V2 ]       120               80
                                     γ[V1/2 ]          0.0              0.0
                                     λ [V−1 ]          0.0              0.0
                                   LM IN [µm]         0.13             0.13

Se non diversamente specificato si assuma per tutti i transistori L=LM IN .
                                                       VDD                 BL
                                     BL

                                           M2                     M5
                                                                       φ
                                            φ                VR
                                                                   M6
                                          M3      VL

                            C BL           M1                     M4            C BL



La figura mostra una cella di memoria RAM statica a sei transistori e la capacità della bit-line vale
CBL =0.1pF . In relazione a tale circuito si chiede di rispondere ai seguenti quesiti.

  1) (12 Punti). Si consideri l’operazione di lettura in cui le due bit-line sono precaricate a VDD ed
     il bit memorizzato è uno zero. Affinché la lettura non deteriori il dato memorizzato è necessario
     che l’aumento di tensione sul nodo VL sia sufficientemente bassa. Questa specifica può essere
     imposta in modo approssimato valutando il valore VLst in condizioni stazionarie, cioè il valore che
     VL raggiungerebbe se il transitorio di lettura fosse infinitamente lungo.
     Detti S1 ed S3 i dimensionamenti di M1 ed M3, rispettivamente, si determini il rapporto CR =S1 /S3
     che garantisce un VLst minore di 0.2V
     Si supponga adesso di avere S3 =1 e S1 =CR S3 e si calcoli il tempo necessario affinché durante la
     lettura la tensione sulla bit-line si riduca di 100mV rispetto a VDD .
2) (6 Punti). Si consideri ora l’operazione di scrittura di uno zero supponendo che il bit memorizzato
   sia un uno. Anche in questo caso si chiede di studiare la scrittura usando la tensione stazionaria
   VLst e, in particolare, di determinare il valore di S2 che garantisce VLst =0.5VDD .




   Si supponga che la cella sia simmetrica e quindi si abbia S1 =S4 , S2 =S5 ed S3 =S6 .

3) (8 Punti). Si calcoli la potenza statica Pst assorbita da una cella di memoria sapendo che la corrente
   Iof f di un dispositivo avente |VGS |<|VT | può essere approssimativamente espressa come:
                                                       !                  "
                                                            |VGS − VT |
                                    Iof f = S Isbth exp −
                                                              ms Vth
   dove S è il dimensionamento del transistore, Isbth =100µA e ms =1.25 sono parametri tecnologici,
   mentre Vth =26mV è la tensione termica (a temperatura ambiente).
   Supponendo inoltre che, a causa delle variabilitå nel processo di fabbricazione, i transistori della
   cella di memoria subiscano una riduzione in valore assoluto della soglia pari a ∆VT =50mV (identica
   per tutti i transistori), si calcoli il nuovo valore della potenza statica Pst .
                  Cognome e Nome
                     Matricola
                       Data                        14 Giugno 2011

                     Prova Scritta di Complementi di Elettronica II
                                         14 Giugno 2011
Sia VDD =1.5V e si assumano i seguenti parametri tecnologici per i MOSFET:

                                Parametro      n-MOSFET      p-MOSFET
                                  VT O [V]        0.35          -0.35
                                     |2ψf |      0.8 [V]       0.8 [V]
                                β ! [µA/V2 ]       180           120
                                  γ[V1/2 ]        0.35           0.35
                                LM IN [µm]        0.12           0.12
                               Cox [fF/µm2 ]        15            15
                               CGS0 [fF/µm]       0.45           0.45
                               CJ0 [fF/µm2 ]       2.8            2.8

Si riportino negli spazi bianchi all’interno del testo l’espressione analitica ed il valore nu-
merico dei risultati.
                                                BL
                                    WL


                               CBL               M1           Vst

                                                        M2



Il circuito in figura rappresenta una cella di memoria RAM dinamica ad un transistore dove la capacità
di memorizzazione è costituita dal terminale di gate del transistore M2. Il transistori M1 ha dimen-
sionamento minimo W =L=LM IN , mentre M2 ha dimensionamento L=LM IN e W =2LM IN . Le bitline
sono costituite da interconnessioni di cui sono noti i seguenti parametri: altezza H=0.12µm, larghezza
W=0.2µm, spessore del dielettrico Tdi =0.09µm e εdi =3.45·10−13 F/cm. Si può assumere per semplicità
che la capacità della bitline sia approssimabile come la sola capacità della interconnessione e che la
lunghezza della bitline sia LBL =50µm.

  1) (8 Punti). Si calcoli la capacità totale CBL della bitline e la capacità di memorizzazione Cst che
     può essere stimata come la capacità di gate del transistore M2.
2) (12 Punti). Supponendo che la word line W L sia polarizzata in scrittura a VDD , si calcoli la tensione
   VST sul nodo di memorizzazione che corrisponde alla scrittura di un ’1’ logico.
   Si calcoli inoltre il tempo di scrittura di un ’1’ logico, considerando esaurito il transitorio al 90%
   della escursione di segnale. Per questo transitorio si assuma che la tensione di soglia di M1 sia
   quella che corrisponde al valore finale della tensione VST .




3) (10 Punti). Si supponga adesso che la corrente Iof f di un MOSFET avente |VGS |<|VT | si possa
   esprimere come:                                  !               "
                                                        |VGS − VT |
                                 Iof f = S Isbth exp −
                                                          ms Vth
   dove S=W/LM IN è il dimensionamento del transistore, Isbth =0.6µA e ms =1.2 sono parametri
   tecnologici, mentre Vth =26mV è la tensione termica (a temperatura ambiente).
   Si indichi quale transistore è responsabile, a causa della sua Iof f , del degrado della tensione VST
   sul nodo di memorizzazione e si calcoli il valore di VST quando è trascorso un tempo tret =18µs
   dalla fine dell’operazione di scrittura di un ’1’ logico.
               Cognome e Nome
                  Matricola
                    Data                       12 Settembre 2008

                Prova Scritta di Complementi di Elettronica Digitale
                                 12 Settembre 2008
Sia VDD =1.8V e si assumano i seguenti parametri tecnologici per i MOSFET:

                              Parametro      n-MOSFET      p-MOSFET
                                VT O [V]        0.35          -0.35
                              Ø 0 [µA/V2 ]      270            150
                              LM IN [µm]        0.18           0.18
                             Cox [fF/µm2 ]       13             13
                             CGS0 [fF/µm]        0.6           0.6
                             CJ0 [fF/µm2 ]       3.2           3.2
                                    Keq         0.75           0.75

Se non diversamente specificato si assuma per tutti i transistori L=LM IN e nel calcolo dei
transitori si consideri la transizione completata al 90% della escursione totale del segnale.

  1) (4 Punti). Si disegni schematicamente una cella di memoria a floating gate indicando chiaramente
     le capacità CG , CS , CD e CB fra il floating gate ed i quattro terminali accessibili.
     Si indichi inoltre l’espressione dei coeﬃcienti di accoppiamento capacitivo ÆG ed ÆD in funzione
     delle capacità CG , CS , CD e CB e si calcolino i valori numerici di ÆG ed ÆD per CG =0.6f F ,
     CD =CS =0.15f F e CB =0.1f F .
2) (10 Punti). Si indichi la relazione che lega la soglia VT della cella di memoria alla soglia VT,T R del
   cosiddetto transistore equivalente (il cui gate è il floating gate della cella stessa) ed alla carica QF G
   immagazzinata nel floating gate.
   Assumendo VT,T R =0.7V , si calcoli il valore della soglia VT 0 della cella per QF G =0 e la carica QF G,4V
   necessaria per avere un aumento di soglia pari a 4V (rispetto a VT 0 ).




3) (8 Punti). Si supponga che la corrente di gate IG durante la scrittura della cella sia una funzione
   esponenzialmente decrescente nel tempo secondo l’espressione

                          IG (t) = ° IG0 e°t/t0   con      IG0 = 3nA        t0 = 0.9µs

   Si scriva l’espressione della tensione di soglia VT (t) in funzione del tempo e si calcoli il tempo tpr
   necessario per avere un aumento di soglia pari a 4V .




4) (8 Punti, da svolgere su foglio separato) Si descriva il modello circuitale per il pilotaggio di
   linee di trasmissione senza perdite con impedenza caratteristica z0 chiarendo l’equivalente circuitale
   alla sorgente, al carico ed alla generica sezione della linea.
   Una volta definiti i coeﬃcienti di riflessione alla sorgente ΩS ed al carico ΩL , si descriva come puó
   essere usato il metodo dei diagrammi a reticolo per calcolare la forma d’onda al carico ed alla
   sorgente per generici valori della resistenza RS di sorgente e RL .
   Infine si mostrino le forme d’onda relative al caso di adattamento alla sorgente ed al carico indicando
   quale condizione è necessaria per ottenere i suddetti adattamenti.
                 Cognome e Nome
                    Matricola
                      Data                           28 Settembre 2006



                              Prova Scritta di Elettronica Digitale
                                           28 Settembre 2006
Se non diversamente specificato si assuma per tutti i transistori L=LM IN .
Si riportino negli spazi bianchi all’interno del testo l’espressione analitica e, quando richiesto,
il valore numerico dei risultati.
In figura é riportato un albero costituito da interconnessioni di tipo RC. La sezione delle interconnessioni
ha una altezza H=0.4µm ed una larghezza W=1.0µm. Lo spessore del dielettrico vale Tox =0.2µm ed
il dielettrico é semplice SiO2 con costante dielettrica assoluta "ox =3.45·10°13 F/cm. La resistivitá del
materiale con cui é fabbricata la interconnessione vale Ω= 6 £ 10°4 [Ohm · cm].
    La lunghezza dei tre rami di interconnessione é indicata in figura, le capacitá al termine dei rami sono
CA =70f F e CB =100f F ed il driver a dimensionamento minimo ha resistenza equivalente RDR =1.8kΩ e
capacitá di ingresso CDR =6f F .

                                                            A
                     W
                                                                           CA
                                                    40um
            H
                                      Driver                     A’
                                 IN                                                            B
           Tox
                                                   40um                   80um                     CB
                                                                B’


  1) (10 Punti). Si calcolino la capacitá per unitá di lunghezza c e la resistenza per unitá di lunghezza
     r della linea di interconnessione.
      Si supponga inoltre di sostituire ogni tratto di interconnessione di lunghezza pari a 40µm con una
      cella a parametri concentrati di tipo Π. Si calcoli la resistenza Rº e la capacitá Cº delle celle a Π e si
      disegni il circuito che descrive il driver (a dimensionamento minimo) e l’albero di interconnessione.
      Si calcoli infine la costante di tempo dominante al nodo B secondo la regola di Elmore.
2) (8 Punti). Supponendo di inserire un buﬀer alla sezione A0 immediatamente all’inizio del ramo
   che porta al nodo A (ma non sul ramo che porta a B), si calcoli di nuovo la costante di tempo
   dominante al nodo B. A tal scopo si assuma che sia il buﬀer di ingresso che quello alla sezione A0
   siano a dimensionamento minimo.




3) (8 Punti). Si supponga adesso di inserire un buﬀer anche alla sezione B 0 che porta al nodo B ed
   un secondo buﬀer sul ramo B per spezzare il ramo stesso in due tratti lunghi 40µm.
   Detto h il dimensionamento dei buﬀer del circuito (identico per tutti i buﬀer), si chiede di deter-
   minare il valore di h che minimizza il ritardo al nodo B e di calcolare la corrispondente costante di
   tempo dominante al nodo B.
                   Cognome e Nome
                      Matricola
                        Data                           21 Luglio 2015



                      Prova Scritta di Complementi di Elettronica II
                                                21 Luglio 2015
   Si assumano i seguenti parametri tecnologici per i MOSFET:

                                 Parametro       n-MOSFET        p-MOSFET
                                   LM IN            45[nm]          45[nm]
                                     β!           90 [µA/V2 ]     70 [µA/V2 ]
                                    Cox          11 [fF/µm2 ]    11 [fF/µm2 ]
                                   CGS0          0.5 [fF/µm]     0.5 [fF/µm]
                                    Cj0          1.9 [fF/µm2 ]   1.9 [fF/µm2 ]
                                    Keq               0.55            0.55

Si riportino negli spazi bianchi all’interno del testo l’espressione analitica e, quando richiesto,
il valore numerico dei risultati.
In figura si mostra un gate CMOS che deve essere dimensionato in modo che il tempo di salita di caso
peggiore sia uguale al tempo di discesa di caso peggiore. La tecnologia CMOS di fabbricazione ha un
ritardo caratteristico tp0 =13ps.

                              VDD

                                            B
                       A
                                            C
                                                F(A,B,C)
                                                                        A
                                    A                                   B        G1
                                                                        C
                       C                B




  1) (8 Punti). Si determini la funzione logica G1 realizzata dal gate. In base ai parametri tecnologici
     riportati in tabella, si determini il parasitic effort pinv dell’invertitore supponendo che la lunghezza
     delle regioni di source e drain sia LS =2LM IN . Si calcoli inoltre il logical effort gG1 ed il parasitic
     effort pG1 del gate G1.
         Soluzione della Prova Scritta di Complementi di Elettronica II
                                            21 Luglio 2015
1) Analizzando il pull-down del gate in figura è evidente che la funzione logica realizzata dal gate è
   G1=A(B + C)=A + (B + C).
   Noti i parametri tecnologici, il parasitic effort dell’invertitore vale:

                                           LM IN (2CGS0 + LS Cj0 Keq )
                                  Pinv =                               ! 0.73
                                            L2M IN Cox + 2LM IN CGS0

   Indichiamo con Sn ed Sp i dimensionamenti dei transistori n-MOS e p-MOS del gate G1. Nel tran-
   sitorio di discesa di caso peggiore il dimensionamento equivalente del pull-down vale Sn,eq =Sn /2 ed
   il dimensionamento del pull-up nella salita di caso peggiore vale Sp,eq =Sp /2. Affinché i tempi di
   salita e discesa di caso peggiore siano uguali dobbiamo quindi avere Sp /Sn =ε con ε=βn! /βp! =1.286.
   Per uguagliare il ritardo di caso peggiore del gate G1 ad un invertitore con dimensionamento
   Sinv è necessario Sn =2Sinv . Dunque, quando Sn vale 2Sinv , la capacità di ingresso di G1 vale
   CG1 =2Sinv (1 + ε)CM 1 . Inoltre al nodo di uscita sono connessi due transistori p-MOS con dimen-
   sionamento Sp =2εSinv ed un n-MOS con dimensionamento Sp =2Sinv .
   Le precedenti considerazioni consentono di calcolare il logical e parasitic effort di G1 come:

                2Sinv (1 + ε)CM 1                          2Sp + Sn           (2 · 2ε + 2)Sinv
        gG1 =                     =2              pG1 =                pinv =                  pinv = 2.29
                 Sinv (1 + ε)CM 1                         Sinv (1 + ε)          (1 + ε)Sinv

2) Il circuito in figura realizza la funzione logica richiesta usando il gate G1:
                              A
                              B      G1                                P
                              C              D
                                            E                              CL


   Per calcolare il path-effort F del circuito complessivo sono necessari il logical effort di tutti i gate.
   Per il gate NOR:
                                        1 + 3ε
                                gnor3 =        = 2.125 pnor3 = 3 pinv = 2.20
                                         1+ε
   La capacità di ingresso di G1 si esprime come CG1 =SnG1 (1 + ε)CM 1 , dove SnG1 indica il dimen-
   sionamento del transistore n-MOS e CM 1 =0.067f F . Per SnG1 =2 abbiamo CG1 !0.308fF.
   Nota la capacità di ingresso di G1 e quella di carico CL =1.1f F , possiamo calcolare il path effort
   come:
                                                            CL
                                      F = G H = gG1 gnor3       ! 15.2
                                                           CG1
                                                                      √
3) Siccome il circuito ha due stadi avremo uno stage effort ottimo fˆ= 2 F =3.90 e la capacità di ingresso
   del NOR può essere calcolata come:
                                                     gnor3 CL
                                           Cnor3 =            ! 0.60f F
                                                        fˆ

   Il ritardo del circuito ottimizzato risulta:
                                       !                     "
                              tp = tp0 2 fˆ + pG1 + pnor3 = 12.28 tp0 ! 160ps.
                  Cognome e Nome
                     Matricola
                       Data                          1 settembre 2016



                              Prova Scritta di Elettronica Digitale
                                           1 settembre 2016

Si consideri una tecnologia CMOS i cui gate devono avere tempi di salita e discesa simmetrici e per la quale
sono note le conducibilità intrinseche dei transistori n-MOS e p-MOS βn! =150µA/V 2 e βp! =75µA/V 2 , la
capacità di gate del transistore a dimensionamento minimo CM 1 =0.75fF ed il parasitic effort pinv =0.95
dell’invertitore. La tensione di soglia per i transistori n-MOS e p-MOS vale in modulo VT =0.25V e la
tensione di alimentazione è VDD =1.0V.
    In riferimento a tale tecnologia si consideri un NAND a 2 ingressi ed una linea di trasmissione pratica-
mente senza perdite caratterizzata da una capacità per unità di lunghezza c=4f F/µm e da un’induttanza
per unità di lunghezza l=0.144nH/µm. La lunghezza della linea è Len=120µm e la capacità di carico a
valle della linea è molto minore rispetto a quella della linea stessa.

In relazione al circuito in oggetto si risponda ai seguenti quesiti:

  1) (Punti 10) Si calcoli l’impedenza caratteristica z0 della linea di trasmissione e la resistenza equiva-
     lente del NAND ai fini del pilotaggio della linea sapendo che i transistori nel pull-down del NAND
     hanno dimensinamento Sn,nand =2. Si determini inoltre il coefficiente di riflessione ρS alla sorgente
     che si realizzerebbe pilotando la linea direttamente col NAND e si commenti sull’opportunità di
     questa tecnica di pilotaggio.
2) (Punti 20) Si supponga di potere inserire a valle nel NAND degli invertitori allo scopo di ottimizzare
   il pilotaggio della linea di interconnessione. Si determini il numero ottimo di tali invertitori che
   minimizza il ritardo, il dimensionamento degli invertitori ed il ritardo complessivo del circuito.
                   Soluzione della Prova Scritta di Elettronica Digitale
                                            1 settembre 2016
                                                  !                                           √
1) La impedenza caratteristica della linea è z0 = l/c=190Ω ed il tempo di volo vale tf l =Len lc=91.2ps.
La resistenza equivalente del gate NAND per la transizione di salita può essere calcolata come

                                               2F (VT 0 /VDD )
                                  Rnand =                         = 12776Ω
                                            2.3 · Sp,nand βp! VDD

dove Sp,nand =2 è il dimensionamento fisico (e anche dimensionamento equivalente) del pull-up del NAND.
Nella precedente espressione si è tenuto conto che, indicata con RLE la resistenza equivalente del gate
per il metodo del logical effort, la resistenza equivalente del driver ai fini del pilotaggio della linea vale
(RLE /2.3). Il coefficiente di riflessione alla sorgente risulta quindi

                                                Rnand − z0
                                         ρS =              # 0.97 .
                                                Rnand − z0
L’ipotesi di pilotare la linea di trasmissione direttamente col gate NAND non rappresenta una pessima
prassi di progetto, infatti la Rnand è troppo grande rispetto alla z0 della linea e questo si traduce in un
transitorio molto lento all’uscita della linea.

2) Per pilotare la linea in modo da minimizzare il tempo di assestamento tstl è opportuno pilotarla con
un invertitore (che chiameremo B1) dimensionato per avere una resistenza equivalente pari a z0 . A tal
fine imponiamo
                                             2F (VT 0 /VDD )
                                     RB1 =                    = z0
                                            2.3 · SB1 βp! VDD
dove SB1 è il dimensionamento del transistore n-MOS dell’invertitore B1. Dalla precedente relazione
otteniamo SB1 #67, a cui corrisponde una capacità di ingresso CB1 =150.7fF.
    Consideriamo adesso il circuito che deve pilotare B1 e valutiamo quanti invertitori inserire sulla
base della metodolgia del logical effort. Il path effort del circuito risulta F =gnand CB1 /Cnand =67, dove i
parametri del gate NAND sono
                                2+ε
                     gnand2 =       = 1.33      Cnand = (Sn,nand + Sp,nand )CM 1 = 3f F
                                1+ε
Lo stage effort ottimo della tecnologia ed il numero ottimo degli stadi per pilotare CB1 sono

                                                                        ln(F )
                          ρ # 2.82 + 0.71pinv # 3.49             N̂ =          = 3.36
                                                                        ln(ρ)

che approssimiamo con N=3. Lo stage effort ottimo è fˆ = F 1/3 = 4.06 e dobbiamo aggiungere due
invertitori fra il NAND e B1. Le capacità di ingresso di tali invertitori sono CB2 =(CB1 /fˆ)=37.1fF e
CB3 =(CB2 /fˆ)=9.1fF. In questo caso il tempo di assestamento della linea è pari a tf l , pertanto il ritardo
complessivo dall’ingresso del NAND all’uscita della linea risulta

                                 tp = tp0 (3fˆ + 2pinv + 2pinv ) + tf l # 549ps

dove tp0 =(Rinv1 Cinv1 )=66.1ps ed il parasitic effort del NAND vale 2pinv .
                    Cognome e Nome
                       Matricola
                         Data                          4 Luglio 2007

                       Prova Scritta di Complementi di Elettronica II
                                              4 Luglio 2007
   Sia VDD =1.8V e si assumano i seguenti parametri tecnologici per i MOSFET:

                                  Parametro     n-MOSFET        p-MOSFET
                                    VT O           0.4 [V]         -0.4 [V]
                                      Ø0        400 [µA/V2 ]    250 [µA/V2 ]
                                      ∏               0                0
                                     Cox        13 [fF/µm2 ]    13 [fF/µm2 ]
                                    CGS0        0.7 [fF/µm]     0.7 [fF/µm]
                                     Cj0         5 [fF/µm2 ]     5 [fF/µm2 ]
                                    LM IN         0.18[µm]        0.18[µm]

Se non diversamente specificato si assuma per tutti i transistori L=LM IN . Si riportino
negli spazi bianchi all’interno del testo l’espressione analitica e, quando richiesto, il valore
numerico dei risultati.
In figura si mostra il circuito di pilotaggio di una linea senza perdite, per la quale sono noti i parametri per
unità di lunghezza c=0.2fF/µm ed l=4.5pH/µm. La lunghezza della linea vale Len =8mm e la impedenza
di carico a valle della linea può essere considerata praticamente infinita. Gli invertitori di pilotaggio sono
ottenuti per mezzo di una tecnologia CMOS i cui parametri sono riportati in tabella.



          IN                                                                                  O2
                   1                            I1
                                                         B1


  1) (6 Punti). Si calcoli il ritardo caratteristico tp0 della tecnologia CMOS in esame e la resistenza
     Rdr con cui si può schematizzare l’invertitore a dimensionamento minimo ai fini del pilotaggio della
     linea. A tal scopo si definisca la Rdr come il rapporto fra la tensione VDSAT a cui il transistore
     nMOS entra in saturazione e la corrente stessa Isat di saturazione.
   Nel seguito dell’analisi si puó, per semplicità , trascurare nel computo dei ritardi le capacità parassite
   prodotte sul nodo di uscita dell’invertitore dagli stessi transistori che lo costituiscono.

2) (10 Punti). Si dimensioni l’invertitore B1 che pilota la linea in modo da minimizzare il settling
   time sull’uscita O2, dove il settling time è definito come il ritardo fra una transizione del segnale
   I1 e l’istante dopo il quale la tensione al nodo O2 si mantiene entro il 5% del suo valore finale.
   Si determini inoltre il numero ed il dimensionamento degli invertitori che minimizzano il ritardo
   del circuito. Si calcoli quindi il valore numerico del ritardo complessivo da una transizione di IN
   all’esaurimento del settling time al nodo O2.




3) (10 Punti) Si supponga che, a causa di imperfezioni nel processo di fabbricazione, i dimensionamenti
   dei MOSFETs dell’invertitore B1 risultino maggiorati del 20% rispetto al valore ottimo determinato
   al punto precedente, e che, inoltre, le tensioni di soglia di B1 siano VT n =|VT p |=0.2V , anzichè il
   valore nominale di 0.4V .
   Si determini il settling time che corrisponde alla versione eﬀettivamente realizzata dell’invertitore
   B1 ed il ritardo complessivo da una transizione di IN all’esaurimento del settling time al nodo O2.
         Soluzione della Prova Scritta di Complementi di Elettronica II
                                             4 Luglio 2004
1) Per l’Inverter ad area minima la capacità di ingresso risulta Cinv1 = (1+")(Cox L2M IN +2LM IN CGS0 ) =
   1.75f F ed il ritardo caratteristico della tecnologia è quello di un invertitore che vede come unico
   carico la propria capacitådi ingresso:
                                             2Cinv1 F (VT /VDD )
                                     tp0 =                       ' 10.1[ps]
                                                  Øn0 VDD
   dove il valore di F (VT /VDD ) è pari a circa 2.09.
   La resistenza dell’invertitore a dimensionamento minimo può essere determinata come:
                           VDSAT             2                       2
                   Rdr =         =                     =                          = 3.57kΩ
                            Isat   1 · Øn0 (VDD ° VT )   1 · 4 · 10°4 (1.8 ° 0.4)
                                                                  p
2) La linea in esame ha un’impedenza
                               p          caratteristica z0 = l/c = 150Ω ed un tempo di volo tf l =
   z0 cLen = lLen/z0 = Len lc = 240ps. Quindi il dimensionamento di B1 che minimizza il set-
   tling time è quello che rende la resistenza equivalente RB1 dell’invertitore pari appunto a 150Ω.
   Dall’espressione di RB1 :
                        VDSAT             2                        2
                RB1 =         =                      =                          = 150Ω
                         Isat   SB1 · Øn (VDD ° VT )
                                       0               SB1 · 4 · 10 (1.8 ° 0.4)
                                                                   °4

   si ricava che il dimensionamento necessario è SB1 '24. In tal caso il settling time della linea coincide
   col tempo di volo tf l =240ps.
   Se trascuriamo nel calcolo dei ritardi degli invertitori il parasitic eﬀort, come suggerito dal testo, il
   numero ottimo di invertitori necessari per pilotare B1 risulta N̂ =ln(CB1 /C1 )=ln(24)=3.18, inoltre
   il corrispondente dimensionamento progressivo dovrebbe essere pari ad e ' 2.718. Nel seguito si
   decide di usare tre stadi con dimensionamento progressivo pari a 3. Quindi i tre invertitori che
   precedono B1 saranno dimensionati 1, 3, 9 (includendo l’invertitore iniziale). Il ritardo relativo agli
   invertitori è quindi:
                                    tinv = (3 + 3 + 24/9) tp0 ' 87.5[ps]

   Il tempo complessivo di propagazione da IN a O2 risulta quindi:

                                              tinv + tf l ' 327.5[ps]

3) A causa delle variazioni dei parametri di B1 in sede di fabbricazione, il valore della sua resistenza
   equivalente diventa:
                                   VDSAT                   2
                           RB1 =         =                                 = 108.5kΩ
                                    Isat   1.2 · 24 · 4 · 10°4 (1.8 ° 0.2)
   invece del valore nominale 150Ω. Questo abbassamento della RB1 produce un coeﬃciente di rifles-
   sione alla sorgente:
                                                 RB1 ° z0
                                            ΩS =            = °0.16
                                                 RB1 + z0
   Usando i diagrammi a reticolo vediamo che all’istante iniziale l’invertitore B1 riesce ad iniettare
   in linea una frazione z0 /(RB1 + z0 )'0.58 della VDD . Inoltre il settling time si allunga a tre tempi
   di volo tf l , in base alla definizione data nel testo. L’aumento del dimensionamento di B1 ha un
   modesto eﬀetto anche sul ritardo degli invertitori in cascata:

                                   tinv = (3 + 3 + (1.2 · 24)/9) tp0 ' 93[ps]

   ed il ritardo complessivo da IN a O2 risulta quindi pari a:

                                              tinv + 3 tf l ' 813[ps]
                   Cognome e Nome
                      Matricola
                        Data                         13 Luglio 2004


                              Prova Scritta di Elettronica Digitale
                                            13 Luglio 2004
Se non diversamente specificato si assuma per tutti i transistori L=LM IN .
Si riportino negli spazi bianchi all’interno del testo l’espressione analitica e, quando richiesto,
il valore numerico dei risultati.
In figura é riportato un albero costituito da interconnessioni di tipo RC. La sezione delle interconnessioni
ha una altezza H=0.3µm ed una larghezza W=0.35µm. Lo spessore del dielettrico vale Tox =0.15µm ed
il dielettrico é semplice SiO2 con costante dielettrica assoluta "ox =3.45·10°13 F/cm. La resistivitá del
materiale con cui é fabbricata la interconnessione vale Ω= 4 £ 10°4 [Ohm · cm].

                                                            A
                                W
                                                                         C2

                         H
                                             IN            A’                  C
                        Tox
                                                           B’   C’                 C1
                                                       L


                                                            B
                                                                 C2



  1) (6 Punti). Si calcolino la capacitá per unitá di lunghezza c e la resistenza per unitá di lunghezza r
     della linea di interconnessione.




     Si assuma che i quattro rami dell’albero di interconnessioni abbiano tutti la medesima lunghezza
     L=30µm e che le capacitá da pilotare siano C1 =60f F al nodo C e C2 =150f F ai nodi A e B. Inoltre,
     in quanto segue, i ritardi della rete ad albero saranno trattati semplificando le interconnessioni con
2) (8 Punti). Si calcolino i valori RT e CT che corrispondono ad una singola cella a T che schematizza un
   ramo di interconnessione di lunghezza L. Si disegni quindi il circuito RC risultante dalla sostituzione
   della cella a T ad ognuno dei quattro rami di interconnessione e si calcoli la costante di tempo
   dominante al nodo C.




   Si supponga adesso di disporre di Buﬀer descritti da un semplice modello lineare caratterizzato da
   una resistenza equivalente R0 = 1500Ohm e da una capacitá di ingresso C0 =12f F .

3) (6 Punti). Suppondendo di inserire due Buﬀer alle sezioni A0 e B 0 immediatamente all’inizio dei
   rami che portano ai nodi A e B (ma non sul ramo che porta a C), si calcoli di nuovo la costante di
   tempo dominante al nodo C.




4) (6 Punti). Si ripeta il calcolo del punto precedente considerando il Buﬀer anche alla sezione C 0
   immediatamente all’inizio del ramo che porta a C.
                  Cognome e Nome
                     Matricola
                       Data                          26 Gennaio 2016

                      Prova Scritta di Complementi di Elettronica II
                                           26 Gennaio 2016
Sia VDD =1.1V e si assumano i seguenti parametri tecnologici per i MOSFET:

                                 Parametro       n-MOSFET         p-MOSFET
                                   VT O [V]         0.3              -0.3
                                 β ! [µA/V2 ]       120              100
                                   γ[V1/2 ]         0.0               0.0
                                 LM IN [µm]         0.09             0.09
                                Cox [fF/µm2 ]        12               12
                                CGS0 [fF/µm]        0.35             0.35

Si riportino negli spazi bianchi all’interno del testo l’espressione analitica ed il valore nu-
merico dei risultati.
                                 BL1                    BL2
                                 WWL

                              RWL

                                                             M3

                             CBL           M1        X                     CBL
                                                            M2
                                                Cs


Il circuito in figura rappresenta una cella di memoria RAM dinamica a tre transistori ed i transistori
M1 ed M3 hanno dimensionamento minimo W =L=LM IN , mentre M2 ha dimensionamento L2 =2LM IN
e W2 =4LM IN .

  1) (8 Punti). Si calcoli la capacità di memorizzazione CS costituita dalla capacità di gate del transistore
     M2. Inoltre, supponendo che sia possibile polarizzare la word line di scrittura W W L ad una tensione
     maggiore di VDD , si determini la minima tensione VW W L della W W L che garantisce una tensione
     VX =VDD sul nodo X nel caso di scrittura di un 1 logico.
     Usando il valore di VW W L appena trovato, si calcoli il tempo di scrittura di un 1 logico, considerando
     esaurito il transitorio al nodo X al 90% della escursione di segnale.
1) (8 Punti). Si esamini adesso l’operazione di lettura supponendo che la tensione VRW L sulla bitline di
   lettura sia VRW L =VDD , che la capacità della bitline sia CBL =0.2pF e che la bitline sia inizialmente
   precaricata alla tensione VDD . Si determini il tempo necessario affiché la tensioni sulla bitline si
   riduca del 10% supponendo che nella cella di memoria sia memorizzato un 1 logico.




3) (8 Punti). Si supponga adesso che la corrente Iof f di un MOSFET avente |VGS |<|VT | si possa
   esprimere come:                                  !              "
                                                       |VGS − VT |
                                 Iof f = S Isbth exp −
                                                         ms Vth
   dove S=W/LM IN è il dimensionamento del transistore, Isbth =100nA e ms =1.2 sono parametri
   tecnologici, mentre Vth =26LmV è la tensione termica (a temperatura ambiente).
   Si consideri una fase di ritenzione in cui il nodo X è caricato a VDD , mentre la BL1 e la WWL
   sono polarizzate a massa. Si indichi quale transistore è responsabile, a causa della sua Iof f , del
   degrado della tensione sul nodo X e si calcoli il tempo necessario affiché la tensione VDD sul nodo
   X si degradi del 30%.
          Soluzione della Prova Scritta di Complementi di Elettronica II
                                            26 Gennaio 2016
1) La capacità di memorizzazione CS può essere stimata in base alla lunghezza e larghezza di M2 e
   risulta CS =AG Cox + 2W2 CGS0 !1.03 fF, dove AG =(2LM IN )(4LM IN ) è l’area di gate. Si noti che,
   siccome M2 non ha dimensionamento minimo, non è possibile usare le espressioni della capacità
   di gate in termini di CM 1 .
   Affinché il nodo X raggiunga VDD nel caso di scrittura di un 1 logico, è necessario che il transistore
   M1 rimanga acceso fino a VX =VDD , quindi la tensione VW W L sulla W W L deve essere pari a
   VDD +VT n0 =1.4, dove si è usato VT n0 per la soglia di M1 perché si ha γ=0 nella tabella dei parametri
   dei transistori.
   Durante la scrittura di un 1 logico avremo quindi la bitline polarizzata a VDD e la W W L polarizzata
   a VDD +VT n0 =2.15, mentre VX rappresenta la tensione di source del transistore M1, attraverso il
   quale il nodo X viene appunto caricato.
   Siccome per il transistore M1 si ha VD =VG −VT n , allora il transistor lavora alla soglia della satu-
   razione durante il transitorio. La tensione Vx (t) è quindi governata dall’equazione differenziale

                                            1 · βn!                              dVX
                             IDS (M 1) =            (VW W L − Vx − VT n0 )2 = CS     .
                                               2                                  dt
   L’equazione si integra facilmente per separazione di variabili e si ottiene un tempo di salita tr
   corrispondente al valore finale VX,f in della tensione al nodo X
                                       !                                             "
                                2CS                    1                  1
                            tr = !                                 −
                                 βn        VW W L − VX,f in − VT n0 VW W L − VT n0

   Sostituendo il valore di VX,f in =0.9VDD , che corrisponde al 90% della escursione di segnale, otteni-
   amo tr !140ps.

2) Durante l’operazione di lettura in esame i transistori M2 ed M3 hanno praticamente la stessa
   tensione di gate VGS =VDD e pertanto possono essere considerati in serie ai fini della descrizione
   del transitorio. Nel piccolo intervallo di tensioni VBL sulla bitline fra VDD e 0.9VDD la serie dei
   transistori lavora in saturazione, pertanto il transitorio è del tutto assimilabile al transitorio di
   discesa di un gate CMOS nel tratto in cui i transistori lavorano in regime di saturazione. Si tratta
   di un semplice transitorio a corrente costante ed il tempo di discesa può essere espresso come

                                                   2CBL (VDD − 0.9VDD )
                                            tf =
                                                    Seq βn! (VDD − VT 0 )2

   dove Seq indica il dimensionamento equivalente della serie dei transistori M2 ed M3 e vale Seq
   =(1/S2 + 1/S3 )−1 , con S2 =2 ed S3 =1. Sostituendo i valori numerici si ottiene tf !859ps.

3) Durante la fase di ritenzione è il transistore M1 che, a causa della sua Iof f , può scaricare la capacità
   CS di immagazzinamento dell’informazione. Si supponga che sul nodo X abbiamo memorizzato la
   tensione VDD e che sia la BL1 che la WWL siano polarizzate a massa. In questo caso M1 ha una
   VDS pari all’intera VDD (quando VX =VDD ), mentre ha VGS =0. In tali condizioni la sua corrente
   di sotto-soglia vale                               #          $
                                                           VT n0
                                   Iof f = S Isbth exp −           = 6.67pA
                                                          ms Vth
   La scarica della capacità CS avviene con una corrente Iof f costante, almeno fino a quando risulta
   VDS maggiore di tre o quattro volte Vth =26mV , quindi il tempo di degrado della tensione VX si
   trova dividendo semplicemente la variazione di carica per la corrente di perdita. Otteniamo in
   questo modo
                                               0.3CS VDD
                                        t30% =            = 51µs
                                                  Iof f
                     Prova Scritta di Circuiti e Sistemi Elettronici
                                            (DIGITALE)
                                           10 Maggio 2021

   Se non diversamente specificato si assuma per tutti i transistori L = LMIN e i tempi
di salita e di discesa di caso peggiore dei singoli gate logici simmetrici. La tensione di
alimentazione è VDD =1.5V.

                                Parameter       n-MOS     p-MOS

                                Vth [V]          0.30       -0.30
                                 0 [µA/V2 ]       300        150
                                LMIN [µm]        0.100      0.100
                                Cox [fF/µm2 ]     10         10
                                CGS0 [fF/µm]      0.5        0.5
                                Cj0 [fF/µm2 ]     3.0        3.0
                                Keq               0.8        0.8
                                  [V 1 ]           0          0


    Il circuito di campionamento qui riportato è costituito da transistori i cui dimensionamenti
assoluti sono Sn =1 e Sp ="= n0 / p0 per i transistori di tipo n-MOS e p-MOS rispettivamente.




  1. Relativamente al percorso IN-O2, indicare la tipologia di circuito di campionamento e graficare
     qualitativamente l’andamento del segnale in uscita al nodo O2 in funzione dei segnali IN e CLK
     (e CLK negato).
2. Al fine di calcolare il tempo di setup del circuito in esame, si calcoli la resistenza equivalente
   (Req ) del pass-transistor complementare e la capacità CO1 al nodo O1. E’ noto che Req
   dipenderà dai potenziali ai due gate dei MOS del pass-transistor e, debolmente, dal potenziale
   dei nodi IN e O1. A tale proposito, per il calcolo di Req si supponga che il segnale di clock
   abbia un’escursione da 0 a VDD e che si voglia trasferire un segnale VIN =VDD con il potenziale
   del nodo O1 pari a VO1 =0V.
   Per il calcolo della capacità al nodo O1, (a) si trascuri il contributo dato dalle capacità
   intrinsiche di canale e si considerino solamente le capacità parassite che accoppiano elettro-
   staticamente il gate con le regioni di source/drain (cioè la capacità di gate-overlap e fringing:
   CGD,parass ) e quelle di giunzione source-bulk (o drain-bulk): CSB (o CDB ); (b) si consideri
   la capacità di ingresso dell’invertitore. La lunghezza delle regioni di source e drain vale
   LSD =3LMIN .




3. Si calcoli il tempo di setup del circuito assumendo un’escursione del segnale del 90%.




4. Si determini la costante di tempo dominante al nodo di uscita O3 assumendo che l’interconnessione
   abbia una resistenza per unità di lunghezza r=1000 ⌦/cm e capacità per unità di lunghezza
   c=1 pF/cm. Si sostituisca ogni tratto di lunghezza 100µm con una cella a T equivalente. Si
   descriva infine, una o più possibili tecniche per ridurre il tempo di attraversamento da IN a
   O3.
         Soluzione della prova Scritta di Circuiti e Sistemi Elettronici
                                         (DIGITALE)
                                        10 Maggio 2021


1. Il circuito in esame è costituito da un LATCH e dunque il dato in ingresso viene campionato
   sul livello logico del segnale di clock e non sul fronte. In particolare, il LATCH in esame è
   un positive LATCH e risulta dunque trasparente rispetto al dato posto in ingresso quando
   CLK=VDD . Inoltre, tale soluzione circuitale ”dinamica” riduce il numero di transistori elim-
   inando l’anello di retroazione presente in LATCH statici o pseudo-statici. Le forme d’onda
   (tralasciando il fatto che l’uscita risulta invertita rispetto all’ingreso) sono le seguenti:




2. Le specifiche di progetto richiedono di calcolare la resistenza equivalente Req nella condizione in
   cui i terminali di source e drain dei transistori del pass-transistor si trovano ad una di↵erenza
   di potenziale pari a VDD . Essendo inoltre la tensione dei gate dei due transistori pari a
   |VGS |=|VDS |, i transistori si trovano in saturazione e, trascurando il fattore di e↵etto body( =
   0), possiamo scrivere
                                           0
                                           n Sn
                                InM OS =      (VDD       Vth )2 = 216µA
                                           2
                                         0
                                         p Sp
                                IpM OS =      (VDD      Vth )2 = 216µA.
                                          2


   Req sarà dunque data dal rapporto tra la tensione ai capi del pass-transistor e la corrente data
   dalla somma di InM OS e IpM OS : Req =VDD /InM OS + IpM OS = 3.47k⌦
   Per calcolare la capacità al nodo O1 notiamo che sono presenti le capacità di ingresso
   dell’inveritore Cinv = SIN V (1 + ") CM 1 = 1 + 2 · Cox L2MIN + 2LMIN CGS0 = 0.6fF e le ca-
   pacità del pass-transistor Cpass . Quest’ultima sarà data dalle capacità di accoppiamento
   parassita tra gate-source/drain e dalle capacità delle giunzioni (CSB e CDB ). Si trascura in-
   fatti, come specificato nel testo, il contributo dato dalla capacità legata alla carica intrinseca
   del canale.
   Per il transistore nMOS del pass-transistor calcoliamo la capacità di giunzione Cj nM OS =
   Sn LMIN · 3LMIN · Cj0 Keq =0.072 fF e, similmente per il transistore di tipo pMOS avremo
   Cj pM OS = Sp LMIN ·3LMIN ·Cj0 Keq =0.144 fF. Infine, la capacità parassita data dall’accoppiamento
   con il terminale di gate vale, CGD nM OS = W CGS0 = Sn LMIN CGS0 = 0.05 fF e CGD pM OS =
   2 · CGD pM OS = 0.1 fF.
   Si ottiene Cpass =Cj nM OS + Cj pM OS + CGD nM OS + CGD pM OS =0.366 fF e dunque CO1 =
   Cpass + Cinv = 0.966 fF

3. Il tempo di setup è il tempo minimo in cui il dato in ingresso del LATCH deve rimanere stabile
   affinchè questo venga correttamente campionato. In questo caso tsetup è dato dal tempo
   affinchè il nodo O1 si porti, come specificato nel testo, al 90% dell’escursione del segnale (
   e quindi, nel caso in cui si voglia trasmettere un 1 logico dal terminale IN, il potenziale di
   O1 deve arrivare almeno alla tensione di 0.9VDD ). Utilizzando Req e CO1 appena calcolati, e
   ricordando di includere il prefattore 2.3 che tiene conto di una carica o scarica di un circuito
   RC al 90% dell’escursione del segnale, scriviamo tsu = 2.3Req CO1 = 7.72 ps.

4. Il circuito equivalente utilizzando celle a elementi concentrati a T, diventa




   dove Rdr è la resistenza del driver associata all’invertitore a dimensionamento minimo SnIN V =1:
                                                           ⇣      ⌘
                                                              VT
                                     RIN V        1     2F   V DD
                             Rdr =          =                       = 3.874k⌦.
                                      2.3     2.3VDD n0 SnIN V

   La resistenza RT della cella a T vale 100 · (r/1⇥104 )/2= 5 ⌦ mentre la capacità CT vale =10fF.
   Usando la regola di Elmore troviamo la costante di tempo dominante da O2 !O3 come:

        ⌧O2 !O3 = (Rdr + RT ) CT + (Rdr + 3RT ) CT + (Rdr + 4RT ) CT + (Rdr + 4RT ) C4 +
                 + (Rdr + 5RT ) CT + (Rdr + 6RT ) C3 = 545.57ps

   La costante di tempo totale sarà quindi ⌧IN !O1 + ⌧O2 !O3 = Req CO1 + ⌧O2 !O3 = 3.35ps +
   116.3ps = 548.93ps
   Il tempo di attraverso da IN a O3 può essere ridotto in diversi modi dipendentemente dalle
   possibili specifiche di progetto, ad esempio legate al numero di transistori che si vuole inserire.
   Una soluzione che richiede solo due transistori, consiste nell’inserire un bu↵er verso la dira-
   mazione che porta alla capacità C4, di modo tale che l’unico contributo dato da quel tratto di
   linea sia costituito dalla capacità di ingresso del bu↵er inserito. Ma si può anche partizionare
   la linea con più bu↵er. Inoltre, si nota che la linea può essere vista come una semplice
   capacità visto che Len < 2.3Rdr /10r e allora potremmo usare dei ripetitori in cascata in cui i
   parametri di progetto possono diventare il numero di inveritori e lo step-up ratio. Questi sono
   solo alcuni esempi che dipendono dalle specifiche di progetto.
                  Cognome e Nome
                     Matricola
                       Data                            14 Giugno 2016


                                     Circuiti e Sistemi II modulo
                                            14 Giugno 2016
   Sia VDD =1.0V e si assumano i seguenti parametri tecnologici per i MOSFET:
                                    Parametro    n-MOSFET       p-MOSFET
                                      VT O          0.35 [V]      -0.35 [V]
                                        β!       120 [µA/V2 ]    60 [µA/V2 ]
                                       Cox       12 [fF/µm2 ]   12 [fF/µm2 ]
                                      CGS0       0.85 [fF/µm]   0.85 [fF/µm]
                                       Cj0        5 [fF/µm2 ]    5 [fF/µm2 ]
                                      LM IN        0.13[µm]       0.13[µm]
Se non diversamente specificato si assuma per tutti i transistori L=LM IN ed LSD =LM IN . Si
riportino negli spazi bianchi all’interno del testo l’espressione analitica e, quando richiesto,
il valore numerico dei risultati.
In figura si mostra un circuito di campionamento del segnale di ingresso D governato dal segnale di clock φ.
I tre rami del circuito R1, R2 ed I1 devono avere tempi di salita e discesa simmetrici. I dimensionamenti
di R1 sono noti ed indicati in figura.

                                     VDD        VDD
                                                                  VDD
                                φ      4
                                                           B1
                                       4               φ
                            D                                             q

                                       2    q          φ                   CW

                              φ        2
                                                                  (I1)
                                     (R1)       (R2)

  1) (6 Punti). Si indichi se il circuito è statico o dinamico e se lavora a livello (latch) oppure a fronte
     (registro). Si tracci la forma d’onda qualitativa dell’uscita q nel grafico sottostante.

      D




      φ                                                     t



      q                                                     t



                                                            t
2) (10 Punti). Si calcoli il logical effort gR dei rami R1 ed R2 ed il ritardo caratteristico tp0 della
   tecnologia.




3) (12 Punti). Nota inoltre CW =3.5f F si trovi il dimensionamento del ramo R2 e dell’invertitore I1
   che minimizzano il ritardo fra D e q ed il valore numerico di tale ritardo.
   Per semplificare l’analisi è possibile trascurare il parasitic effort, ovvero l’effetto delle capacità
   parassite CGS0 e Cj0 .
         Soluzione della Prova Scritta di Complementi di Elettronica II
                                         14 Giugno 2016
1) Il circuito in esame è statico e rappresenta un latch trasparente durante il livello basso del clock φ.
   Da questo si deducono immediatamente le forme d’onda sul nodo q.

2) Il ritardo intrinseco della tecnologia si calcola come il ritardo di un inverter con capacità di carico
   pari a quella di ingresso. Detta CM 1 =L2M IN Cox +2LM IN CGS0 !0.424f F la capacità del transistore
   ad area minima L2M IN , il tempo tp0 puó essere ottenuto considerando un invertitore a dimensiona-
   mento minimo:
                                         2(1 + ε)CM 1
                                   tp0 =               F (VT /VDD ) = 58ps
                                             βn! VDD
   dove F(VT /VDD ) vale circa 2.74 per i valori di VDD e VT in esame, mentre ε=βn! /βp! =2.
   Per quanto riguarda il logical effort gR , notiamo che i dimensionamenti degli nMOS e pMOS dei
   blocchi R1 ed R2 devono essere pari rispettivamente a 2 e 2ε affinché la resistenza equivalente sia
   uguale a quella di un invertitore ad area minima. La corrispondente capacità di ingresso per i gate
   R1 ed R2 sarà 2(1 + ε)CM 1 e quindi avremo gR =2.

3) Il ritardo fra D e q deve essere valutato quando il latch è trasparente e quindi per φ=0. In questa
   situazione il gate R2 gioca il semplice ruolo di un carico sul nodo di uscita. Infatti sul nodo q
   insistono la capacità CW =3.5f F ed anche la capacità di ingresso CR2 di R2. Si deduce che il
   dimensionamento ottimo di R2 per minimizzare il ritardo da D a q è semplicemente quello minimo,
   ovvero nMOS dimensionato ad 1 e pMOS dimensionato a ε=βn! /βp! =2 (per la simmetria dei ritardi).
   In questo caso la capacità totale sull’uscita q vale COU T =CW + (1 + ε)CM 1 =4.77f F . La capacità
   di ingresso Cin al nodo D vale Cin =2(1 + ε)CM 1 =2.54f F quindi, trascurando il parasitic effort
   (ovvero il le capacità parassite Cj0 e CGS0 ), il path effort risulta F =gR · (COU T /Cin )=3.75.
                                                                                               √
   Il numero degli stadi è due e quindi avremo uno stage effort ottimo pari a fˆ= F =1.94, da
   cui deduciamo la capacità di ingresso dell’invertitore I1 che vale Cinv =COU T /fˆ=2.46f F . Sic-
   come Cinv =Sinv (1 + ε)CM 1 possiamo immediatamente calcolare il dimensionamento di I1 come
   Sinv =Cinv /(1 + ε)CM 1 =1.94.
   Se trascuriamo il parasitic effort dei gate avremo un ritardo da D a q pari a:

                                          T = tp0 (2fˆ + 0) ! 225ps
                  Cognome e Nome
                     Matricola
                       Data                         8 Settembre 2004



                             Prova Scritta di Elettronica Digitale
                                          8 Settembre 2004
Sia VDD =2.5V e si assumano i seguenti parametri tecnologici per i MOSFET:

                                  Parametro    n-MOSFET       p-MOSFET
                                    VT O          0.4 [V]        -0.4 [V]
                                      Ø0       500 [µA/V2 ]   200 [µA/V2 ]
                                     Cox       14 [fF/µm2 ]   14 [fF/µm2 ]
                                     Cj0        7 [fF/µm2 ]    7 [fF/µm2 ]
                                    LM IN        0.25[µm]       0.25[µm]

Se non diversamente specificato si assuma per tutti i transistori L=LM IN .
La figura illustra un circuito in cui un Gate CMOS pilota direttamente una interconnessione di tipo
RC. Per la interconnessione si possono assumere una resistenza per unitá di lunghezza r=1.0[Ohm/µm]
ed una capacitá per unitá di lunghezza c=1.4[f F/µm]. La lunghezza della linea é Len =200µm. Come
inidcato anche in figura la capacitá di caricoi CO a valle della linea é molto minore della capacitá della
linea Cint .

                                          VDD
                             A                  B

                                  C
                                                       r, c

                              A                                   CO << Cint
                                                C
                              B



  1) (8 Punti). Con riferimento ai parametri indicati nella tabella, si calcolino il ritardo caratteristico ø
     della tecnologia, nonché la resistenza equivalente Rinv e la capacitá di ingresso Cinv di un buﬀer a
     dimensionamento minimo. Assumendo inolte che la lunghezza delle regioni di source e drain siano
     LS =LD =3LM IN , si calcoli il Parastic Eﬀort pinv dell’Inverter.
2) (6 Punti). Si calcolino il Logical Eﬀort ed il Parasitic Eﬀort del Gate in figura.




3) (6 Punti). Si supponga ora di usare per il Gate il massimo dimensionamento intero (S=1, 2, 3 ...)
   compatibile con una capaictá di ingresso CIN < 10f F e di pilotare la interconnessione direttamente
   col Gate. Si stimi il ritardo di pilotaggio della interconnessione.




4) (6 Punti). Per questo tipo di interconnessione e di Driver l’aggiunta di Buﬀer fra l’uscita del Gate
   e la interconnessione puó essere una buona tecnica per ridurre il ritardo complessivo del circuito ?
   Si risponda in modo breve ma motivato alla precedente domanda e si indichino eventualmente il
   numero ed i dimensionamenti dei Buﬀer.
                 Soluzione della Prova Scritta di Elettronica Digitale
                                          8 Settembre 2004
1) Per la tecnologia in esame la simmetria dei ritardi nell’Inverter impone un dimensionamento relativo
   fra pMOSFET ed nMOSFET pari ad Æinv = Øn0 /Øp0 = 2.5. La capacitá di ingresso per un Inverter
   a dimensionamento minimo é quindi subito data da Cinv = (1 + 2.5)Cox L2M IN =3.06f F . Il ritardo
   caratteristico puó essere calcolato considerando per un Inverter una capacitá di carico pari alla
   capacitá di ingresso. Riferendoci ad un Inverter a dimensionamento minimo otteniamo:
                                              2Cinv
                                        ø=           F (VT /VDD ) = 9.16ps
                                             Øn0 VDD

   Per la resistenza equivalente dell’Inverter ad area minima si ha dunque Rinv = ø /Cinv =2990Ohm.
   Se le lunghezze LS = LD = 3LM IN allora la capacitá delle giunzioni per un Inverter ad area minima
   é Cd =(1 + Æinv )3L2M IN Cj0 e quindi il Parasitic EÆort vale pinv =Cd /Cg =3Cj0 /Cox =1.5.

2) Sia nel caso peggiore di salita che nel caso peggiore di discesa abbiamo due transistori in serie.
   Quindi per ottenere una simmetria di ritardi dobbbiamo imporre ÆG = Øn0 /Øp0 = 2.5. Per calcolare
   il Logical EÆort del Gate notiamo che, per avere la stessa resistenza equivalente di un Inverter con
   dimensionamento di Pull-Down Sinv il Gate deve avere dimensionamento di Pull-Down SG =2Sinv .
   Dal rapporto fra la capacitá di ingresso del Gate e quella dell’Inverter otteniamo quindi un Logical
   EÆort pari a 2. Per quanto rigiarda il Parasitic EÆort, due transistor nMOS ed un transistor p-
   MOS sono connessi all’uscita. Inoltre, per avere stessa resistenza dell’Inverter dimensionato Sinv ,
   gli n-MOS dovranno essere dimensionati Sn =2Sinv ed i p-MOS Sp =2ÆG Sinv =5Sinv . Il Parasitic
   EÆort sará dunque dato da:
                                             2 · 2Sinv + 5Sinv
                                      PG =                     £ pinv = 3.86
                                              (1 + Æinv )Sinv

3) La capacitá di ingresso del Gate é proporzionale al dimensionamento Sn dei transistori nel Pull-
   Down secondo CIN = Sn (1 + ÆG )L2M IN Cox =3.06 ·Sn [f F ]. Il massimo dimensionamento intero
   compatibile con CIN < 10f F é quindi Sn =3 a cui corrisponde CIN =9.2f F . siccome sappiamo
   che la resistenza equivalente RG del Gate in esame é uguale alla resistenza Rinv di un inverter ad
   area minima (calcolata al punto (1)) quando Sn =2 ed inoltre sappiamo che RG é inversamente
   proporzionale ad Sn , allora la resistenza equivalente del Gate per Sn =3 sará semplicemente RG =
   (2/3)Rinv ' 1990Ohm. Se la linea viene quindi direttamente pilotata dal Gate, il ritardo di
   pilotaggio al 90% della escursione risulta:
                                  RG
                     Ttot ' 2.3       cLen + rcL2en = TDR + Tint = 560 + 56[ps] = 616[ps]
                                  2.3
   dove TDR indica il ritardo relativo alla resistenza del Driver per la capacitá di interconnessione
   mentre Tint é il ritardo intrinseco di interconessione. Nella scrittura del ritardo si é tenuto conto
   del fatto che la capacitá a valle della linea é trascurabile rispetto a quella della linea stessa.

4) Siccome in questa situazione il ritardo del Driver é di gran lunga dominante, il ritardo complessivo
   puó essere migliorato in modo sensibile aggiungendo dei BuÆer a valle Gate. Visto che il ritardo
   intrinseco della linea e’ piuttosto piccolo (perché la resistivitá r é bassa), allora posso organizzare
   i BuÆer come se la linea fosse una pura capacitá Cint = Len c = 280f F . A questo punto, nota
   la capacitá di ingresso del gate CIN =9.18f F , posso calcolare il Path EÆort complessivo come
   F=g · (Cint /CIN )'61. Lo Stage EÆort ottimo puó essere stimato come Ω̂ = 0.71pinv + 2.82=3.88 da
   cui ottengo un numero ottimo di stadi N̂ =lnF/lnΩ=3.03. Scelgo quindi N̂ =3 con Ω = F 1/3 =3.94.
   Si tratta quindi di aggiungere due Inverter con dimensionamenti (espressi in termini di capacitá di
   ingresso) pari a C1 = Cint /Ω=71fF e C2 = Cint /Ω2 =18 fF.
   In questo modo la resistenza equivalente del BuÆer che pilota la interconnessione é pari a R1 =
   Rinv (Cinv /C1 )=129Ohm ed il tempo di pilotaggio relativo al BuÆer scende a 2.3(R1 /2.3)cLen =83.1[ps].
Naturalmente il ritardo complessivo consta adesso anche dei ritardi dei BuÆer, quindi nel complesso
si ha:
                                   R1
Ttot = ø (2Ω + PG + Pinv ) + 2.3       cLen + rcL2en = 9.16(2 · 3.94 + 3.86 + 1.5) + 36 + 56 [ps] = 213 [ps]
                                   2.3
                  Cognome e Nome
                     Matricola
                       Data                         13 Luglio 2004



                             Prova Scritta di Elettronica Digitale
                                            13 Marzo 2006
Si riportino negli spazi bianchi all’interno del testo l’espressione analitica e, quando richiesto,
il valore numerico dei risultati.
In figura è riportato un albero per la distribuzione di due fasi di clock complementari ¡ e ¡ costituito
da interconnessioni di tipo RC. Le interconnessioni hanno resistività per unità di lunghezza r=40≠/µm
e capacità per unità di lunghezza c=0.35f F/µm. I buÆer riportati in figura sono descrivibili con un
semplice modello lineare. In particolare, i buÆer a dimensionamento minimo hanno resistenza Rdr =2k≠
e capacità Cdr =6f F . Il parasitic eÆort dei buÆer può essere trascurato.
    Si assuma che i rami di interconnessione abbiano tutti la medesima lunghezza Len =25µm e che le
capacità da pilotare siano C1 =30f F e C2 =39f F per la fase ¡ e ¡, rispettivamente. I ritardi della rete
ad albero devono essere calcolati schematizzando i tre rami di interconnessione con opportune reti a
parametri concentrati.

                                                                                      φ
                                              h1
                                                                                       C1
                                                                     Len
                                        B
             IN
                             Len
                                                                                       φ
                                             h2         h2
                                                                                          C2
                                                                       Len


  1) (6 punti). Si calcolino i valori Rº e Cº che corrispondono ad una singola cella a ¶ che schematizza
     un ramo di interconnessione. Si disegni quindi il circuito costituito dai buÆer e dagli elementi RC
     risultanti dalla sostituzione delle celle a ¶ ad ogni ramo di interconnessione.




                                                                           Vedi 19 marzo 2007
2) (6 punti). Supponendo che in ingresso all’albero di interconnessioni sia applicato un gradino di
   tensione da 0V a VDD , si esprimano la costante di tempo dominante ø (¡) al nodo sede di C1 e la
   costante di tempo dominante ø (¡) al nodo sede di C2 in funzione dei dimensionamenti dei buÆer
   h1 ed h2.




3) (8 punti). Si esprima h1 in funzione di h2 a±nché risulti ø (¡)=ø (¡).




4) (6 punti) Si determinino h1 ed h2 in modo da minimizzare le costanti di tempo ø (¡)=ø (¡) e si
   calcoli il valore numerico del ritardo delle fasi ¡ e ¡ al 90% della escursione di segnale.
                Soluzione della Prova Scritta di Elettronica Digitale
                                           13 Marzo 2006
1) Per una lunghezza L=25µm si ha una capacitá totale ed una resistenza totale per ogni ramo di
   interconnessione pari a Cint =8.75f F ed Rint =1000Ohm. Se schematizziamo ogni ramo di intercon-
   nessione con una singola cella a ¶ otteniamo Rº =Rint =1000Ohm e Cº =Cint /2=4.375fF. Il circuito
   risultante è illustrato in figura:




2) La costante di tempo dominante delle fasi si può calcolare sommando le costanti di tempo dall’ingresso
   IN al nodo B e quindi dal nodo B verso i nodi sede di C1 e C2 . La resistenza e capacità di un buÆer
   con dimensionamento h1 sono Rdr /h1 e h1Cdr , rispettivamente. Analoghe espressioni valgono per
   il buÆer con dimensionamento h2. Se calcoliamo le costanti di tempo tramite la regola di Elmore
   otteniamo:

                 ø (¡) = Rº [Cº + (h1 + h2)Cdr ] + (Rdr /h1)Cº + (Rdr /h1 + Rº )(Cº + C1 )

           ø (¡) = Rº [Cº + (h1 + h2)Cdr ] + Rdr Cdr + (Rdr /h2)Cº + (Rdr /h2 + Rº )(Cº + C2 )
   Si noti che sul ramo che genera la fase ¡ si deve tenere in conto la costante di tempo del ritardo di
   un invertitore. Se trascuriamo il parasitic eÆort, come suggerito nel testo, la suddetta costante di
   tempo vale Rdr Cdr .

3) La relazione fra h2 ed h1 che rende uguali ø (¡) e ø (¡) si ottiene uguagliando le espressioni del punto
   precedente. Se introduciamo le costanti:

   tc1 = Rdr Cdr + Rº (C2 ° C1 ) ' 21ps    tc2 = Rdr (C2 + 2Cº ) = 95.5ps   tc3 = Rdr (C1 + 2Cº ) = 77.5ps

   otteniamo:
                                                           h2 tc3
                                                 h1 =
                                                        tc2 + h2 tc1

4) Se sostituiamo l’espressione di h1 in funzione di h2 in ø (¡) o ø (¡) otteniamo una espressione in h2
   la cui minimizzazione è complicata dal fatto che si tratta di un polinomio di quarto grado. Possiamo
   ricavare una ottimizzazione approssimata imponendo:

                                   @ø (¡)            Rdr (C2 + 2Cº )
                                          = Rº Cdr °                 =0
                                    @h2                    h22
   da cui otteniamo:                             s
                                                     Rdr (C2 + 2Cº )
                                          h2 =                       '4
                                                          Rº Cdr
   Il valore di h1 ottenuto dalla relazione fra h1 ed h2 del punto (3) risulta h1'1.73. Sostituendo i
   valori numerici di h1 ed h2 nelle espressioni per le costanti di tempo si ottiene ø (¡)=ø (¡)'118ps.
   Il ritardo delle fasi al 90% della escursione di segnale risulta quindi T90% =2.3ø (¡)=271.4ps.
                   Cognome e Nome
                      Matricola
                        Data                                     2 Febbraio 2009

                       Prova Scritta di Complementi di Elettronica II
                                                     2 Febbraio 2009
Si riportino negli spazi bianchi all’interno del testo l’espressione analitica ed il valore nu-
merico dei risultati.
                                                 VDD                        VDD
                                                                      A    B               Ci
                                A                    B
                                                                                           A
                                     B               Ci                                    B
                                     A                                                     Ci
                                                            Co                                  S
                                     Ci                                                Ci
                          (a)                               A

                                 A               B                                     B
                                                            B A        B         Ci
                                                                                       A


                                            GC                             GS

                           A0         GC0              X             GC1
                           B0               C0                                        C1
                                                           A1
                           Ci                              B1                              CW
                                      A0         GS0                 A1        GS1
                           (b)        B0
                                                                S0
                                                                     B1
                                                                                 S1
                                      Ci

Il circuito in figura è realizzato con una tecnologia CMOS in cui: Øn0 =221µA/V 2 e Øp0 =130µA/V 2 , ritardo
caratteristico tp0 =13ps, parasitic eﬀort dell’invertitore pinv =0.95 e CM 1 =Cox L2M IN +2CGS0 LM IN =0.9f F .
La parte (a) della figura mostra il circuito che realizza la somma dei due bit A e B e del bit di carry-in
Ci . Tale circuito è costituito dal gate logico GC, che calcola il carry-out in forma negata CO , e dal gate
logico GS, che invece calcola il bit di somma S. La parte (b) della figura mostra il circuito che realizza
la somma di due parole a due bit (A0 ,A1 ) ed (B0 ,B1 ) sfruttando due gate GC0, GC1 del tipo GC e due
gate GS0, GS1 del tipo GS.
     Tutti gli n-MOSFET all’interno di uno stesso gate logico hanno il medesimo dimensionamento Sn e
tutti i p-MOSFET il medesimo dimensionamento Sp . Tutti i gate devono avere tempi di salita e discesa
simmetrici. I dimensionamenti dei transistori n-MOS dei gate GC0 e GS0 sono Sn =1.
   1) (12 Punti). Si calcolino i logical eﬀort gGC (A), gGC (B) e gGC (Ci) del gate CG e gGS (A), gGS (B)
       e gGS (Ci) del gate GS. Si calcolino inoltre i parasitic eﬀort PGC e PGS dei due gate.
      Noto Sn =1, si calcolino le capacità di ingresso C(A0), C(B0) e C(Ci) del gate GC0.
2) (10 Punti). Si scriva l’espressione del ritardo del bit di riporto fra l’ingresso Ci e l’uscita C1 in
   funzione della capacità di ingresso ai gate GC1 e GS1 e della capacità di uscita CW .
   Si determinino i dimensionamenti dei gate GC1 e GS1 che minimizzano il suddetto ritardo da Ci
   a C1 per CW =35f F (il dimensionamento può essere espresso come capacità di ingresso dei gate).
   Si calcoli inoltre il valore numerico di tale ritardo.




3) (8 Punti). Usando i dimensionamenti di GC1 e GS1 determinati al punto precedente si calcoli il
   branching eﬀort bX al nodo X.
   Supponendo adesso di usare un branching eﬀort bX pari al valore appena trovato, si minimizzi il
   ritardo del gate secondo la metodologia del logical eﬀort per branching eﬀort costante e si determini
   il valore numerico del ritardo.
   Si commenti brevemente il rapporto fra l’ottimizzazione ottenuta in quest punto rispetto a quella
   ottenuta al punto (2).
         Soluzione della Prova Scritta di Complementi di Elettronica II
                                            2 Febbraio 2009
1) Per il calcolo del logical eﬀort del gate GC notiamo che il caso peggiore per il transitorio di salita
   corrisponde a A=B=0 e Ci =0. In questo caso il dimensionamento equivalente Sp,eq del pull-up vale
                                    1           2   1                       2
                                           =      +         )     Sp,eq =     Sp
                                   Sp,eq        Sp 2Sp                      5
   Nel caso peggiore di discesa abbiamo semplicemente due transistori n-MOS in serie, quindi si ha
   Sn,eq =Sn /2. L’uguaglianza dei ritardi di caso peggiore per il gate GC richiede Øp0 Sp,eq =Øn0 Sn,eq , da
   cui si ottiene un rapporto Sp /Sn fra i dimensionamenti nei gate di tipo GC pari a Sp /Sn =(5")/4=2.125,
   con "=Øn0 /Øp0 =1.7. Per uguagliare il ritardo di caso peggiore del gate GC a quello di un invertitore di
   riferimento con dimensionamento Sinv nel pull-down dobbiamo avere Sn =2Sinv , quindi la capacità
   agli ingressi A e B vale C(A)=C(B)=2Sn [1 + (5")/4]CM 1 =Sinv (4 + 5")CM 1 , dove si è tenuto conto
   del fatto che gli ingressi A e B pilotano due coppie di transistori. La capacità all’ingresso Ci è la
   metà della C(A) perché Ci pilota una sola coppia di transistori. Per quanto riguarda la capacità
   parassita sul nodo di uscita, notiamo che nel gate GC due transistori di tipo n-MOS e due di tipo
   p-MOS sono connessi all’uscita stessa. Da quanto detto si ottiene:
                                           4 + 5"                       2Sn + 2Sp          4 + 5"
    gGC (A) = gGC (B) = 2 gGC (Ci ) =             = 4.63        PGC =               pinv =        pinv = 4.39
                                           1+"                          (1 + ")Sinv         1+"

   Per quanto riguarda il gate GS, la salita di caso peggiore avviene per A=B=Ci =0 e CO =1 ed in
   tal caso il dimensionamento equivalente si ottiene come
                                    1          3   1                         3
                                           =     +          )    Sp,eq =       Sp
                                  Sp,eq        Sp 3Sp                       10
   Nel caso peggiore di discesa abbiamo semplicemente tre transistori in serie e quindi Sn,eq =Sn /3.
   Uguagliando i ritardi di salita e discesa di caso peggiore otteniamo Sp /Sn =(10")/9=1.89. Per
   equalizzare il ritardo rispetto all’invertitore di riferimento dobbiamo avere Sn =3Sinv , quindi la
   capacità agli ingressi A e B vale C(A)=C(B)=C(Ci )=2Sn [1 + (10")/9]CM 1 =Sinv [6 + (20")/3]CM 1 .
   La capacità all’ingresso CO è la metà della C(A). Nel gate GS due transistori di tipo n-MOS e due
   di tipo p-MOS sono connessi all’uscita, per cui otteniamo
                            6 + (20")/3                          2Sn + 2Sp          6 + (20")/3
      gGS (A) = gGS (B) =               = 6.42           PGS =               pinv =             pinv = 6.1
                               1+"                               (1 + ")Sinv           1+"
   Noto Sn =1 per il gate CG0, la capacità di ingresso vale C(A)=C(B)=C(Ci )=2Sn [1+(5")/4]CM 1 =5.625f F .

2) Per esprimere il ritardo notiamo che la capacità totale CX al nodo X vale CX =CGS0 (CO ) +
   CGC1 (Ci ) + CGS1 (Ci ), dove la CGS0 è la capacità nota al gate GC0 mentre le CGC1 e CGS1 sono
   le capacità incognite dei gate GC1 e GS1. La capacità al nodo di uscita vale CW +CGS1 (CO ) ed il
   ritardo adimensionale può quindi essere espresso come:

                     CGS0 (CO ) + CGC1 (Ci ) + CGS1 (Ci )                  CW + CGS1 (CO )
    tad = gGC (Ci)                                        + PGC + gGC (Ci)                 + PGC (1)
                                 CGC0 (Ci )                                  CGC1 (Ci )
   dove CGC0 (Ci )=2.812f F è la capacità di ingresso del circuito. Evidentemente, per il ritardo del
   bit di riporto, le capacità CGS1 (Ci ) e CGS1 (CO ) del gate GS1 sono solo capacità di carico, quindi
   per minimizzare il ritardo dobbiamo usare dimensionamento minimo per il gate GS1, cioé Sn =1
   ed Sp =(10")/9, a cui corrisponde CGS1 (Ci )=CGS1 (CO )=2.6f F . Siccome anche il gate GS0 ha
   dimensionamento minimo, si ha CGS0 (CO )=CGS1 (CO )=2.6f F . Note CGS1 (Ci ) e CGS1 (CO ), il
   valore di tad può essere ottimizzato rispetto a CGC1 (Ci ) annullando la relativa derivata. Cosı̀
   facendo si ottiene:
                                           q
                           CGC1 (Ci ) =        CGC0 (Ci ) (CW + CGS1 (CO )) = 10.3f F
3) Note le capacità di GC1 possiamo esprimere il branching eﬀort al nodo X:

                                           CGS0 (CO ) + CGS1 (Ci )
                                bX = 1 +                           ' 1.50
                                                 CGC1 (Ci)

   Il path eﬀort vale quindi F =(gGC (Ci ))2 p
                                             bX H'107.9, con H=[CW + CGS1 (CO )]/CGC0 (Ci )=13.37.
                                         ˆ
   Lo stage eﬀort ottimo risulta quindi f = 2 F =10.38 da cui si ottiene subito

                                              [CW + CGS1 (CO )]
                               CGC1 (Ci ) =                     = 8.38f F
                                                     fˆ
   Sostituendo in Eq.1 otteniamo tad =30.82.
   I valori di ritardo ottenuti col metodo di minimizzazione esatto e con quello approssimato non
   coincidono. Il metodo esatto è quello usato al punto 2, che infatti fornisce un ritardo minore,
   quindi migliore. La diﬀerenza è tuttavia molto piccola, perché nel metodo approssimato, che è
   approssimato appunto perché assume un valore costante per il branching eﬀort, abbiamo inserito il
   valore di bX ottenuto col metodo esatto. L’ottimizzazione approssimata dà quindi in questo caso
   un risultato molto simile all’ottimizzazione esatta.
                      Prova Scritta di Circuiti e Sistemi Elettronici
                                          (DIGITALE)
                                         22 Febbraio 2021

   Se non diversamente specificato si assuma per tutti i transistori L = LMIN e i tempi
di salita e di discesa di caso peggiore dei singoli gate logici simmetrici.
   Il circuito logico in figura é costituito da un gate dinamico, un invertitore statico a dimensiona-
mento minimo e dei gate NOR statici. Sono note le conducibilità intrinseche dei transistori n-MOS
e p-MOS n0 =300µA/V 2 e p0 =150µA/V 2 , la capacità di gate del transistore a dimensionamento
minimo CM 1 = 0.75f F e il parasitic e↵ort dell’invertitore pinv = 1.2. La tensione di soglia dei
transistori n-MOS e p-MOS vale Vtn =|Vtp |=0.40V e la tensione di alimentazione é VDD = 3.0V .




  1. Calcolare il logical e↵ort dall’ingresso A al nodo O1 e il parasitic e↵ort del gate dinamico
     assumendo che tutti i transistori nMOS del gate dinamico abbiano lo stesso dimensionamento
     e che i tempi di salita (il tempo di precarica) e di discesa di caso peggiore siano simmetrici.




  2. Determinare il dimensionamento assoluto di tutti i transistori del gate dinamico di modo che la
     resistenza equivalente di caso peggiore sia la metà di quella di un invertitore a dimensionamento
     minimo. Calcolare inoltre il tempo caratteristico della tecnologia.
3. Noto il dimensionamento assoluto dei transistori del gate dinamico calcolato al punto prece-
   dente, calcolare il tempo di attraversamento dall’ingresso A al nodo O4 assumendo che l’invertitore
   tra il nodo O1 e O2 sia a dimensionamento minimo, che i gate NOR siano stati realizzati
   con transistori nMOS aventi dimensionamento pari a SnN OR =6 e che la capacità di uscita
   COU T connessa al nodo O4 sia molto inferiore rispetto alla capacità dell’interconnessione.
   L’interconnessione ha una lunghezza L = 5000µm. Si consideri un ritardo di pilotaggio al 90%
   dell’escursione totale.




4. Descrivere una possibile tecnica per diminuire il tempo di ritardo dall’ingresso A al nodo
   O4 assumendo che non sia possibile modificare il dimensionamento dei gate NOR e del gate
   dinamico e che sia possibile cambiare il dimensionamento dell’invertitore tra i nodi O1 e O2.
   Si richiede una risposta breve ma motivata, non é necessario procedere con una valutazione
   quantitativa determinando i vari dimensionamenti.
         Soluzione della prova Scritta di Circuiti e Sistemi Elettronici
                                         (DIGITALE)
                                        22 Febbraio 2021


1. Affinché i tempi di salita e discesa di caso peggiore siano simmetrici si nota che nel caso peggiore
   per la transizione di discesa ci sono 3 transistori in serie e per quella di salita (la transizione
                                                                                                   0
   di precarica) é presente un solo transistore pMOS dunque Sp,GAT E = " · Sn,GAT E /3 = n0 /3 ·
                                                                                                  p
   Sn,GAT E = 23 ·Sn,GAT E . Per il calcolo del logical e↵ort del gate dinamico, assumiamo che questo
   abbia la stessa resistenza equivalente di un inveritore con dimensionamento SIN V (dove SIN V
   indica il dimensionamento del transistore nMOS dell’inveritore con tempi di salita e discesa
   simmetrici), dunque Sn,GAT E = 3SIN V . Perciò , il logical e↵ort per l’ingresso A si trova come
   rapporto di capacità notando che l’ingresso A viene connesso solamente a 2 transistori nMOS
                                 2 · Sn,GAT E CM 1    2 · 3SIN V CM 1
                           g=                      =                    = 2.
                                SIN V (1 + ") CM 1   SIN V (1 + ") CM 1

   Per il calcolo del parasitic e↵ort si nota che sono presenti 2 nMOS e 1 pMOS sul nodo di uscita,
   e dunque
                          2Sn,GAT E + Sp,GAT E         2 · 3SIN V + 2SIN V
               pGAT E =                        pIN V =                     pIN V = 3.2.
                              SIN V (1 + ")                SIN V (1 + ")

2. La resistenza equivalente del gate dinamico é inversamente proporzionale al dimensionamento
   e possiamo scrivere che RGAT E = 1/2 · RIN V quando Sn,GAT E /3 = 2SIN V . Visto che al
   punto 2 dobbiamo considerare un invertitore a dimensionamento minimo allora SIN V = 1 e
   dunque Sn,GAT E = 6. Il dimensionamento del pMOS si ottiene dalla relazione trovata al punto
   precedente Sp,GAT E = 23 · Sn,GAT E = 4.
   Il tempo caratteristico della tecnologia tp0 , che per definizione non dipende dal dimensiona-
   mento assoluto, vale:
                                                  ⇣    ⌘
                                             2F VVDD T

                        tp0 = RIN V CIN V =       0
                                                         (1 + ") CM 1 = 8.95ps
                                                 n VDD

3. Il calcolo del tempo di attraversamento é dato dal tempo di attraversamento dei primi due
   gate logici sommato al tempo di pilotaggio dell’interconnessione da parte del gate NOR:
                                                       2
                                                                   !
                                                      X
         t = tLOGIC(A!O2) + tDRIV ER + tIN T = tp0       gi hi + pi + 2.3Rdr,N OR cL + rcL2
                                                         i=1

          = tp0 (gGAT E,A hGAT E,A + pGAT E + gIN V hIN V + pIN V ) + 2.3Rdr,N OR cL + rcL2



   Il logical e↵ort del gate dinamico per l’ingresso A é già stato calcolato al punto 1 e vale
   gGAT E,A = 2, lo stesso vale per il parasitic e↵ort che vale pGAT E = 3.2. L’electrical e↵ort
   relativo al primo gate vale:
                                    CIN V         (1 + ") CM 1    (1 + 2) CM 1   1
                     hGAT E,A =              =                  =              =
                                  CGAT E,A       2Sn,GAT E CM 1     2 · 6CM 1    4
   Per quanto riguarda l’inveritore, il logical e↵ort é gIN V = 1, il parasitic e↵ort é pIN V = 1.2.
   Notiamo esserci branching e↵ort ma essendo interessati a calcolare il tempo di propagazione
   tLOGIC(A!O2) dall’ingresso A al nodo O2, possiamo assumere che i tre gate NOR costituiscano
   un semplice carico per l’inveritore e dunque
                             3CN OR3   3Sn,N OR (1 + 3") CM 1   3 · 6 (1 + 3")
                   hIN V =           =                        =                = 42
                              CIN V      SIN V (1 + ") CM 1         (1 + ")

   Si calcolano ora capacità e resistenza per unità di lunghezza dell’interconnessione
                                     2⇡"SiO2           W          fF
                                c=     4tox +H
                                               + "SiO2      = 0.1    ,
                                   ln     H
                                                       tox        µm
                                     ⇢                 ⌦
                                r=       = 4.5 ⇥ 10 4     .
                                   WH                 µm

   Infine, la resistenza del driver (di caso peggiore) che pilota l’interconnessione é pari a
                                                              ⇣     ⌘
                                                                 VT
                                        RN OR        1    2F    VDD
                            Rdr,N OR =         =                       = 288⌦
                                          2.3     2.3VDD n0 SnN OR

   Dunque il tempo di propagazione di un segnale da A ad O4 é :

         t = tp0 (gGAT E,A hGAT E,A + pGAT E + gIN V hIN V + pIN V ) + 2.3Rdr,N OR cL + rcL2
                    ✓                      ◆
                         1
           = 8.95ps 2 · + 3.2 + 42 + 1.2 + 2.3Rdr,N OR cL + rcL2
                         4
           = tLOGIC(A!O2) + tDRIV ER + tIN T = 419ps + 331ps + 1.12ps = 751ps



4. Non essendo possibile modificare il dimensionamento dei gate NOR si puó diminuire separata-
   mente tLOGIC(A!O2) e t(O2!O4) . Si nota come il tempo caratteristico dell’interconnessione
   tIN T risulta piccolo rispetto a quello del driver che pilota l’interconnessione (tDRIV ER ) quindi
   risulta conveniente aggiungere dei bu↵er tra il gate NOR e l’interconnessione . Inoltre, visto che
   L < 2.3RDRIV ER / (10r) = 147mm risulta soddisfatta possiamo considerare l’interconnessione
   come una semplice capacitá di valore Cint = cL. A questo punto si puó utilizzare la metodologia
   del logical e↵ort per ottimizzare t(O2!O4) calcolando il path e↵ort come F = gN OR3 Cint /CN OR3
   = (1 + 3")/(1 + ") · cL/ [Sn,N OR (1 + 3") CM 1 ] = 36.97. Continuando con una analisi quan-
   titativa, anche se non richiesto al punto 4, lo stage e↵ort ottimo necessario per dimensionare
   i bu↵er vale ⇢ = 0.71pIN V + 2.82 = 3.67. Ne consegue che il numero di stadi ottimo vale
   N = ln(F )/ln(⇢) = 2.77 che viene approssimato a N = 3 (dunque aggiungeremo due bu↵er).
                                                           p
   Procediamo ricalcolando lo stage e↵ort ottimo fˆ = 3 F = 3.33 e dunque i bu↵er da inserire
   tra il gate NOR e l’interconnessione avranno dimensionamento espresso in termini di capacità
   di ingresso pari a C1 = cL/fˆ = 150f F e C2 = cL/      ˆ2
                                                        ⇣f =⌘45f F . Si ottiene quindi tDRIV ER =
   2.3Rdr,IN V 1 cL dove Rdr,IN V 1 = RIN V 1 /2.3 = 2F VVDDT
                                                                (1 + ") CM 1 / (2.3VDD C1 n0 ) = 26⌦ e
   dunque tDRIV⇣ER = 2.3Rdr,IN V 1 cL⌘= 29.8ps. Il ritardo dal nodo O2 al nodo O4 sarà pari a
   tO2!O4 = tp0 2fˆ + pIN V + pN OR3 +tDRIV ER +tIN T = 102.53ps+27.35ps+1.12ps = 133.4ps.
   Similmente, usando la metodologia del logical e↵ort possiamo procedere alla minimizzazione
   del tempo tLOGIC(A!O2) .
                  Cognome e Nome
                     Matricola
                       Data                                 3 Settembre 2007

                       Prova Scritta di Complementi di Elettronica II
                                                  3 Settembre 2007
Si riportino negli spazi bianchi all’interno del testo l’espressione analitica ed il valore nu-
merico dei risultati.
Il circuito illustrato in figura é realizzato con una tecnologia CMOS in cui: Øn0 =450µA/V 2 e Øp0 =180µA/V 2 ,
ritardo caratteristico tp0 =11ps, parasitic eﬀort dell’invertitore pinv =1.2 e CM 1 =Cox L2M IN +2CGS0 LM IN =1.2f F .
La parte (a) della figura mostra il circuito che realizza la somma dei due bit A e B e del bit di carry-in
Ci . Tale circuito é costituito dal gate logico GC, che calcola il carry-out in forma negata CO , e dal gate
logico CS, che invece calcola il bit di somma S. La parte (b) della figura mostra il circuito che realizza
la somma di due parole a due bit (A0 ,A1 ) ed (B0 ,B1 ) sfruttando i gate GC e GS.
                                                                                   VDD
                                  VDD                                                     B

                              A               B             A             B         Ci
                                                       B                                  A

                                                       A                                  Ci
                              Ci                             Co                                 S
                                                       A                                  Ci
                       (a)
                              A               B        B        A         B         Ci   A

                                                                                         B


                                        GC                                    GS

                        A0                         X
                        B0        GC
                                        C0                                               C1
                                                       A1       GC
                        Ci                             B1                                      CW
                                   A0                                A1
                                         GS                                   GS
                        (b)        B0
                                                            S0
                                                                     B1
                                                                                   S1
                                   Ci
I logical eﬀort valgono gGC (A)=gGC (B)=4, gGC (Ci)=2 per il gate CG e gGS (A)=gGS (B)=6, gGS (Ci)=3
per il gate GS. I parasitic eﬀort valgono PGC =4pinv e PGS =6pinv . Tutti gli n-MOSFET all’interno
di uno stesso gate logico hanno il medesimo dimensionamento Sn e tutti i p-MOSFET il medesimo
dimensionamento Sp . Tutti i gate devono avere tempi di salita e discesa simmetrici; tutti i gate GS
hanno dimensionamento minimo Sn =1.
   1) (10 Punti). Si calcolino Sn ed Sp del primo gate di tipo GC aﬃnché la capacità CGC0 (Ci ) all’ingresso
       Ci risulti pari a 8.4f F . Si determinino inoltre le capacità CGS (CO ), CGS (Ci ) agli ingressi CO e
       Ci del gate GS. Si esprima il ritardo del bit di carry fino al nodo di uscita C1 in funzione delle
       capacità nota CGS (CO ), CGS (Ci ) agli ingressi CO e Ci dei gate GS, della capacità in uscita CW e
       della capacità non nota CGC1 (Ci ) del secondo gate GC.
2) (10 Punti). In base all’espressione per il ritardo del bit di carry ricavata al punto precedente,
   si determinino i dimensionamenti Sn (GC1) ed Sp (GC1) del secondo gate GC che minimizzano il
   ritardo stesso e si valuti il valore numerico del ritardo minimo per CW =29.4f F .
   Sulla base di tale dimensionamento si calcoli quindi il branching eﬀort bX al nodo X.




3) (6 Punti). Si supponga adesso di sfruttare i gate GC e GS per realizzare la somma di due parole a
   quattro bit (A0 ,A1 ,A2 ,A3 ) e (B0 ,B1 ,B2 ,B3 ). Supponendo che il branching eﬀort sia in tutti gli stadi
   pari al valore bX calcolato al punto precedente, si dimensioni il circuito per minimizzare il ritardo
   e si calcoli il ritardo minimo.
   Il dimensionamento può essere espresso in termini delle capacità CGC1 (Ci ), CGC2 (Ci ), CGC3 (Ci )
   dei tre gate di tipo GC.
         Soluzione della Prova Scritta di Complementi di Elettronica II
                                         3 Settembre 2007
1) Il dimensionamento Sn degli n-MOSFETs del primo gate GC può essere calcolato imponendo:

                                    CGC (Ci ) = Sn £ (1 + ")CM 1 = 8.4f F

   che fornisce Sn =2 per "=Øn0 /Øp0 =2.5. Quindi, per garantire la simmetria dei ritardi di salita e discesa,
   il dimensionamento dei p-MOSFETs sarà Sp =5. Le capacità CGS (CO ) e CGS (Ci ) agli ingressi CO e
   Ci del gate GS sono diverse perchè CO pilota due transistori mentre Ci ne pilota quattro. Sapendo
   che i gate GS hanno dimensionamento minimo si ha quindi CGS (CO )=1 · (1 + ")CM 1 =4.2f F e
   CGS (Ci )=2 · CGS (CO )=8.4f F .
   Per esprimere il ritardo notiamo che la capacità totale CX al nodo X vale CX =CGC1 (Ci ) +
   CGS (CO ) + CGS (Ci ). La capacità al nodo di uscita vale CW +CGS (CO ) ed il ritardo complessivo
   può quindi essere espresso come:
               ∑                                                                                           ∏
                        CGC1 (Ci ) + CGS (CO ) + CGS (Ci )                  CW + CGS (CO )
    td = tp0 £ gGC (Ci)                                    + PGC + gGC (Ci)                + PGC
                                      CIN                                     CGC1 (Ci )

   dove si è indicato con CIN =8.4f F la capacità all’ingresso Ci del primo gate GC (determinata al
   punto precedente), mentre CGC1 (Ci ) è la capacità all’ingresso Ci del secondo gate GC dalla quale
   il ritardo dipende in modo non monotono, come era naturale aspettarsi.

2) Il ritardo determinato al punto precedente può essere minimizzato rispetto a CGC1 (Ci ) minimiz-
   zando la corrispondente derivata. Cosiıfacendo otteniamo:
                                             q
                              CGC1 (Ci ) =       CIN (CW + CGS (CO )) = 16.8f F

   Siccome la capacità di ingresso CGC1 (Ci ) vale Sn (GC1) · (1 + ")CM 1 , ricaviamo subito Sn (GC1)=4
   e quindi, per garantire la simmetria dei ritardi di salita e discesa, Sp (GC1)=10.
   Il valore del ritardo ottimo si ottiene sostituendo CGC1 (Ci )=16.8f F nell’espressione del ritardo
   ricavata al punto (1) e vale tp =20.6 tp0 '227[ps].
   In base al dimensionamento di GC1 possiamo esprimere il branching eﬀort al nodo S:

                                              CGS (CO ) + CGS (Ci )
                                   bX = 1 +                         ' 1.75
                                                   CGC1 (Ci)

3) Se supponiamo noto bX =1.75 in tutti gli stadi, l’ottimizzazione del circuito per quattro stadi procede
   in modo standard secondo la metodologia del logical eﬀort. In particolare avremo G=[gGCp     (Ci )]4 =16
   e B=[bX ]3 =5.36, inoltre H=CW /CIN =3.5. Il path eﬀort è quindi F =G B H'300 ed fˆ= 4 F =4.16.
   Mantenendo fissato il numero di stadi a quattro avremo quindi:

                    gGC (CW + CGS (CO ))                                    bX gGC CGC2 (Ci)
      CGC3 (Ci) =                        = 16.1f F            CGC3 (Ci) =                    = 13.6f F
                            fˆ                                                     fˆ

                                                  bX gGC CGC2 (Ci)
                                  CGC1 (Ci) =                      = 11.4f F
                                                         fˆ
   Il ritardo puó quindi essere calcolato come:

                      T = tp0 (4 fˆ + 4PGC ) = tp0 (4 fˆ + 16Pinv ) = 35.84 tp0 ' 394[ps]
                   Cognome e Nome
                      Matricola
                        Data                           3 Dicembre 2007



                        Prova Scritta di Complementi di Elettronica II
                                             3 Dicembre 2007
Si assuma per tutti i transistori L=LM IN . Si riportino negli spazi bianchi all’interno del
testo l’espressione analitica ed il valore numerico dei risultati.
In figura si mostra un circuito in cui tutti i gate sono realizzati in tecnologia Fully CMOS e sono dimen-
sionati in modo da avere tempi di salita e discesa uguali.
Della tecnologia in questione sono noti il ritardo di riferimento per la metodologia del Logical Eﬀort
tt0 =9ps, il parasitic eﬀort dell’invertitore pinv =1.1, i valori di Øn0 =270µA/V 2 , Øp0 =135µA/V 2 e la capacità
al terminale di gate del transistore a dimensionamento minimo CM 1 =1.3f F .
In figura è indicato il dimensionamento Sn =2 degli n-MOSFET del gate NAND, mentre Sexor ed Snor
indicano i dimensionamenti non noti del gate EXOR e NOR. Le capacità di carico valgono CL =82f F e
CL2 =27f F è indicato in figura.

                                                                               Out
                   IN                          X

                                                          Snor                       CL=82fF
                  CIN
                                   Sn=2
                                                                        Out2

                                                          Sexor                CL2=27fF



  1) (8 Punti). Si calcoli il logical eﬀort e parasitic eﬀort dei tre gate nel circuito e la capacità di ingresso
     Cin .
2) (10 Punti). Si scriva l’espressione del ritardo (in unità di tp0 ) dall’ingresso IN all’uscita Out in
   funzione delle capacità Cnor e Cexor .
   Si determinino quindi i valori delle capacità Cnor e Cexor e dei corrispondenti dimensionamenti Snor
   ed Sexor che minimizzano il ritardo al nodo Out e si calcoli il valore numerico del ritardo minimo.




3) (8 Punti). Noti i valori di Snor ed Sexor determinati al punto precedente, si calcoli il branching
   eﬀort bX al nodo X ed il ritardo dall’ingresso IN all’uscita Out2.
         Soluzione della Prova Scritta di Complementi di Elettronica II
                                             3 Dicembre 2007
1) I logical e parasitic eﬀort dei gate possono essere calcolati usando le consuete espressioni. Per il
   NOR a 3 ingressi si ha:              1 + 3"
                                 gnor =        = 2.33 pnor = 3pinv = 3.3
                                         1+"
   ottenuti per "=Øn0 /Øp0 =2.0.
   Per il NAND a 2 ingressi avremo:
                                             2+"
                                   gnand =       = 1.33      pnand = 2pinv = 2.2
                                             1+"
   mentre per l’EXOR a 2 ingressi:
                                    2 + 2"                  2(2 + 2")
                         gexor =           =2     pexor =             pinv = 4pinv = 4.4
                                    1+"                       1+"

   La capacità di ingresso al circuito è quella del NAND a due ingressi e vale:

                                    Cin = Cnand = Sn (1 + "/2)CM 1 = 5.2f F

2) Per ottenere l’espressione del ritardo al nodo Out notiamo che l’electrical eﬀort del NAND e del
   NOR valgono:
                                          Cnor + Cexor             CL
                                 hnand =                   hnor =
                                              Cin                 Cnor
   dove soltanto Cin è una capacittà nota. Il ritardo al nodo Out può essere espresso in unità di tp0
   come:
                                       Cnor + Cexor          CL
                          tad = gnand                + gnor      + Pnand + Pnor
                                           Cin              Cnor
   e risulta sempre crescente all’aumentare di Cexor mentre presenta un minimo in funzione di Cnor .
   Siccome il gate EXOR rappresenta soltanto una capacità di carico in relazione al percorso di segnale
   verso Out, non risulta sorprendente che il dimensionamento ottimo del gate EXOR risulti quello
   minimo, cioè Sexor =1, a cui corrisponde Cexor =Sexor (1 + ")CM 1 =3.9f F . Il valore di Cnor che
   minimizza il ritardo, invece, si ottiene annullando la derivata di tad rispetto a Cnor . Cosı̀ facendo
   otteniamo:                             q
                                  Cnor = Cin CL (gnor /gnand ) = 27.3f F
   a cui corrisponde Snor =Cnor /[CM 1 (1 + 3" CM 1 )]'3.
   Sostituendo il valore ottimo di Cnor nell’espressione del ritardo otteniamo tad =20.5 e tp =tad ·
   tp0 =184.5[ps].

3) Noto il dimensionamento del gate NOR, il branching eﬀort al nodo X in relazione al percorso di
   segnale da In a Out2 vale:
                                                 Cnor
                                       bX = 1 +        =8
                                                 Cexor
   ed il ritardo può essere calcolato come:
                                               Cexor         CL2
                             tad = gnand bX          + gexor       + Pnand + Pexor
                                               Cnand         Cexor

   che fornisce tad =28.44 e tp =tad · tp0 =256[ps].
                   Cognome e Nome
                      Matricola
                        Data                         4 Febbraio 2010

                   Prova Scritta di Complementi di Elettronica Digitale
                                     4 Febbraio 2010
Sia VDD =1.8V e si assumano i seguenti parametri tecnologici per i MOSFET:

                                 Parametro       n-MOSFET      p-MOSFET
                                   VT O [V]         0.35          -0.35
                                 Ø 0 [µA/V2 ]       300            150
                                   ∞[V1/2 ]           0             0
                                 LM IN [µm]         0.18           0.18
                                Cox [fF/µm2 ]        13             13
                                CGS0 [fF/µm]         0.6           0.6
                                CJ0 [fF/µm2 ]        3.2           3.2
                                       Keq          0.75           0.75
                                      LSD          2LM IN        2LM IN

Se non diversamente specificato si assuma per tutti i transistori L=LM IN e nel calcolo dei
transitori si consideri la transizione completata al 90% della escursione totale del segnale.
                       φ1                                     φ2                           Q

               D              A I1              I2
                                                        X              B   I3         I4
                       M1                                     M3
                                       M2                                       M4


                                        φ2                                      φ1
                              Latch1                                   Latch2
Il circuito in figura deve realizzare un registro a campionamento sul fronte positivo di ¡1 con fasi ¡1 e ¡2
prive di overlap per avere immunità alle sovrapposizioni delle stesse. Si impone Sn =1 per gli n-MOSFETs
e Sp ="=Øn0 /Øp0 per i p-MOSFETs.

  1) (12 Punti). Disegnare qualitativamente l’andamento delle fasi ¡1 e ¡2 , indicando chiaramente
     l’istante di campionamento. In aggiunta si indichi l’andamento delle tensioni ai nodi X e Q cor-
     rispondente al campionamento di D=1 quando il dato precedentemente memorizzato è Q=0.
2) (10 Punti). Si determini il tempo di set-up tSU nel caso in cui si campioni D=1 con Q=0, motivando
   chiaramente il criterio usato per definire il tSU stesso. A tal fine si supponga che la capacità ai nodi
   A, X e B sia schematizzabile come la sola Cinv dell’invertitore a valle e che la capacità vista dagli
   invertitori I2 e I4 sia la somma delle capacità parassita tra gate e drain CGDp e della capacità di
   giunzione CJ del pass-transistor pilotato.




3) (8 Punti). Supponendo che il periodo T delle fasi sia pari a 1 ns e che ¡1 e ¡2 abbiano un andamento
   temporale come quello riportato in figura, si determini il ritardo t¡°Q dall’istante di campionamento
   a quello in cui il dato è disponibile in uscita per la transizione analizzata al punto 2. Si motivi
   chiaramente il criterio usato per definire il t¡°Q stesso.
                                                  T
                            φ1


                                         0.3T                               t
                                  0.2T          0.2T
                            φ2


                                                                            t
                                  Soluzione della Prova Scritta

                                           4 Febbraio 2010
1) Se ¡1 =0 e ¡2 =1 il latch 1 è trasparente mentre il latch 2 è in hold. Quando ¡1 =¡2 =1 entrambi
   i latch sono in hold. Quindi il valore di D campionato dal circuito è quello in corrispondenza del
   fronte di salita di ¡1 . Nel caso in cui ¡1 =1 e ¡2 =0 il latch 1 è in hold mentre il latch 2 è trasparente.
   Di conseguenza il dato campionato viene portato all’uscita Q.
   Si noti come la configurazione ¡1 =¡2 =0 sia quella in cui si avrebbe la corsa critica. Questo viene
   evitato mediante l’uso di fasi senza overlap. Gli andamenti qualitativi delle fasi e delle tensioni ai
   diversi nodi corrispondenti al campionamento di D=1 quando il dato precedentemente memorizzato
   è Q=0 sono riportati in figura.

                                φ1


                                                                                t
                                φ2



                                 A                                              t




                                 X                                          t




                                B                                           t




                                Q                                           t




                                                                            t

2) Il tempo di set-up tSU è il tempo in cui il dato in ingresso deve rimanere stabile aﬃnchè venga
   campionamento correttamente. In questo circuito il dato campionato deve propagarsi attraverso il
   transistor M 1, i due invertitori I1 e I2 fino al transistor M 2 aﬃnché l’accensione di quest’ultimo
   riproponga sul nodo A il dato campionato. Ne risulta che tSU =tp,M 1 +tp,I1 +tp,I2 dove tp,M 1 è il
   ritardo del pass-transistor M1 mentre tp,I1 e tp,I2 sono rispettivamente i ritardi dell’invertitore I1 e
   I2 .
   Le capacità del circuito possono essere valutate nel seguente modo. La capacità di giunzione del
   transistore M2 è :
                                 Cj,M 2 = Sp LM IN LSD Keq Cj0 = 0.311 fF
   dove LSD vale 2LM IN , mentre la componente parassita della capacità gate-drain vale:

                                     CGDp,M 2 = Sp LM IN CGS0 = 0.216 fF

   Quindi la capacità prodotta dal transistore M 2 è pari a

                                     Cp,M 2 = Cj,M 2 + CGDp,M 2 = 0.527 fF
   La capacità di ingresso degli invertitori vale invece semplicemente:

                                          Cinv = Sn (1 + ") CM = 1.912 fF

   con CM = L2M IN Cox + 2LM IN CGS0 = 0.637 fF.
   I ritardi parziali risultano essere:
                                              2 Cinv
                                  tp,M 1 =              F (|VT,p |/VDD ) = 14.05 ps
                                             Sp Øp0 VDD

                                               2 Cinv
                                   tp,I1 =              F (VT,n /VDD ) = 14.05 ps
                                             Sn Øn0 VDD
                                              2 Cp,M 2
                                  tp,I2 =               F (|VT,p |/VDD ) = 3.875 ps
                                             Sp Øp0 VDD

   Quindi risulta che tSU = 31.98 ps.

3) Nelle condizioni indicate nel testo si ha che

                                          t¡°Q = ∆t¡1 ",¡2 # + tp,M 3 + tp,I3

   dove ∆t¡1 ",¡2 # = 0.2T = 0.2 ns, e tp,I3 =tp,I1 = 14.05 ps. Per il calcolo di tp,M 3 si noti che il transistore
   M3 è saturo per tutto il transitorio di scarica della capacità d’ingresso Cinv di I3 . Il transitorio
   termina quando M3 si spegne cioé quando VGS =°|VT,p |. Il transitorio è governato dalla equazione
   diﬀerenziale °Cinv (dVB /dt)=(Øp0 Sp /2)(VB (t) ° |VT,p |)2 =IM 3 dove VB =°VGS del transistore M3 .
   Per separazione di variabili si ottiene:
                                               ∑                            ∏
                                     2Cinv     1             1
                             tp,M 3 = 0                °              = 79.1 ps
                                     Øp Sp Vf ° |VT,p | Vin ° |VT,p |

   dove la tensione iniziale del transitorio è Vin =VDD mentre quella finale si ottiene al 90% della
   escursione come Vf = VDD ° 0.9(VDD ° |VT,p |)=0.495 V.
   Risulta quindi t¡°Q = 0.293 ns.
                 Cognome e Nome
                    Matricola
                      Data                         5 Settembre 2006



                      Prova Scritta di Complementi di Elettronica II
                                          5 Settembre 2006
Sia VDD =2.5V e si assumano i seguenti parametri tecnologici per i MOSFET:

                    Parametro    n-MOSFET       p-MOSFET        n-MOS a Svuotamento
                      VT O          0.4 [V]       -0.4 [V]             -1.0[V]
                        Ø0       476 [µA/V2 ]   230 [µA/V2 ]        400 [µA/V2 ]
                        ∏              0              0                   0

Si riportino negli spazi bianchi all’interno del testo l’espressione analitica e, quando richiesto,
il valore numerico dei risultati.
Si consideri una interconnessione a basse perdite di cui sono note la capacitá c=6.67·10°2 f F/µm e la
resistenza r=0.05Ω/µm per unitá di lunghezza. La linea puó essere approssimata come un conduttore
isolato immerso nell’ossido di silicio, quindi la velocitá della luce nella interconnessione vale vl º1.5 ·
1010 cm/s.
    Si intende studiare il pilotaggio della interconnessione per mezzo di invertitori simmetrici nei ritardi
e realizzati per mezzo di transistori MOSFET i cui principali parametri sono riassunti in tabella. A tal
proposito si pongono i seguenti quesiti:

  1) (8 Punti). Si calcoli il valore della resistenza equivalente Rdr dell’invertitore a dimensionamento
     minimo ricavata dalla retta che, sul grafico delle caratteristiche di uscita del transistore n-MOS,
     unisce l’origine al punto in cui il transistore entra in saturazione. Si assuma inoltre nel resto dei
     calcoli una capacitá di ingresso Cdr =0.5f F per l’invertitore a dimensionamento minimo.
     Inoltre, in relazione alla interconnessione, si calcoli la sua impedenza caratteristica z0 ad alta
     frequenza (cioé per rø! l) ed il tempo di volo per micron di lunghezza tf l [s/µm].
2) (6 Punti). Sia Len =4.167mm la lunghezza della interconnessione e se ne studi il pilotaggio con-
   siderandola una linea di tipo RC, cioé trascurando le componenti induttive della linea stessa. Si
   calcoli il numero ottimo kott di stadi di buﬀering ed il dimensionamento hott degli invertitori per uno
   schema a dimensionamento ottimo. Si calcoli inoltre il ritardo T90% della interconnessioni (ottenuto
   trascurando gli eﬀetti induttivi, congruentemente con lo schema di pilotaggio utilizzato), sia per il
   caso di pilotaggio con buﬀer a dimensionamento minimo che per il caso di buﬀer a dimensionamento
   ottimo.




3) (10 Punti). Si riconsideri adesso il comportamento della interconnessione in considerazione delle
   componenti induttive. Utilizzando il valore di z0 ottenuto al punto (1) si calcoli il coeﬃciente di
   riflessione alla sorgente ΩS per ogni tratto di linea sia per il pilotaggio con buﬀer a dimensionamento
   minimo che per il pilotaggio con buﬀer a dimensionamento ottimo.
   Confrontando il tempo di volo sulla linea con i tempi T90% calcolati al punto (2) e considerando i
   valori di ΩS ad ogni sezione della interconnessione si discuta brevemente:

     a) La validtá e l’opportunitá dell’approccio di pilotaggio che trascura gli eﬀetti induttivi;
     b) L’attendibilitá quantitativa dei ritardi della interconnessione stimati per mezzo del T90% cal-
        colato al punto (2).

   Si distingua chiaramente la discussione dei punti (a) e (b) per il caso di dimensionamento minimo ed
   ottimo dei buﬀer oppure si indichi esplicitamente che le considerazione svolte valgono per entrambi
   i tipi di dimensionamento.
         Soluzione della Prova Scritta di Complementi di Elettronica II
                                           5 Settembre 2006
1) Il valore di Rdr per un invertitore a dimensionamento minimo calcolato in base al punto di ingresso
   in saturazione sulla caratteristica di uscita del transistore vale:
                                                         2
                                         Rdr =                         ' 2kΩ
                                                 1 · Øn0 (VDD ° VT )

   Nota la velocitá della luce vl º1.5 · 1010 cm/s nella interconnessione, il tempo di volo per micron
   di lunghezza vale tf l =1µm/vl º 6.67[f s/µm]. Inoltre la capacitá c e l’induttanza l per unitá di
   lunghezza sono legate dalla relazione c l=1/vl2 , quindi l’impedenza della interconnessione ad alta
   frequenza vale:                               s
                                                   l    1
                                           z0 '      =      ' 100Ω
                                                   c   c vl

2) Se consideriamo di pilotare la interconnessione come una semplice linea di tipo RC il numero ottimo
   di stadi ed il dimensionamento ottimo degli invertitori sono:
                                     r                                          s
                                            rc                                      Rdr c
                        kott = Len                  '5                 hott =             ' 73
                                         2.3Rdr Cdr                                 rCdr

   Se trascuriamo gli eﬀetti induttivi possiamo calcolare i tempi di commutazione al 90% in base
   alle espressione proprie delle interconnessioni di tipo RC. Per il caso di buﬀer a dimensionamento
   minimo si ha:
                                                 p
         T90% = Len [2.3(Rdr c + c Cdr ) + 2 2.3 Rdr Cdr r c] ' 0.314[ps/µm] £ Len [µm] ' 1308ps

   mentre per il dimensionamento ottimo otteniamo:
                                     p
                       T90% = 7.6 Rdr Cdr r c] ' 0.0139[ps/µm] £ Len [µm] ' 58ps

3) La resistenza del driver che pilota i kott =5 tratti di interconnessione vale Rdr =2kΩ nel caso di
   dimensionamento minimo e Rdr /hott =2kΩ/73'27.4Ω nel caso di dimensionamento ottimo. Nei due
   casi avremo quindi un coeﬃciente di riflessione alla sorgente pari a:
                               Rdr ° z0                                 Rdr /hott ° z0
                    ΩS,min =            ' 0.9                ΩS,ott =                  ' °0.57
                               Rdr + z0                                 Rdr /hott + z0

   Ricordiamo inoltre che il tempo di volo per micron di lunghezza della linea vale tf l =6.67f s/µm,
   quindi la somma dei tempi di volo nei cinque tratti di interconnessione vale tf l,tot =4167 · 6.67f s =
   27.8ps.
   Se consideriamo adesso il pilotaggio con buﬀer a dimensionamento minimo vediamo che il ritardo
   stimato considerando solo la parte RC della linea vale T90% = 1308ps, quindi é molto maggiore del
   tempo di volo sulla linea tf l,tot =27.8ps. Inoltre in questo caso abbiamo un coeﬃciente di riflessione
   ΩS,min = 0.9. Se ne deduce che, se la linea viene pilotata con buﬀer a dimensionamento minimo,
   allora i buﬀer hanno una resistenza talmente alta che gli eﬀetti induttivi sono trascurabili. Questo
   si traduce in un ΩS,min positivo e grande che conferisce ai transitori un andamento di tipo RC.
   Se consideriamo il pilotaggio con buﬀer ottimo, invece, il tempo di volo tf l,tot non é aﬀatto trascur-
   abile rispetto a T90% = 58ps. Inoltre ΩS,ott = °0.575 indica che alla sorgente ci sono ampie oscil-
   lazioni di tensione dovute ad una eccessiva conducibilitá del buﬀer. Se ne deduce che, se usiamo un
   grande dimensionamento per i buﬀer, allora la corrispondente resistenza é cosı́ bassa da invalidare
   l’ipotesi per cui si trascurano gli eﬀetti induttivi. In questo caso l’ipotesi usata per progettare il pi-
   lotaggio non risulta verificata a posteriori ed il settling time sulla interconnessione é molto superiore
   rispetto al tempo T90% calcolato al punto (2).
                   Cognome e Nome
                      Matricola
                        Data                        6 Aprile 2005



                             Prova Scritta di Elettronica Digitale
                                            6 Aprile 2005
Se non diversamente specificato si assuma per tutti i transistori L=LM IN .
Si riportino negli spazi bianchi all’interno del testo l’espressione analitica e, quando richiesto,
il valore numerico dei risultati.

Si consideri una tecnologia CMOS avente LM IN =0.3µm, Cox =8f F/µm2 , CGS0 =0.6f F/µm ed "=(Øn0 /Øp0 ) =
2. Sia inoltre ø =18ps il ritardo caratteristico della tecnologia secondo Metodologia del Logical EÆort e
pinv =1.4 il parasitic eÆort dell’invertitore.
    Con tale tecnologia si intende progettare il circuito per la decodifica di riga di una memoria Non-
Volatile per mezzo di gate Fully CMOS con ritardi simmetrici. Tale circuito ha per ingressi i 16 bits
A0 .. A15 degli indirizzi e deve pilotare in uscita la Word Line della memoria che é costituita da una
interconnessione di tipo RC a cui sono connesse le celle di memoria, ognuna delle quali introduce un
carico di tipo capacitivo come specificato in seguito. Piú precisamente si assuma che i parametri della
linea siano:
Larghezza W=0.7µm; Altezza H=0.6µm; Spessore dielettico tdi =0.5µm;
Costante Dielettr. ≤di =3.9; Resistivitá del materiale Ω=150µ≠ · cm
Inoltre si assuma che le celle di memoria introducano una capacitá Ccell =0.25f F e siano connesse ad una
distanza di 0.8µm l’una dall’altra. Ogni Word Line pilota 256 celle ed ha quindi una lunghezza pari circa
a Len ' 0.8 £ 256=205µm.

  1) (6 Punti). Si disegni il circuito al livello di gate che realizza WL=A0 A1 .. A15 . A tal scopo si
     devono usare soltanto gate di tipo NAND e NOR con fan-in pari a quattro.
2) (6 Punti). Si calcoli la capacitá c e la resistenza r per unitá di lunghezza della linea e la capacitá
   totale CW L della Word Line comprensiva della Cint della linea e della capacitá delle celle connesse.




3) (6 Punti). Supponendo che il gate di ingresso del decodificatore abbia i transistori nMOSFET
   dimensionati Sn =2 (ed i pMOS dimensionati per avere ritardi simmetrici), si calcoli il numero
   ottimo di stadi per pilotare la capacitá totale CW L della Word Line e quindi il numero di invertitori
   che é necessario aggiungere. Si calcolino quindi i dimensionamenti degli stadi (basta indicare la
   capacitá di ingresso di ogni stadio).




4) (8 Punti). Si calcoli la resistenza equivalente dell’invertitore che pilota la Word Line e quindi il
   ritardo complessivo fra l’ingresso del decodificatore e l’ultima cella connessa alla Word Line.
                 Soluzione della Prova Scritta di Elettronica Digitale
                                             6 Aprile 2005
1) Il circuito di decodifica deve essere organizzato usando gate con fan-in non troppo elevato e nel
   testo si suggerisce di usare NAND e NOR con fan-in di quattro. Utilizzando le note regole di De
   Morgan possimo scrivere:

              W L = A0 A1 ..A15 = A0 A1 A2 A3 + A4 A5 A6 A7 + A8 A9 A10 A11 + A12 A13 A14 A15

   e quindi il segnale W L puó essere ottenuto per mezzo di quattro NAND a 4 ingressi seguiti da un
   NOR a quattro ingressi.

2) La capacitá per unitá di lunghezza della linea puó essere espressa come:
                               "di          2º"di
                          c=       W+                  = 0.048 + 0.148 = 0.196f F/µm
                               tdi    ln[(4tdi + H)/H]

   mentre la resitivitá per unitá di lunghezza é:
                                                    Ω
                                             r=       = 3.57 Ω/µm
                                                   HW
   La capacitá e resistenza totale della linea sono quindi Cint =cLen '40.1f F e Rint =rLen =732Ω. La
   capacitá totale della linea, comprensiva della capacitá delle celle, é quindi CW L =Cint +256Ccell =104f F .

3) Il gate di ingresso del decodificatore é un NAND a 4 ingressi con Sn =2 e quindi dimensionamento
   del pMOS Sp =("/4)Sn =1. La sua capacitá di ingresso é quindi Cin =CM 1 (2 + 1)=3.24f F dove
   CM 1 =Cox L2M IN +2CGS0 LM IN = 1.08f F . L’electrical eﬀort vale quindi H = CW L /Cin =32.. I logical
   e parasitic eﬀort dei gate sono:
                           1 + 4"                     4+"
                 gnor4 =          =3      gnand4 =        =2      pnand4 = pnor4 = 4pinv = 5.6
                            1+"                       1+"
   Il Path Eﬀort complessivo é quindi F=GH=gnand4 gnor4 H=192.
   Dato pinv =1.4 lo Stage Eﬀort ottimo risulta Ω ' 0.71pinv + 2.82=3.8 ed il numero ottimo di stadi
   é quindi N̂ = ln(F )/ln(Ω)=3.93. p
                                     Scelgo quindi N̂ = 4 che richiede di inserire due invertitori e di
   usare uno stage eﬀort pari a fˆ = 4 F = 3.72.
   Indicando con Inv1 l’invertitore che pilota direttamente la Word Line avremo quindi Cinv1 =
   CW L /fˆ = 28f F . Per il secondo invertitore si ha Cinv2 = CW L /fˆ2 = 7.51f F mentre per il NOR a
   quattro ingressi Cnor4 = (gnor4 Cinv2 )/fˆ = 6.06f F .

4) L’invertitore Inv1 ha capacitá di ingresso Cinv1 = 28f F e quindi la sua resistenza equivalente per
   la metodologia del Logical Eﬀort vale Rinv1 =ø /Cinv1 =643Ω.
   Il ritardo complessivo puó essere stimato considerando il ritardo fra un ingresso del decodificatore e
   l’ingresso dell’invertitore Inv1 che pilota la linea sommato al tempo necessario ad Inv1 per pilotare
   la interconnessione fino alla sua intera lunghezza Len , cioé dove é connessa l’ultima cella.
   Il primo ritardo é:

          td (Ai ! Inv1) = ø [3fˆ + pnand4 + pnor4 + pinv ] = (11.16 + 9 · 1.4)ø = 23.76ø ' 428ps

   mentre il ritardo di pilotaggio della linea da parte di Inv1 puó essere stimato come:
                                                  Rinv1
                                   T90% = 2.3 ·         CW L + Rint CW L ' 143ps
                                                   2.3
   ed il ritardo compessivo é quindi 571ps. Nel calcolo del ritardo si é assimilats la capacitá delle celle
   connesse alla linea ad una capacitá distribuita da aggiungere a quella della interconnessione. Visto
   il gran numero di celle posizionate molto vicine questa approssimazione sembra ragionevole.
                  Cognome e Nome
                     Matricola
                       Data                         8 Settembre 2004



                             Prova Scritta di Elettronica Digitale
                                          8 Settembre 2004
Sia VDD =2.5V e si assumano i seguenti parametri tecnologici per i MOSFET:

                                  Parametro    n-MOSFET       p-MOSFET
                                    VT O          0.4 [V]        -0.4 [V]
                                      Ø0       500 [µA/V2 ]   200 [µA/V2 ]
                                     Cox       14 [fF/µm2 ]   14 [fF/µm2 ]
                                     Cj0        7 [fF/µm2 ]    7 [fF/µm2 ]
                                    LM IN        0.25[µm]       0.25[µm]

Se non diversamente specificato si assuma per tutti i transistori L=LM IN .
La figura illustra un circuito in cui un Gate CMOS pilota direttamente una interconnessione di tipo
RC. Per la interconnessione si possono assumere una resistenza per unitá di lunghezza r=1.0[Ohm/µm]
ed una capacitá per unitá di lunghezza c=1.4[f F/µm]. La lunghezza della linea é Len =200µm. Come
inidcato anche in figura la capacitá di caricoi CO a valle della linea é molto minore della capacitá della
linea Cint .

                                          VDD
                             A                  B

                                  C
                                                       r, c

                              A                                   CO << Cint
                                                C
                              B



  1) (8 Punti). Con riferimento ai parametri indicati nella tabella, si calcolino il ritardo caratteristico ø
     della tecnologia, nonché la resistenza equivalente Rinv e la capacitá di ingresso Cinv di un buﬀer a
     dimensionamento minimo. Assumendo inolte che la lunghezza delle regioni di source e drain siano
     LS =LD =3LM IN , si calcoli il Parastic Eﬀort pinv dell’Inverter.
2) (6 Punti). Si calcolino il Logical Eﬀort ed il Parasitic Eﬀort del Gate in figura.




3) (6 Punti). Si supponga ora di usare per il Gate il massimo dimensionamento intero (S=1, 2, 3 ...)
   compatibile con una capaictá di ingresso CIN < 10f F e di pilotare la interconnessione direttamente
   col Gate. Si stimi il ritardo di pilotaggio della interconnessione.




4) (6 Punti). Per questo tipo di interconnessione e di Driver l’aggiunta di Buﬀer fra l’uscita del Gate
   e la interconnessione puó essere una buona tecnica per ridurre il ritardo complessivo del circuito ?
   Si risponda in modo breve ma motivato alla precedente domanda e si indichino eventualmente il
   numero ed i dimensionamenti dei Buﬀer.
                 Soluzione della Prova Scritta di Elettronica Digitale
                                          8 Settembre 2004
1) Per la tecnologia in esame la simmetria dei ritardi nell’Inverter impone un dimensionamento relativo
   fra pMOSFET ed nMOSFET pari ad Æinv = Øn0 /Øp0 = 2.5. La capacitá di ingresso per un Inverter
   a dimensionamento minimo é quindi subito data da Cinv = (1 + 2.5)Cox L2M IN =3.06f F . Il ritardo
   caratteristico puó essere calcolato considerando per un Inverter una capacitá di carico pari alla
   capacitá di ingresso. Riferendoci ad un Inverter a dimensionamento minimo otteniamo:
                                              2Cinv
                                        ø=           F (VT /VDD ) = 9.16ps
                                             Øn0 VDD

   Per la resistenza equivalente dell’Inverter ad area minima si ha dunque Rinv = ø /Cinv =2990Ohm.
   Se le lunghezze LS = LD = 3LM IN allora la capacitá delle giunzioni per un Inverter ad area minima
   é Cd =(1 + Æinv )3L2M IN Cj0 e quindi il Parasitic EÆort vale pinv =Cd /Cg =3Cj0 /Cox =1.5.

2) Sia nel caso peggiore di salita che nel caso peggiore di discesa abbiamo due transistori in serie.
   Quindi per ottenere una simmetria di ritardi dobbbiamo imporre ÆG = Øn0 /Øp0 = 2.5. Per calcolare
   il Logical EÆort del Gate notiamo che, per avere la stessa resistenza equivalente di un Inverter con
   dimensionamento di Pull-Down Sinv il Gate deve avere dimensionamento di Pull-Down SG =2Sinv .
   Dal rapporto fra la capacitá di ingresso del Gate e quella dell’Inverter otteniamo quindi un Logical
   EÆort pari a 2. Per quanto rigiarda il Parasitic EÆort, due transistor nMOS ed un transistor p-
   MOS sono connessi all’uscita. Inoltre, per avere stessa resistenza dell’Inverter dimensionato Sinv ,
   gli n-MOS dovranno essere dimensionati Sn =2Sinv ed i p-MOS Sp =2ÆG Sinv =5Sinv . Il Parasitic
   EÆort sará dunque dato da:
                                             2 · 2Sinv + 5Sinv
                                      PG =                     £ pinv = 3.86
                                              (1 + Æinv )Sinv

3) La capacitá di ingresso del Gate é proporzionale al dimensionamento Sn dei transistori nel Pull-
   Down secondo CIN = Sn (1 + ÆG )L2M IN Cox =3.06 ·Sn [f F ]. Il massimo dimensionamento intero
   compatibile con CIN < 10f F é quindi Sn =3 a cui corrisponde CIN =9.2f F . siccome sappiamo
   che la resistenza equivalente RG del Gate in esame é uguale alla resistenza Rinv di un inverter ad
   area minima (calcolata al punto (1)) quando Sn =2 ed inoltre sappiamo che RG é inversamente
   proporzionale ad Sn , allora la resistenza equivalente del Gate per Sn =3 sará semplicemente RG =
   (2/3)Rinv ' 1990Ohm. Se la linea viene quindi direttamente pilotata dal Gate, il ritardo di
   pilotaggio al 90% della escursione risulta:
                                  RG
                     Ttot ' 2.3       cLen + rcL2en = TDR + Tint = 560 + 56[ps] = 616[ps]
                                  2.3
   dove TDR indica il ritardo relativo alla resistenza del Driver per la capacitá di interconnessione
   mentre Tint é il ritardo intrinseco di interconessione. Nella scrittura del ritardo si é tenuto conto
   del fatto che la capacitá a valle della linea é trascurabile rispetto a quella della linea stessa.

4) Siccome in questa situazione il ritardo del Driver é di gran lunga dominante, il ritardo complessivo
   puó essere migliorato in modo sensibile aggiungendo dei BuÆer a valle Gate. Visto che il ritardo
   intrinseco della linea e’ piuttosto piccolo (perché la resistivitá r é bassa), allora posso organizzare
   i BuÆer come se la linea fosse una pura capacitá Cint = Len c = 280f F . A questo punto, nota
   la capacitá di ingresso del gate CIN =9.18f F , posso calcolare il Path EÆort complessivo come
   F=g · (Cint /CIN )'61. Lo Stage EÆort ottimo puó essere stimato come Ω̂ = 0.71pinv + 2.82=3.88 da
   cui ottengo un numero ottimo di stadi N̂ =lnF/lnΩ=3.03. Scelgo quindi N̂ =3 con Ω = F 1/3 =3.94.
   Si tratta quindi di aggiungere due Inverter con dimensionamenti (espressi in termini di capacitá di
   ingresso) pari a C1 = Cint /Ω=71fF e C2 = Cint /Ω2 =18 fF.
   In questo modo la resistenza equivalente del BuÆer che pilota la interconnessione é pari a R1 =
   Rinv (Cinv /C1 )=129Ohm ed il tempo di pilotaggio relativo al BuÆer scende a 2.3(R1 /2.3)cLen =83.1[ps].
Naturalmente il ritardo complessivo consta adesso anche dei ritardi dei BuÆer, quindi nel complesso
si ha:
                                   R1
Ttot = ø (2Ω + PG + Pinv ) + 2.3       cLen + rcL2en = 9.16(2 · 3.94 + 3.86 + 1.5) + 36 + 56 [ps] = 213 [ps]
                                   2.3
                  Cognome e Nome
                     Matricola
                       Data                           10 Gennaio 2007



                       Prova Scritta di Complementi di Elettronica II
                                              10 Gennaio 2007
   Si assumano i seguenti parametri tecnologici per i MOSFET:

                                  Parametro       n-MOSFET       p-MOSFET
                                    VT O            0.35 [V]       -0.35 [V]
                                      Ø0          200 [µA/V2 ]   80 [µA/V2 ]
                                    LM IN           0.18[µm]       0.18[µm]
                                     Cox          15[fF/µm2 ]    15[fF/µm2 ]
                                    CGS0          0.8 [fF/µm]    0.8 [fF/µm]

Si riportino negli spazi bianchi all’interno del testo l’espressione analitica e, quando richiesto,
il valore numerico dei risultati.
In figura si mostra un gate CMOS che indicheremo col simbolo G1 e che implementa la funzione logica
F =A(B©C). Il circuito è dimensionato in modo che il tempo di salita di caso peggiore sia uguale al
tempo di discesa di caso peggiore. La tecnologia CMOS di fabbricazione è caratterizzata da un ritardo
ø =9ps e da un parasitic eﬀort dell’invertitore pari a pinv =0.95. Si supponga che i segnali siano disponibili
sia in forma vera che in forma negata.

                                VDD
                        B                 C

                        C                 B


                            A                                        A
                                          F(A,B,C)                   B     G1
                                                                     C
                                      B       B
                       A
                                      C       C




  1) (8 Punti). Si determinino il logical eﬀort gG1 ed il parasitic eﬀort pG1 del gate G1.
2) (8 Punti). Si disegni lo schema a livello gate del circuito che realizza la funzione logica
   F =[A(B © C) + D]EF facendo uso del gate G1, di un NAND, di un NOR e di un invertitore.
   Si supponga inoltre che il gate G1 abbia il dimensionamento necessario aﬃnché la sua resistenza
   equivalente sia pari a quella di un invertitore ad area minima e si calcoli la capacità di ingresso CG1
   del gate ed il path eﬀort del circuito supponendo che la capacità di carico sia CL =500f F .




3) (8 Punti). Si valuti la necessitá di aggiungere invertitori al circuito per migliorarne le prestazioni
   dinamiche e si determinino i dimensionamenti dei gate che minimizzano il ritardo complessivo.
          Soluzione della Prova Scritta di Complementi di Elettronica II
                                            10 Gennaio 2007
1) Indichiamo con Sn ed Sp i dimensionamenti dei transistori n-MOS e p-MOS del gate G1. Nel
   transitorio di discesa di caso peggiore il dimensionamento equivalente del pull-down vale Sn,eq =Sn /2
   mentre il dimensionamento del pull-up nella salita di caso peggiore vale Sp,eq =Sp /3. Aﬃnchè i tempi
   di salita e discesa di caso peggiore siano uguali dobbiamo quindi avere Sp =(3/2)"Sn =3.75Sn , in
   quanto "=Øn0 /Øp0 vale 2.5. Per uguagliare il ritardo di caso peggiore del gate G1 ad un invertitore
   con dimensionamento minimo è necessario Sn =2, quindi Sp =3.75Sn =7.5. Dunque, quando Sn vale
   2, la capacità di ingresso di G1 vale CG1 =2(1 + 3.75)CM 1 , inoltre al nodo di uscita sono connessi
   tre transistori n-MOS con dimensionamento Sn =2 ed un p-MOS con dimensionamento Sp =7.5.
    Le precedenti considerazioni consentono di calcolare il logical e parasitic eﬀort di G1 come:
                  2(1 + 3.75)CM 1                      Sp + 3Sn        7.5 + 3 · 2
         gG1 =                    = 2.71       pG1 =            pinv =             pinv = 3.86pinv = 3.66
                    (1 + ")CM 1                         (1 + ")        (1 + 2.5)

2) Il circuito in figura realizza la funzione logica richiesta usando il gate G1.
                      A
                      B     G1
                      C                                I1                           F
                                 D                            E
                                                              F
                                                                                        CL


    Aﬃnché il gate G1 abbia un ritardo uguale ad un invertitore ad area minima é necessario che abbia
    Sn =2 ed Sp =3.75 · 2=7.5. La capacitá di ingresso del gate risulta quindi:

                 CG1 = (2 + 7.5)CM 1 = 7.35f F         CM 1 = Cox L2M IN + 2LM IN CGS0 = 0.774f F

    Per calcolare il path-eﬀort F del circuito complessivo sono necessari il logical eﬀort di tutti i gate.
    Per il NAND ed il NOR avremo:
                                          1 + 2"                         3+"
                                 gnor =          = 1.71       gnand =        = 1.57
                                           1+"                           1+"
    Nota la capacità di ingresso di G1 vale 7.35f F e quella di carico CL =500f F , possiamo calcolare il
    path eﬀort come:
                                                                  500
                                  F = G H = gG1 · gnor · gnand ·      ' 495
                                                                 7.35
3) Lo stage eﬀort ottimo per la tecnologia in esame vale Ω'0.71pinv +2.82=3.47, quindi il numero
   ottimo di stadi per il path eﬀort del circuito considerato vale N̂ =ln(F )/ ln(Ω)=4.98. É dunque
   opportuno che il circuito abbia almeno 5 stadi e risulta quindi conveniente aggiungere un invertitore.
                                                                                               p
   Lo stage eﬀort fˆ che minimizza il ritardo considerando cinque stadi di logica risulta fˆ= 5 F =3.46,
   che praticamente coincide col valore ottimo Ω. Noto lo stage eﬀort ottimo fˆ ed indicando con I2
   l’invertitore aggiunto rispetto al circuito in figura, otteniamo i dimensionamenti (espressi in termini
   di capacitá di ingresso):
                      CL                              gnand CI2                     Cnand
             CI2 =       = 144.5f F         Cnand =             ' 65.6      CI1 =         = 18.95f F
                      fˆ                                  fˆ                          fˆ
    ed infine:
                                                       gnor CI1
                                              Cnor =            ' 9.36
                                                          fˆ
    Si verfica che il dimensionamento del gate G1 calcolato come gG1 Cnor /fˆ risulta congruente col
    valore usato per il calcolo dei dimensionamenti.
                  Cognome e Nome
                     Matricola
                       Data                          16 Giugno 2014

                       Prova Scritta di Complementi di Elettronica II
                                            16 Giugno 2014
Si assumano i seguenti parametri tecnologici per i MOSFET:

                                 Parametro     n-MOSFET        p-MOSFET
                                   VT O          0.45 [V]        -0.45 [V]
                                     β!        180 [µA/V2 ]    120 [µA/V2 ]
                                    Cox        13 [fF/µm2 ]    13 [fF/µm2 ]
                                   CGS0        0.6 [fF/µm]     0.6 [fF/µm]
                                   LM IN         0.09[µm]        0.09[µm]

Se non diversamente specificato si assuma per tutti i transistori L=LM IN . Si riportino
negli spazi bianchi all’interno del testo l’espressione analitica e, quando richiesto, il valore
numerico dei risultati.
In figura si mostra un circuito in cui tutti i gate sono realizzati in tecnologia Fully CMOS e sono dimen-
sionati in modo da avere tempi di salita e discesa uguali.

                IN                                                                 O1

                                                                                         CL
                 Cin

  1) (10 Punti). In base ai parametri tecnologici riportati in tabella si calcolino il ritardo caratteristico
     della tecnologia tp0 per VDD =1.0V e la capacità di ingresso Cin , sapendo che i transistori nel
     pull-down del NAND in ingresso hanno dimensionamento pari a 3.
     Si supponga quindi noto il parasitic effort dell’invertitore pinv =0.9 e si calcoli il logical e parasitic
     effort dei gate usati nel circuito.
2) (8 Punti). Supponendo che la capacità di carico sia CL =35fF, si determini il numero ottimo degli
   stadi e l’eventuale opportunità di inserire invertitori. Si determini quindi il dimensionamento ottimo
   di tutti i gate (espresso in termini della loro capacità di ingresso), ed il corrispodente ritardo del
   circuito.




3) (10 Punti). In questo punto di intende analizzare l’energia per ciclo di clock consumata nel circuito
   considerando la energia dinamica, Edyn , e l’energia dovuta alle Iof f dei transistori, Elkg . Per
   semplificare l’analisi si può procedere come segue:

      – Per la Edyn si supponga che l’energia in ogni nodo interno al circuito sia stimabile usando la
        sola capacità di ingresso del gate a valle e che l’attività di commutazione sia α=0.15 in ogni
        nodo;
      – Per la Elkg si consideri il solo contributo degli invertitori (che è comunque dominante rispetto
        agli altri gate), e si supponga che i transistori nello stato OF F abbiano corrente Iof f =S Iof f 1 ,
        dove S è il dimensionamento e Iof f 1 =3 nA è la corrente OF F di un transistore a dimension-
        amento minimo. La corrente statica dei due invertitori si può stimare come media delle Iof f
        del caso in cui l’uscita circuito è alta oppure bassa.
        Si calcoli infine Elkg =100·tp0 ·Pst , dove Pst è appunto la potenza statica dell’invertitore.

   Si determinino Edyn e Elkg per VDD =1.0V e si dica come ci si attende che vari il rapporto Elkg /Edyn
   al ridursi della tensione di alimentazione VDD .
         Soluzione della Prova Scritta di Complementi di Elettronica II
                                            16 Giugno 2014
1) Per VDD =1.2V il ritardo caratteristico della tecnologia vale
                                                2Cinv1 F (VT /VDD )
                                        tp0 =                       ! 21.2ps
                                                     βn! VDD
   dove ε=βn! /βn! =1.5, inoltre, siccome per VT =0.45V e VDD =1.0V , si ha F(VT /VDD )=3.58 e la ca-
   pacità di ingresso dell’invertitore a dimensionamento risulta invece

           Cinv1 = (1 + ε)CM 1 = 0.533f F                CM 1 = Cox L2M IN + 2LM IN CGS0 = 0.213f F

   La capacità di ingresso del circuito coincide con la capacità di ingresso del gate NAND, i cui
   transistori di tipo n-MOS hanno dimensionamento pari a due. Nota la topologia del gate, la
   capacità di ingresso risulta

                                Cin = (1 + ε/3)Sn,N AN D CM 1 = 0.960f F

   dove Sn,N AN D =3 è il dimensionamento dei transistori nel pull-down del NAND in ingresso.
   I logical effort sono:
                                                3+ε                    (2 + 2ε)
                                    gnand =         = 1.8    gxnor =            =2
                                                1+ε                     (1 + ε)
   inoltre i parasitic effort sono pnand =3pinv !2.7 e pxnor =4pinv =3.6.
2) Il logical effort del percorso di segnale vale G=gxnor gnand =3.6, mentre l’electrical effort risulta
   H=C1 /Cin =36.5. Il path effort complessivo è quindi F =GHbx !131. Noto pinv =0.9, lo stage effort
   ottimo della tecnologia risulta ρ=2.82 + 0.71pinv =3.46, quindi il numero ottimo di stadi risulta
   N̂ =F 1/3 =3.93. Scegliamo di √ usare quattro stadi e dobbiamo quindi aggiungere 2 invertitori. Lo
   stage effort ottimo risulta fˆ= 4 F =3.38.
   Noto il valore di fˆ si possono calcolare dimensionamenti degli stadi:
                            C1                 CI1                   gxnor CI2
                  CI1 =        = 10.3f F CI2 =     = 3.05f F Cxnor =           = 1.80f F
                            fˆ                  fˆ                      fˆ
   dove I1 è l’invertitore che pilota C1 , mentre I2 è quello che lo precede.
   Il ritardo complessivo vale quindi:

                             tp = tp0 (4fˆ + pxnor + pnand + 2pinv ) ! 21.6 tp0 ! 459ps.

3) La Edyn può essere immediatamente stimata in base a quanto suggerito nel testo come
                                      2
                            Edyn = α VDD (Cin + Cxnor + CI2 + CI1 + CL ) ! 7.67f J

   Per l’energia legata alla Iof f ho bisogno dei dimensionamenti dei transistori negli invertitori, che
   sono
                                        CI1                      CI2
                            Sn1 =               ! 19.4 Sn2 =             ! 5.7
                                    (1 + ε)CM 1              (1 + ε)CM 1
   Dette IOH e IOL la somma delle correnti statiche degli invertitori quando l’uscita del circuito
   èrispettivamente alta e bassa, avremo

          IOH = Sn1 Iof f 1 + ε Sn2 Iof f 1 ! 83.9nA Iof f 1 IOL = ε Sn1 Iof f 1 + Sn2 Iof f 1 ! 104.4nA

   e quindi la corrente media è Iavg =(IOH + IOL )/2=94.2 nA. L’energia dovuta alle Iof f dei transistori
   risulta quindi
                                       Elkg = 100 tp0 VDD Iavg ! 0.20f J
   Riducendo la VDD la Edyn si riduce e tp0 aumenta, quindi il rapporto Elkg /Edyn aumenta sensibil-
   mente.
                 Cognome e Nome
                    Matricola
                      Data                           17 Settembre 2007



                                Prova Scritta di Elettronica Digitale
                                           17 Settembre 2007
Si riportino negli spazi bianchi all’interno del testo l’espressione analitica e, quando richiesto,
il valore numerico dei risultati.
In figura è riportato un albero costituito da interconnessioni di tipo RC. La capacità per unità di lunghezza
vale c=0.45f F/µm e la resistenza per unità di lunghezza vale r=19.83Ω/µm. L’albero è pilotato da
un driver a dimensionamento minimo che ha resistenza equivalente RDR =2.1kΩ e capacità di ingresso
CDR =5f F . La lunghezza dei tre rami di interconnessione è indicata in figura, le capacità al termine dei
rami sono CA =80f F e CB =110f F .

                                                     A
                                                                     CA
                                              30um
                                 Driver                   A’
                           IN                                               B

                                                                                CB
                                             30um        B’ 30um


  1) (10 Punti). Si supponga di sostituire ogni tratto di interconnessione di lunghezza 30µm con una
     cella a parametri concentrati di tipo L e si calcoli il valore RI e CI della resistenza e della capacità
     della cella ad L. Si disegni il circuito che descrive il driver e le celle ad L che schematizzano le linee
     RC. Utilizzando le costanti di tempo dominanti fornite dalla regola di Elmore, si determinino i
     ritardi TA e TB al 90% della escursione di segnale al nodo A e B.
   I valori diversi della capacità di carico CA e CB producono ritardi diversi TA e TB . Allo scopo di
   equalizzare i ritardi e ridurne i valori si vuole inserire un driver alle sezioni A0 e B 0 di accesso ai
   rami A e B.

2) (8 Punti). Indicando con hA ed hB il dimensionamento dei driver alle sezioni A0 e B 0 , rispettiva-
   mente, si esprimano i ritardi TA e TB in funzione di hA ed hB e si determini la relazione fra hA ed
   hB necessaria per avere TA =TB .
   Allo scopo di ottenere un’espressione compatta del risultato utile anche per il punto seguente, si
   suggerisce di esprimere il legame fra hA ed hB nella forma:
                                                 1        k2
                                                   = k1 +
                                                hA        hB
   indicando le espressioni dei coeﬃcienti k1 e k2 .




3) (8 Punti). Sfruttando il legame fra hA ed hB trovato al punto precedente si esprima TB in funzione
   del solo hB . Si indichi, motivando brevemente la risposta, se si ritiene che il valore cosı̀ ottenuto di
   TB abbia un valore minimo rispetto ad hB e si calcoli TB per hB =2, 4 e 6.
                Soluzione della Prova Scritta di Elettronica Digitale
                                           17 Settembre 2007
1) La resistenza e la capacità per un tratto di interconnessione lungo 30µm sono Rint =595Ohm e
   Cint =15.75f F . Se schematizziamo ogni tratto di linea di 30µm con una singola cella ad L otteni-
   amo quindi RI =Rint =595Ohm e CI =Cint =15.75f F . Sostituendo le celle ad elementi concentrati
   otteniamo il circuito indicato in figura (dove CI e RI indicano CI ed RI , rispettivamente, mentre
   RDR indica la resistenza RDR del driver a dimensionamento minimo).




                                                          CA
                                                 A
                                IN                        CI
                                                 RI

                                     RDR
                                           RI    X             RI            B
                                            CI                      CI            CB


   Facendo uso della regola di Elmore per stimare la costante dominante ai nodi A e B si ottiene:

           øA = (RDR + RI )CI + (RDR + RI )(CI + CB ) + (RDR + 2RI )(CI + CA ) = 696[ps]

           øB = (RDR + RI )CI + (RDR + RI )(CI + CA ) + (RDR + 2RI )(CI + CB ) = 714[ps]
   I ritardi al 90% della escursione di segnale sono quindi TA =2.3øA =1.6ns e TB =2.3øB =1.64ns.

2) L’inserimento dei driver all’inizio dei due rami fa in modo che ogni ramo contribuisca alla costante
   di tempo dell’altro soltanto tramite la capacità di ingresso del suo driver. Le espressioni per le
   costanti di tempo diventano:
                                                                             µ             ∂
                                                                                  RDR
                 øA = (RDR + RI )(CI + hA CDR + hB CDR ) +                            + RI (CI + CA )
                                                                                   hA
                                                                             µ             ∂
                                                                                  RDR
                 øB = (RDR + RI )(CI + hA CDR + hB CDR ) +                            + RI (CI + CB )
                                                                                   hB
   Imponendo che le due costanti di tempo siano uguali si ottiene:

                                      1    1 CI + CB   RI (CB ° CA )
                                        =    ·       +
                                     hA   hB CI + CA RDR (CI + CA )
                                                      |   {z   }         |   {z        }

   dove, in relazione all’espressione per la relazione fra hA ed hB proposta nel testo, l’elemento indicato
   dalla prima parentesi graﬀa rappresenta k2 mentre quello indicato dalla seconda parentesi graﬀa
   rappresenta k1 . I valori numerici sono

3) In base alla relazione fra hA ed hB individuata al punto precedente si può facilmente ricavare
   hA =hB /(k1 hB + k2 ). La costante di tempo øB può quindi essere espressa in funzione del solo hB
   come:                         µ                           ∂ µ             ∂
                                                   hB CDR          RDR
              øB = (RDR + RR ) CI + hB CDR +                  +         + RI (CI + CB )
                                                  k1 hB + k2        hB
   Questa espressione di øB diventa arbitrariamente grande sia per valori di hB molto piccoli che per
   valori molto grandi, è quindi naturale che esista un valore di hB che minimizza il ritardo. In eﬀetti
   il ritardo al 90% della escursione di segnale TB =2.3 øB vale circa 711ps, 621ps e 633ps per hB =2, 4
   e 6 e si può dimostrare infatti che il valore di hB che minimizza il ritardo è prossimo a 4.
                    Cognome e Nome
                       Matricola
                         Data                          18 Aprile 2007

                         Prova Scritta di Complementi di Elettronica II
                                             18 Aprile 2007
   Sia VDD =1.8V e si assumano i seguenti parametri tecnologici per i MOSFET:

                    Parametro       n-MOSFET       p-MOSFET       n-MOS a Svuotamento
                      VT O             0.4 [V]        -0.4 [V]           -1.0[V]
                        Ø0          400 [µA/V2 ]   250 [µA/V2 ]       250 [µA/V2 ]
                       Cox          13 [fF/µm2 ]   13 [fF/µm2 ]       13 [fF/µm2 ]
                      CGS0          0.7 [fF/µm]    0.7 [fF/µm]        0.7 [fF/µm]
                       Cj0           5 [fF/µm2 ]    5 [fF/µm2 ]        5 [fF/µm2 ]
                      LM IN           0.18[µm]       0.18[µm]           0.18[µm]

Se non diversamente specificato si assuma per tutti i transistori L=LM IN . Si riportino
negli spazi bianchi all’interno del testo l’espressione analitica e, quando richiesto, il valore
numerico dei risultati.
In figura si mostra un circuito in cui tutti i gate sono realizzati in tecnologia Fully CMOS e sono dimen-
sionati in modo da avere tempi di salita e discesa uguali. L’invertitore I1 ha dimensionamento minimo
e parte dell’esercizio richiede di valutare la necessità di inserire invertitori al posto dei punti indicati in
figura.

                    IN                                                      O1
                               I1
                                                             X                   C1=50fF
                            Cinv1

                                                                              O2

                                                                                   C2=70fF




  1) (8 Punti). In base ai parametri tecnologici riportati in tabella si calcolino il ritardo caratteristico
     della tecnologia tp0 , la capacità di ingresso Cinv1 di un invertitore a dimensionamento minimo ed il
     parasitic eﬀort pinv dell’invertitore. A tal scopo si assuma che la lunghezza delle estensioni di source
     e drain sia LSD =3LM IN e si trascuri la dipendenza dalla tensione delle capacità di giunzione.
      Si determini inoltre il logical e parasitic eﬀort dei gate (trascurando la non linearitá della capacitá
      delle giunzioni).
2) (10 Punti). Si determini la relazione fra la capacità di ingresso Cxnor e Cnor dei gate XNOR e NOR
   aﬃnchè siano uguali i ritardi dall’ingresso al nodo O1 e dall’ingresso al nodo O2. Si calcoli quindi
   il branching eﬀort bx al nodo X e relativo al percorso di segnale che porta ad O2.




3) (8 Punti). Si calcoli il numero di invertitori da aggiungere per minimizzare il ritardo del circuito. Si
   determini quindi il dimensionamento di tutti i gate del circuito (esprimendolo in termini di capacità
   di ingresso dei gate stessi), e si calcoli il valore numerico del ritardo ottimizzato.
         Soluzione della Prova Scritta di Complementi di Elettronica II
                                             18 Aprile 2007
1) Per l’Inverter ad area minima la capacitá di ingresso risulta Cinv1 = (1+")(Cox L2M IN +2LM IN CGS0 ) =
   1.75f F , dove "=Øn0 /Øp0 =1.6. Siccome per VT =0.4V e VDD =1.8V si ha F (VT /VDD )=2.09, il ritardo
   caratteristico della tecnologia vale
                                                 2Cinv1 F (VT /VDD )
                                         tp0 =                       = 10.1ps
                                                      Øn0 VDD

   Il parasitic eﬀort dell’invertitore vale invece:
                                                    2CGS0 + Cj0 LSD
                                          Pinv =                     ' 1.1
                                                   2CGS0 + Cox LM IN
   dove si é sfruttato LSD =3LM IN e si è posto Keq =1 (che corrisponde ad avere trascurato la non
   linearitá della capacitá delle giunzioni).
   I logical eﬀort sono:
                             1 + 4"                          2+"                        (2 + 2")
                   gnor =           = 2.85         gnand =       = 1.4        gxnor =            =2
                              1+"                            1+"                         (1 + ")
   inoltre i parasitic eﬀort sono pnand =pnor =2pinv =2.2 e pxnor =pnor =4pinv =4.4.
2) Aﬃnchè siano uguali i ritardi al nodo O1 ed O2 è necessario che siano uguali i ritardi dal nodo X
   ad O1 ed O2. Imponendo l’uguaglianza di tali ritardi otteniamo:
                                    µ                        ∂           µ                  ∂
                                           C1                                  C2
                              tp0   gxnor       + pxnor          = tp0   gnor      + pnor
                                          Cxnor                               Cnor
   Siccome pnor e pxnor sono uguali otteniamo la semplice relazione di proporzionalità fra Cxnor e Cnor :
                                                    Cxnor   gxnor C1
                                                          =
                                                    Cnor    gnor C2

   Questa relazione consente di ottenere un branching eﬀort indipendente dai dimensionamenti:
                                                   Cxnor     gxnor C1
                                        bx = 1 +         =1+          ' 1.5
                                                   Cnor      gnand C2

3) La relazione fra Cxnor e Cnor individuata al punto precedente assicura che i ritardi al nodo O1 ed
   O2 siano uguali. Nel seguito consideriamo quindi il percorso di segnale dall’ingresso IN al nodo
   O2. Il logical eﬀort vale G=gnand gnor =3.99, mentre l’electrical eﬀort risulta H=C2 /Cinv1 =40. Il
   path eﬀort complessivo è quindi F =GHbx =240. Noto il valore di pinv =1.1, lo stage eﬀort ottimo
   della tecnologia risulta Ω=2.82 + 0.711.06=3.6, quindi il numero ottimo di stadi per il circuito in
   esame
       p  risulta N̂ =ln F/ ln Ω=4.5. Scegliamo di usare cinque stadi e quindi lo stage eﬀort ottimo vale
   ˆ
   f = F =2.99. Inoltre sarà necessario aggiungere 2 invertitori.
       5


   Noto il valore di fˆ, si possono calcolare i dimensionamenti degli stadi:
            gnor C2                   gnand bx Cnor                   Cnand                   Cinv3
   Cnor =           = 66.7f F Cnand =               = 46.9f F Cinv3 =       = 15.7f F Cinv2 =       = 5.24f F
               fˆ                           fˆ                          fˆ                     fˆ
   dove Cinv3 e Cinv2 sono le capacità degli invertitori aggiunti. Inoltre il valore di Cxnor si ottiene dal
   legame fra Cxnor e Cnor discusso al punto (2):
                                           gxnor C1
                               Cxnor =              Cnor = (bx ° 1)Cnor = 33.3f F
                                           gnor C2

   Il ritardo complessivo vale quindi:

                           tp = tp0 (5 · fˆ + 3pinv + 2pinv + 4pinv ) ' 24.8 tp0 ' 250ps.
                   Cognome e Nome
                      Matricola
                        Data                         18 Luglio 2018



                             Prova Scritta di Elettronica Digitale
                                            18 Luglio 2018
Se non diversamente specificato si assuma per tutti i transistori L=LM IN .
Sia VDD =1.1V e si assumano i seguenti parametri tecnologici per i MOSFET:

                                Parametro     n-MOSFET         p-MOSFET
                                  VT O            0.3 [V]         -0.3 [V]
                                    β!        100 [µA/V2 ]      75 [µA/V2 ]
                                  LM IN         0.065[µm]        0.065[µm]
                                   Cox         11[fF/µm2 ]      11[fF/µm2 ]
                                  CGS0        0.45 [fF/µm]     0.45 [fF/µm]

Si consideri un’interconnessione avente altezza H=0.18µm e larghezza W=0.35µm. Lo spessore del
dielettrico vale Tox =0.092µm ed il dielettrico è semplicemente SiO2 con costante dielettrica assoluta
εox =3.45·10−13 F/cm. La resistività del materiale con cui è fabbricata la interconnessione vale ρ=
3·10−4 [Ω·cm].

  1) (10 Punti). Si calcolino la capacità per unità di lunghezza c e la resistenza per unità di lunghezza r
     della linea di interconnessione, nonché la capacità di ingresso Cdr1 e la resistenza equivalente Rdr1
     dell’invertitore a dimensionamento minimo e con ritardi di salita e discesa uguali. La resistenza
     Rdr1 deve essere determinata come l’inverso della conduttanza del transistore n-MOS per VDS =0V .
2) (6 Punti). Si consideri adesso un tratto di linea di lunghezza Len =180µm e si supponga di volerla
   approssimare con un numero N =6 di celle di tipo L a parametri concentrati.
   Si determinino i valori CL ed RL delle capacità e resistenze delle N celle a parametri concentrati. Si
   esprima quindi la costante di tempo dominante al nodo di uscita della rete a parametri concentrati
   usando le regole di Elmore e se ne calcoli il valore numerico.




3) (10 Punti). Allo scopo di migliorare il ritardo si introduce un buffer a dimensionamento h dopo
   ogni tratto di linea, e un identico buffer all’inizio del circuito.
   Si chiede di determinare il dimensionamento h dei ripetitori che minimizza il ritardo del circuito ed
   il valore numerico di tale ritardo.
                 Soluzione della Prova Scritta di Elettronica Digitale
                                          18 Luglio 2018
1) La capacità per unità di lunghezza della linea di interconnessione è data da una componente Cpp
   relativa al piatto inferiore della linea e da una componente di fringing Cf r per la quale si può usare
   il modello basato sul condensatore cilindrico. Nel complesso si ha:
                                   εox          2πεox
                              c=       W+                  ! 0.326f F/µm
                                   Tox    ln[(4Tox + H)/H]

   mentre la resistenza per unità di lunghezza vale r = ρ/(H · W )=47.6 Ohm/µm.
   La resistenza e la capacità del buffer a dimensionamento minimo sono:
                                    1
                Rdr1 =                         = 12500Ω       Cdr1 = (1 + ε) CM 1 = 0.245f F
                         1 · βn! (VDD − VT 0 )

   con CM 1 =0.105f F ed ε=1.33.

2) La resistenza e la capacità per un tratto di interconnessione lungo Len =180µm sono Rint !8571Ω e
   Cint =58.7f F e l’approssimazione con N celle ad L ha resistenza RL =Rint /N =1428.7Ω e capacità
   CL =Cint /N =9.78 fF. La costante di tempo dominante al nodo di uscita del circuito RC ottenuto
   tramite le celle ad L a parametri concentrati risulta

                                                       N (N + 1)
                                      τN = Rint Cint             ! 293ps
                                                          2N 2
   La stima del ritardo dell’interconnessione al 90% dell’escursione di segnale risulta t90% =2.3τN =675
   ps.

3) Nel circuito a resistenze e capacità (proveniente dalla rappresentazione a parametri concentrati della
   interconnessione) ogni buffer con dimensionamento h ha una resistenza equivalente Rdr1 /h con cui
   pilota una cella ad L. In parallelo alla CL della suddetta cella ad L c’è la capacità di ingresso hCdr1
   del buffer successivo per tutti gli stadi escluso l’ultimo, che invece pilota soltanto la CL . Il ritardo
   del circuito può quindi essere scritto come
                                  !         "             #                          $
                                                Rdr1                      Rdr1
                         tp = 2.3 (N − 1)            + RL (hCdr1 + CL ) +      CL
                                                 h                         h
   Il valore di h che minimizza il ritardo si ottiene annullando la derivata di tp rispetto ad h e vale
                                            %
                                                  N Rdr1 CL
                                       h=                      ! 20.5 .
                                                (N − 1)RL Cdr1

   Usando h=20.5 si ottiene un ritardo ottimo pari a circa 360ps.
                   Cognome e Nome
                      Matricola
                        Data                           19 Marzo 2007



                              Prova Scritta di Elettronica Digitale
                                             19 Marzo 2007
Si riportino negli spazi bianchi all’interno del testo l’espressione analitica e, quando richiesto,
il valore numerico dei risultati.
In figura è riportato un albero per la distribuzione di due fasi di clock complementari ¡ e ¡ costituito
da interconnessioni di tipo RC. Le interconnessioni hanno resistività per unità di lunghezza r=30Ω/µm
e capacità per unità di lunghezza c=0.45f F/µm. I buﬀer riportati in figura sono descrivibili con un
semplice modello lineare ed i buﬀer a dimensionamento minimo hanno resistenza equivalente Rdr =1.6kΩ
e capacità di ingresso Cdr =5f F .
    I dimensionamenti dei buﬀer nei due rami dell’albero sono indicati con h1 ed h2. Le lunghezze dei
tratti di interconnessione sono L1 =40µm ed L2 =18µm e le capacità di carico sono CA =25f F e CB =40f F ,
rispettivamente per la fase ¡ e ¡.

                                                                        φ
                                  h1
                                                                         CA
                                                        L1



                                                                                          φ
                                 h2                           h2
                                                                                          CB
                                                L2                       L2


  1) (12 punti). Si esprimano i ritardi T (¡) e T (¡) (al 90% della escursione di segnale) sui due rami del
     circuito in funzione dei dimensionamenti h1 ed h2 dei buﬀer e degli altri parametri del circuito. In
     particolare, anche allo scopo di facilitare l’analisi dei punti successivi, si chiede di esprimere T (¡) e
     T (¡) con le espressioni compatte:
                                               tc2                                  tc5
                               T (¡) = tc1 +       + tc3 h2         T (¡) = tc4 +
                                               h2                                   h1
     fornendo (a) le espressioni di tc1 , tc2 , tc3 , tc4 , tc5 in funzione dei parametri del circuito; (b) i cor-
     rispondenti valori numerici.
2) (8 punti). Si determini il valore di h2 che minimizza T (¡) e si calcoli il valore di tale ritardo minimo.
   Quindi si ricavi il valore di h1 che consente di ottenere T (¡)=T (¡).




3) (6 punti). Si assuma di esprimere la resistenza dei buﬀer come
                                                           2
                                            Rdr =
                                                    Øn0 (VDD ° VT )

   e che i valori nominali di tensione di alimentazione e soglia siano VDD =2.5V e VT =0.4V .
   Si supponga che, a causa di disturbi, la tensione di alimentazione dei driver del ramo che genera ¡
   si riduca a VDD1 =1.8V (rimanendo invece VDD =2.5V per il ramo che genera ¡). Si calcoli il valore
   di T (¡) che corrisponde a VDD1 =1.8V e quindi lo sfasamento che si genera fra ¡ e ¡.
                Soluzione della Prova Scritta di Elettronica Digitale
                                              19 Marzo 2007
1) Il ramo che genera ¡ consiste in un unico tratto di interconnessione con una capacità di carico CA .
   Il suo ritardo al 90% della escursione di segnale risulta quindi:
                                                       µ                                   ∂
                                                           Rdr                Rdr
                                 T (¡) = rcL21 + 2.3           cL1 + rL1 CA +     CA
                                                           h1                 h1

   che può essere scritto nella forma T (¡) = tc4 + tc5 /h1 identificando i coeﬃcienti:

               tc4 = rcL21 + 2.3 rL1 CA ' 90.6[ps]               tc5 = 2.3 Rdr (c L1 + CA ) ' 158[ps]

   Il ramo che genera ¡ è formato da due tratti di interconnessione. Il primo tratto ha una capacità
   di carico h2 Cdr , mentre il secondo ha una capacità di carico CB . Il ritardo al 90% della escursione
   di segnale, considerando semplicemente addittivi i ritardi dei due tratti di interconnessione, risulta
   quindi:
                         µ                                          ∂                  µ                 ∂
                             Rdr                    Rdr                      Rdr                Rdr
   T (¡) = rcL22 + 2.3           cL2 + rL2 h2 Cdr +     h2 Cdr + rcL22 + 2.3     cL2 + rL2 CB +     CB
                             h2                     h2                       h2                 h2

   che può essere scritto nella forma T (¡) = tc1 + tc2 /h2 + tc3 h2 identificando i coeﬃcienti:

         tc1 = 2rcL22 + 2.3(Rdr Cdr + r L2 CB ) ' 76.8[ps] tc2 = 2.3 Rdr (2c L2 + CB ) ' 207[ps]

                                             tc3 = 2.3rL2 Cdr ' 6.2[ps]

2) Il minimo del ritardo relativo a ¡ in funzione del dimensionamento h2 si ottiene imponendo:
                                                                               s
                                 @T (¡)    tc2                                     tc2
                                        = ° 2 + tc3 = 0         )       h2 =           =' 5.8
                                  @h2      h2                                      tc3

   da cui otteniamo:
                                                        tc2
                                        T (¡) = tc1 +       + tc3 h2 ' 148.5[ps]
                                                        h2
   Il valore di h1 che assicura T (¡)=T (¡) si ottiene imponendo:
                                                  tc5                              tc5
                                  T (¡) = tc4 +       = T (¡)    )      h1 =
                                                  h1                           T (¡) ° tc4

   L’espressione del dimensionamento h1 ci dice che la specifica T (¡)=T (¡) può essere soddisfatta solo
   se T (¡) è maggiore di tc4 =90.6. Nel caso in esame il vincolo per l’esistenza di h1 è soddisfatto e
   possiamo quindi calcolare h1 '2.7.

3) Vista l’espressione per Rdr suggerita nel testo, il valore di Rdr per VDD1 =1.8V risulta:

                                                                          VDD ° VT
                             Rdr (VDD1 = 2.5V ) = Rdr (VDD=2.5V ) ·                 = 2.4kΩ
                                                                          VDD1 ° VT
   quindi la riduzione della VDD ha provocato un aumento di Rdr che si traduce in un aumento dei
   ritardi sul ramo di ¡. Più precisamente, il valore di tc3 non cambia (perché non dipende da Rdr ),
   mentre tc1 e tc2 diventano tc1 '86.1[ps] e tc2 '310[ps]. Per i nuovi valori di tc1 e tc2 si ottiene:
                                                           tc2
                                         T (¡) = tc1 +         + tc3 h2 ' 176[ps]
                                                           h2

   quindi la fase ¡ risulta in ritardo rispetto a ¡ di circa 28[ps].
                 Cognome e Nome
                    Matricola
                      Data                           19 Settembre 2005



                       Prova Scritta di Complementi di Elettronica II
                                           19 Settembre 2005
Si assuma per tutti i transistori L=LM IN . Si riportino negli spazi bianchi all’interno del
testo l’espressione analitica ed il valore numerico dei risultati.
In figura si mostra un circuito in cui tutti i gate sono realizzati in tecnologia Fully CMOS e sono dimen-
sionati in modo da avere tempi di salita e discesa uguali.
Della tecnologia in questione é noto il ritardo di riferimento per la metodologia del Logical EÆort ø =
14ps, Øn0 =350µA/V 2 , Øp0 =200µA/V 2 , la capacitá dell’ossido di gate dei MOSFET Cox =14f F/µm2 e la
lunghezza e±cace minima LM IN =0.25µm. Inoltre la capacitá per unitá di area delle giunzioni di source
e drain vale Cj0 =9f F/µm2 , mentre la lunghezza delle regioni di diÆusione é LSD =2LM IN .
In figura sono indicati i dimensionamenti Sn degli n-MOSFET del gate NOR e NAND, mentre Sexor
indica il dimensionamento non noto del gate EXOR. Anche il valore numerico delle capacitá di carico CL
e CL1 é indicato in figura.

                                                                             Out
                                               X          Sexor
                  IN
                                                                                    CL=90fF
                 CIN             Sn=1



                                                                             CL1=20fF
                                                          Sn=3


  1) (8 Punti). Si calcoli il parasitic eÆort pinv dell’invertitore ed il logical eÆort e parasitic eÆort dei tre
     gate nel circuito.
2) (10 Punti). Si scriva l’espressione del ritardo (in unitá di ø ) dall’ingresso IN all’uscita Out in
   funzione della capacitá di ingresso incognita Cexor del gate EXOR. Si calcoli quindi il valore di Sexor
   che minimizza il ritardo.




3) (6 Punti). Si calcoli il valore numerico del ritardo ottenuto dalla ottimizzazione del punto prece-
   dente. Si determini quindi il branching eÆort bX al nodo X.
          Soluzione della Prova Scritta di Complementi di Elettronica II
                                            19 Settembre 2005
1) Il parasitic eﬀort dell’invertitore é il rapporto fra la capacitá parassita al nodo di uscita e la capacitá
   di ingresso al gate stesso:

              (Wn LSD + Wp LSD )Cj0      LSD LM IN (1 + ")Cj0   LSD LM IN Cj0   1.125f F
    pinv =                             =                      =               =          = 1.286
             (Wn LM IN + Wp LM IN )Cox    LM IN (1 + ")Cox
                                            2                      2
                                                                 LM IN Cox      0.875f F

   Inoltre, per il NOR a 2 ingressi si ha:
                                      1 + 2"
                             gnor2 =         = 1.636          pnor2 = 2pinv = 2.572
                                       1+"
   ottenuti per "=Øn0 /Øp0 =1.75.
   Per il NAND a 3 ingressi avremo:
                                            3+"
                               gnand3 =         = 1.727     pnand3 = 3pinv = 3.858
                                            1+"
   mentre per l’EXOR a 2 ingressi:
                                   2 + 2"                  2(2 + 2")
                         gexor =          =2     pexor =             pinv = 4pinv = 5.144
                                   1+"                       1+"

2) La metodologia del Logical Eﬀort non é immediatamente applicabile al circuito in esame perché il
   branching eﬀort al nodo X dipende dal dimensionamento incognito Sexor , tuttavia una minimiz-
   zazione diretta é possibile. Se indichiamo infatti con Cnor2 , Cexor e Cnand3 le capacitá di ingresso
   dei gate del circuito, l’electrical eﬀort del NOR e dell’EXOR valgono:
                                             Cexor + Cnand3                   CL
                                   hN OR =                         hexor =
                                                 Cnor2                       Cexor
   dove le capacitá di ingresso dei gate NOR e NAND sono:

                              Cnor2 = (1 + 2")COXM          Cnand3 = (3 + ")COXM

   Quindi il ritardo puó essere espresso in unitá di ø come:

                                     Cexor + (3 + ")COXM          CL
                       d = gnor2 ·                       + gexor       + Pnor2 + Pexor
                                        (1 + 2")COXM             Cexor

   e risulta minimo per il valore di Cexor che ne annulla la relativa derivata:
                                        q
                              Cexor =     (1 + 2")COXM CL (gexor /gnor2 ) = 20.8f F

   Nota la espressione della capacitá di ingresso del gate EXOR Cexor =(1 + ")Sexor COXM , otteniamo
   Sexor '8.64.

3) Il valore minimo del ritardo si ottiene sostituendo Cexor =20.8f F nella espressione del ritardo
   derivata al punto (2):
                  µ                                                                  ∂
                            20.8 + (3 + 1.75)0.875      CL
           td = ø 1.636 ·                          +2         + 2.572 + 5.144 = 26.64ø = 374ps
                                (1 + 3.5)0.875        20.8f F

   Il branching eﬀort al nodo X é dato

                                      Cexor + Cnand3     (3 + 1.75)0.875
                              bX =                   =1+                 = 1.2
                                           Cexor               20.8
          Prova Scritta di Circuiti e Sistemi Elettronici
                                   (DIGITALE)
                                  23 Febbraio 2022

    Si consideri una tecnologia CMOS i cui gate devono avere tempi di
salita e discesa simmetrici. Si vuole utilizzare la metodologia del logical e↵ort
per determinare il tempo di attraversamento di una serie di gate logici e trovare i
dimensionamenti ottimi che ne consentono la minimizzazione tenendo in consider-
azione la presenza di interconnessioni tra un gate e l’altro.




  1. Dato il circuito dove per il momento si assume G1 e G2 due generici gate
     logici, si richiede di scrivere l’espressione per il ritardo dal nodo IN al nodo A
     in funzione dei parametri tipici della metodologia del logical e↵ort. Per fare
     questo assuma che, i) l’interconnessione possa essere approssimata da una rete
     a parametri concentrati a pi-greco ad 1 cella e ii) si utilizzi il metodo di Elmore
     per calcolare il ritardo tIN A per un’escursione del segnale al 90%.
     Si consiglia di scrivere il ritardo nella forma tIN A = tp0 [g1 (h1 + hW 1 ) + p1 + pW 1 ]
     dove i coefficienti g1 , h1 e p1 , in accordo con la metodologia del logical e↵ort,
     sono definiti come g1 = Rt1 Ct1 /tp0 , h1 = Ct2 /Ct1 e p1 = Rt1 Cp1 /tp0 (con Cti la
     capacità di ingresso di un generico gate logico e Rti la resistenza di uscita del
     generico gate considerando già un’escursione del segnale al 90%) mentre hW 1
     e pW 1 sono termini introdotti dalla presenza dell’interconnessione.
2. Si scriva l’espressione della condizione che minimizza il ritardo dal nodo IN
   al nodo OUT assumendo che i parametri delle interconnessioni non possano
   essere modificati dalla procedura di minimizzazione. In particolare si riporti
   l’espressione per il dimensionamento del gate generico G2 in termini di capacità
   di ingresso del gate stesso.




3. Calcolare la capacità di ingresso del gate G2 che minimizza il ritardo come
   ricavato al punto 2). Si considerino ora i gate G1 e G2 come un gate NAND2
   e NOR3 rispettivamente. Sono noti i seguenti parametri: le interconnessioni
   hanno una resistenza per unità di lunghezza r= 28 ⌦/µm e capacità per unità
   di lunghezza c=0.45 fF/µm. La lunghezza della prima interconnessione è di
   40µm, mentre la seconda è di 80µm. Vengono inoltre forniti: i) il ritardo
   caratteristico della tecnologia tp0 = 20ps; e ii) la capacità di ingresso di un
   transistore a dimensionamento minimo (quindi con W = L = Lmin ) CM 1 =
   2.5f F . La conducibilità intrinseca dei transistori nMOS é pari a n0 =300
   µA/V2 mentre quella dei transistori pMOS vale p0 =150 µA/V2 . Il gate
   NAND2 ha un dimensionamento della rete di pull-up pari a Sp,N AN D =2 n0 / p0 .
2. Si scriva l’espressione della condizione che minimizza il ritardo dal nodo IN
   al nodo OUT assumendo che i parametri delle interconnessioni non possano
   essere modificati dalla procedura di minimizzazione. In particolare si riporti
   l’espressione per il dimensionamento del gate generico G2 in termini di capacità
   di ingresso del gate stesso.




3. Calcolare la capacità di ingresso del gate G2 che minimizza il ritardo come
   ricavato al punto 2). Si considerino ora i gate G1 e G2 come un gate NAND2
   e NOR3 rispettivamente. Sono noti i seguenti parametri: le interconnessioni
   hanno una resistenza per unità di lunghezza r= 28 ⌦/µm e capacità per unità
   di lunghezza c=0.45 fF/µm. La lunghezza della prima interconnessione è di
   40µm, mentre la seconda è di 80µm. Vengono inoltre forniti: i) il ritardo
   caratteristico della tecnologia tp0 = 20ps; e ii) la capacità di ingresso di un
   transistore a dimensionamento minimo (quindi con W = L = Lmin ) CM 1 =
   2.5f F . La conducibilità intrinseca dei transistori nMOS é pari a n0 =300
   µA/V2 mentre quella dei transistori pMOS vale p0 =150 µA/V2 . Il gate
   NAND2 ha un dimensionamento della rete di pull-up pari a Sp,N AN D =2 n0 / p0 .
         Soluzione della prova Scritta di Circuiti e Sistemi Elettronici
                                         (DIGITALE)
                                        23 Febbraio 2022


1. Il circuito equivalente utilizzando una cella a ⇧ per descrivere l’interconnessione, diventa:




   Secondo il modello di Elmore possiamo scrivere:
                                  ✓            ◆        ✓            ◆
                                           CW 1             CW 1
           tIN A,90% = 2.3⌧ = 2.3 Cp1 +            RG1 +         + Ct2 (RG1 + RW 1 )
                                              2              2
                                                    ✓            ◆
                                                       CW 1
                      = 2.3 RG1 (CW 1 + Ct2 ) + RW 1        + Ct2 + RG1 Cp1
                                                        2
   definendo Rti = 2.3RGi la resistenza da utilizzare nel modello del logical-e↵ort, e moltiplicando
   e dividendo per il tempo caratteristico della tecnologia tp0 otteniamo:
                          2         0              1                                       3
                           6R C BC             C            ✓          ◆
                           6 t1 t1 B W 1 Ct2 C         RW 1 C W 1         Rt1 Cp1 7
                                                                                  7
           tIN A,90% = tp0 6        B    +     C + 2.3            + Ct2 +         7
                           4 tp0 @ Ct1     Ct1 A        tp0     2           tp0 5
                             | {z }   | {z   }     |          {z       } | {z }
                                 g1        hW 1 +h1                   pW 1              p1

                      = tp0 [g1 (h1 + hW 1 ) + p1 + pW 1 ] .

   Si nota che, nel caso in cui CW 1 e RW 1 siano nulli, si ottiene il risultato noto tIN A,90% =
   tp0 (g1 h1 + p1 ).

2. Grazie al risultato di cui al punto precedente possiamo scrivere:

           tIN OU T,90% = tp0 {[g1 (h1 + hW 1 ) + p1 + pW 1 ] + [g2 (h2 + hW 2 ) + p2 + pW 2 ]}

   e sapendo che h2 = CL /Ct2 ed esplicitando in funzione di h1 otteniamo
                     ⇢                          ✓              ◆          ✓           ◆
                                         2.3RW 1 CW 1                         CL + CW 2
   tIN OU T,90% = tp0 g1 (h1 + hW 1 ) +                 + h1 Ct1 + p1 + g2                + pW 2 + p2
                                            tp0     2                           Ct1 h1
   Visto che Ct1 è noto essendo un parametro di progetto, l’unica dipendenza dai dimensionamenti
   si ha attraverso h1 , dunque minimizzare tIN OU T significa annullare il termine @t/@h1 .
                           @t            RW 1              CL + CW 2
                              = g1 + 2.3      Ct1       g2              =0
                          @h1             tp0                Ct1 h21
                                         RW 1                CL          CW 2
                              = g1 + 2.3      Ct1       g2      2    g2         =0
                                          tp0              Ct1 h1       Ct1 h21
                                                           | {z }       | {z }
                                                             h2 /h1   hW 2 /h1

                              si ottiene quindi
                              ✓                   ◆
                                          RW 1
                                 g1 + 2.3      Ct1 h1 = g2 (h2 + hW 2 ) .
                                           tp0
   Si nota che nel caso di assenza di interconnessioni la condizione di minimo tempo di attraver-
   samento si ottiene quando g1 h1 = g2 h2 . Utilizzando l’uguaglianza h1 =Ct2 /Ct1 e (h2 + hW 2 ) =
   CL +CW 2
      Ct2   si ottiene il dimensionamento del secondo gate espresso in termini di capacità di
   ingresso del gate stesso:
                                             s
                                               Ct1 g2 (CL + CW 2 )
                                     Ct2 =
                                                g1 + 2.3 Rtp0
                                                           W1
                                                              Ct1

3. La capacità di ingresso del primo gate logico vale Ct1 = (Sn,N AN D2 + Sp,N AN D2 ) CM 1 e, noto
   il dimensionamento dei transistori della rete di pull-up e visti i vincoli richiesti per avere tempi
   di salita e di discesa di caso peggiori uguali scriviamo Ct1 = (4 + 2") CM 1 = 20 fF. Il logical
   e↵ort dei due gate vale g1 = (2 + ")/(1 + ") = 4/3 e g2 = (1 + 3")/(1 + ") = 7/3. La resistenza
   della prima interconnessione vale RW 1 = 1.12 k⌦ mentre la capacità della seconda CW 2 = 36
   fF. Si ottiene quindi:
                                        s
                                           Ct1 g2 (CL + CW 2 )
                                  Ct2 =                        = 80f F
                                            g1 + 2.3 Rtp0
                                                       W1
                                                          Ct1
          Prova Scritta di Circuiti e Sistemi Elettronici
                                 (DIGITALE)
                                27 Gennaio 2021

    Se non diversamente specificato si assuma per tutti i transistori L =
LM IN . Si consideri una tecnologia CMOS i cui gate devono avere tempi di salita e
discesa simmetrici e per la quale sono note le conducibilitá intrinseche dei tran-
sistori n-MOS e p-MOS n0 =150µA/V 2 e p0 =75µA/V 2 , la capacitá di gate del
transistore a dimensionamento minimo CM 1 = 0.75f F e il parasitic e↵ort pinv =
1.2 dell’invertitore. La tensione di soglia per i transistori n-MOS e p-MOS vale
Vtn =|Vtp |=0.25V e la tensione di alimentazione é VDD = 1.0V .




  1. Determinare la funzione logica implementata dal gate in esame (fino al nodo
     O1) e calcolare logical e↵ort e parasitic e↵ort assumendo ritardi simmetrici
     di caso peggiore e assumendo che siano disponibili gli ingressi A,B,C e i loro
     negati.
2. L’uscita del gate logico viene connessa ad una linea di lunghezza L=50mm, re-
   alizzata in Alluminio (⇢=2.7⇥10 8 ⌦m) con sezione in prima approssimazione
   circolare di diametro D=7µm che giace sopra ad un piano di massa e separata
   da esso da ossido di Silicio ("r,SiO2 =3.9) alla distanza td =30µm. Calcolare
   la capacitá per unitá di lunghezza c, la resistenza per unitá di lunghezza r,
   l’induttanza per unitá di lunghezza l, l’impedenza caratteristica della linea Z0
   e il tempo di volo tf l . Motivare se la linea in esame puó considerarsi come
   fortemente dispersiva oppure a basse perdite.




3. Si calcoli il coefficiente di riflessione alla sorgente e quello al carico assumendo
   che la linea sia connessa ad una capacitá di valore molto minore rispetto a
   quello della linea stessa. Si assuma che il dimensionamento assoluto degli
   n-MOS del gate logico sia Sn = 2. Commentare la strategia migliore per il
   pilotaggio della linea (assumendo che non sia possibile partizionarla) al fine di
   minimizzare il ritardo dall’ingresso al nodo O2 e, in particolare, come rendere
   il settling time della linea pari ad un solo tempo di volo.
Soluzione della prova Scritta di Circuiti e Sistemi Elettronici
                                  (DIGITALE)
                                 27 Gennaio 2021


  1. La funzione logica implementata dal gate é

                 F = ĀB̄ + AB C + ĀB + AB̄ C̄ =
          Ā B̄ C̄ + BC + A B C̄ + B̄C = A ⌦ B ⌦ C

    un gate XOR a tre ingressi.
    Per il calcolo del logical e↵ort si nota come il percorso di caso peggiore per la
    rete di pull-up sia costituito da 3 p-MOS in serie e per la rete di pull-down
    da 3 n-MOS in serie. Assumendo la resistenza equivalente di caso peggiore
    del gate logico uguale a quella dell’inveritore di riferimento possiamo scrivere
    che RXOR = Rinv ! Sn,XOR /3=Sn,inv . Uguagliando invece i tempi di salita e di
    discesa di caso peggiore si deriva che Sp,XOR = n0 / p0 Sn,XOR ="Sn,XOR =2Sn,XOR
    Per il calcolo del logical e↵ort notiamo come l’ingresso A (e lo stesso vale per
    A negato) sia connesso a 2 p-MOS ed 1 n-MOS dunque:
                     Sn,XOR (1 + 2") CM 1
          gXOR,A =                           = 5.
                      [Sn,inv (1 + ") CM 1 ]

    L’ingresso B (e lo stesso vale per B negato) é connesso a 2 p-MOS e 2 n-MOS
    dunque:
                     Sn,XOR (2 + 2") CM 1
          gXOR,B =                           = 6.
                      [Sn,inv (1 + ") CM 1 ]

    L’ingresso C (e lo stesso vale per C negato) é connesso a 1 p-MOS e 2 n-MOS
    dunque:
                     Sn,XOR (2 + ") CM 1
          gXOR,C =                          = 4.
                     [Sn,inv (1 + ") CM 1 ]

    Per quanto riguarda il parasitic e↵ort sono presenti 2 p-MOS e 2 n-MOS sul
    nodo di uscita e dunque
                   2Sn,XOR + 2Sp,XOR
          pXOR =                      pinv = 6pinv = 7.2
                     [Sn,inv (1 + ")]
2. Si calcolano la capacitá, induttanza e resistenza per unitá di lunghezza notando
   che l’interconnessione é a sezione circolare (e non quadrata)

               2⇡"SiO2          fF       "r,SiO2         pH
         c=      4td +D
                        = 0.074    , l=       2
                                                 = 0.579    ,
              ln D              µm         cv0           µm
                                       ⇢Al              4 ⌦
                                r=          2 = 7 ⇥ 10
                                    ⇡ (D/2)              µm

   si calcola infine l’impedenza caratteristica della linea Z0 . A questo proposito,
   per semplicità, si considera il comportamento ad alte frequenze (! >> r/l) di
                                                                   p
   modo che Z0 non dipenda dalla pulsazione ! e vale Z0 = l/c = 88⌦. La
   linea in esame si puó considerare a basse perdite, infatti si può verificare che
   L < Z0 / (2r)=62.7mm.
                                        p
   Infine il tempo di volo vale tf l = L lc = 0.33ns

3. La resistenza equivalente del gate XOR che pilota l’interconnessione per la
   transizione di salita (o di discesa) puó essere calcolata come
                                      ⇣       ⌘
                                         VT
                   RXOR          2F     VDD
         Rdriver =         =      Sp,XOR 0
                                                  = 19.16k⌦
                     2.3      2.3           p VDD
                                    3

   dove si é utilizzata la relazione Sp,XOR = "Sn,XOR = 4 calcolata al punto 1.
   Il coefficiente di riflessione alla sorgente vale ⇢S = R driver Z0
                                                           Rdriver +Z0
                                                                       =0.99. Il coef-
   ficiente di riflessione al carico sapendo che la capacitá del carico é di molto
   inferiore rispetto a quello della linea risulta ⇢L ⇡ 1.
   Il pilotaggio risulta altamente inefficiente vista la resistenza di uscita del gate
   XOR molto piú grande rispetto all’impedenza caratteristica della linea. Es-
   sendo il coefficiente di riflessione della linea al carico pari a 1, al fine di avere
   il settling time pari ad un solo tempo di volo sará necessario aggiungere un
   driver (un invertitore) tale per cui Rdriver =Z0 . Successivamente si utilizzerá la
   metodologia del logical e↵ort per, eventualmente, aggiungere degli invertitori
   tra il gate XOR e il driver che pilota la linea per minimizzare il ritardo tra
   ingresso del gate XOR e ingresso del driver connesso all’interconnessione.
                 Cognome e Nome
                    Matricola
                      Data                          30 Novembre 2004



                      Prova Scritta di Complementi di Elettronica II
                                         30 Novembre 2004
   Sia VDD =2.0V e si assumano i seguenti parametri tecnologici per i MOSFET:

                   Parametro     n-MOSFET        p-MOSFET       n-MOS a Svuotamento
                     VT O           0.35 [V]       -0.35 [V]           -1.0[V]
                       Ø0        450 [µA/V2 ]    200 [µA/V2 ]       450 [µA/V2 ]
                      Cox         9 [fF/µm2 ]     9 [fF/µm2 ]        9 [fF/µm2 ]
                      Cj0         7 [fF/µm2 ]     7 [fF/µm2 ]        7 [fF/µm2 ]
                     LM IN         0.25[µm]        0.25[µm]           0.25[µm]

Se non diversamente specificato si assuma per tutti i transistori L=LM IN . Si riportino
negli spazi bianchi all’interno del testo l’espressione analitica e, quando richiesto, il valore
numerico dei risultati.
In figura si mostra un circuito in cui tutti i gate sono realizzati in tecnologia Fully CMOS e sono dimen-
sionati in modo da avere tempi di salita e discesa uguali.

                                                                       Out
                        IN                      X
                                                                             COUT
                                  CIN



  1) (8 Punti). In base ai parametri tecnologici riportati in tabella si calcolino la resistenza equivalente
     Rinv e la capacitá di ingresso Cinv per un invertitore a dimensionamento minimo. Si calcoli quindi
     il ritardo ø caratteristico della tecnologia ed il parasitic eÆort pinv dell’invertitore, a tal scopo si
     assuma che la lunghezza delle estensioni di source e drain sia LSD =2LM IN .
2) (6 Punti). Detto SN 3 il dimensionamento degli nMOSFET nel Pull-Down del NOR e supponendo
   che il dimensionamento nel Pull-Down dell’EXOR sia proporzionale ad SN 3 , ovvero SEXOR =
   Kex SN 3 , si determini Kex a±nché il branching eÆort al nodo X sia bx =2.




3) (6 Punti). Assumendo in quanto segue il valore di Kex individuato al punto precedente, si cal-
   coli il Path EÆort complessivo fra l’ingresso IN e l’uscita Out sapendo che COU T =59f F e che il
   dimensionamento nel Pull-Down del NAND in ingresso é SN AN D3 =2.




4) (6 Punti) Si ottimizzi il ritardo di segnale da IN ad Out determinandone il valore numerico. Si
   calcolino inoltre i dimensionamenti SN 3 ed SP 3 degli nMOSFET e pMOSFET del NOR.
         Soluzione della Prova Scritta di Complementi di Elettronica II
                                         30 Novembre 2004
1) Per l’Inverter ad area minima la capacitá di ingresso risulta Cinv = (1 + ")Cox L2M IN = 1.826 mentre
   la resistenza risulta Rinv = (2/Øn0 VDD )F (VT /VDD ) = 4.27k≠, in quanto si ha "=Øn0 /Øn0 = 2.25 e,
   per VDD =2 e VT 0 =0.35V , si trova F'1.92.
   Il ritardo della tecnologia é ø =Cinv Rinv = 7.8ps. Il Parasitic EÆort vale invece:

                                        Cj0 (LSD · LM IN )(1 + ")   2Cj0
                              Pinv =                              =      ' 1.56
                                            Cox LM IN (1 + ")
                                                 2                  Cox

   dove si é sfruttato LSD =2LM IN .

2) Siccome le capacitá di ingresso per il NOR a tre ingressi e per l’EXOR sono:

         Cnor3 = (1 + 3")SN 3 COXM            Cexor = (1 + ")SEXOR COXM = (1 + ")Kex SN 3 COXM

   dove COXM =Cox L2M IN , allora il branching eÆort al nodo X vale:

                                       Cexor + Cnor3   (1 + ")Kex + (1 + 3")
                               bx =                  =
                                           Cnor3              (1 + 3")

   Imponendo bx =2 otteniamo quindi Kex =(1 + 3")/(1 + ")=2.38.

3) Per determinare il Path EÆort F dobbiamo determinare il Logical e Parasitic EÆort dei gate sul
   percorso di segnale. Per il NOR ed il NAND si ha:
                                         1 + 3"                        3+"
                              gnor3 =           = 2.38      gnand3 =       = 1.62
                                          1+"                          1+"
   inoltre entrambi i gate hanno il medesimo Parasitic EÆort pnand3 =pnand3 =3pinv =4.68. Il Path
   Logical EÆort é quindi G=gnor3 gnand3 =3.86.
   Per calcolare il Path Electrical EÆort H é invece necessario sapere la capacitá di ingresso CIN al
   percorso di segnale che é la capacitá di ingresso del NAND. Siccome conosciamo il dimensionamento
   Pull-Down del NAND in ingresso del gate SN AN D3 =2, allora:

                              CN AN D3 = (1 + "/3)SN AN D3 COXM ' 1.97f F

   e quindi si ha H=COU T /CN AN D3 '30. Il Path Branching EÆort vale invece B=bX =2 e quindi
   F =GHB=231.6.

4) Siccome il percorso di segnale é composto
                                           p da due stadi e non si chiede di interporre stadi buÆer, lo
   stage eÆort ottimo é subito dato da fˆ= F =15.22 che si traduce in una capacitá di ingresso per il
   NOR pari a CN OR3 =gN OR3 COU T /fˆ=9.23fF.
   Il ritardo complessivo vale quindi:
                                        td = ø (2 · fˆ + 2 · 3pinv ) ' 310ps.

   Il dimensionamento SN 3 si ottiene da:

                                   Cnor3 = (1 + 3")SN 3 COXM = 9.23f F

   che fornisce SN 3 =2.12 ed SP 3 =3"SN 3 =14.3.
                   Cognome e Nome
                      Matricola
                        Data                          19 Giugno 2009

                       Prova Scritta di Complementi di Elettronica II
                                             19 Giugno 2009
Sia VDD =1.8V e si assumano i seguenti parametri tecnologici per i MOSFET:

                    Parametro     n-MOSFET        p-MOSFET         n-MOS a Svuotamento
                      VT O           0.4 [V]         -0.4 [V]             -1.0[V]
                        Ø0        210 [µA/V2 ]    140 [µA/V2 ]         140 [µA/V2 ]
                       Cox        14 [fF/µm2 ]    14 [fF/µm2 ]         14 [fF/µm2 ]
                      CGS0        0.55 [fF/µm]    0.55 [fF/µm]         0.55 [fF/µm]
                       Cj0         3 [fF/µm2 ]     3 [fF/µm2 ]          3 [fF/µm2 ]
                       Keq             0.68            0.68                 0.68
                      LM IN         0.18[µm]        0.18[µm]             0.18[µm]

Se non diversamente specificato si assuma per tutti i transistori L=LM IN . Si riportino
negli spazi bianchi all’interno del testo l’espressione analitica e, quando richiesto, il valore
numerico dei risultati.
In figura si mostra un circuito in cui tutti i gate sono realizzati in tecnologia Fully CMOS e sono dimen-
sionati in modo da avere tempi di salita e discesa uguali. L’invertitore I1 ha dimensionamento minimo
e parte dell’esercizio richiede di valutare la necessità di inserire invertitori al posto dei punti indicati in
figura.
                                                                          O1
                       IN
                                 I1
                                                             X                  C1=94fF
                              Cinv1

                                                                           O2

                                                                                C2=120fF



  1) (8 Punti). In base ai parametri tecnologici riportati in tabella si calcolino il ritardo caratteristico
     della tecnologia tp0 , la capacità di ingresso Cinv1 di un invertitore a dimensionamento minimo ed
     il parasitic eﬀort pinv dell’invertitore. A tal scopo si assuma che la lunghezza delle estensioni di
     source e drain sia LSD =2LM IN .
      Si determini inoltre il logical e parasitic eﬀort dei gate usati nel circuito.
2) (10 Punti). Si determini la relazione fra la capacità di ingresso CN OR e CN AN D dei gate NOR e
   NAND aﬃnchè siano uguali i ritardi dall’ingresso al nodo O1 e dall’ingresso al nodo O2. Si calcoli
   quindi il branching eﬀort bx al nodo X per il percorso di segnale che porta ad O2.




3) (8 Punti). Si calcoli il numero di invertitori da aggiungere per minimizzare il ritardo del circuito. Si
   determini quindi il dimensionamento di tutti i gate del circuito (esprimendolo in termini di capacità
   di ingresso dei gate stessi) e si calcoli il valore numerico del ritardo ottimizzato.
         Soluzione della Prova Scritta di Complementi di Elettronica II
                                             19 Giugno 2009
1) Per l’invertitore ad area minima la capacitá di ingresso risulta
            Cinv1 = (1 + ")CM 1 = 1.63f F                    CM 1 = Cox L2M IN + 2LM IN CGS0 = 0.65f F
   con "=1.5. Siccome per VT =0.4V e VDD =1.8V si ha F (VT /VDD )=2.09, il ritardo caratteristico
   della tecnologia vale
                                      2Cinv1 F (VT /VDD )
                                tp0 =                     = 18.0ps
                                           Øn0 VDD
   Il parasitic eﬀort dell’invertitore vale invece:
                                                   2CGS0 + Keq Cj0 LSD
                                         Pinv =                        ' 0.51
                                                    2CGS0 + Cox LM IN
   dove si é sfruttato LSD =2LM IN .
   I logical eﬀort sono:
                              1 + 3"                         3+"                          (2 + 2")
                    gnor =           = 2.2         gnand =       = 1.8          gexor =            =2
                               1+"                           1+"                           (1 + ")
   inoltre i parasitic eﬀort sono pnand =pnor =3pinv =1.52 e pexor =4pinv =2.03.
2) Aﬃnchè siano uguali i ritardi al nodo O1 ed O2 è necessario che siano uguali i ritardi dal nodo X
   ad O1 ed O2. Imponendo l’uguaglianza di tali ritardi otteniamo:
                                    µ                   ∂            µ                         ∂
                                          C1                                    C2
                              tp0   gnor      + pnor         = tp0       gexor       + pnand
                                         Cnor                                  Cnand
   Siccome pnor e pnand sono uguali otteniamo la semplice relazione di proporzionalità fra Cnor e Cnand :
                                                          gnor C1
                                               Cnor =             Cnand
                                                         gnand C2

   Questa relazione consente di ottenere un branching eﬀort indipendente dai dimensionamenti:
                                                   Cnor       gnor C1
                                        bx = 1 +         =1+          = 1.96
                                                   Cnand     gnand C2

3) La relazione fra Cnor e Cnand individuata al punto precedente assicura che i ritardi al nodo O1 ed
   O2 siano uguali. Nel seguito consideriamo quindi il percorso di segnale dall’ingresso IN al nodo
   O2. Il logical eﬀort vale G=gexor gnand =3.6, mentre l’electrical eﬀort risulta H=C2 /Cinv1 =73.7. Il
   path eﬀort complessivo è quindi F =GHbx =519.1. Noto il valore di pinv =0.51, lo stage eﬀort ottimo
   della tecnologia risulta Ω=2.82 + 0.71pinv =3.18, quindi il numero ottimo di stadi per il circuito in
   esame
       p risulta N̂ =ln F/ ln Ω=5.4. Scegliamo di usare sei stadi e quindi lo stage eﬀort ottimo vale
   fˆ= 6 F =2.83.
   Noto il valore di fˆ si possono calcolare dimensionamenti degli stadi:
                  gnand C2                             gexor bx Cnand                               Cexor
        Cnand =            = 76.2f F        Cexor =                   = 105f F            Cadd1 =         = 37.1f F
                     fˆ                                       fˆ                                     fˆ
                                         Cadd1                                Cadd2
                             Cadd2 =           = 13.1f F        Cadd3 =             = 4.61f F
                                          fˆ                                   fˆ
   dove Cadd1 , Cadd2 e Cadd3 sono le capacità degli invertitori aggiunti. Inoltre il valore di Cnor si
   ottiene dal legame fra Cnor e Cnand discusso al punto (2):
                                           Cnor = (bx ° 1)Cnand = 72.9f F

   Il ritardo complessivo vale quindi:
                           tp = tp0 (6 · fˆ + 4pinv + pexor + pnand3 ) ' 22.6 tp0 ' 407ps.
                           Prova Scritta di Circuiti e Sistemi Elettronici
                                                 (DIGITALE)
                                                 19 Luglio 2022

   Viene richiesto di progettare un circuito in grado di generare due uscite: A e A. In particolare definiamo
come da figura:
     ramo 1: il ramo che produce l’uscita A utilizzando N (con N pari) invertitori
     ramo 2: il ramo che produce l’uscita A utilizzando N-1 invertitori.


                                                                               A
                                                                                      ramo 1
                                             N stadi                     CL1
                  A

                                                                               A      ramo 2

                                            N-1 stadi                    CL2


   Questo circuito rappresenta necessariamente il carico per un determinato driver e quindi le specifiche di
progetto impongono che la capacità al nodo di ingresso del circuito sia fissata e sia quindi un dato di
progetto assieme alle capacità di carico sui nodi di uscita CL1 e CL2 .

  1. Utilizzando quanto appreso dalla metodologia del logical e↵ort e fissato il numero N di stadi si scriva
     l’espressione che consente di minimizzare il tempo di generazione delle uscite A e A.

  2. Si consideri il circuito di figura con N=2, il vincolo sulla capacità totale al nodo di ingresso A del
     circuito impone CIN =15 fF, mentre CL1 =300 fF e CL2 =210 fF e pinv =3. Utilizzando i risultati di cui al
     punto precedente, trovare i dimensionamenti di tutti gli invertitori del circuito che minimizzano il tempo
     di generazione dei segnali A e A.
     (SUGGERIMENTO: dati i vincoli di progetto, si otterrà un’equazione di terzo grado in cui
     solo una delle soluzioni risulta fisicamente sensata.)


   Si consideri il gate asimmetrico con dimensionamento dei transistori della rete di pull down diversi:
                                               VDD



                                 IN
                                            Sp    Sp
                                                                  OUT



                                                  Sn = 1
                                                      1 �             �������
                                             1
                                        Sn =
                                             �                RESET




  3. Assumendo che tutti i MOSFET abbiano L=LM IN e con il vincolo che trise,worst case = tf all,worst case , si
     riportino le espressioni relative al logical e↵ort per l’ingresso IN e per l’ingresso RESET.
               Soluzione della prova Scritta di Circuiti e Sistemi Elettronici
                                                (DIGITALE)
                                                19 Luglio 2022


1. Dalla metodologia del logical e↵ort sappiamo che, preso il singolo ramo e per un numero fissato di stadi N,
   il ritardo sarà minimo quando lo stage e↵ort di ogni singolo stadio è pari allo stage e↵ort ottimo fˆ:
                                 1/N
                         fˆ1 = F
                              1      ; con F1 = G1 B1 H1 = CL1 /CIN,1       per il ramo 1
                              1/(N 1)
                       fˆ2 = F2       ;   con F2 = G2 B2 H2 = CL2 /CIN,2          per il ramo 2

  dove CIN,1 (CIN,2 ) rappresenta la capacità di ingresso del primo invertitore del ramo 1 (ramo 2).
  I tempi adimensionali relativi ai rami 1 e 2 saranno dati da:
                                        tad,1 = N fˆ1 + N pinv
                                          tad,2 = (N     1)fˆ2 + (N      1)pinv

  A questo punto si nota che per diminuire tad,1 è necessario aumentare valore di capacità CIN,1 . Il vincolo
  di progetto però, assume che la capacità totale di ingresso sia fissata e pari a CIN =CIN,1 +CIN 2 . In questo
  modo ad un aumento di CIN,1 deve corrispondere ad una diminuzione di CIN,2 e quindi un aumento di tad,2
  e il viceversa. Il altre parole, possiamo scrivere

                         CIN = CIN,1 + CIN,2 = ↵CIN + (1             ↵)C    con 0  ↵  1.
                                               | {z } |              {z IN}
                                                      CIN,1      CIN,2

  Dunque:
                                                r
                                                     CL1
                   tad,1 = N fˆ1 + N pinv = N   N
                                                          + N pinv
                                                    CIN ↵
                                                                      s
                                                                             CL2
                   tad,2 = (N   1)fˆ2 + (N      1)pinv = (N    1) N 1               + (N     1)pinv
                                                                          CIN (1 ↵)

  Risulta evidente che tad,1 (tad,2 ) è una funzione monotona decrescente(crescente) all’aumentare di ↵ come
  rappresentato in figura:




  Il ritardo ottimo nella generazione dei segnali A e A si ottiene imponendo tad,1 =tad,2 :
                            r                              s
                               C L1                               CL2
                         NN          + N pinv = (N 1) N 1               + (N 1)pinv
                              CIN ↵                           CIN (1 ↵)

  Da questa equazione non lineare nella variabile ↵ è possibile ricavare (in modo numerico per un generico
  N) il valore di ↵ e quindi il valore dei path e↵ort e dunque i dimensionamenti di tutti gli invertitori del
  circuito.
  Una soluzione alternativa che non richiede di calcolare esplicitamente ↵ consiste nel notare (come fatto
  prima) che la minimizzazione del ritardo si ottiene quando i ritardi dei due rami sono i medesimi e scrivere:

                                 tad,1 = tad,2 = N fˆ1 + N pinv = (N             1)fˆ2 + (N     1)pinv

  dalla quale si ricava:
                                                                N fˆ1 + pinv
                                                          fˆ2 =              .
                                                                   N 1
  Utilizzando quanto noto dalla metodologia del logical e↵ort, lo stage e↵ort ottimo si scrive come:
                                      r
                                         CL1               CL1
                                fˆ1 = N
                                               ! CIN 1 =
                                        CIN 1               fˆ1N
                                        r
                                          CL2                           CL2
                                fˆ2 = N 1        ! CIN 2 = ⇣                 ⌘N 1
                                          CIN 2                  N fˆ1 +pinv
                                                                                  N 1

  Il vincolo CIN =CIN,1 +CIN 2 ci consente di scrivere dopo qualche passaggio matematico:
                         ⇣             ⌘N 1                ⇣             ⌘N 1
                     fˆ1N N fˆ1 + pinv                  H̃1 N fˆ1 + pinv            H̃2 fˆ1N (N     1)N 1 = 0

  dove H̃1 = CL1 /CIN e H̃2 = CL2 /CIN . La soluzione di questa equazione consente di calcolare lo stage
  e↵ort ottimo del primo ramo, dal quale è poi possibile ricavare i dimensionamenti di tutti gli invertitori del
  circuito.

2. Utilizzando l’ultima espressione trovata al punto precedente, scriviamo per N=2:
                                     ⇣            ⌘    ⇣           ⌘
                                 fˆ12 2fˆ1 + pinv   H1 2fˆ1 + pinv     H2 fˆ12 = 0.

  Sapendo che H̃1 = CL1 /CIN = 300/15 = 20 e H̃2 = CL2 /CIN = 210/15 = 14 e che pinv =3 scriviamo:

                          pinv       H̃2 ˆ2               H̃1
                   fˆ13 +               f1    H̃1 fˆ1         pinv = 0 ! fˆ13         5.5fˆ12     20fˆ1   30 = 0.
                                 2                         2

  Di questa equazione cubica siamo interessati alla radice reale positiva che in questo caso corrisponde a fˆ1 =
  8.3324. Si ricavano tad,1 = N fˆ1 + N pinv = 2 · 8.3324 + 2 · 3 = 22.66 e tad,2 = (N 1)fˆ2 + (N 1)pinv =
  (2fˆ1 + pinv ) + pinv = 19.66 + 3 = 22.66 i quali sono ovviamente i medesimi e dunque i dimensionamenti
  sono:

       ramo 1: CIN,1 = CL1 /fˆ12 = 4.32 fF e CIN,2 = CL1 /fˆ1 = 36 fF
       ramo 2: CIN,1 = CL2 /fˆ2 = CL2 /(2fˆ1 + pinv ) = 10.68 fF


                                                 CIN=4.3 fF CIN =36 fF
                                                                                                A
                                                                                        CL1 =300 fF
                   A
                             CIN =15 fF                                                         A
                                                          CIN =10.7 fF                  CL2 =210 fF
3. Utilizzando le approssimazioni viste a lezione, possiamo calcolare il dimensionamento equivalente della rete
   di pull-down come il parallelo dei dimensionamenti dei due transistori e quindi
                                                               ! 1
                                                       1   1
                                          Seq,P D =    1 + ↵         =1
                                                      1 ↵

  mentre, nel caso peggiore per la rete di pull-up si avrà Seq,P U = Sp . La condizione trise,worst case =
  tf all,worst case impone che Seq,P U = "Seq,P D e dunque Sp = " = n0 / p0 . Per il calcolo del logical e↵ort
  utilizziamo la definizione g=Ct /CIN V imponendo Rt =RIN V (cioè SIN V =Seq,P D =1). I logical e↵ort per gli
  ingressi IN e RESET si calcoleranno dunque come:
                                                                 1
                                       CIN     Sn,IN + Sp,IN    1 ↵ +"
                                 gIN =       =                =
                                       CIN V    SIN V (1 + ")    1+"
                                                                     1
                                      CRESET   Sn,RESET + Sp,RESET   ↵ +"
                             gRESET =        =                     =
                                       CIN V       SIN V (1 + ")     1+"

  nel caso simmetrico in cui ↵ = 1/2 si trova, come noto, gN AN D = (2 + ")/(1 + ").
                    Cognome e Nome
                        Matricola
                           Data                       28 Gennaio 2022



                                Prova Scritta di Elettronica Digitale
                                                                                     Vedi 19 marzo 2007
                                             28 Gennaio 2022
Si riportino negli spazi bianchi all'interno del testo l'espressione analitica e, quando richiesto,
il valore numerico dei risultati.
In figura è riportato un albero per la distribuzione di due fasi di clock complementari o e o costitito
da intercomessioni di tipo RC. Le interconessioni hanno resistività per unità di lunghezza r=35S2/u7m
e   capacità per unità di lunghezza c=0.42fF/um.        I    buffer riportati in figura sono descrivibili con un

semplice modello lineare ed i bufjer a dimensionamento minimo hanno resistenza equivalente Ra=2.6ks2
e capacità di ingresso
                       Cdr=2.6fF.
     I dimensionamenti dei buffer nei due rami dell'albero sono indicati con hl ed h2.        Le lunghezze dei
tratti di interconnessione sono Li=401u1m ed L=20ume le capacitàdi carico sono CA=17fF e CB=30fF,
rispettivamente per la fase o e o.


                                  h1o
                                                                          CA
                                                        L1




                                  h2                         h20-                        o
                                                                                         CB
                                                 L2                        L2



    1) (14 punti). Si esprimano i ritardi T(6) e T() (al 90% della escursione di segnale) sui due rami del
       circuito in funzione dei dimensionamenti hl ed h2 dei bufer utilizzando le espressioni per il ritardo
       di una linea RC pilotata da un driver.
       In particolare, anche allo scopo di facilitare l'analisi dei punti successivi, si chiede di determinare le
       espressioni simboliche ed i valori numerici dei cinque coefficienti tel, tc2, tes, te4, tes che consentono
      di esprimente T(6) e T(o) per mezzo delle espressioni compatte:


                                  T() =tel+hTc2
                                            ha
                                                +t3 h2                T() = te4t
                                                                                    h
2) (10 punti). Si determini il valore di ho che minimizza T(o) e si calcoli il valore di tale ritardo
   minimo. Quindi si calcoli il valore di
                                          hi che consente di ottenere T(¢)=T(o).




3) (6 punti). Si assuma di esprimere la resistenza dei buffer come

                                                        2
                                          Rdr
                                                 BL(VDD-Vro)
   e che i valori nominali di tensione di alimentazione e soglia siano VpD=1.1V e V=0.35V.
   Si supponga che, a causa delle fiuttuazioni statistiche dei parametri dei transitori nei processi di
   fabbricazione, le tensioni di soglia dei driver del ramo che genera d si modifichino in Vr=Vro+AVr
   rimanendo invece Vro per il ramo che genera o. Si calcoli lo sfasamento Ao fra d e o prodotto da
   un valore di AVr pari a 0.15V.
                    Soluzione della Prova Scritta di Elettronica Digitale
                                            28 Gennaio 2022
 lramo che genera o è formato da due tratti di interconnessione. Il primo tratto ha una capacita di
       Carico    Cars mentre il secondo ha una capacità di carico Cp. Pertanto il ritardo al 90% della escur-
    S1one di segnale, considerando semplicemente addittivi i ritardi dei due tratti di interconnessione,
       può essere scritto come:

    T(O)        rel+2.3           cL2 + rLa ha Car +h Car)+rcL2+2.3                 cL2 +rLaCB +CB
            =


                              2

    II ritardo può essere posto nella forma T(6) = tel + ta/h2 + tea ha identificando i coefficienti:


            te=2rcl + 2.3(Ra Car + r La Cp) 75.61ps] ta=2.3 Ra (2c Lg + Ca)                   2801po]

                                            tea-2.3rLaCar 4.19|ps)
    l ramo che genera ó consiste in un unico tratto di interconnessione con una capacità di carico Ca
    Il suo ritardo al 90% della escursione di
                                              segnale risulta quindi:

                                  T(o)=ret?+2.3(cL +rLiCa +Ca
   e    può essere posto nella forma T(6) =tes +tes/h1 identificando icoefficienti

                   tosrcl?+2.3rL1Ca 125|ps]                 tes2.3Rd-(cLi + Ca)202[ps]
2) Il minimo del ritardo relativo a o in funzione del dimensionamento ha si ottiene inmponendo:

                                  OT() httes =0 h--8.18
                                  ah2
   da cui otteniam0:
                                      T)=ta ++tahh2144(ps
   I valore di h1 che assicura T(6)=T(#) si ottiene imponendo:

                                  T(o) =teh +      T()            1           tcs
                                                                        T(-to4
  L'espressione del dimensionamento hi rivela che la specifica T(¢)=T() può essere soddisfata solo
  se T() è maggiore di tos. Nel caso in esame questo vincolo è soddisfatto e possiamo quindi calcolare
  h 10.7.
3) Vista l'espressione per Rar suggerita nel testo, il valore di Rar per VTn0=Vrot+AVre Vrpo=-Vro-AVr
   risulta:
                                                            VDD - Vr
                         Rdr(AVr) = Rár(AVr=0)' Von - Vr - AVr 3380N

  quindi la variazione della tensione di soglia provoca un aumento di Rdr che si traduce in un aumento
  dei ritardi sul ramo di o. Più precisamente, il valore di tes non cambia (perché non dipende da
  Ra-), mentre tel e tea diventano te80.3ps e tea364ps. Per i nuovi valori di tel e ta si ottiene:


                                        T) =tel ++tea ha              159ps
                                                       h2
  quindi la fase o risulta in ritardo rispetto a o di circa 15 ps.
