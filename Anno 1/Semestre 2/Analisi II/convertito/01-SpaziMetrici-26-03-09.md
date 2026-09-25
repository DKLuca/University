---
fonte: "01-SpaziMetrici-26-03-09.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Spazi metrici


     Lorenzo D’Ambrosio
lorenzo.dambrosio@uniud.it



       9 marzo 2026
Sia D ⊆ R2 non vuoto e f : D → R.
A seconda della convenienza, f può essere indicata con
                − NOTAZIONE VETTORIALE: f come funzione della variabile vettoriale
                P ∈ D, cioè     f : P → f (P)
                a volte anche con P ∈ D, e f : P → f (P) (il grassetto per indicare che P
                è un vettore)
                − NOTAZIONE SCALARE: f come funzione delle due variabili reali
                (x, y ) ∈ D, cioè f : (x, y ) → f (x, y ) ∈ R

Nota che il grafico di una funzione reale di due variabili reali è un sottoinsieme di R3 ,
precisamente:
                        Gf = {(x, y , f (x, y )) | (x, y ) ∈ D } ⊂ R3 .

                p
Es. f (x, y ) = 9 − x 2 − y 2 . Ha un insieme di definizione D = {(x, y ) t.c. x 2 + y 2 ≤ 9}
ossia il disco di centro 0 e raggio 3.
FIGURA
Sia D ⊆ R3 non vuoto e f : D → R.
A seconda della convenienza, f può essere indicata con
                 − NOTAZIONE VETTORIALE: f come funzione della variabile vettoriale
                 P ∈ D, cioè     f : P → f (P)
                 a volte anche con P ∈ D, e f : P → f (P)
                 − NOTAZIONE SCALARE: f come funzione delle due variabili reali
                 (x, y , z) ∈ D, cioè f : (x, y , z) → f (x, y , z) ∈ R

Nota che il grafico di una funzione reale di tre variabili reali è un sottoinsieme di R4 ,
precisamente:
                      Gf = {(x, y , z, f (x, y , z)) | (x, y , z) ∈ D } ⊂ R4 .
               p
Es. f (x, y ) = 9 − x 2 − y 2 − z 2 . Ha un insieme di definizione
D = {(x, y , z) t.c. x 2 + y 2 + z 2 ≤ 9} ossia la palla di centro 0 e raggio 3.
Problemi: per D ⊆ R2 non vuoto, (x0 , y0 ) ∈ D e f : D → R funzione data,

  1   Cosa vuol dire che f è continua in (x0 , y0 )?

  2   Cosa vuol dire che f è differenziabile in (x0 , y0 )?

                                              ovvero:

  3   quando è definito piano tangente al grafico di f nel punto (x0 , y0 , f (x0 , y0 ))? e in tal
      caso come posso calcolare la sua equazione?
La definizione di limite per una funzione f : R → R può essere enunciata in termini di
distanze. Ad esempio, nel caso in cui x0 ∈ R e ℓ ∈ R, abbiamo:

          lim f (x) = ℓ ⇐⇒ ∀ε > 0 ∃δ > 0 : 0 < |x − x0 | < δ ⇒ |f (x) − ℓ| < ε
         x→x0


dove:
    |x − x0 | è la distanza tra x e x0 nel dominio (R in questo caso),
    |f (x) − ℓ| è la distanza tra f (x) e ℓ nel codominio (ancora R in questo caso).
La definizione si può quindi estendere a funzioni f : X → Y tra insiemi X e Y dotati di
una distanza, detti spazi metrici.
Prerequisiti dal corso di Algebra lineare: lo spazio R2 .


  Mettiamo in evidenza alcune strutture presenti in R2 , che estenderemo ad insiemi più
  generali

  In R2 possiamo definire:
    1   una struttura algebrica (spazio vettoriale)
    2   una struttura di spazio metrico, in particolare di spazio normato
        (norma di P ∈ R2 ≡ distanza di P da 0 = (0, 0))
    3   un prodotto scalare
    4   una struttura di spazio topologico

  Le stesse strutture si definiscono in modo del tutto simile in Rn , n ≥ 2.
  A tal fine, invece di usare la notazione P = (x, y ) per le coordinate di P ∈ R2 ,
  scriveremo spesso
                          R2 = {P = (x1 , x2 ) | xi ∈ R ∀i = 1, 2 }
  e quindi
                   Rn = {P = (x1 , x2 , . . . , xn ) | xi ∈ R   ∀i = 1, 2, . . . , n }.
Struttura algebrica


   R2 è uno spazio vettoriale di dimensione 2, rispetto alle operazioni di somma e di
   prodotto esterno : se P = (x1 , x2 ), P ′ = (x1′ , x2′ ) ∈ Rn , λ ∈ R, si ha

                      P + P ′ = (x1 + x1′ , x2 + x2′ )         λP = (λx1 , λx2 ) .

   La base canonica di R2 è formata dai vettori                e 1 := (1, 0)   e 2 := (0, 1)
                                           2
                                           X
   In particolare,   P = x1 e 1 + x2 e 2 =   xj e j .
                                                j=1
   R3 è uno spazio vettoriale di dimensione 3 , rispetto alle operazioni di somma e di
   prodotto esterno : se P = (x1 , x2 , x3 ), P ′ = (x1′ , x2′ , x3′ ) ∈ R3 , λ ∈ R, si ha

               P + P ′ = (x1 + x1′ , x2 + x2′ , x3 + x3′ )        λP = (λx1 , λx2 , λx3 ) .

   La base canonica di R3 è formata dai vettori

                        e 1 := (1, 0, 0)   e 2 := (0, 1, 0),       e 3 := (0, 0, 1)
                                                         3
                                                         X
   In particolare,      P = x1 e 1 + x2 e 2 + x3 e 3 =         xj e j .
                                                         j=1
Sia X insime non vuoto con le operazioni di somma ” + ”
(P, Q) ∈ X × X 7→ P + Q ∈ X e prodotto esterno ” · ” λ ∈ R, P ∈ X 7→ λ · P ∈ X .
Diremo che X è uno spazio vettoriale su campo degli scalari R se le operazioni godono
delle seguenti
  1   Associativity of vector addition P + (Q + R) = (P + Q) + R
  2   Commutativity of vector addition P + Q = Q + P
  3   ∃O ∈ X t.c. ∀P ∈ X : P + O = P (O è detto elemento neutro e lo indicheremo
      con 0 e lo diremo lo zero delle spazio vettoriale)
  4   ∀P ∈ X esiste un unico P ′ ∈ X tale che P + P ′ = 0 (P ′ si dice elemento opposto
      di P e lo indicheremo con −P)
  5   Compatibility of scalar multiplication with field multiplication
      α · (β · P) = (αβ) · P
  6   Identity element of scalar multiplication 1 · P = P,
  7   Distributivity of scalar multiplication with respect to vector addition ∀λ ∈ R,
      ∀P, Q ∈ X : λ · (P + Q) = λ · P + λ · Q.
  8   Distributivity of scalar multiplication with respect to field addition
      (α + β) · P = α · P + β · P
Gli elementi di X li diremo vettori .
 Esempio 1. Rn è uno spazio vettoriale di dimensione n , rispetto alle operazioni di
somma e di prodotto esterno : se P = (x1 , x2 , . . . , xn ), P ′ = (x1′ , x2′ , . . . , xn′ ) ∈ Rn , λ ∈ R,
si ha

           P + P ′ = (x1 + x1′ , x2 + x2′ , . . . , xn + xn′ )        λP = (λx1 , λx2 , . . . , λxn ) .

La base canonica di Rn è formata dai vettori

              e 1 := (1, 0, . . . , 0)   e 2 := (0, 1, . . . , 0),   . . . , e n := (0, 0, . . . , 0, 1)
                                                                     n
                                                                     X
In particolare,         P = x1 e 1 + x2 e 2 + · · · + xn e n =             xj e j .
                                                                     j=1
 Esempio 2. X := {P : R → R|P e‘ un polinomio di grado ≤ 100}
E’ uno spazio vettoriale munito della somma tra funzioni e prodotto per uno scalare.
Una base è Pn (x) = x n , n = 0, . . . , 100. Spazio vettoriale di dimensione 101.
 Esempio 3. X := {P : R → R|P e ′ un polinomio}
E’ uno spazio vettoriale munito della somma tra funzioni e prodotto per uno scalare.
Una base è Pn (x) = x n . Spazio vettoriale di dimensione infinita.
 Esempio 4. X = C ([a, b]), l’insime delle funzioni continue è uno spazio vettoriale.
 Esempio 5. X = C k ([a, b]), l’insime delle funzioni continue con le loro derivate fino
all’ordine k.
 Esempio 6. X = C ∞ ([a, b]), l’insime delle funzioni continue con tutte le loro derivate,
 Esempio 7. X = {f :] − 1, 1[→ R| f sviluppabile in serie di Taylor in 0}
 Esempio 8. X = R[a, b] l’insieme delle funzioni integrabili secondo Riemann in [a, b]
• R2 è uno spazio normato: La funzione
                                      p
         ∥ · ∥ : R2 → R , ∥(x, y )∥ := x 2 + y 2 = ”distanza di (x, y ) da (0, 0)”

è una norma su R2 , nel senso che soddisfa alcune proprietà molto generali (vedi dopo) e
definisce anche una distanza in R2 : la distanza Euclidea trap          i vettori
P = (x1 , x2 ), P ′ = (x1′ , x2′ ) ∈ R2 è dE (P, P ′ ) := ∥P − P ′ ∥ = (x1 − x1′ )2 + (x2 − x2′ )2
(Teorema di Pitagora).
Questa ”distanza” gode di alcune proprietà:
D1) d(P, P ′ ) = 0 se e solo se P = P ′ ;
D2) d(P, P ′ ) = d(P ′ P) ;
D3) d(P, Q) ≤ d(P, R) + d(R, Q) per ogni P, Q, R ∈ R2 (disuguaglianza triangolare)
• Rn è uno spazio normato: Analogamente si definisce la norma Euclidea in Rn
                                                           q
              ∥ · ∥ : Rn → R , ∥(x1 , x2 , . . . , xn )∥ := x12 + x22 + · · · + xn2

”distanza di P = (x1 , x2 , . . . , xn ) da 0 = (0, 0, . . . , 0)”
Definiamo la distanza Euclidea tra ip       punti P = (x1 , x2 , . . . , xn ) e P ′ = (x1′ , x2′ , . . . , xn′ ) di
  n              ′                   ′
R come dE (P, P ) := ∥P − P ∥ = (x1 − x1′ )2 + (x2 − x2′ )2 + · · · + (xn − xn′ )2 . Inoltre
valgono le Proprietà D1), D2), D3). (D1, D2 immediate, D3 posticipiamo)
 Osserv. Quando n = 1 la distanza euclidea coincide con la distanza del valore assoluto.
Questa funzione ∥ · ∥ è un caso particolare della nozione generale di norma che daremo in
seguito. Per il momento ci servirà come modello per delle nozioni più generali.
Spazi metrici


Definizione
Sia X un insieme qualsiasi (non vuoto). Una metrica o distanza in X è una funzione
d : X × X → [0, +∞[ soddisfacente le seguenti proprietà:
D1) d(x, y ) = 0 se e solo se x = y ;
D2) d(x, y ) = d(y , x) per ogni x, y ∈ X ; (Simmetrica )
D3) d(x, y ) ≤ d(x, z) + d(z, y ) per ogni x, y , z ∈ X (disuguaglianza triangolare )
La coppia (X , d) si chiama spazio metrico ; X si chiama sostegno dello spazio metrico.

Es.1) Rn con metrica euclidea (per n = 1: metrica del valore assoluto) (La dimostrazione
della dis triangolare per n ≥ 3 la rinviamo)
Es.2) metrica discreta In un insieme qualsiasi X
                                                (
                                                  0 se x = y
                                dDIS (x, y ) :=
                                                  1 se x ̸= y

Dim....
Es.3) In R definiamo d(x, y ) := | arctan(x) − arctan(y )|. Allora d è una metrica.
Dim....
Es.4) Una classe molto importante di esempi di spazi metrici sono gli spazi normati.

Definizione (Norma)
Sia X uno spazio vettoriale. Una norma è una applicazione ∥ · ∥ : X → [0, +∞[ che
verifica
N1) Positività, non degeneratezza: ∥P∥ ≥ 0 e [ ∥P∥ = 0 ⇔ P = 0 ]
N2) Positiva omogeneità: ∥λP∥ = |λ| ∥P∥        ∀λ ∈ R , P ∈ X
N3) Disuguaglianza triangolare: ∥P + P ∥ ≤ ∥P∥ + ∥P ′ ∥.
                                         ′

Uno spazio normato è una coppia (X , ∥ · ∥) formata da uno spazio vettoriale X e da una
norma ∥ · ∥ su X .
 Osservazione. Una norma è definta su uno spazio vettoriale, mentre una distanza solo
su un insieme (quindi senza alcuna struttura algebrica).

Proposizione
Sia (X , ∥ · ∥) spazio normato. La funzione

        d : X × X → [0, ∞[ definita come      d(P, Q) := ∥P − Q∥,       P, Q ∈ X

è una distanza su X . Tale distanza la diremo distanza dedotta dalla norma.
Dim. Dobbiamo dimostrare solo la dis. triangolare delle distanze. Siano P, Q, R ∈ X
                 ∥P − Q∥ = ∥P − R + R − Q∥ ≤ ∥P − R∥ + ∥R − Q∥
Es.5) Sia S uno insieme non vuoto. Sia X = B(S) := {f : S → R| f limitata}
(Esercizi: • X è uno spazio vettoriale;
           • X ha dimensione finita se e solo se S ha un numero finito di punti).
Per ogni f ∈ X = B(S) definiamo ∥f ∥∞ := sup |f (x)| (norma uniforme/ infinito).
                                                x∈S
• ∥ · ∥∞ è una norma. ∥f ∥∞ ≥ 0: ovvia; ∥f ∥∞ = 0 se e solo se f = 0: ovvia.
Dimostriamo la N2). Sia λ ∈ R, f ∈ B(S) e x ∈ S

                    |λf (x)| = |λ| |f (x)| ≤ |λ|supy ∈S |f (y )| = |λ| ∥f ∥∞

passando al supx∈S abbiamo che ∥λf ∥∞ ≤ |λ| ∥f ∥∞ il viceversa in modo analogo.

                      |λ| |f (x)| = |λf (x)| ≤ supy ∈S |λf (y )| = ∥λf ∥∞

passando al supx∈S abbiamo la N2).
Dimostriamo la N3). Siano f , g ∈ B(S) e x ∈ S, abbiamo che

    |f (x) + g (x)| ≤ |f (x)| + |g (x)| ≤ supy ∈S |f (y )| + supy ∈S |g (y )| = ∥f ∥∞ + ∥g ∥∞

essendo vero per ogni x ∈ S, facendo il supx∈S su S otteniamo la N3)

                                 ∥f + g ∥∞ ≤ ∥f ∥∞ + ∥g ∥∞

Quindi (B(S), ∥ · ∥∞ ) è uno spazio normato. La distanza indotta da questa norma, detta
distanza del sup, è
                          d(f , g ) := ∥f − g ∥∞ = sup |f (x) − g (x)|
                                                      x∈S
Es.6) In Rn per P = (x1 , x2 , . . . , xn ) definiamo

                                    ∥P∥∞ := max{|x1 |, |x2 |, . . . , |xn |}

Questa è una norma che si chiama norma del sup o norma infinito.
La distanza indotta sarà tra P = (x1 , x2 , . . . , xn ) e P ′ = (x1′ , x2′ , . . . , xn′ )
dsup (P, P ′ ) := max{|x1 − x1′ |, |x2 − x2′ |, . . . , |xn − xn′ |}.
Es.7) Manhattan metric....
In Rn per P = (x1 , x2 , . . . , xn ) definiamo
                                                                           n
                                                                           X
                               ∥P∥1 := |x1 | + |x2 | + · · · + |xn | =            |xj |
                                                                            j=1

(dimostrate che è una norma) si dice norma-1
La metrica associata per P = (x1 , x2 , . . . , xn ) e P ′ = (x1′ , x2′ , . . . , xn′ ) sarà definita come

                         d1 (P, P ′ ) := |x1 − x1′ | + |x2 − x2′ | + · · · + |xn − xn′ |
Es.8) Su una sfera (che non è uno spazio vettoriale) ....
La distanza geodetica è la lunghezza del cammino più breve sulla sfera che unisce i due
punti ed è sempre maggiore della distanza euclidea.
Ad esempio sulla circonferenza
                                               dgeo (x, y )
                                       y        d2 (x, y )       x




Figura: Visualizzazione della sfera con la distanza euclidea (tratteggiata) e quella geodetica (arco
rosso).

Es.9) Distanza tempo...
Es.10) Sia q > 1. In Rn per P = (x1 , x2 , . . . , xn ) definiamo
                                                                           n
                                                                                             !1/q
                                                              q 1/q
                                 q         q
                                                                           X             q
                  ∥P∥q := |x1 | + |x2 | + · · · + |xn |                =         |xj |
                                                                           j=1

(si dimostra che è una norma) si dice norma-q
Il caso q = 2 è la norma Euclidea.
Es.11) Consideriamo C ([a, b]) lo spazio delle funzioni continue in [a, b] e consideriamo la
funzione                                        Z      b
                               f ∈ C ([a, b]) 7→           |f (t)|dt.
                                                   a

Dimostrare che è una norma. La si indica con ∥f ∥1 o anche ∥f ∥L1
Osservazioni

1) Utilizzando la disuguaglianza triangolare si ottiene facilmente la
”seconda disuguaglianza triangolare”:

                         |d(x, y ) − d(x, z)| ≤ d(y , z), ∀x, y , z ∈ X .

Infatti: fissati x, y , z ∈ X , dalla disuguaglianza triangolare abiamo

                                 d(x, y ) − d(x, z) ≤ d(z, y )
scambiando y e z e tenendo conto della simmetria:

                                 d(x, z) − d(x, y ) ≤ d(z, y )

moltiplichiamo per −1
                               −d(x, z) + d(x, y ) ≥ −d(z, y )
Che messe assieme danno

                   −d(z, y ) ≤ d(x, y ) − d(x, z) ≤ d(z, y )
Osservazioni


 2) Sia (X , d) uno spazio metrico e sia A ⊂ X . Sia d|A la restrizione della metrica d
 all’insieme A × A. Abbiamo che
 • La funzione d|A è una metrica in A, detta metrica indotta in A.
 • La coppia (A, d|A ) è uno spazio metrico, che chiamiamo sottospazio metrico di
 (X , d).
 Spesso, se non ci sono ambiguità, al posto di scrivere d|A scriveremo solo d
 3) Sia (X , ∥ · ∥) uno spazio normato e sia A ⊂ X un sottospazio vettoriale. Sia ∥ · ∥|A
 la restrizione della norma ∥ · ∥ all’insieme A. Abbiamo che
 • La funzione ∥ · ∥|A è una norma in A, detta norma indotta in A.
 • La coppia (A, ∥ · ∥|A ) è uno spazio normato, che chiamiamo sottospazio normato di
 (X , ∥ · ∥).
 Spesso, se non ci sono ambiguità, al posto di scrivere ∥ · ∥|A scriveremo solo ∥ · ∥
Elementi di topologia in uno spazio metrico


Definizione
Sia (X , d) uno spazio metrico. Siano x0 ∈ X e r > 0. L’insieme

                               Br (x0 ) := {x ∈ X | d(x, x0 ) < r }

si chiama intorno sferico (o palla) di centro x0 e raggio r

La definizione è formalmente identica a quella data in R3 .
Esempi:
• in R con la distanza euclidea, la palla di raggio r > 0 di centro x0 è
Br (x0 ) =]x0 − r , x0 + r [.
• in R2 con la distanza euclidea, la palla di raggio r > 0 di centro x0 è
Br (x0 ) = {(x, y )|(x − x0 )2 + (y − y0 )2 < r 2 }, il disco di centro x0 e raggio r > 0
• in R2 con la distanza del sup, la palla di raggio r > 0 di centro x0 è
Br (x0 ) = il quadrato di centro x0 e lato 2r
• in R2 con la distanza della norma-1.....
Definizione
Sia (X , d) uno spazio metrico e sia E ⊂ X . Diremo che E è limitato in X se esiste un
x0 ∈ X e r > 0 tale che E ⊂ Br (x0 ).

Esempio. Una palla è sempre limitata.
Esempio. Un insime finito di punti è sempre limitato.
Esempio. In R3 con la distanza euclidea. R3 non è limitato. R2 visto come sottospazio
vettoriale, non è limitato.
Esempio. In R con la distanza euclidea, l’insime {1/n | n ∈ N} è limitato
Esempio. (Esercizio) In R con la distanza dell’esempio 3),
d(x, y ) := | arctan(x) − arctan(y )|. Qualsiasi insieme è limitato.
Definizione (Convergenza in spazi metrici)
Sia (X , d) uno spazio metrico. Una successione in X è una applicazione N → X

                                      h ∈ N 7→ Ph ∈ X .

che indicheremo con (Ph )h≥0 o (Ph )h o anche (Ph )h∈N .
Sia (Ph )h una successione in uno spazio metrico (X , d) e sia P ∈ X . Si dice che Ph
converge a P nello spazio metrico X e scriveremo Ph → P o anche limh Ph = P, se

                                     lim d(Ph , P) = 0.
                                      h

Diremo che (Ph )h è una successione convergente in X se esiste P ∈ X tale che Ph → P.

Osserviamo che dire che Ph → P equivale a dire che
1) ∀ϵ > 0, d(Ph , P) < ϵ definitivamente
2) ∀ϵ > 0 Ph ∈ Bϵ (P) definitivamente
3) ogni intorno sferico di P contine Ph definitivamente
In particolare se (X , ∥ · ∥) è uno spazio normato allora Ph → P se e solo se

                                     lim ∥Ph − P∥ = 0.
                                      h


 Osservazione. Quando X = R e d(x, y ) = |x − y | questa definizione di successione
convergente coincide con la vecchia definizione.
Proposizione. Una successione non può convergere a due limiti distinti.
Dim. se Ph → Q e Ph → P, allora

                  0 ≤ d(P, Q) ≤ d(P, Ph ) + d(Ph , Q) −→ 0 =⇒ P = Q

 Proposizione. Una successione convergente è limitata.
Dim. come analisi 1
Sia Ph → P0 . Allora in corrsipondenza di B1 (P0 ) si ha che Ph ∈ B1 (P0 ) definitivamente,
ossia esiste ν ∈ N tale che
∀h ≥ ν : Ph ∈ B1 (P0 ). Pertanto, posto
M := max{d(P0 , P1 ), d(P0 , P2 ), . . . , d(P0 , Pν ), 1} + 1, risulta che

                                  ∀h ∈ N : Ph ∈ BM (P0 )
Esempio.

Sia X lo spazio R2 con la norma Euclidea
Sia (Ph )h = (xh , yh )h una successione in R2 , e sia P0 = (x0 , y0 ) ∈ R2 .
Si ha
                       (xh , yh ) → (x0 , y0 ) ⇐⇒ xh → x0         e   yh → y0 ,
Dim. ⇒                               p
                      |xh − x0 | ≤       (xh − x0 )2 + (yh − y0 )2 = ∥Ph − P0 ∥
Poichè ∥Ph − P0 ∥ → 0 abbiamo che xh → x0 . Analogamente yh → 0.
Dim. ⇐. Sappiamo che xh → x0 e yh → y0 ossia in corrispondenza di ϵ > 0 risulta che
|xh − x0 | < ϵ e |yh − y0 | < ϵ definitivamente. Allora

            ∥Ph − P0 ∥2 = (xh − x0 )2 + (yh − y0 )2 ≤ ϵ2 + ϵ2 definitivamente
                  √
Ossia ∥Ph − P0 ∥ ≤ 2ϵ definitivamente.
Enunciato analogo vale in Rn con la norma Euclidea.
xk → x in Rn ossia xk = (xk,1 , xk,2 , . . . , xk,n) ) → x = (x1 , . . . , xn ) con la norma euclidea,
se e solo se, limk xk,i = xi per ogni i = 1, . . . , n. Dimostrarlo!
Stessi enunciati valgono in Rn con una qualsiasi norma ∥ · ∥q con 1 ≤ q ≤ ∞ Dimostrarlo!
Esercizio. Per quali valori di α ∈ R converge la seguente successione
                                               sin(h)
                                       (αh ,          )
                                                  h

Esercizio. Sia (αh )h ⊂ R successione infinitesima mai nulla. Per quali valori di α > 0 la
successione
                                             sin(αh )
                                      (ααh ,          )
                                                αh
è convergente. Disegnare la successione in R2 nel caso (αh )h sia decrescente.
 Osservazione. La nozione di convergenza per una successione dipende dalla metrica.
Ovvero se su un insieme X ci sono 2 metriche da e db può accadere che una successione
converga nella metrica da ma non nella metrica db .
Esempio. In R consideriamo la successione xn = 1/n.
Tale successione nella metrica Euclidea tende a 0: |1/n − 0| → 0.
Se in R consideriamo la metrica discreta dDIS (0, 1/n) = 1 che non è infinitesima.
Quindi, anche in uno spazio vettoriale, in generale, la convergenza dipenderà dalla norma
che consideriamo sullo spazio.

Definizione
Sia X spazio vettoriale. Siano ∥ · ∥a e ∥ · ∥b norme su X . Diremo che ∥ · ∥a e ∥ · ∥b sono
norme equivalenti se esistono α, β > 0 tali che

                            ∀P ∈ X : α∥P∥a ≤ ∥P∥b ≤ β∥P∥a                               (∗)

Osservazione. Dalla (*) segue anche che
                                      1              1
                           ∀P ∈ X :     ∥P∥b ≤ ∥P∥a ≤ ∥P∥b
                                      β              α
Proposizione. Se due norme ∥ · ∥a e ∥ · ∥b sono equivalenti, una successione (Pn )n
converge a P in norma ∥ · ∥a se e solo se converge a P in norma ∥ · ∥b .
Dim. Usando la (*) con Pn − P abbiamo
                        α∥Pn − P∥a ≤ ∥Pn − P∥b ≤ β∥Pn − P∥a
Teorema
In Rn tutte le norme sono equivalenti.

   Dim. Dimostriamo solo che le norme ∥ · ∥q (1 ≤ q ≤ ∞) sono equivalenti tra loro.
   Esercizio!
   Suggerimento. Passo 1. dimostrare che ∥ · ∥1 e ∥ · ∥∞ sono equivalenti.
   Passo 2. dimostrare che ∥ · ∥q e ∥ · ∥∞ sono equivalenti.
   Passo 3. dimostrare che in generale se ∥ · ∥a e ∥ · ∥b sono norme equivalenti e ∥ · ∥b e
   ∥ · ∥c sono norme equivalenti, allora anche ∥ · ∥a e ∥ · ∥c sono norme equivalenti.

In uno spazio infinito dimensionale non tutte le norme sono equivalenti (vedremo un
esempio esplicito).
Elementi di topologia in spazi metrici

Sia (X , d) uno spazio metrico e sia x0 ∈ X . Per ε > 0 l’insieme
                              Bε (x0 ) = {x ∈ X : d(x, x0 ) < ε}
(ossia la palla aperta di centro x0 e raggio ε) è anche detto ε-intorno di x0 .

Definizione (Punti interni - Insieme aperto)
Sia A ⊆ X non vuoto. Un punto x0 ∈ A si dice punto interno ad A se esiste un ε-intorno
di x0 contenuto in A.
L’insieme A è detto aperto se ogni suo punto è punto interno.
Per definizione anche l’insieme vuoto si considera aperto.
Deduciamo che:
 1 Il vuoto e X sono aperti;

 2 Le unioni arbitrarie di aperti sono aperte (dimostrarlo);

 3 Le intersezioni finite di aperti sono aperte (dimostrarlo).

 4 le palle aperte sono aperte.


Nota: Le intersezioni infinite di aperti possono non essere aperte. Ad esempio in R2 ,
                                    \
                                          B1/n (x0 ) = {x0 }
                                  n∈N\{0}

non è aperto.
Definizione (Insiemi chiusi)
Un sottoinsieme C ⊆ X si dice chiuso se il suo complementare è aperto.

Deduciamo che:
  1   Il vuoto e X sono chiusi;
  2   Le intersezioni arbitrarie di chiusi sono chiuse (dimostrarlo);
  3   Le unioni finite di chiusi sono chiuse (dimostrarlo).
  4   Inoltre, le palle chiuse
                                      {x ∈ X : d(x, x0 ) ≤ r }
      sono chiusi.

Nota: Le unioni infinite di chiusi possono non essere chiuse (Esercizio: esibire un
esempio).
Definizione (Intorni)
Sia x0 ∈ X . Un sottoinsieme U ⊆ X si dice intorno di x0 se esiste un aperto A tale che

                                            x0 ∈ A ⊆ U.
Se x0 ∈ X , gli intorni di x0 includono:
  1   Gli ε-intorni;
  2   Ogni aperto contenente x0 ;
  3   Ogni insieme che contiene un intorno di x0 ;
  4   Le intersezioni finite di intorni di x0 .
Indichiamo con U(x0 ) la famiglia di tutti gli intorni di x0 .
Punti aderenti e punti di accumulazione


Definizione
Sia A ⊆ X . Un punto x0 ∈ X si dice:
    Aderente ad A se U ∩ A ̸= ∅ per ogni intorno U di x0 ;
    Di accumulazione per A se U ∩ (A \ {x0 }) ̸= ∅ per ogni intorno U di x0 .
Si denota con Dr (A) l’insieme dei punti di accumulazione di A.
Chiusura, parte interna e frontiera


Definizione
La chiusura di A, denotata A, è definita come
                             \
                        A = {C ⊆ X : C è chiuso e C ⊇ A},

cioè l’insieme dei punti aderenti ad A.

L’interno di A, denotato Å, o int(A) è dato da
                                    [
                              Å := {B ⊆ A : B è aperto},

cioè l’insieme dei punti interni di A.

La frontiera di A è definita da
                                          ∂A := A \ A◦ .


Un sottoinsieme D ⊆ X si dice denso in X se D = X .
Esercizi

Siano A e B sottoinsiemi di uno spazio metrico X (ad esempio X = R2 ). Dimostrare che:
  1   A ∪ B = A ∪ B.
  2   A ∩ B ⊆ A ∩ B (mostrare che l’inclusione può essere stretta).
  3   Se A è aperto allora A◦ = A, e se A è chiuso allora A = A.
  4   (A ∩ B)◦ = A◦ ∩ B ◦ .
  5   A = X \ (X \ A)◦ .
  6   A◦ ⊆ A ⊆ A.
  7   Dimostrare che (Q2 )◦ = ∅ e Q2 = R2 .
  8   Dimostrare che il complementare di Q2 è denso in R2 .
  9   Se A = [0, 1)2 , determinare A◦ , A e ∂A.
 10   Trovare un insieme A ⊆ R2 tale che A◦ , A e ∂A siano tutti distinti.
Esercizi

Sia (X , d) uno spazio metrico e sia A ⊂ X . Sia x0 ∈ X .
Diciamo che x0 è punto esterno a E se è interno a Ac (complementare di A ), cioè se
esiste un intorno sferico di x0 contenuto in Ac ;
Dimostrare che
• punto di frontiera per A se non è né interno né esterno a A, cioè se ogni intorno sferico
di x0 contiene sia punti di A che punti di Ac ;
• chiusura di A = A ∪ Dr (A).
Esercizi Importanti

Naturalmente valgono le medesime osservazioni fatte in R. Per esempio si dimostrino i
seguenti fatti:
• x0 è di accumulazione per A se e solo se esiste una successione (xn )n ⊂ A \ {x0 } tale
che xn → x0
   Dim. x0 di accumulazione, ⇒ per ogni intorno B1/n (x0 ) si ha che
   B1/n (x0 ) ∩ A \ {x0 } ̸= ∅
   Sia xn ∈ B1/n (x0 ) ∩ A \ {x0 }, quindi xn ̸= x0 e d(x0 , xn ) < 1/n.

• x0 ∈ ∂A se e solo se esistono due successioni (xn )n ⊂ A, (yn )n ⊂ Ac tali che xn → x0 e
yn → x0 . (Dim esercizio)
• x0 ∈ Ā se e solo se esiste una successione (xn )n ⊂ A tale che xn → x0
   Dim. ⇒ Se x0 ∈ A basta considerare xn := x0 e quindi d(x0 , xn ) = 0. Se x0 è di
   accumulazione vedi proprietà precedente.
   Dim ⇐ se c’è un xn = x0 allora per ipotesi x0 ∈ A ⊂ Ā.
   Se tutti xn ̸= x0 allora x0 è di accumulazione
• L’insieme dei punti esterni di A coincide con l’interno del complementare;
• A e il suo complementare Ac hanno la stessa frontiera;
• int(A) ⊂ A ⊂ Ā;
• A ∪ ∂A = Ā.
• in generale gli insiemi A, Dr (A), ∂A non sono confrontabili per inclusione;
Esercizi

 Proposizione. Le seguenti proprietà, tra loro equivalenti:
(a) ∀x0 ∈ A, ∃r > 0 tale che Br (x0 ) ⊂ A (A è aperto)
(b) int(A) = A
(c) E ∩ ∂A = ∅
 Proposizione. Le seguenti proprietà, tra loro equivalenti:
(a) Dr (A) ⊂ A
(b) A = Ā
(c) Se (xn )n ⊂ A è una successione convergente, allora limn xn ∈ A.
(d) ∂A ⊂ A
(e) Ac è aperto (A è chiuso)
 Osservazione. Dalle precedenti considerazioni gli insiemi chiusi li possiamo carattrizzare
attraverso le successioni convergenti, quindi anche gli aperti (essendo i complementari dei
chiusi) sono caratterizzabili descrivendo le successioni convergenti. Pertanto in uno
spazio normato il fatto che un insime sia aperto/chiuso dipende dalla norma.

Proposizione. Se due norme ∥ · ∥a e ∥ · ∥b sono equivalenti, allora un insieme è aperto
[chiuso] nella norma ∥ · ∥a se e solo se lo è anche nella norma ∥ · ∥b .
Definizione
Sia X uno spazio vettoriale. Un prodotto scalare su X è una applicazione
< ·, · >: X × X → R, (P, P ′ ) 7→< P · P ′ >= P · P ′ , che verifica le seguenti proprietà.
PS1) Positività e non degeneratezza: P · P ≥ 0 e ( P · P = 0 ⇔ P = 0 )
PS2) Simmetria: P · P ′ = P ′ · P
PS3) Bilinearità: Per ogni λ ∈ R, P, P ′ , Q ∈ X risulta

                   (λP) · P ′ = λ(P · P ′ )             (P + Q) · P ′ = P · P ′ + Q · P ′


Se P, Q ∈ X sono tali che < P, Q >= 0, diremo che P e Q sono ortogonali.
Esempio [Il più semplice esempio di prodotto scalare.] Il prodotto in R può essere visto
anche come un prodotto scalare in R.
Esempio In Rn un prodotto scalare è definito come segue.
Per P = (x1 , x2 , . . . , xn ) e P ′ = (x1′ , x2′ , . . . , xn′ ) dati in Rn , poniamo
                                                                                    n
                                                                                    X
                      < P · P >= P · P := x1 x1′ + x2 x2′ + . . . , xn xn′ =              xi xi′   (1)
                                                                                    i=1

Dimostrate che è un prodotto scalare, ossia valgono le PS1)-PS2)-PS3).
Nota che ∥P∥2 =< P, P > (norma Euclidea su Rn ).
Teorema
Sia X uno spazio vettoriale dotato di prodotto scalare < ·, · >. Allora l’applicazione
                                     p
                             ∥P∥ := < P, P > , P ∈ X

è una norma su X , che diremo norma indotta dal prodotto scalare, ed inoltre
PS4) ∥P + P ′ ∥2 = ∥P∥2 + ∥P ′ ∥2 + 2 < P, P ′ >
PS5) | < P, Q > | ≤ ∥P∥ ∥Q∥ .

 Osservazione. Non tutte le norme derivano da un prodotto scalare. Per le norme ∥ · ∥q
con 1 ≤ q ≤ ∞ e q ̸= 2 non esiste un prodotto scalare che induce tali norme.
 Osservazione. Se P e P ′ sono ortogonali, < P, P ′ >= 0, la PS4) esprime il teorema di
Pitagora.
Dim. Le dimostrazioni delle prime due proprietà della norma:
N1) ∥P∥ ≥ 0 e [ ∥P∥ = 0 ⇔ P = 0 ]
N2) ∥λP∥ = |λ| ∥P∥
sono facili (esercizio);
la PS4) si dimostra per calcolo diretto usando la bilinearità e la simmetria del
prodotto scalare.

∥P + P ′ ∥2 = < P + P ′ , P + P ′ >=< P, P > + < P, P ′ > + < P ′ , P > + < P ′ P ′ >
           =∥P∥2 + 2 < P, P ′ > +∥P ′ ∥2

Verifichiamo la       PS5) | P · Q | ≤ ∥P∥ ∥Q∥.
Osserviamo che per ogni x ∈ R risulta (per N1), PS4), N2), PS3)),

                  0   ≤   ∥xP − Q∥2 = ∥xP∥2 + 2(xP) · (−Q) + ∥Q∥2
                      =   ∥P∥2 x 2 − 2 (P · Q) x + ∥Q∥2                              (2)
                          | {z }       | {z }      | {z }
                            a             b          c

                                   2
Abbiamo dimostrato che:          ax − 2bx + c ≥ 0 ∀x ∈ R            con a, b, c numeri
reali definiti nella (2). Quindi    b 2 − ac ≤ 0  cioè

              (P · Q)2 − ∥P∥2 ∥Q∥2 ≤ 0         ⇒     (P · Q)2 ≤ ∥P∥2 ∥Q∥2

da cui segue subito la PS5).
Rimane da dimostrare l’importantissima disuguaglianza triangolare:
                            N3) ∥P + Q∥ ≤ ∥P∥ + ∥Q∥.
A tal fine usiamo la PS4) e poi la PS5):

                     ∥P + Q∥2     =    ∥P∥2 + ∥Q∥2 + 2P · Q
                                  ≤    ∥P∥2 + ∥Q∥2 + 2|P · Q|
                                  ≤    ∥P∥2 + ∥Q∥2 + 2∥P∥∥Q∥
                                  =    (∥P∥ + ∥Q∥)2

da cui la N3).

 Osservazione. Il precedente risultato dimostra la disuguaglianza triangolare per la
norma euclidea in Rn . Che avevamo lasciato in sospeso.
Per le norme ∥ · ∥q con 1 < q < ∞ e q ̸= 2 abbiamo detto (senza dimostrarlo) che
vale la dis. triangolare.
Esempio Sia X = C ([a, b]) (spazio vettoriale). Possiamo definire l’applicazione
                                                                    Z b
      < ·, · >: C ([a, b]) × C ([a, b]) → R, (f , g ) 7→< f · g >:=     f (x)g (x)dx.
                                                                     a

È un prodotto scalare (dimostrare per esercizio).
La norma indotta è
                                          s
                                             Z b
                                 ∥f ∥2 :=        f 2 (x)dx.
                                               a


Osserviamo che su C ([a, b]) abbiamo definito due norme: ∥f ∥∞ e ∥f ∥2 . Queste due
norme non sono equivalenti (lo vedremo inseguito).
   Ricordiamo che in C ([a, b]) abbiamo definito anche la norma
                                             Z b
                                    ∥f ∥1 :=     |f (x)|dx.
                                               a

   Si può dimostrare che ∥f ∥1 e ∥f ∥∞ non derivano da un prodotto scalare.
Prodotto scalare in R2 e coordinate polari

Qui identifichiamo ogni punto P = (x, y ) ∈ R2 , P ̸= 0 con il segmento orientato
(vettore) che congiunge l’origine con il punto (x, y ) del piano Cartesiano.




Possiamo scrivere P in coordinate polari (r , θ)pol (vedi figura). Risulta
       (                    (     p
         x = r cos θ          r = x 2 + y 2 = ∥P∥ > 0
         y = r sin θ          θ = arctan yx per i punti P nel primo quadrante
Proposizione
Proposizione Siano P = (x, y ) = (r , θ)pol , P ′ = (x ′ , y ′ ) = (r ′ , θ′ )pol allora
< P, P ′ >= rr ′ cos(θ − θ′ )

   Dim. In coordinate cartesiane si ha
   P = (r cos θ, r sin θ) , P ′ = (r ′ cos θ′ , r ′ sin θ′ )       ⇒
   < P · P ′ >= rr ′ (cos θ)(cos θ′ ) + rr ′ (sin θ)(sin θ′ ) = rr ′ (cos θ)(cos θ′ ) + (sin θ)(sin θ′ )
                                                                    

       = rr ′ (cos(θ − θ′ ))

• Siano P, P ′ ∈ Rn e sia π un piano passante per i tre punti P, P ′ , 0 (se non sono
collineari i tre punti P, P ′ , 0 individuano un unico piano), allora detto ϕ l’angolo che
questi due vettori formano in questo piano π, risulta che

                                  < P, P ′ >= ∥P∥2 ∥P ′ ∥2 cos(ϕ)



• Due vettori non nulli di Rn sono ortogonali se formano un angolo retto.
Proposizione
Sia (X , ∥ · ∥) spazio normato. Siano (Pn )n e (Qn )n successioni in X tale che Pn → P e
Qn → Q. Sia λ ∈ R, e (αn )n ⊂ R tale che αn → α in R. Allora

                                         λPn → λP
                                         αn P → αP
                                        αn Pn → αP
                                     Pn + Qn → P + Q
                                        ∥Pn ∥ → ∥P∥

Se la norma è indotta dal prodotto scalare < ·, · >, allora si ha

                                  < Pn , Qn >→< P, Q >

   Dim. Si dimostrano usando la seconda forma della disuguaglianza triangolare. il fatto
   che le successioni convergenti sono limitate e la PS5).
Ricordiamo che data una successione (Ph )h una sua sottosuccessione (Phj )j è una
successione estratta dalla (Ph )h con la legge hj : j ∈ N 7→ hj ∈ N strettamente crescente.
• Se Ph → P allora ogni sua sottosuccessione (Pkj )j converge verso lo stesso limite P.
• Se (Ph )h è convergente allora (Ph )h è limitata (già visto)
Il viceversa non è vero, ma come nel caso reale, in Rn vale il seguente importante

Teorema
Sia (Ph )h ⊂ Rn una successione limitata. Allora esiste una sottosuccessione convergente.

   Dim. Passo 1. n = 1 Analisi 1. Passo 2. n = 2
   Sia Ph = (xh , yh ) una successione limitata in R2, cioè esiste M > 0 tale che ∥Ph ∥ < M,
   il che vuol dire xh2 + yh2 < M 2 ⇒ |xh |, |yh | < M
   cioè le succ.ni di numeri reali (xh )h , (yh )h sono limitate in R.
   Per il passo 1,
   (xh )h ha una sottosuccessione, diciamo (xhj )j , convergente ossia ∃x0 = limj→∞ xhj ∈ R
   Ora consideriamo la successione (yhj )j (che e’ una sottosuccessione di (yh )h ). Tale
   successione è limitata, e per il passo 1 ammette un’estratta convergente diciamo
   (yhj i )i che converge verso un opportuno y0
   Con la stessa legge hj i consideriamo la successione (xhj i )i che è un’estratta da (xhj )j e
   pertanto converge verso x0 .
   Quindi concludendo          Phj i = (xhj i , yhj i )i → (x0 , y0 )
Da RINVIARE

Es.5) (ripresa) Sia S uno insieme non vuoto. Sia X = B(S) := {f : S → R| f limitata}.
Abbiamo visto che (B(S), ∥ · ∥∞ ) è uno spazio normato. Sia (fn )n ⊂ B(S) una
successione, se (fn )n converge a f uniformemente, allora effettivamente f ∈ B(S)
(funzioni limitate che convergono uniformemente lo fanno ad una funzione limitata.)
        (fn )n converge a f uniformemente ⇔ (fn )n converge a f in (B(S), ∥ · ∥∞ )
Se consideriamo Y = C ([a, b]), è un sottospazio di X = B([a, b]) e su C ([a, b]) possiamo
considerare la restrizione della norma ∥ · ∥∞ , ossia (C ([a, b]), ∥ · ∥∞ ) è un sottospazio
normato di (B(S), ∥ · ∥∞ ).
Ricordando che la convergenza uniforme ”conserva” la continuità, abbiamo che data una
successione (fn )n ⊂ C ([a, b]) che converge uniformemente ad f , allora anche
f ∈ C ([a, b]). Questo ci dice che C ([a, b]) è un chiuso di B([a, b]).
Consideriamo Z = C 1 ([a, b]). Z è sottospazio di C e quindi anche di B perciò
(C 1 ([a, b]), ∥ · ∥∞ ) è un sottospazio di C ed anche di B. Ma Z non è chiuso in quanto ci
sono successioni di Z convergenti nella norma (ossia uniformemente), ma la funzione
limite non è in Z :....
Es.5bis) Consideriamo Z = C 1 ([a, b]). Su questo spazio vettoriale consideriamo la
funzione
                                ∥f ∥C 1 := ∥f ∥∞ + ∥f ′ ∥∞
Dimostrate che è una norma.
