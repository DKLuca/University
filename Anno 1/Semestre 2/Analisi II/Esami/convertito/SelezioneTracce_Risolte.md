---
fonte: "SelezioneTracce_Risolte.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Selezione Tracce d'Esame  Risolte
             Analisi Matematica II            ·   Prof. L. D'Ambrosio            ·   Università di Udine


     Ogni esercizio riporta la traccia originale, il procedimento (quale strumento applicare e perché) e lo
                                             svolgimento con la soluzione.


  DUE CORREZIONI RISPETTO ALLA VERSIONE PRECEDENTE
       Rileggendo le scansioni originali ad alta risoluzione sono emersi due errori di trascrizione
  automatica (OCR) che cambiavano il risultato. Sono stati corretti qui:

    Prova 3/09/2025, es. 1: il denominatore della serie è (2n n)2 = 4n n2 e non 2n n2 . Il raggio
     di convergenza è ρ = 4 (non 2) e l'insieme di convergenza è [0, 8).

    Prova 22/01/2025, es. 1: l'equazione è y ′ = xy 3 ey , con l'esponenziale a moltiplicare (non
                                                                        2


      a denominatore). Di conseguenza la soluzione               non è globale: esplode in tempo nito.

    Nota sulla ricostruzione dei fogli.        Le due prove Parte prima sono scansionate in formato due-pagine-per-

foglio; l'abbinamento fra il quesito 1 e i quesiti 23 di ciascuna prova è stato ricostruito dalla disposizione del libretto.

L'eventuale scambio fra le due prove non inuisce in alcun modo sulle soluzioni.




Contents
1 Prova del 16/09/2024  Parte prima (teoria)                                                                              2
2 Prova del 04/07/2024  Parte prima (teoria)                                                                              5
3 Prova del 17/09/2025                                                                                                     7
4 Prova del 3/09/2025                                                                                                    10
5 Prova del 22/01/2025                                                                                                   13
6 Prova del 04-07-2024 (Parte seconda)                                                                                   16




                                                             1
Prova del 16/09/2024  Parte prima (teoria)
Esercizio 1  Identità di Parseval
 TRACCIA
    Enunciare e dimostrare il teorema dell'identità di Parseval.        Nel caso in cui non si dovesse
 ricordare la dimostrazione nei dettagli, scrivere quali sono gli strumenti (altri teoremi e denizioni)
 che giocano un ruolo importante nella dimostrazione.




 PROCEDIMENTO  quale strumento usare e perché
    La traccia concede esplicitamente una via di riserva: se non ricordi la dimostrazione, elenca
 gli strumenti.   Struttura la risposta in tre blocchi:   (i) enunciato preciso con le ipotesi; (ii) di-
 mostrazione articolata su ortogonalità → Pitagora/Bessel → convergenza in media quadratica;
 (iii) elenco esplicito degli strumenti. Il punto delicato è che Bessel dà solo la disuguaglianza : per
 ottenere l'uguaglianza serve ∥f − SN ∥2 → 0, che discende dal teorema di convergenza della serie
 di Fourier.




 SVOLGIMENTO E SOLUZIONE
      Enunciato. Sia f 2π -periodica eRRiemann-integrabile su [−π, π], con coecienti di Fourier
                                            π
 a0 , am , bm . Posta l'energia E(f ) := π1 −π |f (x)|2 dx = ∥f ∥22 , vale
                                                    ∞
                                               a20 X 2
                                                     am + b2m .
                                                             
                                     E(f ) =      +
                                               2
                                                   m=1

    Dimostrazione. Sia SN (x) = a20 +
                                          PN                             
                                              R π am cos mx + bm sin mx . R π
                                             m=1
    Passo 1 (ortogonalità). Dalle relazioni −π cos mx cos kx dx = πδmk , −π sin mx sin kx dx =
       Rπ
 πδmk , −π cos mx sin kx dx = 0, si verica per calcolo diretto che ⟨f − SN , SN ⟩ = 0 rispetto al
                            1 π
                             R
 prodotto scalare ⟨g, h⟩ :=
                            π −π gh dx: il resto è ortogonale allo spazio delle armoniche no a N .
    Passo 2 (Pitagora e Bessel). Scrivendo f = SN + (f − SN ) come somma di addendi ortogonali,
                                                                    N
                                                             a20 X 2
               E(f ) = E(SN ) + E(f − SN ) ≥ E(SN ) =           + (am + b2m )          ∀N.
                                                             2
                                                                  m=1

 Le somme parziali sono crescenti e limitate da E(f ): la serie converge (disuguaglianza di Bessel ).
     Passo 3 (uguaglianza). Serve E(f −SN ) → 0. Se f è C 1 a tratti, il teorema di convergenza della
 serie di Fourier dà SN → f uniformemente sugli intervalli di continuità; su un intervallo limitato la
                                                              Rπ            2                  2
 convergenza uniforme implica quella in norma ∥ · ∥2 , poiché
                                                               −π |f − SN | ≤ 2π sup |f − SN | → 0.
 Passando al limite in E(f ) = E(SN ) + E(f − SN ) si ottiene la tesi. ■
    Strumenti chiave. Relazioni di ortogonalità del sistema trigonometrico; prodotto scalare
      0
 su C2π e norma indotta; teorema di Pitagora per vettori ortogonali (da cui Bessel); teorema di
 convergenza puntuale/uniforme della serie di Fourier per funzioni C
                                                                         1 a tratti.




Esercizio 2  Sviluppabilità in serie di Taylor
 TRACCIA
    Esibire un esempio di funzione sviluppabile in serie di potenze ed uno di una funzione non
 sviluppabile in serie di potenze di Taylor (giusticando le aermazioni).




                                                   2
 PROCEDIMENTO  quale strumento usare e perché
    Per il primo esempio scegli una funzione di cui sai controllare il resto : la giusticazione consiste
 nel mostrare Rn (x) → 0, non nel calcolare i coecienti. Per il secondo, la richiesta nasconde il
 punto concettuale dell'esercizio: serve una funzione C
                                                              ∞ la cui serie di Taylor converge, ma non

 alla funzione. L'esempio canonico è quello di Cauchy, con tutte le derivate nulle nell'origine.


 SVOLGIMENTO E SOLUZIONE
    Sviluppabile: f (x) = ex . Tutte le derivate valgono ex , quindi f (n) (0) = 1 per ogni n. Il resto
                                                          eξ     n+1 con ξ compreso tra 0 e x; dunque, per
 di Lagrange di ordine n centrato in 0 è Rn (x) =
                                                        (n+1)! x
 ogni x ssato,
                                                   e|x|
                                    |Rn (x)| ≤            |x|n+1 −−−→ 0
                                                 (n + 1)!        n→∞

 perché il fattoriale prevale su qualunque potenza. La serie di Taylor converge quindi a e
                                                                                               x su tutto

 R (ρ = +∞): f è sviluppabile.
    Non sviluppabile: esempio di Cauchy
                                                        2
                                                  (
                                                   e−1/x      x ̸= 0
                                        f (x) =
                                                    0         x = 0.

                                            (n) (x) = P
                                                             −1/x2
                                                              1                                    −1/x2
 Per x ̸= 0 ogni derivata ha la forma f                      e
                                                            n x     con Pn polinomio; poiché e
                                             k
 tende a 0 più rapidamente di quanto 1/x diverga, si prova per induzione che f
                                                                                    (n) (0) = 0 per ogni

 n ≥ 0.
     Di conseguenza il polinomio di Taylor centrato in 0 è identicamente nullo a ogni ordine e la
 serie di Taylor è la serie nulla, che converge (a 0) per ogni x. Tuttavia f (x) = e
                                                                                    −1/x2 > 0 per ogni

 x ̸= 0: in ogni intorno di 0 la somma della serie (= 0) è diversa da f (x). Quindi f è C ∞ ma non
 sviluppabile in serie di Taylor in un intorno dell'origine. ■




Esercizio 3  Dierenziabilità e dierenziale
 TRACCIA
    Sia f : A → R
                    m con A aperto di Rn e x
                                                  0 ∈ A. Scrivere la denizione di dierenziabilità e di
 dierenziale di f nel punto x0 .




 PROCEDIMENTO  quale strumento usare e perché
    È una domanda di pura denizione: vanno riportate con precisione l'esistenza dell'applicazione
 lineare, il limite normalizzato da ∥h∥ e l'unicità che consente di chiamare L il dierenziale. Aggiun-
 gere la rappresentazione tramite gradiente/jacobiana mostra padronanza senza allungare troppo.




 SVOLGIMENTO E SOLUZIONE
    Dierenziabilità. f si dice dierenziabile in x0 se esiste un'applicazione lineare Lx0 : Rn →
 Rm tale che
                                     f (x0 + h) − f (x0 ) − Lx0 (h)
                                 lim                                = 0,
                                 h→0             ∥h∥
 equivalentemente f (x0 + h) = f (x0 ) + Lx0 (h) + o(∥h∥) per h → 0.
    Dierenziale. Tale applicazione lineare, che si dimostra essere unica, si chiama dierenziale
 di f in x0 e si denota df (x0 ) (oppure Df (x0 )).




                                                        3
   Rappresentazione. Se m = 1: Lx0 (h) = ⟨∇f (x0 ), h⟩. In generale Lx0 è rappresentata dalla
matrice jacobiana Jf (x0 ) di formato m × n, cioè Lx0 (h) = Jf (x0 ) h.




                                                 4
Prova del 04/07/2024  Parte prima (teoria)
Esercizio 1  Teorema di Weierstrass in più variabili
 TRACCIA
    Enunciare e dimostrare il teorema di Weierstrass per funzioni di più variabili.      Nel caso in
 cui non si dovesse ricordare la dimostrazione nei dettagli, scrivere quali sono gli strumenti (altri
 teoremi e denizioni) che giocano un ruolo importante nella dimostrazione.




 PROCEDIMENTO  quale strumento usare e perché
    La dimostrazione ha due tempi da tenere separati:        prima si prova che   f è limitata (per
 assurdo, con BolzanoWeierstrass), poi che gli estremi sono raggiunti (successione massimizzante
 + compattezza + continuità). Entrambe le ipotesi vanno spese: la limitatezza di K serve per
 estrarre la sottosuccessione, la chiusura per garantire che il limite resti in K .




 SVOLGIMENTO E SOLUZIONE
    Enunciato. Sia K ⊂ Rn compatto (chiuso e limitato) non vuoto e f : K → R continua. Allora
 f ammette massimo e minimo assoluti su K : esistono xm , xM ∈ K tali che f (xm ) ≤ f (x) ≤ f (xM )
 per ogni x ∈ K .
    Dimostrazione.
     Passo 1: f è limitata. Per assurdo f non sia limitata superiormente: esiste (xh )h ⊂ K
 con f (xh ) → +∞. Essendo K limitato, per BolzanoWeierstrass esiste una sottosuccessione
 xhk → x0 ; essendo K chiuso, x0 ∈ K . Per continuità f (xhk ) → f (x0 ) ∈ R, in contraddizione con
 f (xhk ) → +∞. Analogamente per l'illimitatezza inferiore.
     Passo 2: gli estremi sono raggiunti. Sia M := supK f , nito per il Passo 1. Per denizione
 di estremo superiore esiste (yh )h ⊂ K con f (yh ) → M . Per compattezza esiste yhk → xM ∈ K ;
 per continuità f (yhk ) → f (xM ), ma la stessa successione tende a M : per unicità del limite
 f (xM ) = M , dunque il sup è un massimo. Analogamente per il minimo. ■
     Strumenti chiave. Teorema di BolzanoWeierstrass in Rn ; caratterizzazione sequenziale
 dei chiusi; criterio successionale di continuità; unicità del limite; denizione di estremo superi-
 ore/inferiore.




Esercizio 2  EDO non lineare a variabili separabili
 TRACCIA
    Dare un esempio di equazione dierenziale non lineare a variabili separabili.




 PROCEDIMENTO  quale strumento usare e perché
      Vanno soddisfatte due condizioni simultanee, ed è bene giusticarle entrambe: non linearità (la
 y compare in modo non ane, cioè l'equazione non è della forma y ′ = a(x)y + b(x)) e separabilità
 (il secondo membro si fattorizza come g(x)h(y)). Risolverla esplicitamente non è richiesto, ma è
 una verica rapida e raorza la risposta.




 SVOLGIMENTO E SOLUZIONE
                                              y′ = x y2.
 Non lineare: compare y 2 , quindi non è della forma y ′ = a(x)y + b(x).
   A variabili separabili: il membro destro si fattorizza come g(x)h(y) con g(x) = x e h(y) =


                                                  5
 y2.
       Verica (risoluzione). Per y ̸= 0:
                         dy             1  x2                 −2
                           2
                             = x dx =⇒ − =    + C =⇒ y(x) = 2     ,
                         y              y  2               x + 2C

 cui va aggiunta la soluzione singolare y ≡ 0, persa nella divisione per y .
                                                                              2



Esercizio 3  Raggio di convergenza
 TRACCIA
       Scrivere la denizione di raggio di convergenza.




 PROCEDIMENTO  quale strumento usare e perché
       Distingui la denizione (il valore che separa convergenza e non convergenza) dalle formule di
 calcolo (CauchyHadamard, rapporto). Ricorda di segnalare che nulla si aerma sugli estremi
 |x − x0 | = ρ, dove il comportamento va studiato caso per caso.


 SVOLGIMENTO E SOLUZIONE
       Denizione. Data la serie di potenze                       n
                                                P
                                                  n≥0 an (x − x0 ) , si chiama raggio di convergenza
 l'elemento ρ ∈ [0, +∞] tale che:

   la serie converge assolutamente per ogni x con |x − x0 | < ρ;

  la serie non converge per ogni x con |x − x0 | > ρ (il termine generale non è innitesimo).
 Nulla si aerma per |x − x0 | = ρ: agli estremi il comportamento va studiato separatamente.
       Formule di calcolo. CauchyHadamard, sempre valida:
                                        1                       1       1
                          ρ=              p       ,       con
                                                                0 = +∞, ∞ = 0.
                               lim supn→∞ n |an |

                                                                      an
 Se esiste il limite del rapporto, equivalentemente ρ = limn→∞
                                                                     an+1 .




                                                      6
Prova del 17/09/2025
Esercizio 1  Successione f (x) = arctan(n )
                                       n
                                                             x


 TRACCIA
      Sia fn (x)   := arctan(nx ).    Determinare l'insieme di convergenza puntuale della successione
 (fn )n , il limite di tale successione e in quali insiemi la convergenza è uniforme.


 PROCEDIMENTO  quale strumento usare e perché
      Per il limite puntuale, studia n
                                           x = ex ln n al variare del segno di x: è lì che il comportamento

 cambia.    Per l'uniformità, la strada rapida non è calcolare il sup ovunque, ma osservare che il
 limite è discontinuo in x = 0 mentre le fn sono continue: il teorema limite uniforme di continue
 è continuo esclude subito l'uniformità vicino a 0. Lontano da 0, il sup si calcola sfruttando la
 monotonia di x 7→ n
                         x (l'estremo dell'intervallo realizza il caso peggiore).




 SVOLGIMENTO E SOLUZIONE
      Convergenza puntuale. Per x ssato, nx = ex ln n :
   x > 0: x ln n → +∞ ⇒ nx → +∞ ⇒ fn (x) → arctan(+∞) = π2 ;

   x = 0: n0 = 1 per ogni n, quindi fn (0) = arctan 1 = π4 (costante);

  x < 0: x ln n → −∞ ⇒ nx → 0+ ⇒ fn (x) → arctan 0 = 0.
 L'insieme di convergenza puntuale è dunque tutto R, con

                                            
                                            0
                                                  x<0
                                     f (x) = π/4 x = 0
                                            
                                              π/2 x > 0.
                                            

      Convergenza uniforme. Il limite f è discontinuo in x = 0, mentre ogni fn è continua: se
 la convergenza fosse uniforme su un intervallo contenente 0, il limite dovrebbe essere continuo lì.
 Quindi   non c'è convergenza uniforme su alcun insieme che contenga 0 (in particolare non su R).
      Sia ora a > 0. Su [a, +∞), essendo x 7→ n
                                                       x crescente, il sup dell'errore si realizza in x = a:

                                                π  π
                                sup fn (x) −      = − arctan(na ) −−−→ 0.
                                x≥a             2  2              n→∞


 Simmetricamente su (−∞, −a]:          supx≤−a |fn (x) − 0| = arctan(n−a ) → 0.
    Soluzione. Convergenza puntuale su tutto R alla funzione a gradino sopra scritta; convergenza
 uniforme su [a, +∞) e su (−∞, −a] per ogni a > 0, non uniforme su ogni insieme contenente
 0.


Esercizio 2  Famiglia f (x, y) = −αx + y +
                                 α
                                                   2        2    x4
                                                                 4

 TRACCIA                                                 4
      Per ogni α ∈ R sia fα (x, y) := −αx
                                              2 + y 2 + x . (a) Determinare i punti critici di f (al variare
                                                                                                α
                                                        4
 del parametro α) e classicarli. (b) Determinare fα (R ).
                                                                 2




 PROCEDIMENTO  quale strumento usare e perché
      (a) Annulla il gradiente: l'equazione in x si fattorizza e il numero di soluzioni dipende dal


                                                         7
 segno di α  la discussione va organizzata sui casi α < 0, α = 0, α > 0. Attenzione al caso α = 0,
 in cui l'hessiana è degenere e il criterio non decide: lì serve l'analisi diretta del segno di f .    (b)
 Poiché y
            2 assume indipendentemente tutti i valori ≥ 0, l'immagine è determinata dal minimo di

 fα ; basta quindi studiare la funzione di una variabile g(x) = fα (x, 0).


 SVOLGIMENTO E SOLUZIONE
    (a) Punti critici. ∇fα = −2αx + x3 , 2y = x(x 2 − 2α), 2y . Da 2y = 0 segue y = 0; da
                                                                           
    2
                                              √
 x(x − 2α) = 0 segue            se α > 0, x = ± 2α.
                   x = 0 oppure,
                    −2α + 3x2 0
    Hessiana: H =                 .
                        0     2
   α < 0: unico punto critico (0, 0), con H = diag(−2α, 2) e −2α > 0: denita positiva, quindi
    minimo. È anche assoluto, poiché fα = |α|x2 + y 2 + x4 ≥ 0 = fα (0, 0).
                                                          4



   α = 0: unico punto critico (0, 0), H = diag(0, 2) degenere: il criterio non decide. Direttamente,
    f0 = y 2 + x4 ≥ 0 = f0 (0, 0): minimo assoluto.
                 4



   α > 0: tre punti critici.
          (0, 0): H = diag(−2α, 2), autovalori discordi ⇒ sella.
              √
          (± 2α, 0): qui x2 = 2α, quindi −2α + 3x2 = 4α > 0 e H = diag(4α, 2) denita positiva
           ⇒ minimi, con valore fα = −2α2 + α2 = −α2 .
     (b) Immagine. Posto g(x) := fα (x, 0) = x4 − αx2 (pari, → +∞ per |x| → ∞), e osservato
                                                      4


 che y
         2 copre indipendentemente [0, +∞):

                                                            (
                                2
                                                           [ 0, +∞)      α ≤ 0,
                          fα (R ) = min fα , +∞ =
                                                             [ −α2 , +∞) α > 0.


Esercizio 3  Problema di Cauchy y =          ′      tet
                                                     2y

 TRACCIA
                                                  tet
     Si consideri il problema di Cauchy   y′ =        ,    y(0) = y0 . (a) Esiste qualche valore di y0 ∈ R
                                                  2y
 per cui il problema ammette soluzione costante?           (b) Determinare le eventuali soluzioni nel caso
 y0 = −1.


 PROCEDIMENTO  quale strumento usare e perché
    (a) Non risolvere: imponi direttamente y ≡ c, cioè y ′ ≡ 0, e verica se l'equazione può essere
 soddisfatta su un intervallo (non solo in un punto isolato). È il ragionamento che l'esercizio
 vuole. (b) Equazione a variabili separabili; l'integrale a destra richiede una integrazione per parti.
 Due punti da non dimenticare: la scelta del segno della radice, dettata dal dato iniziale, e la
 determinazione del dominio massimale tramite lo studio del segno del radicando.




 SVOLGIMENTO E SOLUZIONE
     (a) Se y ≡ c fosse soluzione, allora y ′ ≡ 0 e dovrebbe valere te2c = 0 per ogni t in un intorno
                                                                           t


 di 0. Ma te = 0 solo nel punto isolato t = 0, non su un intervallo. Non esiste alcun y0 per cui
            t

 la soluzione sia costante.
     (b) Separando le variabili: 2y dy = tet dt. Integrando (per parti a destra, tet dt = tet −et +C ):
                                                                                    R


                                          y 2 = et (t − 1) + C.


                                                      8
Imponendo y(0) = −1:     1 = e0 (0 − 1) + C = −1 + C ⇒ C = 2. Dunque y 2 (t) = et (t − 1) + 2 e,
poiché y0 = −1 < 0, per continuità si sceglie il ramo negativo:

                                             p
                                     y(t) = − et (t − 1) + 2 .

   Dominio. Sia h(t) := et (t − 1) + 2. Allora h′ (t) = tet , negativa per t < 0 e positiva per t > 0:
h ha minimo in t = 0 con h(0) = 1 > 0. Inoltre h(t) → 2 per t → −∞ e h(t) → +∞ per t → +∞.
Quindi h > 0 su tutto R e la soluzione è denita (dunque globale) su R.




                                                  9
Prova del 3/09/2025
Esercizio 1  Serie di potenze
 TRACCIA
    Determinare gli intervalli di convergenza semplice e uniforme della serie

                                         ∞          √
                                         X n+           n+1
                                                              (x − 4)n .
                                               (2n n)2
                                         n=1




 PROCEDIMENTO  quale strumento usare e perché                                         √
    Prima semplica il coeciente:     (2n n)2 = 4n n2 , quindi an ∼ 4n1n  il termine n + 1 è
 trascurabile rispetto a n. Applica CauchyHadamard per il raggio, poi studia separatamente i due
 estremi (il criterio non dice nulla lì). Per l'uniformità: convergenza uniforme sui compatti interni
 per il teorema di struttura, estesa no a un estremo in cui la serie converge grazie al teorema di
 Abel.


 SVOLGIMENTO E SOLUZIONE √           √
                       n+ n+1     n+ n+1    1
    Raggio. Posto an =    n   2
                                =    n  2
                                          ∼ n ,
                        (2 n)       4 n    4 n
                                                     1/n
                                   √            1    1       1
                         lim sup   n
                                       an = lim            =           =⇒       ρ = 4.
                             n                n 4    n       4

 Centro x0 = 4:     convergenza assoluta per        |x − 4| < 4, cioè x ∈ (0, 8); non convergenza per
 |x − 4| > 4.                                                              √     √
                                                       n+                   1  n+1 n+1
    Estremo x = 8 ((x − 4)n = 4n ): il termine diventa           2
                                                                          = +            . La prima
                                                               n            n      n2
 parte è la serie armonica (diverge), la seconda converge (∼ n
                                                               −3/2 ): la serie diverge.
                                                                              √
                                                                          n+ n+1
     Estremo x = 0 ((x − 4) = (−4) ): il termine diventa (−1)
                                n         n                             n            , serie a segni
                      √                                                       n2
 alterni con bn =
                    n+ n+1
                      n2
                           → 0 decrescente denitivamente: per il criterio di Leibniz converge
 (semplicemente, non assolutamente).

    Soluzione.
         convergenza semplice:     [ 0, 8)     convergenza uniforme:            [ 0, 8 − ε ] ∀ε ∈ (0, 8)

 La convergenza è uniforme su ogni compatto contenuto in (0, 8) e, per il teorema di Abel, si
 estende no all'estremo sinistro x = 0 (dove la serie converge). Non è uniforme su tutto [0, 8),
 perché avvicinandosi a x = 8 la serie diverge.




Esercizio 2  Estremi su una regione triangolare
 TRACCIA
                          y2
    Sia f (x, y)   := x2 +   + x2 y + 2. (a) Determinare i punti critici di f e classicarli. (b)
                          2
 Determinare massimo e minimo assoluto di f nella regione triangolare chiusa di vertici O = (0, 0),
 A = (1, −1), B = (1, 0).




                                                        10
 PROCEDIMENTO  quale strumento usare e perché
    (b) è un problema di Weierstrass su un compatto: la procedura standard è interno + bordo.
 Primo passo: individuare quali punti critici cadono internamente al triangolo (qui nessuno: vanno
 scartati, non classicati di nuovo). Secondo passo: parametrizzare i tre lati riducendoli a funzioni
 di una variabile e studiarne la monotonia. Se tutti i lati risultano monotoni, gli estremi cadono
 nei vertici e basta confrontare tre numeri.




 SVOLGIMENTO E SOLUZIONE
    (a) Punti critici. ∇f = 2x + 2xy, y + x2 = 2x(1 + y), y + x2 . Da 2x(1 + y) = 0: x = 0
                                                                            

 oppure y = −1; da y + x
                             2 = 0: y = −x2 .

   x = 0 ⇒ y = 0: punto (0, 0).

  y = −1 ⇒ x2 = 1 ⇒ x = ±1: punti (1, −1) e (−1, −1).
                                                                         2
 Hessiana: fxx = 2 + 2y , fxy = 2x, fyy = 1, quindi det H = (2 + 2y) − 4x .

  (0, 0): det H = 2 > 0, fxx = 2 > 0 ⇒ minimo locale, f = 2.

   (1, −1): det H = 0 − 4 = −4 < 0 ⇒ sella, f = 25 .

   (−1, −1): det H = −4 < 0 ⇒ sella, f = 25 .
     (b) Estremi sul triangolo T . Nessun punto critico è interno a T : (0, 0) e (1, −1) sono
 vertici, (−1, −1) è esterno. Gli estremi vanno quindi cercati sul bordo.
     Lato OA (y = −x, x ∈ [0, 1]): g(x) = f (x, −x) = 32 x2 − x3 + 2, con g ′ (x) = 3x(1 − x) ≥ 0:
                                  5
 crescente da g(0) = 2 a g(1) = .
                                  2
                                                        2
     Lato AB (x = 1, y ∈ [−1, 0]): h(y) = 3 + y + y2 , con h′ (y) = 1 + y ≥ 0: crescente da h(−1) = 52
 a h(0) = 3.
     Lato BO (y = 0, x ∈ [0, 1]): f (x, 0) = x2 + 2, crescente da 2 a 3.
                                                                                                   5
     Tutti i lati sono monotoni: gli estremi cadono nei vertici. Confrontando f (O) = 2, f (A) = ,
                                                                                                   2
 f (B) = 3:
                        max f = 3 in B = (1, 0),       min f = 2 in O = (0, 0).
                         T                                  T



Esercizio 3  Campo vettoriale lungo una curva
 TRACCIA
                                                                                           2
    Sia F (x, y, z) := (x, yz, z) un campo vettoriale e r la curva r(t) := (cos t, sin t, t ), t ∈ [−π, π].
 (a) Stabilire se r è chiusa e se è regolare (eventualmente a tratti). (b) Calcolare l'integrale del
 campo F lungo r . Dal valore trovato, è possibile dedurre se il campo è conservativo?




 PROCEDIMENTO  quale strumento usare e perché
     (a) Chiusa si verica confrontando r(−π) e r(π); regolare richiede r′ (t) ̸= 0 per ogni t:
 conviene calcolare ∥r (t)∥ e mostrare che non si annulla mai. (b) Calcola F (r(t)) · r (t) e, prima
                       ′    2                                                             ′

 di integrare, osserva la parità : su un intervallo simmetrico una funzione dispari ha integrale nullo,
 il che evita ogni calcolo di primitive. La domanda nale è concettuale e contiene una trappola:
 un valore nullo su una curva chiusa non basta. Per rispondere davvero, calcola il rotore.




 SVOLGIMENTO E SOLUZIONE
    (a) r(−π) = (cos(−π), sin(−π), π 2 ) = (−1, 0, π 2 ) e r(π) = (−1, 0, π 2 ): coincidono, quindi r è
 chiusa.
    r′ (t) = (− sin t, cos t, 2t) è continua e ∥r′ (t)∥2 = sin2 t + cos2 t + 4t2 = 1 + 4t2 ≥ 1 > 0: il


                                                    11
vettore derivato non si annulla mai, dunque r è        regolare su tutto [−π, π] (non solo a tratti).
   (b) F (r(t)) = (cos t, t2 sin t, t2 ), quindi
           F (r(t)) · r′ (t) = − cos t sin t + t2 sin t cos t + 2t3 = sin t cos t (t2 − 1) + |{z}
                                                                                              2t3 .
                                                                                           dispari
                                                                      |        {z        }
                                                                           dispari

La funzione integranda è dispari e l'intervallo [−π, π] è simmetrico rispetto all'origine, dunque

                                               Z
                                                    F · dr = 0.
                                                r

   Il campo è conservativo? No, e comunque non lo si potrebbe dedurre dal valore
trovato: la conservatività richiede l'annullamento dell'integrale su ogni curva chiusa del dominio,
non su una sola. Per decidere si usa il rotore:
                                                             
         ∇ × F = ∂y F3 − ∂z F2 , ∂z F1 − ∂x F3 , ∂x F2 − ∂y F1 = (−y, 0, 0) ̸≡ (0, 0, 0).

Il campo non è irrotazionale e l'irrotazionalità è condizione           necessaria per la conservatività:
dunque F   non è conservativo.




                                                       12
Prova del 22/01/2025
Esercizio 1  Problema di Cauchy y = xy e          ′            3 y2


 TRACCIA                                               2
    È dato il problema di Cauchy   y ′ = xy 3 ey , y(0) = 1. (a) Dopo aver dedotto che il problema
 ammette un'unica soluzione locale y = y(x), calcolare il valore di minimo di y sul suo dominio
 di esistenza massimale, giusticando la risposta; (b) dimostrare che y(x) è pari; (c) dire se la
 soluzione y è globale.




 PROCEDIMENTO  quale strumento usare e perché
    Tutti e tre i punti si risolvono senza calcolare esplicitamente la soluzione. (a) L'unicità (TEUL)
 serve come strumento: garantisce che la soluzione non possa incrociare la soluzione costante y ≡ 0,
 da cui il segno di y ; noto il segno, il segno di y
                                                            ′ dipende solo da x e la monotonia dà subito il

 minimo.  (b) Tecnica standard: poni z(x) := y(−x), verica che risolve lo stesso problema di
 Cauchy e concludi per unicità. Non serve alcun calcolo esplicito. (c) Qui il fattore e
                                                                                       y 2 è decisivo:

 la crescita è super-polinomiale, quindi ci si aspetta esplosione in tempo nito. Il modo rigoroso e
 rapido è il confronto con un'equazione più semplice di cui si conosce l'istante di esplosione.




 SVOLGIMENTO E SOLUZIONE
     Unicità. f (x, y) = xy 3 ey è di classe C ∞ su R2 , quindi in particolare continua e localmente
                                 2


 lipschitziana in y : per il TEUL il problema ammette un'unica soluzione locale.
     (a) Minimo. La funzione costante y ≡ 0 risolve l'equazione; per unicità, la soluzione con
 y(0) = 1 ̸= 0 non può mai annullarsi, dunque y(x) > 0 su tutto il dominio. Allora in y ′ (x) =
              2                  2
 x y(x)3 ey(x) i fattori y 3 e ey sono positivi e il segno di y ′ coincide con quello di x: y è decrescente
                                            ′
 per x < 0, crescente per x > 0, con y (0) = 0. Quindi x = 0 è punto di minimo assoluto sul
 dominio massimale e
                                             min y = y(0) = 1.
    (b) Parità. Poniamo z(x) := y(−x). Allora
                                            h                  2
                                                                 i             2
                     z ′ (x) = −y ′ (−x) = − (−x) y(−x)3 ey(−x) = x z(x)3 ez(x) ,

 cioè z risolve la stessa equazione, con lo stesso dato z(0) = y(0) = 1. Per unicità z ≡ y sul dominio
 comune, cioè y(−x) = y(x): yè pari. ■
    (c) Globalità. Poiché y ≥ 1 su tutto il dominio (punto (a)), per x ≥ 0 vale ey ≥ e > 1 e
                                                                                  2


 quindi
                                                                2
                                         y ′ (x) = x y 3 ey         ≥ x y3.
 Confrontiamo con il problema u
                                     ′ = xu3 , u(0) = 1, che si risolve esplicitamente:


                       du              1     x2 1              1
                        3
                          = x dx =⇒ −    2
                                           =   − =⇒ u(x) = √        ,
                       u              2u     2  2            1 − x2
                         −
 che esplode per x → 1 . Per il teorema del confronto y(x) ≥ u(x) nché entrambe sono denite,
 dunque y esplode a un istante x
                                     ∗ ≤ 1 nito.

    Più precisamente, separando le variabili si ottiene la caratterizzazione implicita

                                              Z y
                                                          ds      x2
                                                                =    ,
                                               1       s 3 e s2   2




                                                           13
 e l'integrale a sinistra converge per y → +∞ (l'integranda decade come e
                                                                                    −s2 ) a un valore nito
    R∞          2                                              √
 I = 1 s−3 e−s ds: l'esplosione avviene esattamente in x∗ = 2I , nito.
                                                                 ∗
    Per la parità dimostrata al punto (b), lo stesso accade in −x . Quindi


                 la soluzione   non è globale: è denita solo su (−x∗ , x∗ ) con x∗ ≤ 1.


Esercizio 2  Successione di funzioni
 TRACCIA
    Studiare la convergenza (puntuale e uniforme) della successione di funzioni (fn )n denita come


                                                   n cos(1 + x2 ) + n2 x
                                       fn (x) :=                         .
                                                        n2 (1 + x2 )


 PROCEDIMENTO  quale strumento usare e perché
    Non calcolare limiti a forza bruta: spezza la frazione dividendo numeratore e denominatore per
 n2 . La successione si separa in un termine indipendente da n (il limite) più un resto che contiene
 1
 n in fattore. A quel punto l'errore |fn − f | è esplicito e, maggiorando i fattori limitati (| cos | ≤ 1,
 1 + x2 ≥ 1), si ottiene una stima indipendente da x: è esattamente ciò che serve per l'uniformità.


 SVOLGIMENTO E SOLUZIONE
    Dividendo numeratore e denominatore per n :
                                                        2


                                                    x      cos(1 + x2 )
                                       fn (x) =          +              .
                                                  1 + x2    n(1 + x2 )

    Limite puntuale. Per ogni x ssato il secondo addendo tende a 0, quindi
                                                           x
                                   fn (x) −→ f (x) :=                ∀x ∈ R,
                                                         1 + x2
 con convergenza puntuale su tutto R.
    Convergenza uniforme. Stimiamo l'errore usando | cos(·)| ≤ 1 e 1 + x2 ≥ 1:
                                            cos(1 + x2 )       1       1
                    |fn (x) − f (x)| =              2
                                                         ≤        2
                                                                     ≤          ∀x ∈ R.
                                             n(1 + x )     n(1 + x )   n
                                                                               1
 La maggiorazione non dipende da x, quindi supx∈R |fn (x) − f (x)| ≤
                                                                               n → 0:

                                   la convergenza è uniforme su tutto R.




Esercizio 3  Punti critici e piano tangente
 TRACCIA
    Sia f (x, y) := x
                        4 − 2x2 y + y 4 .   (a) Si determinino tutti i punti critici di f e se ne studi la
 natura. (b) Scrivere il piano tangente al graco di z = f (x, y) nel punto (1, 0).




 PROCEDIMENTO  quale strumento usare e perché
    (a) Il sistema ∇f = 0 si risolve fattorizzando la prima equazione e sostituendo nella seconda.
 Nell'origine l'hessiana è nulla : il criterio non decide e occorre l'analisi diretta del segno di f




                                                       14
lungo direzioni opportune  la scelta giusta è la curva y = x , suggerita dal termine −2x y . (b)
                                                                      2                             2

Applicazione diretta della formula del piano tangente: quota + gradiente nel punto. Non serve
vericare la dierenziabilità: f è un polinomio, quindi C
                                                               ∞.




SVOLGIMENTO E SOLUZIONE
   (a) Punti critici. ∇f = 4x3 − 4xy, −2x2 + 4y 3 = 4x(x2 − y), −2x2 + 4y 3 .
                                                                                                   
                                                                                                           Da
4x(x2 − y) = 0: x = 0 oppure y = x2 .
 x = 0: la seconda equazione dà 4y 3 = 0 ⇒ y = 0. Punto (0, 0).

  y = x2 con x ̸= 0: sostituendo, −2x2 + 4x6 = 0 ⇒ 2x2 (2x4 − 1) = 0 ⇒ x4 = 21 , cioè x = ±2−1/4
            2
   e y = x = 2
                 −1/2 .
                         −1/4 , 2−1/2 , −2−1/4 , 2−1/2 .
                                                      
Punti critici: (0, 0), 2
                          2
    Hessiana: fxx = 12x − 4y , fxy = −4x, fyy = 12y .
                                                         2
                           
                        0 0
    In (0, 0): H =                                                                              4
                              , criterio inconcludente. Analisi diretta: lungo x = 0 si ha f = y ≥ 0;
                        0 0
              2
lungo y = x si ha


                     f (x, x2 ) = x4 − 2x4 + x8 = x4 (x4 − 1) < 0         per 0 < |x| < 1.


In ogni intorno di (0, 0) la funzione assume sia valori positivi sia negativi, mentre f (0, 0) = 0:
dunque (0, 0) è un   punto di sella.
   In (±2−1/4 , 2−1/2 ): posto b := 2−1/2 (così x2 = b, y = b, y 2 = 21 ):
                                                                             2
               fxx = 12b − 4b = 8b > 0,          fyy = 12 · 12 = 6,         fxy = 16x2 = 16b,

                                       det H = 8b · 6 − 16b = 32b > 0.
Hessiana denita positiva:     entrambi sono      minimi locali, con valore f = x4 − 2x2 y + y 4 =
b2 − 2b2 + b4 = 21 − 1 + 41 = − 14 .
   (b) Piano tangente in (1, 0). f è un polinomio, dunque C ∞ e dierenziabile.
              f (1, 0) = 1,     fx (1, 0) = 4 · 1 − 0 = 4,      fy (1, 0) = −2 · 1 + 0 = −2.

Quindi ∇f (1, 0) = (4, −2) e


   z = f (1, 0) + fx (1, 0)(x − 1) + fy (1, 0)(y − 0) = 1 + 4(x − 1) − 2y =⇒           z = 4x − 2y − 3 .

Verica: in (1, 0) si ottiene z = 4 − 0 − 3 = 1 = f (1, 0). ✓




                                                     15
Prova del 04-07-2024 (Parte seconda)
Esercizio 1  Integrale doppio con valore assoluto
 TRACCIA                                ZZ
     Calcolare l'integrale doppio               2|x|y dx dy dove D è il triangolo di vertici (−1, 0), (2, 0),
                                            D
 (0, 2).


 PROCEDIMENTO  quale strumento usare e perché
     Il triangolo è normale rispetto a y : conviene far variare y ∈ [0, 2] e ricavare i due lati obliqui
 come funzioni x = x(y). Il punto delicato è il             valore assoluto: poiché per ogni y l'intervallo di
 integrazione in x contiene lo 0, l'integrale interno va spezzato in [xmin , 0] e [0, xmax ], cambiando
 segno nel primo. Chi dimentica di spezzare ottiene un risultato sbagliato.




 SVOLGIMENTO E SOLUZIONE
     Descrizione del dominio. Il lato da (−1, 0) a (0, 2) ha equazione x = y2 − 1; quello da (2, 0)
 a (0, 2) ha equazione x = 2 − y . Per y ∈ [0, 2]:

                                 n                                                          o
                                                                      y
                              D = (x, y) : 0 ≤ y ≤ 2,                 2 −1≤x≤2−y             ,

 e in tale intervallo x varia da un valore negativo a uno positivo: contiene sempre 0.
     Integrale interno (spezzando per il valore assoluto):
               Z 2−y                  Z 0                     Z 2−y                        2
                                                                                     y
                          2|x| dx =            2(−x) dx +              2x dx =       2 −1        + (2 − y)2 .
                  y/2−1                y/2−1                      0

                  y   2 y 2
 Espandendo:
                  2 −1  = 4 − y + 1 e (2 − y)2 = y 2 − 4y + 4, la cui somma è 54 y 2 − 5y + 5.
     Integrale esterno:
             Z 2                     Z 2                       h                  i2
                y 54 y 2 − 5y + 5 dy =      5 3
                                            4 y − 5y 2
                                                       + 5y   dy =   5 4
                                                                     16 y − 5 3
                                                                            3 y + 5 2
                                                                                  2 y    .
              0                                  0                                                              0

                           5         5       5           40            40  5
 Valutando in y = 2:
                           16 · 16 − 3 · 8 + 2 · 4 = 5 − 3 + 10 = 15 − 3 = 3 .
                                                ZZ
                                                                         5
                                                         2|x|y dx dy =
                                                     D                   3


Esercizio 2  Punti critici e derivata direzionale
 TRACCIA
     Sia f (x, y) = x y(x − y + 1). (a) Si determinino tutti i punti critici di f e se ne studi la natura.
                     2

 (b) Calcolare la derivata direzionale Dv (1, 1) con v = (3, 4).


 PROCEDIMENTO  quale strumento usare e perché
     (a) Espandi il prodotto prima di derivare, poi fattorizza le derivate: emerge che x = 0 annulla
 entrambe, quindi i punti critici non sono isolati ma formano un'intera retta.                          È il tratto carat-
 teristico di questo esercizio: su tale retta l'hessiana è degenere e la natura va discussa studiando




                                                             16
 il segno di f nelle vicinanze, al variare del punto.      (b) Il vettore v = (3, 4) non è unitario: va
 normalizzato prima di applicare Dv = ⟨∇f, v̂⟩. È l'errore più frequente in questo tipo di quesito.




 SVOLGIMENTO E SOLUZIONE
                                3
    Espandendo: f (x, y) = x y − x y
                                        2 2 + x2 y , da cui


      fx = 3x2 y − 2xy 2 + 2xy = xy(3x − 2y + 2),             fy = x3 − 2x2 y + x2 = x2 (x − 2y + 1).

    (a) Punti critici.
    Caso x = 0: entrambe le derivate si annullano per ogni y . L'intera retta {(0, y) : y ∈ R} è
 fatta di punti critici (coerentemente con f (0, y) ≡ 0).
     Caso x ̸= 0: da fy = 0 segue x = 2y − 1.
   con y = 0: x = −1, punto (−1, 0);

   con 3x− 2y + 2 = 0 e x = 2y − 1: 3(2y − 1) − 2y + 2 = 0 ⇒ 4y = 1 ⇒ y = 41 , x = − 12 , punto
      − 12 , 14 .
                                     2              2
     Hessiana: fxx = 6xy − 2y + 2y , fxy = 3x − 4xy + 2x, fyy = −2x .
                                                                              2

     In (−1, 0): fxx = 0, fxy = 3 − 0 − 2 = 1, fyy = −2, quindi det H = 0 − 1 = −1 < 0: sella.
     In
       −      2 , 4 1: fxx3 = −
                1 1               3    1  1     3         3    1           1         1
                                  4 − 8 + 2 = − 8 , fxy = 4 + 2 − 1 = 4 , fyy = − 2 , da cui det H =
  − 8 − 2 − 16 = 16 − 16 = 8 > 0 con fxx < 0: massimo locale, di valore f = 64
    3        1                  1    1                                                   1
                                                                                           .
     Sulla retta x = 0: per x piccolo e y vicino a y0 si ha f (x, y) ≈ x y0 (1 − y0 ), quindi il segno di
                                                                            2

 f vicino al punto (0, y0 ) è quello di y0 (1 − y0 ) (mentre f (0, y0 ) = 0):
   0 < y0 < 1: f > 0 attorno ⇒ minimi (non stretti);

   y0 < 0 oppure y0 > 1: f < 0 attorno ⇒ massimi (non stretti);

   y0 = 0 e y0 = 1: casi di transizione, degeneri; servirebbe un'analisi di ordine superiore.
                                                                    √
     (b) Derivata direzionale. Il vettore va normalizzato: ∥v∥ = 9 + 16 = 5, quindi v̂ =              3 4
                                                                                                          
                                                                                                      5, 5 .
 Inoltre


     fx (1, 1) = 1 · 1 · (3 − 2 + 2) = 3,      fy (1, 1) = 1 · (1 − 2 + 1) = 0 =⇒ ∇f (1, 1) = (3, 0).

 Poiché f è un polinomio (dunque dierenziabile), vale la formula del gradiente:


                             Dv f (1, 1) = ⟨∇f (1, 1), v̂⟩ = 3 · 35 + 0 · 45 = 59 .


Esercizio 3  Serie di Fourier di una funzione 4-periodica
 TRACCIA                                              (
                                                       1 − x x ∈ [0, 1]
     Sia f funzione 4-periodica denita come f (x) :=                      e riessa dispari in [−2, 0[.
                                                       0        x ∈ ]1, 2]
 (a) Calcolare esplicitamente i coecienti di Fourier di f ; (b) scrivere la serie di Fourier di f in
 forma compatta; (c) studiare la convergenza della serie di Fourier di f .




 PROCEDIMENTO  quale strumento usare e perché
    Prima di ogni calcolo, sfrutta la   simmetria: la funzione è dispari, quindi tutti gli am (compreso
 a0 ) sono nulli e resta solo la serie di seni  questo dimezza il lavoro.            Con periodo T   = 4 il
                                            π
 semiperiodo è L = 2 e la pulsazione è
                                            2 : attenzione a non usare le formule del caso 2π -periodico.
 Nell'integrale, il contributo su ]1, 2] è nullo perché lì f     ≡ 0. Per (c) individua i punti di salto




                                                      17
vericandoli, senza darli per scontati: qui l'unico salto è in x ≡ 0, generato proprio dalla riessione
dispari.




SVOLGIMENTO E SOLUZIONE
   (a) Coecienti. f è dispari, quindi am = 0 per ogni m ≥ 0 e restano solo i coecienti dei
seni. Con T = 4, L = 2:

                Z L                          Z 2                       Z 1
            2                    mπx                     mπx                       mπx 
       bm =            f (x) sin        dx =     f (x) sin        dx =     (1 − x) sin        dx,
            L      0               L          0              2          0                2
                                                  mπ
poiché su ]1, 2] si ha f ≡ 0. Posto k :=
                                                   2 e integrando per parti:
                Z 1                             Z 1
                                  1 − cos k                          cos k sin k
                  sin(kx) dx =              ,       x sin(kx) dx = −      + 2 ,
                0                     k           0                    k    k
                    Z 1
                                              1 − cos k cos k sin k       1 sin k
              =⇒        (1 − x) sin(kx) dx =            +       − 2 = − 2 .
                     0                            k         k      k      k   k
                   mπ
Sostituendo k =
                    2 :


                                                                      4 sin mπ
                                                                                      
                                                                  2          2
                                am = 0 ∀m ≥ 0,              bm =    −
                                                                 mπ     m2 π 2
                   mπ
                        
Esplicitando sin
                    2       ∈ {1, 0, −1, 0} per m ≡ 1, 2, 3, 0 (mod 4):

                                              2      4
                                           
                                           
                                                −   2  2
                                                             m ≡ 1 (mod 4),
                                            mπ m π
                                           
                                           
                                           
                                              2
                                     bm =                    m pari,
                                           
                                            mπ
                                            2 + 4
                                           
                                           
                                                             m ≡ 3 (mod 4).
                                           
                                             mπ m2 π 2
   (b) Forma compatta.
                                            ∞
                                                  "                   #
                                            X          2   4 sin mπ
                                                                  2
                                                                               mπx 
                                 Sf (x) =                −                 sin        .
                                                      mπ     m2 π 2              2
                                            m=1

   (c) Convergenza. Verichiamo i punti di raccordo su un periodo:
 in x = 1: f (1− ) = 1 − 1 = 0 e f (1+ ) = 0 ⇒ continua (c'è solo un punto angoloso);

 in x = 2: f (2− ) = 0 e, per periodicità e disparità, f (2+ ) = f (−2+ ) = −f (2− ) = 0 ⇒ continua;

 in x = 0: f (0+ ) = 1 mentre f (0− ) = −f (0+ ) = −1 ⇒ salto di ampiezza 2.
              1
Dunque f è C a tratti con salti solo nei punti x ≡ 0 (mod 4). Per il teorema di convergenza:

 la serie converge puntualmente su tutto R;

 nei punti di continuità converge a f (x);
                                                                                      −   +
 nei punti di salto x = 4k converge alla media dei limiti laterali, f (0 )+f
                                                                           2
                                                                              (0 )
                                                                                   = −1+1
                                                                                      2   = 0;

 la convergenza è uniforme su ogni intervallo chiuso privo di punti ≡ 0 (mod 4), ma non in
   un intorno di tali punti (fenomeno di Gibbs).




                                                           18
