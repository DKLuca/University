---
fonte: "25_Seminario-Accessibilita-Web.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Accessibilità web
   David Trevisan
    2026-05-21




   David Trevisan · UniUD   1
     PARTE 1

La teoria




David Trevisan · UniUD   2
Cos’è l’accessibilità digitale?

   Progettare siti e strumenti digitali in modo che tutte le persone,
   indipendentemente da eventuali disabilità, possano utilizzarli in modo
   autonomo.

             16%
        della popolazione mondiale
                                                    96%
                                                   delle homepage ha
                                                                                       87M
                                                                                   persone nell'UE vivono
    vive con una disabilità (OMS, 2023)   almeno un errore WCAG (WebAIM, 2024)   con una disabilità (Eurostat)




                                               David Trevisan · UniUD                                            3
Tipologie di disabilità

 Permanenti                    Temporanee                      Situazionali
   Cecità                        Braccio ingessato               Sole sullo schermo
   Sordità                       Occhio infiammato               Una mano occupata
   Paralisi motoria              Recupero post-operatorio        Ambiente molto rumoroso
   Daltonismo

  Curb-Cut Effect
  I marciapiedi abbassati nascono per le sedie a rotelle, ma li usano tutti: ciclisti,
  genitori col passeggino e corrieri.




                                    David Trevisan · UniUD                                 4
Perché è importante




     David Trevisan · UniUD   5
Un diritto fondamentale

 🏥 Salute
   Prenotare visite, leggere referti, accedere al                  🎓 Istruzione
                                                                     Piattaforme e-learning, materiali didattici, iscrizioni
       fascicolo sanitario                                               universitarie

 🏛️ Pubblica  amministrazione
    SPID, moduli fiscali, servizi comunali                         🛒 Commercio
                                                                     Acquisti online, banking, servizi di streaming

                   Escludere qualcuno dal web significa escluderlo dalla società.
                         (oltre ad essere uno svantaggio competitivo)




                                                    David Trevisan · UniUD                                                     6
Il quadro normativo

  🇮🇹 ITALIA                                           🇪🇺 UNIONE EUROPEA
 Legge Stanca                                        European Accessibility Act
 L. 4/2004                                           Direttiva 2019/882 · in vigore dal 28 giugno 2025
   Pubblica Amministrazione                            E-commerce e marketplace
   Aziende partecipate dallo Stato                     Servizi bancari e finanziari
   Imprese con fatturato > 500M€                       Streaming audio e video
                                                       Trasporti e telefonia




                                     David Trevisan · UniUD                                              7
Storia dell’accessibilità web

         1990                  1994               1999                  2004                     2008                  2025
          ADA                   W3C              WCAG 1.0           Legge Stanca                WCAG 2.0                EAA
   USA: diritti digitali   "Web universale"   Prime linee guida    Italia: PA obbligata   Standard internazionale   Privati inclusi




                                                     David Trevisan · UniUD                                                           8
Tecnologie assistive

 Screen Reader                                                    Ingranditori
 NVDA · JAWS · VoiceOver                                          Lente di Windows · Zoom macOS
   Legge il contenuto ad alta voce                                  Ingrandisce una porzione dello schermo
   Richiede HTML semantico, ruoli ARIA e testi alternativi          Richiede alto contrasto e layout responsive
   ( alt )

 Solo tastiera                                                    Controllo vocale
   Navigazione tramite Tab , frecce e scorciatoie                   Attiva pulsanti e link pronunciando il nome visibile
   Richiede il focus visibile, nell'ordine logico                   Richiede etichette visibili su tutti i controlli interattivi




                                                    David Trevisan · UniUD                                                         9
  WCAG




David Trevisan · UniUD   10
Livelli di conformità WCAG

       Livello A                  Livello AA             Livello AAA
  Senza questi il sito è     Spesso richiesto come       Non sempre
     inutilizzabile            standard minimo           obbligatorio




                                David Trevisan · UniUD                  11
1. Percepibile

  L’informazione deve essere percepita dai sensi dell’utente
Senza alt text                                            Contrasto insufficiente
<img src="grafico.png">
                                                          Testo 1.9:1
Con alt text                                              Contrasto sufficiente
<img src="grafico.png"
     alt="Vendite Q3: +15% rispetto a Q2">
                                                          Testo 8.6:1
                                                             Requisiti minimi WCAG 2.1 AA
                                                               4.5:1 testo normale
                                                                3:1 testo grande



                                             David Trevisan · UniUD                         12
2. Operabile

   L’interfaccia non può richiedere interazioni impossibili per l’utente
Non raggiungibile da tastiera                           Raggiungibile da tastiera
 <div class="button" onclick="submit()">                  <button>
   Invia                                                  Invia
 </div>                                                   </button>



Non accessibile con Tab .                                Tab   → focus visibile → Enter → azione.
  Prova: Cliccami con Tab + Enter                          Prova: Cliccami con Tab + Enter




                                           David Trevisan · UniUD                                   13
3. Comprensibile

   Informazioni e interfaccia devono essere comprensibili
Senza label                                                            Con label
 <input type="email"                                                     <label for="email">Email</label>
        placeholder="Email">                                             <input type="email" id="email"
                                                                         required placeholder="nome@dominio.it">



    Email
                                                                          Email    nome@dominio.it


Screen reader: “campo di testo, modifica” — senza contesto.            Screen reader: “Email, campo di testo obbligatorio”




                                                          David Trevisan · UniUD                                             14
4. Robusto

  Il contenuto deve funzionare con qualsiasi tecnologia assistiva
HTML non semantico                                                                  HTML semantico
<div class="header">...</div>                                                       <header>...</header>
<div class="nav">                                                                   <nav aria-label="Menu">
  <div onclick="go()">Home</div>                                                      <a href="/">Home</a>
</div>                                                                              </nav>
<div class="main">...</div>                                                         <main>...</main>




   header                          Lo screen reader non riconosce i ruoli e legge     header                  Lo screen reader riconosce i ruoli e li
   Home                            solo il testo: “header, selezionabile. home,       Home                    annuncia: “header, navigazione, main.” (il
   main                            selezionabile. main, selezionabile.”               main                    risultato esatto varia in base allo screen
                                                                                                              reader e browser scelto)


 Con HTML semantico lo screen reader riconosce automaticamente landmark, navigazione e contenuto principale:
 l’utente può spostarsi direttamente tra queste zone invece di leggere la pagina dall’alto.

                                                                    David Trevisan · UniUD                                                                 15
HTML semantico




   David Trevisan · UniUD   16
Elementi semantici

 <article>                                                    <section>
 Contenuto autonomo — un post, una card prodotto, un          Sezione tematica con titolo — raggruppa contenuti
 commento                                                     correlati dentro una pagina

 <figure> / <figcaption>                                      <details> / <summary>
 Immagine con didascalia associata — alt descrive             Accessibile da tastiera senza JavaScript
 l'immagine




                                                David Trevisan · UniUD                                            17
 <button> vs <a>

 <button type="submit">Invia</button>                          <a href="/contatti">Contattaci</a>
 <button type="button">Apri menu</button>                      <a href="/doc.pdf" download>Scarica PDF</a>



Azioni, toggle, apertura di pannelli                         Link a pagine, ancore o download

   Prova: Invia Contattaci — lo screen reader annuncia “pulsante” o “collegamento” in base al tag.




                                                David Trevisan · UniUD                                       18
     PARTE 2

Il workshop




 David Trevisan · UniUD   19
Demo screen reader




     David Trevisan · UniUD   20
Come usare uno Screen Reader?

 Windows — NVDA                                         macOS / iOS — VoiceOver
 Attiva / Esci              Insert + Q                  Attiva / Esci              Cmd + F5

 Naviga                     ↑ /↓                        Naviga                     VO + ←/→

 Titolo avanti / indietro   H / Shift+H                 Titolo avanti / indietro   VO + Cmd + H

 Elemento interattivo       Tab                         Elemento interattivo       Tab

 Lista elementi             Insert + F7                 Lista elementi             VO + U
                                                        VO = Ctrl+Option




                                          David Trevisan · UniUD                                  21
Demo — pagina non accessibile
<div>   al posto di <button> e <a> , nessun alt , nessuna <label> , contrasto basso, focus invisibile — provare con Tab e screen reader.




                                                                  David Trevisan · UniUD                                                   22
Demo — pagina accessibile
Stessa pagina con <button> , <a> , alt descrittivi, <label> associati, contrasto adeguato e focus visibile.




                                                                  David Trevisan · UniUD                      23
           PARTE 3

Confronto errori WCAG




       David Trevisan · UniUD   24
1. Alt text mancante
 WCAG 1.1.1 — contenuti non testuali
Ogni immagine deve avere un attributo alt che ne descriva il contenuto. Senza alt , lo screen reader legge il nome del file.
  Non accessibile                                                             Accessibile




 <img src="scarpe.jpg">                                                      <img src="scarpe.jpg"
                                                                               alt="Scarpa da corsa Nike Air Max,
                                                                                    colore bianco">




                                                            David Trevisan · UniUD                                             25
2. Contrasto insufficiente
 WCAG 1.4.3 — contrasto minimo
Il testo deve avere un rapporto di contrasto di almeno 4.5:1 (testo normale) o 3:1 (testo grande) rispetto allo sfondo.
  Contrasto 2.3:1                                                               Contrasto 8.6:1




                                                             David Trevisan · UniUD                                       26
3. Informazione solo tramite colore
 WCAG 1.4.1 — uso del colore
Il colore non deve essere l’unico mezzo per trasmettere informazioni.
  Solo pallino colorato                                                    Colore + testo




 <p>                                                                       <p>
   <span class="dot available"></span>                                       <span class="dot available"
   Nike Air Max                                                                    aria-hidden="true"></span>
 </p>                                                                        Nike Air Max —
                                                                             <strong class="available">
                                                                               Disponibile
                                                                             </strong>
                                                                           </p>




                                                            David Trevisan · UniUD                              27
4. Heading non semantici
 WCAG 1.3.1 — informazioni e relazioni
Usare <p><strong> per i titoli di sezione impedisce allo screen reader di costruire un indice dei titoli.
  p + strong                                                                     h3 semantico



 <p class="section-title">
   <strong>Iscriviti alla newsletter</strong>
 </p>


                                                                                 <h3>Iscriviti alla newsletter</h3>




                                                              David Trevisan · UniUD                                  28
5. Tabella senza intestazioni
 WCAG 1.3.1 — informazioni e relazioni
Le tabelle dati devono usare <th scope="col"> per le intestazioni e <caption> per il titolo. Senza questi, lo screen reader legge solo numeri
senza contesto.
  Solo td, no caption                                                         th + caption




 <table>                                                                     <p id="table-desc" class="visually-hidden">Tabella di conversione
   <tr>                                                                               taglie tra sistema europeo (EU), britannico (UK) e
     <td>EU</td><td>UK</td><td>CM</td>                                                centimetri (CM).</p>
   </tr>                                                                     <table aria-describedby="table-desc">
   <tr>                                                                        <caption>Guida taglie</caption>
     <td>40</td><td>6.5</td><td>25.5</td>                                      <thead>
   </tr>                                                                         <tr>
 </table>                                                                          <th scope="col">EU</th>
                                                                                   <th scope="col">UK</th>
                                                                                   <th scope="col">CM</th>
                                                                                 </tr>
                                                                               </thead>
                                                                               <tbody>
                                                                                 <tr><td>40</td><td>6.5</td>...




                                                            David Trevisan · UniUD                                                               29
6. Skip link assente
 WCAG 2.4.1 — salto dei blocchi
Un link “Vai al contenuto principale” permette agli utenti di tastiera e screen reader di saltare header e navigazione. Appare visivamente solo al
focus.
  Nessuno skip link                                                             Skip link presente




 <!-- Nessuno skip link -->                                                    <a href="#main-content" class="skip-link">
 <header>                                                                        Vai al contenuto principale
   <h1>Il mio negozio</h1>                                                     </a>
 </header>                                                                     <header>
 <nav>...</nav>                                                                  <h1>Il mio negozio</h1>
                                                                               </header>
                                                                               <nav aria-label="Menu principale">...




                                                             David Trevisan · UniUD                                                                  30
7. Focus order errato
 WCAG 2.4.3 — ordine del focus
Valori tabindex positivi forzano un ordine di navigazione imprevedibile. L’ordine del focus deve seguire l’ordine logico del DOM.
  tabindex positivi                                                            Ordine naturale del DOM




 <article class="product-card" tabindex="4">                                  <li>
   ...                                                                          <article class="product-card">
 </article>                                                                       ...
 <article class="product-card" tabindex="1">                                    </article>
   ...                                                                        </li>
 </article>

                                                                            L’ordine di focus segue l’ordine visivo della pagina.
L’utente con Tab salta al prodotto 2, poi 4, poi 3, poi 1.

                                                             David Trevisan · UniUD                                                 31
8. Link generici
 WCAG 2.4.4 — scopo del link
Il testo del link deve descrivere la destinazione. “Clicca qui” non ha significato fuori contesto — l’utente sente solo “clicca qui”.
  "clicca qui"                                                                     Link descrittivo


 <p>Per la nostra politica di reso                                                <p><a href="#">Consulta la nostra
    <a href="#">clicca qui</a>.</p>                                                  politica di reso</a></p>
 <p>Per le condizioni di vendita                                                  <p><a href="#">Leggi le condizioni
    <a href="#">clicca qui</a>.</p>                                                  di vendita</a></p>




                                                               David Trevisan · UniUD                                                   32
9. Label mancanti nei form
 WCAG 3.3.2 — etichette o istruzioni
Ogni campo deve avere un <label for="..."> associato. Il placeholder scompare durante la digitazione e non è letto da tutti gli screen reader
come etichetta.
  Solo placeholder                                                          Label + autocomplete



 <input type="text" placeholder="Nome">
 <input type="text" placeholder="Email">
 <div class="btn">Iscriviti</div>


                                                                           <label for="nome">Nome</label>
                                                                           <input type="text" id="nome"
                                                                             autocomplete="name" required>

                                                                           <label for="email-nl">Email</label>
                                                                           <input type="email" id="email-nl"
                                                                             autocomplete="email" required>

                                                                           <button>Iscriviti</button>




                                                          David Trevisan · UniUD                                                                33
10. Div al posto di button
 WCAG 4.1.2 — nome, ruolo, valore
Un <div> con onclick non è focusabile da tastiera, non ha ruolo “button” e non risponde a Enter / Space .
  div con classe .btn                                                       button nativo




 <div class="btn">Acquista</div>                                           <button aria-label="Acquista Nike Air Max">Acquista</button>



Non raggiungibile con Tab , non attivabile con Enter .                    Tab → focus → Enter → azione. Screen reader: “Acquista Nike Air
                                                                          Max, pulsante”.


                                                          David Trevisan · UniUD                                                            34
Risorse e approfondimenti
Demo prima / dopo
  W3C WAI — Before and After Demonstration · pagina e-commerce in versione
  inaccessibile e accessibile
  Accessible University — University of Washington · homepage universitaria in
  versione inaccessibile e accessibile
Risorse
  The A11y Project — Checklist · checklist pratica per verificare la conformità WCAG di
  una pagina




                                   David Trevisan · UniUD                                 35
         Grazie
         SLIDE E MATERIALE DELLA DEMO
Frontend/JS/AK_demo-seminario-accessibilita-web/




            David Trevisan · UniUD                 36
