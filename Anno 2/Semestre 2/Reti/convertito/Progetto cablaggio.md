---
fonte: "Progetto cablaggio.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

UNIVERSITÀ DEGLI STUDI DI UDINE
            FACOLTÀ DI INGEGNERIA




        Dipartimento di Ingegneria Elettronica
            Corso di Reti dei Calcolatori




PROGETTO SUL CABLAGGIO STRUTTURATO




                                                 Membri:​
                                                 Stefano Bortolussi​
                                                 Veronica Maniscalco​
                                                 Luca Pes




          ANNO ACCADEMICO 2024/2025
INDICE
INDICE​                      1
OBBIETTIVO​                  2
CABLAGGIO STRUTTURATO​       2
RETE LOCALE​                 5
   Topologia​                5
   Armadi di permutazione​   6
   Fault tolerance​          8
   VLAN​                     8
PIANO INDIRIZZAMENTO​        9




                             1
OBBIETTIVO
Lo scopo della presente esercitazione è sviluppare un progetto per la realizzazione di una rete locale
(LAN) e del relativo cablaggio strutturato in un edificio a cinque piani. L’obiettivo è garantire
connettività ad alta efficienza, scalabilità e sicurezza, rispettando gli standard internazionali
(TIA/EIA-568, ISO/IEC 11801) e le esigenze dell’utenza.


CABLAGGIO STRUTTURATO

L'edificio si compone di due parti: il piano terreno, che è composto dalla hall, una sala riunioni e
qualche ufficio, ed i restanti 4 piani, contenenti solo ed esclusivamente uffici. Per normativa di legge
una postazione di lavoro occupa non meno di 10 m^2 di spazio utile e pertanto gli edifici
dell’immobile sono stati suddivisi logicamente in:

-     Uffici di dimensione piccola: aventi una metratura di 23 m^2 e quindi utilizzabili da non più di
    due dipendenti;

-     Uffici di dimensione grande: aventi una metratura di 40 m^2 e quindi utilizzabili da non più di
    quattro dipendenti;

Ogni postazione di lavoro è dotata di due prese di rete, entrambe realizzate con connettori di tipo
RJ45, al fine di garantire una connettività stabile e ridondante per dispositivi informatici e telefonici.
La scelta di adottare connettori RJ45 anche per i terminali telefonici rappresenta una soluzione
strategica in quanto permette il facile interscambio tra dispositivi di tipo dati e voce. Grazie alla
standardizzazione del cablaggio, è infatti possibile adattare dinamicamente la destinazione d’uso delle
prese di rete senza interventi hardware aggiuntivi, contribuendo così a una maggiore efficienza
operativa.

Inoltre ogni ufficio piccolo dispone di quattro prese aggiuntive mentre ogni ufficio grande di sei, al
fine di garantire la funzionalità dell’ufficio anche considerando l’eventuale spostamento di mobilio.

In fase di analisi preliminare, è emerso che l'edificio non dispone né di pavimento flottante né di
controsoffitto, elementi comunemente utilizzati per l’alloggiamento delle infrastrutture di rete. Per
ovviare a tali limitazioni, si è deciso di far passare i cavi all'interno delle pareti, attraverso canaline
incassate, al fine di garantire sia l’estetica che la protezione dell’impianto. È stato inoltre deciso di
adottare cavi di rete di categoria Cat 6, affiancati da prese di tipo RJ45 compatibili, in modo da
garantire prestazioni elevate e affidabilità nel tempo. Questa scelta si basa sul fatto che i cavi Cat 6
supportano pienamente lo standard Gigabit Ethernet (1 Gbps) che rappresenta una velocità
considerata adeguata e coerente con le esigenze tipiche di un ambiente d’ufficio generalizzato. Tale
velocità consente un’ottima gestione del traffico dati, inclusi trasferimenti di file, utilizzo di
applicativi in rete, videoconferenze e navigazione simultanea da più postazioni. Inoltre, l’utilizzo del
Cat 6 rappresenta un investimento lungimirante, in quanto offre una maggiore capacità di banda e
migliori prestazioni rispetto ai cavi di categoria inferiore, risultando così adatto anche a futuri
ampliamenti o aggiornamenti della rete.

I cavi di rete orizzontali sono utilizzati per collegare le prese installate presso le postazioni di lavoro ai
permutatori di piano, ovvero gli armadi di distribuzione situati su ciascun livello dell’edificio. Da
questi permutatori, i collegamenti proseguono verso il permutatore di edificio attraverso una dorsale
in fibra ottica, che garantisce elevate prestazioni e larghezza di banda su lunghe distanze.


                                                                                                            2
Per migliorare l'affidabilità complessiva dell'infrastruttura di rete e assicurare la continuità del servizio
anche in caso di guasto di un collegamento della dorsale principale, i permutatori dei diversi piani
sono collegati tra loro tramite connessioni in rame. Questi collegamenti supplementari, sebbene non
primari, svolgono una funzione di ridondanza, permettendo il reindirizzamento del traffico di rete
attraverso percorsi alternativi in caso di interruzioni o malfunzionamenti.

Di seguito è riportata una tabella riepilogativa dei costi e dei materiali preventivati:

  Componente          Modello          Rivenditore        Quantità        Costo unitario     Costo totale
                                                                          (IVA inclusa)

   Dorsale in       OM4LCDX                FS               120 m           1.36 €/m            168 €
   fibra ottica

   Dorsale in      C6UTPSGSP               FS               20 m            1.097 €/m            22 €
     rame              VC

   Prese RJ45         3253541          Amphenol              516              92.52             4.774€
     doppie

    Cavi cat6       PFM923I-6U           Dahua            48335 m           0.514 €/m          2.4880 €
                       N-C


Si riporta lo schema delle canalizzazioni e della predisposizione delle porte di rete. Si evidenzia in
colore violetto il percorso delle canalizzazioni e in blu le prese di rete (2 per blocco evidenziato).




                                                                                                            3
Si riporta un dettaglio del progetto per maggior comprensione




                                                                4
RETE LOCALE

Topologia
La topologia di rete sotto riportata, prevede una struttura gerarchica a stella, con switch di piano
(Switch piano 1-4) identici per ciascun livello (dal primo al quarto piano), rappresentati in modo
semplificato nello schema per garantire chiarezza e una maggior leggibilità, omettendo i dettagli
ridondanti dei collegamenti verso gli host.​
Lo switch di centro stella è stato implementato in configurazione ridondata insieme ai collegamenti
verso gli switch di piano e al server DHCP presente. Questo garantisce una maggior resilienza contro i
guasti critici che si possono verificare nella rete.
Al piano terra, oltre ai due switch dedicati all’interconnessione degli utenti, sono presenti i
collegamenti verso i quattro access point necessari per la copertura wireless dell’intera area. Per
rafforzare la sicurezza, inoltre, è stato integrato un firewall con funzionalità di filtraggio del traffico in
ingresso e in uscita. È stato deciso un
È stato riportato lo schema topologico della rete. I piani dal primo al quarto, caratterizzati dagli switch
di piano (Switch piano 1-4) presentano un livello inferiore di switch. La stessa struttura è identica in
tutti i piani, è stato riportato per chiarezza e leggibilità unicamente un piano, senza specificare tutti i
collegamenti verso gli host e proponendo un semplice esempio.




                                                                                                            5
Armadi di permutazione
Gli armadi di permutazione (o armadi rack) sono elementi fondamentali del cablaggio strutturato, essi
sono progettati per ospitare e organizzare i dispositivi di rete (switch, router, patch panel) e i punti di
terminazione dei cavi. Posizionati strategicamente su ciascun piano, garantiscono una distanza
massima di 90 metri (orizzontale + patch cord) dalle prese utente, conformemente agli standard per
prestazioni fino a 500 MHz (Cat 6A). In contesti con estensioni superiori ai 100 metri, è prevista
l’installazione di armadi aggiuntivi per rispettare i parametri di attenuazione del segnale.

Per garantire la completa connettività delle 234 prese di rete presenti sui piani dal primo al quarto,
sono stati implementati 5 patch panel da 48 porte ciascuno. Ciò permette una copertura di 240 porte
totali con un margine residuo di 6 porte per eventuali utilizzi temporanei. ​
​
La soluzione propone l’utilizzo di patch cord modello FME 23540 forniti da Elettronew, essi sono
caratterizzati da una lunghezza di 0,5 metri particolarmente adatta per collegamenti intra-armadio.
Tali patch cord, al costo unitario di € 2,12 (IVA inclusa), presentano piena compatibilità con il
cablaggio orizzontale che fa uso di Cat 6, garantendo prestazioni certificate. La scelta è stata presa
basandosi su criteri di economicità, prestazioni e funzionalità.

Per garantire un’efficiente gestione del traffico all’interno della rete, è stata adottata una topologia
gerarchica a tre livelli, implementando uno switch di distribuzione per piano (24 porte) e degli switch
di accesso (48 porte) per la connessione alle singole porte. La soluzione proposta prevede l’utilizzo di
cinque switch MikroTik CRS354 (forniti da OMG.de al costo unitario di € 538 IVA inclusa), ciascuno
dotato di 48 porte Ethernet Gigabit e 4 porte SFP+ per il collegamento in fibra ottica, garantendo così
scalabilità e ridondanza.

Viene riportata la tabella riassuntiva dei vari componenti inseriti nell’armadio di permutazione dei
piani dal primo al quarto.


                                                                         Costo Unitario
  Componente           Modello        Rivenditore       Quantità                               Costo Totale
                                                                         (IVA inclusa)

 Patch Panel 48
                      CP48BLY            Rexel              5                97,60 €             488,00 €
     porte

   Patch Cord         FME 23540       Elettronew           234                2,12 €             496,08€

                       MikroTik
Switch 48 porte                         OMG.de              5               538,00 €            2.690,00 €
                       CRS354

                       MikroTik
Switch 24 porte       CRS326-24         OMG.de              1               169,28 €             169,28 €
                       G-2S+IN

Il primo piano è strutturato diversamente rispetto agli altri e l’armadio di permutazione conterrà
dispositivi in quantità differente, infatti, le porte da gestire sono nettamente inferiori.
Per la gestione delle 96 porte presenti sono necessari unicamente 2 switch di accesso e altrettanti
patch panel come riportato nella tabella riassuntiva:




                                                                                                         6
                                                                            Costo Unitario
  Componente            Modello          Rivenditore         Quantità                          Costo Totale
                                                                            (IVA inclusa)

 Patch Panel 48
                       CP48BLY              Rexel                2              97,60 €          195,20 €
     porte

  Patch Cord          FME 23540          Elettronew             96              2,12 €           203,52 €

                        MikroTik
Switch 48 porte                           OMG.de                 2             538,00 €         1.076,00 €
                        CRS354

                      MikroTik
Switch 24 porte      CRS326-24G-          OMG.de                 1             169,28 €          169,28 €
                       2S+IN


 L’armadio di centro stella (o di edificio) ha una struttura unica rispetto agli altri armadi di
 permutazione, esso, infatti, contiene degli apparecchi di rete necessari al collegamento con i vari
 servizi forniti dall’ISP.


                                                                            Costo Unitario
  Componente             Modello           Rivenditore        Quantità                         Costo Totale
                                                                            (IVA inclusa)

 Patch Panel 24
                       UPP6001-24             Rexel               1             51,85 €           51,85 €
     porte

Patch Panel fibra    FHD-FAP12LCD
                                              fs.com              1             30,50 €           30,50 €
    12 porte             XSMF

Switch con porte         TP-Link
                                             TP-Link              2            189,99 €          379,98 €
   per fibra           TL-SG2016P

                       MikroTik
     Router                                 MikroTik              1            366,00 €          366,00 €
                     RB4011iGS+RM


 Sono stati inseriti nell’armadio di centro stella due switch aventi 5 porte per la fibra utilizzate come
 dorsali per connettere gli armadi di piano posti nell’edificio. È stato deciso di inserire un secondo
 switch per una questione di robustezza della rete; introducendo una ridondanza nel nodo centrale
 dell’edificio, si riesce a sopperire ad alcuni dei guasti considerati come intollerabili.​
 Lo switch presenta altre 4 porte per una connessione con doppino Cat6 utilizzabile per la connessione
 dei vari access point presenti nel pian terreno dell’edificio, esse, inoltre, sono fornite di tecnologia
 PoE. Il router proposto offre la possibilità di configurare un firewall per una maggior protezione della
 rete, andando a filtrare il traffico in ingresso e in uscita e potendo personalizzare i criteri dei filtri
 utilizzati.
 Per il pian terreno è stata predisposta una connessione Wi-Fi tramite l’utilizzo di access-point. Sono
 stati proposti e installati dei TL-WA1201 della TP-Link che forniscono una buona copertura. Per
 l’alimentazione degli stessi si possono sfruttare le porte PoE dello switch e tale tecnologia è
 supportata dagli access point proposti. Il costo del singolo è di € 39.99 (IVA inclusa) e, dopo
 un’attenta analisi e progettazione, sono risultati necessari unicamente 4 access point per fornire una
 buona copertura dell’intera area di interesse. Il costo totale è di € 159,96 (IVA inclusa) acquistabili da
 TP-Link direttamente.​



                                                                                                         7
​
I costi totali degli armadi di permutazione vengono riportati nella tabella riassuntiva posta di seguito:


            Elemento                            Quantità                          Costo Totale

       Armadio piano 1-4                            4                             15373,44 €

      Armadio pian terreno                          1                              1644,00 €

      Armadio centro stella                         1                               828,33 €

          Access Point                              4                               159,96 €



Fault tolerance
Per garantire robustezza e sicurezza all’infrastruttura di rete, è stata implementata una topologia
gerarchica a tre livelli che permette di isolare efficacemente eventuali guasti e limitare la
propagazione del traffico non necessario. ​
Nella progettazione della rete, è fondamentale distinguere tra guasti tollerabili e intollerabili per
valutare l’impatto sull’operatività dell’intera rete e azienda.​
I guasti tollerabili includono il malfunzionamento di uno switch del livello più basso che isolerebbe al
massimo 48 porte, o l’interruzione di un collegamento orizzontale o di una singola presa, limitando
l’inacessibilità a un unico host. Questi scenari, seppur critici, non compromettono l’intera
infrastruttura e possono essere gestiti e risolti con interventi tempestivi.​
Al contrario, i guasti intollerabili, coinvolgono componenti centrali e critici come gli switch del
secondo livello o gli switch core (primo livello), la cui rottura causerebbe l’isolamento di un intero
piano o dell’azienda stessa. Tale distinzione sottolinea l’importanza di implementare delle ridondanze
mitigando i rischi di guasti intollerabili e limitando i guasti localizzati.

VLAN
La soluzione adotta switch di livello 3 che supportano la tecnologia VLAN, esse sono fondamentali
per segmentare e suddividere logicamente la rete secondo le specifiche di progetto. ​
Le VLAN possono essere suddivise in due classi principali: la prima fa uso di una programmazione
delle porte dello switch assegnando ciascuna a una VLAN precisa. La seconda fa uso degli indirizzi
MAC che vengono assegnati a una VLAN. Per quanto riguarda le specifiche del progetto, non
essendo presente alcun vincolo, si è deciso di optare per una VLAN basata sulle porte degli switch.
Questo rende più veloce la configurazione delle stesse e non è richiesto l’indirizzo MAC di ogni
dispositivo connesso. Entrambe le soluzioni richiedono degli interventi in caso di modifiche della rete
e si presuppone che i dispositivi non vengano spostati da un ambiente lavorativo all’altro. Per far
comunicare delle VLAN su più switch a causa di mancanza di porte libere sullo stesso o per la
distribuzione della stessa rete logica su più piani, è necessario usare un collegamento trunk.




                                                                                                            8
    PIANO INDIRIZZAMENTO
    La rete dell’edificio è suddivisa in 3 VLAN di tipo produzione, amministrazione e sperimentale in
    grado di gestire in modo autonomo il proprio traffico, garantendo isolamento logico, sicurezza e una
    gestione più ordinata delle risorse di rete. Oltre alle 3 reti locali virtuali, le quali dispongono al
    massimo di 62 indirizzi IP pubblici ognuna, è presente anche una rete wifi la quale copre solo il piano
    terreno ed è predisposta all’assegnazione dinamica degli indirizzi IP tramite DHCP per dispositivi
    mobili e computer portatili.
    All’ente è stata assegnata la rete di classe C 196.111.250.0, la quale copre un totale di 254 indirizzi
    escludendo l’indirizzo di rete e quello di broadcast.
    Disponendo di un numero di indirizzi IP pubblici nettamente inferiore rispetto al numero di indirizzi
    necessario al fine di strutturare il piano di indirizzamento dell’intero edificio, viene fatto uso del
    servizio NAT (Network Address Translation) il quale permette di risparmiare indirizzi pubblici in
    quanto limitati e di mascherare gli indirizzi privati nella comunicazione con internet e server esterni al
    fine di proteggerli.
    La NAT effettua una traduzione degli indirizzi privati in un indirizzo pubblico associato all'interfaccia
    del router con internet.


                                           IP                                     RANGE IP
     VLAN              IP RETE                              NETMASK                                   NETMASK
                                       BROADCAST                                   PRIVATI

                                                                                 192.168.0.0 -
  1.Produzione       196.111.250.0      196.111.250.63      255.255.192.0                             255.255.248.0
                                                                                 192.168.2.255

                                                                                 192.168.3.0 -
2.Amministrazione    196.111.250.64    196.111.250.127      255.255.192.0                             255.255.248.0
                                                                                 192.168.3.255

                                                                                 192.168.4.0 -
 3.Sperimentale     196.111.250.128    196.111.250.191      255.255.192.0                             255.255.248.0
                                                                                 192.168.5.255

                                                                                  192.168.6.0 -
     4.WiFi                /                   /                   /                                  255.255.248.0
                                                                                  192.68.6.255



    Le 3 VLAN coprono un totale di 1140 indirizzi, 524 di produzione, 212 di amministrazione e 404 di
    sperimentale. Per creare un’unica rete suddivisa in 3 VLAN e contenente tutti gli IP privati è
    necessario fare uso di una netmask 255.255.248.0 (/21). Nel piano di indirizzamento alla VLAN1
    sono stati assegnati 765 indirizzi per ragioni di organizzazione e ordine, inoltre, in questo modo,
    rimarranno degli indirizzi privati inutilizzati che garantiranno una copertura più ampia in vista di
    sviluppi futuri. Allo stesso modo anche le altre due VLAN presentano degli indirizzi aggiuntivi per le
    medesime ragioni.
    La rete Wifi fa uso di IP privati, i quali vengono assegnati dinamicamente e in modo autonomo
    tramite DHCP. Questa assegnazione dinamica permette l’utilizzo di uno stesso indirizzo IP a utenti
    diversi e in momenti diversi. Dopo un certo tempo di lease, previo rinnovo, il DHCP dunque riassegna
    l’indirizzo a un altro utente. È stato predisposto un massimo di 256 utenti che facciano uso della rete
    in contemporanea.




                                                                                                            9
Il DHCP fornisce le seguenti informazioni:
    -​ indirizzo IP (privato) dell’host
    -​ netmask che va a definire l’ambito della rete locale
    -​ indirizzo IP del default gateway: 192.168.7.254 necessario per raggiungere le reti esterne
    -​ server DNS: 8.8.8.8 (il server DNS primario di Google)
In questo modo si garantisce un utilizzo efficiente degli indirizzi IP disponibili e un’architettura
scalabile, sicura, organizzata e in grado di evolversi con le esigenze future dell’ente.

Si riporta la disposizione degli access point wifi che riescono a coprire in maniera sufficiente ed
adeguata tutta la superficie del primo piano. Si è deciso di utilizzare quattro access point in quanto la
copertura offerta da 3 soli risulterebbe molto limitata e alcune aree all’interno del piano risulterebbero
non coperte.




                                                                                                       10
