---
fonte: "Riassunto_logiche_e_memorie_Dalzi.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Sequential Logic Circuits


Logica sequenziale
Sono logiche nelle quali le uscite non dipendono istantaneamente dagli ingressi (logiche combinatorie) ma
hanno degli “stati”




un circuto sequenziale è composto da degli ingressi che vengono elaborati mediante una logica combinatoria.
L’esito di questa elaborazione porta a delle uscite + lo stato nel quale dovrà trovarsi la logica al prossimo ciclo.



Definizione dei tempi




tsu → tempo minimo per il quale il dato deve rimanere stabile prima del fronte di clock in modo che venga
campionato correttamente

thold → tempo minimo per il quale il dato deve rimanere stabile dopo del fronte di clock in modo che venga
campionato correttamente

tc-q (t di clock to q)→ tempo di caso peggiore nel quale il dato viene copiato in uscita (tempo dopo il quale
l’uscita è stabile) (a     seguito del fronte di clock
Questi tempi impongono un vincolo sulla frequenza di clock che dovrà avere un periodo:

                 Tclock > tsu + tc-q + tprop-logica (tempo di propagazione della logica combinatoria)


inoltre è presente un tempo definito tcd (contamination delay) che definisce il tempo dopo cui l’uscita varia a
fronte della variazione di ingresso




Per far si che l’ingresso arrivi così com’è al registro (entrando dallo stesso) bisognerà avere che:
                                                 tcdreg + tcdlogic > thold
Se quel tempo fosse minore del tempo di hold, avrei delle perturbazioni sul nodo di ingresso prima che finisca
il tempo di hold e questo non va bene proprio per la definizione di tempo di hold.
Tipologie di registri
   ●   latch
           ○   è level sensitive
                   ■ positive
                          ● trasparente (fa passare il dato) → CLK = 1
                          ● hold (mantiene il dato in memoria) → CLK = 0
                   ■ negative
                          ● trasparente → CLK = 0
                          ● hold → CLK = 1
   ●   registro
           ○ è edge-triggered ovvero è trasparente al fronte di salita (positive edge) al fronte di discesa
               (negative edge)

I registri possono essere:
    ● statici → preservano lo stato finchè c’è alimentazione
    ● =  dinamici → dati immagazzinati per un brave periodo di tempo (storage nei condensatori e per il
         leakege vanno refreshati come ad esempio la DRAM)



Bistabile
é la serie retroazionata di un numero pari di inverter (ovvero l’uscita dell’ultimo è l’ingresso del primo).
                                        =




Abbiamo graficato la caratteristica del primo inverter, la caratteristica del secondo non è altro che quella del
primo ribaltata in quanto l’uscita di 1 è l’ingresso di 2 e vicerversa. Unendo le caratteristiche trovo 3 punti di
intersezione che rappresentano i punti di lavoro del circuito.
    ● A e B sono punti stabili → la caratteristica dell’inverter deve essere >1 in modo che abbia effetto la
        proprietà rigenerativa dei segnali digitali (ovvero che se un segnale analogico non è riconoscibile nè
        come 1 nè come 0, ponendo in cascata più inverter il segnale si sposta verso il relativo valore digitale)
    ● C è il punto metastabile
            ○ se si introduce del rumore in ingresso al primo inverter provocando uno spostamento del punto
                di lavoro nella caratteristica, si vede che il punto di lavoro si sposta verso uno dei due punti
                stabili A o B
Mux-Based Latch




  ●   l’inverter dopo D consente al canale di ingresso di essere direzionale (il pass-transistor che segue è
      per sua natura bidirezionale)
  ●   in questo circuito il clock-load (il carico attaccato al clock come numero di mosfet) è alto e quindi la
      distribuzione del clock può avere dei ritardi con possibili clock overlapping (sovrapposizioni del clock)




  ●   in questo caso il clock load è basso e c’è meno rischio di clock overlapping
  ●   ho solo nMOS (no pass-transistor complementare) e quindi ho il problema del trasferimento dell’ “1
      debole” Vdd-Vt (signal integrity) che porta al consumo statico degli invertitori che seguono(rivedi
      pass-transistor)
In questo circuito ho un bistabile che viene pilotato da un pass-transistor complementare. Quando sul latch è
immagazzinato per esempio uno zero e voglio imporre un uno in ingresso, dovrò fare in modo che il rapporto
di forza tra il pass-transistor e il transistor Mn2 sia più favorevole al pass-transistor (in quanto Mn2 tenderà a
tenere a massa il nodo di uscita).

Per evitare questa contesa si può progettare il circuito nel seguente modo, nel quale ho due pass-transistor:
   ● uno che gestisce la scrittura sul latch
   ● l’altro (che è in controfase con l’altro) che gestisce la lettura
Master-Slave (edge-triggered) Register




                              CLKT                                             Clk




                                     Clk                                                CTK




                                                                                  CLK
                                 CTK




  ●   i due multiplexer-based latch lavorano in controfase in modo che lo slave possa copiare l’ingresso
      campionato dal master
  ●   T1 è un pass-transistor di tipo transmission gate ovvero un pass transistor complementare nei
      quali ai gate dei due mosfet c’è un segnale di controllo a sua volta complementare
          ○ quando il segnale di controllo che arriva al gate dell’nMOS è il clock allora si parla di
              pass-transistor di tipo clock (se fosse arrivato il clock negato sarebbe stato di tipo clock
              negato)
  ●   la retroazione di I3 su I2 serve a mantenere stabile il bistabile
          ○ è necessario un tsetup in modo che D sia stabile mentre I2 sta valutando il suo ingresso
          ○ non c’è thold in quanto se CLK = 1, T1 è spento e il latch è in stato di hold
  ●   I4 porta l’ingresso allo slave e rende unidirezionale il circuito → T3 non può pilotare a monte
FUNZIONAMENTO:
CLK = 0
   ● T1 ON, T4 ON
   ● voglio che il dato arrivi fino all’uscita di I2 per essere immagazzinato nel bistabile
        ○ infatti quando avremo CLK = 1, T2 si accenderà ribadendo il dato a I3 (in quanto si vede che
             l’ingresso di I3 è logicamente uguale all’uscita di I2)
        ○ ci vuole tuttavia il tempo che il dato arrivi all’uscita di I2
                  ■ supponiamo che D commuti da 0 a 1 poco prima che CLK = 1, se il dato arriva in Qm
                     (che sarà uguale a uno) e in quel momento arriva il clock (perchè è molto ravvicinato al
                     cambio del dato) I2 non è ancora riuscito a valutare l’uno e quindi valuterà lo zero (dato
                     precedente) quando si accenderà T2 (ovvero Qm) al clk = 1




                   ■   questo porta a una contesa (chi vince?) in quanto
                           ● I2 valuta lo zero e impone un’uno in ingresso a I3
                           ● l’ingresso di I3 vale però zero (perchè il dato era uno)
                           ● la vincita della contesa dipende dalla variabilità dei transistor
                   ■   come azione cautelativa si impone che il dato rispetti il tempo di setup, ovvero che D
                       rimanga stabile per un certo tempo prima dell’evento di clock, fino alla valutazione di I2
                       così che al livello di clk alto I2 ribadisca semplicemente il dato
                   ■   in questo caso il dato è arrivato sia in I2 che in I4 quindi il tc-q è il tempo necessario per
                       attraversare T3 e I6

CLK = 1
   ● T2 ON, T3 ON
   ● il dato nel bistabile arriverà a T3 e poi all’uscita con I6
                                                  tempo di setup

                                                             ●   D commuta “gradualmente” da 0 a 1
                                                             ●   inv 1 porterà in uscita una transizione 1 - 0
                                                             ●   al pass-transistor però arriva un segnale di
                                                                 clock che anch’esso non varia
                                                                 istantaneamente
                                                             ●   se il tempo di setup è troppo vicino alla
                                                                 variazione del clock, il pass-transistor non ha
                                                                 abbastanza tempo per far passare tutto il
                                                                 segnale in uscita da inv1
                                                             ●   aumenta quindi il tc-q fino al fallimento




                                                 tempo di hold




La variazione del tempo di hold permette di contrastare il problema della sovrapposizione delle fasi, pertanto
se il dato rimane stabile dopo il campionamento per un certo tempo di hold, non ho il rischio che in caso di
clock overlapping questo dato possa commutare nel frattempo.
Reduced Clock Load Master-Slave Register
Nel circuito precedente il clock load era pesante (10 transistor attaccati al clock)




   ●   I2 (e I4) progettato per essere debole ad esempio con dimensionamento minimo (evita la contesa)
       serve per assicurarsi che sia un bistabile
   ●   è un registro positive edge-triggered statico
   ●   non c’è più unidirezionalità (perdita di robustezza) → i pass-transistor devono prevalere sugli invertitori
       retorazionati
   ●   problema della reverse conduction: lo slave può ripilotare il master




Clock overlapping
Quando il circuito legge due fasi che sono complementari può sorgere il problema che queste non commutino
nello stesso istante a causa dei tempi di propagazione




Quando ho delle sovrapposizioni:
   ● (1,1) → tutti nMOS accesi
   ● (0,0) → tutti pMOS accesi

Se ho una sovrapposizione nell’istante di campionamento del master e D commuta a valle della transizione
del clock, quando le fasi tornano a posto lo slave copia questo valore
Il circuito avendo solo pass-transistor nMOS è sensibile solamente a una sovrapposizione di fase ovvero
quella (1,1).
Quando ho una sovrapposizione (0,0) ho un funzionamento dinamico in cui i pass-transistor sono tutti spenti.

Per evitare la sovrapposizione di fase (1,1) posso pensare di usare due fasi distinte entrambe con duty cycle
del 25% nel seguente modo




in questo modo se avessi un ritardo di fase ho un 25% del periodo di margine (“cuscinetto”) prima di avere una
sovrapposizione (1,1).
Meccanismi di storage dinamici




La memorizzazione dinamica si basa sulla carica e scarica di capacità quindi è necessario un refresh continuo
in quanto si hanno delle correnti di leakage.
esempio di registro dinamico master-slave
C2MOS




   ●   CLK = 0
          ○ M3 e M4 ON → il master si comporta come un inverter ed è trasparente
   ●   CLK = 1
               ■ M7 e M8 ON → lo slave si comporta come un inverter ed è trasparente

Essendo la cascata di due inverter praticamente, il segnale si propaga solamente quando è attivo il PU di uno
e il PD dell’altro o viceversa. Questo fà si che sia molto più robusto alle sovrapposizioni dei clock




Ad esempio nel caso (0,0), se nell’istante di campionamento del master c’è una sovrapposizione 0,0 e il dato
commuta nell’istante di campionamento o poco dopo:
   ● il master può solamente catturare uno zero per accendere il PU
   ● il nodo x viene caricato a vdd (“1”)
    ●   quindi va nel PD dello slave che però è staccato da Q (M7 è spento con clk = 0) e quindi l’uscita non
        viene toccata
    ●   quando le fasi si mettono a posto (cioè clk = 0 e !clk = 1) lo slave è in hold quindi non copia x in uscita:
        non c’è corsa critica

Quindi in questo circuito non c’è corsa critica (campionamento del dato sbagliato) e con l’introduzione
di un tempo di hold e possibile anche evitare le sovrapposizioni di fase

l’unico caso critico è quello del fatto di avere delle transizioni dei clock lente. Infatti se per esempio il clock e il
clock negato sono a VDD/2 (nella transizione), tutti i p e n MOS sono parzialmente conduttivi. Per delle
transizioni ragionevoli non dovrebbero esserci problemi di corse critiche


TPSC: truly single-phased latches




            ●   Il circuito non è influenzato dal ritardo dei clock
            ●   sono due latch che sono trasparenti rispettivamente quando clk = 1 e clk = 0 in cui ho due
                invertitori in serie
   ●   unisco il campionamento con la funzione logica (nell’esempio è nand + not)
   ●   nell’esempio, se il clk= 0 il PD del master è spento, il PU porta il nodo x a VDD ma lo slave può
       valutare solo uno zero (anche il suo PD è spento) quindi tutto il registro è in hold
   ●   con clk = 1 ho la nand + la not



Precharged Register (TSPC: truly single-phased circuit)
Posso migliorare il numero di transistor




   ●   primo stadio I1 → invertitore quando clk = 0
   ●   terzo stadio I3 → invertitore quando clk = 1
   ●   secondo stadio I2 → logica dinamica
           ○ clk = 0 → precarica del nodo y con mosfet M6
           ○ clk = 1 → valutazione dell’ingresso accendendo M4

   ●   clk = 0
           ○ I1 trasparente → porta in X !D
           ○ I2 precarica → porta y a Vdd
           ○ I3 spento → y alta impedenza
   ●   clk = 1
           ○ I1 spento
           ○ I2 valutazione
           ○ I3 acceso → porta in Q y

Il circuto è positive edge-triggered, e per un corretto campionamento è necessario un tempo di setup del dato
(in modo che possa raggiungere il nodo x) che equivale di fatto al tempo di propagazione del primo invertitore.
Semiconductor Memories

classificazione delle memorie
   ●   Read-Write Memories
          ○ Random Access (SRAM,DRAM)
          ○ Non-random access (FIFO,LIFO, Shift Register, CAM)
   ●   Non-Volatile Read-Write memory (EPROM, E2PROM, FLASH)
   ●   Read-only memory (ROM) (Mask-Programmed, programmable PROM)



Memory timing: Definizione dei tempi




Read access → tempo dopo il quale, nel dato in uscita, trovo il dato letto (tempo per leggere il dato)
Read cycle → non si possono fare due letture consecutive troppo ravvicinate per la presenza di circuiti
periferici che usano il dato letto pertanto è più lungo del read access
Write access → tempo per scrivere il dato
write cycle → tempo più lungo del write access
Memory Architecture: Decoders




Solitamente il numero di parole immagazzinate N è molto più grande del numero di bit M usati per parola e se
associassi una sequenza di bit a una specifica parola avrei N sequenze diverse e quindi N segnali di
selezione

Si fa quindi uso dei decoder:
    ● N = 2k parole → k = log2N
    ● ho k segnali di selezione che sono molti di meno rispetto agli N di prima




   ●   word line: linee che selezionano le parole e sono le uscite del decodificatore
   ●   bit line: linee di input/output dei dati che uso per leggere o scrivere
   ●   storage cell (cella di memoria): stanno nell’incrocio tra bit line e word line
   ●   sense amplifier
   ●   row decode: decodificano gli indirizzi di riga (L-K bit). E’ di fatto un multiplexer perchè di fatto
       seleziona la riga
   ●   column decoder: decodificano gli indirizzi di colonna (K bit). Dopo che il decodificatore di riga ha
       selezionato la riga, con la bit line porto in uscita l’effettivo dato che andrà scritto/letto.

Un indirizzo è quindi rappresentato da L bit ( (L-K) + K ). Al giorno d’oggi le memorie sono dell’ordine dei Giga
quindi ogni indirizzo è rappresentato da almeno 30 bit.

il problema di questa organizzazione matriciale si pone quando il numero di parole è molto maggiore del
numero di bit di una singola parola. Infatti quando devo far scorrere le informazioni lungo le word line o lungo
le bit line uso delle interconnessioni on-chip le quali però all’aumentare della lunghezza fanno aumentare più
che linearmente il ritardo (indicativamente quadratico).
Di conseguenza dato che il ritardo è dato dal caso peggiore, conviene fare delle memorie che siano per così
dire “quadrate” ovvero che le interconnessioni orizzontali e verticali siano simili




Con l’aumentare delle dimensioni delle memorie la dimensione della matrice è diventata un problema
soprattutto per la lunghezza delle interconnesioni. Si fa quindi uso di più matrici interconnesse tra loro.
In questo caso gli indirizzi si spezzano ulteriormente, infatti ho
    ● un selettore del blocco
    ● un selettore della riga (per ogni blocco)
    ● un selettore della colonna (per ogni blocco)

vantaggi:
   ● posso limitare la dimensione delle singole matrici (interconnessioni più corte)
   ● i circuiti periferici analogici come i sense amplifier consumano molto in termini di energia: avendo più
      blocchi posso attivare solamente i circuiti periferici legati al singolo blocco mentre tutti gli altri sono
      spenti
Read-Write Memories (RAM) (Volatile)
  ●   SRAM (Static RAM)
        ○ è statica perchè non ha bisogno di refresh
        ○ i dati sono immagazzinati fintanto che c’è alimentazione (memoria volatile)
        ○ veloci
        ○ differenziali → la cella restituisce il dato in forma dritta e negata
        ○ grandi → sono composti da 6 transistor per cella
               ■ 2 inverter (bistabile)
               ■ 2 mos per leggere e scrivere
  ●   DRAM (Dynamic RAM)
        ○ è necessario un refresh dei dati (sono immagazzinati in capacità)
        ○ più lente delle SRAM
        ○ single ended → la cella restituisce un solo dato (o dritto o negato)
        ○ piccole → composte da 1-3 transistor per cella
               ■ condensatore
               ■ 1 transistor di accesso
        ○ il dato viene perso dopo essere stato letto



6-transistor CMOS SRAM Cell




  ●   WL (word line)
         ○ se bassa → la cella è in ritenzione (ferma)
         ○ se alta → accende M5 e M6 facendo passare le BL (bit line) che sono il dato da memorizzare
Lettura (read)




                                         6



                                                      v9
                                     s            s       s

                                                              G




                                                      S




                                             Vq
                                             "




                                 K




   ●   entrambe le BL sono precaricate a V DD
            ○ sono in alta impedenza ovvero vengono staccate dal driver che le pilota
            ○ le bit line hanno una capacità grande data dalle interconnessioni lunghe e dai nodi (mosfet) che
                sono collegati alla BL
   ●   supponiamo che nella cella sia immagazzinato un “1” (Q = 1)
            ○ vuol dire che in ingresso all’invertitore di destra c’è uno zero (è acceso solo M4)
            ○ !Q = 0
            ○ in ingresso all’invertitore di sinistra c’è un 1 quindi è acceso solo M1
   ●   in generale però dove l’uscita è “0” (sia per Q che per !Q), vorrei che si producesse un effetto sulla BL
       che è vicina a quell’uscita. Nel nostro esempio la BL di sinistra
   ●   In particolare vorremmo che la BL si scaricasse completamente a massa ma questo non sarà mai
       possibile in quanto:
            ○ i tempi sarebbero molto lunghi (alto read access time) in quanto la capacità della BL è molto
                grande (100 volte più grande di un transistor elementare)
            ○ se le scaricassi tutte, comunque ad ogni lettura dovrei ricaricarle fino a VDD quindi sarebbe
                un’operazione energivora e lunga
   ●   La BL quindi viene sbilanciata (ad esempio del 10% rispetto a V DD) e questo sbilanciamento porta
       all’intervento dei sense amplifier: amplificatori differenziali che leggono le due BL e consentono la
       lettura del dato
problema:
quando attivo la WL (la porto a V DD) il mosfet M5 ha:
   ● drain a VDD
   ● gate a VDD
   ● source a 0 (!Q = 0)

Di conseguenza il pass-transistor inietterà tutta la corrente sul source che vedrà il suo potenziale alzarsi
(sovratensione) e poi abbassarsi in quanto si scaricherà su M1.
Tuttavia !Q è l’ingresso dell’invertitore di destra quindi se la sovratensione è troppo ampia o troppo lunga si ha
il problema del read abset ovvero viene cambiato il contenuto della cella.

Questo problema si verifica quando la sovratensione accende il transistore n (M3) dell’invertitore di destra.Si
progetta quindi la cella affinchè questa sovratensione sia sufficientemente contenuta e in particolare minore
della tensione di soglia del n mos
    1. inserisco una capacità che posso dimensionare nel nodo !Q
    2. attendo che il nodo !Q, a rapporto tra M5 e M1 , arrivi ad una tensione intermedia tra VDD e massa
            a. M5 è saturo: se Vq < Vt → Vdd > Vdd - Vt
            b. M1 è triodo: se Vq < Vt → Vq < Vdd - Vt
            c. deltaV: potenziale di Q
            d. K è il beta
            e. CR (cell ratio): rapporto di forza tra M1 e M5




Più il rapporto di forza è grande (ovvero M1 è più forte) minore sarà la sovratensione del nodo
Write




   ●    ora le BL portano il dato che bisogna scrivere nella cella (nell’esempio BL = 0 mentre Q = 1)
   ●    le possibilità sono due:
            ○ o scrivo nella cella lo stesso dato
            ○ o scrivo il dato opposto
   ●    nel caso di scrittura del dato opposto, la tensione di uscita è sempre opposta alla tensione della BL da
        tutte e due le parti
   ●    nella lettura abbiamo detto che sul lato sinistro non posso scrivere su !Q in quanto la BL varierebbe di
                                                         )
        poco ( la scarica sorelle energivore
                                                   ecc




   ●    quindi devo scrivere sul lato destro: lo si può fare solamente se il pass-transistor M6 prevale su M4 in
        modo che Q si possa scaricare (write ability)
            ○ non si scarica del tutto ma bisogna far sì che sia minore della soglia elettrica dei transistori del
                PD in modo che essi si spengano (mentre i p mos del PU si accendono così che in !Q venga
                scritto un 1)

quindi:
    ● M6 trido : noi vogliamo che Vq < Vt quindi Vd < Vg - Vt → Vq < Vdd - Vt → circa 0 < Vdd -0 → triodo
    ● M4 saturo: Vdd - Vq > Vdd - Vt → se Vq < Vt è rispettata
    ● PR (pull-up ratio): rapporto di forza tra M6 e M4



                                                                        e    =
                                                                                 ¥
                                                                                                     Va -0
                                                                  più    è       piccolo   ,
                                                                                               più
                                                               Cancro   56 » 54)
Resistance-load SRAM Cell




  ●   il PD diventa importante in lettura in quanto deve essere particolarmente forte
  ●   Il PU deve essere debole per la scrittura (il pass-transistor deve essere più forte, vedi sopra)
          ○ non è necessario che sia fatto di transistor, in questo caso il PU è costituito da delle resistenze
              (polisilicio poco drogata)
          ○ consumo di area

  ●   questo circuito non ha transistori p
  ●   BL precaricate a V DD
  ●   quando gli nmos sono spenti la corrente delle R deve essere sufficientemente più grande della
      corrente di off dei mosfet per portare il nodo a VDD. Basta una piccola corrente quindi possono essere
      anche resistenze elevate
Leakage nelle SRAM
Con lo scaling della tecnologia si sono abbassate le tensioni di alimentazione e anche le tensioni di soglia dei
transistori. Questo ha portato ad avere dei transistor che si spengono “più lentamente” e quindi ad avere delle
correnti di leakage (o correnti di off) non proprio trascurabili portando ad uno stand-by power




   ●   mettendo i transistori in serie al PU e PD comandati da un segnale di sleep che mi dice quando il
       circuito deve funzionare o è appunto in sleep mode
3-transistor DRAM Cell




   ●    CS capacità di gate
   ●    M1, M3 → mos di accesso rispettivamente di scrittura e lettura
   ●    WWL : write word line
   ●    RWL: read wordl line

write
    ●   WWL a Vdd, RWL a 0 (mutuamente esclusive)
    ●   X = 0, voglio scrivere un 1 con BL1 = 1
    ●   carico la capacità Cs fino a Vdd-Vt (pass-transistor con n mosfet)
            ○ potrei survoltare con dei condensatori (oltre Vdd) le BL (che sono delle capacità) per avere
                appunto una carica fino a Vdd

read
   ●    RWL a Vdd, WWL a 0
   ●    X = 1, voglio leggerlo
   ●    la BL2 inizialmente precaricata a Vdd o Vdd-Vt si scarica se su X c’è un 1 (che accende M2 che è
        collegato a massa)
            ○ se X era 0 allora non si scaricava
   ●    la lettura non è distruttiva
1-Transistor DRAM Cell



                                      ✗
                                     •




   ●    precarico la BL a Vdd/2

write
    ●   WL a Vdd
    ●   BL a Vdd
    ●   Carico Cs

read
   ●    avviene per ripartizione di carica
           ○ distruttiva
           ○ meno robusta
           ○ cella molto piccola (vantaggio)
   ●    BL precaricata a Vdd/2
   ●    M1 ha come source e drain due condensatori a tensioni diverse quindi si innesca un transitorio che si
        può esaurire se
           ○ M1 si spegne (non è possibile in quanto il gate è a Vdd e il drain è a Vdd/2 e il source non
               riuscirà mai a raggiungere Vdd -Vt per spegnere il transistore)
           ○ la Vds si annulla e quindi annulla la corrente (le due capacità hanno la stessa tensione)
                   ■ se X era caricata a Vdd la ripartizione porterà sulla BL una tensione più vicina a Vdd e
                       viceversa se X era a 0 la ripartizione porterà sulla BL una tensione più vicina a massa
                       leggendo così la x
                   ■ va letta la differenza tra il valore precaricato della BL e il valore della BL
   ●   Vpre : tensione della BL precaricata
   ●   Vbit : tensione della capacità Cs
   ●   Vbl: tensione della BL a transitorio esaurito che sarà uguale a quella sulla capacità Cs
                   𝐶𝑠        𝐶𝑠/𝐶𝑏𝑙    𝐶𝑠
   ●   il termine 𝐶𝑏𝑙 +𝐶𝑠 = 1+𝐶𝑠/𝐶𝑏𝑙 ≃ 𝐶𝑏𝑙
           ○   essendo Cbl grande è un rapporto piccolo

Quindi:
   ● 1T DRAM richiede di avere un sense amplifier per ogni bit line che legga la differenza di tensione che
        si è innescata in lettura
   ● sono celle single ended (una sola uscita)
   ● la capacità Cs è inclusa esplicitamente (nel 3T DRAM era la capacita del gate di M2)
   ● la lettura è distruttiva: dopo ogni lettura è necessario un refresh
            ○ viene fatto dal sense amplifier che ripilota la BL così come l’ha letta per poterla refreshare
Sense Amplifier




   ●   C → capacità della bit line
   ●   deltaV → differenza di potenziale da leggere
   ●   Iav → corrente media che serve per spostare la carica C*deltaV
   ●   Tp → ritardo

I sense amplifier sono circuiti analogici periferici che interpretano il dato che arriva dalla memoria. Essi non
ottengono degli zeri o uni come i registri ma ottengono delle frazioni di Vdd.
Si usano i sense amplifier in quanto è preferibile che le escursioni delle BL siano il più piccole possibile. se
così non fosse
    ● i tempi sarebbero lunghi
    ● si richiederebbe parecchia energia per caricare le capacità delle BL
Oggigiorno si possono leggere un centinaio di mV con i sense amplifier (le tensioni di Vdd sono dell’ordine di
1V)
Differential Sense Amplifier                ( SRAM )



                                                       S
                             S
                                        G    o             |
                             io
                                                           52

                    s                                          s

                                  bis            bis
                   rt                                          I




   ●   Il segnale di sensing SE serve per evitare che il circuito abbia un consumo statico di potenza ( i circuiti
       analogici soffrono di questo problema)
            ○ viene attivato dopo che è stato generato quel deltaV da leggere
   ●   bit → bit line (precaricate a Vdd nel caso delle SRAM)
   ●   Se nel circuito bit e !bit sono uguali e i mosfet sono tutti uguali allora c’è un bilanciamento nel senso
       che y è uguale al drain del mosfet con bit (sx)
   ●   quando c’è uno sbilanciamento, comincia a scorrere più corrente su uno dei due mosfet e quindi il
       nodo y si alza o si abbassa




   ●   !PC → transistore di precarica
          ○ quando è basso accende i transistori di precarica delle due BL + il transistore di
             equalizzazione EQ
          ○ il transistore EQ serve a bilanciare le due BL (tende a portare la sua Vds = 0)
   ●   Dopo la precarica disattivo !PC e attivo la WL per la lettura
          ○ la cella che ha uno zero tende ad abbassare la BL dalla sua parte
   ●   quando la BL si sbilancia abbastanza (si è generato un deltaV), attivo il sense amplifier



Single to differential conversion (DRAM)
Nella DRAM viene prodotto uno sbilanciamento sulla BL e lo voglio confrontare con Vdd/2 che era il valore di
precarica della BL (così so che dato è stato letto)
    1. una possibilità è prendere un generatore di riferimento che però è critica: quel riferimento dovrebbe
       seguire le vicende delle celle in termini di
           a. variazioni istante per istante di Vdd
           b. variazioni di temperatura
           c. problema dell’aging (i transistori invecchiano e possono cambiare le letture dopo moltissime
               letture)




                                           ywl
                               BL

                                b




                                Dar
                                    core
Latch-based sense amplifier (DRAM)




                                                          ⑤

                                     zosz Kaine
                                   ①              )
                                                              §   uso   (   a   resina )



                                                      9




Nella DRAM la lettura è distruttiva: devo cercare un metodo per poter riscrivere il valore letto
Viene preso un bistabile e portato (con EQ) nel punto metastabile (idealmente Vdd/2 se gli invertitori sono
perfettamente simmetrici) che ha tanto guadagno e li non sta mai (è un punto instabile).
Quando SE = 0 e !SE = 1 posso forzare il circuito nello stato Vdd/2 in tutte e due le uscite (valore a cui
precarico le BL).
Prima di attivarlo (ovvero SE=1 e !SE = 0) lascio il tempo alle BL di sbilanciarsi un pò in modo che poi il
bistabile vada a finire in uno dei punti stabili.
    ● Le BL dettano in primo luogo lo sbilanciamento al sense amplifier (ingresso)
    ● successivamente il sense amplifier ripilota le BL portandole ai valori stabili
    ● se la WL è rimasta attiva riscrivo il dato nella cella con le BL
            ○ quindi il refresh del dato avviene semplicemente leggendo
  Row Decoders




             bit
M : n° di




                                                                                       {
                                                                                               "
                                                                                                       n°   di    usate
                                                                                           2       :




                                                                          gelato
                                                                                                       quindi    di


                                                                              determina        si
  Il numero di transistor (transistor count) è Nt = 2M * (2 * M) = M*2M+1                zr        :

                                                                                                   gote
                                                                                               per
       ● ho 2M gate (uscite) e ogni gate CMOS è costituito da 2*M transistor
  Sappiamo tuttavia che i gate CMOS cominciano a diventare lenti e inefficienti (nonchè ad occupare parecchia
  area) per fan in > 4


  Decoder gerarchici




     ●   M=8
     ●   logica a due stadi


     ●
     ●   Nt = 2M * 8 + 2M * 4
             ○ le nand sono 2M che sono le uscite totali e ogni NAND a quattro ingressi ha 8 transistor
             ○ le NOR sono 16 e ogni NOR a due ingressi ha 4 transistor
             ○ sono circa la metà del modello precedente
     ●   in questo modo le WL sono più leggere e aumentano quindi le prestazioni
Decoder dinamici




  ●   elimina la ridondanza tra PU e PD dei gate
  ●   consente un transistor count migliore
  ●   NOR
          ○ Si precaricano le WL
          ○ Ho N connessioni di transistor collegati a massa in parallelo(N è il numero di bit)
          ○ è attivata solamente una WL per volta; in questo esempio solamente se A 0 e A 1 sono uguali a
             zero, la WL0 resta precaricata a Vdd e tutte le altre si scaricano essendo i mos in parallelo
          ○ dal punto di vista energetico è poco efficiente perchè precarico tutte le WL e le scarico tutte
                                                     nor
             tranne una                                                     nord



                                                     :| :
                                                  00




                                                                        :|
                                                                                     1
  ●   NAND                                                 0

                                                  :
                                                                         °    .  .
                                                 .
          ○ precarica tutte le WL                                       1
                                                     .
                                                                             o   1
                                                         o
                                                                                 .

          ○ i transistor ora sono in serie
          ○ mantiene a Vdd tutte le WL eccetto quella con entrambi gli ingressi a uno che viene scaricata a
             massa
          ○ più efficiente
          ○ all’aumentare del numero di bit metto transistor in serie quindi dal punto di vista delle
             prestazioni dinamiche è peggiore
Column decoder

4-input pass-transistor based column decoder




  ●    Di fatto la selezione delle colonne è una operazione di multiplexing
  ●   in questo caso il decodificatore di colonna ha un numero di transistori pari alle BL
  ●   se L è il numero di bit ho i transistori del decoder di riga + 2 L transistor
  ●   il tempo per la decodifica di riga, lo sbilanciamento delle BL e l’arrivo ai sense amplifier, può essere
      sfruttato dal decodificatore di colonna (non introduce quindi ritardo al memory access time)




  ●   partendo dal basso (vicino a D) sul nodo di uscita si hanno 2 transistori, su quello più a monte (sopra
      !A1) se ne hanno 4,ecc. (struttura ad albero)
              ○ se ci fossero stati altri bit i transistor duplicavano ad ogni livello
    ●   Nt = 2 + 4 + … 2L = 2*(2L - 1)
              ○ vantaggio nel numero di transistori
    ●   il ritardo tende in modo quadratico



Charge Pump




    ●     Per far fronte al problema del trasferimento di tensioni che sono minori di Vdd si fa uso di questi circuiti
          di pump che fanno uso di un condensatore di pump
     ● M1 e M2 hanno connessione a diodo
     ● quando clk = 1
              ○ il nodo A è basso
              ○ pensando che Cload sia inizialmente scarico
                      ■ il nodo B si carica a Vdd -Vt (pass-transistor con solo nMos)
                      ■ Vload si carica fino a (Vdd-Vt) - Vt = Vdd - 2Vt VLOAD
                                                                             =




                      ■ sul condensatore alla fine c’è Cpump (Vdd - Vt) → B è Vdd - Vt e A = 0
     ● quando clk = 0                                     Upunp  =VB Va Us ( VA è
                                                                     -
                                                                         =
                                                                                     a  mora)


              ○ A va aaaaa
                       basso
                      ■ in prima istanza il condensatore Cpump non cambia la sua carica quindi A va a V DD e B
                                                               V8
                          va a VDD + (VDD - VT) = 2VDD -VT   =




                      ■ M1 è spento in quanto il suo source ora è sopra Vdd quindi è in inversa (connessione a
                          diodo)       ULOAD=  V52 >   V8=  VB

                      ■ M2 è acceso (diodo in diretta) → carica il condensatore fin chè può (perchè è un
                          condensatore anche Cpump quindi c’è una sorta di ripartizione di carica)
                              ● il transitorio dura fintanto che B non raggiunge nuovamente VDD - VT
Il ciclo ripartirà facendo salire di carica e quindi di tensione CLOAD un pò alla volta fintanto che la tensione Vload
non sarà (2VDD-VT) -VT = 2(VDD-VT) ovvero la tensione per cui il diodo non sarà più acceso perchè in inversa
(Vb arriva
=
massimo a 2VDD-VT.

Si genera una tensione alta, ma la capacità di erogare corrente è limitata da Cpump e dalla frequenza di clock
●   sulle ascisse ci sono numero di bit per chip
●   sulle ordinate ci sono scale logaritmiche
●   Cs è la capacità di immagazzinamento
●   Cd capacità della bitline
●   Vsmax è lla tensione equivalente letta dal sense amplifier

●   Si vede che Qs si è ridotta più di Cs in quando si è ridotta Vdd. Vdd si è ridotta grazie allo scaling
    arrivando ai giorni nostri a circa 1V.
●   la tensione di sbilanciamento della BL è data da Qs/(Cs + Cd)




●   l’asse della capacità è logaritmico quindi la capacità delle memorie è cresciuta esponenzialmente
●   le flash si sono sviluppate in 3D pertanto il numero di bit per area è aumentato (conta la planarità)
Memorie non volatili (ROM: Read-Only Memory)
L’informazione rimane disponibile anche quando non viene data alimentazione al sistema. All’inizio venivano
create già col contenuto che potevano solamente essere letto.




ROM DIODO:
  ● diodo connesso tra WL e BL (non sono isolate come nelle non volatili)
  ● quando la WL si attiva inietta una corrente sulla BL
  ● Lo stato 1 o 0 corrisponde ad avere o non avere il diodo

ROM MOS
  ● il mos connette la BL
  ● le BL e WL sono isolate
  ● se attivo il mos carico la BL a 1 altrimenti rimane a 0 (primo caso)
  ● ho precaricato la BL a Vdd → se c’è il mos la scarico a 0 altirmenti no   ( secondo   caso   )
  ● leggo il contenuto ma non lo posso modificare
      MOS OR ROM




  sono
         dltnde
 in   modo       →

mutuamente
esclusivo




         ●   tiene le BL a 0 (prescaricate)
         ●   non appena si accende una WL, le BL associate vengono caricate a Vdd (“1”)
         ●   il contatto (connessione tra due linee indicato col puntino nero) prende un area paragonabile a quella
             del transistore (corrisponde al dato)
         ●   nelle memorie l’eliminazione dei contatti riduce l’area della memoria (obiettivo di progetto)
         ●   vdd non è presente tra WL1 e WL2 in quanto fisicamente le linee di Vdd sono separate e le celle pari e
             dispari stanno “dentro due Vdd” e condividono il contatto (in quella banda i mosfet se ci sono
             condividono il contatto. in questo modo si risparmia un contatto (quello condiviso è solo 1))
         ●   architettura di tipo OR → i transistori che connettono una BL a Vdd sono in parallelo
MOS NOR ROM




 ●   architetura NOR → i transistori che connettono la BL a massa sono in parallelo




 ●   le diffusioni corrispondono a gnd
 ●   le connessioni di polisilicio sono le WL
 ●   tra due linee di massa ci sono due WL
 ●   in verticale ci sono le metal 1
 ●   i quadratini neri sono i contatti
   ●   il contatto c’è solo con i transistori di PU in quanto i transistori sono in serie
   ●   più efficace dal punto di vista dell’area
   ●   i mosfet che sono direttamente connessi, sono connessi da una connessione “naturale” in quanto sono
       comunque due tasche n+ in contatto
   ●   architettura NAND → dove c’è il transistore viene impedita la scarica della BL. Tutte le WL sono alte
       tranne quella che voglio selezionare (nand)
   ●   l’informazione consiste nel avere o non avere il transistore
   ●   i transistori che non sono presenti in realtà sono dei transistori con soglia negativa che non possono
       essere mai spenti e quindi non possono essere selezionati



                                "




TRANSISTORI




              È:            •


                                C. C




                                C. L
                                       .




                                       .




   ●   grande compattezza
   ●   in rosso le WL vanno ai transistori (sono i gate)
   ●   dove c’è la METAL1 on diffusion tra due tranistori vuol dire che essi sono cortocircuitati (S=D) (non ci
       sono) pertanto per qualsiasi valore della WL essi sono sempre spenti
           ○ il corcto circuito è nella teraz direzione ovvero corre sopra
           ○ c’è bisogno di un contatto per ogni S e D → ce ne sono tanti (quadratini neri)
   ●   dove non c’è la metal vuol dire che c’è il transistore
   ●   in questo layout i transistori che devono condurre sono quelli cortocircuitati
                                      •       00     8        •




                                      •
                                             •       •       •




                                      •      a       00      ①



                                                                        00   TRANSISTORE
                                             a               •
                                      o              ③




   ●   non ci sono più contatti
   ●   la presenza del transistore è ottenuta con l’alterazione della soglia
           ○ i transistori sono di tipo n con silicio di tipo p
           ○ viene impiantato del silicio di tipo n nel silicio di tipo p (colore rosa)
           ○ in pratica vengono connessi S e D (che sono n+)
           ○ è equivalente ad aver creato una tensione di soglia negativa (il transistor è sempre acceso)
   ●   l’architettura nand ha come svantaggio che le BL hanno connessioni verso massa attraverso
       dei transistori in serie: all’aumentare del numero di transistori tende a rallentare: il ritardo tende
       a crescere in maniera più che lineare (c’è una resistenza e una capacità)


NOR → meno compatta (più contatti), più veloce (transistori in parallelo)
NAND → più compatta, più lenta
Modello equivalente MOS NOR ROM




  ●   la WL è na interconnessione: sistema distribuito di tipo RC che hanno una loro costante di tempo
      intrinseca: il ritardo aumenta più che linearmente con la lunghezza
  ●   le WL sono realizzate il polisilicio e sono dello stesso materiale usato per il gate del transistore
  ●   le BL sono metalliche → l’effetto di resistenza non è critico ma essendo lunga la capacità è grande alla
      quale si aggiunge la capacità parassita del MOS
NOR:
  ● il suo vantaggio è che se viene attivata la cella elementare (transistor n), questa produce una
     connessione tra BL e massa attraverso un solo transistore

NAND:
  ● per la BL si ha una connessione di MOS in serie che possono essere visti come un sistema distribuito
      RC che da un ritardo che cresce più che linearmente col numero di MOS.
  ● ogni mos è dato da una resistenza e una capacità
  ● se devo leggere grandi quantità di dati quello che conta e lo throghput: nelle memorie NAND pur
      avendo l’accesso alla singola informazione relativamente lento, hanno un parallelismo grande quindi lo
      throghput è grande ?



Decreasing WL delay




   ●   la distanza la misuro dal driver → se piiloto da due parti, inietto corrente dagli estremi
   ●   metal bypass → sopra il transistore c’è un metalo che collega source e drain
            ○ l’aggiunta di metal bypass aiuta in quanto è come replicare gli ingressi alla WL e ho
                 praticamente lo stesso segnale in tutta la WL
   ●   siliciuri → sono delle leghe tra metalli e silicio (e quindi anche polisilicio)
            ○ la resistenza del source (n+) è una resistenza di accesso solitamente grande che dipende dalla
                 profondità (verso il basso) della tasca
            ○ non può essere troppo profonda per lo scaling → il mod funziona male
            ○ i siliciuri cortocircuitano la tasca n+ → hanno conducibilità migliori del silicio
Precharged MOS NOR ROM
      FLoating-gate transistor (FAMOS)




               ●    è un mosfet con due gate
                        ○ control gate (quello sopra) → è quello accessibile che può essere polarizzato
                        ○ floating-gate → pilota direttamente la zona attiva (polarizza il silicio, ovvero il mosfet) ma non
                            ha una connessione perchè è circondato completamente dall’ossido (floating). Non è
                            accessibile dall’esterno direttamente
                                ■ è accoppiato capacitivamente sia col control gate (CPP → parallel plate) che con le
                                     tasche del source e drain (CFD , CFS→ floating drain e source di fringing) che con il silicio
                                     (CFB → floating bulk)
               ●    se prendiamo dei condensatori lineari, la carica nel floating gate è:
                        ○ QFG = CPP (VFG - VG) + ma VFS (VFG - VS) + CFD (VFG, - VD) + CFB (VFG - VB)
                        ○ se Ct = Cpp + Cfs + Cfd + Cfb
                        ○ Vfg = (Qfg / Ct) + Cpp*Vg/Ct + Cfd*Vd/Ct + Cfs*Vs/Ct + Cfb*Vb/Ct
               ●    lo stato on/off dipende direttamente dalla tensione al floating gate ma solo indirettamente da quella del
                    control gate




 UFG                                                  nè            Ces
                                                                          ¥       CFS
                                                                                        ¥   +   CFB
                                                                                                            ¥
                                                                                                        .


                                                                              +

                   ¥÷
                                        (                      +
           =                    +
                                            pp
                                                 .




se    US   =
               V8   =   o




Ufo   =



               ¥÷
                            +       (
                                        pp
                                             .




                                                     Viè   t       Ces
                                                                         ¥
f-       ↳ fa
                       Gip        È           Ejus              Ij
     =             •         -
                                          •                -




V6
          '
     =
                           II. vs        Ij
                                     -
                       -




         LETTURA: condizione in cui vado a testare la soglia
            ● supponiamo Vs = Vb = 0 , Vd = Vdt
            ● quale tensione Vg sul gate devo applicare per accendere il transisotre ovvero per far si che Vfg >Vt?
            ● Vt,fg = Vt0
            ● Vt : Vg tale che Vfg = Vt,fg
            ● Vt = Vt,fg*Ct/Cpp - Cfd*Vd/Cpp - Qfg/Cpp = Vt,fg/alpha_fg - Cfd* Vd/Cpp - Qfg/Cpp
                  ○ la Vt è sicuramente più grande di Vt,fg in quanto c’è a denominatore il termine alpha_fg che è
                      sicuramente <1 (Cpp/Ct)
                  ○ il drain contribuisce all’accensione del transistor, con l’accoppiamento capacitico il drain
                      “spinge” il floating gate                    ↳ nell' equazione si riduce la tensione Nt da
                  ○ se metto una carica negativa la soglia sale        applicare nel gala




                                                                                2T   SOGLIA
                                                                            e

                                                                       tensioni
                                                  TSUGA
                                                                       di lettura



              ●   se in questo dispositivo si vanno a iniettare elettroni e si riesce a modulare la carica nel floating gate, la
                  modulazione della soglia è molto efficace. L’effetto è molto robusto
              ●   se Q = 0 la tensione di lettura è maggiore della tensione di soglia e quindi il transistor si
                  accende e leggo una corrente abbastanza alta
              ●   se Q > 0 la tensione di lettura è minore della tensione di soglia (va programmata) e quindi
                  essendo il transistor spento leggo una corrente pressochè nulla
              ●   posso quindi associare allo stato ‘0’ una corrente > 0, e allo stato ‘1’ una corrente nulla
              ●   se la carica è sufficiente e gli ossidi sono abbastanza spessi, la carica rimane immagazzinata e non è
                  volatile (ci vogliono 3 elettronvolt di barriera di potenziale)
                      ○ il dato rimane valido per circa 10 anni
Programmazione floating-gate
Si tratta di iniettare una carica nel floating-gate




Come si riesce a far passare la carica attraverso l’ossido?
I portatori sono confinati nel semiconduttore (non passano attraverso l’ossido) in quanto l’ossido offre una
barriera di energia potenziale molto alta affinchè gli elettroni riescano a passare (circa 3ev). gli elettroni hanno
energie acquisite dell’ordine di decine di mev.
Quando l’elettrone arriva all’ossido vede che l’energia che serve è molto alta e quindi torna indietro (turning
point)




    1. hot-carrier injection → si trova un modo per cedere energia agli elettroni tale da poter passare sopra
       la barriera. Si applicano dei campi elettrici e delle tensioni tra source e drain che non sono consueti per
       il normale funzionamento dei mosfet (tensioni inconsuetamente grandi → 20V). Con una tensione Vg
       molto alta il transistore è molto acceso. In media il campo elettrico vale Vds/L (lunghezza del
       transistore) che non è uniforme ma risulta “piccato” dalla parte del drain.
            a. il campo elettrico è talmente intenso vicino al drain che gli elettroni saltano nel floating-gate
               rimanendo intrappolati (hanno ossido attorno)
            b. occupazione di boltzmann exp(-E/KbT) → si otterrebbe l’effetto anche scaldando
   2. rimuovo queste tensioni dopo che gli elettroni sono stati inseriti nel floating-gate. Avendo messo carica
      negativa la tensione del FG va giù (nell’esempio 5V). La tensione di soglia è cresciuta molto

Funziona bene avendo un ossido spesso (qualche decina di nm)
   ● buono per la ritenzione degli eletroni

Per tirare fuori gli elettroni
   ● il riscaldamento o campo elettrico non funziona (emula un metallo il floating gate)
   ● effetto tunnel se avevo ossidi poco spessi (<10nm)
   ● l’unico modo era toglierle dalla scheda e metterle sotto una lampada UV (optoelettronico)

Inoltre l’iniezione di elettroni tende a rallentare l’iniezione stessa in quanto il processo è autolimitante: quando
inietto elettroni nel floating gate, la tensione nel floating gate si abbassa e questo tende a spegnere l’iniezione
(tende a spegnere il transistore e ricude il campo elettrico che è favorevole ad attrarre elettroni nel floating
gate). Se non fosse limitante porterebbe ad eventi fisici che danneggierebbero la cella stessa
FLOTOX EEPROM




   ●   FLOating Tunneling OXide
   ●   nella regione in cui il floating gate si sovrapponeva con una regione n+ (ad esempio col drain) c’è una
       regione con un ossido più sottile.
   ●   il meccanismo di attraversamento ora è di tipo tunneling (campo elettrico)
           ○ è un meccanismo bidirezionale ovvero posso estrarre o introdurre elettroni semplicemente
               invertendo il campo elettrico
           ○ la probabilità di attraversare la barriera di potenziale decresce espnenzialmente con l’altezza
               della barriera e lo spessore della barriera stessa
           ○ se l’ossido però è troppo sottile ho rischi di leakage
           ○ fissato lo spessore fisico dell’ossido, posso modulare la corrente di elettroni con il campo
               elettrico in quanto riduco il cammino degli elettroni (distanza di tunneling → distanza che
               determina la probabilità che un elettrone possa attraversare la barriera)
                   ■ rendere la barriera “trasparente”

Grafico → se applico una tensione sufficientemente alta allora passerà corrente (di elettroni da silicio a floating
gate). Funziona anche dalla parte opposta e quindi il dispositivo diventa electrically erasable EEPROM

               _
Se applico una tensione negativa, praticamente Si e floating gate (nello schema “poly”) si invertono e quindi
sta volta gli elettroni modulando il campo E vanno dal FG al silicio. Per la lettura leggo la corrente, con una
tensione della WL a seconda di dove è la soglia leggo la corrente o non la leggo

Se programmo miliardi di celle non si può pensare che abbiano tutte la stessa soglia; questo diventa un
problema in quanto, guardando al grafico di lettura, quelle con soglia bassa formeranno un “fascio di corrente”
così come quelle con soglia alta e le cose andranno bene fintanto che le soglie del livello alto e del livello
basso non iniziano a somigliarsi. La distribuzione delle soglie è una figura di merito molto importante.




Nelle FLOTOX (Fowler-Nordheim) il controllo della tensione di soglia è poco preciso. C’è una dispersione
statistica molto grande e spesso certe celle si trovano ad avere una soglia negativa e non è più possibile
spegnerle (overerasing → le celle sono state cancellate troppo)
    ● le WL non idirizzate sono a zero e le celle sulle WL non indirizzate conducono se la soglia è negativa
         quindi è un effetto indesiderato
EEPROM CELL




 ●   si mette in serie al floating gate (quello col beccuccio e i due gate) un access transistor
 ●   quando si ha una cella della quale si fa fatica ad assicurare che sia spenta quanto viene applicata una
     tensione pari a zero, l’access transistor (ha la sua soglia) si prende la WL
 ●   le celle EEPROM sono più grandi delle EPROM



Flash EEPROM




 ●   unisce le caratteristiche delle FAMOS e delle FLOTOX (elettroni caldi e tunneling)
 ●   hanno un ossido sottile tra floating gate e substrato (circa 10nm)
 ●   la programmazione avviene per elettroni caldi (source a massa, gate e drain a tensioni elevate)
 ●   la cancellazione avviene con un meccanismo di tunneling confinato al source: questo è legato alle
     tensioni che vengono usate (control gate a massa e sulla source line si tira sù la tensione a >10V)
         ○ gli elettroni vengono attratti dal source che ha tensione alta e positiva
         ○ il drain non è polarizzato → annulla le correnti e consente di realizzare la cancellazione
             sull’intera matrice
         ○ a livello di blocco viene cancellato l’intero blocco (la source line è unica)
 ●   c’è anche qua il problema delle soglie (OVERERASING)
NOR




 ●    la linea di 12V è la source line
 ●    non c’ il transistore di selezione
 ●    i gate sono a massa, i drain non sono contattati e il source è a 12V
 ●    se si da a tutte le celle uno stesso impulso di cancellazione, quelle che erano scritte e quelle che non
      erano scritte avranno una soglia diversa
           ○ un modo è quello di cercare di uniformare lo stato delle celle prima di cancellarle
           ○ si tende a portare positive le soglie prima di cancellare




 ●    drain e gate alti, source a massa
●   se i mosfet hanno tensione di soglia negativa conducono (non va bene)
NAND




   ●   sono le memorie con cui si arrivano a fare gli SSD
   ●   la cella di memoria è impilata (espansione in verticale)
   ●   per leggere il contenuto di una cella, devono essere accese tutte le altre
           ○ tutte le celle non indirizzate devono avere WL alta e soglia più bassa della WL
           ○ la cella che voglio leggere ha una WL più bassa
   ●   gate a zero, source alto per la cancellazione

Programmazione multilivello: se in un dispositivo fisico riesco ad immagazzinare più di due livelli (vedi il
grafico di lettura, e immagina di avere 4 linee diagonali invece che due → avrei 4 valori quindi 2 bit)
Digital Adders




  ●   nella control processing unit vengono effettuate operazioni di tipo logico e aritmetico (datapath +
      control nello schema)
  ●   questa architettura è quella di von neumann
  ●   nella ALU (dentro il datapath) ci sono gli adders




  ●
Full Adder




  ●   è il blocco elementare per la somma di numeri di n bit (somma due bit)




  ●




  ●
  ●   delete → assicura che il carry out è zero indipendentemente dal carry in (se fosse uno lo cancella) (not
      A and not B)
  ●   propagate → propaga il riporto in uscita (A xor B)
  ●   generate → si genera il riporto indipendentemente dal riporto in ingresso (A and B)
CMOS Full Adder




                 E        7




   ●   x = not Co
   ●   utlizzo il calcolo di Co per il calcolo della somma in modo da ridurre il numero di transistor (infatti non
       servirebbe)
   ●   il calcolo di Co nel circuto di sinistra è uguale a quello definito prima (guarda il PD e vedi che fa (AB +
       Ci (A+B))

S = ABC I + (!A!BCI + !AB!CI + A!B!C I)

CO = AB + AC I + BCI → !CO = !(AB) and !(ACI) and !(BCI) = (!A + !B) (!B + !C I) (!A + !C I)= !A!B + !A!B!CI + !A!CI
+ !B!CI

!CO(A+B+CI) = A!B!C I + BCI!A + !A!BC I che è uguale alla seconda parte dell’ “S” che sarà quindi S=ABC i +
A!B!CI + BCI!A + !A!BC I

   ●   nel circuito di destra guardando al PD ho proprio questa funzione (ricorda che il PD dà la funzione
       negata infatti dopo c’è un invertitore
   ●   se si dovesse implementare la funzione logica originale senza il Co nel S (che è una somma di 4
       termini ognuno composto da 3 ingressi) avrei (3*4)*2 + i 10 transistor per il calcolo di Co + gli invertitori
   ●   il bit di somma dovrà aspettare il Co che è quello che si deve propagare e che dà il percorso critico
       quindi anche se la somma aspetta Co non è un problema
   ●   in questo schema ci sono delle criticità come ad esempio le lunghe serie di transistori in serie
Mirror Adder




  ●   il PU e il PD sono speculari
  ●   l’organizzazione speculare di un gate cmos non è così banale ovvia, la condizione necessaria per una
      sintesi corretta di un gate cmos è quella che la funzione logica di PU e PD siano l’una il negato
      dell’altra. Questo assicura che PU e PD siano attivi in modo mutiamente esclusivo (ci sarebbe una
      contesa nel pilotaggio dell’uscita)
  ●   questi gate non sono duali ma soddisfano la condizione dei CMOS ovvero che PU e PD siano attivi in
      modo mutuamente esclusivo
  ●   di buono c’è il fatto che per il bit di Co adesso il circuito che lo produce ha al massimo due transistori in
      serie sia per salita che per discesa
  ●   kill = delete
  ●   il circuito a sinistra è composto da tre “pezzi” che gestiscono generate, delete e propagate (guarda
      immagine) per la generazione di !Co
            ○ Co = G + maaD + Ci (A + B)
  ●   il circuito a destra produce !S
            ○ !S = ABC i + Co(A+B+Ci)
  ●   E’ diminuito il numero di transistori ma soprattutto si è snellita la generazione del C o (per il fatto che ho
      al caso peggiore 2 transistori in serie nel PU e nel PD
  ●   il Ci è collegato molto vicino all’uscita (è sempre il transistor più vicino al nodi di uscita); infatti se per
      esempio nel PD del nodo S, A e B sono a uno e dovrebbe esserlo anche C i ma esso non è ancora
      arrivato, nel frattempo il source del transistor di Ci sarà già stato scaricato a massa. Quando arriva Ci
      c’è solo un transistor da scaricare. Se fosse stato il più lontano, le capacità intermedie non avrebbero
      potuto scaricarsi a massa. E’ sempre meglio avere i segnali critici vicino al nodo di uscita
●
●   il nodo Co è elettricamente pesante nel senso che ha colegate 4 capacità di diffusione delle giunzioni (a
    sinistra) due capacità interne e sei capacità del gate che segue
Transmission gate Full Adder




  ●   essendo incentrato sullo XOR è bene utilizzate i pass-transistor di tipoi transmission gate (lo XOR puà
      essere visto come un multiplexer portando in uscita b se a è negato ad esempio)
  ●   ci sono sia P che !P in quanto servono entrambi negli step successivi
  ●   in questo schema si fa uso del propagate (A xor B)
          ○ se A=0 è acceso il pass-transistor in alto e viene portato B in P (l’invertitore a destra di P è in
             alta impedenza in quanto le alimentazioni sono girate)




           ○
           ○ se A=1 il pass-transistor è spento e viene portato !B in P dall’invertitore
  ●   il negato dell’xor è l’equivalence (AB + !A!B)
  ●   Sum
           ○ S = P exor Ci
           ○ il nodo intermedio implementa l’equivalence, infatti il pass-transistor sopra è di tipo !P che fa
              passare !Ci , quello sotto è di tipo P che fa passare Ci
  ●   carry out
           ○ Co = G + PCi
           ○ Se P = 0 A e B devono essere uguali in quanto P = A exor B
Ripple-Carry Adder




   ●   la catena dei riporto è il persorso critico
   ●   tsum → tempo necessario per il singolo FA per generare la somma
   ●   tcarry → tempe necessario per il singolo FA per generare il carry in uscita
   ●   il carry si deve propagare per N - 1 FA



Inversion Property




   ●   il negato della somma degli ingressi in forma vera è la somma degli ingressi in forma negata
   ●   stessa cosa per il carry out
   ●   vale solo in questo caso

Se questa cosa è vera allora posso “mangiarmi l’invertitore in uscita
●   dal punto di vista del ritardo di propagazione viene migliorato in quanto gli inverter che servono per
    negare gli ingressi, rendono disponibile l’ingresso agli stadi quando il primo stadio sta propagando il
    carry out del primo stadio
●   primo stadio → carry negato
●   secondo stadio → ingressi negati → carry dritto e somma negata
                                         OUT
Carry Bypass Adder




                           /   b        tà
                                        STADIO
                     TOTAL /
                               STADIO
Linear Carry Select Adder




  ●   nell’ottica di guadagnare tempo, calcolo tutte e due le possibilita di carry out (o zero o uno)
  ●   con un multiplexer seleziono quello giusto quando mi arriva il carry in




  ●   divido il numero di 16 bit in 4 gruppi → gli ingressi arrivano ai 4 stadi contemporaneamente e possono
      andare avanti in parallelo (setup degli ingressi)
  ●   tutti gli stadi calcolano il carry out sia nel caso che il Cin sia 0 che nel caso sia 1 (cin non è ancora
      arrivato
  ●   quando arriva il vero carry in nel primo stadio, calcola la somma e manda il carry out allo stadio
      successivo che ha già calcolato tutto e deve solo fare il multiplexing a seconda del carry che gli arriva
      dal primo stadio
  ●   N = numero di bit, M = numero di bit in ogni sottogruppo, tsetup = tempo necessario per il setup dei bit di
      ingresso, tcarry= ritardo del primo gruppo per produrre il carry (sono M bit), tmux = ritardo legato ai
      multiplexer (che sono N/M)
  ●   quello che guardiamo è la dipendenza da N numero di bit; se tmux/M è apprezzabilmente più piccolo di
      tcarry (che era quello legato a N nel ripple adder) allora il ritardo di propagazione crescerà più
      lentamente all’aumentare del numero di bit




Square Root Carry Select




  ●   il più a sinistra ha soltanto due bit, quello immediatamente successivo ne prende 3, e così via
  ●   è inutile che i blocchi più a destra finiscano assieme al primo perchè tanto poi rimangono in attesa
  ●   rendo il blocco di sinistra meno profondo e quindi più veloce, di fatto la velocità di propagazione
      diminuisce gradualmente verso destra
●   ogni blocco dovrebbe essere dimensionato in modo che l’ultimo finisca il setup e la generazione dei
    due carry out poco prima che arrivi il carry in
●   la dipendenza del ritardo da N non è più lineare (radice quadrata di N)
