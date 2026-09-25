---
fonte: "Esercizi_scelti_RISOLTI.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Esercizi     Scelti
                                 Analisi Matematica II
                                                            Risolti
                                                         Università di Udine
                                                                      ·
                                   Traccia → Procedimento → Svolgimento e soluzione
                                  Documento cumulativo  stato: 81 esercizi su 197 risolti

   SCOPERTA IMPORTANTE: LE PROVE D'ESAME SONO PRESE DA QUESTO FILE

       Confrontando questo elenco con le prove d'esame che abbiamo già risolto, la corrispondenza è
   letterale : i temi d'esame sono ripresi quasi alla lettera da questi esercizi.

                       Esercizio del le Prova d'esame                        Stato in questo documento
                       Es. 10 [CP 2.14]          22/01/2025, es. 2            risolto (sez. 2)
                       Es. 28 [CP 2.32]          3/09/2025, es. 1             risolto (sez. 2)
                       Es. 61 [CP 4.19]          17/09/2025, es. 3            risolto (sez. 3)
                       Es. 75 [S10 8.7]          22/01/2025, es. 1            risolto (sez. 5)
                       Es. 115 [CP 8.12]         17/09/2025, es. 2            risolto (sez. 3)
                       Es. 129 [CP 8.24]         3/09/2025, es. 2             risolto (sez. 3)
                       Es. 187 [CP 10.8]         3/09/2025, es. 3             risolto (sez. 7)
   Conseguenza pratica: questo le non è materiale di contorno, è il bacino da cui vengono pescati
   i temi. Lavorarlo a fondo vale più di qualunque altra attività di preparazione. Tutti e sette gli
   esercizi con riscontro d'esame sono ora risolti in questo documento.
       Le due correzioni sono confermate. Gli esercizi 28 e 75 confermano, in tipograa pulita, le
   due letture che avevo corretto sulle scansioni: il denominatore è (2
                                                                                        n n)2 e l'equazione è y ′ = xy 3 ey 2 .

   Le soluzioni aggiornate consegnate in precedenza sono quelle giuste.




   NOTA SULLA SEZIONE 3 (DIFFERENZIABILITÀ)

       Il le, alla sezione 3, non riporta esercizi ma una sola riga:                    Gli esercizi in questo caso si
   limitano a calcolare il piano tangente ad una funzione data in un punto dato .                           È esattamente
   l'argomento della guida operativa già consegnata: quella sezione è quindi già coperta.


    Avvertenza sul testo delle tracce.              Le formule sono state lette dalle pagine del PDF renderizzate ad alta
                                                                                                                x2n
risoluzione, non dall'estrazione automatica del testo, che in diversi casi le storpiava (ad es. l'es. 2 è     n arctan
                                                                                                                    e non

                                                          non arctan(n )
                                                                                                                         n
          x               nx                        n                     x
n arctan 2n ; l'es. 9 è
                        3+n4 x4
                                ; l'es. 11 è arctan
                                                    x
                                                      e                       ).




   STATO DI AVANZAMENTO DEL DOCUMENTO

       Questo è un unico documento che viene esteso progressivamente.                            Sezioni completate e da
   completare:




                                                                  1
           Sezione                            Esercizi   N.   Stato
            1.1 Successioni di funzioni       112       12   completata
           1.2 Serie di funzioni              1332      20   completata
           1.3 Serie di Fourier               3348      16   completata
           2.1 EDO del primo ordine           4968      20   solo l'es. 61 (tema d'esame)
           2.2 Analisi qualitativa            6980      12   completata
           2.3 Equazioni del secondo ordine   81105     25   da fare
           3 Dierenziabilità                            0   coperta dalla guida operativa
           4 Teorema del Dini                 106         1   completata
           5.1 Ottimizzazione libera          107123    17   solo l'es. 115 (tema d'esame)
           5.2 Ottimizzazione vincolata       124156    33   solo l'es. 129 (tema d'esame)
           6 Integrali multipli               157180    24   da fare
           7 Campi vettoriali                 181197    17  completata
           Totale                                        197 81 risolti, 116 da svolgere

Contents
1 Successioni di funzioni                                                                      3
2 Serie di funzioni                                                                           12
3 Esercizi comparsi nei temi d'esame                                                          25
4 Serie di Fourier                                                                            27
5 Analisi qualitativa delle soluzioni di EDO                                                  38
6 Teorema del Dini                                                                            44
7 Campi vettoriali                                                                            45
Appendice  Esercizi non ancora svolti                                                        54




                                                  2
1 Successioni di funzioni
 SCHEMA GENERALE PER TUTTA LA SEZIONE

       Ogni esercizio di questo tipo si aronta con la stessa procedura in tre mosse:

  1.   Limite puntuale: ssa x e fai tendere n → ∞. Attenzione ai valori di x che cambiano il
       comportamento (tipicamente x = 0, |x| = 1, o dove un denominatore si annulla): la discussione
       va spezzata proprio lì.

  2.   Sospetto di non uniformità: se la funzione limite f è discontinua (o illimitata) mentre le
       fn sono continue, la convergenza non può essere uniforme in un intorno di quel punto. Questa
       osservazione risolve metà degli esercizi senza calcoli.

  3.   Calcolo del sup: altrimenti studia supx |fn (x) − f (x)|. Se l'errore ha un massimo interno,
       derivalo e valuta nel punto di massimo xn (spesso xn → un punto critico): la convergenza è
       uniforme   ⇐⇒ quel massimo tende a 0.
 Il trucco ricorrente: il punto di massimo dell'errore si sposta con n (tipicamente xn = 1/n).
 Una successione che converge puntualmente a 0 può avere un picco viaggiante di altezza costante:
 è il caso classico di convergenza puntuale ma non uniforme.



Esercizio 1     [S5 1.2]

 TRACCIA

       Determinare tutti e soli gli α > 0 tali che la successione di funzioni fn : [0, ∞) → R,   fn (x) =
     x
         , converge uniformemente su [0, ∞).
  x + nα
   α




 PROCEDIMENTO

       Il limite puntuale è banalmente 0, quindi tutto il lavoro sta nel sup.      Poiché il dominio è
 illimitato, prima di derivare conviene guardare il comportamento all'innito: già quello esclude
 alcuni α. Il segno della derivata dipende dal segno di (1 − α): è lì che si separa la discussione.




 SVOLGIMENTO E SOLUZIONE

       Limite puntuale. Per x ≥ 0 ssato, nα → +∞, dunque fn (x) → 0: f ≡ 0.
       Studio del sup. Derivando rispetto a x:
                                         (xα + nα ) − x αxα−1   (1 − α)xα + nα
                             fn′ (x) =                        =                .
                                              (xα + nα )2         (xα + nα )2

       Caso α < 1: il numeratore è sempre positivo, quindi fn è crescente; inoltre fn (x) ∼ x
                                                                                                  1−α →

 +∞ per x → +∞. Dunque sup = +∞: niente convergenza uniforme.
   Caso α = 1: fn (x) = x+n → 1 per x → +∞, quindi sup = 1 ̸→ 0: niente convergenza
                         x

 uniforme.
    Caso α > 1: il numeratore si annulla in xn = n(α − 1)
                                                         −1/α , punto di massimo. Sostituendo, e
         α    nα
 usando xn =
             α−1 :

                                      xn      xn (α − 1)   (α − 1)1−1/α 1−α
                     fn (xn ) =    nα       =            =             n    −−−→ 0,
                                  α−1 + n
                                          α      α nα           α           n→∞


 poiché 1 − α < 0. Dunque         convergenza uniforme.

                                  Convergenza uniforme su [0, ∞)   ⇐⇒ α > 1.




                                                       3
Esercizio 2     [S5 1.3]

 TRACCIA
                                                                                           x2n
     Determinare gli intervalli di R su cui la successione di funzioni fn (x) = n arctan       converge
                                                                                            n
 puntualmente; determinare quindi gli intervalli di R su cui c'è convergenza uniforme.




 PROCEDIMENTO

     Compare x
                   2n : il comportamento cambia radicalmente a seconda che |x| sia < 1, = 1 o > 1  la

 discussione va organizzata su questi tre casi. Per |x| < 1 conviene usare l'equivalenza arctan t ∼ t
 per t → 0, che fa sparire il fattore n. Per |x| > 1 l'arcotangente satura a π/2 e resta il fattore n
 che diverge.




 SVOLGIMENTO E SOLUZIONE

     Limite puntuale.
                                    2n                                          2n
   |x| < 1: x2n → 0, quindi xn → 0 e, usando arctan t ∼ t, fn (x) ∼ n · xn = x2n → 0.

   |x| = 1: x2n = 1, dunque fn (±1) = n arctan n1 → 1 (sempre per arctan t ∼ t).
                 2n
   |x| > 1: xn → +∞ (l'esponenziale batte n), quindi arctan → π2 e fn (x) ∼ n π2 → +∞: non
     converge.
                                                                           (
                                                                            0 |x| < 1
                      Insieme di convergenza puntuale: [−1, 1],    f (x) =
                                                                            1 |x| = 1.
     Convergenza uniforme. La funzione limite è discontinua in x = ±1, mentre ogni fn è
                non c'è convergenza uniforme su [−1, 1] né su alcun insieme che contenga un
 continua: quindi
 intorno di ±1.
     Sia invece 0 < a < 1. Su [−a, a], sfruttando arctan t ≤ t per t ≥ 0:


                                                  x2n     a2n
                                   sup n arctan       ≤n·     = a2n → 0.
                                   |x|≤a           n       n

                           Puntuale su [−1, 1];   uniforme su [−a, a]   ∀ 0 < a < 1.


Esercizio 3     [CP 2.2]

 TRACCIA

     Studiare la convergenza puntuale e uniforme nell'intervallo [0, 1] della successione fn (x)      =
    n2 x
            .
  1 + n2 x2


 PROCEDIMENTO

     Qui il limite puntuale non è nullo: per x > 0 i termini n
                                                                  2 si semplicano e resta 1/x. Il punto

 x = 0 va trattato a parte (dà 0), ed è proprio lì che nasce la discontinuità del limite  che è anche
 illimitato vicino a 0. Due motivi indipendenti per escludere l'uniformità su [0, 1].




 SVOLGIMENTO E SOLUZIONE




                                                      4
    Limite puntuale. fn (0) = 0 per ogni n. Per x ∈ (0, 1]:
                                     n2 x        x         x  1
                                        2 2
                                            = 1     2
                                                      −−−→ 2 = .
                                    1+n x     n2
                                                 + x n→∞ x    x
                                             
                                             0 x = 0
                                    f (x) = 1
                                                  0 < x ≤ 1.
                                               x
    Uniforme su [0, 1]: no. Il limite f è discontinuo in x = 0 (anzi illimitato per x → 0+ ) mentre
 le fn sono continue: la convergenza non può essere uniforme.
    Uniforme su [a, 1], a > 0: sì. Per x ≥ a:
               n2 x     1   |n2 x2 − (1 + n2 x2 )|        1             1
                  2 2
                      −   =             2 2
                                                   =        2 2
                                                                 ≤               → 0.
              1+n x     x        x(1 + n x )         x(1 + n x )   a(1 + n2 a2 )

                   Puntuale su [0, 1] a f ;   uniforme su [a, 1] ∀a > 0, non su [0, 1].




Esercizio 4   [CP 2.3]

 TRACCIA

    Studiare la convergenza puntuale ed uniforme, sia in tutto R che in ogni intervallo limitato
                                                         x2
 I = [0, a], della successione di funzioni fn (x) =           .
                                                      n2 + x2


 PROCEDIMENTO

    Il limite puntuale è 0.       Per l'uniformità su R non serve derivare:    basta osservare che fn è
 crescente in |x| e tende a 1 per x → ±∞, quindi il sup vale 1 per ogni n. Su un intervallo limitato
 il sup si realizza all'estremo.




 SVOLGIMENTO E SOLUZIONE

    Limite puntuale. Per x ssato, n2 → ∞ dunque fn (x) → 0: f ≡ 0 su R.
                                         x2
    Su R: non uniforme. Poiché lim              = 1, si ha supx∈R |fn (x) − 0| = 1 ̸→ 0.
                                x→+∞ n2 + x2
    Su [0, a]: uniforme. La funzione x 7→ n2x+x2 è crescente su [0, a] (numeratore crescente,
                                              2


 denominatore che cresce più lentamente in proporzione), quindi


                                              x2        a2
                                      sup   2    2
                                                   =         −−−→ 0.
                                     0≤x≤a n + x     n2 + a2 n→∞

                         f ≡ 0;     non uniforme su R,     uniforme su ogni [0, a].




Esercizio 5   [CP 2.4]

 TRACCIA

    Studiare la convergenza puntuale ed uniforme, sia in tutto R che in ogni intervallo limitato,
 della successione di funzioni                  (
                                                 2, en ≤ x < en+1
                                       fn (x) =
                                                 0, altrimenti.




                                                      5
 PROCEDIMENTO

    È l'esempio-modello del gradino viaggiante: la funzione non si abbassa mai (vale sempre 2 sul
 suo supporto), ma il supporto scappa verso destra. Da qui: convergenza puntuale a zero (ogni x
 viene denitivamente scavalcato) ma sup costante, quindi niente uniformità su R. Su un intervallo
 limitato il supporto esce di scena dopo un numero nito di passi.




 SVOLGIMENTO E SOLUZIONE

    Limite puntuale. Fissato x, poiché en → +∞ esiste n̄ tale che en > x per ogni n ≥ n̄; per
 tali n si ha fn (x) = 0. Dunque fn (x) → 0: f ≡ 0 su R.
    Su R: non uniforme. Per ogni n, supx∈R |fn (x)| = 2 ̸→ 0 (il valore 2 è assunto su tutto
 [en , en+1 ), intervallo mai vuoto).
    Su un intervallo limitato I : uniforme. Sia M = sup I < ∞ e n̄ tale che en̄ > M . Per
 n ≥ n̄ si ha fn ≡ 0 su I , quindi supI |fn − 0| = 0 denitivamente: la convergenza è uniforme
 (banalmente).


                 f ≡ 0;    non uniforme su R,    uniforme su ogni intervallo limitato.




Esercizio 6   [CP 2.5]

 TRACCIA

    Studiare, al variare del parametro α > 0, la convergenza puntuale ed uniforme nell'intervallo
 [0, 1], della successione di funzioni
                                         
                                             α       0 ≤ x ≤ 1/n
                                         xn , 
                                         
                                         
                                           2      α
                                           n − x n , 1/n < x ≤ 2/n
                                fn (x) =
                                         
                                                     2
                                         
                                                     n < x ≤ 1.
                                         0,



 PROCEDIMENTO

    Non serve derivare: la funzione è una cuspide triangolare con base [0, 2/n] e vertice in x = 1/n.
 Basta calcolare l'altezza del picco. La base si stringe (quindi ogni x > 0 nisce fuori: limite nullo),
 ma l'altezza dipende da α: è il confronto fra i due eetti a decidere l'uniformità.




 SVOLGIMENTO E SOLUZIONE

    Limite puntuale. fn (0) = 0 per ogni n. Per x ∈ (0, 1] ssato, non appena n2 < x (cioè
 n > 2/x) si ha fn (x) = 0. Dunque f ≡ 0 su [0, 1], per ogni α > 0.
    Altezza del picco. Il massimo si ha nel vertice x = 1/n:
                                sup |fn | = fn n1 = n1 · nα = nα−1 .
                                                 
                                    [0,1]


    Conclusione. nα−1 → 0 ⇐⇒ α − 1 < 0.
                          Puntuale a 0 ∀α > 0;      uniforme   ⇐⇒ 0 < α < 1.

 Per α = 1 il picco resta di altezza 1; per α > 1 diverge: in entrambi i casi la convergenza non è
 uniforme, pur restando puntuale.



Esercizio 7   [CP 2.6]




                                                   6
 TRACCIA

      Studiare, al variare del parametro α > 0, la convergenza puntuale ed uniforme in ogni intervallo
 [0, a] con a > 0, della successione di funzioni fn (x) = xnα e−nx .


 PROCEDIMENTO

    Stessa struttura dell'esercizio precedente, ma con picco liscio invece che triangolare: qui il
 massimo va trovato derivando. Il risultato sarà lo stesso (xn = 1/n, altezza ∝ n
                                                                                       α−1 ): vale la pena

 notare la parentela, perché è lo schema che ricorre in tutta la sezione.




 SVOLGIMENTO E SOLUZIONE

    Limite puntuale. fn (0) = 0. Per x > 0 ssato, e−nx tende a 0 più rapidamente di quanto
 nα diverga, dunque fn (x) → 0: f ≡ 0.
    Massimo dell'errore. Derivando:
                                                                           1
                              fn′ (x) = nα e−nx (1 − nx) = 0 ⇐⇒ xn =         ,
                                                                           n
 punto di massimo (la derivata cambia segno da + a −). Per n > 1/a si ha xn ∈ [0, a] e


                                                              nα−1
                                 sup fn = fn n1 = n1 nα e−1 =
                                               
                                                                   .
                                 [0,a]                         e

    Conclusione.
                    Puntuale a 0 ∀α > 0;          uniforme su [0, a]   ⇐⇒ 0 < α < 1.


Esercizio 8   [CP 2.12]

 TRACCIA

    Studiare la convergenza puntuale ed uniforme in [1, +∞), in [1, 2] e in [2, +∞) della successione
 di funzioni fn (x) = 2n(x − 1)x
                                   −n .




 PROCEDIMENTO

    La traccia propone tre insiemi diversi proprio perché la risposta cambia: conviene calcolare
 una volta per tutte il punto di massimo xn e poi vericare in quale dei tre insiemi cade. Il fattore
 x−n decade esponenzialmente per x > 1 e batte il fattore n; ma vicino a x = 1 la competizione è
 serrata, ed è lì che si concentra il problema.




 SVOLGIMENTO E SOLUZIONE

    Limite puntuale. fn (1) = 0. Per x > 1: xn cresce esponenzialmente, dunque xnn → 0 e
 fn (x) → 0. Quindi f ≡ 0 su [1, +∞).
    Punto di massimo. Derivando:
                               h                   i
                   fn′ (x) = 2n x−n − n(x − 1)x−n−1 = 2n x−n−1 x − n(x − 1) ,
                                                                          


                                                    n       1                 +
 che si annulla per x − nx + n = 0, cioè xn =          =1+     . Poiché xn → 1 , per n ≥ 2 tale
                                                   n−1     n−1
 punto appartiene a [1, 2].




                                                     7
     Valore del massimo. Con xn − 1 = n−1                        n−1 n
                                             −n
                                                                                    n
                                       1
                                                                           1 − n1        → e−1 :
                                                                    
                                          e xn =                       =
                                                                  n

                                               1          n               2
                            fn (xn ) = 2n ·       · 1 − n1    −−−→ 2 · e−1 = ̸= 0.
                                              n−1             n→∞           e
     Conclusioni.
   Su [1, +∞) e su [1, 2] (entrambi contengono xn ): sup |fn | → 2e ̸= 0, non uniforme.

   Su [2, +∞): per n ≥ 3 si ha xn ≤ 23 < 2, quindi fn è decrescente su [2, +∞) e supx≥2 fn =
                            2n → 0: uniforme.
    fn (2) = 2n · 1 · 2−n = 2n
                     f ≡ 0; non uniforme su [1, +∞) e [1, 2]; uniforme su [2, +∞).


Esercizio 9     [CP 2.13]

 TRACCIA

     Studiare la convergenza puntuale e uniforme in [0, 2] della successione di funzioni fn (x) =
     nx
            .
  3 + n4 x4


 PROCEDIMENTO

     Ancora il picco viaggiante: si calcola il massimo derivando. Qui il risultato è particolarmente
 istruttivo, perché il valore del picco è costante (indipendente da n): la successione tende a zero in
 ogni punto, ma conserva sempre una gobba della stessa altezza che si sposta verso l'origine.




 SVOLGIMENTO E SOLUZIONE

     Limite puntuale. fn (0) = 0. Per x > 0: il denominatore cresce come n4 , il numeratore come
 n, dunque fn (x) → 0. Quindi f ≡ 0 su [0, 2].
     Massimo. Derivando (numeratore della derivata):
                   n(3 + n4 x4 ) − nx · 4n4 x3 = n 3 + n4 x4 − 4n4 x4 = 3n 1 − n4 x4 ,
                                                                                   

                               1
 che si annulla per xn =         (punto di massimo). Il valore è
                               n
                                           n · n1      1    1
                              fn n1 =                                per ogni n.
                                   
                                              4   1 = 3+1 = 4
                                        3 + n · n4

     Conclusioni. sup[0,2] |fn | = 14 ̸→ 0: non uniforme su [0, 2]. Su [a, 2] con a > 0: per n > 1/a
                  1                                                                             na
 il punto xn =
                  n è fuori dall'intervallo e fn è decrescente, quindi sup[a,2] fn = fn (a) = 3+n4 a4 → 0:
 uniforme.
                       f ≡ 0;      non uniforme su [0, 2],   uniforme su [a, 2] ∀a > 0.




Esercizio 10     [CP 2.14]

 TRACCIA

     Studiare la convergenza puntuale ed uniforme in R della successione di funzioni fn (x) =
  n cos(x2 + 1) + n2 x
                       . (Coincide con l'esercizio 2 della prova del 22/01/2025.)
       n2 x2 + n2




                                                         8
 PROCEDIMENTO

    Non calcolare limiti a forza bruta: spezza la frazione.             Raccogliendo n
                                                                                         2 al denominatore, la
                                                                                          1
 successione si separa in un termine indipendente da n (che è il limite) più un resto con
                                                                                          n in fattore.
                                                                                            2
 L'errore diventa allora esplicito e si maggiora con i due fatti elementari | cos | ≤ 1 e x + 1 ≥ 1,
 ottenendo una stima indipendente da x.




 SVOLGIMENTO E SOLUZIONE
             2 2 + n2 = n2 (x2 + 1):
    Poiché n x


                                 n cos(x2 + 1)       n2 x        x      cos(x2 + 1)
                      fn (x) =                 +             =        +             .
                                  n2 (x2 + 1)    n2 (x2 + 1)   x2 + 1    n(x2 + 1)

    Limite puntuale. Il secondo addendo tende a 0 per ogni x, dunque
                                                                 x
                                        fn (x) −→ f (x) =              ∀x ∈ R.
                                                             x2 + 1

    Convergenza uniforme. Usando | cos(·)| ≤ 1 e x2 + 1 ≥ 1:
                                                cos(x2 + 1)       1       1
                      |fn (x) − f (x)| =                    ≤           ≤           ∀x ∈ R,
                                                 n(x2 + 1)    n(x2 + 1)   n
                                                                      1
 maggiorazione indipendente da x, quindi supR |fn − f | ≤
                                                                      n → 0.

                                           x
                             f (x) =             ;   convergenza uniforme su tutto R.
                                        x2 + 1


Esercizio 11     [CP 2.16]

 TRACCIA
                              n
    Sia fn (x)   = arctan           .    Determinare l'insieme di convergenza puntuale della successione
                             x
 {fn }, la funzione limite f (x) e in quali intervalli la convergenza è uniforme.


 PROCEDIMENTO
                                                                                                     n
    Il dominio esclude x = 0: va detto subito. Il limite dipende dal segno di x, perché
                                                                                                     x → ±∞
 di conseguenza. Sull'uniformità c'è un ribaltamento rispetto agli esercizi precedenti, ed è il punto
                                                    n
 interessante: qui il problema non è vicino a 0 (dove
                                                    x è grandissimo e l'arcotangente è già satura),
                      n
 ma all'innito, dove
                      x → 0 e il limite non viene mai raggiunto.




 SVOLGIMENTO E SOLUZIONE

    Dominio e limite puntuale. Le fn sono denite per x ̸= 0.
   x > 0: nx → +∞, quindi fn (x) → π2 ;

   x < 0: nx → −∞, quindi fn (x) → − π2 .
                                                                                    (
                                                                                      π
                                                                        π             2     x>0
               Convergenza puntuale su R \ {0},                  f (x) = sgn(x) =
                                                                        2            − π2   x < 0.
    Convergenza uniforme. Consideriamo x > 0 (il caso x < 0 è simmetrico). L'errore
                                                          π  π         n
                                               fn (x) −     = − arctan
                                                          2  2         x


                                                             9
                                                n
 è crescente in x (al crescere di x l'argomento
                                                x diminuisce e l'arcotangente pure).
   Su (0, a] con a > 0: il sup si realizza in x = a, quindi sup(0,a] fn − π2 = π2 − arctan na → 0:
    uniforme.
   Su [a, +∞): per x → +∞ l'errore tende a π2 − arctan 0 = π2 , quindi sup = π2 ̸→ 0: non
    uniforme.
             Uniforme su (0, a] e su [−a, 0) ∀a > 0; non uniforme su insiemi illimitati.


 Osservazione. È il rovescio del caso tipico: la convergenza è migliore vicino alla singolarità x = 0
 e peggiore all'innito.



Esercizio 12     [CP 2.17]

 TRACCIA
                  n2 x2 + nx
    Sia fn (x) =              . Determinare l'insieme di convergenza puntuale della successione {fn },
                   x2 + n2
 la funzione limite f (x) e in quali intervalli la convergenza è uniforme.




 PROCEDIMENTO

    Il limite puntuale si ottiene confrontando i gradi in n: numeratore e denominatore sono en-
                                                                               2
 trambi di grado 2, quindi il limite è il rapporto dei coecienti, cioè x . Per l'uniformità, calcola
 l'errore come unica frazione (denominatore comune) e poi cerca una successione di punti xn che
 dipenda da n: se l'errore lì non tende a 0, l'uniformità su R è esclusa. La scelta xn = n è quella
 che funziona.




 SVOLGIMENTO E SOLUZIONE

    Limite puntuale. Per x ssato:
                                      n2 x2 + nx   x2 + nx
                                                 = x2
                                                           −−−→ x2 .
                                       x2 + n2      2 + 1
                                                           n→∞
                                                       n

 Dunque la convergenza è puntuale su tutto R, con f (x) = x .
                                                                     2

    Errore. Mettendo a denominatore comune:
                                             n2 x2 + nx − x2 (x2 + n2 )   |nx − x4 |
                         |fn (x) − x2 | =                               =            .
                                                      x2 + n2              x2 + n2

    Su R: non uniforme. Scegliendo xn = n:
                                            |n · n − n4 |   n4 − n2   n2 − 1
                        |fn (n) − n2 | =                  =         =        → +∞.
                                              n2 + n2         2n2        2
 Dunque supR |fn − f | = +∞.
    Su [−a, a]: uniforme. Per |x| ≤ a:
                                       |nx − x4 |   na + a4
                                                  ≤         −−−→ 0.
                                        x2 + n2       n2    n→∞


                      f (x) = x2 ;   non uniforme su R,       uniforme su ogni [−a, a].




                                                       10
RIEPILOGO DELLA SEZIONE  I DUE SCHEMI CHE RITORNANO

   1. Il picco viaggiante (es. 6, 7, 9, e in parte 8). La successione converge puntualmente a 0
ma conserva una gobba di altezza hn che si sposta verso un punto (di solito xn = 1/n → 0). La
convergenza è uniforme    ⇐⇒ hn → 0. Negli es. 6 e 7 l'altezza è ∝ nα−1 (uniforme ⇐⇒ α < 1);
                        1
nell'es. 9 è costante =
                        4 (mai uniforme).
    2. Il limite discontinuo (es. 2, 3, 11). Se f è discontinua e le fn sono continue, l'uniformità è
esclusa in un intorno del punto critico, senza calcolare alcun sup. Restringendo il dominio lontano
da quel punto la convergenza torna uniforme.

   Regola generale che se ne ricava: la convergenza uniforme si perde quasi sempre in
prossimità di un punto critico (una discontinuità del limite, un picco che si concentra, o l'innito).
La domanda giusta da farsi non è converge uniformemente? ma dove si rompe l'uniformità?,
e poi restringere il dominio evitando quel punto.




                                                  11
2 Serie di funzioni
 SCHEMA GENERALE PER TUTTA LA SEZIONE

       Le quattro nozioni in gioco stanno in questa gerarchia:


                                                    uniforme
                                                  (
                                   totale =⇒                      =⇒ puntuale
                                                    assoluta

 (nessuna freccia si inverte; uniforme e assoluta sono fra loro indipendenti).
     Procedura operativa:
  1. Controlla la condizione necessaria: se il termine generale non tende a 0, la serie diverge e
       hai nito (es. 24 si risolve solo così).

  2.   Tenta subito il criterio
                             P di Weierstrass (M-test): maggiora supx |fn (x)| ≤ Mn con Mn
       indipendente da x; se  Mn < ∞ hai la convergenza totale, e con essa uniforme e assoluta in
       un colpo solo. È la via più rapida e va sempre provata per prima.

  3.   Se è una serie di potenze (anche mascherata, dopo una sostituzione): calcola il raggio con
       CauchyHadamard, poi studia a parte i due estremi.

  4.   Se
       P è geometrica (anche mascherata): individua la ragione q(x), imponi |q(x)| < 1 e usa
                 n =    q
         n≥1 q         1−q per la somma.
 Il riconoscimento è metà del lavoro: molti esercizi di questa sezione sono geometriche o serie
                          t
 note (log(1 + t), e ) camuate da una sostituzione. Prima di calcolare, chiediti sempre che serie
 è, sotto mentite spoglie?



Esercizio 13       [S6]

 TRACCIA
                                                                             ∞
                                                                             X       x2n
       Studiare la convergenza puntuale, uniforme e totale della serie                     , x ∈ R.
                                                                                   1 + x2n
                                                                             n=1



 PROCEDIMENTO

       Compare x
                       2n : come sempre in questi casi la discussione si spezza su |x| < 1, |x| = 1, |x| > 1.

 La chiave è la condizione necessaria: per |x| ≥ 1 il termine generale non è innitesimo, e questo
 chiude subito il caso. Per l'uniformità sull'intervallo aperto, usa il fatto che supx |fn (x)| → 0 è
                       1
 necessario : qui vale 2 e basta a escludere tutto.




 SVOLGIMENTO E SOLUZIONE

       Convergenza puntuale. Posto t = x2n ≥ 0, il termine è 1+t
                                                              t
                                                                 .
                                  2n
   |x| < 1: x2n → 0 e 1+x
                         x
                           2n ≤ x
                                  2n = (x2 )n , termine generale di una serie geometrica di ragione

    x2 < 1: la serie converge.

   |x| = 1: il termine vale 21 per ogni n, non innitesimo: diverge.

   |x| > 1: x2n → +∞ dunque il termine → 1 ̸= 0: diverge.
                                       Insieme di convergenza puntuale: (−1, 1).

    Convergenza totale (e uniforme) su [−a, a], a < 1. sup|x|≤a 1+x       x         2n
                                                                                   2n e    a2n < ∞:
                                                                                                 P
                                                                            2n ≤ a
 per il criterio di Weierstrass la convergenza è totale, quindi anche uniforme.
    Su tutto (−1, 1): non uniforme. sup|x|<1 1+x    x2n               x2n     1
                                                      2n = lim|x|→1− 1+x2n = 2 ̸→ 0, e la condizione




                                                          12
 sup |fn | → 0 è necessaria per l'uniformità.

            Puntuale su (−1, 1); totale/uniforme su [−a, a] ∀a < 1; non uniforme su (−1, 1).




Esercizio 14      [CP 2.18]

 TRACCIA
                                                                        +∞     √
                                                                        X  cos( n x) + 1
     Trovare gli insiemi di convergenza uniforme e totale della serie                         .
                                                                              log(n) n2
                                                                        n=1



 PROCEDIMENTO

     Esercizio-tipo da M-test: la variabile x compare solo dentro un coseno, che è limitato. Mag-
 giorando il coseno si ottiene subito una stima indipendente da x, e resta da studiare una serie
 numerica. Non serve altro.




 SVOLGIMENTO E SOLUZIONE

     (La somma parte da n = 2, poiché log 1 = 0 annullerebbe il denominatore.)
                           √                     √
     Poiché −1 ≤ cos(    n x) ≤ 1, si ha 0 ≤ cos( n x) + 1 ≤ 2 per ogni x ∈ R, dunque
                                   √
                             cos( n x) + 1         2
                                          2
                                             ≤ 2        =: Mn      ∀x ∈ R.
                                 log(n) n       n log n
                     P         2                            P 1
 La serie numerica     n≥2 n2 log n converge (confronto con      , essendo log n ≥ log 2 > 0). Per il
                                                              n2
 criterio di Weierstrass la convergenza è totale su tutto R, e quindi anche uniforme e assoluta su
 tutto R.
                          Convergenza totale (dunque uniforme) su tutto R.




Esercizio 15      [S7 6]

 TRACCIA
                                                               X (−1)n n2  x − 2 n
     Studiare la convergenza puntuale e uniforme della serie                              .
                                                                n
                                                                    n4 + 2     x+5


 PROCEDIMENTO
                                                                 x−2
 P È nuna serie di potenze mascherata : la sostituzione t = x+5 la riporta alla forma standard
    cn t . Si studia in t e solo alla ne si torna a x risolvendo la disequazione |t| ≤ 1. Attenzione:
                                 1
 i coecienti decadono come 2 , quindi la serie converge anche sul bordo |t| = 1  il che rende
                                 n
 l'insieme nale più ampio del previsto.




 SVOLGIMENTO E SOLUZIONE
                                  x−2                                                     n 2
     Sostituzione. Posto t :=                                               n con c = (−1) n , e
                                                                      P
                                      (con x ̸= −5), la serie diventa   c
                                                                       n n t       n
                                  x+5                                                  n4 + 2
           1
 |cn | ∼      .
           n2
    Raggio. lim supn |cn |1/n = 1, quindi ρ = 1:Pconvergenza assoluta per |t| < 1.
    Bordo |t| = 1. Qui |cn tn | = |cn | ∼ n12 e    1
                                                   n2
                                                      converge: la serie converge assolutamente
 anche per |t| = 1. Dunque converge per ogni |t| ≤ 1.
    Ritorno a x. La condizione |t| ≤ 1 signica |x − 2| ≤ |x + 5|; elevando al quadrato (entrambi


                                                  13
 i membri sono ≥ 0):


                                                                           3
                x2 − 4x + 4 ≤ x2 + 10x + 25 ⇐⇒ −14x ≤ 21 ⇐⇒ x ≥ − .
                                                                           2
     Convergenza totale. Su tutto l'insieme − 32 , +∞ vale |t| ≤ 1, quindi
                                                    


                                                              n2                       X
                               sup |cn tn | ≤ |cn | =              =: Mn ,                  Mn < ∞.
                              x≥−3/2                        n4 + 2

                                               totale, quindi uniforme, su tutto − 23 , +∞ .
                                                                                                     
 Per Weierstrass la convergenza è


                                                                                                          3
                   Converge (assolutamente, totalmente, uniformemente) per x ≥ −
                                                                                                          2.



Esercizio 16      [S7 7(a)]

 TRACCIA
                                                                                   X        3n x2n
     Studiare la convergenza puntuale ed uniforme della serie                                        e calcolarne la somma,
                                                                                         2 (x2 + 1)n
                                                                                   n≥0
 ove possibile.




 PROCEDIMENTO

                                                geometrica di ragione q(x) = x3x
                                                                                             2
     Raccogliendo, si vede che è una                                          2 +1 moltiplicata per la costante
  1
  2 . Tutto si riduce allora a risolvere q(x) < 1 e ad applicare la formula della somma geometrica.
 Nota che q ≥ 0 sempre, quindi non serve il valore assoluto.




 SVOLGIMENTO E SOLUZIONE

     Riconoscimento. La serie si riscrive come
                                                           n
                                                   3x2                              3x2
                                              
                                    1X
                                                                ,        q(x) :=          ≥ 0.
                                    2             x2 + 1                           x2 + 1
                                        n≥0

     Condizione di convergenza.
                                                                         1
                           q(x) < 1 ⇐⇒ 3x2 < x2 + 1 ⇐⇒ 2x2 < 1 ⇐⇒ |x| < √ .
                                                                          2

     Somma (geometrica da n = 0, quindi 1−q
                                         1
                                            ):



                            1    1       1     x2 + 1                                x2 + 1
               S(x) =         ·      2 =   ·              =                                          |x| < √12 .
                            2 1 − 3x
                                   2
                                         2 (x2 + 1) − 3x2                          2(1 − 2x2 )
                                       x +1

     Convergenza uniforme.                         < √12 si ha q(x) ≤ q(a) =: q̄ < 1 (poiché q
                                              Su [−a, a] con a
                                             1 n
                                                         q̄ < ∞: convergenza totale, dunque
                                                      P n
 è crescente in |x|), quindi sup |termine| ≤
                                           2 q̄ con

 uniforme. Su tutto   − √12 , √12 la convergenza non è uniforme: per |x| → √12 si ha q → 1 e il
 termine generale non tende a 0 uniformemente (inoltre S(x) → +∞).



Esercizio 17      [S7 9]




                                                                    14
 TRACCIA
                                                     X 2n−1
    Studiare la convergenza puntuale della serie                    (arctan x)n e calcolarne la somma pun-
                                                            π n−1
                                                     n≥1
 tuale, ove possibile.     Caratterizzare inoltre gli intervalli di         R su cui la serie converge total-
 mente/uniformemente.




 PROCEDIMENTO

    Ancora una geometrica mascherata, ma con una particolarità che rende l'esercizio istruttivo:
                                        2u            2u                         π
 posto u = arctan x, la ragione è
                                                       π < 1 equivale a |u| < 2 , che è sempre
                                        π e la condizione
                                                     π
 vericata perché l'arcotangente non raggiunge mai ± 2 . Quindi la serie converge ovunque  ma
 proprio perché la ragione tende a 1 all'innito, l'uniformità su tutto R salta.




 SVOLGIMENTO E SOLUZIONE

    Riconoscimento. Posto u := arctan x ∈ − π2 , π2 , il termine si riscrive come
                                                             

                                                                 n−1
                                           2n−1 n
                                                        
                                                            2u
                                                 u =u                   .
                                           π n−1            π
                               2u
 È una geometrica di ragione
                               π e primo termine u.
    Convergenza puntuale. Serve 2u       π  < 1 ⇐⇒ |u| < π2 : condizione sempre soddisfatta,
                      2 per ogni x ∈ R. Dunque la serie converge per ogni x ∈ R, con somma
                      π
 poiché | arctan x| <


                                          u        πu              π arctan x
                             S(x) =            =        =                       .
                                        1 − 2u
                                            π
                                                 π − 2u          π − 2 arctan x

     Convergenza totale/uniforme. Su [−a, a]: |u| ≤ arctan a < π2 , quindi la ragione è maggio-
 rata da una costante < 1 e il criterio di Weierstrass dà convergenza totale (dunque uniforme).
     Su tutto R no: calcolando il sup del termine n-esimo,


                                      2n−1 n    2n−1  π n π
                                  sup   n−1
                                            u =            =                  ∀n,
                                  x∈R π         π n−1 2      2

 che non tende a 0: la condizione necessaria per l'uniformità è violata.


                Puntuale su R; totale/uniforme su ogni [−a, a]; non uniforme su R.




Esercizio 18   [CP 2.19]

 TRACCIA
                                     
                      x       |x| + n
    Sia fn (x) =            log        . Determinare l'insieme di convergenza puntuale e l'insieme
                   1 + n|x|      n
                                     +∞
                                     X
 di convergenza uniforme della serie    fn (x).
                                         n=1



 PROCEDIMENTO
                                                                                                        
    La strada è la stima asintotica del termine: riscrivendo il logaritmo come log             1 + |x|
                                                                                                    n        e usando

 log(1 + t) ≤ t, si scopre che fn si comporta come nx2  quindi la serie converge ovunque. Per
                                       |x|2
 l'uniformità, il punto è che la stima      dipende da x e non è limitata: su insiemi illimitati salta
                                        n2
 tutto.




                                                    15
 SVOLGIMENTO E SOLUZIONE

      Stima del termine. Scrivendo |x|+n
                                     n   = 1 + |x|
                                                n e usando 0 ≤ log(1 + t) ≤ t per t ≥ 0, insieme
       |x|    1
 a
     1+n|x| ≤ n :                                       
                                      |x|            |x|     1 |x|     |x|
                        |fn (x)| =           log 1 +       ≤ ·      = 2.
                                   1 + n|x|           n      n n       n
    Convergenza puntuale. Per ogni x ssato,               < ∞: la serie converge assolutamente
                                                    P |x|
                                                       n2
 per ogni x ∈ R.
    Convergenza   uniforme su [−a, a]. Qui la stima diventa |fn (x)| ≤ na2 =: Mn , indipendente
             Mn < ∞: convergenza totale, dunque uniforme.
           P
 da x, con
    Su tutto R: no. Il singolo termine è illimitato: per x → +∞, 1+nx
                                                                    x
                                                                         → n1 mentre log 1 + nx →
                                                                                               

 +∞, quindi supx∈R |fn (x)| = +∞. Violata la condizione necessaria, non c'è uniformità su R.

                         Puntuale su R; uniforme (totale) su ogni [−a, a]; non su R.




Esercizio 19        [CP 2.20]

 TRACCIA
                                             +∞
                                             X
      Si consideri la serie di funzioni             enx .    Si determini l'insieme di convergenza puntuale, la
                                             n=1
 somma della serie e in quali intervalli la convergenza è uniforme.




 PROCEDIMENTO
                                                x        x < 1, cioè x < 0. L'unica accortezza è
      Geometrica pura di ragione q = e : la condizione è e
                                                                   q         1
 che la somma parte da n = 1 e non da n = 0, quindi la formula è
                                                                  1−q e non 1−q .



 SVOLGIMENTO E SOLUZIONE

      Convergenza puntuale.                         nx               x n                            = ex > 0;
                                         P                   P
                                           n≥1 e         =     n≥1 (e ) è geometrica di ragione q
 converge ⇐⇒ ex < 1 ⇐⇒ x < 0 .
      Somma (primo indice n = 1):

                                                 q              ex
                                       S(x) =       =                ,      x < 0.
                                                1−q           1 − ex

      Convergenza
              P −a nuniforme. Su (−∞, −a] con a > 0: q = e ≤ e < 1, quindi sup |e | ≤
                                                                    x     −a                     nx

 (e−a )n con    (e ) < ∞: convergenza totale, dunque uniforme.
      Su tutto (−∞, 0) no: supx<0 e
                                   nx = 1 ̸→ 0 (il sup si realizza per x → 0− ), e infatti S(x) → +∞

 per x → 0 .
             −

                                Puntuale su (−∞, 0); uniforme su (−∞, −a] ∀a > 0.




Esercizio 20        [CP 2.21]

 TRACCIA
                                                                                 +∞
                                                                                 X  n! arctan((n2 + 1)x)
      Studiare la convergenza puntuale, uniforme e totale della serie                                      .
                                                                                             nn
                                                                                 n=1




                                                              16
 PROCEDIMENTO
                                                                                            π
      Come nell'es. 14, la x è connata dentro un'arcotangente, che è limitata da               : maggiorandola
                                P n!                                                    2
 resta una serie numerica pura,      n , la cui convergenza si stabilisce col criterio del rapporto (dove
                                   n
                                 1 n
                                   
 compare il limite notevole 1 +
                                 n     → e).


 SVOLGIMENTO E SOLUZIONE

      Maggiorazione. Poiché | arctan(·)| < π2 per ogni argomento,
                         n! arctan((n2 + 1)x)      π n!
                                     n
                                                ≤ · n =: Mn       ∀x ∈ R.
                                   n               2 n

     Convergenza di Mn (criterio del rapporto):
                       P

                                                           n
                                  nn    (n + 1) nn
                                                     
          Mn+1       (n + 1)!                           n            1          1
                 =              ·     =            =          =          n −−−→ < 1,
           Mn      (n + 1)n+1 n!        (n + 1)n+1     n+1        1 + n1    n→∞ e

        P
 quindi    Mn converge.
     Conclusione. Per il criterio di Weierstrass la convergenza è totale su tutto R, e con essa
 uniforme, assoluta e puntuale su tutto R.


                     Convergenza totale (dunque uniforme e assoluta) su tutto R.




Esercizio 21   [CP 2.22]

 TRACCIA
                                                                             +∞
                                                                             X
                                                                                   cos(x)n nell'insieme
                                                                                                          π π
      Studiare la convergenza puntuale, uniforme e totale della serie
                                                                                                           4, 2 .
                                                                             n=1



 PROCEDIMENTO
                                                                       π π
      Geometrica di ragione cos x. La restrizione all'intervallo
                                                         √              4 , 2 è il regalo dell'esercizio: lì il
                                                π         2
 coseno è decrescente e vale al massimo cos         =         < 1.    Si ottiene quindi una maggiorazione
                                                4        2
 uniforme con una costante strettamente minore di 1, che è esattamente ciò che serve per il criterio
 di Weierstrass.



 SVOLGIMENTO E SOLUZIONE

      Range della ragione. Su
                                  π π
                                   4 , 2 il coseno è decrescente, quindi
                                                                     √
                                                                      2
                                 0 = cos π2 ≤ cos x ≤ cos π4 =          < 1.
                                                                     2
                                                          √ n
      Convergenza totale. supx∈[π/4,π/2] | cosn x| =           2               P
                                                              2      =: Mn e       Mn è geometrica di ragione
  √
                converge. Per Weierstrass la convergenza è totale, dunque uniforme e assoluta,
   2
  2 < 1, quindi
           π π
 su tutto   ,
           4 2 .
                                               cos x
     Somma (geometrica da n = 1): S(x) =                       π
                                                                 
                                                       , con S
                                             1 − cos x         2 = 0.

                                                                   π π               cos x
                   Convergenza totale (dunque uniforme) su
                                                                    4, 2 ;     S(x) = 1−cos  x.



Esercizio 22   [CP 2.25]



                                                    17
 TRACCIA

     Studiare la convergenza puntuale e totale, in [0, +∞) e in [a, +∞) per ogni a > 0, della serie
               +∞
               X
 di funzioni         xe−2nx .
               n=1



 PROCEDIMENTO

     Anche qui geometrica (ragione e
                                             −2x ), ma il fattore x davanti cambia le cose sul bordo. Il punto

 interessante è la convergenza totale su [0, +∞): il sup del termine n-esimo si calcola derivando
                 1                1
 e cade in xn = 2n , dando Mn ∝
                                  n  serie armonica, divergente. È il classico caso in cui c'è
 convergenza puntuale ma non totale, perché il picco si sposta verso 0.




 SVOLGIMENTO E SOLUZIONE

     Convergenza puntuale. Per x = 0 tutti i termini sono nulli. Per x > 0 la serie è geometrica
 di ragione e
               −2x < 1 moltiplicata per x, quindi converge, con somma


                                              xe−2x
                                    S(x) =               (x > 0),     S(0) = 0.
                                             1 − e−2x
 La convergenza puntuale vale dunque su tutto [0, +∞).
     Convergenza totale su [0, +∞): no. Studiamo gn (x) = xe−2nx :
                                                           1                                          1
          gn′ (x) = e−2nx (1 − 2nx) = 0 ⇐⇒ xn =                                         1
                                                                                          
                                                             (massimo),        Mn = gn 2n   =             .
                                                          2n                                         2n e

              2ne diverge (armonica), il criterio di Weierstrass fallisce e in eetti non c'è convergenza
          P 1
 Poiché
 totale su [0, +∞).
     Convergenza totale su [a, +∞), a > 0: sì. Per n > 2a
                                                        1
                                                          il punto di massimo xn =
                                                                                    1
                                                                                   2n cade
 fuori dall'intervallo e gn è decrescente su [a, +∞), quindi


                                           sup gn (x) = gn (a) = ae−2na ,
                                           x≥a

            −2na è geometrica di ragione e−2a < 1: converge. Convergenza totale (dunque uniforme).
     P
 e   n ae

                      Puntuale su [0, +∞); totale su [a, +∞) ∀a > 0, non su [0, +∞).




Esercizio 23     [CP 2.27]

 TRACCIA
                                                                               +∞
                                                                               X         x
     Studiare la convergenza puntuale e totale della serie di funzioni                           .
                                                                                     n(1 + nx2 )
                                                                               n=1



 PROCEDIMENTO

     Simile al precedente nella forma, ma con esito opposto :            vale la pena metterli a confronto.
                                                                               1
 Anche qui il sup del termine si trova derivando e il massimo si sposta (xn = √ ), ma stavolta
                                                                                           n
 l'altezza decade come n
                                −3/2 , che è sommabile. Morale: non basta che il picco viaggi, conta quanto

 in fretta si abbassa.




                                                         18
 SVOLGIMENTO E SOLUZIONE

    Convergenza puntuale. Per x = 0 i termini sono nulli. Per x ̸= 0 ssato, n(1+nx
                                                                                 x         1
                                                                                    2 ) ∼ n2 x , e

       converge: la serie converge assolutamente per ogni x ∈ R.
 P 1
    n2
                                                      x
    Convergenza totale su R. Studiamo gn (x) =            2
                                                            ; a meno del fattore
                                                                                  1
                                                                                  n si tratta di
                                                                   n(1 + nx )
          x
 h(x) = 1+nx2 , con



                                     (1 + nx2 ) − x · 2nx    1 − nx2                1
                          h′ (x) =                        =             = 0 ⇐⇒ x = √ ,
                                         (1 + nx2 )2        (1 + nx2 )2              n
                    √
 e h    √1
          n
                  = 1/2 n = 2√1 n . Dunque

                                                               1   1    1
                                       Mn := sup |gn (x)| =      · √ = 3/2 .
                                              x∈R              n 2 n  2n
              P     1                             3
                        converge (p-serie con p =
 Poiché
                  2n3/2                           2 > 1), per il criterio di Weierstrass la convergenza è
 totale su tutto R, dunque uniforme.

                                 Convergenza totale (dunque uniforme) su tutto R.


                                              1
 Confronto con l'es. 22: là il picco valeva ∝ n (non sommabile), qui ∝ n
                                                                         −3/2 (sommabile). Stessa

 struttura, conclusioni opposte.



Esercizio 24         [CP 2.28]

 TRACCIA

        fn (x) = cos nx per x ∈ [−π, π].
                        
       Sia                                            Determinare le regioni di convergenza puntuale ed
                      +∞
                      X
 uniforme della serie    fn (x).
                            n=1



 PROCEDIMENTO

       Prima di qualunque calcolo, applica la         condizione necessaria: il termine generale deve
                  x                  x
 tendere a 0. Qui
                  n → 0 e quindi cos n → 1. L'esercizio è interamente in questa osservazione, ed
 è messo lì apposta per vericare che non ci si getti a calcolare sup inutili.




 SVOLGIMENTO E SOLUZIONE

       Condizione necessaria. Per ogni x ∈ [−π, π] ssato,
                                                             x
                                      lim fn (x) = lim cos          = cos 0 = 1 ̸= 0.
                                     n→∞            n→∞        n
 Il termine generale non è innitesimo, dunque la serie             nonP
                                                                       converge in alcun punto di [−π, π]
 (le somme parziali divergono a +∞, comportandosi come                     1).

              L'insieme di convergenza puntuale è vuoto; a maggior ragione non c'è uniformità.




Esercizio 25         [CP 2.29]

 TRACCIA




                                                          19
                                                               +∞        √
                                                               X   3n + n n
      Studiare la convergenza puntuale ed uniforme della serie                x .
                                                                  5n + log(n)
                                                                             n=1



 PROCEDIMENTO

      Serie di potenze: per il raggio conta solo il comportamento asintotico dei coecienti. I termini
 √                                                                                 3 n
     n e log n sono trascurabili rispetto a 3n e 5n , quindi cn ∼
                                                                                     
                                                                                       e il raggio si legge a colpo
                                                                                   5
 d'occhio. Sul bordo il termine tende a una costante non nulla: la serie diverge.



 SVOLGIMENTO E SOLUZIONE
                                               √
      Raggio di convergenza. Poiché 3n + n ∼ 3n e 5n + log n ∼ 5n :
                               √       n
                           3n + n      3              √      3       5
                      cn = n        ∼      =⇒ lim sup n cn =   =⇒ ρ = .
                          5 + log n    5         n           5       3
                                  5
 Convergenza assoluta per |x| <
                                  3.
      Estremi x = ± 3 . Il termine generale vale cn
                    5
                                                               n        3 n       5 n
                                                        ± 35                           = (±1)n , che non è innites-
                                                                                    
                                                                    ∼    5         3
 imo: la seriediverge in entrambi gli estremi.
    Convergenza uniforme. Su [−a, a] con a < 53 vale |cn xn | ≤      cn an con   cn an < ∞:
                                                                               P
 convergenza totale, dunque uniforme. Non è uniforme su tutto − ,
                                                               5 5
                                                                   
                                                               3 3 (avvicinandosi agli estremi
 la serie diverge).


                                            5                                   5
                       Converge per |x| <
                                            3 ; totale/uniforme su [−a, a] ∀a < 3 .



Esercizio 26     [CP 2.30]

 TRACCIA
                                                                             +∞
                                                                             X  5n
      Studiare la convergenza puntuale ed uniforme della serie                          xn .
                                                                                   2n
                                                                             n=1



 PROCEDIMENTO
                                                                                                           √
      Serie di potenze elementare: il fattore polinomiale 5n non inuisce sul raggio, perché
                                                                                                           n
                                                                                                               n → 1.
 Sul bordo il termine cresce linearmente, quindi diverge.



 SVOLGIMENTO E SOLUZIONE
                                 √
                                 n
                    5n √           5n    1         √
     Raggio. cn = n e n cn =          → (poiché n n → 1), dunque ρ = 2.
                    2              2     2
     Estremi x = ±2. Il termine vale 5n
                                      2n (±2)n = ±5n, non innitesimo: diverge in entrambi.

     Convergenza uniforme. Su [−a, a] con a < 2: 5n        n ≤ 5n a n e
                                                                              n
                                                                          n a2 < ∞ (criterio
                                                                       P
                                                      2n x        2
                       2 < 1): convergenza totale, dunque uniforme.
                       a
 del rapporto, ragione


              Converge per |x| < 2 (insieme (−2, 2)); totale/uniforme su [−a, a] ∀a < 2.




Esercizio 27     [CP 2.31]

 TRACCIA
                                                           +∞
                                                           X  n+1
      Determinare l'insieme di convergenza della serie                        xn . (i) Si discuta il tipo di conver-
                                                                        2n
                                                           n=1
 genza. (ii) Si integri la serie termine a termine e si calcoli la somma della serie ottenuta. (iii) Si




                                                   20
 deduca inne la somma della serie di partenza.




 PROCEDIMENTO

    La strategia dei punti (ii)(iii) è un metodo generale da imparare:             la serie di partenza ha
 coecienti con un fattore (n+1) che rende dicile riconoscerla; integrando termine a termine quel
 fattore si semplica con il denominatore n + 1 prodotto dall'integrazione, e resta una geometrica.
 Si somma quella (facile) e poi si riderivano il risultato  lecito perché il teorema di derivazione
 per serie di potenze garantisce che il raggio non cambia.




 SVOLGIMENTO E SOLUZIONE
                                                             √
    Raggio e insieme di convergenza. cn = n+1
                                           2n ,
                                                n c → 1 , quindi ρ = 2. Agli estremi x = ±2
                                                   n  2
 il termine vale ±(n + 1), non innitesimo: diverge.


                                        Insieme di convergenza: (−2, 2).


 (i) La convergenza è    assoluta in (−2, 2) e totale (quindi uniforme) su ogni [−a, a] con a < 2;
 non è uniforme su tutto (−2, 2).
                                                                      Z xX
                                                                              n+1 n
    (ii) Integrazione termine a termine.         Posto F (x)     :=               t dt, scambiando serie e
                                                                      0 n≥1    2n
 integrale (lecito per la convergenza uniforme sui compatti):

                                                                           x
                        Xn+1            xn+1   X xn+1     X  x n
                                                                           2       x2
              F (x) =               ·        =        = x          = x ·        =     .
                               2n       n+1       2n          2          1 − x2   2−x
                        n≥1                     n≥1            n≥1

                                                          ′
    (iii) Somma della serie di partenza. La serie data è F (x):


                              2x(2 − x) − x2 · (−1)   4x − 2x2 + x2           x(4 − x)
        S(x) = F ′ (x) =                            =               =                  ,        |x| < 2.
                                    (2 − x)2             (2 − x)2             (2 − x)2

 Verica:   S(0) = 0, coerente col fatto che la serie in x = 0 vale 0.


Esercizio 28    [CP 2.32]

 TRACCIA
                                                                                   +∞       √
                                                                                   X  n+        n+1
    Determinare l'insieme di convergenza semplice e uniforme della serie                              (x − 4)n .
                                                                                           (2n n)2
                                                                                   n=1
 (È l'esercizio 1 della prova del 3/09/2025.)




 PROCEDIMENTO

    Prima di tutto semplica il coeciente :          (2n n)2 = 4n n2  è il passaggio in cui si sbaglia
 più spesso, e da esso dipende l'intero risultato.          Poi CauchyHadamard per il raggio, e i due
 estremi studiati separatamente: uno dà la serie armonica (diverge), l'altro una serie a segni alterni
 (Leibniz). L'uniformità si estende no all'estremo convergente grazie al teorema di Abel.




 SVOLGIMENTO E SOLUZIONE
                                                 √
    Raggio. Poiché (2n n)2 = 4n n2 e n + n + 1 ∼ n:
                            √
                         n+ n+1    1             √      1
                    an =    n  2
                                 ∼ n  =⇒ lim sup n an =   =⇒ ρ = 4.
                           4 n    4 n       n           4


                                                       21
 Centro x0 = 4: convergenza assoluta per |x − 4| < 4, cioè x ∈ (0, 8).
                                                                             √                        √
    Estremo x = 8 ((x − 4)n = 4n ): il termine diventa n+ n2n+1 = n1 + nn+1
                                                                          2 ; la prima parte è

 armonica (diverge), la seconda converge (∼ n      ): la serie diverge.
                                              −3/2
                                                                     √               √
    Estremo x = 0 ((x − 4) = (−4) ): il termine diventa (−1)n n+ n2n+1 , con bn = n+ n2n+1 → 0
                            n        n

 decrescente denitivamente: per Leibniz la serie converge (semplicemente, non assolutamente).


                   Convergenza semplice: [0, 8);               uniforme: [0, 8 − ε]            ∀ε ∈ (0, 8).
 La convergenza è uniforme sui compatti interni e, per il teorema di Abel, si estende no all'estremo
 sinistro x = 0 dove la serie converge; non è uniforme su tutto [0, 8).



Esercizio 29     [CP 2.33]

 TRACCIA
                                                                             +∞
                                                                             X  (−2)n
      Si studi la convergenza puntuale ed uniforme della serie                                 xn .
                                                                                      n
                                                                             n=1



 PROCEDIMENTO
                      (−2)n n (−2x)n                                                          P un
                                     : la sostituzione u = −2x la riporta alla serie notevole
      Raccogliendo,
                        n x =   n                                                               n =
 − log(1 − u).     È il caso da ricordare a memoria, perché i due estremi hanno comportamento
 asimmetrico : in u = −1 converge per Leibniz, in u = +1 è la serie armonica e diverge.



 SVOLGIMENTO E SOLUZIONE
                       X (−2)n                X un
      Sostituzione.                    xn =             con u := −2x.
                                 n                  n
                       n≥1      n≥1
      Convergenza in u. La serie un ha raggio 1; in u = −1 converge (Leibniz), in u = 1 è la
                                P  n


 serie armonica e diverge. Insieme: u ∈ [−1, 1).
      Ritorno a x. −1 ≤ −2x < 1 ⇐⇒ − 12 < x ≤ 21 .
                                                                                 − 12 , 12 .
                                                                                          
                                     Insieme di convergenza puntuale:


      Somma. Usando              un
                             P
                             n≥1 n = − log(1 − u):


                                 S(x) = − log(1 − (−2x)) = − log(1 + 2x) .

      Convergenza uniforme. Totale su ogni [−a, a] con a < 12 ; per il teorema di Abel si estende
                            1
                                                                                                      −a, 12                  1
                                                                               
 no all'estremo destro x =                                                                                    per ogni a <
                            2 (dove la serie converge), quindi è uniforme su                                                  2.
                                 1
 Non lo è in un intorno di x = − , dove la serie diverge.
                                 2



Esercizio 30     [CP 2.37]

 TRACCIA
                                              +∞
                                              X  (−1)n x3n+4
      Calcolare la somma della serie                               , stabilendo il tipo di convergenza.
                                                        n+1
                                              n=1



 PROCEDIMENTO

    Due mosse: (a) raccogliere le potenze di x che non dipendono dall'indice in modo sommabile
 (x
   3n+4 = x4 · (x3 )n ) e (b) sostituire t = x3 per ricondursi alla serie notevole del logaritmo. Il

 denominatore n + 1 (invece di n) richiede un piccolo riallineamento dell'indice: si moltiplica e




                                                              22
 divide per t in modo da far comparire t
                                                n+1 .




 SVOLGIMENTO E SOLUZIONE

     Riduzione. x3n+4 = x4 (x3 )n ; posto t := x3 ,
                                     X (−1)n x3n+4              X (−1)n tn
                                                         = x4                .
                                                n+1                   n+1
                                     n≥1                        n≥1

     Somma ausiliaria. Moltiplicando e dividendo per t e ponendo m = n + 1:
             X (−1)n tn           1 X (−1)n tn+1   1 X (−1)m−1 tm  1h             i
                              =                  =                = log(1 + t) − t ,
                    n+1           t     n+1        t       m       t
             n≥1                   n≥1                    m≥2

                P        (−1)m−1 tm
 avendo usato      m≥1       m      = log(1 + t) e sottratto il termine m = 1, che vale t.
     Somma nale.
                                          log(1 + x3 ) − x3
                            S(x) = x4 ·                     = x log(1 + x3 ) − x4 .
                                                 x3
     TipoPdi convergenza. La serie in t converge per |t| < 1 e, in t = 1, per Leibniz; in t = −1
             1
 diventa
            n+1 , divergente. Quindi −1 < t ≤ 1, cioè

                         x ∈ (−1, 1] :      assoluta per |x| < 1, semplice in x = 1.


 Uniforme (totale) su [−a, a] con a < 1 e, per Abel, su [−a, 1].



Esercizio 31    [CP 2.38]

 TRACCIA
                                           +∞
                                           X       1
     Calcolare la somma della serie                      x3n−1 , stabilendo il tipo di convergenza.
                                                (n − 1)!
                                          n=1



 PROCEDIMENTO

     Il fattoriale (n − 1)! segnala l'esponenziale. La mossa è il        cambio di indice k = n − 1, che
                                                P tk      t
 allinea il fattoriale a k! e fa comparire
                                                    k! = e . Le potenze di x in eccesso si raccolgono fuori
 dalla somma.




 SVOLGIMENTO E SOLUZIONE

     Cambio di indice. Ponendo k = n − 1 (quindi n = k + 1, e 3n − 1 = 3k + 2):
                            X x3n−1     X x3k+2      X (x3 )k         3
                                      =         = x2          = x2 e x .
                             (n − 1)!       k!           k!
                            n≥1              k≥0                k≥0

    Tipo di convergenza. La serie esponenziale ha raggio ρ = +∞: la convergenza è assoluta
 per ogni x ∈ R, e totale (dunque uniforme) su ogni intervallo limitato [−a, a], poiché lì x k! ≤
                                                                                            3k+2


  a3k+2     P a3k+2   2 a3 < ∞. Non è uniforme su tutto R (la somma è illimitata).
    k!  con
                k! = a e



Esercizio 32    [CP 2.39]




                                                         23
TRACCIA
                                            +∞
                                            X
   Calcolare la somma della serie                (−1)n nx2n−1 , stabilendo il tipo di convergenza.
                                            n=1



PROCEDIMENTO

   La presenza del fattore n e dell'esponente 2n − 1 suggerisce una                   derivata: infatti dx
                                                                                                         d 2n
                                                                                                           x =
2nx2n−1 . Si riconosce quindi la serie come la derivata (a meno del fattore 21 ) di una geometrica in
−x2 , che si somma subito. È la mossa speculare a quella dell'es. 27, dove si era invece integrato.


SVOLGIMENTO E SOLUZIONE
                                                                d
   Riconoscimento della derivata. Poiché                          (−x2 )n = (−1)n 2nx2n−1 :
                                                                         
                                                               dx
                                      X                             1 d X
                                           (−1)n nx2n−1 =                 (−x2 )n .
                                                                    2 dx
                                      n≥1                                 n≥1

   Somma della geometrica. Per x2 < 1, con ragione q = −x2 :
                                                  X                   −x2
                                                      (−x2 )n =             .
                                                                     1 + x2
                                                  n≥1

   Derivazione (lecita: il teorema di derivazione per serie di potenze conserva il raggio):
                          −x2             1 −2x(1 + x2 ) + x2 · 2x
                                 
              1 d                                                   1    −2x                     −x
       S(x) =                         =     ·                      = ·           =                       .
              2 dx       1 + x2           2             2
                                                 (1 + x ) 2         2 (1 + x2 )2              (1 + x2 )2

   Tipo di convergenza. Raggio ρ = 1; agli estremi x = ±1 il termine vale ±n, non innitesimo,
quindi diverge. Convergenza assoluta su (−1, 1), totale (uniforme) su ogni [−a, a] con a < 1.




RIEPILOGO: LE QUATTRO SERIE NOTEVOLI DA RICONOSCERE A VISTA


                            X               1                X             q
                                  qn =         ,                   qn =         (|q| < 1)
                                           1−q                            1−q
                            n≥0                              n≥1

     X un                                                      X (−1)m−1 um
               = − log(1 − u) (−1 ≤ u < 1),                                      = log(1 + u) (−1 < u ≤ 1)
           n                                                               m
     n≥1                                                       m≥1

                                                  X tk
                                                             = et (t ∈ R)
                                                        k!
                                                  k≥0

Le due manovre da avere in mano: se compare un fattore n al numeratore, la serie è la
derivata di una nota (es. 32); se compare al denominatore ( n1 , n+1
                                                                  1
                                                                     ), è l'integrale di una nota
(es. 27, 29, 30).

   Sulla convergenza totale: il criterio di Weierstrass è la prima cosa da provare sempre.
Quando fallisce, il motivo è quasi sempre che il sup del termine n-esimo si realizza in un punto xn
                                                                                                             1
che si sposta con n, e l'altezza corrispondente non è sommabile: confronta l'es. 22 (altezza ∝
                                                                                                             n,
fallisce) con l'es. 23 (altezza ∝ n
                                          −3/2 , funziona).




                                                               24
3 Esercizi comparsi nei temi d'esame
 PERCHÉ QUESTA SEZIONE ESISTE

    Raccoglie i tre esercizi d'esame che non ricadevano nelle sezioni nora svolte, così che         tutti
 gli esercizi con riscontro nei temi d'esame risultino risolti. Gli altri quattro (es. 10, 28, 75, 187) si
 trovano nelle rispettive sezioni.



Esercizio 61   [CP 4.19  prova del 17/09/2025, es. 3]

 TRACCIA
                                                  x
    Si consideri il problema di Cauchy y
                                            ′ = xe , y(0) = y . Esiste qualche valore di y per cui la
                                                             0                            0
                                                 2y
 soluzione sia costante? Determinare la soluzione nel caso y0 = −1.




 PROCEDIMENTO

    Per la prima domanda non risolvere: imponi y ≡ c e verica se l'equazione può valere su un
 intervallo. Per la seconda, variabili separabili con integrazione per parti; non dimenticare la scelta
 del segno della radice (dettata dal dato iniziale) e lo studio del dominio.




 SVOLGIMENTO E SOLUZIONE

     (a) Se y ≡ c, allora y ′ ≡ 0 e servirebbe xe2c = 0 per ogni x di un intervallo; ma xex = 0 solo
                                                  x


 nel punto isolato x = 0. Non esiste alcun y0 .
     (b) Separando: 2y dy = xex dx, e integrando per parti a destra ( xex dx = xex − ex ):
                                                                       R


                    y 2 = ex (x − 1) + C;      y(0) = −1 ⇒ 1 = −1 + C ⇒ C = 2.

 Essendo y0 < 0 si sceglie il ramo negativo:

                                               p
                                       y(x) = − ex (x − 1) + 2 .

 Dominio. h(x) := ex (x − 1) + 2 ha h′ (x) = xex , negativa per x < 0 e positiva per x > 0: minimo
 in x = 0 con h(0) = 1 > 0. Dunque h > 0 su tutto R e la soluzione è globale.



Esercizio 115   [CP 8.12  prova del 17/09/2025, es. 2]

 TRACCIA
                                   4
    Sia f (x, y) = −αx
                        2 + y 2 + x , con α ∈ R. i) Trovare i punti critici al variare di α e classicarli;
                                 4
                     2
 ii) determinare f (R ).



 PROCEDIMENTO

    Il gradiente si fattorizza e il numero di punti critici dipende dal segno di α: la discussione va
 organizzata sui casi α < 0, α = 0, α > 0. Per l'immagine basta osservare che y
                                                                                         2 copre [0, +∞)

 indipendentemente da x: tutto si riduce al minimo di g(x) = f (x, 0).




 SVOLGIMENTO E SOLUZIONE
                                                                                       √
    ∇f = x(x2 − 2α), 2y : da y = 0 e x(x2 − 2α) = 0 segue x = 0 oppure, se α > 0, x = ± 2α.
                       
                           2
 Hessiana H = diag(−2α + 3x , 2).

  α < 0: unico punto (0, 0), H = diag(−2α, 2) denita positiva ⇒ minimo (assoluto: f =


                                                      25
                      4
    |α|x2 + y 2 + x4 ≥ 0).

   α = 0: (0, 0) con H degenere; direttamente f0 = y 2 + x4 ≥ 0: minimo assoluto.
                                                                      4


                                                               √
   α > 0: (0, 0) ha H = diag(−2α, 2) indenita ⇒ sella; in (± 2α, 0) si ha −2α + 3x2 = 4α > 0,
    H denita positiva ⇒ minimi, di valore −α2 .
                                            (
                                             [0, +∞)      α≤0
                                  f (R2 ) =       2
                                             [−α , +∞) α > 0.


Esercizio 129       [CP 8.24  prova del 3/09/2025, es. 2]

 TRACCIA
                               2
     Sia f (x, y)   = x2 + y2 + x2 y + 2.       (i) Determinare i punti critici liberi e classicarli.   (ii)
 Determinare massimo e minimo assoluti nella regione triangolare chiusa di vertici (0, 0), (1, −1),
 (1, 0).


 PROCEDIMENTO

     Problema di Weierstrass su un compatto: procedura interno + bordo.               Prima verica quali
 punti critici cadono internamente (qui nessuno), poi parametrizza i tre lati riducendoli a funzioni
 di una variabile. Se tutti i lati sono monotoni, gli estremi cadono nei vertici.




 SVOLGIMENTO E SOLUZIONE

     ∇f = 2x(1 + y), y + x2 : punti critici (0, 0), (1, −1), (−1, −1). Con fxx = 2 + 2y , fxy = 2x,
                               

 fyy = 1, det H = (2 + 2y) − 4x2 : (0, 0) minimo (det = 2 > 0, fxx > 0, f = 2); (±1, −1) selle
                     5
 (det = −4 < 0, f = ).
                     2
     (ii) Nessun punto critico è interno a T : (0, 0) e (1, −1) sono vertici, (−1, −1) è esterno. Sui
                                3 2   3        ′
 lati: OA (y = −x): g(x) = x − x + 2, g = 3x(1 − x) ≥ 0 su [0, 1]: crescente da 2 a . AB
                                                                                               5
                                2                                                              2
                         y 2
 (x = 1): h(y) = 3 + y +
                                 ′
                             , h = 1 + y ≥ 0: crescente da
                                                             5                     2
                                                               a 3. BO (y = 0): x + 2, crescente da
                          2                                  2
 2 a 3. Tutti monotoni ⇒ estremi nei vertici:

                                   max f = 3 in (1, 0),        min f = 2 in (0, 0).
                                    T                           T




                                                          26
4 Serie di Fourier
 SCHEMA GENERALE


  1.   Sfrutta subito la simmetria: f pari ⇒ bn = 0 (soli coseni); f dispari ⇒ an = 0 (soli seni).
       Dimezza il lavoro e va sempre controllata per prima.

  2.   Adatta le formule al periodo. Con periodo T e semiperiodo L = T /2, la pulsazione è
       ω = 2π    π
            T = L e
               Z                                            Z
             2                                          2                                             a0 X                      
       an =           f (x) cos(nωx) dx,           bn =                f (x) sin(nωx) dx,        f∼     +  an cos nωx+bn sin nωx .
             T periodo                                  T   periodo                                   2
                                                                                                         n≥1

       Usare le formule del caso 2π -periodico quando T ̸= 2π è l'errore più frequente.

  3.   Convergenza: se f è C 1 a tratti, la serie converge puntualmente a f nei punti di continuità
       e alla media dei limiti laterali nei salti; converge uniformemente sugli intervalli chiusi privi di
       salti, e su tutto R se f è ovunque continua. Vicino ai salti compare il fenomeno di Gibbs.

 Verica dei punti di salto: vanno controllati, non dati per scontati  spesso una funzione
 denita a tratti risulta continua nei punti di raccordo interni e discontinua solo agli estremi del
 periodo (o viceversa).



Esercizio 33     [S9 1]

 TRACCIA

       Serie di Fourier della funzione 2π -periodica f (x) = π − |x| per x ∈ (−π, π], e studio della
 convergenza puntuale e uniforme.




 PROCEDIMENTO

       f è pari (|x|), quindi solo coseni. Inoltre è continua su tutto R (agli estremi f (±π) = 0 e si
 raccorda), il che darà convergenza uniforme ovunque.




 SVOLGIMENTO E SOLUZIONE

       Simmetria. f pari ⇒ bn = 0.
                                     Z π                         Z π
                                 1                          2      2 π2
                          a0 =             (π − |x|) dx =            · (π − x) dx =
                                                                          = π.
                               −ππ                 0        π      π 2

                      2 π
                       Z                           Z π              Z π
                                               2h                                   i
                 an =     (π − x) cos(nx) dx =   π     cos(nx) dx −     x cos(nx) dx .
                      π 0                      π
                                                 | 0 {z         }    0
                                                                               =0
                                 h                    iπ
           Rπ                        x sin nx                   (−1)n −1
 Poiché
            0 x cos(nx) dx =             n    + cosn2nx =         n2
                                                                           :
                                                       0
                                                                     
                                             2     1 − (−1)n         0             n pari
                                      an =     ·                 =
                                             π        n2              4            n dispari.
                                                                      πn2

                                               π X     4                    
                                     f (x) =     +            cos (2k + 1)x
                                               2   π(2k + 1)2
                                                     k≥0




                                                                27
 Convergenza. f è continua su tutto R e C 1 a tratti (punti angolosi in x ≡ 0, π ): la serie converge
 a f (x) per ogni x e la convergenza è uniforme su tutto R (nessun salto, nessun Gibbs).



Esercizio 34    [S9 2]

 TRACCIA

     Serie di Fourier della funzione 2π -periodica f (x) = 0 se −π ≤ x ≤ 0, f (x) = 1 se 0 < x < π , e
 studio della convergenza.




 PROCEDIMENTO

     Nessuna simmetria utile (non è né pari né dispari), ma il calcolo è elementare perché f vale 0
 o 1. È l'onda quadra : attenzione ai due salti per periodo.




 SVOLGIMENTO E SOLUZIONE

                            Z π                                 Z π
                      1                                 1                            1 h sin nx iπ
                 a0 =                1 dx = 1;     an =               cos(nx) dx =                 = 0;
                      π         0                       π        0                   π      n    0
                                                                         
                           1
                                     Z π
                                                        1               0       n pari
                                                            1 − (−1)n =
                                                                     
                      bn =                sin(nx) dx =
                           π          0                nπ                 2 n dispari.
                                                                           nπ
                                                1 X          2                  
                                        f (x) ∼ +                 sin (2k + 1)x
                                                2       (2k + 1)π
                                                   k≥0

 Convergenza. Salti in x ≡ 0 e x ≡ π (mod 2π ). La serie converge a f nei punti di continuità
                0+1
 e alla media
                 2       = 12 in entrambi i salti (coerente col fatto che tutti i seni si annullano lì).
 Convergenza uniforme su ogni chiuso privo di salti; fenomeno di Gibbs in loro prossimità.



Esercizio 35    [S9 3]

 TRACCIA

    Serie di Fourier della funzione 2π -periodica f (x) = − cos x se −π ≤ x ≤ 0, f (x) = cos x se
 0 < x < π , e studio della convergenza.


 PROCEDIMENTO

     Verica la simmetria: f (−x) = −f (x), quindi f è dispari e restano solo i seni. Nel calcolo di
 R
   cos x sin(nx) conviene la formula di Werner, che trasforma il prodotto in somma; il caso n = 1
 va trattato a parte perché genera sin(0).




 SVOLGIMENTO E SOLUZIONE

     Simmetria. Per x ∈ (0, π): f (−x) = − cos(−x) = − cos x = −f (x): f è dispari, dunque
 an = 0.                   Z π                             Z π
                     2                                 1                                         
                bn =                cos x sin(nx) dx =               sin((n + 1)x) + sin((n − 1)x) dx,
                     π      0                          π    0
                           1
                                                                               Rπ                  1−(−1)m
 avendo usato sin α cos β = [sin(α + β) + sin(α − β)]. Poiché                                              per m ̸= 0
                           2                                                    0 sin(mx) dx =        m
 e = 0 per m = 0:

   n = 1: b1 = π1 1−1
                          
                    2  + 0   = 0;



                                                            28
                     h                     i
                         1+(−1)n         n
   n ≥ 2: bn = π1         n+1   + 1+(−1)
                                     n−1   , nullo per n dispari e, per n pari, =
                                                                                  2    2n
                                                                                  π · n2 −1 .
                                                  X         8k
                                        f (x) ∼                     sin(2kx)
                                                        π(4k 2 − 1)
                                                  k≥1

 Convergenza. Salti in x ≡ 0 (da −1 a 1) e in x ≡ π : in entrambi la serie converge alla media 0.
 Altrove converge a f ; uniforme sui chiusi privi di salti.



Esercizio 36   [S9 4]

 TRACCIA
                                                                         1
    Serie di Fourier della funzione 2π -periodica f (x) = 1 +
                                                                         2 x per x ∈ [0, 2π), prolungata per
 periodicità, e studio della convergenza.




 PROCEDIMENTO

    Nessuna simmetria (il periodo è centrato in π , non in 0): si integra su [0, 2π].           Il calcolo è
                                                                                                    1
 quello del dente di sega: i coseni si annullano tutti, restano solo i seni con coecienti −
                                                                                                    n.



 SVOLGIMENTO E SOLUZIONE



                                1 2π 
                                  Z
                                          x       1
                                                       2π + π 2 = 2 + π.
                                                                
                           a0 =        1+     dx =
                                π 0       2        π
        R 2π                    R 2π                x sin nx           2π
 Poiché
         0   cos(nx) dx = 0 e 0 x cos(nx) dx =           n    + cosn2nx 0 = 0:            an = 0.    Poiché
 R 2π                 R 2π               x cos nx sin nx 2π
  0 sin(nx) dx = 0 e 0 x sin(nx) dx = −      n    + n2 0 = − 2π       n :

                                                  1 1  2π    1
                                          bn =     · · −     =− .
                                                  π 2    n     n

                                                         π X sin(nx)
                                          f (x) ∼ 1 +      −
                                                         2      n
                                                               n≥1

 Convergenza. Salto in x ≡ 0 (mod 2π ): f (0+ ) = 1, f (2π − ) = 1 + π ; la serie vi converge alla
             π
 media 1 +
             2 , che è esattamente il termine costante (i seni si annullano in 0)  ottima verica del
 risultato. Altrove converge a f , uniformemente sui chiusi privi di salti.



Esercizio 37   [S9 5]

 TRACCIA

    f dispari, 2-periodica, denita da f (x) = 1 se x ∈ (0, 1). Determinarne la serie di Fourier e
 studiarne la convergenza.




 PROCEDIMENTO

    Periodo T = 2, quindi L = 1 e ω = π : non si usano le formule del caso 2π -periodico. Dispari
 ⇒ soli seni. È l'onda quadra classica.


 SVOLGIMENTO E SOLUZIONE




                                                          29
    Con T = 2, L = 1, e f dispari (an = 0):

                                                                              0
                                                                           n                              n pari
                 Z L                           Z 1                
             2                   nπx                           2 1 − (−1)
      bn =             f (x) sin        dx = 2     sin(nπx) dx =              =
             L    0                L            0                     nπ         4                       n dispari.
                                                                                 nπ
                                                   X           4                   
                                         f (x) ∼                     sin (2k + 1)πx
                                                           (2k + 1)π
                                                   k≥0

 Convergenza. f ha salti in tutti gli interi (da −1 a 1 in x ≡ 0): la serie vi converge a 0 (media),
 altrove a f ; uniforme sui chiusi privi di interi.



Esercizio 38     [S9 6]

 TRACCIA

    f di periodo T = 3, con f (x) = x su [0, 1), f (x) = 1 su [1, 2), f (x) = 3 − x su [2, 3).
 Determinarne la serie di Fourier e studiarne la convergenza.




 PROCEDIMENTO

    Prima di calcolare, cerca una simmetria nascosta : si verica che f (3 − x) = f (x), cioè, per
 periodicità,    f (−x) = f (x).         Dunque f è         pari e bn = 0, benché la denizione a tratti non lo
 suggerisca aatto. Questa osservazione dimezza il lavoro.




 SVOLGIMENTO E SOLUZIONE

    Simmetria. Per x ∈ [0, 1) si ha 3−x ∈ (2, 3] e f (3−x) = 3−(3−x) = x = f (x); analogamente
 sugli altri tratti. Per periodicità f (−x) = f (3 − x) = f (x): f è pari, dunque bn = 0.
                            2π
    Con T = 3 e ω =
                             3 :
                                   Z 3
                               2              2h 1            1
                                                                i 4                              a0  2
                          a0 =           f=       2  +  1  +  2  =                      =⇒          = ,
                               3    0         3 |{z}   |{z} |{z}   3                             2   3
                                                   [0,1)     [1,2)    [2,3)

                      2
                      3 è il valor medio di f su un periodo.
 coerente col fatto che
                                                  3                                     3
                                                                                           
    Sfruttando la parità rispetto al centro x =
                                                  2 e riportandosi in x (con cos nω(x − 2 ) =
 (−1)n cos(nωx), poiché nω · 23 = nπ ) si ottiene

                     3 (−1)n cos nπ
                                      
                                  3 −1                                                  2 X         2πnx 
                an =                     ,                  bn = 0,           f (x) ∼     + an cos          .
                           n2 π 2                                                       3              3
                                                                                           n≥1


 Si noti che an = 0 per n multiplo di 3.
     Convergenza. f è continua su tutto R (i raccordi in x = 1, 2, 3 coincidono) e C 1 a tratti: la
 serie converge a f ovunque e uniformemente su tutto R.



Esercizio 39     [S9 7]

 TRACCIA

    Serie di Fourier di f (x) = 1 − x
                                              2 per x ∈ [−1, 1], prolungata periodicamente (T = 2), e studio

 della convergenza.




                                                                 30
 PROCEDIMENTO

    Pari ⇒ soli coseni; T       = 2, L = 1, ω = π . La funzione è continua nel raccordo (f (±1) = 0),
                                                                                                  1
 quindi ci si aspetta convergenza uniforme e coecienti che decadono come                            .
                                                                                                  n2



 SVOLGIMENTO E SOLUZIONE

    f pari ⇒ bn = 0. Con T = 2:
                   Z 1                 Z 1
                             2                               2  4                                 a0  2
              a0 =     (1 − x ) dx = 2     (1 − x2 ) dx = 2 · =                          =⇒          = .
                    −1                  0                    3  3                                 2   3
                 Z 1                                Z 1                                     Z 1
          an =         (1 − x2 ) cos(nπx) dx = 2          (1 − x2 ) cos(nπx) dx = −2              x2 cos(nπx) dx,
                  −1                                  0                                       0
          R1                                                                 R1                 2(−1)      n
                                                                                 2
 poiché
            0 cos(nπx) dx = 0. Integrando due volte per parti,                0 x cos(nπx) dx = n2 π 2 , quindi

                                                      4(−1)n    4(−1)n+1
                                             an = −           =          .
                                                       n2 π 2     n2 π 2

                                                   2 X 4(−1)n+1
                                        f (x) =      +          cos(nπx)
                                                   3     n2 π 2
                                                       n≥1

 Convergenza. f è continua su R e C 1 a tratti (angoli negli interi dispari): convergenza a
 f ovunque e uniforme su tutto R (i coecienti sono O(n−2 ), quindi c'è anche convergenza
 totale).



Esercizio 40     [S9 8]

 TRACCIA

    f dispari, 2-periodica, denita da f (x) = πx2 per x ∈ [0, 1). Determinarne la serie di Fourier
 e studiarne la convergenza.




 PROCEDIMENTO
                                                                   R1       2 sin(nπx) richiede due integrazioni per
    Dispari ⇒ soli seni, con L = 1, ω = π . L'integrale
                                                                    0 x
                                   1            1
 parti e produce sia un termine in
                                   n sia uno in n3 .



 SVOLGIMENTO E SOLUZIONE

    an = 0 e                           Z 1                          Z 1
                                               2
                              bn = 2         πx sin(nπx) dx = 2π            x2 sin(nπx) dx.
                                        0                               0
 Integrando due volte per parti:

                                                                      n−1
                                Z 1                                      
                                                      (−1)n   2  (−1)
                                   x2 sin(nπx) dx = −       +               ,
                                 0                     nπ          n3 π 3

 da cui
                                 2(−1)n 4 (−1)n − 1
                                                  
                                                                                  X
                          bn = −       +             ,              f (x) ∼             bn sin(nπx).
                                   n        n3 π 2
                                                                                  n≥1

 Convergenza. Nei punti x ≡ 1 (mod 2) c'è un salto: f (1− ) = π e, per disparità e periodicità,
 f (1+ ) = −π ; la serie vi converge alla media 0. Anche in x ≡ 0 c'è salto (da 0− a 0+ la funzione


                                                             31
 dispari si raccorda con continuità: f (0) = 0, quindi lì è continua). Altrove converge a f ; uniforme
                                                                        1
 sui chiusi privi dei punti di salto. La presenza del termine
                                                                        n conferma la discontinuità.



Esercizio 41       [CP 2.40]

 TRACCIA
                                                                                               π
     Si consideri la funzione f , 2π -periodica, tale che f (x) = 1 per 0 ≤ x ≤
                                                                                               2 e f (x) = −1 per
  π
  2 < x ≤ π . (i) Discutere la convergenza della serie di Fourier; (ii) scrivere la serie di Fourier di f .



 PROCEDIMENTO

     Attenzione: il testo denisce f solo su [0, π], cioè su mezzo periodo, ma la dichiara 2π -
 periodica.    Manca quindi l'informazione su [−π, 0) e la risposta dipende dall'estensione scelta.
 Adotto l' estensione dispari (la più frequente in questi eserciziari, e l'unica che rende la funzione
 ben denita come onda a valori ±1); segnalo la scelta perché va dichiarata anche in sede d'esame.




 SVOLGIMENTO E SOLUZIONE

     Estensione dispari. Posto f (−x) = −f (x), si ha an = 0 e
                               Z π
                                                        2 h π/2
                                                           Z                Z π
                          2                                                               i
                     bn =            f (x) sin(nx) dx =        sin(nx) dx −     sin(nx) dx .
                          π     0                       π 0                  π/2

          R π/2                     1−cos nπ   Rπ                cos nπ −(−1)n
 Poiché
           0      sin(nx) dx =         n
                                           2
                                             e
                                                π/2 sin(nx) dx =      2
                                                                        n      :


                                 2 h           nπ        i                     X
                        bn =         1 − 2 cos    + (−1)n ,          f (x) ∼         bn sin(nx).
                                nπ              2
                                                                               n≥1

                                                4                          8
 Esplicitamente: bn = 0 per n ≡ 2 (mod 4); bn =
                                               nπ per n dispari; bn = nπ per n ≡ 0 (mod 4).
     (i) Convergenza. f è C a tratti con salti in x ≡ 0, ± 2 , π : la serie converge alla media dei
                           1                               π

 limiti laterali in tali punti (rispettivamente 0, 0, 0) e a f altrove; uniforme sui chiusi privi di salti,
 con fenomeno di Gibbs in loro prossimità.



Esercizio 42       [CP 2.41]

 TRACCIA

     Sia f (x) = x
                     2 per x ∈ [0, π], ripetuta periodicamente fuori da [0, π]. (a) Calcolare i coecienti

 di Fourier rispetto alla base trigonometrica. (b) Calcolare lo scarto quadratico medio tra f e la
 sua media.




 PROCEDIMENTO

     Il punto cruciale: ripetuta fuori da [0, π] signica       periodo T = π , non 2π ; quindi ω = 2π
                                                                                                      T =2
 e nelle formule compaiono cos(2nx), sin(2nx). Per (b) si usa Parseval: lo scarto quadratico medio
 rispetto alla media è la radice dell'energia delle sole armoniche n ≥ 1 (il termine costante è proprio
 la media).




 SVOLGIMENTO E SOLUZIONE




                                                           32
     (a) Con T = π , ω = 2:
                                                Z π
                                            2                      2π 2    a0   π2
                                       a0 =           x2 dx =           =⇒    =    .
                                            π    0                  3      2    3
                                                                         2 sin(2nx) dx = − π 2 , da cui
                           Rπ        2 cos(2nx) dx =     π
                                                                 Rπ
 Integrando per parti,
                               0 x                      2n2
                                                            e
                                                                   0 x                     2n


                        1                  π                       π 2 Xh cos(2nx) π           i
               an =        ,         bn = − ,          f (x) ∼        +           −   sin(2nx)  .
                        n2                 n                       3         n2     n
                                                                           n≥1



    R (b) La 2media di f su un periodo è
                                                          a0         π2
                                                          2    =     3 .    Per l'identità di Parseval, con        E(g) :=
  2
  T periodo |g| :

                    a0  X 2       X 1   π2  π4      2 π
                                                             2   8π 4
                E f−     = an + b2n =     +     =    + π  ·    =      .
                     2                 n4 n2      90        6     45
                                       n≥1                 n≥1

                                                                                              1
                                                                                                      |f − media|2 = 12 E(·):
                                                                                                  R
 Lo scarto quadratico medio è la radice del valor medio del quadrato, cioè
                                                                                              T

                                                          r
                                                               4π 4   2π 2
                                                     σ=             = √
                                                                45   3 5


Esercizio 43   [CP 2.42]

 TRACCIA

     Discutere la convergenza della serie di Fourier associata a f (x) = 1 − x
                                                                                                  2 per x ∈ [−1, 1], estesa

 per periodicità su R, e scriverne la serie.




 PROCEDIMENTO

     È la stessa funzione dell'esercizio 39: il calcolo è già svolto lì. Qui l'accento è sulla discussione
 della convergenza.




 SVOLGIMENTO E SOLUZIONE

     Dall'esercizio 39:
                                                     2 X 4(−1)n+1
                                         f (x) =       +          cos(nπx).
                                                     3     n2 π 2
                                                        n≥1

 Discussione. f è 2-periodica, continua su tutto R (nei raccordi x = ±1 vale 0 da entrambi i
 lati) e di classe C
                       1 a tratti (nei punti x dispari la derivata ha un salto, ma la funzione no). Per il

 teorema di convergenza:

   la serie converge puntualmente a f (x) per ogni x ∈ R (nessun punto di salto);

   la convergenza è uniforme su tutto R; anzi è totale, poiché
                                                                P         P 4
                                                                  |an | =  n2 π 2
                                                                                  < ∞ (criterio
    di Weierstrass);


   non si presenta il fenomeno di Gibbs, proprio per l'assenza di discontinuità.


Esercizio 44   [CP 2.43]

 TRACCIA

     Funzione periodica di periodo 4, dispari, con f (x) = x per 0 ≤ x ≤ 1 e f (x) = 2 − x per




                                                                33
 1 < x ≤ 2. (i) Discutere la convergenza; (ii) scriverne la serie di Fourier.


 PROCEDIMENTO

     T = 4, L = 2, ω = π2 ; dispari ⇒ soli seni. C'è inoltre la simmetria f (2 − x) = f (x) (onda
 triangolare), che fa annullare i bn di indice pari: conviene notarla, perché dimezza i termini.




 SVOLGIMENTO E SOLUZIONE
                                      nπ
    Con an = 0, L = 2 e k :=
                                       2 :
                        Z 2                           Z 1                      Z 2
                 bn =         f (x) sin(kx) dx =            x sin(kx) dx +              (2 − x) sin(kx) dx.
                         0                             0                           1

 Nel secondo integrale la sostituzione w = 2−x (e sin(2k −kw) = −(−1)
                                                                                               n sin(kw), poiché 2k = nπ )
         n 1 w sin(kw) dw . Dunque
          R
 dà −(−1)
            0
                                         Z 1
                                                                        cos k sin k 
                 bn = 1 − (−1)n                x sin(kx) dx = 1 − (−1)n −
                                                           
                                                                               + 2 .
                                             0                              k    k
                                                                     n−1
                                               nπ          nπ
 Per n pari bn = 0; per n dispari cos
                                                2 = 0 e sin 2 = (−1)
                                                                      2 , quindi



                                n−1                                                       n−1
                     8 (−1) 2                                             X        8(−1) 2        nπx 
                bn =                  (n dispari),           f (x) =                          sin        .
                        n2 π 2                                                       n2 π 2         2
                                                                       n dispari


 (i) Convergenza. f è l'onda triangolare: continua su tutto R e C 1 a tratti, quindi la serie
 converge a f ovunque e uniformemente su R (coecienti O(n
                                                            −2 ): convergenza anche totale).

 Nessun fenomeno di Gibbs.



Esercizio 45   [CP 2.45]

 TRACCIA
                                                               2
     (a) Calcolare lo sviluppo in serie di Fourier di f (x) = x su (−π, π], ripetuta periodicamente.
                                                   1
 (b) Usando la formula di Werner sin α cos β = 2 [sin(α + β) + sin(α − β)], trovare lo sviluppo di
 f (x) = x cos x su (−π, π].


 PROCEDIMENTO
                                    2
     (a) è lo sviluppo classico di x (2π -periodico, pari): da ricordare a memoria, perché valutandolo
                                               dispari
               P 1       2
 in x = π dà
                  n2
                     = π6 . (b) x cos x è        : soli seni, e Werner riduce cos x sin(nx) a una somma
 di seni, di cui si conosce l'integrale. Il caso n = 1 va isolato.




 SVOLGIMENTO E SOLUZIONE
                                                                                                              n
    (a) f pari ⇒ bn = 0; a0 = π1 −π
                                 π                           2                Rπ
                                    x2 dx = 2π3                           2            2 cos(nx) dx = 4(−1) :
                                         R
                                                                 e an =
                                                                          π   0 x                       n2


                                                    π 2 X 4(−1)n
                                             x2 =      +         cos(nx)
                                                    3       n2
                                                           n≥1


    (b) g(x) = x cos x è dispari ⇒ an = 0. Con Werner, cos x sin(nx) = 12 [sin((n + 1)x) + sin((n −




                                                             34
                         Rπ                             π(−1)m
 1)x)], e usando          0 x sin(mx) dx = −              m    (m ̸= 0), = 0 per m = 0:

                                                  Z π
                                              1                                       
                                      bn =              x sin((n + 1)x) + sin((n − 1)x) dx.
                                              π    0
                                                                                                          h
                                                            b1 = π1 − π2 = − 21 . Per n ≥ 2: bn = −(−1)n+1 n+1
                                                                                                            1
                                                                        
 Per n = 1 resta solo il primo addendo:                                                                        +
        i            n
   1
  n−1       = 2n(−1)
               n2 −1
                     .

                                                      1        X 2n(−1)n
                                           x cos x = − sin x +           sin(nx)
                                                      2           n2 − 1
                                                                       n≥2

 Convergenza. In (a) f è continua: convergenza uniforme su R. In (b) g ha salto in x ≡ π
 (g(π
        − ) = −π , g(π + ) = π ): la serie vi converge a 0, uniformemente sui chiusi che lo evitano.



Esercizio 46         [CP 2.47]

 TRACCIA
                                                       2π                          4π
    Funzione 2π -periodica con f (x) = x per x ∈ [0,
                                                        3 ] e f (x) = 0 per x ∈ (− 3 , 0), ripetuta
 periodicamente. (a) Calcolare i coecienti di Fourier. (b) Discutere la convergenza.




 PROCEDIMENTO

                          − 4π   2π
                                      
    L'intervallo
                             3 , 3        ha ampiezza esattamente 2π : è un periodo completo, solo non centrato
 in 0. Nessuna simmetria; il contributo all'integrale viene solo dal tratto in cui f = x.




 SVOLGIMENTO E SOLUZIONE
                         2π
    Posto α :=
                          3 , poiché f ≡ 0 sul resto del periodo:
                                                               Z α
                                                           1                  α2   2π
                                                   a0 =              x dx =      =    .
                                                           π    0             2π    9
              Rα                                                       Rα
 Usando
               0   x cos(nx) dx = α sin(nα)
                                      n     + cos(nα)−1
                                                  n2
                                                        e
                                                                        0   x sin(nx) dx = − α cos(nα)
                                                                                                 n     + sin(nα)
                                                                                                            n2
                                                                                                                 :



                           1 h 2π     2πn cos 2πn
                                               3 −1
                                                    i                               1 h 2π   2πn sin 2πn
                                                                                                       3
                                                                                                         i
                   an =           sin    +            ,                      bn =      − cos    +         .
                           π 3n        3       n2                                   π   3n    3     n2

    (b) Convergenza. f è C 1 a tratti. In x = 0 è continua (0 da entrambi i lati); in x = 2π 3 ha
 un salto da
             2π                                        π
                a 0, e lì la serie converge alla media   . Altrove converge a f ; uniformemente su
              3                                        3
                                                               2π
 ogni chiuso che non contenga i punti x ≡
                                                                3 (mod 2π ), con fenomeno di Gibbs in loro prossimità.



Esercizio 47         [CP 2.48]

 TRACCIA
                              √
    Sia f (x) = cos( 2x) per x ∈ [− π2 , π2 ], ripetuta periodicamente. (a) Calcolarne i coecienti di
                               1                                                                    π
 Fourier (usando cos A cos B = [cos(A + B) + cos(A − B)]). (b) Valutando lo sviluppo in x = ,
                               2                                                                    2
           +∞
          X      1
 calcolare                        .
                     2k 2 − 1
               k=1




                                                                      35
 PROCEDIMENTO

    Il periodo è T        = π (l'intervallo dato ha ampiezza π ), quindi ω = 2. La funzione è pari: soli
 coseni. Il punto (b) è l'applicazione tipica: si valuta la serie in un punto di continuità e si risolve
 rispetto alla somma incognita.




 SVOLGIMENTO E SOLUZIONE

    (a) f pari ⇒ bn = 0. Con T = π , ω = 2:
                                                                    π    √
                                                     √       4 sin √2
                                        Z π/2
                                   4                                    2 2     π
                              a0 =              cos( 2x) dx = · √     =     sin √ .
                                   π     0                   π     2     π       2
 Con la formula di prostaferesi suggerita,

                                                              √                    √
                                  √                  2 h sin ( 2 + 2n) π2     sin ( 2 − 2n) π2 i
                    Z π/2                                                                    
                4
           an =               cos( 2x) cos(2nx) dx =         √              +     √             .
                π     0                              π         2 + 2n               2 − 2n
            π
                        = (−1)n sin √π2 :
                      
 Poiché sin √
               2
                 ± nπ

                                                         √      n     π
                                                        2 2 (−1) sin √2
                                                   an =    ·
                                                         π    1 − 2n2

    (b) In x = π2 la funzione è continua (per periodicità i due limiti laterali coincidono), quindi la
                          π
                              = cos √π2 . Poiché cos(2n · π2 ) = (−1)n :
                      
 serie converge a f
                          2

                     √             √            √
                 π    2     π   X 2 2 sin √π2     2     π h       X      1 i
             cos √ =    sin √ +               =     sin √   1 − 2             .
                  2  π       2 n≥1 π 1 − 2n2    π         2       n≥1
                                                                      2n2 − 1

 Risolvendo rispetto alla somma:

                                             X         1      1h    π       π i
                                                            =   1 − √   cot √
                                                   2k 2 − 1   2       2       2
                                             k≥1



Esercizio 48    [CP 2.50]

 TRACCIA

    Sia f = −1 su [−2, −1], f = x su (−1, 1), f = 1 su [1, 2], ripetuta periodicamente fuori da
 [−2, 2]. (a) Trovare i coecienti di Fourier. (b) Calcolare lo scarto quadratico medio tra f e il
 suo polinomio di Fourier di ordine k = 2.




 PROCEDIMENTO

     T = 4, L = 2, ω = π2 . La funzione è dispari (si verica sui tre tratti): soli seni. Per (b), lo
 scarto rispetto al polinomio di ordine 2 è, per Parseval, la radice dell'energia della coda n ≥ 3.




 SVOLGIMENTO E SOLUZIONE

    (a) f dispari ⇒ an = 0. Posto k := nπ
                                        2 :
                                 Z 2                        Z 1                    Z 2
                          bn =         f (x) sin(kx) dx =         x sin(kx) dx +         sin(kx) dx.
                                  0                          0                      1




                                                              36
      R1                cos k sin k
                                         R2                  cos k−(−1)n
Con
      0 x sin(kx) dx = − k + k2 e         1 sin(kx) dx =           k     (poiché 2k = nπ ):

                                         
                                              2
                                     n
                                         −
                                                                        n pari
                           sin k (−1)    
                                             nπ
                       bn = 2 −        =          n−1
                            k      k
                                          4(−1)         2
                                                   2
                                                     +                  n dispari.
                                             n2 π 2     nπ

   (b) Detto S2 il polinomio di Fourier di ordine 2, per Parseval l'energia dell'errore è la coda
della serie dei quadrati:

                                                                     s
                                        X                                1X 2
                        E(f − S2 ) =          b2n   =⇒          σ=         bn
                                                                         2
                                        n≥3                               n≥3

                                         1           1
                                                             |f − S2 |2 = 12 E(f − S2 )). Numericamente
                                                         R
con i bn sopra calcolati (la costante
                                         2 deriva da T
                                                                   1                         1
si può stimare troncando la serie: i termini decadono come
                                                                   n nei quadrati, cioè come n2 , quindi
poche decine di addendi danno già ottima precisione.




                                                    37
5 Analisi qualitativa delle soluzioni di EDO
 SCHEMA GENERALE  LA CASSETTA DEGLI ATTREZZI QUALITATIVA

       Tutti questi esercizi si risolvono senza (o quasi) calcolare la soluzione, con cinque mosse sempre
 uguali:

  1.   TEUL: verica che f sia continua e localmente lipschitziana in y (di solito basta f ∈ C 1 ):
       garantisce esistenza e unicità locale.

  2.   Soluzioni costanti (equilibri): risolvi f (x, y) = 0 rispetto a y .               Per    unicità, nessuna
       soluzione può attraversarle: questo conna la soluzione in una striscia e ne determina il segno.

  3.   Monotonia: noto il segno di y , il segno di y ′ = f (x, y) dà crescenza/decrescenza e gli eventuali
       massimi/minimi (dove y
                                    ′ = 0).

  4.   Concavità: deriva l'equazione, y ′′ = fx + fy y ′ , e studiane il segno.
  5.   Intervallo massimale: se la soluzione resta limitata (perché connata fra due equilibri, o
       perché f è sublineare), è globale; se invece f cresce più che linearmente in y (es. y , e ),
                                                                                            3   y

       attendi esplosione in tempo nito e dimostrala per confronto.



Esercizio 69       [S10 Es.4]

 TRACCIA

       Dato il problema di Cauchy             y ′ = arctan(y), y(0) = 1, studiarne la soluzione (insieme di
 denizione, asintoti, max, min, crescenza, concavità).




 SVOLGIMENTO E SOLUZIONE

    TEUL. f (y) = arctan y ∈ C ∞ : esistenza e unicità locale.
    Equilibri e segno. arctan y = 0 ⇐⇒ y = 0: y ≡ 0 è soluzione costante. Poiché y(0) = 1 > 0,
 per unicità y > 0 sempre, dunque y = arctan y > 0: la soluzione è strettamente crescente
                                    ′

 (nessun massimo né minimo).
                                ′
     Concavità. y ′′ = 1+y
                        y
                           2 =
                               arctan y
                                1+y 2
                                        > 0 per y > 0: la soluzione è convessa su tutto il dominio.
     Intervallo massimale. Poiché |y ′ | = | arctan y| < π2 , la crescita è al più lineare: non c'è
 esplosione in tempo nito e la soluzione è globale su R.
     Asintoti. Per x → −∞ la soluzione decresce restando > 0: tende a 0+ , quindi y = 0 è
 asintoto orizzontale a −∞. Per x → +∞, y → +∞ con y ′ → π2 : c'è un asintoto obliquo di
              π
 pendenza
              2.



Esercizio 70       [S10 Es.5]

 TRACCIA

                                          ′ =       1
       Dato il problema di Cauchy y                       , y(0) = 1, studiarne la soluzione.
                                                 1 + 3y 2


 SVOLGIMENTO E SOLUZIONE

       TEUL. f ∈ C ∞ ; inoltre 0 < f ≤ 1, quindi f è limitata: la soluzione è globale su R.
       Monotonia. y ′ > 0 ovunque: strettamente crescente, nessun estremo. Non ci sono
 soluzioni costanti (f non si annulla mai).
                          6y y ′
       Concavità. y ′′ = −          , di segno opposto a y : la soluzione è concava dove y > 0,
                       (1 + 3y 2 )2
 convessa dove y < 0, con esso nel punto in Rcui y = 0.
    Forma implicita e asintoti. Separando, (1 + 3y 2 ) dy = x + c dà y + y 3 = x + 2 (imponendo


                                                           38
 y(0) = 1).     Per x   → ±∞ si ha y ∼ x1/3 → ±∞: nessun asintoto (crescita sublineare, ma
 illimitata).



Esercizio 71    [S10 Es.7]

 TRACCIA

     Dato il problema di Cauchy y
                                          ′ = ln(y) , y(0) = 2, studiarne la soluzione.
                                                y


 SVOLGIMENTO E SOLUZIONE

    Dominio e TEUL. Serve y > 0; lì f (y) = lnyy ∈ C ∞ : TEUL vale.
    Equilibri e segno. ln y = 0 ⇐⇒ y = 1: y ≡ 1 è soluzione costante. Poiché y(0) = 2 > 1,
                                       y > 0: strettamente crescente.
                                   ′  ln y
 per unicità y > 1 sempre, dunque y =
                               1 − ln y
    Concavità. y ′′ = y ′ ·       , con y > 0: la soluzione è convessa per 1 < y < e e concava
                                         ′
                             y2
 per y > e, con un esso dove y = e.
    Intervallo massimale e asintoti. Per x → +∞: y cresce e y ′ = lnyy → 0, quindi la crescita
 è sublineare e non c'è esplosione: globale, con y → +∞ (nessun asintoto orizzontale). Per
 x → −∞: y decresce restando > 1, quindi y → 1+ e y = 1 è asintoto orizzontale. Dominio:
 tutto R.



Esercizio 72    [S10 Es.8.2]

 TRACCIA

     Determinare, per ogni α ∈ R \ {0}, la soluzione del problema di Cauchy y
                                                                                      ′ = y − y −2 , y(0) = α.



 PROCEDIMENTO

     L'equazione è a variabili separabili e  fatto non ovvio  si integra esattamente con la
                                 3                                                        2 compare     y2
 sostituzione implicita u = y : moltiplicando numeratore e denominatore per y                                , la
                                                                                                      y 3 −1
 cui primitiva è logaritmica.



 SVOLGIMENTO E SOLUZIONE

     Dominio ed equilibri. Serve y ̸= 0; f (y) = y − y −2 si annulla per y 3 = 1, cioè y ≡ 1 (unica
 soluzione costante).
     Risoluzione. Separando e moltiplicando per y 2 :
                      y 2 dy        1
                       3
                             = dx =⇒ ln |y 3 − 1| = x + c =⇒ y 3 − 1 = (α3 − 1)e3x ,
                     y −1           3

 avendo imposto y(0) = α. Dunque

                                                 h                i1/3
                                           y(x) = 1 + (α3 − 1)e3x      .

     Discussione qualitativa e dominio. L'espressione perde senso dove si annulla (y = 0 è
             1 + (α3 − 1)e3x = 0          ⇐⇒             1
                                                 e3x = 1−α                                            ∗ =
 escluso):                                                 3 , possibile solo se α < 1, e allora in x

 − 31 ln(1 − α3 ).
   α > 1: y > 1 crescente, denita su tutto R; y → 1+ per x → −∞, y ∼ (α3 − 1)1/3 ex → +∞
    per x → +∞.


   0 < α < 1: y ′ < 0, la soluzione decresce e raggiunge 0 in x∗ > 0: intervallo massimale (−∞, x∗ ).


                                                        39
   α < 0: y ′ < 0, la soluzione decresce; qui x∗ < 0 e l'intervallo massimale è (x∗ , +∞), con
    y → −∞.


Esercizio 73   [S10 Es.8.3(a)]

 TRACCIA

                                                                                         ′ =       |y|
    Determinare l'unica soluzione locale e l'intervallo massimale di esistenza per y                       ,
                                                                                               2 + 2x + x2
 y(0) = −1.


 PROCEDIMENTO

    Due osservazioni preliminari: il denominatore è (x + 1)
                                                                   2 + 1 > 0, quindi non crea singolarità;

 e il valore assoluto, che renderebbe f non C
                                                1 in y = 0, è innocuo perché il dato iniziale è negativo

 e la soluzione non può attraversare l'equilibrio y ≡ 0.       Nella regione y < 0 l'equazione diventa
 lineare.



 SVOLGIMENTO E SOLUZIONE

     Connamento. y ≡ 0 è soluzione; poiché y(0) = −1 < 0, per unicità y < 0 sempre, dunque
 |y| = −y e l'equazione diventa lineare:
                                                      −y
                                           y′ =                .
                                                  (x + 1)2 + 1

                    y′           1
    Risoluzione.       =−                dà ln |y| = − arctan(x + 1) + c; imponendo y(0) = −1 (cioè
                    y       (x + 1)2 + 1
                            π
 ln 1 = − arctan 1 + c, c = 4 ):
                                                      π
                                        y(x) = −e 4 −arctan(x+1)
     Intervallo massimale. L'espressione è denita e regolare per ogni x ∈ R e resta limitata: la
 soluzione è globale, I = R. Inoltre y > 0 (crescente), con asintoti orizzontali y → −e
                                      ′                                                 −π/4 per

 x → +∞ e y → −e3π/4 per x → −∞.


Esercizio 74   [S10 Es.8.3(b)]

 TRACCIA
                                                                                                      1 + y4
    Determinare l'unica soluzione locale e l'intervallo massimale di esistenza per             y′ =          ,
                                                                                                        y
 y(0) = −1.


 SVOLGIMENTO E SOLUZIONE
                                                                                                  4
     Dominio e segno. Serve y ̸= 0; con y(0) = −1 < 0 resta y < 0, dove y ′ = 1+y
                                                                               y  < 0: la
 soluzione decresce.
                             y dy
     Risoluzione. Separando:      4
                                    = dx, e con t = y 2 ( dt = 2y dy ):
                                 1+y
                            1                                                π
                              arctan(y 2 ) = x + c;        y(0) = −1 ⇒ c =     .
                            2                                                8
 Dunque arctan(y
                   2 ) = 2x + π e, poiché y < 0,
                              4

                                               r 
                                                         π
                                       y(x) = − tan 2x +
                                                         4



                                                      40
    Intervallo massimale. Serve 0 < 2x + π4 < π2 (l'estremo sinistro è escluso perché darebbe
 y = 0, fuori dal dominio), cioè
                                                  π π
                                               I= − ,   .
                                                   8 8
              si ha y → −∞: esplosione in tempo nito, coerente col fatto che f (y) ∼ y per
           π−                                                                          3
 Per x →
           8
 |y| grande (crescita superlineare).


Esercizio 75     [S10 Esercizio 8.7  prova del 22/01/2025, es. 1]

 TRACCIA
             ′           2
    Dato y   = xy 3 ey , y(0) = 1: calcolare il valore minimo dell'unica soluzione locale sul suo
 dominio di esistenza, giusticando la risposta, quindi dimostrare che y(x) è pari.




 SVOLGIMENTO E SOLUZIONE

    TEUL. f (x, y) = xy 3 ey ∈ C ∞ : unica soluzione locale.
                                2


    Minimo. y ≡ 0 è soluzione; per unicità, essendo y(0) = 1 ̸= 0, si ha y > 0 sempre. Allora in
             2                      2
 y ′ = x y 3 ey i fattori y 3 ed ey sono positivi e il segno di y ′ coincide con quello di x: decrescente
 per x < 0, crescente per x > 0. Dunque


                                             min y = y(0) = 1.

    Parità. Posto z(x) := y(−x):
                                                                2              2
                       z ′ (x) = −y ′ (−x) = − (−x)y(−x)3 ey(−x) = x z(x)3 ez(x) ,
                                              


 cioè z risolve la stessa equazione con lo stesso dato z(0) = 1. Per unicità z ≡ y , ossia y(−x) = y(x):
 y è pari. ■
    Osservazione (globalità). Per x ≥ 0 vale y ≥ 1, quindi ey ≥ e e y ′ ≥ xy 3 ; confrontando
                                                                       2


 con u
      ′ = xu3 , u(0) = 1, che dà u = (1 − x2 )−1/2 esplodente in x = 1, si conclude che y esplode in

 un tempo nito x
                     ∗ ≤ 1: la soluzione non è globale ed è denita su (−x∗ , x∗ ).



Esercizio 76     [CP 4.49]

 TRACCIA

    Dato y
            ′ = − arctan(x)(ey − 1 − y), y(0) = y > 0: 1. sono vericate le ipotesi del teorema
                                                   0
 di esistenza e unicità locale? E di quello globale? 2. determinare il luogo dei punti a tangente
 orizzontale, dove le soluzioni crescono o decrescono, ed eventuali soluzioni costanti. 3. determinare
 l'intervallo massimale.



 SVOLGIMENTO E SOLUZIONE

    1. f (x, y) = − arctan(x)(ey − 1 − y) ∈ C ∞ (R2 ): le ipotesi del TEUL sono vericate. Quelle
 del teorema di esistenza globale no:     f cresce come ey , quindi non è sublineare in y (la globalità
 andrà dedotta altrimenti).
    2. Posto g(y) := ey − 1 − y , si ha g(y) ≥ 0 con g(y) = 0 ⇐⇒ y = 0 (è il resto di Taylor
 dell'esponenziale). Dunque:

   soluzioni costanti: y ≡ 0;

   tangente orizzontale (y ′ = 0): l'unione {x = 0} ∪ {y = 0};

   essendo y0 > 0, per unicità y > 0 sempre e quindi g(y) > 0: il segno di y ′ è opposto a quello di
    arctan x, cioè le soluzioni crescono per x < 0 e decrescono per x > 0. In particolare x = 0


                                                     41
      è un punto di   massimo.
      3. Dal punto 2 la soluzione è compresa fra 0 (che non può raggiungere) e il valore massimo y0 :
 è dunque  limitata. Una soluzione limitata non può esplodere in tempo nito e il dominio Ω = R2
 non ha frontiera da raggiungere, quindi


                                       I=R     (la soluzione è globale).




Esercizio 77     [CP 4.51]

 TRACCIA
                         p
               ′ = log
                                  
      Dato y              1 + 2y 2 , y(0) = y0 ∈ R: 1. ipotesi di esistenza e unicità locale/globale? 2.
 al variare di y0 , luogo dei punti a tangente orizzontale, crescenza, decrescenza, soluzioni costanti.
 3. regioni di convessità e concavità.



 SVOLGIMENTO E SOLUZIONE
                                     1          2
      Conviene riscrivere f (y) =
                                     2 ln(1 + 2y ).
    1. f ∈ C ∞ (R): TEUL vericato. Inoltre f cresce come ln |y|, dunque sublinearmente : sono
 soddisfatte anche le ipotesi del teorema di esistenza globale, e ogni soluzione è denita su tutto
 R.
     2. f (y) = 0 ⇐⇒ 1 + 2y 2 = 1 ⇐⇒ y = 0. Quindi:
   soluzione costante: y ≡ 0;

   tangente orizzontale: la retta y = 0;

   per y ̸= 0 si ha f (y) > 0: tutte le soluzioni non costanti sono strettamente crescenti, sia
    per y0 > 0 sia per y0 < 0 (nessun massimo o minimo).
                                                   +
 Per y0 > 0: y → +∞ per x → +∞ e y → 0 per x → −∞ (asintoto y = 0). Per y0 < 0: y → 0
                                                                                                        −

 per x → +∞ (asintoto y = 0) e y → −∞ per x → −∞.
                                         2y
    3. Derivando, y ′′ = f ′ (y) y ′ =          y ′ , e poiché y ′ > 0 il segno di y ′′ è quello di y :
                                       1 + 2y 2

                                convessa dove y > 0,        concava dove y < 0.




Esercizio 78     [CP 4.54]

 TRACCIA

      Eseguire l'analisi qualitativa del problema di Cauchy y
                                                                     ′ = (x2 − 1)(1 − sin y), y(1) = 0, senza

 calcolare esplicitamente la soluzione.



 SVOLGIMENTO E SOLUZIONE

      TEUL. f ∈ C ∞ (R2 ): unica soluzione locale.
      Equilibri e connamento. 1 − sin y = 0 ⇐⇒ y = π2 + 2kπ : sono soluzioni costanti. Poiché
 y(1) = 0 sta fra − 3π   π                                                            3π      π
                     2 e 2 , per unicità la soluzione resta connata nella striscia − 2 < y < 2 : è
 dunque limitata e quindi globale su R.
    Monotonia. Nella striscia si ha 1 − sin y > 0, quindi il segno di y ′ è quello di x2 − 1:
                      y ′ > 0 per |x| > 1,    y ′ < 0 per |x| < 1,       y ′ = 0 in x = ±1.

 Dunque x = −1 è un punto di  massimo locale e x = 1 (dove y = 0) un punto di minimo locale.
      Asintoti. Essendo monotona e limitata per x → ±∞, la soluzione ammette limiti niti ℓ± ;
                                                       π                   3π
 tali limiti devono essere equilibri, quindi y →
                                                       2 per x → +∞ e y → − 2 per x → −∞ (asintoti




                                                       42
 orizzontali).



Esercizio 79     [CP 4.55]

 TRACCIA

    Eseguire l'analisi qualitativa della soluzione del problema di Cauchy y
                                                                               ′ = yey , y(0) = 1.




 SVOLGIMENTO E SOLUZIONE

    TEUL. f (y) = yey ∈ C ∞ .
    Equilibri e segno. yey = 0 ⇐⇒ y = 0: y ≡ 0 è l'unica soluzione costante. Poiché
 y(0) = 1 > 0, per unicità y > 0 sempre e y ′ > 0: strettamente crescente.
    Concavità. y ′′ = y ′ dy
                           d
                             (yey ) = y ′ ey (1 + y) > 0 per y > 0: convessa.
    Intervallo massimale. In avanti la crescita è superesponenziale : separando, 1y e s ds = x,
                                                                                R −s

 e l'integrale a sinistra converge per y → +∞, quindi esiste x
                                                                    ∗ < +∞ con y → +∞ per x → x∗− :

 esplosione in tempo nito.         All'indietro   y decresce verso 0+ senza raggiungerlo, quindi la
                                   ∗
 soluzione è denita per ogni x < x :


                         I = (−∞, x∗ ),       y = 0 asintoto orizzontale a − ∞.


Esercizio 80     [CP 4.57]

 TRACCIA

    Eseguire lo studio qualitativo della soluzione del problema di Cauchy y
                                                                                ′ = y 2 − y − 2, y(0) = 3
                                                                                                        2
 (insieme di denizione, asintoti, max, min, crescenza, concavità).




 SVOLGIMENTO E SOLUZIONE

    Equilibri. y 2 − y − 2 = (y − 2)(y + 1) = 0: soluzioni costanti y ≡ 2 e y ≡ −1.
    Connamento e monotonia. Il dato y(0) = 32 sta fra i due equilibri, quindi per unicità
 −1 < y < 2 sempre. In tale striscia (y − 2) < 0 e (y + 1) > 0, dunque y ′ < 0: la soluzione è
 strettamente decrescente (nessun massimo o minimo).
    Insieme di denizione. Essendo limitata fra −1 e 2, la soluzione non può esplodere: è
 globale, I = R.
    Asintoti. Monotona e limitata: ammette limiti niti agli estremi, che devono essere equilibri.
 Quindi
                             y → 2− (x → −∞),            y → −1+ (x → +∞) :
 y = 2 e y = −1 sono asintoti orizzontali.
    Concavità. y ′′ = (2y − 1)y ′ ; poiché y ′ < 0, il segno di y ′′ è opposto a quello di 2y − 1:
                                        1                      1                     1
                     convessa per y <
                                        2,   concava per y >
                                                               2,   esso dove y =
                                                                                     2.




                                                    43
6 Teorema del Dini
Esercizio 106    [Esame 13/06/2023]

 TRACCIA
                                                   1    1
    Siano a > 0, x0 ∈ R e y0 > 0. Data F (x, y) =    − + a(x − x0 )2 : 1. stabilire se F (x, y) = 0
                                                  y 2 y02
 denisce implicitamente y = y(x) o x = x(y) in un intorno di (x0 , y0 ); 2. determinarne la derivata;
 3. dire se tale funzione risolve un problema di Cauchy e quale.



 PROCEDIMENTO

    Applicazione diretta del Dini: verica F (x0 , y0 ) = 0, poi calcola le due derivate parziali nel
 punto. Quella rispetto a y è non nulla, quella rispetto a x si annulla: è questo a decidere quale
 delle due variabili si può esplicitare.       Il punto 3 è il colpo di scena:   la formula della derivata
 implicita è un'equazione dierenziale.




 SVOLGIMENTO E SOLUZIONE

    1. Anzitutto F (x0 , y0 ) = y12 − y12 + 0 = 0 ✓, e F ∈ C 1 in un intorno di (x0 , y0 ) (essendo
                                  0        0
 y0 > 0, il denominatore non si annulla). Le derivate parziali sono
                                                                       2
                                      Fx = 2a(x − x0 ),         Fy = − 3 .
                                                                      y

 Nel punto:   Fx (x0 , y0 ) = 0 mentre Fy (x0 , y0 ) = − y23 ̸= 0 (poiché y0 > 0). Per il teorema del
                                                            0
 Dini l'equazione denisce implicitamente

                                        y = y(x) in un intorno di x0

 (mentre non si può concludere per x = x(y), dato che Fx si annulla nel punto).
    2. La derivata della funzione implicita è
                                      Fx (x, y)    2a(x − x0 )
                        y ′ (x) = −             =−             = a(x − x0 ) y 3
                                      Fy (x, y)       − y23

    3. Sì: la funzione y = y(x) così denita soddisfa, per costruzione, anche la condizione y(x0 ) =
 y0 . Dunque risolve il problema di Cauchy
                                           (
                                            y ′ = a(x − x0 ) y 3
                                            y(x0 ) = y0 .

 Osservazione. È esattamente la struttura dell'esercizio 75 (con a = 1, x0 = 0, y0 = 1, a meno
             y2
 del fattore e   ): equazione a variabili separabili con crescita cubica in y , dunque soluzione non
 globale.




                                                       44
7 Campi vettoriali
 SCHEMA GENERALE


  1.   Dominio e topologia: individua dove F è denito, quante componenti connesse ha, e se
       ciascuna è convessa / semplicemente connessa. Da qui dipende tutto il resto.

  2.   Irrotazionalità: in R2 verica Ay = Bx ; in R3 calcola ∇ × F . È condizione necessaria per la
       conservatività.

  3.   Conservatività: se F è irrotazionale e il dominio è semplicemente connesso, allora è conserva-
       tivo (Poincaré). Se il dominio non lo è, non si può concludere: bisogna o esibire un potenziale
       (e allora è conservativo comunque) o trovare una curva chiusa con integrale non nullo (e allora
       non lo è).

       Calcolo del lavoro: se F è conservativo, γ F = U (ne) − U (inizio) e su curve chiuse vale 0;
                                                              R
  4.

                                                         F (γ(t)) · γ ′ (t) dt.
                                                    R
       altrimenti si parametrizza e si calcola

                                                                                           ∇u
 Il trucco che risolve metà degli esercizi: riconoscere che il campo è della forma              per
                                                                                           h(u)
                                                                             1
 qualche funzione u(x, y).      In tal caso il potenziale è una primitiva di
                                                                             h composta con u, ed è
 automaticamente ben denita anche su domini non semplicemente connessi.



Esercizio 181       [CP 10.2]

 TRACCIA
                                                          q              q         
                                                                  y+3         x+3                         2      y2
       Calcolare l'integrale del campo F (x, y) =
                                                                  x+3 ,       y+3       esteso all'ellisse x +
                                                                                                                 9 = 1 percorsa
 in verso antiorario.




 SVOLGIMENTO E SOLUZIONE

       Irrotazionalità. Scrivendo A = (y + 3)1/2 (x + 3)−1/2 e B = (x + 3)1/2 (y + 3)−1/2 :
                                    Ay = 12 (y + 3)−1/2 (x + 3)−1/2 = Bx .

       Potenziale. Si verica direttamente che
                                           p
                               U (x, y) = 2 (x + 3)(y + 3)
               q                q
                                   y+3 = B . Il campo è dunque conservativo nella regione
                 y+3               x+3
 soddisfa Ux =       = A e Uy =
                 x+3
 {x > −3, y > −3}, che è convessa e contiene l'ellisse (dove x ∈ [−1, 1], y ∈ [−3, 3]).
    Conclusione. L'ellisse è una curva chiusa e F è conservativo:
                                         I
                                           F · dr = 0.


 (Il potenziale U si estende con continuità anche al punto (0, −3), dove U = 0.)



Esercizio 182       [S16F pag 22]

 TRACCIA
                          2                   2
                                                         
                           x +2xy+2y
       Dato F (x, y) =
                            (x2 −2y)2
                                      ,   − (xx2 −2y)
                                                 +2x
                                                     2       : (a) dominio e componenti connesse; (b) semplice

 connessione; (c) conservatività e potenziali; (d) integrale da P                          = (−2, 1) a Q = (2, 1): dipende
 dalla curva?




                                                                  45
 SVOLGIMENTO E SOLUZIONE

    (a) Dominio. D = {(x, y) : y ̸= x2 }, cioè il piano privato di una parabola: non è connesso,
                                         2


 ma si scrive come unione delle due componenti connesse

                                     n    x2 o                n    x2 o
                                 D+ = y >     ,           D− = y <     .
                                          2                        2
    (b) D+ è l'epigraco di una funzione convessa, quindi convesso e in particolare semplice-
 mente connesso; D
                   − è omeomorfo a un semipiano, dunque semplicemente connesso (ma non

 convesso).
    (c) Un calcolo diretto dà
                                               2x3 + 6x2 + 4xy + 4y
                                   Ay = Bx =                        ,
                                                    (x2 − 2y)3

 quindi F è irrotazionale; essendo entrambe le componenti semplicemente connesse, F è         conserva-
 tivo su ciascuna. Integrando B rispetto a y e derivando rispetto a x per determinare la costante,
 si trova
                                                      x(x + 2)
                                      U (x, y) = −              +c
                                                     2(x2 − 2y)

    (d) Entrambi i punti stanno in D− (per P e Q: x2 − 2y = 4 − 2 = 2 > 0), che è connesso e
 semplicemente connesso, quindi l'integrale dipende solo dagli estremi:

                      Z Q                                   2 · 4
                            F · dr = U (2, 1) − U (−2, 1) = −       − 0 = −2 .
                        P                                     2·2

 Sì, il valore non dipende dalla curva scelta, purché essa resti dentro D− .

Esercizio 183    [S16F pag 26]

 TRACCIA
                                x2 −y 2 −1       2xy        2     2     2 2           4
    Dato F = (A, B) con A =
                                    D      , B =
                                                  D e D = (x − 1) + 2y (x + 1) + y : (a) dominio
 e sue proprietà topologiche; (b) conservatività b.1) nella palla aperta di centro l'origine e raggio
 1, b.2) nel suo dominio.




 PROCEDIMENTO

    Il denominatore, all'apparenza illeggibile, si semplica: si verica che D = (x
                                                                                      2 + y 2 − 1)2 + 4y 2 ,
                                   2                                                    2    2
 che si annulla solo dove y = 0 e x = 1. Equivalentemente, con z = x + iy , si ha D = |z − 1| e
 A − iB = z 21−1 : è la scorciatoia che rende tutto trasparente.


 SVOLGIMENTO E SOLUZIONE

    (a) Dominio. Sviluppando, D = (x2 + y 2 − 1)2 + 4y 2 : somma di quadrati, nulla solo se y = 0
    2
 e x = 1. Dunque
                                      Ω = R2 \ {(1, 0), (−1, 0)} :
 è aperto e   connesso, ma non semplicemente connesso (due punti rimossi) e non convesso.
     (b.1) La palla B1 (0) non contiene i due punti singolari (che stanno sulla frontiera) ed è
 convessa, quindi semplicemente connessa. Si verica che F è irrotazionale (per calcolo diretto, o
                               è olomorfa): per il lemma di Poincaré F è conservativo in B1 (0).
                            1
 osservando che A − iB = 2
                          z −1
     (b.2) Nel dominio completo la semplice connessione manca, quindi il lemma non si applica;



                                                     46
 tuttavia si esibisce un potenziale globale :


                                                       1 (x − 1)2 + y 2
                                          U (x, y) =    ln
                                                       4 (x + 1)2 + y 2

                  2
 Verica: posto r1 = (x − 1)
                                  2 + y 2 , r 2 = (x + 1)2 + y 2 (con D = r 2 r 2 ),
                                             2                             1 2

                                       1 h x − 1 x + 1 i (x2 − 1) − y 2
                                Ux =            −       =               = A,
                                       2 r12       r22       r12 r22

 e analogamente Uy      = B.      Poiché U è ben denita e a un solo valore su tutto Ω, il campo è
 conservativo anche nel suo dominio, pur non essendo questo semplicemente connesso.

Esercizio 184    [S16F pag 31]

 TRACCIA
                                                      
                                 4x              9y
    Dato F (x, y) =                        ,                : (a) dominio e componenti connesse; (b) conves-
                            log(4x2 +9y 2 ) log(4x2 +9y 2 )
 sità/semplice connessione di ciascuna; (c) conservatività.




 SVOLGIMENTO E SOLUZIONE

    (a) Dominio. Serve 4x2 + 9y 2 > 0 (esclude l'origine) e log(·) ̸= 0, cioè 4x2 + 9y 2 ̸= 1. Dunque
 D è il piano privato dell'origine e dell'ellisse 4x2 + 9y 2 = 1, e ha due componenti connesse:

         D1 = {0 < 4x2 + 9y 2 < 1} (interno bucato),                  D2 = {4x2 + 9y 2 > 1} (esterno).

    (b) D1 è una corona ellittica degenere (disco privato del centro): non semplicemente connessa,
 non convessa. D2 è l'esterno di una curva chiusa: anch'esso non semplicemente connesso e non
 convesso.
    (c) Posto u := 4x2 + 9y 2 , si ha ∇u = (8x, 18y) = 2(4x, 9y), quindi
                                                            ∇u
                                                    F =           .
                                                           2 ln u
                              1
 Detta G una primitiva di         (esiste su ciascun intervallo u ∈ (0, 1) e u ∈ (1, +∞), dove ln u
                           2 ln u                                                     ′
 ha segno costante e non si annulla), la funzione U := G(u(x, y)) soddisfa ∇U = G (u)∇u = F .
 Dunque
                             F è conservativo su ciascuna componente connessa
 pur non essendo queste semplicemente connesse: il potenziale dipende solo da u, quindi è auto-
 maticamente a un solo valore e non si generano salti girando attorno al buco.



Esercizio 185    [CP 10.5]

 TRACCIA
                            2 2
                      xyz, x 2z , log z . (a) Determinare il dominio e calcolarne il rotore; il campo
                                       
    Sia F (x, y, z) =
                                                               2   2
 è conservativo? (b) Calcolare la circuitazione lungo C1 = {x + y = 1, z = 1}.




 SVOLGIMENTO E SOLUZIONE

    (a) Dominio: z > 0, semispazio convesso (quindi semplicemente connesso).
        ∇ × F = ∂y F3 − ∂z F2 , ∂z F1 − ∂x F3 , ∂x F2 − ∂y F1 = −x2 z, xy, xz 2 − xz ̸≡ 0.
                                                                                   




                                                           47
 Il campo     non è irrotazionale, dunque non è conservativo (l'irrotazionalità è necessaria).
        (b) Parametrizzando r(t) = (cos t, sin t, 1), t ∈ [0, 2π], con r′ (t) = (− sin t, cos t, 0) e F (r(t)) =
                   2
  cos t sin t, cos2 t , 0 :
                      

                                                                               cos3 t
                                              F · r′ = − cos t sin2 t +               .
                                                                                 2
                                                                                    R 2π                        sin3 t 2π
 Entrambi gli addendi hanno integrale nullo su un periodo (
                                                                                     0     cos t sin2 t dt =      3     0
                                                                                                                              = 0 e
 R 2π
  0     cos3 t dt = 0), quindi
                                                      I
                                                                F · dr = 0.
                                                        C1

 Nota: valore nullo su una curva chiusa, ma il campo non è conservativo  conferma che un solo
 integrale nullo non prova nulla.



Esercizio 186       [CP 10.6]

 TRACCIA
                                                           
                                 2x          8y                              2 + 4y 2 > 1}. (a) Trovare tutti i potenziali
        Sia F (x, y) =                  ,            + 2y       su Ω = {x
                             x2 +4y 2 −1 x2 +4y 2 −1
 in Ω. (b) Si poteva dedurre l'esistenza del potenziale dalla teoria? (c) Calcolare il lavoro lungo
 φ(t) = (2 cos t, sin t), t ∈ [0, 2π].


 SVOLGIMENTO E SOLUZIONE

        (a) Posto u := x2 + 4y 2 − 1, si ha ∇u = (2x, 8y), quindi la prima parte del campo è ∇u
                                                                                             u =
 ∇(ln u); la seconda, (0, 2y), è ∇(y 2 ). Dunque

                                   U (x, y) = ln x2 + 4y 2 − 1 + y 2 + c,
                                                              
                                                                                           c ∈ R.

                     2x        8y
 (Verica: Ux =
                     u , Uy = u + 2y ✓.)
        (b) No.    Ω è l'esterno di un'ellisse, quindi non è semplicemente connesso: il lemma di
 Poincaré non si applica e la sola irrotazionalità non basta a garantire l'esistenza del potenziale.
 Qui la conservatività si stabilisce solo esibendo U esplicitamente.
        (c) La curva è chiusa e contenuta in Ω (su di essa x2 + 4y 2 = 4 > 1); poiché F è conservativo
 in Ω:
                                                       I
                                                                F · dr = 0.
                                                            φ



Esercizio 187       [CP 10.8  prova del 3/09/2025, es. 3]

 TRACCIA
                                                                         2
        Siano F (x, y, z) = (x, zy, z) e r(t) = (cos t, sin t, t ), t ∈ [−π, π]. (a) Stabilire se r è chiusa
 e regolare. (b) Calcolare il lavoro di F lungo r ; dal valore trovato si può dedurre se il campo è
 conservativo?



 SVOLGIMENTO E SOLUZIONE

    (a) r(−π) = (−1, 0, π 2 ) = r(π): chiusa. Inoltre r′ (t) = (− sin t, cos t, 2t) con ∥r′ ∥2 = 1+4t2 ≥
 1 > 0: regolare ovunque.
    (b) F (r(t)) = (cos t, t2 sin t, t2 ), quindi
                   F (r) · r′ = − cos t sin t + t2 sin t cos t + 2t3 = sin t cos t (t2 − 1) + |{z}
                                                                                               2t3 ,
                                                                                                        dispari
                                                                       |        {z        }
                                                                                         dispari




                                                                  48
                                                                            Z
 e l'integrale di una funzione dispari su [−π, π] è nullo:                         F · dr = 0 .
                                                                               r
     Conservatività: no, e comunque non deducibile dal valore trovato (servirebbe l'annullamento
 su ogni curva chiusa). Il rotore


                 ∇ × F = (∂y F3 − ∂z F2 , ∂z F1 − ∂x F3 , ∂x F2 − ∂y F1 ) = (−y, 0, 0) ̸≡ 0

 mostra che F non è irrotazionale, dunque                  non conservativo.

Esercizio 188    [CP 10.11]

 TRACCIA
                                                         
                          √      x           √      y
     Sia F (x, y) =                      ,                  .   (a) Dominio e sue caratteristiche topologiche.                 (b)
                              x2 +y 2 −4         x2 +y 2 −4
                                                                                                                              √
 Mostrare che F è irrotazionale e trovarne un potenziale. (c) Calcolare il lavoro lungo r(t) = (t,                                t),
 t ∈ [2, 3].


 SVOLGIMENTO E SOLUZIONE

    (a) Serve x2 + y 2 > 4: Ω è l'esterno del disco di raggio 2. È aperto e connesso, non convesso
 e non semplicemente connesso.
    (b) Posto u := x2 + y 2 − 4 (con ∇u = (2x, 2y)):
                              ∇u  √                                                       p
                          F = √ =∇ u                          =⇒        U (x, y) =          x2 + y 2 − 4
                             2 u

 Essendo un gradiente, F è automaticamente irrotazionale; e poiché U è ben denita su tutto Ω,
 il campo vi èconservativo√(nonostante Ω non sia semplicemente
                                                       √         connesso).
     (c) Estremi: r(2) = (2, 2) con u = 2, e r(3) = (3, 3) con u = 8. Dunque
                               Z                                               √           √        √
                                     F · dr = U (r(3)) − U (r(2)) =                8−          2=       2.
                                 r



Esercizio 189    [CP 10.12]

 TRACCIA
                                 2
                      xey + 3, x2 ey . Calcolare γ F · T ds, essendo γ(t) =                              4            2
                                               R                                                                     
     Sia F (x, y) =
                                                                                                         π arctan t, t , 0 ≤ t ≤ 1.



 SVOLGIMENTO E SOLUZIONE

     Conservatività. Ay = xey = Bx e il dominio è R2 (convesso): F è conservativo, con
                                             x2 y                                                   2
                          U (x, y) =           e + 3x           (Ux = xey + 3, Uy = x2 ey ✓).
                                             2
     Estremi della curva. γ(0) = (0, 0) e γ(1) =                        4 π
                                                                                   
                                                                        π · 4, 1       = (1, 1).
     Lavoro.       Z                                                      e                           e
                              F · T ds = U (1, 1) − U (0, 0) =                 +3 −0=                     +3
                          γ                                                2                            2


Esercizio 190    [CP 10.15]




                                                                   49
 TRACCIA

     Calcolare il lavoro del campo F (x, y) = (2xy,                  x2 − y 2 ) lungo γ(t) = (t2 , t), t ∈ [0, 1].


 SVOLGIMENTO E SOLUZIONE

     Conservatività. Ay = 2x = Bx su R2 (convesso): conservativo, con potenziale
                                                       y3
                              U (x, y) = x2 y −               (Ux = 2xy, Uy = x2 − y 2 ✓).
                                                       3
 Lavoro. γ(0) = (0, 0), γ(1) = (1, 1):
                                      Z
                                                                                        1     2
                                          F · dr = U (1, 1) − U (0, 0) = 1 −              =
                                      γ                                                 3     3


Esercizio 191     [CP 10.17]

 TRACCIA
                                                                           √
                                                                             3
                            2xy 2                                                t
                                      y log[(x2 + 1)2 ] e r(t) =
                                                              , t2 − 3t , t ∈ [0, 3]: dire se il campo è
                                                                         
     Dati F (x, y) =              ,
                            x2 +1                                           t2 +1
 irrotazionale e conservativo, calcolarne il potenziale, calcolare il lavoro lungo r .




 SVOLGIMENTO E SOLUZIONE

    Semplicazione. y log[(x2 + 1)2 ] = 2y log(x2 + 1).
                            4xy                 2x       4xy
    Irrotazionalità. Ay = 2       e Bx = 2y ·        = 2        : uguali, quindi irrotazionale. Il
                           x +1               x2 + 1    x +1
 dominio è R (convesso), dunque anche conservativo.
            2
                                                              2
    Potenziale. f (x, y) = y 2 log(x2 + 1) (infatti fx = x2xy                   2
                                                           2 +1 e fy = 2y log(x + 1) ✓).
                                                                     √
                                                                     3
     Lavoro. Estremi: r(0) = (0, 0) e r(3) =                           3
                                                                             
                                                                     10 ,   0 .      In entrambi y    = 0, quindi f = 0 in
 entrambi:                            Z
                                              F · dr = f (r(3)) − f (r(0)) = 0 − 0 = 0 .
                                          r



Esercizio 192     [CP 10.18]

 TRACCIA
                                            2
                        ax log z, by 2 z, xz + y 3 . (i) Trovare a, b anché il campo sia conservativo.
                                                  
     Sia F (x, y, z) =
                                                         2   3
 (ii) Calcolare il lavoro di G(x, y, z) = (2x log z, 2y z, y ) lungo il segmento da (1, 1, 1) a (2, 1, 2).




 SVOLGIMENTO E SOLUZIONE

     (i) Il dominio è {z > 0}, convesso: basta imporre ∇ × F = 0.
                                                                                     ax               2x
             ∂y F3 = 3y 2 ,      ∂z F2 = by 2 ⇒ b = 3;                ∂z F1 =           ,   ∂x F3 =      ⇒ a = 2,
                                                                                      z                z

 mentre ∂x F2 = ∂y F1 = 0 ✓. Dunque                    a = 2, b = 3 .
     (ii) Attenzione: G non è il campo del punto (i) (∂y G3 = 3y 2 ̸= 2y 2 = ∂z G2 ), quindi non è
 conservativo e va calcolato direttamente. Parametrizzando il segmento con r(t) = (1 + t, 1, 1 + t),
 t ∈ [0, 1], e r′ = (1, 0, 1):

                                      G(r(t)) · r′ (t) = 2(1 + t) log(1 + t) + 0 + 1.



                                                                50
                                                                              2
                                                2s ln s ds = s2 ln s − s2 :
                                           R
 Con la sostituzione s = 1 + t e

     Z 1                             h          s2 i2                   1                1
         2(1 + t) log(1 + t) + 1 dt = s2 ln s −
                               
                                                      + 1 = 4 ln 2 − 2 +    + 1 = 4 ln 2 −
      0                                         2 1                      2                 2


Esercizio 193       [CP 10.19]

 TRACCIA
                           1
                                         
    Sia F (x, y) =            + sin y,
                                  x cos y . (i) Determinare il dominio D e dire se è semplicemente
                           x2
                                                               2        2
 connesso; (ii) stabilire se F è conservativo in Ω = {(x − 3) + (y − π) ≤ 1}; (iii) determinare il
 potenziale U in Ω con U (3, π) = 0.




 SVOLGIMENTO E SOLUZIONE

     (i) Serve x ̸= 0: D è l'unione dei due semipiani {x > 0} e {x < 0}. Non è connesso ; ciascuna
 componente è    convessa, dunque semplicemente connessa.
     (ii) Ay = cos y = Bx : irrotazionale. Inoltre Ω (palla di centro (3, π) e raggio 1) è contenuta
 in {x > 0} ed è convessa: per il lemma di Poincaré F è conservativo in Ω.
     (iii) Integrando: U = − x1 + x sin y + c. Imponendo U (3, π) = − 13 + 0 + c = 0 si ottiene c = 13 :

                                                                  1             1
                                                 U (x, y) = −       + x sin y +
                                                                  x             3


Esercizio 194       [CP 10.21]

 TRACCIA
                                                   
                            y−4x
    Sia F (x, y) =
                           4x2 +y 2
                                    , − 4xx+y
                                           2 +y 2       . (i) Dominio D e semplice connessione; (ii) dimostrare che

 F è irrotazionale in D; (iii) calcolare il lavoro lungo γ(t) = (cos t, 2 sin t), t ∈ [0, 2π].


 PROCEDIMENTO

    È l'esempio-modello di campo irrotazionale ma non conservativo su un dominio con un buco.
 Per (iii) conviene notare che sulla curva data il denominatore 4x
                                                                                        2 + y 2 è costante (= 4): il calcolo

 diventa immediato.




 SVOLGIMENTO E SOLUZIONE

    (i) D = R2 \ {(0, 0)}: aperto, connesso, non semplicemente connesso.
    (ii) Posto Q := 4x2 + y 2 :
             Q − (y − 4x)2y   4x2 − y 2 + 8xy                                      Q − (x + y)8x   4x2 − y 2 + 8xy
      Ay =                  =                 ,                           Bx = −                 =                 ,
                   Q2               Q2                                                  Q2               Q2
 uguali: F è  irrotazionale in D.
    (iii) Sulla curva 4x2 + y 2 = 4 cos2 t + 4 sin2 t = 4, e γ ′ = (− sin t, 2 cos t):
                   (2 sin t − 4 cos t)             cos t + 2 sin t              −2 sin2 t − 2 cos2 t   1
   F (γ) · γ ′ =                       (− sin t) + −                  (2 cos t) =                      =− .
                            4                              4                               4             2
                                          I                  Z 2π 
                                                                          1
                                                F · dr =              −      dt = −π ̸= 0.
                                            γ                 0           2




                                                                  51
 Il lavoro su una curva chiusa è non nullo:         F non è conservativo, pur essendo irrotazionale 
 possibile proprio perché D non è semplicemente connesso.



Esercizio 195   [Esame 15/02/2024]

 TRACCIA
                                                                                               
                                                       2x                 y
    Dire per quali a ∈ R il campo F (x, y) =                    + y, (ax2 +y 2 )2 + x è conservativo. Per
                                                   (ax2 +y 2 )2
                                                                           2
 tali a: calcolarne un potenziale e calcolare l'integrale sull'ellisse ax + y = 2.
                                                                                  2




 SVOLGIMENTO E SOLUZIONE

    Determinazione di a. Posto u := ax2 + y 2 :
                                         8xy                                4axy
                                Ay = −       + 1,                Bx = −          + 1.
                                          u3                                 u3

 L'uguaglianza Ay = Bx richiede 8xy = 4axy per ogni (x, y), cioè                       a=2.
    Potenziale (per a = 2). Con u = 2x2 + y 2 si ha ∇u = (4x, 2y), quindi (2x, y) = 21 ∇u e
                                      (2x, y)   ∇u      1 1
                                              =     = −   ∇   ;
                                        u2      2u2     2   u
 inoltre (y, x) = ∇(xy). Dunque


                                                             1
                                   U (x, y) = −                           + xy + c
                                                     2(2x2 + y 2 )

 (verica: Ux =
                  2x
                  u2
                     + y , Uy = uy2 + x ✓).
    Integrale sull'ellisse. U è ben denita su tutto R2 \ {0}, dunque F vi è conservativo; l'ellisse
 2x2 + y 2 = 2 è una curva chiusa contenuta nel dominio, quindi
                                                I
                                                     F · dr = 0.



Esercizio 196   [Esame 04/09/2023]

 TRACCIA
                                                                                                     
                                                                     ax                   y
    Stabilire per quali a ∈ R il campo A(x, y) =                                + y, (ax2 +y 2 )2 + ax  è conservativo e
                                                                 (ax2 +y 2 )2
 calcolarne i potenziali.




 SVOLGIMENTO E SOLUZIONE

    Posto u := ax
                   2 + y2:

                                    4axy                              4axy
                             ∂y A1 = − 3 + 1,                    ∂x A2 = − 3 + a.
                                       u                                   u

 L'uguaglianza impone 1 = a, cioè     a=1.
                                                          1      (x,y)
                    2   2                                                                           = − 12 ∇ u1 ; inoltre
                                                                                                               
    Per a = 1: u = x + y , ∇u = (2x, 2y), quindi (x, y) =
                                                          2 ∇u e u2
 (y, x) = ∇(xy). Dunque

                                                    1
                               U (x, y) = −                      + xy + c,           c∈R
                                              2(x2 + y 2 )



                                                            52
 denita su R
                2 \ {(0, 0)}: il campo è conservativo su tutto il suo dominio, benché questo non sia

 semplicemente connesso.



Esercizio 197    [Esame 15/02/2023]

 TRACCIA
                         (x − 3, y − 1)
     Dato F (x, y) =                       : 1. stabilire il dominio; 2. stabilire se è irrotazionale; 3.
                       (x − 3)2 + (y − 1)2
 calcolare l'integrale lungo la circonferenza di centro (3, 1) e raggio 1; 4. stabilire se è conservativo
 e determinarne un potenziale.




 SVOLGIMENTO E SOLUZIONE

     1. D = R2 \ {(3, 1)}: aperto, connesso, non semplicemente connesso.
     2. e 4. Posto u := (x − 3)2 + (y − 1)2 , si ha ∇u = 2(x − 3, y − 1), dunque

                      ∇u    1                                  1 
                                                                   ln (x − 3)2 + (y − 1)2
                                                                                          
                F =      = ∇ ln u         =⇒        U (x, y) =
                      2u     2                                   2

 Essendo un gradiente, F è irrotazionale; e poiché U è a un solo valore su tutto D , F è conser-
 vativo in D (nonostante l'assenza di semplice connessione: qui il campo è radiale, non rotante
 come quello dell'es. 194).
     3. La circonferenza è chiusa e contenuta in D; per la conservatività
                                              I
                                                  F · dr = 0.


 (Verica diretta: sulla circonferenza F è radiale e il versore tangente è ortogonale al raggio, quindi
 l'integranda F · T è identicamente nulla.)




 IL CONFRONTO DA RICORDARE: ES. 194 CONTRO ES. 197

     Entrambi hanno dominio R
                                  2 meno un punto (non semplicemente connesso) ed entrambi sono

 irrotazionali. Ma:

   l'es. 197 è radiale (F = ∇( 12 ln u)): ammette potenziale globale a un solo valore ⇒ conserva-
    tivo, circuitazione nulla;
   l'es. 194 ha una componente rotatoria: la circuitazione attorno al buco vale −π ̸= 0 ⇒ non
  conservativo.
 Morale: su un dominio non semplicemente connesso, l'irrotazionalità non decide. Bisogna sempre
 o esibire un potenziale globale, o calcolare la circuitazione attorno al buco. Un campo della forma
  ∇u
  h(u) (esercizi 184, 186, 188, 195, 196, 197) è sempre conservativo, perché il potenziale dipende solo
 da u.




                                                     53
Appendice  Esercizi non ancora svolti
  COME LEGGERE QUESTA APPENDICE

         Sono i   116 esercizi del le non ancora risolti: nessuno di essi ha nora avuto riscontro nei
  temi d'esame (tutti e sette gli esercizi con riscontro sono risolti nel corpo del documento). Per
  ciascuno riporto numero, riferimento bibliograco e argomento.
         Perché non riporto qui le formule per esteso. L'estrazione automatica del testo da questo
  PDF storpia sistematicamente le formule  ha già prodotto due errori sostanziali nelle soluzioni
  dei temi d'esame (il denominatore (2
                                              n n)2 letto come 2n n2 , e y ′ = xy 3 ey 2 letto con l'esponenziale

  a denominatore). Le formule vanno quindi lette dalle pagine renderizzate ad alta risoluzione, una
  per una: è ciò che faccio via via che risolvo ciascuna sezione, ed è la ragione per cui qui trovi
  l'indice e non una trascrizione che sarebbe inadabile.



2.1 Equazioni dierenziali del primo ordine (19 esercizi)
Es. 49     [CP 4.1] lineare, y(1) = a; limite del rapporto incr.     Es. 59    [CP 4.13] lineare, sviluppo di Taylor
Es. 50     [CP 4.2] separabili, e−y ; intervallo massimale           Es. 60    [CP 4.14] lineare con sin x
Es. 51     [CP 4.3] separabili, (2x2 + 1)y ′ = 2x/y                  Es. 62    [CP 4.20] lineare, y(2) = 1
Es. 52     [CP 4.5] y ′ = −x6 y 2 ; integrale su Iβ                  Es. 63    [CP 4.21] integrale generale su (1, +∞)
Es. 53     [CP 4.6] x′ = 4t3 x; max/min su [1, 3]                    Es. 64    [CP 4.22] y ′ = ex cos2 y
Es. 54     [CP 4.7] soluzioni stazionarie; Mac Laurin                Es. 65    [CP 4.24] famiglia con f (x); Taylor in x0 = 4
Es. 55     [CP 4.8] y ′ + ty = t; asintoto obliquo di F              Es. 66    [CP 4.27] y ′ = (2 − y)(3 − y); convergenza integral
Es. 56     [CP 4.9] y ′ + 2y cos x = cos x; Taylor e graco          Es. 67    [CP 4.28] due problemi con y/(x + 1)
Es. 57     [CP 4.10] y ′ = 2y − y 2 ; derivate in 0, esso           Es. 68    [CP 4.35] regioni di esistenza/unicità; limite
Es. 58     [CP 4.12] y ′ = x2 /y 3 ; limitatezza e integrale

2.3 Equazioni del secondo ordine (25 esercizi)
Es. 81     [CP 4.98] y ′′ + y ′ = t2 + 1                           Es. 94     [CP 4.111] parametro k ; soluzione particolare
Es. 82     [CP 4.99] x′′ − 2x′ + 2x = cos t; Cauchy                Es. 95     [CP 4.113] y ′′ − 2y ′ + y = 2e2x
Es. 83     [CP 4.100] y ′′ + 9y = cos(3t) (risonanza)              Es. 96     [CP 4.114] y ′′ + 2y ′ − 3y = ex sin(2x)
Es. 84     [CP 4.101] y ′′ − 4y = 5 sin x                          Es. 97     [CP 4.115] y ′′ − 2y ′ = x + ex
Es. 85     [CP 4.102] y ′′ + 6y ′ + 9y = 7                         Es. 98     [CP 4.116] y ′′ + y ′ − 6y = 2e−x
Es. 86     [CP 4.103] 2x′′ − 4x′ + 2x = t; calcolo di x̄′′ (0)     Es. 99     [CP 4.117] y ′′ − y = cos x; Cauchy
Es. 87     [CP 4.104] y ′′ + 2y ′ + 3y = ex ; Cauchy               Es. 100    [CP 4.118] x′′ + 2x′ = αx; comportamento a +∞
Es. 88     [CP 4.105] y ′′ − 2y ′ + y = ex (risonanza doppia)      Es. 101    [CP 4.119] y ′′ − 2y ′ + y = cos(3x)
Es. 89     [CP 4.106] y ′′ − 3y ′ + 2y = x + e3x                   Es. 102    [CP 4.120] y ′′ + 4y = ex cos x
Es. 90     [CP 4.107] y ′′ − y ′ /3 = 2x2 − 3x − 4                 Es. 103    [S11 2.1] autovalori di −z ′′ = µz , z(0) = z(1) = 0
Es. 91     [CP 4.108] soluzione particolare, termine et            Es. 104    [S11 2.2] autovalori di −z ′′ + 2z ′ = µz
Es. 92     [CP 4.109] determinare f (t) data la soluzione          Es. 105    [S11 3] sei integrali generali (a)(f)
Es. 93     [CP 4.110] y ′′ + 2ay ′ + y = 0; limitatezza

5.1 Ottimizzazione libera (16 esercizi)
Es. 107     [CP 8.2] x3 + y 3 + 4x2 − 2y 2               Es. 117    [CP 8.16] ex−y (x2 − 2y 2 )
                                                                                4   3    2    2
Es. 108     [CP 8.3] −x4 − y 4 + 2x2 − 4xy + 2y 2        Es. 118    [CP 8.17] ex +y −4x −3y
Es. 109     [CP 8.4] x3 y 2 (1 − x − y)                  Es. 119    [CP 8.18] estremi assoluti di −x4 − y 2 + 4y − 2
                              2  2
Es. 110     [CP 8.5] xye−x −y ; matrice Hessiana         Es. 120    [CP 8.19] estremi assoluti di (x + y)2
Es. 111     [CP 8.7] (ey − 1)(2 + y − ex )               Es. 121    [S09F p.24] x2 y − xy
Es. 112     [CP 8.8] ex (x − 1)(y − 1) + (y − 1)2        Es. 122    [S09F p.34] x2 + y 3 + z 2 − xy − xz (3 variabili)
                                  2
Es. 113     [CP 8.9] y 2 + ye−x                          Es. 123    [S09F p.35] 4xy + xz + 6y 2 + x2 z + 2xyz
Es. 114     [CP 8.10] −x4 + 2x2 + x2 y − y 2 + 4y

5.2 Ottimizzazione vincolata (32 esercizi)

                                                          54
Es. 124   [S09F p.19] (y − x2 )(x2 + y 2 + 2y) su palla        Es. 141     [CP 8.39] xy − y 2 + 3 su x + y 2 = 1
Es. 125   [CP 8.13] su {0 ≤ x ≤ 1, 0 ≤ y ≤ x2 }                Es. 142     [CP 8.40] x2 + y 2 su xm + y m = 1
Es. 126   [CP 8.20] su rettangolo; f (R) e f (R2 )             Es. 143     [CP 8.41] x − y su regione con arctan
                                                                                            2
Es. 127   [CP 8.22] xey sul bordo di un quadrato               Es. 144     [CP 8.42] ey−x p   su regione fra retta e arco
Es. 128   [CP 8.23] x4 + x2 + y 4 − y 6 ; tre insiemi          Es. 145     [CP 8.43] xy + 4 − x2 − y 2 su disco
Es. 130   [CP 8.25] ex+y su x2 + y 2 = 1                       Es. 146     [CP 8.44] x2 y 2 − 2x2 y + x2 su disco
Es. 131   [CP 8.26] x2 + y su x2 + 2y 2 = 1                    Es. 147     [CP 8.45] (x + y)2 + 2y 2 + 3 su triangolo
                    √                                                                    2
Es. 132   [CP 8.27] 3 xy su x2 + y 2 − xy = 1                  Es. 148     [CP 8.46] x2x
                                                                                      2 +y 2 su regione
                                                                                           y
                                      2       2
Es. 133   [CP 8.28] Lagrange con ex + ey − 4 = 0               Es. 149     [CP 8.47] −x + x|y| su cerchio
Es. 134   [CP 8.29] xy 3 su 2x2 + y 2 = 3                      Es. 150     [CP 8.48] 4x + 6y − x2 − y 2 su rettangolo
Es. 135   [CP 8.30] x2 y su disco unitario                     Es. 151     [CP 8.49] xye2y−x su regione triangolare
Es. 136   [CP 8.31] (3x − 1)2 + (3y − 1)2 su triangolo         Es. 152     [S13F p.16] xy su circonferenza unitaria
Es. 137   [CP 8.35] x2 y su settore di ellisse                 Es. 153     [S13F p.12] x + 3y − z su due insiemi di R3
                                                                                              2    2
Es. 138   [CP 8.36] x2 yz 2 su x + y + z = 1                   Es. 154     [S13F p.25] e−(x /2+y     /3) 2
                                                                                                        (x + y 2 )
Es. 139   [CP 8.37] x2 − y 2 su x2 + 2y 2 ≤ 1                  Es. 155     [S13F p.29] (x + y) x + y 2 su palla
                                                                                                 p
                                                                                                     2
                         √
Es. 140   [CP 8.38] cos( xy); dominio ed estremi               Es. 156     [Esame 18/09/2023] (xy − 1)2 su palla

6 Integrali multipli (24 esercizi)
Es. 157   [S17F p.27] x + y 2 su settore di corona         Es. 169       [CP 9.14] x2 + y 2 su unione triangolo/settore
Es. 158   [S17F p.40] con log(y/x) su corona               Es. 170       [CP 9.16] x2 su regione ellittica
Es. 159   [CP 9.2] xy
                   √ su triangolo
                          √
                                                           Es. 171       [CP 9.18] x2 + y 2 − xy su ellisse
Es. 160   [CP 9.4] √x3 ey/ x                               Es. 172       [CP 9.20] cambio u = y/x, v = x2 + y 2
Es. 161   [CP 9.5] e x +y (polari)                         Es. 173       [CP 9.22] x cos(1 − y)
                       2   2

                                                                                          2 2
Es. 162   [CP 9.6] xe2y fra due parabole                   Es. 174       [CP 9.23] x2 ex +y su cerchio
                                                                                       2
Es. 163   [CP 9.7] y − x2 + 2                              Es. 175                  2 +y 2 su settore
                                                                         [CP 9.26] x2x   y
                   p

Es. 164   [CP 9.8] (2x + y) fra circonferenze e rette      Es. 176       [CP 9.28] trasformazione T (u, v) = (uv, v)
                        2
Es. 165   [CP 9.9] x2xy
                      +y 2 su semicerchio                  Es. 177       [Esame 06/07/2023] volume di S ⊂ R3
                          2
Es. 166   [CP 9.10] xyex su unione                         Es. 178       [S17F p.35] area, baricentro, solido di rotazione
Es. 167   [CP 9.11] ey/x                                   Es. 179       [S17F p.38] baricentro e volume in R3
                          2  2
Es. 168   [CP 9.13] e−(x +y ) su semidisco                 Es. 180       [Esame 22/01/2024] volume e supercie laterale



  ORDINE CONSIGLIATO PER IL COMPLETAMENTO

                                   5.15.2 Ottimizzazione (48 esercizi, il blocco più grande
      Per valore d'esame decrescente:
                                           6 Integrali multipli (24), poi 2.3 Equazioni del
  e con due riscontri d'esame già emersi), poi
  secondo ordine (25, molto meccaniche una volta ssato il metodo), inne 2.1 EDO del primo
  ordine (19).




                                                          55
