---
fonte: "Slide G-loop (DRIUSSI).pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Teoria dei circuiti reazionati
Differenze tra lo schema di reazione ideale e il circuito con retroazione:
 Ogni blocco dello schema a blocchi ha una direzione e un
    trasferimento che non dipende dai blocchi a cui è collegato, lo schema
    elettrico non è sempre direzionale e il trasferimento dipende dagli
    elementi a cui è connesso
 I segnali dello schema elettrico possono essere di tensione o di
    corrente
 Non c’è una equivalenza netta tra lo schema a blocchi e lo schema
    circuitale c’ è solo una similitudine, infatti il trasferimento complessivo
    non è ricavabile in modo immediato dal trasferimento degli schemi a
    blocchi.

                α                 VI(t)                α                  VO(t)

I(t)                   O(t)
                                      II(t)                           IO(t)
                                                        β
                β
Individuazione delle reazioni in
uno schema
Per l’analisi della reazione è fondamentale individuare
  il blocco α e β:
 Per l’individuazione della direzione dell’anello è
  necessario seguire la direzione dei componenti
  direzionali di cui è composto lo schema
                         D


                  G


                         S
   Reazione serie e parallelo
         La natura della reazione (corrente o tensione) dipende dall’accesso dell’ingresso e dell’uscita

                                                      +                   α
                                               Sin                                             Sout
                                                                          β
Inserimento con un segnale di tensione su un ramo della reazione:             Inserimento con un segnale di corrente su un nodo della reazione:
Inserimento serie dell’ingresso (reazione di tensione) (il nodo               Inserimento parallelo dell’ingresso (reazione di corrente) (il nodo
sommatore è realizzato dalla maglia “ramo” di tensione) (alta                 sommatore è realizzato dall’equazione del bilanciamento del nodo
impedenza in ingresso) (l’anello si interrompe se si inserisce un             corrente) (bassa impedenza in ingresso) (l’anello si interrompe se si
segnale di corrente)                                                          inserisce un segnale di corrente)

                                       α                                                                                α
                    Vin
                                       β                                                            Iin
                                                                                                                        β
Prelievo del segnale di uscita serie (uscita su un ramo), il segnale di        Prelievo del segnale di uscita parallelo (uscita su un nodo), il segnale
uscita è identificato dalla corrente (alta impedenza in uscita)                di uscita è identificato dalla tensione (bassa impedenza in uscita)



                                                     Iout                                                                                       Vout
                                  α                  Rout
                                                                                                               α
                                                                                                                                       Gout
                                  β                                                                             β
Esempi
       +                 +

         -               -




     Ingresso serie   Ingresso parallelo




       +                 +

         -               -             RL




     Uscita      RL    Uscita
     parallelo         serie
Trasferimento reale
Il trasferimento reale si può scomporre nei seguenti
    contributi di calcolo più immediato

          Gideale   Gdiretto
Greale =       −1
                  +
         1 − Gloop 1 − Gloop
   Greale: Guadagno reale del trasferimento reazionato
   Gloop:Guadagno d’anello del circuito retroazionato
   Gideale: Guadagno reale del trasferimento se il Gloop è infinito
   Gdiretto: Guadagno reale del trasferimento se il Gloop è nullo
Calcolo del guadagno d’anello
   Il guadagno d’anello è il meccanismo che permette di ottenere il guadagno
    ideale
   Il calcolo del guadagno d’anello si ottiene spezzando l’anello in un punto
    “comodo” e calcolando il trasferimento sul circuito ottenuto ai capi del punto di
    rottura nella direzione dell’anello
   Si sopprimono gli ingressi (si aprono i generatori di corrente e si cortocircuitano
    quelli di tensione)
   Il calcolo si può anche realizzare in simulazione
   Questo calcolo è semplice da fare perché lo schema è direzionale


                                  R               VAC=1        RC >> τ dello schema
                                        VC
     Vin                  Vin     C                VC             Vout




                           T(s)
Calcolo del guadagno d’anello
Il punto di rottura più comodo è l’ingresso o
   l’uscita di una generatore comandato ideale
   altrimenti è necessario ricostruire le
   impedenze modificate dalla rottura
                            Gloop Itest       Itest
             α                            α




              β                           β
Calcolo del guadagno ideale
   Il guadagno ideale è un trasferimento che si ottiene
    facendo tendere a zero la variabile di ingresso della
    del circuito con retroazione, ovvero l’ingresso del
    blocco α sia essa corrente che tensione
Calcolo del guadagno diretto
Questo calcolo si ottiene annullando il guadagno del blocco α e
  calcolando il trasferimento tra ingresso ed uscita:
 Questo calcolo può essere realizzato in simulazione
  inserendo il blocco senza generatore di tensione AC utilizzato
  per il calcolo del guadagno d’anello connesso in modo da non
  perturbare il trasferimento diretto del segnale. Il generatore
  AC necessario per la valutazione di questo trasferimento va
  inserito all’ingresso del circuito.
Singolarità del guadagno reale
 I poli del guadagno reale sono le soluzioni
  dell’equazione: 1 − Gloop = 0
 Tutti i poli del guadagno ideale sono degli zeri del
  guadagno d’anello (non vale il viceversa)
 Il guadagno d’anello e il guadagno diretto hanno gli
  stessi poli
Rappresentazione del
guadagno reale
 Rappresentazione del guadagno reale in
 frequenza:                          Greale ≅ Gideale
              − Gloop Gideale        Gloop >> 1
  Greale ≅
                1 − Gloop
                                    Greale ≅ −GidealeGloop
   − Gloop Gideale
                                     Gloop << 1
                     Gideale
                                Il modulo del guadagno reale si
     Greale                     traccia tracciando la minima curva tra
                                il guadagno ideale e il prodotto del
                                guadagno d’anello per il guadagno
                                ideale
Metodo delle costanti di tempo
ipotesi
Si applica ai condensatori della rete la cui
  dinamica è osservabile sull’uscita che sono
  indipendenti, interagenti :
 Indipendenti: le loro tensioni non formano
  una maglia e sono linearmente indipendenti
 Interagenti: due condensatori interagenti
  inducono una corrente sull’altro dipendente
  dal loro stato di carica (questa relazione deve
  essere reciproca)
Metodo delle costanti di tempo
tesi
Valgono le seguenti uguaglianze :


   ∑ τ = ∑ R′ C
        i         i   i

              1
   ∑ ωi = ∑ R′′C
             i   i

Dove τi (ωi =1/τi) sono le costanti di tempo della rete e R’ sono le
  resistenze calcolate ai morsetti di connessione delle capacità
  Ci con le altre capacità scollegate e R’’ sono le resistenze
  calcolate ai morsetti di connessione delle capacità Ci con le
  atre capacità cortocircuitate
Teorema di Miller
Il teorema stabilisce che un'impedenza Z(s) che sia
    collegata fra i due nodi V1 e V2 può essere
    eliminata sostituendola con due impedenze: Z'(s)
    collegata fra il primo nodo e il riferimento di massa,
    Z"(s) collegata fra il secondo e massa, dove
                                            Z(s)
                Z (s)
  Z ′( s ) =
              1 − K (s)
               K (s)Z (s)      V1          K(s)               V2
  Z ′′( s ) =
               1 − K (s)
              V2 ( s )
  K (s) =
              V1 ( s)          V1 Z’(s)     K(s)     Z’’(s)   V2
