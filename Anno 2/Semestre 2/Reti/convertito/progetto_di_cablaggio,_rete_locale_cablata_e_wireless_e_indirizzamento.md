---
fonte: "progetto_di_cablaggio,_rete_locale_cablata_e_wireless_e_indirizzamento.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Reti di Calcolatori
                            Esercitazione di laboratorio su progetto di cablaggio strutturato e rete locale
                                                              Pier Luca Montessoro

1. Obiettivo
Scopo della presente esercitazione è sviluppare un progetto di massima di una rete
locale e del relativo cablaggio strutturato per l’edificio di cinque piani rappresentato a
lato. Le planimetrie sono disponibili sul sito web del corso nella sezione “Esercitazioni di
laboratorio”.

2. Requisiti di progetto: cablaggio strutturato
È richiesto un cablaggio standard ISO/IEC11801 con 2 prese in rame per ogni posto di
lavoro.
In aggiunta alla topologia stellare è richiesta l’introduzione di collegamenti in rame
(almeno 4 cavi da 4 coppie) tra gli armadi adiacenti, per la realizzazione di reti fisiche di
                                                                                                             piano terreno                                                                                  LAN produzione
estensione limitata in piccole zone dell’edificio e per eventuali cammini ridondanti per                                                                                                                    LAN amministrazione
soluzioni fault tolerant.                                                                                                                                                                                   LAN sperimentale
Uno dei locali dell’edificio (adeguatamente indicato nelle planimetrie) dovrà essere adibito
                                                                                                                                                                                                             m 27
a sala macchine e ospiterà i server.                                                                                                    hall


Un centralino telefonico sarà ospitato nel vano al piano terreno che ospiterà anche




                                                                                                                                                           ascensori
l’armadio di centro stella di edificio; in tale vano arriveranno i collegamenti ai servizi
esterni.




                                                                                                      m 35
                                                                                                                                                                                           locale             sala macchine
3. Requisiti di progetto: rete locale                                                                                                                                                      tecnico               (server)
                                                                                                                                                                                                                              servizi




Si devono realizzare tre reti locali fisicamente distinte, interconnesse tramite router, di cui                                                sala riunioni



due estese in tutto l’edificio (una per l’amministrazione, l’altra per la produzione) e una                             scale


sperimentale in una sola zona, agli ultimi due piani (v. planimetrie a fianco). Nelle                               locale tecnico
                                                                                                                      (centralino
                                                                                                                      telefonico)
planimetrie sono indicati con simboli differenti i posti di lavoro che devono essere serviti
dalle tre reti. In alternativa alla realizzazione di reti fisicamente distinte è possibile valutare                                                                         m 50
l’impiego di Virtual LAN.
La rete locale dovrà prevedere un minimo di ridondanza sul centro stella e sul
                                                                                                                piani 1o e 2o                                                                               LAN produzione
                                                                                                                                                                                                            LAN amministrazione
collegamento dei server, con un limitato impatto sui costi.                                                                                                                                                 LAN sperimentale
Inoltre, si vuole servire il piano terreno dell’edificio con una rete WiFi. Facendo uso di
                                                                                                                                                                                                             m 27
strumenti di simulazione di copertura radio (per esempio il tool online gratuito
https://www.cambiumnetworks.com/products/software/wifi-designer/) si definiscano numero




                                                                                                                                                                ascensori
e posizioni degli access point necessari.
                                                                                                         m 35
4. Requisiti di progetto: piano di indirizzamento IP                                                                                                                                            locale
                                                                                                                                                                                                                              servizi
                                                                                                                                                                                               tecnico

All’ente è stata assegnata la rete di classe C 196.111.250.0, con la quale deve essere
realizzato l’intero piano di indirizzamento della rete cablata; si prevede che ognuna delle tre
reti locali utilizzerà al massimo 62 indirizzi IP pubblici. La rete WiFi fornisce invece indirizzi                        scale



privati tramite DHCP e quindi gli access point devono essere collegati ad una interfaccia                                 locale
                                                                                                                         tecnico

del router con funzionalità di NAT.
                                                                                                                                                                                 m 50

5.   Passi progettuali: cablaggio strutturato
                                                                                                                    piani 3o e 4o                                                                            LAN produzione
•    Definire la dislocazione degli armadi                                                                                                                                                                   LAN amministrazione
•    Definire i passaggi dei cavi di dorsale                                                                                                                                                                 LAN sperimentale
•    Definire i punti dove collocare le prese telematiche
                                                                                                                                                                                                               m 27
•    Definire delle possibili canalizzazioni dove poter installare successivamente il cablaggio
                                                                                                                                                                            ascensori




     orizzontale
•    Calcolare il numero totale di prese utente
•
                                                                                                             m 35




     Calcolare il numero totale di prese nei pannelli di permutazione degli armadi
     (calcolandone il numero per ogni armadio, sia in rame che in fibra ottica)                                                                                                                    locale
                                                                                                                                                                                                  tecnico
                                                                                                                                                                                                                                 servizi


•    Calcolare la quantità di cavo necessaria (sia in rame che in fibra ottica), specificandone
     il tipo scelto                                                                                                             scale

•    Riportare un elenco di massima dei componenti che si utilizzerebbero (possibilmente
                                                                                                                             locale
     con foto tratte dai cataloghi dei produttori).                                                                         tecnico




6.   Passi progettuali: rete locale                                                                                                                                                     m 50


•    Disegnare la topologia logica della rete locale, indicando, per ogni apparecchiatura di rete necessaria, il tipo, l’armadio presso cui
     verrà installata, il tipo e la topologia dei collegamenti alle altre apparecchiature
•    Riportare un elenco di massima degli apparati scelti (possibilmente con foto tratte dai cataloghi dei produttori)
•    Evidenziare alcuni esempi di guasti tollerabili (coperti dalla ridondanza) e guasti non tollerabili (bloccanti tutta o parte della la rete)

7. Passi progettuali: piano di indirizzamento IP
Definire il piano di indirizzamento IP indicando:
•   per le apparecchiature di rete, tutti gli indirizzi IP necessari;
•   per gli elaboratori degli utenti ed i server, un esempio di indirizzo per ogni rete per ogni piano.

Riferimenti: per le tipologie e i costi dei componenti si possono visitare i siti dei produttori, ad esempio http://www.vimar.it,
http://www.te.com, ecc., ma anche semplicemente Amazon..
