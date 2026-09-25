---
fonte: "esperienza 4.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Reti di Calcolatori

      Esercitazione di laboratorio sui protocolli del livello applicazione (network analyzer)


Pier Luca Montessoro


1.        DNS
Si descrivano i messaggi intercettati relativi alle interrogazioni DNS.

Durante la query di nslookup, siccome permette all’utente di scrivere solo un dominio
parziale, vengono create molte query in contemporanea con più domini. Queste richieste
con dei domini non esistenti, non ottengono una risposta con un campo Answer

     -​   nei primi pacchetti in cui viene interrogato il DNS, si può osservare come nel campo
          Queries c’è indicato il type=A
              -​ Nel pacchetto di risposta, c’è un campo aggiuntivo “Answers”:




     -​   nelle successive richieste, sempre con type=A, si può vedere come il server di
          risposta risulta diverso e anche il pacchetto mandato dal server ha un campo
          “Answer” con un contenuto simile al precedente, ma che presenta delle differenze




Siccome il server DNS è interno, è necessario cambiare il server in: 158.110.1.7 per poter
ottenere le informazioni desiderate dalla query type=MX
Si vede poi come la risposta fornita dal DNS ha indirizzi ip diversi tra ww.uniud.it e uniud.it




2.     FTP



Si può notare come i pacchetti contenenti le credenziali utilizzate per il login siano in chiaro,
ovvero, se un malintenzionato sta sniffando i pacchetti, può vedere le credenziali da usare.

a. Si visualizzi la lista dei file contenuti nella home directory dell’utente demo_reti sul server
allegro.diegm.uniud.it e si descrivano relativi i messaggi intercettati.

Viene instaurata una connessione di un server TCP sulla porta 21 per il trasferimento dei
file.




Come si può notare, sono presenti più pacchetti del protocollo TCP in quanto i primi sono
per instaurare la connessione (3 way handshake), uno restituisce la risposta e altri per
chiudere la connessione.
b. Si effettui la copia sul vostro disco locale del file che si trova in tale direttorio e si
descrivano relativi i messaggi intercettati.

Una volta ricevuta la risposta del server in cui viene accettato il comando, inizia il
trasferimento dei file tramite protocollo TCP. La porta utilizzata dal TCP non è la solita porta
20, ma 21. Questo indica che è stata aperta una connessione e il trasferimento dei dati
viene eseguito con un protocollo affidabile.​
Una volta completato il trasferimento del file, viene chiusa la connessione e il protocollo FTP
risponde che l’operazione è stata eseguita.
Come si può vedere, il contenuto del file è stato visualizzato in chiaro come la richiesta dei
file e le varie risposte affermative da parte del server.



3.    HTTP



Si descrivano relativi i messaggi intercettati durante la navigazione su un sito web HTTP:

Una volta aperto il sito, dal protocollo HTTP, si può vedere la GET della pagina pagina
HTML che compone il sito base. Si possono vedere numerose richieste per tutte le immagini
che vengono spedite una per volta. Oltre a ciò, si può vedere come la pagina principale è
troppo grande per essere inviata in un pacchetto solo e viene frammentata.
