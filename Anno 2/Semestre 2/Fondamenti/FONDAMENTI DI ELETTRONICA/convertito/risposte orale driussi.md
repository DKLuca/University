---
fonte: "risposte orale driussi.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

ANALOGICA
1- Perché c’è la necessità di variare la conducibilità del Si?
       La variazione della conducibilità del silicio è necessaria per realizzare dispositivi elettronici come diodi e transistor. Questo si
       ottiene attraverso il drogaggio, un processo in cui vengono introdotte impurità specifiche nel silicio per modificarne le proprietà
       elettriche. Il silicio puro (intrinseco) ha una conducibilità molto bassa, quindi non è adatto per applicazioni elettroniche.
       Con il drogaggio, si ottengono due tipi di silicio conduttivo:
       Silicio di tipo N (𝑆𝑖𝑛 ): contiene donatori (es. fosforo), che aggiungono elettroni liberi (cariche negative).
       Silicio di tipo P (𝑆𝑖𝑝 ): contiene accettori (es. boro), che creano lacune (cariche positive).
       Questa distinzione è fondamentale per la creazione di giunzioni PN, il principio di base per il funzionamento di diodi, BJT e
       MOSFET.
       Oltre ad ingegnerizzare la conducibilità del Si è anche possibile renderlo un isolante trasformandolo in biossido di silicio (𝑆𝑖𝑂2 )
       fondamentale ad esempio nei MOSFET per separare il gate dal canale.

2- Semiconduttori drogati: come funziona quali sono le caratteristiche elettriche finali che ne derivano. Che cos’è la condizione di
COMPLETA IONIZZAZIONE?
      I semiconduttori drogati sono composti da un elemento generalmente del IV gruppo della tavola periodica (Si) al quale viene
      aggiunto in concentrazioni variabili in base alle necessità un altro elemento appartenente al III o al V gruppo.
      Nel caso di un elemento del V gruppo si chiamerà drogante donore, esso infatti, avendo un elettrone in più (non impegnato in
      legami covalenti con gli altri atomi di Si), se sottoposto a condizioni di energia favorevoli tenderà a cedere tale elettrone
      liberando una carica libera negativa e assumendo carica fissa positiva.
      Nel caso di un elemento del III gruppo si chiamerà drogante accettore, esso, avendo solo 3 elettroni di valenza tenderà ad
      "assorbire" un elettrone libero in modo da completare i 4 legami covalenti richiesti dal Si, in questo modo verrà a crearsi un
      deficit di elettroni ed un surplus di lacune. In questo caso le lacune sono cariche positive libere mentre gli atomi di drogante, una
      volta assorbito un elettrone diventeranno cariche fisse negative.
      La completa ionizzazione si verifica quando tutti gli atomi di drogante hanno ceduto (nel caso dei donori) o catturato (nel caso
      degli accettori) elettroni, raggiungendo il massimo numero di portatori di carica liberi nel semiconduttore.
      Il verificarsi di questa condizione dipende dalla temperatura: a temperature sufficientemente alte (≈ 300 K, temperatura
      ambiente), l'energia termica è sufficiente per ionizzare quasi tutti gli atomi di drogante.
      A temperature molto basse, alcuni donori potrebbero non cedere il loro elettrone e alcuni accettori potrebbero non catturarlo,
      riducendo la concentrazione di portatori liberi.
      La completa ionizzazione è quindi lo stato in cui tutti gli atomi di drogante hanno formato i 4 legami covalenti richiesti dalla
      struttura cristallina del silicio e hanno generato il massimo numero possibile di portatori di carica.

3- Modello drift-diffusion.
      Il modello drift-diffusion ha lo scopo di descrivere il moto delle cariche all’interno di un semiconduttore. Esso descrive le due
      principali correnti di cariche libere che si verificano all’interno di un semi-conduttore soggetto ad un campo elettrico e ad una
      distribuzione di carica irregolare. La prima corrente, chiamata di DERIVA descrive il comportamento di elettroni e lacune nel
      momento in cui sul conduttore viene applicato un campo elettrico:

                                                       ⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗
                                                       Jn,drift = (−qn) ⋅ (−μn ⃗E) = qμn nE   ⃗
                                                          𝐽⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗           ⃗          ⃗
                                                             𝑝,drift = (𝑞𝑝) ⋅ (𝜇𝑝𝐸 ) = 𝑞𝜇𝑝 𝑝𝐸


       Queste sono le due equazioni che descrivono il moto di elettroni e lacune all’interno di un campo elettrico, 𝑛 e 𝑝 sono la
       concentrazione di elettroni e lacune, μ𝑛 e μ𝑝 sono coefficienti che rappresentano della mobilità delle cariche, μ𝑛 ≈ 2 ⋅ μ𝑝 . Nel
       caso degli elettroni, avendo carica negativa avranno il coefficiente che ne indica la mobilità con segno negativo. Sommando le
       due componenti da lacune ed elettroni si ottiene la corrente totale di deriva:
                                                        ⃗⃗⃗⃗⃗
                                                        Jtot = ⃗⃗⃗
                                                               Jn + ⃗⃗⃗
                                                                    Jp = q(μnn + μp p)E  ⃗

       La seconda corrente chiamata di diffusione deriva da differenze di concentrazione di carica all’interno del conduttore, questo
       squilibrio di carica andrà a creare correnti dalle zone in cui esse sono più concentrate verso le zone in cui esse sono meno
       concentrate. Immaginando quindi di avere un gradiente di concentrazione all’interno del conduttore questo comporterà un
       flusso di cariche nella direzione opposta al gradiente.
                                                                               𝑑𝑛         𝑑𝑛
                                                        𝐽⃗⃗⃗⃗⃗⃗⃗⃗⃗
                                                           𝑛,diff = (−𝑞)𝐷𝑛 (−     ) = 𝑞𝐷𝑛
                                                                               𝑑𝑥         𝑑𝑥
                                                                            𝑑𝑝           𝑑𝑝
                                                           ⃗⃗⃗⃗⃗⃗⃗⃗⃗
                                                           𝐽𝑝,diff = 𝑞𝐷𝑝 (− ) = −𝑞𝐷𝑝
                                                                            𝑑𝑥           𝑑𝑥

       𝐷𝑛 e 𝐷𝑝 sono coefficienti di diffusione di elettroni e lacune.
       Le correnti risultanti dal flusso di elettroni e di lacune hanno segno opposto dato che elettroni e lacune hanno carica opposta, il
       gradiente di concentrazione viene scelto negativo dato che esso indica la direzione di maggior pendenza della curva di
       concentrazione mentre le cariche si muovono nella direzione opposta (da concentrazione alta a concentrazione bassa).
       Sommando quindi le correnti date dal flusso di elettroni e lacune:

                                                    ⃗⃗⃗⃗⃗⃗⃗⃗
                                                    𝐽𝑛,tot = ⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗
                                                               𝐽𝑛,drift + ⃗⃗⃗⃗⃗⃗⃗⃗⃗
                                                                           𝐽𝑛,diff = 𝑞μ𝑛 𝑛𝐸⃗ + 𝑞𝐷𝑛 ∇𝑛
                                                    𝐽⃗⃗⃗⃗⃗⃗⃗⃗  ⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗ ⃗⃗⃗⃗⃗⃗⃗⃗⃗       ⃗
                                                       𝑝,tot = 𝐽𝑝,drift + 𝐽𝑝,diff = 𝑞μ𝑝𝑝𝐸 − 𝑞𝐷𝑝 ∇𝑝
                                           ⃗⃗⃗⃗⃗
                                           𝐽tot = ⃗⃗⃗⃗⃗⃗⃗⃗
                                                  𝐽𝑛,tot + ⃗⃗⃗⃗⃗⃗⃗⃗
                                                           𝐽𝑝,tot = 𝑞(μ𝑛 𝑛 + μ𝑝 𝑝)𝐸⃗ + 𝑞𝐷𝑛 ∇𝑛 − 𝑞𝐷𝑝 ∇𝑝

       Nel caso in cui si valutasse il modello drift-diffusion in Si drogato si può assumere che la conduzione avvenga solo tramite le
       cariche libere maggioritarie, di conseguenza, nel caso di 𝑆𝑖𝑛 si valuta solo la corrente di elettroni:
                                                           𝐽⃗⃗⃗⃗⃗   ⃗⃗⃗⃗⃗⃗⃗⃗      ⃗
                                                              tot ≈ 𝐽𝑛,tot = qμ𝑛 𝑛𝐸 + q𝐷𝑛 ∇𝑛
       Mentre nel caso di 𝑆𝑖𝑝 si valuta solo la corrente data dal flusso di lacune:
                                                         ⃗⃗⃗⃗⃗
                                                         𝐽tot ≈ ⃗⃗⃗⃗⃗⃗⃗⃗
                                                                𝐽𝑝,tot = qμ𝑝 𝑝𝐸⃗ − q𝐷𝑝 ∇𝑝

4- Giunzione PN e DIODI
       La giunzione PN è alla base del componente elettronico più semplice, cioè il diodo. La giunzione PN, come suggerisce il nome è
       formata da due porzioni di Si drogato adiacenti in modo che ci sia una superficie di interfaccia che permetta lo scambio di
       cariche. Una porzione sarà 𝑆𝑖𝑛 mentre l’altra 𝑆𝑖𝑝 , in questo modo all’interfaccia si verrà a creare un gradiente di concentrazione
       di cariche libere che causerà una corrente di diffusione; a questo punto le cariche libere non saranno più presenti per bilanciare
       la carica fissa, di conseguenza le due regioni di svuotamento risulteranno cariche, da notare però che il componente nella sua
       interezza rimane a carica neutra dato che non è stata né aggiunta né tolta carica. La regione di 𝑆𝑖𝑛 risulterà quindi carica
       positivamente mentre la regione di 𝑆𝑖𝑝 risulterà carica negativamente. La regione a ridosso dell’interfaccia, da cui le cariche si
       spostano si chiama regione di svuotamento ed ha una lunghezza che è funzione della concentrazione di drogante all’interno del
       Si:
                                                                 𝑞 𝑁𝐴 𝑥𝑝 = 𝑞 𝑁𝐷 𝑥𝑛
       So che l’uguaglianza è verificata dato che la carica che lascia una regione di Si dovrà necessariamente spostarsi nell’altra
       regione, di conseguenza più bassa sarà la concentrazione di drogante 𝑁𝑝 ed 𝑁𝑛 , più grandi saranno le regioni di svuotamento 𝑥𝑝
       ed 𝑥𝑛 .
       La carica fissa nella regione di svuotamento crea un campo elettrico che induce una corrente di deriva che andrà ad opporsi a
       quella di diffusione iniziale. Le due correnti raggiungeranno un equilibrio nel momento in cui I tot= 0, è un equilibrio dinamico dato
       che la corrente totale è uguale a zero ma 𝐼𝑑𝑖𝑓𝑓 = 𝐼𝑑𝑟𝑖𝑓𝑡 ≠ 0 .
       Per studiare il campo elettrico all’interno della zona di svuotamento si utilizza la
       legge di Gauss:
                             𝑑𝐸   ρ                    1
                                =ε       → 𝐸(𝑥) = ε ∫ ρ(𝑥) 𝑑𝑥
                             𝑑𝑥   𝑆𝑖                    𝑆𝑖
       La densità di carica ( ρ = 𝑞𝑁𝐴/𝐷 ) è costante all’interno della regione di
       svuotamento, di conseguenza il campo elettrico avrà andamento lineare.
       Il campo elettrico sarà massimo in corrispondenza della giunzione e avrà un
       valore 𝐸(0) che dipende dalla quantirà di carica fissa nella zona di svuotamento
       (➔drogaggio).
       Partendo dal campo elettrico è possibile calcolare il profilo di potenziale tramite
       l’equazione di Poisson in una dimensione:
                                         dϕ       dϕ
                                  E = − dx → d𝑥 = −𝐸(𝑥)
       ϕ𝑗 è il potenziale di barriera o di built-in e si oppone alla diffusione delle
       cariche, esso quindi è il responsabile del raggiungimento dell’equilibrio della
       giunzione.
                                                   𝑥𝑝 + 𝑥𝑛           𝑥𝑝 + 𝑥𝑛
                              Φ𝑗 = 𝐸(𝑥 = 0)                 = 𝑞𝑁𝐴 𝑥𝑝
                                                          2           2 ϵ𝑆𝑖
       Il potenziale di built-in è l’integrale del campo elettrico, di conseguenza, essendo E
       lineare equivale all’area del triangolo in verde.
       Partendo dalle equazioni totali delle correnti ottenute in precedenza:
                          𝐽⃗⃗⃗⃗⃗⃗⃗⃗   ⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗ ⃗⃗⃗⃗⃗⃗⃗⃗⃗     ⃗
                             𝑛,tot = 𝐽𝑛,drift + 𝐽𝑛,diff = 𝑞μ𝑛 𝑛𝐸 + 𝑞𝐷𝑛 ∇𝑛 = 0
                           𝐽⃗⃗⃗⃗⃗⃗⃗⃗  ⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗ ⃗⃗⃗⃗⃗⃗⃗⃗⃗     ⃗
                              𝑝,tot = 𝐽𝑝,drift + 𝐽𝑝,diff = 𝑞μ𝑝 𝑝𝐸 − 𝑞𝐷𝑝 ∇𝑝 = 0
       Essendo in condizioni di equilibrio anche le singole correnti di elettroni e di lacune ( 𝐽𝑛,𝑡𝑜𝑡 𝑒 𝐽𝑝,𝑡𝑜𝑡 ) sono nulle, di conseguenza,
       risolvendo le equazioni differenziali ottengo:
                                                                                     𝑞Φ
                                                          𝑝(Φ) = 𝑝(0) ⋅ exp (−            )
                                                                                    𝑘𝐵 𝑇
                                     𝑛2
       Con: 𝑝(0) = 𝑁𝐴 ; 𝑝(Φ𝑗 ) = 𝑁𝑖 .
                                      𝐷
       Ricavando ϕ𝑗 :
                                                                                𝑁𝐴 𝑁𝐷
                                                                Φ𝑗 = 𝑉𝑡ℎ ln (         )
                                                                                 𝑛𝑖2
                   𝑘𝐵 𝑇
       Con 𝑉𝑡h =        come descritto da relazione di Einstein.
                    𝑞


       Nel momento in cui applico una tensione esterna al diodo il sistema va fuori equilibrio ed una corrente può scorrere nel
       dispositivo: nel momento in cui applico una tensione 𝑉𝐷 < 0 la differenza di potenziale tra la zona Sip e Sin aumenta, di
       conseguenza aumenta anche il campo elettrico che a sua volta mi porterà ad avere una zona di svuotamento più larga. Questa
       tensione 𝑉𝐷 < 0 incentiva la corrente di deriva rispetto alla diffusione che vede una barriera di potenziale più alta rispetto alle
       condizioni di equilibrio → 𝐼𝑑𝑟𝑖𝑓𝑡 > 𝐼𝑑𝑖𝑓𝑓 . La corrente di deriva però è dovuta ai portatori minoritari, di conseguenza anch’essa è
       molto piccola, addirittura trascurabile. Questa condizione è detta POLARIZZAZIONE INVERSA (→diodo OFF).
       Se la tensione applicata è 𝑉𝐷 > 0 la differenza di potenziale e il potenziale di barriera tra le zone di Si drogato diminuiranno, di
       conseguenza anche il campo elettrico dovuto alle cariche fisse diminuirà, questo mi porta ad avere una zona di svuotamento più
       stretta. Il campo elettrico diminuendo porta ad una consequenziale diminuzione della corrente di deriva rendendola trascurabile
       nei confronti della corrente di diffusione che, aiutata dal minor salto di potenziale tra le due zone sarà di gran lunga più potente
       dato che in questo caso sarà dovuta alle cariche maggioritarie. Questa condizione è chiamata POLARIZZAZIONE DIRETTA
       (→diodo ON) ed è la condizione in cui il diodo risulta più conduttivo.

       La corrente nel diodo è descritta dalla legge:
                                                                   𝑉𝐷                        𝑉𝐷
                                             𝐼𝐷 = 𝐴 ⋅ 𝐽𝑆 ⋅ [exp (      ) − 1] = 𝐼𝑆 ⋅ [exp (      ) − 1]
                                                                  𝑛𝑉𝑡ℎ                      𝑛𝑉𝑡ℎ
       Dove 𝐴 è l’area della giunzione, 𝐽𝑠 è la densità di corrente di saturazione ed 𝑛 è un fattore di non idealità (1.0 − 1.1) che spesso
       viene tralasciato.
       Questo modello verifica i casi visti in precedenza:
          •     𝑉𝐷 = 0 → 𝐼𝐷 = 0
          •     𝑉𝐷 < 0 → 𝐼𝐷 ≈ −𝐼𝑆 (trascurabile)
          •     𝑉𝐷 > 0 → 𝐼𝐷 > 0

       Il diodo è un elemento che fa passare corrente solo in un verso, è di conseguenza un interruttore pilotato in tensione. La corrente
       ha dipendenza esponenziale dalla tensione.
       Con tensioni negative possiamo considerare il diodo spento e la sua corrente trascurabile, purché 𝑉𝐷 > 𝑉𝑏k . Nel momento in
       cui 𝑉𝐷 scende al di sotto di 𝑉𝑏𝑘 il diodo comincia a condurre anche in inversa. 𝑉𝑏𝑘 può essere più o meno elevata, questo
       dipende dalla quantità di drogaggio del Si; se il silicio è poco drogato inoltre avrò un breakdown distruttivo, mentre se il silicio è
       molto drogato si può verificare l’effetto Zener che è alla base degli omonimi diodi.


5- Modelli per i diodi: esponenziale, grafico, di Newton, iterativo, a soglia
      Nel diodo ideale la caratteristica è a squadra, nel diodo reale però la corrente ha andamento esponenziale rispetto alla tensione.
      La natura esponenziale e, di conseguenza, non lineare del grafico V-I del diodo rende difficile o spesso addirittura impossibile la
      risoluzione analitica di sistemi di reti elettriche con essi al loro interno, per questo esistono medodi alternativi come quello
      grafico, di Newton oppure iterativo.
          Il metodo grafico consiste nel disegnare la retta di carico del circuito che sarà ovviamente in funzione dei valori di corrente e
      tensione del diodo, successivamente, disegnando l’andamento esponenziale del diodo si individua il punto di incidenza tra la
      retta e la curva, questo sarà il punto di lavoro del circuito.
          Il metodo di Newton si basa sull’omonimo metodo di ricerca ricorsiva delle radici di funzioni. Partendo sempre dalle equazioni
      della rete utilizzando la formula:
                                                                                 𝑓(𝑉𝐷𝑖 )
                                                                𝑉𝐷𝑖+1 = 𝑉𝐷𝑖 − ′
                                                                                 𝑓 (𝑉𝐷𝑖 )
      Questo metodo tende a convergere lentamente, non è quindi pratico da utilizzare se non per un calcolatore o un simulatore.
           Il metodo iterativo prevede di partire con una soluzione di tentativo e procedere,
       utilizzando il modello esponenziale e la retta di carico, proiettando alternativamente
       sulle due curve. Questo metodo tende a convergere molto velocemente.
       Fare attenzione ad utilizzare l’equazione del diodo in forma logaritmica altrimenti il
       metodo non converge.

       Spesso il modello esponenziale complica molto la soluzione dei circuiti, posso
       approssimare linarmente il modello esponenziale definendo una 𝑉γ chiamata
       tensione di soglia oltre la quale il diodo va in conduzione. Questo modello risulterà
       quindi lineare a tratti formato da due semirette:
            •      Diodo OFF: 𝐼𝐷 = 0 per 𝑉𝐷 < 𝑉γ
            •      Diodo ON: 𝑉𝐷 = 𝑉γ per 𝐼𝐷 > 0
       Per utilizzare questo metodo è necessario fare un’ipotesi iniziale delle
       condizioni di conduzione del diodo, successivamente questa ipotesi
       dovrà essere verificata. Se la soluzione non è consistente con il
       funzionamento del diodo l’ipotesi iniziale era sbagliata → devo
       cambiare ipotesi iniziale.




6- Applicazioni dei diodi
       Raddrizzatore a semionda singola:
       Tramite un singolo diodo in serie ad un generatore di tensione alternata 𝑉𝑖𝑛 e ad un resistore
       è possibile rendere un’onda a valor medio nullo in una a valore medio non nullo, di fatto
       “cancellando” le porzioni d’onda che impongono una
       tensione 𝑉𝑖𝑛 < 𝑉γ .
       La criticità principale di questo circuito è che la semionda
       negativa non viene utilizzata.

       È inoltre possibile, inserendo un condensatore in parallelo al
       resistore aggiungere un’azione filtrante che rallenta la caduta
       di tensione sul fronte discendente dell’onda. Il condensatore
       fornirà corrente al carico quando D è off.




       Raddrizzatore a doppia semionda:
       Questo tipo di raddrizzatore, utilizzando 4 diodi anziché uno è in grado di
       sfruttare anche la semionda negativa.
       A differenza di quello a semionda singola in questo caso in ogni
       semiperiodo ci sono sempre due diodi in serie, di conseguenza per poter
       mandare in conduzione entrambi avrò bisogno di una 𝑉𝑖𝑛 > 2𝑉γ .
La tensione sulla resistenza di conseguenza sarà sempre positiva ed il valor
medio della forma d’onda gfenerata è doppio rispetto a quello del raddrizzatore a
semionda singola.
Anche in questo caso è possibile inserire un condensatore in parallelo al
resistore per rallentare la caduta di tensione tra un picco d’onda e il successivo.




Rivelatore di picco:
Se 𝑉𝑖 − 𝑉𝑜 < 𝑉γ il diodo è OFF.
Se 𝑉𝑖 − 𝑉𝑜 > 𝑉γ il diodo è ON, il
condensatore si carica e si porta al limite
𝑉𝑀 − 𝑉γ; successivamente 𝑉𝑜 rimane a
𝑉𝑀 − 𝑉γ perché il diodo è OFF e
impedisce a 𝐶 di scaricarsi.




Clamper negativo (positivo):
Rende a valor medio negativo un segnale a valor medio nullo, cioè lo trasla verso il
basso di un valore 𝑉γ − 𝑉𝑀 .
Se 𝑉𝑖 − 𝑉𝑐 < 𝑉γ il diodo è OFF → 𝑉𝑜 = 𝑉𝑖 − 𝑉𝑐
Se 𝑉𝑖 − 𝑉𝑐 > 𝑉γ il diodo è ON → 𝑉𝑜 = 𝑉γ, 𝐶 si carica a 𝑉𝑐 = 𝑉𝑀 − 𝑉γ
Quando 𝑉𝑖 cala non vale più l’ipotesi ON, il diodo impedisce alla corrente di
invertirsi e 𝐶 resta carico.
A questo punto 𝑉𝑜 segue 𝑉𝑖 traslata di 𝑉γ − 𝑉𝑀

Invertendo il verso del diodo si ottiene un clamper positivo, esso traslerà verso l’alto il segnale di
un valore 𝑉𝑀 − 𝑉γ




Duplicatore di tensione:
È la cascata di un clamper positivo e di un rivelatore di picco:
il primo condensatore trasla la sinusoide fino ad un valore massimo
di 2𝑉𝑀 − 𝑉γ e successivamente il rivelatore di picco la blocca a quel
valore.




Regolatore di tensione:
Utilizza uno zener in breakdown per scaricare a terra nel momento in cui la
tensione supera il valore desiderato.
      𝑅𝐿
𝑉𝑖          > 𝑉𝑍 → il diodo è ON in breakdown e scarica a terra.
     𝑅+𝑅𝐿
7- Effetti reattivi nella giunzione pn e derivazione delle formule
        Il caso di polarizzazione diretta e quello di polarizzazione inversa, visti dal punto di vista delle cariche sono molto diversi, nel
        primo caso ci saranno molte cariche libere in movimento, mentre nel secondo ci sarà molta carica spaziale data dalle cariche
        fisse. Per questo motivo saranno necessari due modelli diversi per rappresentare gli effetti reattivi nel caso di polarizzazione
        diretta e nel caso di polarizzazione inversa.
        POLARIZZAZIONE INVERSA (capacità di giunzione):
        Carica nella zona di svuotamento: 𝑄𝑛 = 𝑞𝑁𝐷 𝑥𝑛 𝐴            (1)

       Bilanciamento delle cariche (+) e (−) nella zona di svuotamento:
                                                              𝑁
                                𝑁𝐷 𝑥𝑛 = 𝑁𝐴 𝑥𝑝 → 𝑥𝑝 = 𝑁𝐷 𝑥𝑛                   (2)
                                                                  𝐴



       Larghezza della zona di svuotamento, sostituendo la (2):
                                                        𝑁                                𝑁
            𝑊dep = 𝑥𝑛 + 𝑥𝑝      → 𝑊𝑑𝑒𝑝 = 𝑥𝑛 + 𝑥𝑛 𝑁𝐷 → 𝑥𝑛 = 𝑊𝑑𝑒𝑝 𝑁 +𝑁
                                                                   𝐴
                                                                                                     (3)
                                                          𝐴                              𝐴   𝐷



       Partendo dalla (1), sostituisco la (3):
                                                  𝑁𝐷 𝑁𝐴
                                       𝑄𝑛 = 𝑞            𝐴𝑊dep
                                                 𝑁𝐷 + 𝑁𝐴

       Sapendo che:
                                                                         2εSi 1 1
                                                       𝑊dep = √              ( + ) (Φ𝑗 − 𝑉𝐷 )
                                                                          𝑞 𝑁𝐴 𝑁𝐷
       Ottengo la funzione non lineare 𝑄𝑛 = 𝑓(𝑉𝐷 ) .
       Derivando si giunge alla capacità differenziale:
                                                                             𝑑𝑄𝑛             1
                                                                      𝐶𝑗 =       = 𝐶𝑗0
                                                                             𝑑𝑉𝐷
                                                                                              𝑉
                                                                                         √1 − Φ𝐷
                                                                                                 𝑗

       POLARIZZAZIONE DIRETTA (capacità di diffusione):
       La carica libera che passa attraverso la giunzione è la principale responsabile degli effetti reattivi → dipendono dal livello di
       corrente:
       Sia τ𝑇 il tempo di transito attraverso la giunzione:
                                                                    𝑄𝐷 = 𝐼𝐷 τ𝑇
       La corrente calcolata con il modello esponenziale del diodo:
                                                                                𝑉𝐷
                                                                𝐼𝐷 ≅ 𝐼𝑆 ⋅ exp ( )
                                                                               𝑉𝑡ℎ
       Quindi ottengo una funzione non lineare che mi porterà ad avere anche in questo caso una capacità differenziale:
                                                                                   𝑉𝐷
                                                         𝑄𝐷 = 𝑓(𝑉𝐷 ) = 𝐼𝑆 ⋅ exp ( ) ⋅ τ𝑇
                                                                                   𝑉𝑡ℎ
       Derivando rispetto a 𝑉𝐷 :
                                                        𝑑𝑄𝐷        𝑑𝐼𝐷 τ𝑇 𝐼𝑆           𝑉𝐷     τ𝑇 𝐼𝐷
                                                 𝐶𝐷 =       = τ𝑇       =       ⋅ exp ( ) =
                                                        𝑑𝑉𝐷        𝑑𝑉𝐷     𝑉𝑡ℎ         𝑉𝑡ℎ     𝑉𝑡ℎ




8- Cosa rappresentano i parametri: Cj, Cjo (effetti reattivi giunzione pn)
       I parametri 𝐶𝑗 e 𝐶𝑗0 rappresentano le capacità di giunzione dovute al moto di deriva delle cariche quando la giunzione è in regione
       di polarizzazione inversa, 𝐶𝑗 è funzione di 𝑉𝐷 ed è la capacità di giunzione nel momento in cui viene applicata una tensione 𝑉𝐷
       che manda il diodo in inversione. 𝐶𝑗0 è la capacità di giunzione a vuoto, misurata quindi quando la 𝑉𝐷 = 0 .
9- Effetto valvola
        L’effetto valvola nel BJT è la proprietà che permette a tale componente di pilotare tramite la tensione 𝑉𝐵𝐸 la corrente 𝐼𝐶 .
        Questo fenomeno si verifica sotto determinate condizioni:
                 -     Giunzione B-E in diretta, così da avere elettroni che diffondono dall’emettitore verso la base
                 -     Giunzione B-C in inversa, così da avere un forte campo elettrico tra collettore e base
                 -     Una base molto stretta
        Essendo B-E polarizzata direttamente verrà indotta una corrente 𝐼𝐸 molto elevata
        che porterà un gran numero di elettroni da E verso B, B-C al contrario, è
        polarizzata inversamente quindi sarà presente un forte campo elettrico ai capi
        della giunzione B-C, questo campo elettrico catturerà gli elettroni iniettati in B da
        E tirandoli verso C e causando appunto una corrente 𝐼𝐶 . In un transistor ideale
        tutti gli elettroni iniettati da E raggiungono C. Nel transistor reale invece c’è una
        piccola parte di elettroni provenienti da E e di lacune provenienti da B che si
        ricombinano tra loro, questo causa una corrente 𝐼𝐵 > 0 ed una 𝐼𝐶 < 𝐼𝐸 .


10- Modello di Ebers-Moll nel BJT
      Modello utilizzato per definire le correnti nel BJT. Le giunzioni vengono viste come due diodi, la corrente di collettore è
      proporzionale a quella di emettitore:
                                                                      𝐼𝐶 = α𝐹 𝐼𝐸
      Le correnti nelle giunzioni seguono le leggi dei diodi:
                                                            𝑣                                  𝑣
                                            𝐼𝐹 = 𝐼𝐸𝑆 [exp ( 𝑉𝐵𝐸) − 1]          𝐼𝑅 = 𝐼𝐶𝑆 [exp ( 𝑉𝐵𝐶) − 1]
                                                                𝑇                                  𝑇
       Modello di Ebers-Moll a 4 parametri:
                                                                       𝑣𝐵𝐸                        𝑣𝐵𝐶
                                        𝐼𝐸 = 𝐼𝐹 − α𝑅 𝐼𝑅 = 𝐼𝐸𝑆 [exp (       ) − 1] − α𝑅 𝐼𝐶𝑆 [exp (     ) − 1]
                                                                       𝑉𝑇                         𝑉𝑇
                                                                          𝑣𝐵𝐸                     𝑣𝐵𝐶
                                        𝐼𝐶 = α𝐹 𝐼𝐹 − 𝐼𝑅 = α𝐹 𝐼𝐸𝑆 [exp (       ) − 1] − 𝐼𝐶𝑆 [exp (     ) − 1]
                                                                          𝑉𝑇                      𝑉𝑇
       Dove i 4 parametri sono:
           -     𝐼𝐸𝑆 : corrente inversa di saturazione della giunzione B-E
           -     𝐼𝐶𝑆 : corrente inversa di saturazione della giunzione B-C
           -     α𝐹
           -     α𝑅


                               𝐼𝐵 = 𝐼𝐸 − 𝐼𝐶




       Nel modello generale:
       𝐼𝐸 = 𝑓(𝑉𝐵𝐸 , 𝑉𝐵𝐶 )
       𝐼𝐶 = 𝑓(𝑉𝐵𝐸 , 𝑉𝐵𝐶 )

       Restringendo il modello alla sola regione normale posso supporre 𝐼𝑅 = 0, con questa supposizione sto dicendo che 𝐼𝐶 è causata
       solamente dagli elettroni provenienti da E, non ho quindi lacune che diffondono dalla B verso C → 𝐼𝐸 = 𝐼𝐹 ed 𝐼𝐶 = α𝐹 𝐼𝐹
       → 𝐼𝐸 = 𝑓(𝑉𝐵𝐸 ) 𝐼𝐶 = 𝑓(𝑉𝐵𝐸 ) .
       Nel caso di regione normale le correnti di collettore ed emettitore dipenderanno solo da 𝑉𝐵𝐸 .


                               In regione normale, dove quindi B-E è in diretta e B-C è in inversa (𝑉𝐵𝐸 > 0, 𝑉𝐶𝐵 > 0) :
                               la corrente 𝐼𝐶 dipende solamente dalla tensione sulla giunzione B-E, essa inoltre cresce
                               esponenzialmente rispetto a tale tensione.
                                       In regione di saturazione, dove quindi entrambe le giunzioni B-E e B-C sono in diretta
                                       (𝑉𝐵𝐸 > 0, 𝑉𝐶𝐵 < 0) la corrente dipende anche da 𝑉𝐵𝐶 :
                                       notare come la corrente 𝐼𝐶 dipenda dalla tensione 𝑉𝐶𝐵 solo quando essa è negativa
                                       (condizione di saturazione), nel momento in cui 𝑉𝐶𝐵 diventa positiva si passa alle
                                       condizioni di regione normale in cui la 𝐼𝐶 dipende solo da 𝑉𝐵𝐸 .




Modello di Ebers-Moll a 3 parametri:
Il modello di Ebers-Moll può essere semplificato in modo da ottenere solo 3
parametri.

Viene definita una condizione di reciprocità:

                                α𝐹 𝐼𝐸𝑆 = α𝑅 𝐼𝐶𝑆 = 𝐼𝑆
Posso affermare questo perché sono entrambe correnti inverse di saturazione di
giunzioni uguali, quindi finché la struttura del BJT rimane simmetrica la
semplificazione rimane valida.

Così è possibile consolidare i parametri α𝐹 e α𝑅 in un unico parametro 𝐼𝑆 :
                                                           𝑉𝐵𝐸                        𝑉𝐵𝐶                    𝑉𝐵𝐸           𝑉𝐵𝐶
   𝐼𝑡 = β𝐹 𝐼𝐵𝐸 − β𝑅 𝐼𝐵𝐶 = α𝐹 𝐼𝐹 − α𝑅 𝐼𝑅 = α𝐹 𝐼𝐸𝑆 [exp (        ) − 1] − α𝑅 𝐼𝐶𝑆 [exp (     ) − 1] = 𝐼𝑆 [exp (     ) − exp (     )]
                                                           𝑉𝑡ℎ                        𝑉𝑡ℎ                    𝑉𝑡ℎ           𝑉𝑡ℎ
Inoltre, basandosi sul circuito qui a fianco:

                                  𝐼𝐸 = 𝐼𝐵𝐸 + 𝐼𝑡 = 𝐼𝐵𝐸 + β𝐹 𝐼𝐵𝐸 − β𝑅 𝐼𝐵𝐶 = 𝐼𝐵𝐸 (1 + β𝐹 ) − β𝑅 𝐼𝐵𝐶
Tornando al modello a 4 parametri, definiamo:
                                                               α                   β
                                                       β𝐹 = 1−α𝐹 → α𝐹 = 1+β𝐹
                                                                    𝐹                   𝐹
                                                               α𝑅                  β𝑅
                                                       β𝑅 =             → α𝑅 =
                                                              1−α𝑅               1+β𝑅
Quindi:
                                 β𝑅
     𝐼𝐸 = 𝐼𝐹 − α𝑅 𝐼𝑅 = 𝐼𝐹 −          𝐼
                               1 + β𝑅 𝑅
              1 + β𝐹     β𝑅
          =          𝐼 −     𝐼
              1 + β𝐹 𝐹 1 + β𝑅 𝑅
                          𝐼𝐹          𝐼𝑅
          = (1 + β𝐹 )          − β𝑅
                        1 + β𝑓      1 + β𝑅

Eguagliando le espressioni di 𝐼𝐸 ottenute dai due modelli:
                                                                                𝐼𝐹          𝐼𝑅
                                      (1 + β𝐹 )𝐼𝐵𝐸 − β𝑅 𝐼𝐵𝐶 = (1 + β𝐹 )              − β𝑅
                                                                              1 + β𝑓      1 + β𝑅
Ottengo che:
                                                              𝐼𝐹                       𝐼𝑅
                                                   𝐼𝐵𝐸 =                   𝐼𝐵𝐶 =
                                                           1+𝛽𝑓                    1+β𝑅




Sostituendo nel modello a 4 parametri:

                                                    𝐼𝐸 = (1 + β𝐹 )𝐼𝐵𝐸 − β𝑅 𝐼𝐵𝐶
Seguendo lo stesso procedimento per 𝐼𝐶 si ottiene:

                                                    𝐼𝐶 = β𝐹 𝐼𝐵𝐸 − (1 + β𝑅 )𝐼𝐵𝐶
11- Effetto Early



       Abbiamo precedentemente notato come, nel BJT ideale in regione normale, la 𝐼𝐶
       dipenda solamente da 𝑉𝐵𝐸 , non da 𝑉𝐶𝐵 .




       L’effetto Early introduce una non idealtà che provoca una
       lieve dipendenza lineare di 𝐼𝐶 da 𝑉𝐶𝐸 .
       L’effetto Early può essere descritto utilizzando un’unico
       parametro 𝑉𝐴 .




       Origine effetto Early:
       Sfruttando le concentrazioni di portatori per le giunzioni all’equiilibrio:
       nella base, 𝑛 dipende dal portenziale:

                       𝑛𝑖2       𝑉𝐵𝐸
       𝑛(𝑥 = 0) =          exp (     )
                       𝑁𝐴        𝑉𝑡ℎ
                      𝑛𝑖2       𝑉𝐵𝐶
       𝑛(𝑥 = 𝑊𝐵 ) =       exp (     )
                      𝑁𝐴        𝑉𝑡ℎ
       Dove 𝑉𝐵𝐸 e 𝑉𝐵𝐶 sono i valori che assume 𝑉(𝑥) agli estremi.
       Studio della corrente di saturazione 𝐼𝑡 che è definita come:
                                                   𝑑𝑛
                                     𝐼𝑡 = −𝑞𝐴𝐷𝑛
                                                   𝑑𝑥
       Dove:

             •      𝑞 : carica dell’elettrone
             •      𝐴 : area della giunzione
             •      𝐷𝑛 : coefficiente di diffusione degli elettroni
             𝑑𝑛
       Con 𝑑𝑥 gradiente di concentrazione dei portatori di carica attraverso la base:

                                 𝑑𝑛   1    𝑛𝑖2    𝑉𝐵𝐶    𝑛𝑖2       𝑉𝐵𝐸       𝑛𝑖2           𝑉𝐵𝐶           𝑉𝐵𝐸
                                    =   ⋅ [ 𝑒𝑥𝑝 (     )−     𝑒𝑥𝑝 (     )] =       ⋅ [𝑒𝑥𝑝 (     ) − 𝑒𝑥𝑝 (     )]
                                 𝑑𝑥 𝑊𝐵 𝑁𝐴         𝑉𝑡ℎ    𝑁𝐴        𝑉𝑡ℎ      𝑊𝐵 𝑁𝐴          𝑉𝑡ℎ           𝑉𝑡ℎ


       Quindi:
                                                                   𝑛𝑖2         𝑉𝐵𝐸           𝑉𝐵𝐶
                                                      𝐼𝑡 = 𝑞𝐴𝐷𝑛         [exp (     ) − exp (     )]
                                                                  𝑊𝐵 𝑁𝐴        𝑉𝑡ℎ           𝑉𝑡ℎ
       Da questo, considerando l’espressione di 𝐼𝑡 ottenuta nel modello a tre parametri, segue che:

                                                                                   𝑛𝑖2
                                                                      𝐼𝑆 = 𝑞𝐴𝐷𝑛
                                                                                  𝑊𝐵 𝑁𝐴

       Dalla formula di 𝐼𝑆 appena ottenuta si può dedurre che la corrente di saturazione del BJT dipende dalla larghezza della base, più
       essa è stretta, più la corrente di saturazione è alta.
        Tornando all’effetto Early, tenendo in considerazione i risultati appena
        ottenuti nello studio della corrente di saturazione: l’aumento della
        tensione 𝑉𝐶𝐵 allarga la regione svuotata della giunzione BC, questo causa
        il restringimento della base. Dato che la corrente di saturazione è
        inversamente proporzionale alla larghezza di base essa tenderà ad
        aumentare.




        Per aggiungere l’effetto Early nel modello di Ebers-Moll si tiene
        conto di risultati sperimentali che dimostrano la dipendenza
        lineare di 𝐼𝐶 da 𝑉𝐶𝐵 in regione lineare; inoltre gli andamenti di 𝐼𝐶
        variando 𝑉𝐵𝐸 hanno un’unica intercetta sull’asse 𝑥
        corrispondente alla tensione −𝑉𝐴 , essa verrà chiamata
        tensione di Early.
                                        𝑉𝐵𝐸         𝑉𝐶𝐵
                          𝐼𝐶 = 𝐼𝑆 exp (     ) (1 +       )
                                        𝑉𝑡ℎ          𝑉𝐴
        Di solito 𝑉𝐶𝐵 ≫ 𝑉𝐵𝐸 → 𝑉𝐶𝐸 = 𝑉𝐶𝐵 − 𝑉𝐵𝐸 ≈ 𝑉𝐶𝐵 :
                       𝑉          𝑉
        IC ≈ 𝐼𝑆 exp ( 𝑉𝐵𝐸) (1 + 𝑉𝐶𝐸 ) la parte in blu corrisponde ad 𝐼𝐶 calcolata con 𝑉𝐶𝐵 = 0
                           𝑡ℎ         𝐴


        Considerando anche l’effetto Early in regione normale le correnti sono ancora proporzionali? No, se cresce 𝑉𝐶𝐵 , aumenta 𝐼𝐶 ma
        non 𝐼𝐵 . Per mantenere la proporzionalità devo fissare la tensione 𝑉𝐶𝐵 , questo mi porterà ad avere un coefficiente di
        proporzionalità che è funzione di 𝑉𝐶𝐵 : definiamo quindi β𝐹0 come il guadagno di corrente a 𝑉𝐶𝐵 = 0. Se non tengo conto
        dell’effetto Early posso scrivere 𝐼𝐶 = β𝐹0 𝐼𝐵 , altrimenti dovrò calcolare:
                                                                         𝑉                          𝑉
                                                       β𝐹 = β𝐹0 (1 + 𝑉𝐶𝐵) → 𝐼𝐶 = 𝐼𝐵 β𝐹0 (1 + 𝑉𝐶𝐵 )
                                                                             𝐴                          𝐴


        Per limitare l’effetto Early posso aumentare la concentrazione di drogante nella base, così facendo riduco la 𝑊𝑑𝑒𝑝 .



12- Tutti gli effetti di non idealità nel BJT (Effetto Early, Cjo)
        L’effetto Early è stato spiegato in dettaglio nella domanda precedente.

        Per quando riguarda gli effetti reattivi, il BJT è composto da due giunzioni PN affiancate. Se consideriamo di essere in regione
        normale una delle due giunzioni (BC) sarà in inversa e l’altra (BE) in diretta. Si possono quindi utilizzare le formule ricavate in
        precedenza per i diodi.
        Per la giunzione CB in polarizzazione inversa calcolo la capacità di giunzione dovuta alla carica spaziale:
                                                                        𝑑𝑄𝑛                1
                                                               𝐶𝐵𝐶 =         = 𝐶𝑗0 ⋅
                                                                        𝑑𝑉𝐶𝐵
                                                                                            𝑉
                                                                                       √1 − ϕ𝐶𝐵
                                                                                               𝑗


        Per la giunzione BE in polarizzazione diretta calcolo la capacità di diffusione dovuta alla carica mobile dentro la base:
                                                                                  𝑑𝑄𝐵
                                                                          𝐶𝐵𝐶 =
                                                                                  𝑑𝑉𝐵𝐸
        Con:

                                                                     𝑊𝐵 𝑛𝑖2        𝑉𝐵𝐸           𝑉𝐵𝐶
                                                         𝑄𝐵 = 𝑞𝐴            [exp (     ) − exp (     )]
                                                                     2𝑁𝐴           𝑉𝑡ℎ           𝑉𝑡ℎ
                                                                      𝑛𝑖2         𝑉𝐵𝐸           𝑉𝐵𝐶
                                                        𝐼𝑡 = 𝑞𝐴𝐷𝑛          [exp (     ) − exp (     )]
                                                                     𝑊𝐵 𝑁𝐴        𝑉𝑡ℎ           𝑉𝑡ℎ
     Definisco τ𝐹 come il tempo di transito in base:

                                                            𝑊2      𝑊2
                                                  τ𝐹 = 2𝐷𝐵 = 2𝑉 𝐵μ         → 𝑄𝐵 = τ𝐹 𝐼𝑡
                                                             𝑛      𝑡ℎ 𝑛

     Di conseguenza:
                                                       𝑑𝑄𝐵          𝑑𝐼𝑡   τ𝐹 𝐼𝑡         τ𝐹 𝐼𝐶
                                               𝐶𝐵𝐸 =        = τ𝐹 ⋅      ≈       ⇒ CBE =
                                                       𝑑𝑉𝐵𝐸        𝑑𝑉𝐵𝐸   𝑉𝑡ℎ            𝑉𝑡ℎ
     Perché posso supporre che 𝐼𝑡 ≈ 𝐼𝐶 in regione normale.


13- MOS

     Il MOS ha una struttura simile a quella di un condensatore
     dotato però di anodo e catodo composti da diversi
     materiali. I due materiali utilizzati nel MOS sono un
     metallo ed un semiconduttore separati da un isolante.
     Ogni materiale ha intrinsecamente una funzione di lavoro
     che rappresenta la quantità di energia necessaria per
     “staccare” un elettrone da un atomo. Per motivi che
     tralascio nel momento in cui vengono affiancati due
     materiali con funzioni di lavoro diverse si crea una differenza di potenziale. Conseguenza del fenomeno appena riportato è che
     nel MOS, senza applicare nessuna tensione esterna 𝑉𝑔 tra bulk e gate, verrà a crearsi una differenza di potenziale 𝑉0
     (condensatore carico anche “a vuoto”), per azzerare questo gradiente sarà necessario imprimere una tensione 𝑉𝑔 = −𝑉0 = 𝑉𝑓𝑏
     opposta alla tensione del MOS (in modo da annullare la tensione tra i due piatti → condensatore scarico).

     Il valore di questa 𝑉𝐹𝐵 dipende dai materiali e dalle concentrazioni di drogaggio del Si, in generale però:
           •     p-Si → 𝑉𝑓𝑏 < 0
           •     n-Si → 𝑉𝑓𝑏 > 0

     Lo studio che segue è stato fatto ponendo lo zero del potenziale in
     profondità nel substrato di p-Si. Variando la tensione 𝑉𝑔 applicata modifico
     la carica sulle facce del “condensatore” e, di conseguenza, modifico il
     profilo di potenziale che viene a crearsi all’interno del MOS.
     Definita la carica come:
                                  q = −𝐶𝑜𝑥 ⋅ (𝑉𝑔 − 𝑉𝑓𝑏 )

     ottenuta tramite leggi del condensatore.

     𝑽𝒈 = 𝟎:
     La tensione ai capi del condensatore è:
                               𝑉𝑔 − 𝑉𝑓𝑏 = −𝑉𝑓𝑏 = 𝑉0
     il profilo di potenziale sarà quindi più alto nel gate (metallo).
     Per quanto riguarda la carica:
                  q = 𝑉𝑓𝑏 ⋅ 𝐶𝑜𝑥 → q < 0 (essendo p-Si 𝑉𝑓𝑏 < 0)
     la carica negativa sarà evidentemente causata da un accumulo di
     elettroni all’interfaccia p-Si ↔ Ox .

     𝑽𝒈 = 𝑽𝒇𝒃 :
     La tensione ai capi del consensatore è:
                                    𝑉𝑔 − 𝑉𝑓𝑏 = 0
     il profilo di potenziale sarà di conseguenza piatto.
     Per quanto riguarda la carica: q = 0 .
𝑽𝒈 < 𝑽𝒇𝒃 ACCUMULAZIONE:
La tensione ai capi del condensatore è:
                                                𝑉𝑔 − 𝑉𝑓𝑏 < 0
il profilo di potenziale sarà quindi più alto nel substrato.
Per quanto riguarda la carica:
                                     q = −𝐶𝑜𝑥 ⋅ (𝑉𝑔 − 𝑉𝑓𝑏 ) → q > 0

la carica positiva è causata da un accumulo di lacune all’interfaccia p-Si ↔ Ox .
Questa regione di funzionamento è detta accumulazione.

𝑽𝒈 > 𝑽𝒇𝒃 SVUOTAMENTO (𝑽𝒈 < 𝑽𝑻 ):
La carica ai capi del condensatore è:
                                                𝑉𝑔 − 𝑉𝑓𝑏 > 0
il profilo di potenziale sarà quindi più alto nel gate (metallo).
Per quanto riguarda la carica:
                                          q = 𝑉𝑓𝑏 ⋅ 𝐶𝑜𝑥 → q < 0
All’interfaccia p-Si ↔ Ox verrà quindi a crearsi carica negativa (n cresce, p cala).
La carica negativa sopracitata sarà dovuta in parte alla carica mobile (di inversione, dato che siamo nel p-Si):
                                                               ρinv = −𝑞𝑛
ed in parte alla carica fissa:
                                                            ρ𝐷 = 𝑞(𝑝 − 𝑁𝐴− )
Per 𝑉𝑔 minore di una certa 𝑉𝑇 che definiremo poi, posso assumere che vicino all’interfaccia p-Si ↔ Ox non esista carica mobile,
di conseguenza ρ𝐷 ≫ ρ𝑖𝑛𝑣 (le lacune del p-Si presenti all’interfaccia hanno ricombinato con un elettrone ma la 𝑉𝑔 non è
abbastanza alta per fare in modo di portare ulteriori elettroni che non avrebbero modo di ricombinare).
Questa regione di funzionamento in cui l’interfaccia viene svuotata dalle lacune è detta appunto regione di svuotamento.


𝑽𝒈 ≫ 𝑽𝒇𝒃 INVERSIONE (𝑽𝒈 > 𝑽𝑻):
Aumentando ulteriormente 𝑉𝑔 , la carica negativa mobile che nel caso dello svuotamento avevamo trascurato, diventa
significativa. Arriverò ad un punto in cui la concentrazione di elettroni sarà molto superiore a quella delle lacune, proprio come
se il substrato (normalmente p-Si) all’interfaccia fosse n-Si, per questo si chiama regione di inversione.
Analizzando le concentrazioni di cariche all’interfaccia (𝑧 = 0 è fissato sull’interfaccia p-Si ↔ Ox):
                                                          ψ                                         ψ
                             𝑛𝑠 = 𝑛(𝑧 = 0) = 𝑛0 exp (𝑉 𝑠 )           𝑝𝑠 = 𝑝(𝑧 = 0) = 𝑝0 exp (− 𝑉 𝑠 )
                                                           𝑡ℎ                                        𝑡ℎ
                                                 𝑛2
Dato che stiamo parlando di p-Si so che 𝑛0 = 𝑁𝑖 mentre 𝑝0 = 𝑁𝐴 .
                                                  𝐴


Per definizione il passaggio all’inversione si ottiene quando la concentrazione di elettroni all’interfaccia diventa uguale o
maggiore al valore del doping nel substrato (𝑛𝑆 = 𝑁𝐴 ), la tensione che è necessario imprimere per raggiungere questa
condizione è chiamata 𝑉𝑇 (tensione di soglia).
Al fine di calcolare la tensione di soglia del mosfet c’è bisogno di
analizzare i contributi che i diversi strati danno quando messi nelle
condizioni di inversione.
Iniziamo con l’individuare il valore del potenziale all’interfaccia p-Si ↔ Ox:
                    𝑛2       𝜓                            𝑁
       𝑛𝑠 = 𝑁𝐴 = 𝑁𝑖 exp (𝑉 𝑠 )      → ψ𝑠 = 2 ⋅ 𝑉𝑡ℎ 𝑙𝑛 ( 𝑛𝐴) = 2ψ𝐹
                     𝐴       𝑡ℎ                               𝑖
dove ψ𝐹 è una quantità che dipende solo da parametri tecnologici.

Procedendo con il calcolo di 𝑉𝑇 passiamo a calcolare 𝑉𝑂𝑥 , per fare ciò è necessario fare una valutazione della carica sulle
armature e del campo elettrico all’interno dell’ossido quando 𝑉𝑔 > 𝑉𝑓𝑏 .
Siano 𝑄𝑀 = − 𝑄𝑆 le cariche per unità d’area nel metallo e nel semiconduttore (stesso valore ma segno opposto essendo facce
del condensatore).
La carica nel semiconduttore è scomponibile in componente dovuta alla carica fissa e componente dovuta alla carica mobile:
                                                         𝑄𝑆 = 𝑄𝐷 + 𝑄𝑖𝑛𝑣
     Passiamo al flusso del campo elettrico interno all’ossido partendo dalla legge di Gauss:
                                                                            𝑄𝑀     𝑄𝑆
                                                                   𝐹𝑂𝑥 =        =−
                                                                            ε𝑂𝑥    ε𝑂𝑥
                                                                                                                                      ε
     Ora, ricordando la legge generale dei condensatori 𝑄 = 𝐶𝑉 e quella particolare del condensatore a facce piane 𝐶 = 𝑑 posso
     scrivere che:
                                        ε                   ε𝑂𝑥                      𝑄       𝑉     𝑉𝐺 −𝑉𝑓𝑏 −ψ𝑆       𝑄
                                 𝑄𝑀 = 𝑇𝑂𝑥 ⋅ 𝑉𝑂𝑥 con               = 𝐶𝑂𝑥 → 𝐹𝑂𝑥 = ε 𝑀 = 𝑇𝑂𝑥 =                      = −ε 𝑆
                                         𝑂𝑥                 𝑇𝑂𝑥                       𝑂𝑥     𝑂𝑥        𝑇𝑂𝑥           𝑂𝑥
     Da cui:
                                                            𝑄               𝑸
                                  𝑽𝑮 − 𝑽𝒇𝒃 − 𝛙𝑺 = − ε 𝑆 𝑇𝑂𝑋 = − 𝑪 𝑺               → 𝑄𝑆 = −𝐶𝑂𝑋 (𝑉𝐺 − 𝑉𝑓𝑏 − ψ𝑆 )
                                                            𝑂𝑋               𝑶𝑿



     Ora, partendo dalla densità di carica fissa: ρ𝐷 = 𝑞(𝑝 − 𝑁𝐴− ) che può essere semplificata se supponiamo, essendo in
     svuotamento, che non ci siano lacune non ricombinate ρ𝐷 = −𝑞𝑁𝐴− , posso calcolare la carica fissa nel semiconduttore:

                                     𝑄𝐷 = −𝑞𝑁𝐴−𝑊𝐷
     per farlo ho integrato la densità di carica su tutta la regione di
     svuotamento, supponendo ρ𝐷 costante al suo interno e nulla al suo
     esterno.
     Utilizzando la stessa formula precedentemente utlizzata per calcolare il
     flusso nell’ossido calcolo il flusso nel substrato. Suppongo 𝑄𝑆 ≈ 𝑄𝐷 dato
     che in svuotamento 𝑄𝐷 ≫ 𝑄𝑖𝑛𝑣 (condizione non valida in inversione ma è
     comunque ragionevole utilizzarla dato che avrò inversione soltalto
     all’interfaccia, la maggior parte del substrato rimane comunque in
     svuotamento):
                                                   𝑄    𝑄         𝑞𝑁𝐴− 𝑊𝐷
                                                                                            Quella che nelle formule è z, nell'immagine è x
             -   Interfaccia: 𝐹(𝑧 = 0+) = − ε 𝑆 ≈ − ε 𝐷 =
                                                   𝑆𝑖    𝑆𝑖         ε𝑆𝑖
                                       𝑞𝑁 −
             -   reg. svuot.: 𝐹(𝑧) ≈ ε 𝐴 ⋅ z
                                        𝑆𝑖
     Integrando su 𝑧 l’espressione del flusso nella regione di svuotamento trovo il potenziale:
                                                                  𝑞𝑁 −                     2ε ψ
                                                        ψ𝑆 = 2ε 𝐴 𝑊𝐷2 → 𝑊𝐷 = √ 𝑞𝑁
                                                                                𝑆𝑖 𝑆
                                                                                  −
                                                                    𝑆𝑖                       𝐴

     Da cui, utlizzando la formula di 𝑄𝐷 precedente:
                                         𝑄𝑆 ≈ 𝑄𝐷 = −𝑞𝑁𝐴− 𝑊𝐷 = −√2𝑞𝑁𝐴− ε𝑆𝑖 ψ𝑆 = −γ𝐶𝑂𝑥 √2ψ𝐹
                 √2𝑞𝑁𝐴− ε𝑆𝑖
     Con γ =                così da semplificare
                   𝐶𝑂𝑥

                                                                     𝑄𝑆          𝑄𝑆    γ𝐶𝑂𝑥 √2ψ𝐹
                                    𝑉𝑂𝑥 = 𝑉𝐺 − 𝑉𝐹𝐵 − ψ𝑆 = −              𝑇𝑂𝑋 = −     =           = γ√2ψ𝐹
                                                                     ε𝑂𝑋         𝐶𝑂𝑋      𝐶𝑂𝑋
     Ora, sommo le componenti di 𝑉𝑇 ottenute:

                                                   𝑉𝑇 = 𝑉𝑓𝑏 + ψ𝑆 + 𝑉𝑂𝑥 = 𝑉𝑓𝑏 + 2ψ𝐹 + γ√2ψ𝐹


14- MOSFET
     Il MOSFET è un tipo di transistore, il suo nome è l’acronimo di Metal-Oxide-Semiconductor Field-Effect-Transistor.

     Alla base di questo componente c’è il MOS, un sandwich di Metallo-Ossido-Semiconduttore, al quale vengono aggiunti due
     terminali con drogaggio opposto rispetto a quello del substrato chiamati source e drain. Sotto determinate condizioni si verrà a
     creare un canale conduttivo nel substrato che separa source e drain il
     quale permetterà il passaggio della corrente 𝐼𝐷𝑆 .
     Questa struttura implica la creazione di due giunzioni PN tra source/drain
     e gate, esse non dovranno mai essere mandate in diretta, altrimenti si
     ottiene un BJT.
     Ora studiamo più approfonditamente l’n-MOSFET, tenendo presente che
     nel caso di p-MOSFET le conclusioni sono molto simili, solo opposte.
     L’n-MOSFET sarà composto da un substrato di p-Si mentre source e drain
     saranno di n-Si, per rispettare la condizione di obbligatoria inversione
     delle giunzioni PN sarà necessario mantenere 𝑉𝑆𝐵 , 𝑉𝐷𝐵 ≥ 0.
     Tipicamente si pone 𝑉𝐵 = 𝑉𝑆 = 0 in modo da utilizzare soltanto 𝑉𝐷 per
     controllare la corrente attraverso il transistor (𝑉𝐷𝐵 ≥ 0, 𝑉𝐷𝑆 ≥ 0).
       Detto questo, andiamo a studiare come il componente MOS all’interno del MOSFET andrà ad influenzarne il funzionamento.

       MOSfet in accumulazione 𝑽𝑮𝑺 (= 𝑽𝑮𝑩 ) ≤ 𝑽𝒇𝒃 :
       giunzione S-B all’equilibrio, mentre giunzione D-B in inversa → 𝐼𝐷𝑆 = 0 indipendentemente dalla tensione 𝑉𝐷𝑆 → MOSFET OFF

       MOSfet in svuotamento 𝑽𝒇𝒃 < 𝑽𝑮𝑺 < 𝑽𝑻 :
       la tensione di gate svuota dalle lacune il substrato p-Si, la regione di svuotamento si estende a tutto il silicio che sta tra source e
       drain → nella regione di svuotamento non c’è carica libera → regione di svuotamento non conduce
       → 𝐼𝐷𝑆 = 0 indipendentemente da 𝑉𝐷𝑆 → MOSFET OFF

       MOSfet in inversione 𝑽𝑮𝑺 > 𝑽𝑻 :
       la tensione di gate è sufficientemente alta per invertire il Si, questo crea uno strato di elettroni liberi all’interfaccia → creazione
       del CANALE CONDUTTIVO di n-Si tra source e drain → source e drain, non avendo più giunzioni che li separano, saranno
       collegati eletticamente → 𝐼𝐷𝑆 > 0 dato che 𝑉𝐷𝑆 > 0→ MOSFET ON
       Maggiore è la tensione 𝑉𝐺𝑆 , maggiore è il numero di elettroni all’interfaccia, il canale è più conduttivo, e, a parità di 𝑉𝐷𝑆 la
       corrente 𝐼𝐷𝑆 aumenta.
       La corrente 𝐼𝐷𝑆 che scorre tra drain e source è quindi funzione della 𝑉𝐺𝑆 applicata sul terminale di gate, questo mi porta ad avere
       l’effetto valvola anche nel MOSFET.

       Questi sono i casi di funzionamento nel caso dell’n-MOSFET, il quale avrà quindi source e gate di n-Si, substrato di p-Si e canale
       conduttivo formato da elettroni.
       Nel caso del p-MOSFET sarà tutto invertito, avrò quindi source e gate di p-Si, substrato di n-Si e canale conduttivo formato da
       lacune.


15- Effetto Body
        Fino ad ora avevamo studiato il MOSFET utilizzando le condizioni di funzionamento così come le avevamo calcolate prendendo
        in analisi soltanto il MOS. Questa è una semplificazione lecita al netto che le giunzioni S-B e D-B siano in equilibrio, in questo
        modo esse non hanno effetti sulla carica interna al substrato. È per questo che precedentemente era stata posta 𝑉𝑆𝐵 = 0 .
        Se 𝑉𝑆𝐵 > 0 la giunzione S-B andrà fuori equilibrio, di conseguenza la carica interna al substrato sarà funzione anche di 𝑉𝑆 , idem
        per la giunzione 𝑉𝐷𝐵 e 𝑉𝐷 .
        È possibile dimostrare, utilizzando modelli dei semiconduttori in condizioni di disequilibrio, che:
                                                                 ψ𝑆 = 2ψ𝐹 + 𝑉𝑆𝐵
       di conseguenza all’aumentare di 𝑉𝑆𝐵 aumenterà anche ψ𝑆 cioè la caduta di potenziale nel semiconduttore.
       Con questa nuova formula di ψ𝑆 andiamo a ricalcolare la carica fissa 𝑄𝐷 e la larghezza della regione di svuotamento 𝑊𝐷

                                                                                                       2ε𝑆𝑖 (2ψ𝐹 +𝑉𝑆𝐵 )
                                 𝑄𝐷 = −γ𝐶𝑂𝑋 √ψ𝑆 = −γ𝐶𝑂𝑋 √2ψ𝐹 + 𝑉𝑆𝐵                           𝑊𝐷 = √
                                                                                                            𝑞𝑁𝐴

       Questo influenza la tensione di soglia:

       𝑉𝐺𝐵,𝑇 = 𝑉𝑓𝑏 + 2ψ𝐹 + 𝑉𝑆𝐵 + γ√2ψ𝐹 + 𝑉𝑆𝐵 = 𝑉𝑇0 − γ√2ψ𝐹 + 𝑉𝑆𝐵 + γ√2ψ𝐹 + 𝑉𝑆𝐵

                                          ➔ 𝑉𝐺𝐵,𝑇 − 𝑉𝑆𝐵 = 𝑉𝑇0 + 𝛾(√2𝜓𝐹 + 𝑉𝑆𝐵 − √2𝜓𝐹 ) = 𝑉𝐺𝑆,𝑇

       Quindi, la tensione di soglia se teniamo conto anche dell’effetto body risulterà:

                                  𝑉𝑇 = 𝑉𝑇0 + 𝛾(√2𝜓𝐹 + 𝑉𝑆𝐵 − √2𝜓𝐹 ) oppure 𝑉𝑇 = 𝑉𝑓𝑏 + 2ψ𝐹 + γ√2ψ𝐹 + 𝑉𝑆𝐵
       La γ ottenuta ora avrà ovviamente formula diversa rispetto a quella ottenuta nello studio senza effetto body, in questo caso γ
       sarà chiamata fattore di effetto body (0.3 ÷ 0.5 √𝑉).
       Ricapitolando, l’effetto body:
            -    aumenta la caduta nel semiconduttore 𝜓𝑆 = 2𝜓𝐹 + 𝑉𝑆𝐵
            -    aumenta la carica di svuotamento e la regione di svuotamento
            -    aumenta la tensione di soglia     𝑉𝑇 = 𝑉𝑇0 + 𝛾(√2𝜓𝐹 + 𝑉𝑆𝐵 − √2𝜓𝐹 )
16- Modelli delle correnti nel MOSFET
       Supponendo di essere in condizione di MOSFET ON (presenza di canale di inversione), c’è bisogno di un modello che permetta di
       calcolare la corrente che passa tra source e drain in funzione delle tensioni applicate sui terminali di controllo del transistor.
       Utilizzando la formula ottenuta in precedenza del potenziale all’interfaccia
       influenzato dalle giunzioni in disequilibrio è possibile notare che, ipotizzando sempre
       𝑉𝐵 = 0:
       se 𝑽𝑺 = 𝑽𝑫 : ψS ≈ 2 ⋅ ψF + VSB = 2 ⋅ ψF + VS = 2 ⋅ ψF + VD → ψ𝑆 è costante
       su tutta la larghezza L del substrato
       se 𝑽𝑺 ≠ 𝑽𝑫 : ψ𝑆 sarà funzione di 𝑥 dato che la 𝑉𝑆𝐵 ≠ 𝑉𝐷𝐵
                                      ψ𝑆 (𝑥 = 0) = 2 ⋅ ψF + VSB
                                      ψ𝑆 (𝑥 = 𝐿) = 2 ⋅ ψF + VDB
       Quindi posso scrivere, ponendo l’origine dell’asse 𝑥 all’interfaccia S-B
                                       ψ𝑆 = 2ψ𝐹 + 𝑉𝑆𝐵 + 𝑉(𝑥)
       Dove 𝑉(𝑥 = 0) = 0 e 𝑉(𝑥 = 𝐿) = 𝑉𝐷𝑆


       Ora, appurato che la differenza di potenziale all’interfaccia ψ𝑆 è funzione della posizione 𝑥 mi ricavo la 𝑄𝑖𝑛𝑣 a partire dalla
       formula già utlizzata in precedenza utilizzando la nuova equazione di ψ𝑆 :
                                                                                𝑄𝑖𝑛𝑣 + 𝑄𝐷
                                                         𝑉𝐺𝐵 − 𝑉𝑓𝑏 − ψ𝑆 = −
                                                                                   𝐶𝑂𝑥
       con 𝑄𝐷 ≈ −γ𝐶𝑂𝑥 √2ψ𝐹 + 𝑉𝑆𝐵 e ψS = 2ψ𝐹 + 𝑉𝑆𝐵 + 𝑉(𝑥)
                                               𝑄𝑖𝑛𝑣 + 𝑄𝐷
       𝑉𝐺𝐵 − 𝑉𝑓𝑏 − 2ψ𝐹 − 𝑉𝑆𝐵 − 𝑉(𝑥) = −
                                                  𝐶𝑂𝑥
                                        𝑄     𝑄                                                𝑄
       → 𝑉𝐺𝑆 = 𝑉𝑓𝑏 + 2ψ𝐹 + 𝑉(𝑥) − 𝐶 𝐷 − 𝐶𝑖𝑛𝑣 = 𝑉𝑓𝑏 + 2ψ𝐹 + 𝑉(𝑥) + γ√2γ𝐹 + 𝑉𝑆𝐵 − 𝐶𝑖𝑛𝑣
                                         𝑂𝑥       𝑂𝑥                                               𝑂𝑥

                          𝑄
       →𝑉𝐺𝑆 = 𝑉𝑇 + 𝑉(𝑥) − 𝐶𝑖𝑛𝑣
                            𝑂𝑥


                                                        → 𝑄𝑖𝑛𝑣 (𝑥) = −𝐶𝑂𝑥 [𝑉𝐺𝑆 − 𝑉𝑇 − 𝑉(𝑥)]
       Dall’equazione della carica libera appena ottenuta si capisce che, se 𝑉𝑆 < 𝑉𝐷 → 𝑉(𝑥) ≥ 0 → la carica si riduce man mano
       che mi avvicino al drain → canale meno conduttivo.
       In generale 𝐽 = − 𝑄(𝑥) ⋅ 𝑣(𝑥) dove 𝐽 è la corrente per unità di larghezza, 𝑄 la carica per unità d’area e la velocità degli
                                        𝑑𝑉
       elettroni 𝑣(𝑥) = −μ𝑛 𝐸𝑥 = μ𝑛 𝑑𝑥 , quindi:
                                                  𝐼
                                               𝐷𝑆
                                         𝐽𝐷𝑆 = 𝑊  = −𝑄𝑖𝑛𝑣 (𝑥) ⋅ 𝑣(𝑥) → 𝐼𝐷𝑆 = −𝑄𝑖𝑛𝑣 (𝑥) ⋅ 𝑣(𝑥) ⋅ 𝑊
                                                                                             𝑑𝑉
                                                        → 𝐼𝐷𝑆 = 𝑊μ𝑛 𝐶𝑂𝑥 [𝑉𝐺𝑆 − 𝑉𝑇 − 𝑉(𝑥)] ⋅ 𝑑𝑥

       Ora, pongo β𝑛 ’ = μ𝑛 𝐶𝑂𝑥 come parametro della conducibilità intrinseca del MOSFET (indipendente da dimensione) ed integro
       entrambi i membri in modo da eliminare la derivata:
         𝐿                   𝐿                                        𝑉𝐷𝑆
                                                       𝑑𝑉
       ∫ 𝐼𝐷𝑆 𝑑𝑥 = 𝑊β′𝑛 ∫ [𝑉𝐺𝑆 − 𝑉𝑇 − 𝑉(𝑥)]                𝑑𝑥 = 𝑊β′𝑛 ∫ [𝑉𝐺𝑆 − 𝑉𝑇 − 𝑉(𝑥)]𝑑𝑉
        0                   0                          𝑑𝑥            0

                                                                      β′                    2 ]
                                                       → 𝐼𝐷𝑆 ⋅ 𝐿 = 𝑊 2𝑛 [2(𝑉𝐺𝑆 − 𝑉𝑇 )𝑉𝐷𝑆 − 𝑉𝐷𝑆

                                                                 𝑊   β′                    2 ]
                                                        → 𝐼𝐷𝑆 = 𝐿 ⋅ 2𝑛 [2(𝑉𝐺𝑆 − 𝑉𝑇 )𝑉𝐷𝑆 − 𝑉𝐷𝑆
                   𝑊
       pongo 𝑆 = 𝐿 come fattore di forma del MOSFET e β𝑛 = β𝑛 ’ ⋅ 𝑆 come parametro della conducibilità del MOSFET
       dipendente dalle dimensioni ed ottengo:
                                                                                       𝟏 𝟐
                                                          𝑰𝑫𝑺 = 𝛃𝒏 [(𝑽𝑮𝑺 − 𝑽𝑻 )𝑽𝑫𝑺 −    𝑽 ]
                                                                                       𝟐 𝑫𝑺
      Studiando l’equazione di 𝐼𝐷𝑆 in funzione di 𝑉𝐷𝑆 mantendo costante 𝑉𝐺𝑆 è possibile
      notare come essa assuma un andamento parabolico con il massimo che coincide
      con il valore 𝑉𝐷𝑆 = 𝑉𝐺𝑆 − 𝑉𝑇 .
      Cosa succede su questo punto di massimo?

      𝑄𝑖𝑛𝑣 (𝐿) = −𝐶𝑂𝑥 [𝑉𝐺𝑆 − 𝑉𝑇 − 𝑉𝐷𝑆 ] = −𝐶𝑂𝑥 [𝑉𝐺𝑆 − 𝑉𝑇 − 𝑉GS + VT ] = 0
      In fondo al canale sono alla soglia dell’inversione, per 𝑉𝐷𝑆 > 𝑉𝐺𝑆 − 𝑉𝑇 il modello
      farebbe addirittura cambiare segno alla carica di inversione, il che non è possibile
      dato che stiamo sempre parlando di elettroni, il modello non è più corretto.
      Restringo quindi la validità del modello ricavato in precedenza alla regione
      𝑉𝐷𝑆 ≤ 𝑉𝐺𝑆 − 𝑉𝑇 che verrà chiamata regione TRIODO o LINEARE

      Modifichiamo ora il modello precedente in modo che valga nella regione
      𝑉𝐷𝑆 > 𝑉𝐺𝑆 − 𝑉𝑇 , questa regione verrà chiamata di SATURAZIONE. In questa regione il canale si “strozza” nei pressi del drain
      (PINCH OFF del canale), in questa zona rimane pochissima carica libera che causa alta resistività e alte cadute di potenziale,
      verrà così a generarsi un campo 𝐸𝑥 (𝑥 = 𝐿) molto grande con conseguente 𝑣(𝑥 = 𝐿) molto alta.
      In questa regione i modelli matematici si complicano notevolmente ma qualitativamente è possibile notare una dipendenza
      della 𝐼𝐷𝑆 da 𝑉𝐷𝑆 molto più debole, di conseguenza la corrente 𝐼𝐷𝑆 per 𝑉𝐷𝑆 > 𝑉𝐺𝑆 − 𝑉𝑇 cresce molto più lentamente rispetto alla
      regione triodo. Viene definita 𝑉𝐷 𝑆𝑎𝑡 = 𝑉𝐺𝑆 − 𝑉𝑇 tensione di saturazione del MOSFET.
      Proprio perché nella regione di saturazione la dipendenza di 𝐼𝐷𝑆 rispetto a 𝑉𝐷𝑆 è molto più debole, per adattare il modello
      precedente semplicemente prolungo le condizioni che ho su 𝑉𝐷 𝑆𝑎𝑡 a tutta la regione di saturazione, partendo quindi dal modello
      valido in regione triodo pongo 𝑉𝐷𝑆 = 𝑉𝐺𝑆 − 𝑉𝑇 :
                                                                        1 2       𝛃𝒏
                                           𝑰𝑫𝑺 = β𝑛 [(𝑉𝐺𝑆 − 𝑉𝑇 )𝑉𝐷𝑆 − 𝑉𝐷𝑆     ]=     (𝑽 − 𝑽𝑻 )𝟐
                                                                        2         𝟐 𝑮𝑺
      Per ottenere il modello precedente in regione di saturazione abbiamo attuato una semplificazione abbastanza brutale ed
      abbiamo ottenuto un modello in cui la 𝐼𝐷𝑆 è totalmente indipendente dalla 𝑉𝐷𝑆 , tuttavia, sperimentalmente è possibile notare
      un modesto aumento lineare di 𝐼𝐷𝑆 con 𝑉𝐷𝑆 , per questo, basandosi su dati empirici, il modello viene spesso corretto
      aggiungendo un fattore λ di modulazione della lunghezza di canale:
                                                             𝛃𝒏
                                                     𝑰𝑫𝑺 =      (𝑽𝑮𝑺 − 𝑽𝑻 )𝟐 (𝟏 + 𝛌𝐕𝐃𝐒 )
                                                             𝟐
      I modelli nelle varie regioni di funzionamento devono incontrarsi nei punti di transizione, di conseguenza devo
      correggere anche il modello per la regione triodo:
                                                                            𝟏
                                              𝑰𝑫𝑺 = 𝛃𝒏 [(𝑽𝑮𝑺 − 𝑽𝑻 )𝑽𝑫𝑺 − 𝑽𝟐𝑫𝑺 ] (𝟏 + 𝝀𝑽𝑫𝑺 )
                                                                            𝟐

17- Modello delle capacità nel MOSFET

     Il fatto che il MOSFET sia basato sul condensatore MOS rende scontata la presenza di effetti reattivi nella struttura.
     𝑄𝑖𝑛𝑣 e 𝑄𝐷 dipendono da 𝑉𝐺𝑆 , 𝑉𝐷𝑆 e 𝑉𝑆𝐵 in maniera non lineare, di conseguenza le capacità che descrivono gli effetti
     reattivi nel MOSFET dipendono dal punto di lavoro, quindi non sono costanti.
     Esamineremo gli effetti reattivi intrinseci del MOSFET, legati quindi al fatto che nella struttura è presente un
     condensatore MOS, essi saranno dovuti alla carica indotta nel substrato dal terminale di gate, ma esamineremo anche
     gli effetti reattivi parassiti legati alle non idealità della struttura e agli effetti di bordo.
     Ora procediamo analizzando gli effetti reattivi intrinseci nelle varie regioni di funzionamento:
     - Regione TRIODO:
          n-MOSFET ON, 𝑉𝐷𝑆 piccola perché non ho pinch off del canale → 𝑉𝐷𝑆 ≪ 𝑉𝐺𝑆 − 𝑉𝑇
          La carica è data dalla formula definita in precedenza:
                                                       𝑄𝑖𝑛𝑣 (𝑥) = −𝐶𝑂𝑥 [𝑉𝐺𝑆 − 𝑉𝑇 − 𝑉(𝑥)]
          Essendo 𝑉𝐷𝑆 molto più piccola di 𝑉𝐺𝑆 − 𝑉𝑇 posso approssimare dicendo che il canale n ha carica uniforme tra drain
          e source, di conseguenza posso considerare anche la resistività dello strato invertito costante, questo mi causa una
          caduta di potenziale lineare tra source e drain:
                                                                                  𝑥
                                                                    𝑉(𝑥) = 𝑉𝐷𝑆 ⋅
                                                                                  𝐿
          Per trovare la carica totale di canale integro la carica di inversione su tutta la lunghezza L del canale e moltiplico per
          la larghezza W:
                       𝐿
         |𝑄𝐶𝐻 | = 𝑊 ∫0 𝐶𝑂𝑋 [𝑉𝐺𝑆 − 𝑉𝑇 − 𝑉(𝑥)] 𝑑𝑥
                                         𝑉
               = 𝑊𝐿𝐶𝑂𝑋 (𝑉𝐺𝑆 − 𝑉𝑇 − 𝐷𝑆 ) pongo 𝑉𝐷𝑆 = 𝑉𝐷𝐺 + 𝑉𝐺𝑆
                                   2
                                         𝑉     𝑉
               = 𝑊𝐿𝐶𝑂𝑋 (𝑉𝐺𝑆 − 𝑉𝑇 − 𝐷𝐺 − 𝐺𝑆 )
                                   2    2
                            𝑉     𝑉
               = 𝑊𝐿𝐶𝑂𝑋 ( 𝐺𝑆 + 𝐺𝐷 − 𝑉𝑇 )
                         2    2
   Ottengo una carica di canale dipendente da 𝑉𝐺𝑆 e da 𝑉𝐺𝐷 dalla quale posso ricavare le capacità differenziali tra i
   terminali G-S e G-D:
                                                      ∂|𝑄𝐶𝐻 | 1
                                              𝐶𝐺𝑆𝐶 =          = 𝑊𝐿𝐶𝑂𝑋
                                                        ∂𝑉𝐺𝑆     2
                                                              ∂|𝑄𝐶𝐻 | 1
                                                     𝐶𝐺𝐷𝐶 =          = 𝑊𝐿𝐶𝑂𝑋
                                                               ∂𝑉𝐺𝐷   2
- Regione SATURAZIONE:
   n-MOSFET ON, 𝑉𝐷𝑆 > 𝑉𝐺𝑆 − 𝑉𝑇 , c’è pinch off del canale.
   Il canale n risulta avere carica libera non uniforme tra drain e source, a causa del pinch off ho molta meno carica
   libera nei pressi del drain, la resistività cresce e ho caduta di potenziale.
   Posso pensare 𝑉(𝑥) a profilo parabolico con vertice su 𝑥 = 0:
                                                                  𝑉𝐷𝑆
                                                          𝑉(𝑥) ≈ 2 ⋅ 𝑥 2
                                                                   𝐿
   Pongo come condizione di essere ai limiti della saturazione: 𝑉𝐷𝑆 = 𝑉𝐺𝑆 − 𝑉𝑇
   Sfruttando la formula della carica di inversione mi calcolo la carica di canale nello stesso modo utilizzato anche nel
   caso triodo:
                 𝐿
   |𝑄𝐶𝐻 | = 𝑊 ∫ 𝐶𝑂𝑋 [𝑉𝐺𝑆 − 𝑉𝑇 − 𝑉(𝑥)] 𝑑𝑥
                0
                 𝐿
                                𝑉𝐷𝑆 2
         = 𝑊 ∫ 𝐶𝑂𝑋 [𝑉𝐺𝑆 − 𝑉𝑇 −     𝑥 ] 𝑑𝑥
             0                  𝐿2
                                        𝑉𝐷𝑆 𝐿
         = 𝑊𝐿𝐶𝑂𝑥 𝑉𝐺𝑆 − 𝑊𝐿𝐶𝑂𝑥 𝑉𝑇 − 𝑊𝐶𝑂𝑥 2 ∫ 𝑥 2 𝑑𝑥
                                         𝐿 0
                                              𝐿
                                    𝑉𝐷𝑆 1
         = 𝑊𝐿𝐶𝑂𝑥 (𝑉𝐺𝑆 − 𝑉𝑇 ) − 𝑊𝐶𝑂𝑥 2 [ 𝑥 3 ]
                                     𝐿 3      0
                                   1
         = 𝑊𝐿𝐶𝑂𝑥 (𝑉𝐺𝑆 − 𝑉𝑇 − 3 𝑉𝐷𝑆 ) con 𝑉𝐷𝑆 = 𝑉𝐺𝑆 − 𝑉𝑇
                             1       1
         = 𝑊𝐿𝐶𝑂𝑥 (𝑉𝐺𝑆 − 𝑉𝑇 − 𝑉𝐺𝑆 + 𝑉𝑇 )
                             3       3
           2
         = 𝑊𝐿𝐶𝑂𝑋 (𝑉𝐺𝑆 − 𝑉𝑇 )
           3
   Ottengo una carica di canale dipendente solamente da 𝑉𝐺𝑆 da cui mi calcolo le capacità di canale:
                                                             ∂|𝑄𝐶𝐻 | 2
                                                    𝐶𝐺𝑆𝑐 =          = 𝑊𝐿𝐶𝑂𝑋
                                                              ∂𝑉𝐺𝑆   3
                                                                 ∂|𝑄𝐶𝐻 |
                                                        𝐶𝐺𝐷𝑐 =           =0
                                                                  ∂𝑉𝐺𝐷



Quando il MOSFET è ON la carica di svuotamento (carica negativa fissa dovuta alla ricombinazione delle lacune del
p-Si con elettroni) è praticamente costante ed è indipendente dalle tensioni applicate, di conseguenza non induce
effetti reattivi tra gate e bulk. In condizioni di triodo e di saturazione gli unici effetti reattivi intrinseci da valutare nello
studio delle capacità del MOSFET sono quindi quelli dovuti alla carica 𝑄𝐶𝐻 che dipende soltanto da 𝑉𝐺𝑆 e 𝑉𝐷𝑆 .

- MOSFET OFF:
   quando il MOSFET è OFF non ho canale conduttivo, di conseguenza non ci sarà carica di inversione, la carica di
   svuotamento vale:

                                                        𝑄𝐷 (𝑥) = −γ𝐶𝑂𝑋 √ψ𝑆

   il potenziale di superficie è pari alla caduta nel substrato, le due giunzioni S-B e D-B isolano il substrato da source e
   drain, di conseguenza la caduta nel substrato dipende soltanto da 𝑉𝐺𝐵 :

                                                                 ∂|𝑄𝐷 |
                                                     𝐶𝐺𝐵 = 𝑊𝐿           ≅ 𝑊𝐿𝐶𝑂𝑥
                                                                 ∂𝑉𝐺𝐵

   La derivata nella formula precedente risulta complicata da risolvere, di conseguenza viene spesso approssimata
       𝜕|𝑄 |
   con 𝜕𝑉 𝐷 ≅ 𝐶𝑂𝑥 che sarebbe l’ipotesi di caso peggiore.
          𝐺𝐵
   La carica di svuotamento non dipende dalle tensioni 𝑉𝐺𝑆 e 𝑉𝐺𝐷 , di conseguenza:

                                                                     ∂|𝑄𝐷 |
                                                            𝐶𝐺𝑆𝐷 =          =0
                                                                     ∂𝑉𝐺𝑆

                                                                      ∂|𝑄𝐷 |
                                                            𝐶𝐺𝐷𝐷 =           =0
                                                                      ∂𝑉𝐺𝐷



Passiamo ora all’analisi degli effetti reattivi parassiti all’interno di un
MOSFET, essi sono dovuti a non idealità e ad effetti di bordo.
In un MOSFET ideale le regioni di source e drain dovrebbero essere
perfettamente allineate con il gate ma non dovrebbero mai sovrapporsi,
imperfezioni nel processo di annealing (trasformazione del Si puro in Si
drogato) però causano un’estensione delle regioni di source e drain al di sotto
del gate (𝑋𝑑 ), da questo fenomeno risultano capacità parassite chiamate di
OVERLAP.
Si definiscono inoltre le capacità di FRINGING (𝐶𝑓𝑟 ) dovute ai campi elettrici
che vengono a crearsi sui confini tra gate e source/drain, dipendono da molti
fattori, per questo spesso si utilizzano dei valori predefiniti diversificati in
base alla tecnologia in esame.

                     CGDp = 𝐶𝐺𝑆𝑝 = 𝑊(𝑋𝑑 𝐶𝑂𝑥 + 𝐶𝑓𝑟 ) = 𝑊𝐶𝐺𝑆0

indipendenti dalle tensioni.

Come precedentemente spiegato per il corretto funzionamento di un
MOSFET le giunzioni S-B e D-B devono essere sempre polarizzate in
inversa, questo mi porterà ad avere delle capacità di giunzione descritte
da formule gia dimostrate in precedenza:
                                         1
                          𝐶𝑗 = 𝐶𝑗0
                                           |𝑉 |
                                    √1 + Φ𝑆𝐵
                                             𝑗

Dove Φ𝑗 è il potenziale di built-in e 𝐶𝑗0 è la capacità di giunzione all’equilibrio
→ 𝐶𝑆𝐵 = 𝐶𝐷𝐵 = 𝑊𝐿𝑆 𝐶𝑗



Quindi, ricapitolando le varie capacità nel MOSFET individuate fino ad ora:

@ 𝐶𝐺𝑆 = 𝐶𝐺𝑆𝑐 + 𝐶𝐺𝑆𝑝
  𝐶𝐺𝐷 = 𝐶𝐺𝐷𝑐 + 𝐶𝐺𝐷𝑝
  le capacità di canale dipendono dalla regione di funzionamento del MOSET e le capacità
  parassite dipendono da parametri di progetto (𝐶𝐺𝑆𝑝 = 𝐶𝐺𝐷𝑝 = 𝑊𝐶𝐺𝑆0 ).

@ 𝐶𝐺𝐵 è diversa da zero solo quando il MOSFET è OFF.
@ 𝐶𝑆𝐵 = 𝐶𝐷𝐵 sono le capacità delle giunzioni S-B e D-B in inversa.


Nella maggior parte dei circuiti con i MOSFET il gate è il terminale di ingresso che viene pilotato dai
circuiti a monte, gli altri terminali sono spesso mantenuti a tensione costante:

             𝐶𝐺 = 𝐶𝐺𝑆 + 𝐶𝐺𝐷 + 𝐶𝐺𝐵 = 𝐶𝐺𝑆𝑐 + 𝐺𝐺𝐷𝑐 + 𝐶𝐺𝐵 + 2𝑊𝐶𝐺𝑆0
Considerando i risultati che si ottengono per 𝐶𝐺 nelle varie regioni di funzionamento
posso semplificare ed usare come approssimazione generale cautelativa:

                               𝐶𝐺 ≈ 𝑊𝐿𝐶𝑂𝑥 + 2𝑊𝐶𝐺𝑆0
18- Inverter CMOS

      L’utilizzo combinato di n-MOSFET e p-MOSFET per la realizzazione di circuiti digitali ha portato allo
      sviluppo della tecnologia CMOS, l’inverter CMOS è la porta logica più semplice, esso è composto
      solamente da un n-MOSFET e un p-MOSFET ed implementa la funzione logica NOT.

      Osservando la topologia della porta è possibile notare come la 𝑉𝑖 corrisponda alla 𝑉𝐺 e la 𝑉𝑜
      corrisponda alla 𝑉𝐷 in entrambi i MOSFET. Nel caso del p-MOSFET il source sarà collegato a 𝑉𝐷𝐷 mentre
      per l’n-MOSFET sarà collegato a terra.
      Analizziamo ora le regioni di funzionamento dei singoli MOSFET al variare delle condizioni imposte
      ricordando che 𝑉𝑇𝑛 > 0 e 𝑉𝑇𝑝 < 0:
      𝑴𝒏 :
         OFF: 𝑉𝐺𝑆𝑛 < 𝑉𝑇𝑛 → 𝑉𝑖 < 𝑉𝑇𝑛 .
         ON: 𝑉𝑖 > 𝑉𝑇𝑛
            TRIODO: 𝑉𝐷𝑛 < 𝑉𝐺𝑛 − 𝑉𝑇𝑛 → 𝑉𝑜 < 𝑉𝑖 − 𝑉𝑇𝑛
            SATURO: 𝑉𝐷𝑛 > 𝑉𝐺𝑛 − 𝑉𝑇𝑛 → 𝑉𝑜 > 𝑉𝑖 − 𝑉𝑇𝑛
      𝑴𝒑 :
        OFF: 𝑉𝐺𝑆𝑝 > 𝑉𝑇𝑝 → 𝑉𝑖 > 𝑉𝐷𝐷 + 𝑉𝑇𝑝 .
        ON: 𝑉𝑖 < 𝑉𝐷𝐷 + 𝑉𝑇𝑝
           TRIODO: 𝑉𝐷𝑝 > 𝑉𝐺𝑝 − 𝑉𝑇𝑝 → 𝑉𝑜 > 𝑉𝑖 − 𝑉𝑇𝑝
           SATURO: 𝑉𝐷𝑝 < 𝑉𝐺𝑝 − 𝑉𝑇𝑝 → 𝑉𝑜 < 𝑉𝑖 − 𝑉𝑇𝑝



      Dopo averli analizzati singolarmente andiamo ad analizzare la porta nel suo insieme differenziando le varie situazioni di
      funzionamento e studiando l’andamento della 𝑉𝑜 in funzione di 𝑉𝑖

      AB: 𝑉𝑖 < 𝑉𝑇𝑛 : 𝑀𝑛 OFF → 𝐼𝐷𝑆𝑛 = 𝐼𝑆𝐷𝑝 = 0 → 𝑀𝑝 triodo con 𝑉𝑆𝐷𝑝 = 0

          → 𝑉𝑜 = 𝑉𝐷𝐷
      BC: 𝑉𝑖 > 𝑉𝑇𝑛 : 𝑀𝑛 ON.
        𝑀𝑝 è ancora regione triodo quindi 𝑉𝑜 = 𝑉𝐷𝑛 = 𝑉𝐷𝐷 , quindi alta e di sicuro
        𝑉𝐷𝑛 > 𝑉𝐺𝑛 − 𝑉𝑇𝑛 → 𝑀𝑛 in saturazione.
         Utilizzando le leggi delle correnti nel MOSFET adeguate alle regioni di
         funzionamento ottengo l’uguaglianza:
        β𝑛                                                 1
           (𝑉 − 𝑉𝑇𝑛 )2 = β𝑝 [(𝑉𝑖 − 𝑉𝐷𝐷 − 𝑉𝑇𝑝 )(𝑉𝑜 − 𝑉𝐷𝐷 ) − (𝑉𝑜 − 𝑉𝐷𝐷 )2]
        2 𝑖                                                2
         Da cui deduco la presenza di una relazione quadratica tra 𝑉𝑖 e 𝑉𝑜.

      CD: 𝑉𝑜 > 𝑉𝑖 − 𝑉𝑇𝑛 (→ 𝑉𝐷𝑛 > 𝑉𝐺𝑛 − 𝑉𝑇𝑛 ) ma anche 𝑉𝑜 < 𝑉𝑖 − 𝑉𝑇𝑝 (→ 𝑉𝐷𝑝 < 𝑉𝐺𝑝 − 𝑉𝑇𝑝)

         → entrambi i MOSFET in saturazione.

                    β𝑛                    β𝑝                   2                   β                      β
                         (𝑉𝑖 − 𝑉𝑇𝑛 )2 =        (𝑉𝑖 − 𝑉𝐷𝐷 − 𝑉𝑇𝑝 )   → 𝑉𝑖 − 𝑉𝑇𝑛 = √β𝑝 |𝑉𝑖 − 𝑉𝐷𝐷 − 𝑉𝑇𝑝 | = √β𝑝 (𝑉𝐷𝐷 + 𝑉𝑇𝑝 − 𝑉𝑖 )
                    2                     2                                         𝑛                      𝑛


         Nel passaggio precedente ho messo entrambi i membri sotto radice, facendo questo però bisogna prestare attenzione al
         segno del radicando, il primo membro è sicuramente positivo dato che 𝑉𝑖 > 𝑉𝑇𝑛 , il secondo membro invece risulta negativo
         dato che 𝑉𝑖 < 𝑉𝐷𝐷 + 𝑉𝑇𝑝 dovrò di conseguenza metterlo a valore assoluto e cambiarci i segni (spiegazione dettagliata a fine
         documento).
         Al passaggio precedente continuando a risolvere isolando 𝑉𝑖 arrivo alla formula seguente:

                                                                           𝛃
                                                                          √ 𝒑 (𝑽𝑫𝑫 + 𝑽𝑻𝒑 )
                                                                           𝛃𝒏
                                                       𝑽𝑳𝑻 = 𝑉𝑖 = 𝑽𝑻𝒏 +
                                                                                   𝛃𝒑
                                                                              𝟏 + √𝛃
                                                                                        𝒏
         Come è possibile notare dal grafico nella sezione CD, l’andamento della tensione 𝑉𝑜 in funzione della 𝑉𝑖 è estremamente
         ripido, in questa regione è quindi possibile semplificare dicendo che alla tensione di ingresso 𝑉𝑖 = 𝑉𝐿𝑇 corrisponde un range
         di valori di 𝑉𝑜 limitato inferiormente da 𝑉𝐿𝑇 − 𝑉𝑇𝑛 (D) e superiormente da 𝑉𝐿𝑇 + |𝑉𝑇𝑝 | (C).



      DE: 𝑉𝑖 < 𝑉𝐷𝐷 + 𝑉𝑇𝑝: 𝑀𝑝 ON
        𝑀𝑛 è in triodo quindi 𝑉𝑜 = 0, di conseguenza 𝑉𝐷𝑝 < 𝑉𝐺𝑝 − 𝑉𝑇𝑝 → 𝑀𝑝 in saturazione.
        Analizzando le equazioni delle correnti nei MOSFET in accordo con le regioni di funzionamento, come è stato fatto per la
        regione BC, si ottiene di nuovo una relazione quadratica tra Vi e 𝑉𝑜.

      EF: 𝑉𝑖 > 𝑉𝐷𝐷 + 𝑉𝑇𝑝 = 𝑉𝐷𝐷 − |𝑉𝑇𝑝 | → 𝑀𝑝 OFF → 𝐼𝑆𝐷𝑝 = 𝐼𝐷𝑆𝑛 = 0 → 𝑉𝐷𝑆𝑛 = 0 → 𝑉𝑜 = 0
                                                                             𝑉
      Generalmente si dimensionano i MOSFET in modo da avere 𝑉𝐿𝑇 = 𝐷𝐷 così che ci siano gli stessi noise margins per la zona di
                                                                   2
      tensione alta e quella di tensione bassa, osservando la formula ottenuta in precedenza di 𝑉𝐿𝑇 si deduce facilmente che la
      condizione appena riportata si ottiene se β𝑝 = β𝑛 .



19- Consumo di potenza in un inverter CMOS

      Se supponiamo che le transizioni all’interno del circuito digitale CMOS siano istantanee il calcolo della potenza assorbita da un
      inverter è relativamente semplice. La potenza statica, se trascuriamo eventuali effetti di non idealità, sarà nulla, questo è dovuto
      al fatto che sia nel caso in cui 𝑉𝐼𝑁 = 0 sia nel caso in cui 𝑉𝐼𝑁 = 𝑉𝐷𝐷 uno dei due MOSFET sarà sempre spento, non consentendo
      il passaggio di corrente di cortocircuito.
      Per quanto riguarda la potenza dinamica, essa seguirà le furmule dimostrate alla domanda 28:
                                                                           2
                                                                𝑃𝑑𝑖𝑛 = 𝐶𝐿 𝑉𝐷𝐷 𝑓0→1



      La supposizione che le transizioni siano istantanee è però poco verosimile, infatti, per
      effetti capacitivi e non idealità la transizione è spesso più giusto considerarla graduale.

      Nel grafico affianco si possono individuare le diverse fasi della transizione al variare di
      𝑉𝐼𝑁 . In magenta (𝑡 < 𝑡1 ) è evidenziata la regione in cui 𝑀𝑛 è spento, in blu (𝑡1 < 𝑡 < 𝑡2 )
      la regione in cui 𝑀𝑛 è saturo e 𝑀𝑝 è triodo, in giallo (𝑡2 < 𝑡 < 𝑡3 ) quella in cui 𝑀𝑛 è triodo
      e 𝑀𝑝 è saturo ed in rosso quella in cui 𝑀𝑝 è spento.
      Il tempo totale per la salita da 𝑉𝐼𝑁 = 0 e 𝑉𝐼𝑁 = 𝑉𝐷𝐷 è 𝑡𝑟 .


      Come per il caso delle transizioni istantanee negli istanti di tempo in cui c’è almeno un
      MOSFET spento (magenta e rosso) la corrente di cortocircuito sarà nulla, la differenziazione rispetto al caso precedente sta nel
      fatto che ora ci sono istanti di tempo in cui entrambi i MOSFET sono accesi, per questo nell’intervallo di tempo 𝑡1 ÷ 𝑡3 ci sarà
      una corrente 𝐼𝑠ℎ𝑜𝑟𝑡 > 0 .

      Volendo essere esaustivi fino in fondo la potenza di corto circuito oltre alla 𝐼𝑠ℎ𝑜𝑟𝑡 sarebbe anche
      dipendente dalla corrente di carica/scarica della capacità di carico 𝐶𝐿 . Questo però
      complicherebbe molto il calcolo, di conseguenza valuteremo il caso peggiore, cioè una 𝐶𝐿
      molto piccola che mi porta ad avere una corrente di carica/scarica trascurabile e una
      𝐼𝑛 ≈ 𝐼𝑝 = 𝐼𝑠ℎ𝑜𝑟𝑡




      Passiamo ora al calcolo vero e proprio, iniziando dall’energia consumata per ogni commutazione:
                       𝑡3                    𝑡2                  𝑡3                        𝑡2                 𝑡2
                                                                                                                β𝑛
              𝐸𝑆𝐶 = ∫ 𝑉𝐷𝐷 𝐼𝑆𝐶 (𝑡)𝑑𝑡 = ∫ 𝑉𝐷𝐷 𝐼𝑛 (𝑡)𝑑𝑡 + ∫ 𝑉𝐷𝐷 𝐼𝑝(𝑡)𝑑𝑡 = 2𝑉𝐷𝐷 ∫ 𝐼𝑛 (𝑡)𝑑𝑡 = 2𝑉𝐷𝐷 ∫                    (𝑉𝑖𝑛 − 𝑉𝑇 )2 𝑑𝑡
                      𝑡1                    𝑡1                  𝑡2                        𝑡1                 𝑡1 2

      Posso supporre che, come è possibile dedurre dal grafico, 𝑉𝐼𝑁 cresca linearmente nell’intervallo tra 0 e 𝑡𝑟 , di conseguenza:
             𝑉
𝑡1 = 𝑡𝑟 𝑉𝑇𝑛
              𝐷𝐷

             𝑉          𝑡                                                𝑉
𝑡2 = 𝑡𝑟 𝑉𝐿𝑇 = 2𝑟 supponendo che 𝑉𝐿𝑇 = 𝐷𝐷
              𝐷𝐷                      2

                                                𝑉                                𝑡
Quindi, in generale, 𝑡 = 𝑡𝑟 ⋅ 𝑉 𝑖𝑛 → 𝑉𝑖𝑛 = 𝑉𝐷𝐷 𝑡
                                                 𝐷𝐷                               𝑟


e inserendo nell’integrale dell’energia:
                                                                                  𝑡𝑟
                                                                                                    𝑡             2            β𝑛 𝑡𝑟 𝑉𝐷𝐷                 3
                                                → 𝐸𝑆𝐶𝑓 = 𝑉𝐷𝐷 β𝑛 ∫ 2 𝑉𝑇𝑛 (𝑉𝐷𝐷 𝑡 − 𝑉𝑇 ) 𝑑𝑡 =                                            ( 2 − 𝑉𝑇 )
                                                                                 𝑡𝑟                  𝑟                           3
                                                                                      𝑉𝐷𝐷

equivalente all’energia consumata per il “rise” del segnale 𝑉𝐼𝑁 (ed il coseguente “fall” di 𝑉𝑜 dato che stiamo parlando di inverter).

                                                                                                        𝛽𝑛 𝑡𝑓 𝑉𝐷𝐷       3
                                                                                       →𝐸𝑆𝐶𝑟 =               ( 2 − 𝑉𝑇 )
                                                                                                         3
equivalente all’energia consumata per il “fall” del segnale 𝑉𝐼𝑁 (ed il conseguente “rise” di 𝑉𝑜).
Nota: Si, i tempi di rise e di fall sono riferiti alla transizione in ingresso mentre l’energia di rise e di fall è riferita alla transizione in uscita. Di conseguenza per calcolare l’energia di fall dovrò utilizzare
i tempi di rise e viceversa dato che essendo un inverter il rise in ingresso mi causerà un fall in uscita. Per quanto mi riguarda questi riferimenti complicano solo le cose ma questo è quello che ha
voluto il grande maestro Driussi.


Ora, è possibile dedurre dalle formule della corrente in un MOSFET che la 𝐼𝑠ℎ𝑜𝑟𝑡 massima si ottenga quando 𝑉𝐼𝑁 = 𝑉𝐿𝑇 quindi:
                                                                                                               2
                                                                               β𝑛                β𝑛 𝑉𝐷𝐷
                                                                 𝐼𝑝𝑒𝑎𝑘 =          (𝑉𝐿𝑇 − 𝑉𝑇 )2 =   (    − 𝑉𝑇 )
                                                                               2                 2 2
che, sostituita all’interno delle formule delle energie:
                             3
             β𝑛 𝑡𝑅 𝑉𝐷𝐷          2𝑡𝑅      𝑉𝐷𝐷
𝐸𝑆𝐶𝑓 =            (    − 𝑉𝑇 ) =     𝐼  (     − 𝑉𝑇 )
              3     2            3 𝑝𝑒𝑎𝑘 2
             2𝑡𝐹         𝑉𝐷𝐷
𝐸𝑆𝐶𝑟 =           𝐼𝑝𝑒𝑎𝑘 (     − 𝑉𝑇 )
              3           2
A questo punto, per ottenere la potenza di corto circuito consumata in un ciclo mi basterà moltiplicare l’energia per la frequenza
                                        𝐸
di commutazione ( 𝑃 = 𝑡 ):

                                                                                       𝑃𝑆𝐶 = (𝐸𝑆𝐶𝑓 + 𝐸𝑆𝐶𝑟 ) ⋅ 𝑓

che si semplifica se suppongo 𝑡𝑐 = 𝑡𝑟 = 𝑡𝑓

                                                                                            4𝑡𝐶      𝑉𝐷𝐷
                                                                                 𝑃𝑆𝐶 =          𝐼  (     − 𝑉𝑇 ) ⋅ 𝑓
                                                                                             3 𝑝𝑒𝑎𝑘 2



Il calcolo appena riportato è stato svolto ipotizzando una capacità di carico molto piccola (assorbe corrente trascurabile) che,
come già scritto, coincide con il caso peggiore. Nel caso in cui questa ipotesi non sussistesse, la capacità 𝐶𝐿 andrà a ridurre la
potenza di corto circuito dato che parte della corrente verrà utilizzata per caricare il condensatore anziché andare a massa,
questa conseguenza, apparentemente positiva, si andrà però a ripercuotere su 𝑡𝑐 che aumenterà.
Con l’aumento di 𝑡𝑐 avrò un conseguente rallentamento della transizione di 𝑉𝑜. Se teniamo conto che, molto probabilmente, la 𝑉𝑜
dello stadio corrente sarà la 𝑉𝑖 di uno stadio successivo, il fatto di avere una capacità non trascurabile in uscita si rivela essere
una caratteristica non sempre desiderabile.
20- Capacità inverter MOSFET ed effetto Miller

       Abbiamo visto in precedenza come sia necessario, al fine di calcolare i tempi di commutazione oppure la potenza consumata,
       conoscere le capacità appartenenti ad un dato inverter, nell’analisi che segue il calcolo verrà diviso in capacità in ingresso e
       capacità in uscita.

       La capacità in ingresso 𝐶𝑖𝑛𝑣 sarà ottenuta sommando le capacità viste sul gate dei due MOSFET, quindi, ipotizzando che le
       capacità di fringing e di overlap siano identiche sia per source e drain dei singoli MOSFET sia per n-MOSFET e p-MOSFET ottengo:

                                                           𝐶𝐺𝑛 ≈ 𝑊𝑛 𝐿𝑛 𝐶𝑂𝑥 + 2𝑊𝑛 𝐶𝐺𝑆0

                                                           𝐶𝐺𝑝 ≈ 𝑊𝑝 𝐿𝑝 𝐶𝑂𝑥 + 2𝑊𝑝 𝐶𝐺𝑆0

       Ipotizzo ora di avere MOSFET a lunghezza minima → 𝐿𝑛 = 𝐿𝑝 = 𝐿𝑀𝐼𝑁

                                          𝐶𝑖𝑛𝑣 = 𝐶𝐺𝑛 + 𝐶𝐺𝑝 = (𝑊𝑛 + 𝑊𝑝 )𝐿𝑀𝐼𝑁 𝐶𝑂𝑥 + 2(𝑊𝑛 + 𝑊𝑝 )𝐶𝐺𝑆0

       Ricordando che:
                                    𝑊                     𝑊                    𝑆      𝑊
                             𝑆𝑛 = 𝐿 𝑛              𝑆𝑝 = 𝐿 𝑝               α = 𝑆𝑝 = 𝑊𝑝     → 𝑊𝑝 = α𝑊𝑛 = α𝐿𝑀𝐼𝑁 𝑆𝑛
                                    𝑀𝐼𝑁                    𝑀𝐼𝑁                  𝑛     𝑛


       Posso semplificare la formula ottenuta in precedenza

       𝐶𝑖𝑛𝑣 = (𝑊𝑛 + 𝑊𝑝 )𝐿𝑀𝐼𝑁 𝐶𝑂𝑥 + 2(𝑊𝑛 + 𝑊𝑝 )𝐶𝐺𝑆0

            = 𝑊𝑛 𝐿𝑀𝐼𝑁 𝐶𝑂𝑥 + 𝑊𝑝 𝐿𝑀𝐼𝑁 𝐶𝑂𝑥 + 2𝑊𝑛 𝐶𝐺𝑆0 + 2𝑊𝑝 𝐶𝐺𝑆0               con 𝑊𝑛 = 𝑆𝑛 𝐿𝑀𝐼𝑁       e 𝑊𝑝 = α𝐿𝑀𝐼𝑁 𝑆𝑛

            = 𝑆𝑛 𝐿2𝑀𝐼𝑁 𝐶𝑂𝑥 + α𝐿2𝑀𝐼𝑁 𝑆𝑛 𝐶𝑂𝑥 + 2𝑆𝑛 𝐿𝑀𝐼𝑁 𝐶𝐺𝑆0 + 2α𝐿𝑀𝐼𝑁 𝑆𝑛 𝐶𝐺𝑆0

            = 𝑆𝑛 [𝐿2𝑀𝐼𝑁 𝐶𝑂𝑥 + 2𝐿𝑀𝐼𝑁 𝐶𝐺𝑆0 + α(𝐿2𝑀𝐼𝑁 𝐶𝑂𝑥 + 2𝐿𝑀𝐼𝑁 𝐶𝐺𝑆0 )]

            = 𝑆𝑛 (1 + α)(𝐿2𝑀𝐼𝑁 𝐶𝑂𝑥 + 2𝐿𝑀𝐼𝑁 𝐶𝐺𝑆0 )

       Definisco ora la 𝐶𝑀1 = 𝐿2𝑀𝐼𝑁 𝐶𝑂𝑥 + 2𝐿𝑀𝐼𝑁 𝐶𝐺𝑆0 che rappresenta la capacità di un MOSFET ad area minima e dipende soltanto
       da parametri tecnologici così da ottenere:

                                                                 𝑪𝒊𝒏𝒗 = 𝑺𝒏 (𝟏 + 𝛂)𝑪𝑴𝟏



       Passiamo ora al calcolo della capacità in uscita 𝐶𝐿 , per farlo terremo conto
       di tutti i possibili contributi capacitivi che agiscono sul nodo di uscita, come
       capacità di carico ipotizzeremo di avere un secondo inverter che mi darà un
       contributo costante:

                                 𝐶𝑖𝑛𝑣2 = 𝑆𝑛2 (1 + α2 )𝐶𝑀1

                        → 𝑪𝑳 = 𝑪𝑮𝑫𝒆𝒒 + 𝑪𝑫𝑩𝒆𝒒 + 𝑪𝑾 + 𝑪𝒊𝒏𝒗𝟐
       𝐶𝑊 è la capacità dell’interconnessione tra i due inverter.

       Iniziamo con il calcolo della capacità di giunzione che viene a crearsi tra drain e bulk:

                                                                                𝐶𝑗0
                                                              𝐶𝐷𝐵 = 𝑊𝐿𝑆
                                                                               |𝑉 |
                                                                           √1 + ϕ𝐷𝐵
                                                                                  𝑗


       Osserviamo però che in questa forma la capacità non è costante dato che risulta essere funzione di 𝑉𝐷𝐵 che a sua volta è
       funzione di 𝑉𝑂𝑈𝑇 .
       Per semplificare definiamo una 𝐶𝐷𝐵𝑒𝑞 che equivale al valore medio di 𝐶𝐷𝐵 durante il transitorio di carica/scarica:
                 ∞                   𝑉𝑂𝑓 𝑊𝐿 𝐶
                        𝑑𝑉𝑂𝑈𝑇               𝑆 𝑗0
       Δ𝑄𝑗 = ∫ 𝐶𝐷𝐵            𝑑𝑡 = ∫              𝑑𝑉𝑂𝑈𝑇
                0        𝑑𝑡         𝑉𝑂𝑖      𝑉𝑂𝑈𝑇
                                        √1 + Φ
                                                     𝑗
           Δ𝑄𝑗             𝑉𝑂𝑓 𝑊𝐿 𝐶
                    1             𝑆 𝑗0
𝐶𝐷𝐵𝑒𝑞 =        =         ∫              𝑑𝑉𝑂𝑈𝑇
          Δ𝑉𝑂𝑈𝑇 𝑉𝑂𝑖 − 𝑉𝑂𝑓 𝑉𝑂𝑖
                                   𝑉𝑂𝑈𝑇
                              √1 + Φ
                                                           𝑗


                                                               VOf
                        WLS Cj0           VOUT
                     =           [2Φj√1 +      ]
                       VOi − VOf           Φj
                                                               VOi


                         2Φj WLS Cj0        VOf        VOi
                     =               [√ 1 +     − √1 +     ]
                          VOi − VOf         Φj         Φj

                               2Φ𝑗              𝑉𝑂𝑓              𝑉
Definiamo ora 𝐾𝑒𝑞 = 𝑉 −𝑉 [√1 + Φ − √1 + Φ𝑂𝑖 ], se supponiamo di essere in condizioni ideali, quindi 𝑉𝑂𝐻 = 𝑉𝐷𝐷 , 𝑉𝑂𝐿 = 0,
                            𝑂𝑖       𝑂𝑓           𝑗                  𝑗

e scegliamo il caso di transitorio di scarica in ingresso (carica in uscita) → 𝑉𝑂𝑖 = 𝑉𝑂𝐿 = 0 e 𝑉𝑂𝑓 = 𝑉𝑂𝐻 = 𝑉𝐷𝐷 ottengo:

                                                       2Φ𝑗        𝑉𝐷𝐷
                                               𝐾𝑒𝑞 =       [√ 1 +     − 1]            𝑪𝑫𝑩𝒆𝒒 = 𝑲𝒆𝒒 𝑾𝑳𝑺 𝑪𝒋𝟎
                                                       𝑉𝐷𝐷        Φ𝑗

Continuiamo ora lo studio andando a calcolare la capacità tra gate e drain. Notiamo che non hanno terminali a massa essendo
posizionati tra 𝑉𝐼𝑁 e 𝑉𝑂𝑈𝑇 , saranno quindi soggetti ad una tensione 𝑉𝐼𝑁 − 𝑉𝑂𝑈𝑇 e di conseguenza dipendono dal punto di lavoro.
La 𝐶𝐺𝐷𝑝 e 𝐶𝐺𝐷𝑛 per la topologia dell’inverter risultano essere in parallelo → 𝐶𝐺𝐷 = 𝐶𝐺𝐷𝑝 + 𝐶𝐺𝐷𝑛 .
In questo modo le capacità dipendono dall’evoluzione temporale di 𝑉𝐼𝑁 e 𝑉𝑂𝑈𝑇 contemporaneamente, il ché è
piuttosto complicato da studiare, fissiamo quindi come ipotesi semplificativa che i transitori di 𝑉𝐼𝑁 e 𝑉𝑂𝑈𝑇 siano
disgiunti così che in ogni istante di tempo risulti variare soltanto una delle due tensioni.
Così facendo possiamo studiare separatamente tutte le diverse regioni di funzionamento dell’inverter, iniziando
dall’effetto del rise in ingresso e finendo con gli effetti del fall in uscita.

Sia (A) la fase di rise di 𝑉𝐼𝑁 quando 0 < 𝑡 < 𝑡𝑟𝑖 → 𝑉𝐼𝑁 varia e 𝑉𝑂𝑈𝑇 = 𝑉𝐷𝐷 :

   - (A1) 𝑉𝐼𝑁 < 𝑉𝑇𝑛 → 𝑀𝑛 OFF e 𝑀𝑝 triodo con 𝑉𝑆𝐷 = 0
                                                       1                                       1
                  𝐶𝐺𝐷𝑛 = 𝑊𝑛 𝐶𝐺𝑆0              𝐶𝐺𝐷𝑝 = 2 𝑊𝑝 𝐿𝑀𝐼𝑁 𝐶𝑂𝑥 + 𝑊𝑝 𝐶𝐺𝑆0          → 𝐶𝐺𝐷 = 2 𝑊𝑝 𝐿𝑀𝐼𝑁 𝐶𝑂𝑥 + (𝑊𝑛 + 𝑊𝑝 )𝐶𝐺𝑆0




   - (A2) 𝑉𝑇𝑛 < 𝑉𝐼𝑁 < 𝑉𝐷𝐷 + 𝑉𝑇𝑝 → 𝑀𝑛 saturo con 𝑉𝐷𝑆 = 𝑉𝐷𝐷 e 𝑀𝑝 triodo
                                                       1                                       1
                  𝐶𝐺𝐷𝑛 = 𝑊𝑛 𝐶𝐺𝑆0              𝐶𝐺𝐷𝑝 = 2 𝑊𝑝 𝐿𝑀𝐼𝑁 𝐶𝑂𝑥 + 𝑊𝑝 𝐶𝐺𝑆0          → 𝐶𝐺𝐷 = 2 𝑊𝑝 𝐿𝑀𝐼𝑁 𝐶𝑂𝑥 + (𝑊𝑛 + 𝑊𝑝 )𝐶𝐺𝑆0

   - (A3) 𝑉𝐼𝑁 > 𝑉𝐷𝐷 + 𝑉𝑇𝑝 → 𝑀𝑛 saturo con 𝑉𝐷𝑆 = 𝑉𝐷𝐷 e 𝑀𝑝 OFF
                            𝐶𝐺𝐷𝑛 = 𝑊𝑛 𝐶𝐺𝑆0     𝐶𝐺𝐷𝑝 = 𝑊𝑝 𝐶𝐺𝑆0                         → 𝐶𝐺𝐷 = (𝑊𝑛 + 𝑊𝑝 )𝐶𝐺𝑆0



Sia (B) la fase di fall di 𝑉𝑂𝑈𝑇 quando 𝑡 > 𝑡𝑟𝑖 ; 𝑉𝑂𝑈𝑇 varia e 𝑉𝐼𝑁 = 𝑉𝐷𝐷 → 𝑀𝑝 OFF e 𝑀𝑛 ON:

   - (B1) 𝑉𝑂𝑈𝑇 > 𝑉𝐷𝐷 − 𝑉𝑇𝑛 → 𝑀𝑛 saturo e 𝑀𝑝 OFF
                            𝐶𝐺𝐷𝑛 = 𝑊𝑛 𝐶𝐺𝑆0    𝐶𝐺𝐷𝑝 = 𝑊𝑝 𝐶𝐺𝑆0                          → 𝐶𝐺𝐷 = (𝑊𝑛 + 𝑊𝑝 )𝐶𝐺𝑆0

   - (B2) 𝑉𝑂𝑈𝑇 < 𝑉𝐷𝐷 − 𝑉𝑇𝑛 → 𝑀𝑛 triodo e 𝑀𝑝 OFF
                           1                                                                   1
                  𝐶𝐺𝐷𝑛 = 2 𝑊𝑛 𝐿𝑀𝐼𝑁 𝐶𝑂𝑥 + 𝑊𝑛 𝐶𝐺𝑆0                     𝐶𝐺𝐷𝑝 = 𝑊𝑝 𝐶𝐺𝑆0   → 𝐶𝐺𝐷 = 2 𝑊𝑛 𝐿𝑀𝐼𝑁 𝐶𝑂𝑥 + (𝑊𝑛 + 𝑊𝑝 )𝐶𝐺𝑆0




Iniziamo ora con il calcolo della carica totale data dalla somma delle cariche nelle fasi (A) (Δ𝑄0 ’) e (B) (Δ𝑄0 ’’)
          ∞                               𝑑𝑉𝑂𝑈𝑇 𝑑𝑉𝐼𝑁
Δ𝑄𝑂 = ∫ 𝐶𝐺𝐷 (𝑉𝐼𝑁 , 𝑉𝑂𝑈𝑇 ) (                    −     ) 𝑑𝑡 = Δ𝑄0 ’ + Δ𝑄0 ’’
          0                                𝑑𝑡    𝑑𝑡
              𝑡𝑟𝑖                                      ∞
                                           𝑑𝑉𝐼𝑁                          𝑑𝑉𝑂𝑈𝑇
     = −∫           𝐶𝐺𝐷 (𝑉𝐼𝑁 , 𝑉𝑂𝑈𝑇 )           𝑑𝑡 + ∫ 𝐶𝐺𝐷 (𝑉𝐼𝑁 , 𝑉𝑂𝑈𝑇 )       𝑑𝑡
              0                             𝑑𝑡        𝑡𝑟𝑖                 𝑑𝑡
       Ricaviamo Δ𝑄0’ con (A1)(A2) e (A3):
                   𝑡𝑟𝑖                              𝑉𝐷𝐷
                                     𝑑𝑉𝐼𝑁
       Δ𝑄0 ’ = − ∫ 𝐶𝐺𝐷 (𝑉𝐼𝑁 , 𝑉𝑂𝑈𝑇 )       𝑑𝑡 = − ∫ 𝐶𝐺𝐷 (𝑉𝐼𝑁 , 𝑉𝑂𝑈𝑇 ) 𝑑𝑉𝐼𝑁
                  0                    𝑑𝑡          0
                    𝑉𝐷𝐷 +𝑉𝑇𝑝                                              𝑉𝐷𝐷
                                 1
             = −∫               [ 𝑊𝑝 𝐿𝑀𝐼𝑁 𝐶𝑂𝑋 + (𝑊𝑛 + 𝑊𝑝 )𝐶𝐺𝑆0 ] 𝑑𝑉𝐼𝑁 − ∫         (𝑊𝑛 + 𝑊𝑝 )𝐶𝐺𝑆0 𝑑𝑉𝐼𝑁
                   0             2                                       𝑉𝐷𝐷 +𝑉𝑇𝑝

                1
             = − 𝑊𝑝 𝐿𝑀𝐼𝑁 𝐶𝑂𝑋 (𝑉𝐷𝐷 + 𝑉𝑇𝑝 ) − (𝑊𝑛 + 𝑊𝑝 )𝐶𝐺𝑆0 𝑉𝐷𝐷
                2

       Ricaviamo Δ𝑄0’’ con (B1) e (B2)
                  ∞                 𝑑𝑉𝑂𝑈𝑇        0
       Δ𝑄0 ’’ = ∫ 𝐶𝐺𝐷 (𝑉𝐼𝑁 , 𝑉𝑂𝑈𝑇 )       𝑑𝑡 = ∫ 𝐶𝐺𝐷 (𝑉𝐼𝑁 , 𝑉𝑂𝑈𝑇 ) 𝑑𝑉𝑂𝑈𝑇
                 𝑡𝑟𝑖                 𝑑𝑡         𝑉𝐷𝐷

                  𝑉𝐷𝐷 −𝑉𝑇𝑛                               0       1
             =∫             (𝑊𝑛 + 𝑊𝑝 )𝐶𝐺𝑆0 𝑑𝑉𝑂𝑈𝑇 + ∫            [ 𝑊𝑛 𝐿𝑀𝐼𝑁 𝐶𝑂𝑋 + (𝑊𝑛 + 𝑊𝑝 )𝐶𝐺𝑆0 ] 𝑑𝑉𝑂𝑈𝑇
                 𝑉𝐷𝐷                                    𝑉𝐷𝐷 −𝑉𝑇𝑛 2

                                    1
             = −(𝑊𝑛 + 𝑊𝑝 )𝐶𝐺𝑆0 𝑉𝐷𝐷 − 𝑊𝑛 𝐿𝑀𝐼𝑁 𝐶𝑂𝑋 (𝑉𝐷𝐷 − 𝑉𝑇𝑛 )
                                    2

       Ipotizziamo 𝑉𝑇𝑛 = |𝑉𝑇𝑝 | = 𝑉𝑇 e sommiamo i risultati appena ottenuti:
                                                                     1
                                    Δ𝑄𝑂 = −2(𝑊𝑛 + 𝑊𝑝 )𝐶𝐺𝑆0 𝑉𝐷𝐷 − (𝑊𝑛 + 𝑊𝑝 )𝐿𝑀𝐼𝑁 𝐶𝑂𝑋 (𝑉𝐷𝐷 − 𝑉𝑇 )
                                                                     2

       A questo punto, una volta ottenuta la carica ricaviamoci la capacità 𝐶𝐺𝐷𝑒𝑞 (𝑉𝑂𝑓 = 0 , 𝑉𝑂𝑖 = 𝑉𝐷𝐷 ):
                                      Δ𝑄0    Δ𝑄0        Δ𝑄0                    1                   𝑉𝐷𝐷 − 𝑉𝑇
                           𝐶𝐺𝐷𝑒𝑞 =        =          =−     = 2(𝑊𝑛 + 𝑊𝑝 )𝐶𝐺𝑆0 + (𝑊𝑛 + 𝑊𝑝 )𝐿𝑀𝐼𝑁 𝐶𝑂𝑋
                                     Δ𝑉𝑜𝑢𝑡 𝑉𝑂𝑓 − 𝑉𝑂𝑖    𝑉𝐷𝐷                    2                     𝑉𝐷𝐷
                       𝑉   −𝑉𝑇
       Pongo 𝑅𝐷𝐷 = 𝐷𝐷            :
                    𝑉      𝐷𝐷
                                                                     𝟏
                                            𝑪𝑮𝑫𝒆𝒒 = 𝟐(𝑾𝒏 + 𝑾𝒑 )𝑪𝑮𝑺𝟎 + (𝑾𝒏 + 𝑾𝒑 )𝑳𝑴𝑰𝑵 𝑪𝑶𝑿𝐑 𝐃𝐃
                                                                     𝟐

       Osserviamo che le componenti parassite costanti vengono raddoppiate, questo è dovuto all’effetto Miller, in base al quale una
       capacità 𝐶𝐼𝑂 collegata tra l’ingresso e l’uscita di un blocco circuitale lineare avente guadagno di tensione 𝐴𝑉 equivale ad una
       capacità di valore (1 − 𝐴𝑉 )𝐶𝐼𝑂 . La commutazione dell’invertitore è un transitorio di grande segnale durante il quale la relazione
       tra 𝑉𝑂𝑈𝑇 e 𝑉𝐼𝑁 non è affatto lineare, tuttavia il guadagno di tensione medio < 𝐴𝑉 > tra 𝑉𝑂𝑈𝑇 e 𝑉𝐼𝑁 vale ovviamente −1
       → (1− < 𝐴𝑉 >) = 2 .


       Ottenute tutte le componenti della capacità totale in uscita, procediamo a calcolarla:

                                                       𝐶𝐿 = 𝐶𝐺𝐷𝑒𝑞 + 𝐶𝐷𝐵𝑒𝑞 + 𝐶𝑊 + 𝐶𝑖𝑛𝑣2
       Dove quelle in giallo sono dette capacità di self loading mentre quelle in rosso sono capacità di carico.

       𝐶𝐿 = 𝐶𝐺𝐷𝑒𝑞 + 𝐶𝐷𝐵𝑒𝑞 + 𝐶𝑊 + 𝐶𝑖𝑛𝑣2
                              1
          = 2(𝑊𝑛 + 𝑊𝑝 )𝐶𝐺𝑆0 + (𝑊𝑛 + 𝑊𝑝 )𝐿𝑀𝐼𝑁 𝐶𝑂𝑋 𝑅𝐷𝐷 + 𝐾𝑒𝑞 (𝑊𝑛 + 𝑊𝑝 )𝐿𝑆 𝐶𝑗0 + 𝐶𝑊 + 2(𝑊𝑛2 + 𝑊𝑝2 )𝐶𝐺𝑆0 +
                              2
            +(𝑊𝑛2 + 𝑊𝑝2 )𝐿𝑀𝐼𝑁 𝐶𝑂𝑋


21- Modello ai piccoli segnali del BJT (Giaccoletto Johnson)
      Il transistor BJT è un componente non lineare con effetti reattivi, di conseguenza, volendolo analizzare dinamicamente sarà
      necessario il passaggio al modello di piccolo segnale e l’utilizzo delle trasformate di Laplace.
      Il BJT è un tripolo, di conseguenza potrà essere facilmente trasformato in un doppio bipolo, il quale verrà descritto tramite matrici
      e circuiti equivalenti.
      Ricordiamo che per quanto riguarda il modello al grande segnale del BJT si era preso come
      riferimento il modello di Ebers-Moll a tre parametri. Partiremo da qua con la linearizzazione dei
      singoli componenti al fine di giungere ad un modello equivalente al piccolo segnale.
      Il modello di Ebers-Moll è composto da due diodi e un generatore di corrente comandato,
      entrambi componenti di cui è già stato trovato un equivalente a piccolo segnale, iniziamo con i
      diodi.
So che al piccolo segnale:
                                        𝑑𝐼                              𝑑𝐼             𝐼   +𝐼𝑆        1
                               𝑖𝐷 = 𝑑𝑉𝐷 | 𝑣𝐷 → 𝑔𝐷 = 𝑑𝑉𝐷 | = 𝐷0𝑉                                  =𝑟
                                             𝐷 𝑄                             𝐷 𝑄           𝑡ℎ         𝐷



                          𝑑𝑄                    𝑑𝐼                                                            1
                  𝐶𝐷 = 𝑑𝑉𝐷 | = τ𝑇 𝑑𝑉𝐷 | = τ𝑇 𝑔𝐷                                             𝐶𝑗 = 𝐶𝑗0              𝑉
                               𝐷                     𝐷 𝑄                                                      𝐷0
                                   𝑄                                                                      √1−     Φ𝑗



Quindi per quanto riguarda la giunzione B-E:
                                                                                           𝑉𝑡ℎ
                                                                          𝑟𝐵𝐸 =
                                                                                       𝐼𝐵𝐸0 + 𝐼𝐵𝐸,𝑠

                                                𝐶𝐵𝐸 = 𝐶𝐷 + 𝐶𝑗 (in diretta 𝐶𝐵𝐸 ≈ 𝐶𝐷 ; in inversa 𝐶𝐵𝐸 ≈ 𝐶𝑗 )
Giunzione B-C:

                                                                                           𝑉𝑡ℎ
                                                                          𝑟𝐵𝐶 =
                                                                                       𝐼𝐵𝐶0 + 𝐼𝐵𝐶,𝑠

                                                𝐶𝐵𝐶 = 𝐶𝐷 + 𝐶𝑗 (in diretta 𝐶𝐵𝐶 ≈ 𝐶𝐷 ; in inversa 𝐶𝐵𝐶 ≈ 𝐶𝑗 )


Passiamo ora alla linearizzazione del generatore comandato:
                                            𝑉                                                                 𝑉
𝐼𝑡 = β𝐹 𝐼𝐵𝐸 − β𝑅 𝐼𝐵𝐶 = β𝐹0 (1 + 𝑉𝐶𝐵) 𝐼𝐵𝐸 − β𝑅 𝐼𝐵𝐶                         con          β𝐹 = β𝐹0 (1 + 𝑉𝐶𝐵)                e   𝐼𝐵𝐸 = 𝑓(𝑉𝐵𝐸 )       𝐼𝐵𝐶 = 𝑓(𝑉𝐵𝐶 )
                                                𝐴                                                                 𝐴


          𝑑𝐼              𝑑𝐼
→ 𝑖𝑡 = 𝑑𝑉 𝑡 | 𝑣𝐵𝐸 + 𝑑𝑉 𝑡 | 𝑣𝐵𝐶 = 𝑎𝑣𝐵𝐸 + 𝑏𝑣𝐵𝐶 = 𝑎𝑣𝐵𝐸 + 𝑏(𝑣𝐵𝐸 + 𝑣𝐸𝐶 ) = 𝑎𝑣𝐵𝐸 + 𝑏𝑣𝐵𝐸 − 𝑏𝑣𝐶𝐸 = (𝑎 + 𝑏)𝑣𝐵𝐸 − 𝑏𝑣𝐶𝐸
           𝐵𝐸 𝑄               𝐵𝐶 𝑄



Siano 𝑔𝑚 = (𝑎 + 𝑏) la trans-conduttanza e 𝑔𝐶𝐸 = −𝑏 la conduttanza di uscita, con:

     𝑑𝐼           𝑑𝐼                   𝑑𝐼                  𝑑𝐼                 1                 𝑑𝐼𝐵𝐶
𝑎 = 𝑑𝑉 𝑡 | = β𝐹 𝑑𝑉𝐵𝐸 | − β𝑅 𝑑𝑉𝐵𝐶 | = β𝐹 𝑑𝑉𝐵𝐸 | = β𝐹 𝑟                                                | =0              perché       𝐼𝐵𝐶 = 𝑓(𝑉𝐵𝐶 )
       𝐵𝐸 𝑄            𝐵𝐸 𝑄                 𝐵𝐸 𝑄                𝐵𝐸 𝑄          𝐵𝐸                𝑑𝑉𝐵𝐸 𝑄


      𝑑𝐼𝑡     𝑑β𝐹           𝑑𝐼𝐵𝐶          𝐼𝐵𝐸0       1
𝑏=        | =     | 𝐼  − β𝑅      | = −β𝐹0      − β𝑅
     𝑑𝑉𝐵𝐶 𝑄 𝑑𝑉𝐵𝐶 𝑄 𝐵𝐸0      𝑑𝑉𝐵𝐶 𝑄         𝑉𝐴       𝑟𝐵𝐶

                                                                  𝟏            𝑰                 𝟏                              𝑰           𝟏
→ 𝒊𝒕 = 𝒈𝒎 𝒗𝑩𝑬 + 𝒈𝑪𝑬 𝒗𝑪𝑬                con          𝒈𝒎 = 𝜷𝑭 𝒓          − 𝜷𝑭𝟎 𝑩𝑬𝟎 − 𝜷𝑹 𝒓                   e       𝒈𝑪𝑬 = 𝜷𝑭𝟎 𝑩𝑬𝟎 + 𝜷𝑹 𝒓
                                                                  𝑩𝑬         𝑽     𝑨             𝑩𝑪                         𝑽       𝑨       𝑩𝑪


Con 𝑟𝐵𝐸 , 𝐶𝐵𝐸 , 𝑟𝐵𝐶 , 𝐶𝐵𝐶 , 𝑔𝑚 , 𝑔𝐶𝐸 parametri differenziali del BJT definiti nel punto di lavoro, 𝑣𝐶𝐸 la tensione di uscita.
22- Modello ai piccoli segnali del MOSFET
      Ricordiamo le leggi della corrente tra drain e source nelle varie regioni di funzionamento del MOSFET:
                                                                         2 (1                  1
       - regione triodo (𝑉𝐷𝑆 ≤ 𝑉𝐺𝑆 − 𝑉𝑇 ): 𝐼𝐷𝑆 = β𝑛 [(𝑉𝐺𝑆 − 𝑉𝑇 )𝑉𝐷𝑆 − 2 𝑉𝐷𝑆 ] + λ𝑉𝐷𝑆 )
                                                                            β𝑛
       - regione saturazione (𝑉𝐷𝑆 > 𝑉𝐺𝑆 − 𝑉𝑇 ): 𝐼𝐷𝑆 =                            (𝑉𝐺𝑆 − 𝑉𝑇 )2(1 + λ𝑉𝐷𝑆 )
                                                                             2
       Con 𝑉𝑇 = 𝑉𝑇0 + γ(√2ψ𝐹 + 𝑉𝑆𝐵 − √2ψ𝐹 ) .

       Procedo con la linearizzazione della corrente rispetto alle tensioni sui tre terminali:
                                               d𝐼               d𝐼                 d𝐼
                                   𝑖𝐷𝑆 = d𝑉𝐷𝑆 | 𝑣𝐺𝑆 + d𝑉𝐷𝑆 | 𝑣𝐷𝑆 + d𝑉𝐷𝑆 | 𝑣𝑆𝐵                      →   𝑖𝐷𝑆 = 𝑔𝑚 𝑣𝐺𝑆 + 𝑔𝐷𝑆 𝑣𝐷𝑆 + 𝑔𝑚𝐵 𝑣𝑆𝐵
                                                    𝐺𝑆 𝑄             𝐷𝑆 𝑄               𝑆𝐵 𝑄


       Dove:
               𝑑𝐼
       𝑔𝑚 = 𝑑𝑉𝐷𝑆 |
                    𝐺𝑆 𝑄


               𝑑𝐼
       𝑔𝐷𝑆 = 𝑑𝑉𝐷𝑆 |
                    𝐷𝑆 𝑄


                d𝐼            𝑑𝐼            𝑑𝑉
       𝑔𝑚𝐵 = d𝑉𝐷𝑆 | = 𝑑𝑉𝐷𝑆| ⋅ 𝑑𝑉 𝑇 |                       dovuta all’effetto Body.
                     𝑆𝐵 𝑄          𝑇   𝑄       𝑆𝐵 𝑄


       Iniziamo calcolando 𝑔𝑚𝐵 ; notiamo che, indipendentemente dalla regione di funzionamento in cui ci troviamo, la legge
       𝑑𝐼𝐷𝑆       𝑑𝐼
       𝑑𝑉𝑇 𝑄
            | = − 𝑑𝑉𝐷𝑆 | vale sempre, di conseguenza:
                     𝐺𝑆 𝑄

                                                                                     ∂𝐼𝐷𝑆     ∂𝑉𝑇
                                                                       𝒈𝒎𝑩 = −            | ⋅     | = −𝒈𝒎 ⋅ 𝜶
                                                                                     ∂𝑉𝐺𝑆 𝑄 ∂𝑉𝑆𝐵 𝑄
                      𝑑𝑉                   γ
       Con α = 𝑑𝑉 𝑇 | =                                .
                       𝑆𝐵 𝑄        2√2ψ𝐹 +𝑉𝑆𝐵0

       Continuiamo con il calcolo di 𝑔𝑚 𝑒 𝑔𝐷𝑆 , essi dipenderanno dalla regione di funzionamento:
       - regione triodo:
                                   1 2
       𝐼𝐷𝑆 = 𝛽𝑛 [(𝑉𝐺𝑆 − 𝑉𝑇 )𝑉𝐷𝑆 − 𝑉𝐷𝑆    ] (1 + 𝜆𝑉𝐷𝑆 )
                                   2
                                                                            𝒅𝑰𝑫𝑺
                                                                 𝒈𝒎 =            | = 𝛃𝒏 (𝟏 + 𝛌𝑽𝑫𝑺𝟎 )𝑽𝑫𝑺𝟎
                                                                            𝒅𝑽𝑮𝑺 𝑸

                                                      𝐝𝑰𝑫𝑺                                             𝛌𝑰𝑫𝑺𝟎
                                           𝒈𝑫𝑺 =           | = 𝛃𝒏 (𝑽𝑮𝑺𝟎 − 𝑽𝑻 − 𝑽𝑫𝑺𝟎 )(𝟏 + 𝛌𝑽𝑫𝑺𝟎 ) +
                                                      𝐝𝑽𝑫𝑺 𝑸                                        (𝟏 + 𝛌𝑽𝑫𝑺𝟎 )

       - regione saturazione:

               𝛽𝑛
       𝐼𝐷𝑆 =      (𝑉 − 𝑉𝑇 )2(1 + 𝜆𝑉𝐷𝑆 )
               2 𝐺𝑆
                                                                            𝒅𝑰𝑫𝑺
                                                                 𝒈𝒎 =            | = 𝛃𝒏 (𝑽𝑮𝑺𝟎 − 𝑽𝑻 )(𝟏 + 𝛌𝑽𝑫𝑺𝟎 )
                                                                            𝒅𝑽𝑮𝑺 𝑸

                                                                      𝒅𝑰𝑫𝑺      𝛃𝒏                  𝛌𝑰𝑫𝑺𝟎
                                                             𝒈𝑫𝑺 =         | = 𝛌 (𝑽𝑮𝑺𝟎 − 𝑽𝑻 )𝟐 =
                                                                      𝒅𝑽𝑫𝑺 𝑸    𝟐                (𝟏 + 𝛌𝑽𝑫𝑺𝟎 )

       So che a livello statico la corrente 𝐼𝐺 = 0 → 𝑖𝐺 = 0 → il gate
       risulterà isolato.

       Gli effetti reattivi sono già stati studiati in precedenza, basterà
       aggiungere le capacità al circuito equivalente di piccolo segnale.
       Ci saranno 𝐶𝐺𝑆 e 𝐶𝐺𝐷 che agiscono sul terminale di gate, 𝐶𝑆𝐵 se non
       suppongo 𝑉𝑆𝐵 = 0 tra source e bulk, 𝐶𝐺𝐷 e 𝐶𝐷𝐵 per quanto riguarda il
       terminale di drain.
23- Funzioni di rete del BJT con studio in frequenza

       Il BJT è un tripolo che, come abbiamo già visto in precedenza, può
       essere rappresentato tramite il circuito equivalente qui a fianco.




       Notiamo come questo circuito sia molto simile ad un altro circuito
       notevole già studiato in precedenza, chiamato circuito π, del quale è già
       stata calcolata la matrice ammettenza utilizzando alcune proprietà:



       Partendo da qua possiamo adattare la matrice al circuito di Giacoletto-Johnson riportato in precedenza ponendo:
                                                  1                                  1                  1
                                           𝑌1 = 𝑟      + 𝑠𝐶𝐵𝐸          𝑌2 = 𝑟                      𝑌3 = 𝑟 + 𝑠𝐶𝐵𝐶
                                                  𝐵𝐸                                 𝐶𝐸                 𝐵𝐶


       Suppongo il BJT sempre in regione normale, di conseguenza la giunzione B-C sempre in inversa, dato che per la realizzazione di
       amplificatori è questa la regione più adatta: 𝑟𝐵𝐶 → ∞ .
       Per tutti i calcoli che seguono inoltre ipotizzeremo che in ingresso ci sia un generatore ideale di corrente → 𝑌𝐺 = 0
       Otteniamo così la seguente matrice ammettenza:




       Utilizzando le formule per il calcolo delle funzioni di rete calcoliamo l’impedenza in ingresso:
                                                                        𝑦𝑟 𝑦𝑓         𝑦𝑟 𝑦𝑓
                                                          𝑌𝐼𝑁 = 𝑦𝑖 −           = 𝑦𝑖 −
                                                                       𝑦𝑜 + 𝑌𝐶         𝑦𝑜
                                                                 𝑦
                                                            −1 = 𝑜
                                                    𝑍𝐼𝑁 = 𝑌𝐼𝑁                   con 𝐷𝑦 = 𝑦𝑖 𝑦𝑜 − 𝑦𝑓 𝑦𝑟
                                                                𝐷 𝑌

                                                                                  1
                                                            𝑦                        +𝑠𝐶𝐵𝐶
                                                   −1 = 𝑜 =                      𝑟𝐶𝐸
                                         → 𝑍𝐼𝑁 = 𝑌𝐼𝑁              1                1
                                                       𝐷     𝑌   (𝑟 +𝑠𝐶𝐵𝐸 +𝑠𝐶𝐵𝐶)(𝑟 +𝑠𝐶𝐵𝐶)+(𝑔𝑚 −𝑠𝐶𝐵𝐶)𝑠𝐶𝐵𝐶
                                                                   𝐵𝐸             𝐶𝐸


       Formula complicata che posso semplificare ipotizzando 𝑦𝑟 = −𝑠𝐶𝐵𝐶 ≈ 0 → 𝑦𝑟 ⋅ 𝑦𝑓 ≈ 0 :

                                              1
                                             𝑟𝐶𝐸 + 𝑠𝐶𝐵𝐶                                 1                      𝑟𝐵𝐸
                          𝑍𝐼𝑁 ≈                                             =                       =
                                    1                  1                           1                  1 + 𝑠𝑟𝐵𝐸 (𝐶𝐵𝐸 + 𝐶𝐵𝐶 )
                                  (𝑟 + 𝑠𝐶𝐵𝐸 + 𝑠𝐶𝐵𝐶 ) (𝑟 + 𝑠𝐶𝐵𝐶 )                 (𝑟 + 𝑠𝐶𝐵𝐸 + 𝑠𝐶𝐵𝐶 )
                                    𝐵𝐸                 𝐶𝐸                          𝐵𝐸

       Da questa funzione di trasferimento possiamo desumere che l’impedenza in ingresso sia una funzione passa basso con un polo:
                                                                       1
                                                         𝑝=−
                                                               𝑟𝐵𝐸 (𝐶𝐵𝐸 + 𝐶𝐵𝐶 )
       All’aumentare della frequenza quindi, l’impedenza di ingresso si abbassa, questo rende il BJT non adatto all’utilizzo come
       amplificatore di tensione.

       Calcoliamo ora l’impedenza in uscita:
                                                                                              𝑦𝑟 𝑦𝑓
                                                           𝑌𝑂𝑈𝑇 = 𝑍𝑂𝑈𝑇 −1 = 𝑦𝑜 −
                                                                                               𝑦𝑖

       Anche in questo caso otteniamo un’espressione complicata ma possiamo utilizzare la stessa semplificazione fatta in
       precedenza ed ottenere:
                                                                                 1             𝑟
                                                         → 𝑍𝑂𝑈𝑇 ≈           1
                                                                                          = 1+𝑠𝑟𝐶𝐸 𝐶
                                                                       (𝑟       +𝑠𝐶𝐵𝐶 )         𝐶𝐸 𝐵𝐶
                                                                        𝐶𝐸


       Questa funzione di trasferimento risulta essere, come nel caso dell’impedenza in ingresso una funzione passa basso, con un
                      1
       polo 𝑝 = − 𝑟           .
                     𝐶𝐸 𝐶𝐵𝐶
All’aumentare della frequenza l’impedenza di uscita si abbassa, questa è una proprietà che rende il BJT un buon amplificatore di
corrente.

Una volta dimostrato come il BJT sia un buon amplificatore di corrente calcoliamo il guadagno di corrente 𝐴𝐼𝑐𝑐 di questo
amplificatore, dato che stiamo calcolando il guadagno di cortocircuito poniamo YC = ∞ :

                                                                                           𝐶 𝑟
             𝑦𝑓      (𝑔𝑚 − 𝑠𝐶𝐵𝐶 )      𝑔𝑚 𝑟𝐵𝐸 − 𝑠𝐶𝐵𝐶 𝑟𝐵𝐸   β0 − 𝑠𝐶𝐵𝐶 𝑟𝐵𝐸             1 − 𝑠 𝐵𝐶 𝐵𝐸
                                                                                             β0
      𝐴𝐼𝐶𝐶 =    =                    =                   =                  = β0
             𝑦𝑖 ( 1 + 𝑠𝐶 + 𝑠𝐶 ) 1 + 𝑠𝑟𝐵𝐸 (𝐶𝐵𝐸 + 𝐶𝐵𝐶 ) 1 + 𝑠𝑟𝐵𝐸 (𝐶𝐵𝐸 + 𝐶𝐵𝐶 )      1 + 𝑠𝑟𝐵𝐸 (𝐶𝐵𝐸 + 𝐶𝐵𝐶 )
                  𝑟𝐵𝐸     𝐵𝐸      𝐵𝐶


Notiamo come siano presenti sia un polo che uno zero nella funzione di
trasferimento:
                                  1                   β0
                     𝑝 = −𝑟                    𝑧=𝑟
                             𝐵𝐸 (𝐶𝐵𝐸 +𝐶𝐵𝐶 )          𝐵𝐸 𝐶𝐵𝐶


Il guadagno di corrente in banda passante sarà quindi pari a β0 , a frequenze
più alte calerà.

Per ω < 𝜔𝐵 sono in banda passante, finché mi trovo in questa regione gli
effetti reattivi sono considerati trascurabili, di conseguenza posso continuare
ad usare il modello di Ebers-Moll e considerare il sistema come quasi-
stazionario, per frequenze più alte questo modello non risulta preciso.
                                                                  DIGITALE

24- Potenza dinamica in una porta logica: come si calcola (integrale… , tensione di swing), “switching activity”

       La potenza dissipata da un ordinario circuito può essere calcolata come:

                                                                     𝑃 = 𝑉𝐶𝐶 𝐼𝐶𝐶
       dove 𝑉𝐶𝐶 è la tesione di alimentazione e la 𝐼𝐶𝐶 è la corrente assorbita.
       Alla potenza totale contribuiscono due fattori, la potenza statica e quella dinamica. Nel caso delle porte logiche CMOS la
       componente statica è nulla dato che si suppone consumo di corrente pari a 0 nei momenti di non commutazione.
       La potenza dinamica è quindi l’unico fattore che contribuisce e per ottenerne la formula iniziamo calcolando l’energia
       consumata per ogni commutazione dell’output:
                          ∞                    ∞         𝑑𝑉𝑂𝑈𝑇               𝑉𝑂𝐻
                  𝐸 = ∫ 𝑉𝐶𝐶 𝐼𝐶𝐶 (𝑡) 𝑑𝑡 = ∫ 𝑉𝐶𝐶 𝐶𝐿              𝑑𝑡 = 𝑉𝐶𝐶 𝐶𝐿 ∫ 𝑑𝑉𝑂𝑈𝑇 = 𝑉𝐶𝐶 𝐶𝐿 (𝑉𝑂𝐻 − 𝑉𝑂𝐿 ) = 𝑉𝐶𝐶 𝐶𝐿 𝑉𝑠𝑤𝑖𝑛𝑔
                         0                    0           𝑑𝑡                𝑉𝑂𝐿

       dove 𝐶𝐿 è la capacità del carico in uscita, 𝑉𝑂𝐻 e 𝑉𝑂𝐿 sono le tensioni nominali che codificano rispettivamente un’uscita positiva
       (1) o negativa (0), la differenza tra i due corrisponde al salto di tensione che avviene in uscita ad ogni commutazione 𝑉𝑠𝑤𝑖𝑛𝑔 .
                                                                                           𝐸
       Una volta calcolata l’energia è semplice ottenere la potenza sapendo che 𝑃 = 𝑡 = 𝐸 ⋅ 𝑓 :

                                                             𝑃𝑑𝑖𝑛 = 𝑉𝐶𝐶 𝐶𝐿 𝑉𝑠𝑤𝑖𝑛𝑔 𝑓0→1

       𝑓0→1 è detta frequenza di commutazione (switching activity), essa rappresenta la frequenza con cui avvengono le commutazioni.
       La frequenza di commutazione a sua volta dipende dalla frequenza di clock e dalla probabilità che, in ogni periodo, l’uscita della
       porta cambi stato:
                                                             𝑓0→1 = 𝑓𝐶𝐾 𝑃0→1
       dove 𝑓𝐶𝐾 è appunto la frequenza di clock e 𝑃0→1 è la probabilità che l’uscita della porta cambi stato. Ovviamente, essendo
       l’output funzione degli ingressi, 𝑃0→1 verrà ricavata a partire dalle probabilità dei singoli simboli in ingresso e dalla funzione
       implementata dalla porta logica .

       Supponendo che 𝑉𝑂𝐻 = 𝑉𝐶𝐶 e che 𝑉𝑂𝐿 = 0 si semplifica la formula ottenuta in precedenza (𝑉𝑠𝑤𝑖𝑛𝑔 = 𝑉𝐶𝐶 ):
                                                                  2
                                                       𝑃𝑑𝑖𝑛 = 𝑉𝐶𝐶   𝐶𝐿 𝑓0→1


25- Quando si parla di self loading, caratteristiche delle porte statiche CMOS
       Per il calcolo del self loading di una porta CMOS è necessario considerare tutti i contributi capacitivi sul nodo di uscita.
       Supponendo di analizzare una porta NAND a 𝑚 ingressi che pilota 𝑘 ingressi a valle:
       - FAN IN = 𝑚
       - FAN OUT = 𝑘
       - tutti i gate a valle caratterizzati dalla stessa 𝐶𝑖𝑛𝑣
       - capacità di interconnessione costante 𝐶𝑊

       Alla capacità sul nodo di uscita contribuiranno le k capacità di ingresso dei gate a valle, la
       capacità 𝐶𝑊 dell’interconnessione, un singolo n-MOSFET dato che nel PD sono disposti in
       serie ed m p-MOSFET dato che nel PU sono disposti in parallelo. Notiamo che la struttura è
       molto simile a quella dell’inverter, con l’unica differenza che in questo caso sarà necessario
       caricare m n-MOSFET anziché uno, di conseguenza, utilizzando le formule per il calcolo della capacità totale in uscita
       dell’inverter:

       𝐶𝐿 = 𝐶𝐺𝐷𝑒𝑞 + 𝐶𝐷𝐵𝑒𝑞 + 𝐶𝑊 + 𝐶𝑖𝑛𝑣
                                           1
          = 𝐶𝑊 + 𝐶𝑖𝑛𝑣 + (𝑊𝑛 + 𝑊𝑝 ) (2𝐶𝐺𝑆0 + 𝐿𝑀𝐼𝑁 𝐶𝑂𝑥 𝑅𝐷𝐷 + 𝐾𝑒𝑞 𝐿𝑆 𝐶𝑗0 )
                                           2
       Adattando quindi queste formule alla porta in analisi si ottiene:
                                                     1
       𝐶𝐿 = 𝑘𝐶𝑖𝑛𝑣 + 𝐶𝑊 + (𝑊𝑛 + 𝑚𝑊𝑝 ) (2𝐶𝐺𝑆0 + 𝐿𝑀𝐼𝑁 𝐶𝑂𝑥 𝑅𝐷𝐷 + 𝐾𝑒𝑞 𝐿𝑆 𝐶𝑗0)
                                                     2
                                    1                                          1
          = 𝑘𝐶𝑖𝑛𝑣 + 𝐶𝑊 + 𝑊𝑛 (2𝐶𝐺𝑆0 + 𝐿𝑀𝐼𝑁 𝐶𝑂𝑥 𝑅𝐷𝐷 + 𝐾𝑒𝑞 𝐿𝑆 𝐶𝑗0 ) + 𝑚𝑊𝑝 (2𝐶𝐺𝑆0 + 𝐿𝑀𝐼𝑁 𝐶𝑂𝑥 𝑅𝐷𝐷 + 𝐾𝑒𝑞 𝐿𝑆 𝐶𝑗0 )
                                    2                                          2
                                       𝑉           𝑊                   𝑊
       Con 𝑅𝐷𝐷 = 1 − 𝑉 𝑇 , 𝑆𝑛 = 𝐿 𝑛 ed 𝑆𝑝 = 𝐿 𝑝 = α𝑁𝐴𝑁𝐷 𝑆𝑛 ottengo:
                                       𝐷𝐷              𝑀𝐼𝑁               𝑀𝐼𝑁


                                                                  𝑪𝑳 = 𝒌𝑪𝒊𝒏𝒗 + 𝑪𝑾 + 𝑺𝒏 (𝟏 + 𝒎𝛂𝑵𝑨𝑵𝑫 )𝑪𝒑𝟏
                                                   1
       Dove 𝐶𝑝1 = 𝐿𝑀𝐼𝑁 (2𝐶𝐺𝑆0 + 2 𝐿𝑀𝐼𝑁 𝐶𝑂𝑥 𝑅𝐷𝐷 + 𝐾𝑒𝑞 𝐿𝑆 𝐶𝑗0 ) è la capacità sul nodo di uscita dovuta ad un transistore di area
       minima 𝑊 = 𝐿 = 𝐿𝑀𝐼𝑁 .


26- Pilotaggio di grandi capacità
        In questa analisi supporremo sempre 𝑡𝑟 = 𝑡𝑓 → 𝛼 = ε
        Come suggerisce la formula del tempo di propagazione del segnale in una porta logica la performance è affetta dalla capacità di
        carico 𝐶𝐿 collegata al nodo di uscita che, più è consistente, più tende a rallentare la porta:
                                                                          2𝐶𝐿         𝑉𝑇    𝐶𝐿 2𝐶𝑖𝑛         𝑉𝑇
                                                                𝑡𝑝 =              𝐹(     )=    ⋅        𝐹(     )
                                                                       β𝑛 ’𝑆𝑛 𝑉𝐷𝐷    𝑉𝐷𝐷    𝐶𝑖𝑛 β′𝑛 𝑉𝐷𝐷    𝑉𝐷𝐷
       Supponendo transistor ad area minima (→ 𝑆𝑛 = 1) pongo:
                 2C                𝑉
       𝑡𝑝0 = β ’𝑉in 𝐹 (𝑉 𝑇 ) che rappresenta il tempo di propagazione di un inverter caricato da un altro inverter identico.
                  𝑛     𝐷𝐷         𝐷𝐷
            𝐶
       𝑋 = 𝐶 𝐿 il tempo di ritardo dipende linearmente da questo coefficiente, che esprime quanto grande è la capacità in uscita. Se
             𝑖𝑛
       l’inverter è connesso ad una lunga linea di interconnessione oppure ad un pin di uscita del circuito integrato mi aspetterò
       𝑋 = 103 ÷ 104 .
       Per poter pilotare grandi capacità senza che il tempo di ritardo aumenti troppo sarà necessario inserire un eventuale buffer del
       quale calcoleremo il dimensionamento di seguito.
       Il tempo di ritardo dipenderà dal dimensionamento del buffer, svolgeremo
       l’analisi in modo da trovare il dimensionamento ottimo che minimizza il
       tempo di ritardo.
       Iniziamo considerando il primo inverter ad area minima, di conseguenza
       𝐶𝑖𝑛 = (1 + ε)𝐶𝑀1 , il secondo inverter sarà invece il buffer con
       dimensionamento dell’n-MOSFET pari ad 𝑆:
                                                                                𝐶
                                   Cin2 = S(1 + ε)CM1 = SCin → 𝑆 = 𝐶𝑖𝑛2
                                                                                    𝑖𝑛
       Il ritardo totale può essere approssimato con la somma dei ritardi dei
       singoli inverter:
                                                   𝐶𝑖𝑛2      𝐶𝐿               𝐶𝑖𝑛2   𝐶𝐿                𝐶𝐿 𝐶𝑖𝑛                 𝑋
                         𝑡𝑝 = 𝑡𝑝1 + 𝑡𝑝2 =               ⋅𝑡 +    ⋅ 𝑡 = 𝑡𝑝0 ⋅ (      +    ) = 𝑡𝑝0 ⋅ (𝑆 +    ⋅     ) = 𝑡𝑝0 ⋅ (𝑆 + )
                                                   𝐶𝑖𝑛 𝑝0 𝐶𝑖𝑛2 𝑝0             𝐶𝑖𝑛 𝐶𝑖𝑛2                 𝐶𝑖𝑛 𝐶𝑖𝑛2               𝑆
       il dimensionamento del buffer è totalmente descritto da S, avendo trovato il tempo di ritardo in sua funzione procediamo
                             𝑑𝑡𝑝
       annullando                  così da trovare il minimo:
                             𝑑𝑆
                                                                    𝑑𝑡𝑝                  𝑋
                                                                          = 𝑡𝑝0 ⋅ (1 − 𝑆 2 ) = 0 → 𝑆𝑜𝑝𝑡 = √𝑋
                                                                    𝑑𝑆
                                                                                                           𝐶
                                                                       → 𝑡𝑝,𝑂𝑝𝑡 = 2𝑡𝑝0 ⋅ √𝑋 = 2𝑡𝑝0 ⋅ √𝐶 𝐿
                                                                                                            𝑖𝑛

       Osserviamo come in questo caso il tempo di ritardo dipenda linaremente da √𝑋 anziché da 𝑋 come nel caso senza buffer.
       Nel caso in cui 𝑋 risultasse essere molto grande però rischio comunque di arrivare ad avere ritardi elevati, di conseguenza posso
       inserire ulteriori buffer, lo studio che segue avrà come obiettivo di trovare il numero ottimo di buffer da aggiungere al fine di
       minimizzare il 𝑡𝑝 .
       Tra il primo inverter e la capacità di carico metto altri
       𝑁 − 1 buffer, essi avranno dimensionamento crescente
       in modo che le dimensioni del successivo siano 𝑈 volte
       quelle del precedente, così facendo il rapporto tra le
       capacità di uscita e quelle di ingresso restano sempre
       pari ad 𝑈:
       𝐶2 = 𝑈𝐶1 ; 𝐶3 = 𝑈𝐶2 = 𝑈 2𝐶1 ; ecc...
       Ottengo quindi:
             𝐶
       𝑡𝑝𝑖 = 𝐶𝑖+1 ⋅ 𝑡𝑝0 = 𝑈 ⋅ 𝑡𝑝0 con 𝑖 = {1, … , 𝑁 − 1}
                    𝑖
                𝐶                          𝐶
       𝑡𝑝𝑁 = 𝐶 𝐿 ⋅ 𝑡𝑝0 = 𝑈 𝑁−1𝐿 𝐶 ⋅ 𝑡𝑝0                 (tutti i tempi di ritardo sono uguali a parte l’ultimo stadio che vede 𝐶𝐿 in uscita)
                  𝑁                            1
       Si dimostra facilmente (non so come) che il caso ottimo si verifica quando tutti i tempi di ritardo sono uguali → 𝑡𝑝𝑖 = 𝑡𝑝𝑁 .
                                                                                        𝐶
                                                                                     ln(𝐶 𝐿 )
                    𝐶                           𝐶                                                 ln 𝑋
       𝑈 ⋅ 𝑡𝑝0 = 𝑈 𝑁−1𝐿 𝐶 ⋅ 𝑡𝑝0 → 𝑈 = 𝑈 𝑁−1𝐿 𝐶 → 𝐶𝐿 = 𝑈 𝑁 𝐶1 = 𝑈 𝑁 𝐶𝑖𝑛 → 𝑁𝑜𝑝𝑡 =          𝑖𝑛
                                                                                                = ln 𝑈
                          1                         1                                  ln 𝑈

       Trovato 𝑁𝑜𝑝𝑡 è possibile calcolare 𝑡𝑝 :
                                               ln 𝑋
       𝑡𝑝 = ∑ 𝑡𝑝𝑖 = 𝑁𝑜𝑝𝑡 ⋅ 𝑈 ⋅ 𝑡𝑝0 =                ⋅ 𝑈 ⋅ 𝑡𝑝0
                                               ln 𝑈
       Trovato il numero di buffer da inserire calcoliamo ora il dimensionamento ottimo annullando la derivata di 𝑡𝑝 :
                                          𝑑𝑡𝑝         ln 𝑋             ln 𝑋           ln 𝑋         1
                                              = 𝑡𝑝0 ⋅      − 𝑡𝑝0 ⋅ U          = 𝑡𝑝0 ⋅      ⋅ (1 −      )=0
                                          𝑑𝑈          ln 𝑈           𝑈(ln 𝑈)2         ln 𝑈        ln 𝑈
       → 𝑼𝒐𝒑𝒕 = 𝒆
                   𝐥𝐧 𝑿                  𝑪
       → 𝑵opt = 𝐥𝐧 𝑼 = 𝐥𝐧 𝑿 = 𝐥𝐧 (𝑪 𝑳 )
                                          in
       → 𝒕𝒑,Opt = 𝑵opt ⋅ 𝑼opt ⋅ 𝒕𝒑𝟎 = 𝐥𝐧(𝑿) ⋅ 𝒆 ⋅ 𝒕𝒑𝟎

       In questo caso notiamo come il tempo di ritardo dipenda logaritmicamente da X.


       L’utilizzo dei buffer riduce notevolmente il tempo
       di ritardo, la tabella affianco riassume quello
       che abbiamo calcolato precedentemente.




27- Il tempo di commutazione nelle logiche pass-transistor, che approccio per il suo calcolo approssimato si è usato
         Il calcolo del tempo di commutazione nelle logiche a pass-transistor è più complicato rispetto alle logiche statiche, sarà di
         conseguenza necessario adottare un approccio approssimato che sia per lo meno in grado di riflettere le dipendenze rispetto al
         dimensionamento e al numero dei transistor.
         Segue l’analisi nel caso di pass transistor complementari:
         supponiamo di dover trasferire un “1” → 𝐴 = 𝐵 = 𝑉𝐷𝐷 .
         Posso individuare tre fasi della transizione di 𝑉𝑋 da 0 → 𝑉𝐷𝐷 in cui i due mosfet sono in
         regioni di funzionamento diverse:
         - 𝑉𝑋 ≤ |𝑉𝑇𝑝0 | → entrambi in saturazione.
         - |𝑉𝑇𝑝0 | < 𝑉𝑋 ≤ 𝑉𝐷𝐷 − 𝑉𝑇𝑛 (𝑋) → n-MOSFET in saturazione; p-MOSFET in triodo.
         - 𝑉𝑋 > 𝑉𝐷𝐷 − 𝑉𝑇𝑛 (𝑋) → n-MOSFET spento; p-MOSFET triodo.
       Per fare un esempio studiamo il secondo caso:
                                           2
            𝑑𝑉𝑋                           𝑉𝐷𝑆𝑝    β𝑛
       𝐶𝑋       = β𝑝 [(𝑉𝐺𝑆𝑝 − 𝑉𝑇𝑝 )𝑉𝐷𝑆𝑝 −      ] + (𝑉𝐺𝑆𝑛 − 𝑉𝑇𝑛 )2
             𝑑𝑡                            2      2
                                                  (𝑉𝑋 − 𝑉𝐷𝐷 )2    β𝑛                     2
                = β𝑝 [(−𝑉𝐷𝐷 − 𝑉𝑇𝑝0 )(𝑉𝑋 − 𝑉𝐷𝐷 ) −              ] + (𝑉𝐷𝐷 − 𝑉𝑋 − 𝑉𝑇𝑛 (𝑉𝑋 ))
                                                       2          2

       Questa risulta essere un’equazione troppo complicata che rappresenta la corrente solo in parte del transitorio. La situazione si
       complica ulteriormente se teniamo conto della dipendenza di 𝑉𝑇𝑛 da 𝑉𝑋 a causa dell’effetto Body.
       Alla soluzione precedente si preferisce spesso una soluzione semplificata che sostituisce il pass transistor con
       una resistenza equivalente indipendente dalle tensioni dei nodi A e X.
       Si può dimostrare che 𝑅𝑒𝑞 dipende poco da 𝑉𝑋 , per questo è possibile considerarla circa costante.
       Essendo 𝑅𝑒𝑞 ≈ 𝑐𝑜𝑠𝑡𝑎𝑛𝑡𝑒 procediamo con il calcolo nel caso più semplice, cioè nel caso in cui 𝑉𝑋 = 0 ed
       entrambi i MOSFET sono in saturazione:
                                𝑉𝐷𝐷                    𝑉𝐷𝐷                                   2𝑉𝐷𝐷
       𝑅𝑒𝑞 (𝑉𝑋 = 0) =                =                                    =
                              𝐼𝑛 + 𝐼𝑝 β𝑛                  β 𝑝           2                   2
                                                                            β𝑛 (𝑉𝐷𝐷 − 𝑉𝑇𝑛0 ) + β𝑝 (𝑉𝐷𝐷 − |𝑉𝑇𝑝0 |)
                                                                                                                 2
                                         (𝑉𝐺𝑆𝑛 − 𝑉𝑇𝑛0)2 + (𝑉𝐺𝑆𝑝 − 𝑉𝑇𝑝0 )
                                       2                   2
       Utilizzando la formula per la carica di una capacità tramite una resistenza mi ricavo il transitorio esponenziale della tensione 𝑉𝑋 :

                                                                                    𝑡
                                                         𝑉𝑋 = 𝑉𝐷𝐷 [1 − exp (−            )]
                                                                                  𝑅𝑒𝑞 𝐶𝑋

       Da cui ricavo il tempo di carica al 90% dell’escursione, per farlo pongo 𝑉𝑋 = 0.9𝑉𝐷𝐷 e risolvo per 𝑡:

                                                        𝑡𝑟,𝑋 = ln 10 ⋅ 𝑅𝑒𝑞 𝐶𝑋 ≈ 2.3 ⋅ 𝑅𝑒𝑞 𝐶𝑋



28- Dinamiche CMOS, il problema della cascata a blocchi
       A differenza delle logiche statiche o a pass transistor le logiche dinamiche CMOS eliminano la
       ridondanza tra PU e PD, di conseguenza necessitano di un numero inferiore di MOSFET.

       Per poter utilizzare solo il PD (blocco Φ𝑛 ) (o solo il PU → blocco Φ𝑝 ) è necessario introdurre un
       ulteriore segnale detto di clock (Φ) che mi permette di “attivare” e “disattivare” il PD. Il clock
       andrà a scandire, tramite l’utlizzo di due ulteriori MOSFET (𝑀𝑛 e 𝑀𝑝 in figura), l’alternanza di due
       fasi, quella di PRE-CARICA (Φ = 0 → 𝑀𝑛 OFF, 𝑀𝑝 ON) (pre-scarica nel caso di Φ𝑝 ) dove il PD
       sarà disattivato e la capacità di carico 𝐶𝐿 verrà caricata, e quella di VALUTAZIONE (Φ = 1 → 𝑀𝑛
       ON, 𝑀𝑝 OFF) dove il PD verrà attivato e, in base all’output descritto dalla funzione implementata
       permetterà a 𝐶𝐿 di scaricare (‘0’ in out) o di rimanere carico (‘1’ in out).
       La fase di valutazione sarà anche l’unico momento in cui sarà consentito leggere l’output della porta dato che nel periodo di pre-
       carica non è garantito che l’uscita rifletta il risultato della funzione logica implementata.
       Per quanto riguarda i tempi di ritardo di una porta con questa architettura ci sarà bisogno di fare una valutazione separata per le
       due fasi e sommare i risultati. Il tempo di pre-carica o pre-scarica si calcola facilmente dato che si tratta semplicemente del
       tempo di carica di un condensatore attraverso un inverter, il tempo di valutazione invece, dipende dall’uscita della funzione.
       Siccome il nodo di uscita (nel caso di una rete Φ𝑛 ) partirà sempre carico, nel caso in cui la funzione richieda un ‘1’ in uscita il
       tempo di ritardo sarà nullo, nel caso contrario il ritardo verrà calcolato, come per le logiche statiche, tramite il metodo del
       dimensionamento equivalente del PD, dato che si tratta semplicemente della scarica di un condensatore attraverso i MOSFET
       del PD (ed 𝑀𝑛 ).

       Il vantaggio di questa architettura è che non c’è mai un percorso conduttivo tra 𝑉𝐷𝐷 e massa, per questo avrò potenza statica
       nulla e corrente di cortocircuito inesistente. Al contrario la potenza dinamica è più alta rispetto alle altre architetture dato che la
       pre-carica mi porta sempre l’uscita a ‘1’, di conseguenza il condensatore 𝐶𝐿 viene caricato ad ogni ciclo di clock.
       Un’altra criticità di questa architettura la troviamo quando colleghiamo più porte in cascata. In questo caso rischio che il
       rallentamento del transitorio in uscita dalla prima mi porti ad una scarica (o carica) parziale del 𝐶𝐿 nella successiva.
       Valutando i vari casi notiamo come un blocco Φ𝑛 sia in grado di accettare senza grosse ripercussioni una variazione lenta del
       tipo 0 → 1 dato che questa mi causerebbe soltanto un rallentamento della scarica a terra. Al contrario una variazione lenta del
       tipo 1 → 0 è pericolosa siccome, inizialmente, manderebbe in conduzione gli n-MOSFET della porta successiva con una
       conseguente scarica parziale del 𝐶𝐿 , successivamente, quando la tensione scende abbastanza per spegnere gli n-MOSFET la
       scarica di 𝐶𝐿 si arresta in una zona intermedia non ben definita che mi lascia in output una tensione che non codifica nessuna
       informazione. Un blocco Φ𝑝 , al contrario è in grado di accettare transizioni lente del tipo 1 → 0 e non è in grado di accettare
       transizioni lente del tipo 0 → 1 .
       Notiamo inoltre che un blocco Φ𝑛 in uscita causerà soltanto transizioni del tipo 1 → 0 siccome esso assume di default la
       condizione con uscita ad 1, un blocco Φ𝑝 sarà il contrario.
       Quindi, un blocco Φ𝑛 è in grado di accettare soltanto transizioni lente del tipo 0 → 1 ma è in grado di produrre solo transizioni del
       tipo 1 → 0, questo rende impossibile metterli in cascata senza separarli con un inverter.

       La cascata di blocchi Φ𝑛 separati da un inverter si chiama logica dinamica domino.

       Oppure posso utilizzare le logiche dinamiche np-CMOS che alternano un blocco Φ𝑛 e un blocco Φ𝑝 dato che le transizioni lente
       che produce il blocco Φ𝑛 sono proprio quelle che può tollerare il blocco Φ𝑝 e viceversa.
29- Vantaggi e svantaggi fra le porte dinamiche e statiche CMOS
       Non esiste uno stile circuitale definitivo che sia perfetto in tutte le applicazioni, ogni stile ha i suoi pro ed i suoi contro, per questo
       è importante, in base all’applicazione, scegliere accuratamente lo stile più adeguato.
       La tabella di seguito riassume i vantaggi e gli svantaggi delle varie famiglie logiche studiate fino ad ora:




       Le principali figure di merito che si valutano per scegliere la giusta famiglia logica sono:
          - immunità ai disturbi
          - velocità
          - consumo di potenza
          - occupazione d’area
       In base all’applicazione, vengono valutate con più o meno peso.

       Un aspetto importante che negli ultimi anni ha assunto sempre più importanza è la predisposizione di una certa architettura ad
       essere progettata tramite programmi T-CAD. In questo aspetto le logiche CMOS statiche eccellono, per questo al giorno d’oggi
       sono largamente utilizzate nei sistemi digitali.
Figura 1: ringrazio ChatGPT per la collaborazione
