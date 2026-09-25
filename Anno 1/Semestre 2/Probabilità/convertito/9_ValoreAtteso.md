---
fonte: "9_ValoreAtteso.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

La funzione generatrice dei momenti

           • Data una v.c. X, la sua funzione generatrice dei momenti
             (f.g.m.) è la funzione reale con argomento t ∈ IR

                                          mX (t) = E et X
                                                            


               ovvero
                                    X
                                    
                                    
                                        et x pX (x)        se X è discreta
                            mX (t) = Zx ∞
                                    
                                    
                                         et x fX (x)dx     se X è continua
                                        −∞


           • La f.g.m. esiste se la sommatoria o l’integrale sono finiti in un
             intervallo aperto che contiene lo zero, ovvero del tipo
             (−t0 , t0 ), con t0 > 0.

a.a 2024/2025 — R. Bellio                                                        1/ 7
                            Proprietà della f.g.m.

       La f.g.m. (che nel caso continuo è simile alla trasformata di Fourier
       della funzione di densità) gode di alcune importanti proprietà:
          1. Il comportamento della funzione nel punto 0 è rilevante

                                  mX (0) = 1
                                  m′X (0) = E(X)
                                  m′′X (0) = E(X 2 )
                                      ...       ...
                                  (n)
                                 mX (0)     = E(X n )

          2. Non è detto che la f.g.m. esista, ma se esiste determina la
             distribuzione, ovvero è in corrispondenza 1:1 con la funzione
             di ripartizione di X (e quindi con pX o fX );


a.a 2024/2025 — R. Bellio                                                       2/ 7
                               Proprietà della f.g.m.

          3. Se X e Y sono indipendenti, si ottiene

                                 mX+Y (t) = mX (t) mY (t) .

               Più inP
                      generale: se X1 , . . . , Xn sono indipendenti, e
               Sn = ni=1 Xi
                                                  Yn
                                   mSn (t) =         mXi (t) ,
                                                i=1

               e se le Xi hanno tutte la stessa distribuzione

                                     mSn (t) = (mX (t))n .


       Commento: la proprietà 1. dà il nome al metodo (e a volte è
       utile), ma le proprietà importanti sono la 2. e la 3.

a.a 2024/2025 — R. Bellio                                                 3/ 7
                                  Alcune f.g.m. notevoli

                       Distribuzione di X       mX (t)          Definita per

                             Bi(n, p)       (1 − p + et p)n       ∀t ∈ IR


                                                     t
                              P(λ)             eλ (e −1)          ∀t ∈ IR


                                                    1     2 2
                            N (µ, σ 2 )       eµ t+ 2 σ t         ∀t ∈ IR


                                                         α           1
                                                    1
                            Ga(α, 1/β)            1−t β           t<
                                                                       β




a.a 2024/2025 — R. Bellio                                                      4/ 7
                                    Applicazioni notevoli
       Usando le proprietà della f.g.m. si possono ottenere molti risultati
       sulle v.c.
           • Otteniamo la f.g.m. di X + Y , con X ∼ P(λ1 ) e Y ∼ P(λ2 ),
             indipendenti
           • dalla proprietà 3. (e usando la tabella) si ottiene
                                                                  t     t
                            mX+Y (t) = mX (t) mY (t) = eλ1 (e −1) eλ2 (e −1) ,
                                                              t
                                       mX+Y (t) = e(λ1 +λ2 ) (e −1)
           • Si riconosce la f.g.m. di una distribuzione P(λ1 + λ2 ), e allora
             dalla proprietà 2. segue che

                                         X + Y ∼ P(λ1 + λ2 )

           • Il risultato si estende ad una somma di un numero qualsiasi di
             v.c. di Poisson indipendenti.
a.a 2024/2025 — R. Bellio                                                        5/ 7
                                      Applicazioni notevoli


           • Si procede in maniera analoga per trovare la distribuzione della
             somma di v.c. normali, Gamma (con lo stesso parametro di
             scala β) o binomiali (con lo stesso parametro p) indipendenti.
           • Analogamente, si ottiene la distribuzione di trasformazione
             lineare di una v.c. normale: i passi sono i seguenti
                  ▶ Sia X ∼ N (µ, σ 2 ) e Y = a + b X, con a, b ∈ IR
                  ▶ Si ottiene facilmente che
                                                                                 2 2   2
                            mY (t) = E[e(a+b X) t ] = ea t mX (b t) = e(a+b µ)t+b t σ /2 ,

                      e si riconosce la f.g.m. di una distribuzione N (a + b µ, b2 σ 2 ),
                      per cui
                                            Y ∼ N (a + b µ, b2 σ 2 ) .




a.a 2024/2025 — R. Bellio                                                                    6/ 7
                            Applicazioni notevoli (continua)
           • Un’altra applicazione notevole è quella per ottenere la
             distribuzione di una combinazione lineare di v.c. normali
             indipendenti.
           • Anche il teorema del limite centrale si dimostra utilizzando la
             f.g.m.: se X1 , . . . , Xn sono i.i.d. con E(Xi ) = µ e
             V (Xi ) = σ 2 , si può verificare che la f.g.m. della v.c.

                                             X −µ
                                        Zn = q
                                                  σ2
                                                  n

               tende alla f.g.m. di una N (0, 1) per n → ∞.
           • Un altro risultato è che se X ∼ N (µ, σ 2 ), allora
                                                      1 2
                                  mX (1) = E eX = eµ+ 2 σ
                                               


               è la media di Y = eX con distribuzione lognormale(µ, σ 2 ).
a.a 2024/2025 — R. Bellio                                                      7/ 7
                   Introduzione all’inferenza statistica:
                campionamento e distribuzioni campionarie




a.a 2024/2025 — R. Bellio                                   1/ 28
                               Inferenza Statistica

           • Il punto di partenza di una indagine statistica è costituito da
             un insieme (la popolazione di riferimento), che costituisce
             l’ambito di interesse;
           • gli elementi di questo insieme (persone, componenti
             elettronici, titoli azionari,. . . ) vengono indicati come unità
             statistiche;
           • sono disponibili dei dati, ovvero delle misurazioni/rilevazioni di
             certe caratteristiche di interesse, ottenuti per una parte delle
             unità statistiche (il campione, da cui indagini campionarie);
           • una descrizione delle caratteristiche del campione è in genere
             ottenuta mediante tecniche di statistica descrittiva;
           • l’inferenza statistica utilizza i dati del campione per fare
             delle affermazioni sulle caratteristiche di tutta la popolazione.


a.a 2024/2025 — R. Bellio                                                         2/ 28
      campione. Le variabili di interesse sarebbero in questo
      caso   rilevate
      Lo schema           solamente
                    qui sotto           sulle cinque
                              cerca di esemplificare     unità statistiche
                                                      la situazione. Le       che
      variabili di interesse sono rilevate solamente sulle unità statistiche
      fanno parte del campione. Nonostante le informazio-
      che fanno parte del campione.
      ni sulla popolazione siano incomplete in un problema
      di  inferenza
      Nonostante          siamo però
                     le informazioni sulla ambiziosi:      conincomplete,
                                           popolazione siano     le informazio-
                                                                           in
      ni   rilevatedi inferenza
      un problema         sul solosi è campione
                                        però ambiziosi:vogliamo      “produrre”
                                                         con le informazioni
      rilevate sul solo campione l’obiettivo è arrivare a conclusioni su
      affermazioni su tutta la popolazione.
       tutta la popolazione !




a.a 2024/2025 — R. Bellio                                                     3/ 28
                    Motivazione per le indagini campionarie



           • tempo e/o costo

           • la popolazione di interesse può essere infinita e virtuale

           • la rilevazione “distrugge” le unità statistiche e quindi,
             dopo una rilevazione esaustiva, la popolazione di partenza non
             interessa più perché non esiste più!

           • precisione dei risultati: a volte rilevazioni campionarie
             (incomplete) portano a risultati più precisi di rilevazioni
             esaustive.




a.a 2024/2025 — R. Bellio                                                     4/ 28
                      Relazione tra popolazione e campione

           • Supponiamo che la popolazione di riferimento siano i pezzi
             prodotti da svariati macchinari in un certo periodo di tempo,
             che sono presenti nel magazzino di una ditta . . .
           • . . . e che si sia interessati a conoscere il loro peso medio ma,
             per far presto, si voglia pesare solamente 10 pezzi.
           • Il primo problema diventa come scegliere i dieci pezzi da
             misurare; due possibilità veloci sono:
                 A) scegliere completamente a caso 10 dei pezzi presenti, e
                    misurare il loro peso;
                 B) scegliere 10 pezzi a caso tra quelli più “semplici”da prendere
                    (ad esempio, considerando un gruppo di 10 pezzi posti vicino
                    all’entrata del magazzino).



a.a 2024/2025 — R. Bellio                                                             5/ 28
           • In ambedue i casi, alla fine si ottengono 10 numeri (le 10
             misurazioni del peso). Però per stimare il peso medio di tutti i
             pezzi presenti non è possibile utilizzare questi numeri nella
             stessa maniera nei due casi A) e B).
                  ▶ Nel primo caso posso pensare di stimare il peso medio
                    utilizzando la media aritmetica delle 10 misurazioni fatte. Se
                    non si è stati particolarmente sfortunati, i pezzi provengono da
                    macchinari diversi ed è plausibile che la media delle dieci
                    misure “cada vicino”al peso medio di tutti.
                  ▶ Nel secondo caso però occorre cautela: potremmo aver scelto
                    pezzi prodotti tutti da un solo macchinario che produce pezzi
                    con peso medio leggermente più basso, ed ottenere cosı̀ un
                    valore troppo basso.

               Quello che cambia nei due casi è la relazione tra la
               popolazione e il campione.


a.a 2024/2025 — R. Bellio                                                               6/ 28
                            Campione casuale semplice
       L’esempio descrive la differenza tra un campione casuale
       semplice, che è rappresentativo della popolazione, e un
       campione di convenienza, che non lo è. Anche se è abbastanza
       intuitivo che il secondo non sia molto affidabile, purtroppo è spesso
       utilizzato nella pratica.

       Un campione casuale semplice (c.c.s.) è un metodo per selezionare
       unità da una popolazione in maniera tale che ogni unità abbia la
       stessa possibilità di far parte del campione.
         • Per ottenere un c.c.s. occorre scegliere le unità totalmente
            a caso.
         • La scelta delle unità può avvenire con reinserimento oppure in
            blocco;
         • per popolazioni infinite (o molto numerose), campionare con
            reinserimento o in blocco non porta a differenze sostanziali.
       D’ora in poi si assumerà sempre di disporre di un c.c.s., estratto
       con reinserimento (esistono però schemi più sofisticati).
a.a 2024/2025 — R. Bellio                                                       7/ 28
         L’indagine campionaria comporta sempre un errore

       Per rendere utili le affermazioni fatte riguardo la popolazione è
       necessario cercare di quantificare il margine d’errore.

       Esempio. Supponiamo di sperimentare un nuovo farmaco su 20
       pazienti e che solo uno di questi 20 pazienti mostri effetti secondari
       indesiderati. Sembra naturale allora stimare la probabilità che il
       farmaco induca effetti tossici rilevanti come pari al 5%.

       In questo caso la popolazione di riferimento è data da tutti i
       pazienti a cui potremmo pensare di somministrare il farmaco sotto
       analisi. È una popolazione virtuale e teoricamente infinita.

       È chiaro che non è possibile affermare che la percentuale di tutti i
       possibili pazienti che potrebbero presentare problemi di tossicità sia
       esattamente uguale al 5%: è importante allora chiedersi di quanto
       potrebbe essere differente (ovvero quale sia l’entità dell’errore).

a.a 2024/2025 — R. Bellio                                                        8/ 28
                            Inferenza statistica e Probabilità


       L’idea alla base dell’inferenza statistica si concretizza nel descrivere
       la relazione tra la popolazione e il campione utilizzando il calcolo
       delle probabilità.

       Nella sostanza, si interpretano i risultati sperimentali (ovvero i dati
       disponibili) come uno dei tanti risultati che un meccanismo
       probabilistico (un esperimento casuale) poteva fornire.

       Una conseguenza importante è che è possibile utilizzare in maniera
       naturale il calcolo delle probabilità per quantificare l’errore
       campionario.




a.a 2024/2025 — R. Bellio                                                         9/ 28
              Ipotesi fondamentale per l’inferenza statistica

       L’ipotesi fondamentale nell’inferenza statistica è che i dati
       campionari osservati, denotati anche con

                                  y = (y1 , . . . , yn ) ,

       siano la realizzazione di n variabili casuali Y1 , . . . , Yn .

       Questo tiene conto del fatto che abbiamo estratto uno tra i molti
       possibili campioni, ovvero della presenza di variabilità
       campionaria. (L’ipotesi non sarebbe necessaria se potessimo
       osservare tutta la popolazione!)

       Nel caso di un campione casuale semplice, le n v.c. che si suppone
       abbiano generato i dati sono variabili casuali indipendenti e
       identicamente distribuite (i.i.d.)


a.a 2024/2025 — R. Bellio                                                   10/ 28
                            Inferenza statistica parametrica

       La distribuzione assunta per le singole variabili dipende dalla
       natura dei dati. Ad esempio, per dati binari sarà naturale ipotizzare
       Yi ∼Bernoulli(p), per misurazioni Yi ∼ N (µ, σ 2 ), per conteggi
       Yi ∼ P(λ), per tempi di guasto Yi ∼ Ga(α, 1/β) (o Weibull), etc.

       In ogni caso, la distribuzione assunta per le v.c. del campione
       dipenderà da ignote costanti dette parametri, vale a dire le
       quantità p, µ, σ 2 , α, β . . .

       I parametri entrano nella definizione della distribuzione delle
       variabili del campione Y1 , . . . , Yn . Nell’inferenza statistica
       parametrica si assume che la distribuzione delle v.c. del campione
       sia nota a meno dei valori dei parametri, che corrispondono
       tipicamente agli aspetti di interesse dell’analisi.


a.a 2024/2025 — R. Bellio                                                       11/ 28
                            Modello statistico parametrico

       Le assunzioni viste vanno allora a definire un modello statistico
       parametrico per i dati del campione.

       Riassumendo, l’idea di base è che i dati siano stati generati dalle
       v.c. Y1 , . . . , Yn , dove:
          1. le variabili Yi sono indipendenti;
          2. tutte le Yi hanno la stessa distribuzione di probabilità;
          3. tale distribuzione è nota a meno dei valori di uno o più
             parametri, indicati genericamente come θ = (θ1 , . . . , θd ),
             d ≥ 1.

       Scopo dell’inferenza statistica è utilizzare i dati del campione per
       ottenere informazioni su θ, i cui elementi sono valori di un certo
       insieme Θ (spazio parametrico).


a.a 2024/2025 — R. Bellio                                                      12/ 28
         Modello statistico parametrico: alcune osservazioni


           • I tre punti citati rappresentano delle assunzioni, che non è
             detto siano necessariamente soddisfatte nella pratica.
           • In ogni caso, tali ipotesi possono essere considerate al più una
             descrizione semplice ed operativamente utile di una realtà
             complessa, quindi ci possiamo accontentare di una validità
             almeno approssimata.
           • Esistono comunque metodi per trattare dati con una certa
             struttura di dipendenza (come le serie storiche), o per
             prescindere dalla conoscenza della forma della distribuzione (i
             metodi non parametrici). Essi comunque sono un’estensione
             dei metodi della statistica parametrica.




a.a 2024/2025 — R. Bellio                                                        13/ 28
                      Statistiche e distribuzioni campionarie
       Si chiama statistica (campionaria) ogni funzione dei dati, che
       viene usata per sintetizzare opportunamente il campione

                                 T = t(Y1 , . . . , Yn ) .

       Sono esempi di statistiche gli indici utilizzati nella statistica
       descrittiva
                     Y , S 2 , la mediana campionaria, . . . . ,
       e occorre sempre distinguere tra la v.c. che rappresenta la
       statistica e il valore che tale statistica assume in un particolare
       campione osservato.

       Tipicamente, è di interesse determinare la distribuzione di alcune
       statistiche di interesse, ovvero la loro distribuzione campionaria.
       A tal fine, si utilizzano i metodi probabilistici sviluppati per le
       funzioni di n v.c. indipendenti.

a.a 2024/2025 — R. Bellio                                                    14/ 28
                            Distribuzioni campionarie



       Vedremo in sintesi alcuni risultati per variabili casuali indipendenti
       (con molti richiami a risultati visti in dettaglio in lezioni passate), e
       in particolare:
         A) Risultati per variabili qualsiasi.
         B) Risultati per variabili bernoulliane.
         C) Risultati per variabili Poisson.
         D) Risultati per variabili normali.




a.a 2024/2025 — R. Bellio                                                          15/ 28
                A) Richiami sulle somme di variabili casuali



           • Y1 , . . . , Yn v.c. con E(Y1 ) = µ1 , . . . , E(Yn ) = µn

                            ⇒ E(Y1 + . . . + Yn ) = µ1 + . . . + µn .


           • Y1 , . . . , Yn v.c indipendenti con V (Y1 ) = σ12 , . . . , V (Yn ) = σn2

                            ⇒ V (Y1 + . . . + Yn ) = σ12 + . . . + σn2 .




a.a 2024/2025 — R. Bellio                                                                 16/ 28
                A) Richiami sulle somme di variabili casuali

       Una conseguenza importante dei risultati appena visti riguarda la
       variabile casuale media campionaria
                                                n
                                             1X
                                     Y =        Yi
                                             n
                                               i=1


           • Se Y1 , . . . , Yn sono v.c. indipendenti con E(Yi ) = µ e
             V (Yi ) = σ 2 , allora
                                        n
                                        X E(Yi )          µ
                              E(Y ) =                =n     = µ,
                                                n         n
                                       i=1
                                       n
                                       X     V (Yi )   σ2   σ2
                            V (Y ) =             2
                                                     =n 2 =    .
                                               n       n    n
                                       i=1




a.a 2024/2025 — R. Bellio                                                  17/ 28
                            A) La v.c. varianza campionaria

       Nel caso di variabili i.i.d., con E(Yi ) = µ e V (Yi ) = σ 2 , ci sono dei
       risultati anche per variabile casuale varianza campionaria
                                                n
                                           1    X
                                 S2 =             (Yi − Y )2
                                        (n − 1)
                                               i=1


           • Se Y1 , . . . , Yn sono v.c. indipendenti con E(Yi ) = µ e
             V (Yi ) = σ 2 , allora

                                          E(S 2 ) = σ 2
                                                           
                                     2      2 2     2     κ
                                 V (S ) = (σ )          +     ,
                                                   n−1 n

               con κ costante che dipende dalla distribuzione (0 per Yi
               normali, ma non in generale).

a.a 2024/2025 — R. Bellio                                                           18/ 28
                            A) Teorema del limite centrale
       Teorema Sia Y1 , Y2 , . . . una successione di v.c. indipendenti,
       ciascuna con E(Yi ) = µ e V (Yi ) = σ 2 . Allora, posto
             √
       Zn = n(Y − µ)/σ, per ogni z
                                            Z z
                                         1           2
                  lim P (Zn ≤ z) = √             e−t /2 dt = Φ(z) .
                 n→∞                     2π −∞

       In simboli il teorema del limite centrale (t.l.c.) si denota scrivendo
                                     √ (Y − µ) D
                              Zn =    n       −→ N (0, 1),
                                          σ
                  D
       dove −→ si legge “converge in distribuzione”.

       Una lettura pratica del teorema del limite centrale è la seguente:
                                            σ2
                                              
                                   a
                                Y ∼ N µ,         ,
                                             n
                a
       dove ∼ significa “distribuita approssimativamente”.
a.a 2024/2025 — R. Bellio                                                       19/ 28
                    A) Teorema del limite centrale: utilizzo
       Il t.l.c. permette di approssimare la distribuzione di Y , o, in
       maniera equivalente, della somma di n v.c. i.i.d.
                              n
                                       a
                              X
                                    Yi ∼ N n µ, n σ 2 .
                                                     

                              i=1

       Si tratta di un risultato molto utile, del tipo chiamato per grandi
       campioni, nel senso che l’approssimazione è migliore per
       dimensioni campionarie elevate. Più precisamente, quanto deve
       essere grande n dipende dalla distribuzione della popolazione:
          • se il campione proviene da una distribuzione quasi simmetrica,
            l’approssimazione è buona già per piccoli valori di n;
          • se la distribuzione è molto asimmetrica, è necessario un valore
            di n abbastanza grande;
          • per la maggior parte delle distribuzioni, un campione di
            numerosità 30 (o più) è sufficientemente elevato affinché
            l’approssimazione normale sia adeguata.
a.a 2024/2025 — R. Bellio                                                       20/ 28
                       B) Risultati per variabili bernoulliane

       Se consideriamo n v.c. bernoulliane Yi ∼Bernoulli(p), i = 1, . . . , n,
       indipendenti, si ottiene facilmente che
                                  n
                                  X
                                         Yi ∼ Bi(n, p) ,
                                   i=1

       Per n elevato è più semplice utilizzare il t.l.c., che permette di
       approssimare la binomiale con la normale. .

       Al crescere di n, la distribuzione di una v.c. binomiale di parametri
       n e p si “avvicina” sempre di più a quella di una normale con
       parametri µ = np e σ 2 = np(1 − p).

       L’approssimazione è ritenuta buona se n p > 5 e n (1 − p) > 5
       (eventualmente utilizzando correzioni di continuità (±0.5), che
       migliorano l’approssimazione normale per v.c. discrete).

a.a 2024/2025 — R. Bellio                                                        21/ 28
                                     n=10, p=0.2                                  n=20, p=0.2




                      0.30




                                                                   0.20
                                                                   0.15
                      0.20
                 fd




                                                              fd

                                                                   0.10
                      0.10




                                                                   0.05
                      0.00




                                                                   0.00
                             0   2     4        6    8   10               0   5       10    15   20

                                           k                                           k




                                     n=40, p=0.2                                  n=80, p=0.2
                      0.15




                                                                   0.08
                      0.10
                 fd




                                                              fd

                                                                   0.04
                      0.05
                      0.00




                                                                   0.00




                             0   10        20       30   40               0   20      40    60   80

                                           k                                           k

a.a 2024/2025 — R. Bellio                                                                             22/ 28
                            C) Risultati per variabili Poisson

       Se Yi ∼ P(λi ), i = 1, . . . , n, indipendenti, allora
                                n               n
                                                     !
                              X                X
                                     Yi ∼ P        λi .
                                   i=1            i=1

       In
       Pnparticolare, per v.c. i.i.d. (dove λi = λ) si ottiene
          i=1 Yi ∼ P(n λ). Anche in questo caso, tuttavia, il t.l.c. è
       spesso utilizzato, ovvero
                                   n
                                            a
                                   X
                                         Yi ∼ N (n λ, n λ) .
                                   i=1

       L’approssimazione è ritenuta buona se n λ > 10.



a.a 2024/2025 — R. Bellio                                                 23/ 28
                            D) Risultati per variabili normali
       Per il caso Yi ∼ N (µ, σ 2 ), i = 1, . . . , n, indipendenti, esistono
       diversi risultati.

       Come caso particolare della proprietà che combinazioni lineari di
       normali indipendenti sono ancora normali, si ottiene

                                                σ2
                                                  
                               Y ∼ N µ,              ,
                                                n
                           X n
                               Yi ∼ N (n µ, n σ 2 ) ,
                                  i=1

       senza alcuna approssimazione!

       Altri risultati richiedono preliminarmente la definizione di due
       distribuzioni collegate alla normale, ovvero la distribuzione
       chi-quadrato e la distribuzione t di Student.

a.a 2024/2025 — R. Bellio                                                       24/ 28
                                   La distribuzione chi-quadrato
       La somma di n v.c. normali standard indipendenti elevate al
       quadrato ha distribuzione chi-quadrato con n gradi di libertà, in
       simboli χ2n . Ovvero, se Zi ∼ N (0, 1), i = 1, . . . , n, indipendenti,
                                     Xn
                                 Y =     Zi2 ∼ χ2n
                                                    i=1
       La distribuzione è un caso particolare di distribuzione Gamma, con
       α = n/2 e β = 2, e allora si trova E(Y ) = n e V (Y ) = 2 n.

                                               Funzione di densità
                                    0.15




                                                               n=5
                                                               n=10
                                                               n=20
                                    0.10
                            f(y)

                                    0.05
                                    0.00




                                           0   10    20   30    40    50
a.a 2024/2025 — R. Bellio                                                        25/ 28
                                   La distribuzione t di Student
       Date due v.c. indipendenti, Z ∼ N (0, 1) e X ∼ χ2n , allora
                                        Z
                                 Y =p         ,
                                        X/n
       ha distribuzione t di Student con n gradi di libertà, Y ∼ tn .
       Molto simile alla normale standard, a cui tende rapidamente al
       crescere di n, con E(Y ) = 0 e V (Y ) = n/(n − 2).

                                               Funzione di densità
                                    0.4
                                    0.3




                                                                 n=5
                                                                 n=10
                                                                 n=100
                            f(y)

                                    0.2
                                    0.1
                                    0.0




                                          !6   !4   !2   0   2   4   6

                                                         y
a.a 2024/2025 — R. Bellio                                                26/ 28
                  Altri risultati per la distribuzione normale


           • Per la varianza campionaria, vale
                         Pn              2
                           i=1 (Yi − Y )     (n − 1) S 2
                                           =             ∼ χ2n−1 .
                                σ2               σ2
           • Y e S 2 sono v.c. indipendenti.

           • Media campionaria standardizzata e media campionaria
             studentizzata
                            Y −µ                  Y −µ
                            r    ∼ N (0, 1) ,     r    ∼ tn−1 .
                              σ2                    S2
                              n                     n




a.a 2024/2025 — R. Bellio                                            27/ 28
                 Un risultato per due campioni indipendenti



       Se X1 , . . . , XnX e Y1 , . . . , YnY rappresentano due c.c.s. tra loro
       indipendenti, con Xi ∼ N (µX , σX        2 ) e Y ∼ N (µ , σ 2 ), allora
                                                       i        Y   Y
       utilizzando la proprietà che combinazioni lineari di v.c. sono
       normali si ottiene
                                          
                                                      σX2   σY2
                                                                
                         X − Y ∼ N µ X − µY ,             +       ,
                                                      nX    nY

       con il risultato che vale in maniera approssimata (via t.l.c.) nel
       caso di medie campionarie di campioni non normali.




a.a 2024/2025 — R. Bellio                                                         28/ 28
                     Stima puntuale e controllo del modello




a.a 2024/2025 — R. Bellio                                     1/ 26
                            I problemi dell’inferenza statistica

       Utilizzando il campione osservato y = (y1 , . . . , yn ), alla luce del
       modello statistico parametrico prescelto, si vogliono ricavare
       informazioni sul parametro ignoto θ ∈ Θ. I principali problemi
       inferenziali sono suddivisibili in tre classi:
           • stima puntuale: si vuole ottenere, sulla base dei dati del
             campione y, un valore numerico per θ;
           • stima intervallare: si vuole ottenere, sulla base dei dati del
             campione y, un sottoinsieme di Θ in cui è plausibilmente
             incluso θ;
           • verifica di ipotesi: data una congettura o un’ipotesi su θ, si
             vuole verificare, sulla base dei dati del campione y, se essa è
             accettabile, cioè in accordo con i dati osservati.



a.a 2024/2025 — R. Bellio                                                        2/ 26
                                Stima puntuale



       Ipotizziamo allora di aver specificato un modello statistico
       parametrico per i dati del campione, ovvero una distribuzione di
       probabilità per Yi che indichiamo genericamente con p(yi ; θ),
       funzione di probabilità o di densità.

       L’obiettivo della stima puntuale è utilizzare i dati per ottenere un
       valore plausibile del parametro, ovvero una sua stima.

       In molti casi, esiste un modo abbastanza intuitivo per ottenere una
       stima di θ.




a.a 2024/2025 — R. Bellio                                                      3/ 26
        Esempio: frazione campionaria di elementi difettosi
       Si analizzano n = 40 elementi, scelti a caso tra quelli prodotti da
       un certo macchinario. Il campione osservato è

                     y = (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

                            0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0) ,
       dove 0 e 1 indicano, rispettivamente, se l’oggetto è o non è
       conforme agli standard di qualità.

       In questo caso è naturale assumere Yi ∼ Bernoulli(p), con
       p ∈ (0, 1), perciò nel caso specifico θ = p e Θ = (0, 1).
       La media campionaria y, ossia la frazione campionaria di
       elementi difettosi, è una stima naturale di p. Con 3 difettosi su
       40 si ottiene
                                      3
                                pb =    = 0.075 .
                                     40

a.a 2024/2025 — R. Bellio                                                                   4/ 26
                       Esempio: peso di scatole di prodotto
       Una macchina produce scatole di un certo prodotto di peso
       nominale 1 Kg., ma in realtà aventi distribuzione N (µ, σ 2 ).

       Si vuole stimare il peso medio effettivo e la varianza sulla base di
       un campione casuale semplice di n = 20 pezzi.

       Dopo l’estrazione del campione si ottiene

                            y = 1.007 Kg ,   s = 0.0027 Kg .

       Appare naturale porre µ           b2 = 0.00272 = 7.29 × 10−6 .
                             b = 1.007 e σ

       Per valutare la proporzione di scatole comprese nell’intervallo
       1 ± 0.01, si utilizzano poi le consuete formule per la normale,
       ovvero
                                                     
                    1.01 − 1.007           0.99 − 1.007
               Φ                     −Φ                   = 0.867 .
                        0.0027                0.0027

a.a 2024/2025 — R. Bellio                                                     5/ 26
                                Stime e stimatori
       La stima di un parametro è definita come un valore numerico
       ottenuto dai dati osservati del campione y1 , . . . , yn .

       Si definisce stimatore di un parametro di interesse una variabile
       casuale funzione delle v.c. Y1 , . . . , Yn che generano i valori
       osservati (quindi lo stimatore è una statistica e la stima ne è il
       valore osservato con i dati).

       In generale, se θ è parametro di interesse, si denota con θb sia la
       stima θ(y
             b 1 , . . . , yn ) che lo stimatore θ(Y
                                                 b 1 , . . . , Yn ), è poi il
       contesto a rendere chiarire a quale delle due ci si riferisce.

       Due punti importanti:
           • Dato uno stimatore, come posso stabilire se si tratta di un
             buon stimatore ? (Proprietà di uno stimatore).
           • Come posso reperire un buon stimatore? (Metodi di stima)

a.a 2024/2025 — R. Bellio                                                        6/ 26
                            Proprietà di uno stimatore
       Si considera il comportamento dello stimatore al variare del
       campione, ovvero la vicinanza della sua distribuzione al valore del
       parametro. Due definizioni:
          • E(θb − θ) è la distorsione di θ;
                                           b
                  b = E[(θb − θ)2 ] è l’errore quadratico medio di θ.
           • EQM (θ)                                                b
       La loro espressione è una funzione del parametro θ e della
       dimensione campionaria n.

       Si parla allora di
           • Stimatore non distorto: ha distorsione nulla, cioè E(θ)
                                                                   b = θ.
           • Stimatore consistente (in media quadratica): al crescere
             della dimensione campionaria
                                          b → 0.
                                     EQM (θ)


a.a 2024/2025 — R. Bellio                                                    7/ 26
                                  Consistenza
       Mentre la non distorsione è una proprietà desiderabile, la
       consistenza è un requisito necessario per uno stimatore
       ragionevole. Vale infatti
                                                       2
                     EQM (θ)b = V (θ)   b + E(θ)  b −θ ,

                                = varianza + (distorsione)2 .
       La condizione di consistenza equivale allora a
                               
                                lim E(θ)
                                        b = θ,
                                 n→∞
                                lim V (θ)
                                        b = 0.
                                  n→∞

       In pratica si richiede che lo stimatore sia non distorto (almeno per
       n → ∞) e che la sua varianza diventi sempre più piccola, ossia la
       sua distribuzione si concentri sempre più attorno al valore θ.
       All’aumentare dell’informazione campionaria, sembra ragionevole
       richiedere che la conoscenza su θ diventi sempre più precisa.
a.a 2024/2025 — R. Bellio                                                     8/ 26
                            Precisione della stima
       Per confrontare due (o più) stimatori consistenti di uno stesso
       parametro, è sufficiente confrontare il loro errore quadratico medio:
       lo stimatore con EQM minore sarà preferibile.

       Se gli stimatori sono non distorti, il confronto si riduce a verificare
       quale stimatore ha la minor varianza a parità di numerosità del
       campione (e si parla allora di stimatore più efficiente tra quelli
       considerati).

       La radice della varianza di uno stimatore è detta errore standard
       (o talvolta incertezza)
                                        q
                                   σθb = V (θ)
                                             b ,

       e la sua valutazione con i dati del campione è detta errore
       standard stimato σ  bθb. L’errore standard stimato è generalmente
       utilizzato come misura della precisione di stima, ed è riportato
       assieme ad essa.
a.a 2024/2025 — R. Bellio                                                        9/ 26
                                          Esempi
           • Modello bernoulliano
             Se Yi ∼Bernoulli(p), uno stimatore di p è la media
             campionaria, cioè pb = Y . Si ottiene
                                                        p (1 − p)
                             E(b
                               p) = p ,       V (b
                                                 p) =             .
                                                            n
               Lo stimatore
                     p      è non distorto e consistente, e vale inoltre
               σpb = p (1 − p)/n.
               Con n = 40 e pb = 0.075, si ottiene σ
                                                   bpb = 0.0416.
           • Modello Poisson
             Se Yi ∼ P(λ), uno stimatore di λ è di nuovo la media
             campionaria, λ
                          b = Y . Si ottiene

                                                             λ
                                E(λ)
                                  b = λ,           V (λ)
                                                      b =      .
                                                             n
               Lo stimatore è non distorto e consistente.
a.a 2024/2025 — R. Bellio                                                   10/ 26
           • Modello normale
             Se Yi ∼ N (µ, σ 2 ), allora Y e S 2 sono due stimatori per µ e
             σ 2 . Si ottiene
                                                           σ2
                                E(Y ) = µ ,      V (Y ) =      ,
                                                            n
                                                          2 (σ 2 )2
                            E(S 2 ) = σ 2 ,    V (S 2 ) =           .
                                                          (n − 1)

               Entrambi gli stimatori sono non distorti e consistenti; il
               denominatore (n − 1) nella definizione di S 2 serve proprio ad
               ottenere la non distorsione.




a.a 2024/2025 — R. Bellio                                                       11/ 26
       Per lo stimatore alternativo (e più intuitivo) per la varianza
                                     Pn
                                2          (Yi − Y )2
                              b = i=1
                              σ
                                             n
       si ottiene
                            (n − 1) 2                (n − 1) 2 (σ 2 )2
                  σ2) =
                E(b                σ ,       σ2) =
                                          V (b              ·          ,
                               n                        n       n
       per cui si tratta comunque di uno stimatore consistente.




a.a 2024/2025 — R. Bellio                                                  12/ 26
                            Lo stimatore media campionaria
       In generale, dato un qualsiasi modello statistico parametrico, la
       media campionaria Y è sempre uno stimatore non distorto e
       consistente di µ = E(Yi ), dato che, se σ 2 = V (Yi )

                                                        σ2
                               E(Y ) = µ ,   V (Y ) =      .
                                                        n
       La consistenza della media campionaria va sotto il nome di legge
       dei grandi numeri. Inoltre, il teorema del limite centrale assicura
       che la distribuzione di Y è approssimativamente normale.

       Si noti inoltre che
                                             σ
                                        σY = √ .
                                              n

       In presenza di outliers, è preferibile utilizzare una media troncata,
       eliminando una percentuale (piccola) di dati. La media troncata è
       un esempio di stimatore robusto.
a.a 2024/2025 — R. Bellio                                                       13/ 26
                                Metodi di stima


       Esistono vari metodi di stima. In casi semplici, si utilizza il metodo
       dell’analogia, che ci porta a stimare la media con la media
       campionaria, la varianza con la varianza campionaria e cosı̀ via.

       Per situazioni generali, esistono vari metodi per reperire stimatori.

       Tra gli altri, citiamo il metodo della massima verosimiglianza,
       che per molti versi è quello preferibile, ed è utilizzato nei software
       statistici per stimare i parametri di distribuzioni quali la Gamma e
       la Weibull, e per modelli statistici più complessi.




a.a 2024/2025 — R. Bellio                                                         14/ 26
                            Controllo empirico del modello


       Alla luce dei dati disponibili y = (y1 , . . . , yn ), per procedere con i
       metodi dell’inferenza statistica parametrica è necessario specificare
       un modello per i dati, ovvero una distribuzione di probabilità per le
       variabili casuali indipendenti Y1 , . . . , Yn .
       In certi casi la specificazione (soprattutto per dati continui) può
       essere non banale, ed è allora necessario procedere ad un controllo
       empirico del modello.

       A tal fine, si utilizzano
           • Metodi della statistica descrittiva, come l’istogramma o la
             funzione di ripartizione empirica.
           • I grafici di probabilità.



a.a 2024/2025 — R. Bellio                                                           15/ 26
                            Controllo mediante istogramma


       L’istogramma nell’ambito inferenziale può essere interpretato come
       una stima della funzione di densità.
           • La stima è valida a prescindere da quale sia la vera
             distribuzione dei dati.
           • La stima è migliore per grandi campioni, cioè quando
             l’informazione campionaria aumenta.
       Il controllo si effettua confrontando l’istogramma con la funzione
       di densità del modello teorico, con i parametri del modello teorico
       rimpiazzati da opportune stime.




a.a 2024/2025 — R. Bellio                                                     16/ 26
                                  Esempio: PM (bassa quota)
       I dati sembrano avere una distribuzione asimmetrica: un modello
       adatto sembra essere la distribuzione Gamma, con αb = 2.03 e
       β = 1.82.
       b

                                                     Dati su scala originale


                                      0.20
                                      0.15
                            Densità

                                      0.10
                                      0.05
                                      0.00




                                             0   2       4     6      8        10   12

                                                               PM



a.a 2024/2025 — R. Bellio                                                                17/ 26
                                  Esempio: PM (bassa quota)
                                                                      √
       In alternativa, è possibile effettuare la trasformazione xi = 4 yi , e
       utilizzare un modello normale, con µ = x̄ e σ 2 = s2x .

                                                         Dati trasformati



                                      1.5
                                      1.0
                            Densità

                                      0.5
                                      0.0




                                            0.6   0.8   1.0   1.2        1.4   1.6   1.8   2.0

                                                                    PM




a.a 2024/2025 — R. Bellio                                                                        18/ 26
        Controllo mediante funzione di ripartizione empirica

       In maniera analoga, è possibile utilizzare la funzione di ripartizione
       empirica, definita come
                               n
                           1   X                  Numero di osservazioni ≤ x
                 Fbn (x) =           Ix (yi ) =                              ,
                           n                                  n
                               i=1

       dove Ix (yi ) è una opportuna funzione indicatrice
                                      (
                                       1        se yi ≤ x
                           Ix (yi ) =
                                       0        se yi > x

       La funzione di ripartizione empirica stima la vera funzione di
       ripartizione, quindi il controllo in questo caso si fa confrontandola
       con la funzione di ripartizione del modello teorico.


a.a 2024/2025 — R. Bellio                                                        19/ 26
                              Grafici di probabilità

       I grafici di probabilità (o carte di probabilità) consentono di
       confrontare la distribuzione ipotizzata per i dati (teorica) con i dati
       campionari. Sono la tecnica più comunemente utilizzata.

       Se F (·) indica la funzione di ripartizione
                                                 teorica, i grafici
                                                                 sono dei
       diagrammi di dispersione delle coppie F (yi ), Fn (yi ) , oppure
                                                        b
                                                             
       (equivalentemente) delle coppie F −1 (yi ), Fbn−1 (yi ) , i = 1, . . . , n.

       Anche in questo caso, occorre rimpiazzare i parametri del modello
       teorico con le stime ottenute dai dati.

       Se il modello teorico è corretto, i punti tenderanno ad essere
       allineati lungo una linea retta.



a.a 2024/2025 — R. Bellio                                                            20/ 26
                            Grafici di probabilità normali

       I grafici di probabilità si possono costruire per tutte le distribuzioni
       continue, però i più utilizzati sono i grafici delle probabilità
       normali, che consentono di confrontare i dati con il modello
       teorico normale.

       Si ottengono mediante un algoritmo in 3 passi
          1. Considero n valori equispaziati tra 0 e 1
                                      i − 0.5
                               pi =           ,   i = 1, . . . , n .
                                         n
          2. Rappresento con
                            un diagramma di dispersione le coppie
               −1
              Φ (pi ), y(i) .
          3. Se il modello normale è corretto, i punti tenderanno ad essere
             disposti lungo una linea retta.


a.a 2024/2025 — R. Bellio                                                          21/ 26
       Situazioni di allontamento dalla normalità possono aversi con
       asimmetria o code pesanti.


                                          Asimmetria                                                     Code pesanti
                            5




                                                                                         5
                            4




                                                                                         0
        Quantili empirici




                                                                     Quantili empirici
                            3




                                                                                         !5
                            2




                                                                                         !10
                            1




                                                                                         !15
                            0




                                !2   !1          0           1   2                             !2   !1          0           1   2

                                          Quantili teorici                                               Quantili teorici




a.a 2024/2025 — R. Bellio                                                                                                           22/ 26
                                            Esempio: PM (bassa quota)


                                        Dati su scala originale                                            Dati trasformati




                                                                                                1.8
                              10




                                                                                                1.6
                              8
        Quantili campionari




                                                                          Quantili campionari

                                                                                                1.4
                              6




                                                                                                1.2
                              4




                                                                                                1.0
                              2




                                                                                                0.8
                              0




                                   !2     !1          0           1   2                               !2   !1          0           1   2

                                               Quantili teorici                                                 Quantili teorici




a.a 2024/2025 — R. Bellio                                                                                                                  23/ 26
                       Esempio: contaminazione d’alluminio


       I dati si riferiscono ad un campione di n = 22 contaminazioni
       d’alluminio (ppm).

                            30    30    60    63    70    79    87
                            90    101   102   115   118   119   119
                            120   125   140   145   172   182
                            183   191   222   244   291   511


       Cerchiamo un modello che sia appropriato per questi dati,
       scegliendo tra le distribuzioni normale, lognormale, esponenziale e
       Weibull, costruendo i grafici di probabilità per ciascuna di queste
       distribuzioni.



a.a 2024/2025 — R. Bellio                                                     24/ 26
                             Normale                                    Lognormale
               500




                                                            500
               400




                                                            400
               300




                                                            300
        Dati




                                                     Dati
               200




                                                            200
               100




                                                            100
                        0    100        200    300                100     200        300   400

                            Quantili teorici                            Quantili teorici




       Il modello lognormale è più appropriato di quello normale. . .


a.a 2024/2025 — R. Bellio                                                                        25/ 26
                               Esponenziale                                              Weibull
               500




                                                                  500
               400




                                                                  400
               300




                                                                  300
        Dati




                                                           Dati
               200




                                                                  200
               100




                                                                  100
                     0   100   200     300     400   500                0   50   100         200          300

                                Quantili teorici                                       Quantili teorici




       . . . e fornisce un miglior adattamento ai dati anche rispetto ai
       modelli esponenziale e Weibull.

a.a 2024/2025 — R. Bellio                                                                                       26/ 26
          Soluzione degli esercizi di ripasso (versione 10/1/2024)

Avvertenza importante
Questo documento riporta le soluzioni sintetiche degli esercizi di ripasso per alcuni capitoli del testo di
Walpole et al. (2016), limitatamente ai quesiti per i quali la soluzione è numerica.
Visto che tali soluzioni non sono incluse nel materiale reso disponibile dalla casa editrice del testo, la loro
diffusione non infrange nessun diritto di copyright.

Cap. 2
  • Es. 2.52: 0.0005844
  • Es. 2.53: Soluzione grafica.

                  13
                        13 13 13
                   4     6
  • Es. 2.54:                52
                                  1   2
                                           =0.001959
                             13
  • Es. 2.55:
      (1) 0.054
      (2) 4/9
  • Es. 2.56: 13/120
  • Es. 2.57:
      (1) 7/25
      (2) 18/25
  • Es. 2.58:
      (1) 0.5515
      (2) 0.2941
  • Es. 2.59:
      (1) 0.0016
      (2) 0.1048
  • Es. 2.60:
      (1) 0.6312
      (2) 0.2841
      (3) 0.0847
  • Es. 2.61: P (Ing.1|E) = 0.5385, mentre P (Ing.2|E) = 0.4615, quindi è più probabile si sia trattato
    dell’Ing.1
  • Es. 2.62: 0.23
  • Es. 2.63: 1/4



                                                       1
  • Es. 2.64: 1/9

Cap. 3
  • Es. 3.30:
      (1) 0.3125
      (2) fY (y) = 12 y (1 − y)2 , per 0 < y < 1 (e 0 altrove)
      (3) 0.25
  • Es. 3.31:
      (1) fY (y) = e−y , per y > 0 (e 0 altrove)
             1
      (2)          = 0.0008263
            e6 3
  • Es. 3.32:
      (1) Basta sostituire alla formula i valori richiesti.
      (2) Soluzione grafica.
      (3) Basta calcolare le somme cumulate dei valori trovati al punto 1.
  • Es. 3.33: L’esercizio si risolve facilmente utilizzando la distribuzione binomiale, argomento del capitolo
    5.
  • Es. 3.34:
                       1 −x/50
      (1) fX (x) =        e    , x > 0 (e 0 altrove)
                       50
      (2) 0.2466
  • Es. 3.35: 0.2231
  • Es. 3.36:
      (1) Occorre risolvere l’integrale.
      (2) 0.0001
  • Es. 3.37:
      (1) fX1 = 2 (1 − x1 ), per 0 < x1 < 1 (e 0 altrove)
      (2) fX2 = 2 x2 , per 0 < x2 < 1 (e 0 altrove)
      (3) 0.2
                                1
      (4) fX1 |X2 (x1 |x2 ) =      , per 0 < x1 < x2 (e 0 altrove)
                                x2
  • Es. 3.38:
                       3 1
      (1) pX (x) =          , x = 0, 1, 2, . . .; risultato analogo vale per Y , e le due v.c. sono indipendenti.
                       4 4x
      (2) 63/64
  • Es. 3.39: 0.999991




                                                           2
Cap. 4
  • Es. 4.40: Non in programma.
  • Es. 4.41: 333
  • Es. 4.42: -2/75
  • Es. 4.43:
     (1) 900 (ore)
     (2) 1620000
          2
     (3) σX =810000, σX = 900.
  • Es. 4.45: 0
  • Es. 4.46:
     (1) 1/18 * 5000ˆ2 (si veda Es. 4.19)
     (2) Non in programma.
     (3) 0.81
  • Es. 4.47: 13000 $
  • Es. 4.48:
     (1) 33500 $
     (2) 39689 $
  • Es. 4.49:
    1., 2., 4., 5., 7.: immediate
     (3) La distribuzione condizionata di X1 dato X2 = 3 ha supporto (0,1,2,3,4) con rispettive probabilità
         (7/15, 3/15, 1/15, 3/15, 1/15)
     (4) 1.2
  • Es. 4.50: 6.55$
  • Es. 4.51:
     (1) 1/11
     (2) 10/11
     (3) 0.006887

Cap. 5
  • Es. 5.39:
     (1) 0.1710
     (2) 0.2832
  • Es. 5.40: 0.0308
  • Es. 5.41:
     (1) 0.000562
     (2) Non sembra credibile l’affermazione del produttore riguardo il tasso di difettosità del 5%, dato il
         valore molto basso della probabilità calcolata al punto 1.



                                                    3
  • Es. 5.42:
     (1) 0.2642
     (2) 0.0371
  • Es. 5.43:
     (1) 0.5177
     (2) 0.4914
  • Es. 5.44:
     (1) 6
     (2) 5.82
     (3) 0.0023
  • Es. 5.45:
     (1) 0.9277
     (2) 0.000981
     (3) 0.01
  • Es. 5.46: 0.4661
  • Es. 5.47: 0.1301
  • Es. 5.48:
     (1) 0.3633
     (2) Anche se il lotto contiene due difettosi, la probabilità di non accettare il lotto non è molto alta (è
         inferiore a 0.5). Per aumentarla si dovrebbero campionare più di n = 10 elementi; ad esempio, con
         n = 15 si ottiene P (X > 0) = ....
     (3) 0.4
  • Es. 5.49:
     (1) 0.008
     (2) 0.096
     (3) 0.896
  • Es. 5.50: 0.3351. L’approssimazione binomiale non è molto buona visto che n/N = 0.2 è troppo elevato.
  • Es. 5.51:
     (1) P (X ≥ 5) ≈ 0. Si tratta di un evento rarissimo, per cui l’affermazione non sembra corretta.
     (2) Anche con l’approssimazione con la distribuzione di Poisson si ha P (X ≥ 5) ≈ 0.

Cap. 6
  • Es. 6.31: 0.6086
  • Es. 6.32: 0.5768
  • Es. 6.33: 0.052
  • Es. 6.34:
     (1) 0.1056



                                                     4
      (2) 0.4013
  • Es. 6.35:
      (1) ≈ 0
      (2) 0.1587
      (3) 0.9270
  • Es. 6.36: 1-0.9772=0.0228
  • Es. 6.37: 1097.633
  • Es. 6.38:
      (1) Si verifica che f (y) ≥ 0 e il suo integrale tra 0 e 1 vale 1.
      (2) 0.410 =0.0001
      (3) α = 1, β = 10
      (4) 0.0909
      (5) 0.006887
  • Es. 6.39: E(Z) = 10, V (Z) = 102
  • Es. 6.40:
      (1) 1-e−21/15 =1-0.2466
      (2) e−30/15 =0.1353
  • Es. 6.41: Svolto a lezione. Per calcolare l’integrale richiesto dalla funzione di ripartizione è consigliabile
    effettuare un cambio di variabile, utilizzando z = α tβ .
  • Es. 6.42: Basta ricordare l’espressione di media e varianza di una v.c. Gamma.

Cap. 9
                                                0
                          b2 è lo stimatore S 2 degli esercizi 9.16 e 9.18, e il confronto tra i due è stato già
  • Es. 9.46: Si noti che σ
    fatto in quei due esercizi. Oltre alle conclusioni di questi due esercizi, si noti che entrambi gli stimatori
    sono consistenti.
  • Es. 9.47: Dopo aver notato che si tratta di dati appaiati, si ottiene l’intervallo osservato (0.99, 6.12) per la
    differenza µP RIM A − µDOP O ; l’intervallo non include lo 0, per cui c’è un effetto positivo del trattamento.
    L’intervallo inoltre include il valore medio 4.5 Kg, e quindi l’affermazione appare giustificata,
  • Es. 9.48: Dopo aver notato che si tratta di dati appaiati, si ottiene l’intervallo osservato (-0.12, 3.12)
    per la differenza µP RIM A − µDOP O ; l’intervallo include lo 0, per cui non c’è nessuna evidenza di un
    effetto positivo. Tuttavia l’intervallo anche include il valore medio 2 cm corrispondente all’affermazione
    del produttore, per cui in questo senso l’affermazione è giustificata; permangono tuttavia dei dubbi e
    sarebbero necessari ulteriori dati.
  • Es. 9.49: Dopo aver notato che si tratta di due campioni indipendenti, utilizzando la formula che
    assume le varianze note (e quindi utilizza i percentili della normale), ovvero
                                                       r
                                                           40002    40002
                                     (x − y) ± z1−α/2             +       ,
                                                             8        8
     dove z1−α/2 = 1.96, si ottiene l’intervallo osservato (2492.5, 10332.5), che indica che la lucidatura porta
     ad una resistenza limite media maggiore.
  • Es. 9.50: Non in programma.



                                                        5
  • Es. 9.51: L’equazione da risolvere nel metodo dei momenti è

                                                         E(Xi ) = x

     da cui si trova subito λ
                            b = x.

  • Es. 9.52: Si deve risolvere il sistema
                                             (       2
                                                 eµ+σ /2              = x
                                                        2     2
                                                 (e2 µ+σ ) (eσ − 1)   = s2

                          s2                b2
                            
                                            σ
              b2 = log 1 + 2 e µ
     Si trova σ                b = log(x) −    .
                          x                 2
  • Es. 9.53:
      (1) (2781.5, 4818.5), che non include lo 0, suggerendo che il salario medio nella regione settentrionale
          è maggiore.
      (2) Gli assunti sono che i dati provengono da due CCS indipendenti; non occorre assumere la normalità
          delle variabili che rappresentano le singole osservazioni perché si tratta di campioni elevati, e si
          può utilizzare il teorema del limite centrale per la media campionaria.
  • Es. 9.54: Non in programma.
  • Es. 9.55: 301, arrotondando all’intero superiore.
  • Es. 9.56: Si trova l’intervallo osservato 0.161 < σ < 0.310, che include il valore 0.3: i dati suggeriscono
    che la variabilità del processo, pur diminuita, è compatibile con quella precedente.
  • Es. 9.57: Il risultato si trova immediatamente tenendo conto i due stimatori dati dalle varianze
    campionarie sono non distorti per σ 2 .
  • Es. 9.58:
      (1) 0.0227, 0.0623)
      (2) (0, 0.0591)
      (3) Usando entrambi gli intervalli (e il secondo appare più appropriato, visto che l’interesse è in
          particolare rivolto verso proporzioni di difettosità più elevate), non abbiamo elementi per contestare
          l’affermazione del produttore. Infatti, in entrambi i casi il valore 0.05 è incluso nell’intervallo di
          confidenza osservato.

Cap. 10
  • Es. 10.49: L’esercizio fornisce solo una descrizione stringata e interamente pre-sperimentale, per cui la
    formulazione delle ipotesi di interesse non è del tutto agevole. Un’interpretazione ragionevole è quella
    di assumere sempre l’alternativa bilaterale, salvo quando il testo suggerisce di fissare H1 unilaterale
    utilizzando termini del tipo “non più” o “almeno il”. Pertanto:
    (1), (3), (5): si adotta H1 bilaterale, quindi (ad esempio) nel caso (1) si scriverà H0 : µ = 21.8 contro
    H1 : µ 6= 21.8.
    (2): coerentemente con i punti sopracitati, la descrizione sembra riferita all’ipotesi nulla, per cui si
    scriverà H0 : p ≤ 0.2 contro H1 : p > 0.2. Poi, va ricordato, le conclusioni saranno le stesse se si passa a
    H0 : p = 0.2, con la medesima H1 .
    (4), (6): in linea con il punto precedente, per il punto (4) ad esempio si scriverà H0 : p ≥ 0.7 contro
    H1 : p < 0.7; anche qui è possibile passare a H0 : p = 0.7.
  • Es. 10.50: Test per due proporzioni con zoss = 2.12, il test è significativo al livello del 5%. Si rifiuta H0 .



                                                          6
• Es. 10.51: Test per due medie (piccoli campioni, varianze ignote) con toss = 3.978, distribuzione di
  riferimento t5 . Si ottiene 0.005 < P-value < 0.01, con forte evidenza contro H0 .
• Es. 10.52: Non in programma.
• Es. 10.53: Test per dati appaiati con toss = −2.12, si trova 0.05 < P-value < 0.10, con evidenza molto
  debole contro H0 . Non si rifiuta H0 , pur con qualche dubbio.
• Es. 10.54: L’esercizio si può risolvere utilizzando un test per due medie (piccoli campioni, varianze
  ignote), senza fare considerazioni sulle varianze. Si trova toss = −5.90, distribuzione di riferimento t13 .
  Si trova P-value > 0.001, si rifiuta H0 senza esitazione.
• Es. 10.55: L’esercizio si può risolvere utilizzando un test per due medie (piccoli campioni, varianze
  ignote), senza fare considerazioni sulle varianze. Si trova toss = 2.592, distribuzione di riferimento t29 .
  Si trova 0.01 < P-value < 0.015, ovvero con una moderata evidenza contro H0 .
• Es. 10.56: Si trova zoss = 2.183, con P-value = 0.0145, con una moderata evidenza contro H0 .




                                                    7
