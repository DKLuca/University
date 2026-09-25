---
fonte: "An2_2025_pres11_curve_pulito.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Curve

              L.Freddi


           March 21, 2025




L.Freddi                    March 21, 2025   1 / 17
Curve in Rn
Sia [a, b] un intervallo di R con −∞ < a < b < +∞. Sia n ≥ 2.
Definizione
Si chiamano curve in Rn le funzioni continue
                    φ : [a, b]   → Rn
                          t      7 → φ(t) = (φ1 (t), φ2 (t), ..., φn (t))

nel senso che ogni funzione componente φi : [a, b] → R è continua.




         L.Freddi                                                     March 21, 2025   2 / 17
Esempi

Casi particolari importanti sono: n = 2 (curve piane) e n = 3 (curve nello spazio)




         L.Freddi                                              March 21, 2025   3 / 17
Esempi

Casi particolari importanti sono: n = 2 (curve piane) e n = 3 (curve nello spazio)
     φ : [0, 2π] → R2 , φ(t) = (r cos t, r sen t), r > 0, è una curva chiusa e
     semplice. Il sostegno è il cerchio di raggio r e centro l’origine
     φ : [0, 4π] → R2 , φ(t) = (r cos t, r sen t), r > 0, è sempre un cerchio di
     raggio r e centro l’origine, ma percorso due volte, quindi non è semplice
     φ : [0, 2π] → R2 , φ(t) = (2 cos t, 3 sen t), è una curva chiusa e semplice. Il
     sostegno è un’ellisse
     φ : [0, π] → R2 , φ(t) = (2 cos t, 3 sen t), è una curva non chiusa e semplice.
     Il sostegno è un arco di ellisse
     φ : [0, c] → Rn , φ(t) = x0 + tv0 , c > 0, x0 , v0 ∈ Rn , è una curva non chiusa
     se v0 ̸= 0.




         L.Freddi                                                 March 21, 2025    3 / 17
Esempio

Siano r > 0, p > 0. La curva
                   φ(t) = (r cos t, r sen t, pt), t ∈ [a, b], (a < b)




        L.Freddi                                                   March 21, 2025   4 / 17
Esempio

La curva φ(t) = (x(t), y (t)) con
                   (
                     x(t) = r t cos t
                                         ,   t ∈ [0, c], c > 0
                     y (t) = r t sen t




         L.Freddi                                                March 21, 2025   5 / 17
Vettore derivato

Definizione
Data una curva
                    φ:   [a, b] →       Rn

                          t      7→     φ(t) = (φ1 (t), φ2 (t), ..., φn (t)),

con componenti φi derivabili in t0 ∈ [a, b], il vettore

                          φ′ (t0 ) = (φ′1 (t0 ), φ′2 (t0 ), ..., φ′n (t0 ))

si chiama vettore derivato (primo) in t0




         L.Freddi                                                             March 21, 2025   6 / 17
Vettore derivato

Definizione
Data una curva
                    φ:   [a, b] →       Rn

                          t      7→     φ(t) = (φ1 (t), φ2 (t), ..., φn (t)),

con componenti φi derivabili in t0 ∈ [a, b], il vettore

                          φ′ (t0 ) = (φ′1 (t0 ), φ′2 (t0 ), ..., φ′n (t0 ))

si chiama vettore derivato (primo) in t0

Fisicamente, φ′ (t) può essere interpretato come la velocità con cui un punto
materiale percorre la traiettoria φ([a, b]).




         L.Freddi                                                             March 21, 2025   6 / 17
Interpretazione geometrica
Se è non nullo, il vettore derivato φ′ (t0 ) ̸= 0 è tangente alla curva nel punto φ(t0 )


                                                                 f(' t0)                .
                                                                                        f( t1)

                                                                                (t 0)
                                                                              -f
                                                                         t)
                                                                       f( 1

                                                        .f(t0)




          L.Freddi                                                         March 21, 2025        7 / 17
Interpretazione geometrica
Se è non nullo, il vettore derivato φ′ (t0 ) ̸= 0 è tangente alla curva nel punto φ(t0 )
Siano t0 , t1 ∈ [a, b]. Se φ(t0 ) ̸= φ(t1 ),
la retta passante per φ(t0 ) e φ(t1 ) è la
“curva”                                                          f(' t0)                .
                                                                                        f( t1)

                     φ(t1 ) − φ(t0 )                                          -f
                                                                                (t 0)
 t 7→ φ(t0 ) +                       (t − t0 ).                          t)
                        t1 − t0                                        f( 1

                                                        .f(t0)




          L.Freddi                                                         March 21, 2025        7 / 17
Interpretazione geometrica
Se è non nullo, il vettore derivato φ′ (t0 ) ̸= 0 è tangente alla curva nel punto φ(t0 )
Siano t0 , t1 ∈ [a, b]. Se φ(t0 ) ̸= φ(t1 ),
la retta passante per φ(t0 ) e φ(t1 ) è la
“curva”                                                          f(' t0)                .
                                                                                        f( t1)

                     φ(t1 ) − φ(t0 )                                          -f
                                                                                (t 0)
 t 7→ φ(t0 ) +                       (t − t0 ).                          t)
                        t1 − t0                                        f( 1


 Passando al limite per t1 → t0 si ot-
                                                        .f(t0)

tiene
  1   t 7→ φ(t0 ) + φ′ (t0 )(t − t0 )




          L.Freddi                                                         March 21, 2025        7 / 17
Esempio


          φ(t) = (r cos t, r sen t) =⇒ φ′ (t) = (−r sen t, r cos t)

                                             f ( t)



                                                      f( t)




     L.Freddi                                                 March 21, 2025   8 / 17
Curve regolari




      L.Freddi   March 21, 2025   9 / 17
Curve regolari
Definizione
Una curva φ ∈ C 1 ([a, b]; Rn ) si dice regolare se φ′ (t) ̸= 0 per ogni t ∈ (a, b).




          L.Freddi                                                 March 21, 2025      9 / 17
Curve regolari
Definizione
Una curva φ ∈ C 1 ([a, b]; Rn ) si dice regolare se φ′ (t) ̸= 0 per ogni t ∈ (a, b).

Esempio
     le curve costanti φ(t) = x0 per ogni t ∈ [a, b]




          L.Freddi                                                 March 21, 2025      9 / 17
Curve regolari
Definizione
Una curva φ ∈ C 1 ([a, b]; Rn ) si dice regolare se φ′ (t) ̸= 0 per ogni t ∈ (a, b).

Esempio
     le curve costanti φ(t) = x0 per ogni t ∈ [a, b] non sono regolari
     le curve grafico di funzioni f di classe C 1 , cioè φ(t) = (t, f (t)) soddisfano

                            |φ′ (t)| = 1 + |f ′ (t)|2 > 0,    ∀t




          L.Freddi                                                 March 21, 2025      9 / 17
Curve regolari
Definizione
Una curva φ ∈ C 1 ([a, b]; Rn ) si dice regolare se φ′ (t) ̸= 0 per ogni t ∈ (a, b).

Esempio
     le curve costanti φ(t) = x0 per ogni t ∈ [a, b] non sono regolari
     le curve grafico di funzioni f di classe C 1 , cioè φ(t) = (t, f (t)) soddisfano

                             |φ′ (t)| = 1 + |f ′ (t)|2 > 0,   ∀t

      quindi sono regolari




          L.Freddi                                                 March 21, 2025      9 / 17
Esempio

Esempio
L’ellisse φ(t) = (2 cos t, 3 sen t), t ∈ [0, 2π], è una curva regolare.




          L.Freddi                                                  March 21, 2025   10 / 17
Esempio

Esempio
L’ellisse φ(t) = (2 cos t, 3 sen t), t ∈ [0, 2π], è una curva regolare.

Infatti φ ∈ C 1 ([0, 2π]) e si ha
                                  φ′ (t) = (−2 sen t, 3 cos t)
da cui
                     |φ′ |2 = 4 sen2 t + 9 cos2 t ≥ 4 sen2 t + 4 cos2 t = 4




          L.Freddi                                                     March 21, 2025   10 / 17
Esempio

Esempio
L’ellisse φ(t) = (2 cos t, 3 sen t), t ∈ [0, 2π], è una curva regolare.

Infatti φ ∈ C 1 ([0, 2π]) e si ha
                                  φ′ (t) = (−2 sen t, 3 cos t)
da cui
                     |φ′ |2 = 4 sen2 t + 9 cos2 t ≥ 4 sen2 t + 4 cos2 t = 4
Si ha poi
     versore tangente:
                                            (−2 sen t, 3 cos t)
                                    ν(t) = √
                                             4 sen2 t + 9 cos2 t




          L.Freddi                                                     March 21, 2025   10 / 17
Curve di livello
Definizione
Data una funzione f : A ⊆ Rn → R, una curva φ : [a, b] → A è detta una curva di
livello di f se f ◦ φ è costante.




         L.Freddi                                            March 21, 2025   11 / 17
Curve di livello
Definizione
Data una funzione f : A ⊆ Rn → R, una curva φ : [a, b] → A è detta una curva di
livello di f se f ◦ φ è costante.




Allora, se φ è una curva di livello di f , si ha
                               (f ◦ φ)′ = 0 ∀t ∈ (a, b)




          L.Freddi                                           March 21, 2025   11 / 17
Curve di livello
Definizione
Data una funzione f : A ⊆ Rn → R, una curva φ : [a, b] → A è detta una curva di
livello di f se f ◦ φ è costante.




Allora, se φ è una curva di livello di f , si ha
                               (f ◦ φ)′ = 0 ∀t ∈ (a, b)
 Se f ∈ C 1 e φ è regolare, allora
                                      0 = ∇f (φ) · φ′


          L.Freddi                                           March 21, 2025   11 / 17
Equazioni parametriche
Una curva è una funzione continua
                φ : [a, b] → Rn
                       t     7→ φ(t) = (φ1 (t), φ2 (t), ..., φn (t))

     La scrittura             
                              
                                x1 = φ1 (t)
                                 x2 = φ2 (t)
                              
                                             , t ∈ [a, b]
                              
                                ..........
                                 xn = φn (t)
                              
     si dice rappresentazione o equazione parametrica della curva.




         L.Freddi                                                March 21, 2025   12 / 17
Equazioni parametriche
Una curva è una funzione continua
                φ : [a, b] → Rn
                       t     7→ φ(t) = (φ1 (t), φ2 (t), ..., φn (t))

     La scrittura             
                              
                                x1 = φ1 (t)
                                 x2 = φ2 (t)
                              
                                             , t ∈ [a, b]
                              
                                ..........
                                 xn = φn (t)
                              
     si dice rappresentazione o equazione parametrica della curva.
     Ad esempio,
       ▶ se n = 3 e gli assi sono x, y e z le equazioni parametriche sono
                                      
                                      x = φ1 (t)
                                      
                                         y = φ2 (t)
                                      
                                         z = φ3 (t)
                                      



         L.Freddi                                                March 21, 2025   12 / 17
Equazioni parametriche
Esempio
La retta passante per (x0 , y0 ) e direzione v = (v1 , v2 ) ̸= (0, 0) ha equazioni
parametriche                       (
                                      x = x0 + tv1
                                      y = y0 + tv2




          L.Freddi                                                  March 21, 2025   13 / 17
Equazioni parametriche
Esempio
La retta passante per (x0 , y0 ) e direzione v = (v1 , v2 ) ̸= (0, 0) ha equazioni
parametriche                       (
                                      x = x0 + tv1
                                      y = y0 + tv2
Se v1 ̸= 0, ricavando t dalla prima equazione e sostituendo nella seconda, si ha
                                             x − x0
                                  y = y0 +          v2
                                               v1




          L.Freddi                                                  March 21, 2025   13 / 17
Equazioni parametriche
Esempio
La retta passante per (x0 , y0 ) e direzione v = (v1 , v2 ) ̸= (0, 0) ha equazioni
parametriche                       (
                                      x = x0 + tv1
                                      y = y0 + tv2
Se v1 ̸= 0, ricavando t dalla prima equazione e sostituendo nella seconda, si ha
                                             x − x0
                                  y = y0 +          v2
                                               v1
che è l’equazione cartesiana della retta




          L.Freddi                                                  March 21, 2025   13 / 17
Equazioni parametriche
Esempio
La retta passante per (x0 , y0 ) e direzione v = (v1 , v2 ) ̸= (0, 0) ha equazioni
parametriche                       (
                                      x = x0 + tv1
                                      y = y0 + tv2
Se v1 ̸= 0, ricavando t dalla prima equazione e sostituendo nella seconda, si ha
                                             x − x0
                                  y = y0 +          v2
                                               v1
che è l’equazione cartesiana della retta

Esempio
La circonferenza di centro 0 e raggio 1 ha equazioni parametriche
                           (
                             x = cos t
                                         , t ∈ [−π, π]
                             y = sen t
          L.Freddi                                                  March 21, 2025   13 / 17
Equazioni cartesiane
Si può eliminare il parametro elevando al quadrato le due equazioni e sommandole
                                    x2 + y2 = 1
e si ottiene cosı̀ una rappresentazione della curva in funzione delle sole coordinate
cartesiane.




         L.Freddi                                                March 21, 2025   14 / 17
Equazioni cartesiane
Si può eliminare il parametro elevando al quadrato le due equazioni e sommandole
                                    x2 + y2 = 1
e si ottiene cosı̀ una rappresentazione della curva in funzione delle sole coordinate
cartesiane.

     In generale, la scrittura di una curva nella forma
                                       F (x, y ) = 0
     è detta rappresentazione o equazione cartesiana della curva.
     La scrittura di una curva nella forma
                                 y = f (x) o x = f (y )
     cioè come grafico di una funzione rispetto ad uno degli assi cartesiani è un
     caso particolare della precedente in cui le coordinate x e y sono esplicitate,
     ed è quindi detta rappresentazione o equazione cartesiana esplicita



         L.Freddi                                                March 21, 2025   14 / 17
Esempio
Se però consideriamo solo il pezzo sopra, diciamo in un intorno di t0 = π/2, vale
la rappresentazione cartesiana
                                 p
                            y = 1 − x 2 , x ∈ [−1, 1]
mentre in un intorno di t0 = 0 vale la rappresentazione cartesiana
                               p
                           x = 1 − y 2 , y ∈ [−1, 1]
Diremo che la curva ammette delle rappresentazioni cartesiane locali




         L.Freddi                                              March 21, 2025   15 / 17
Esempio
Se però consideriamo solo il pezzo sopra, diciamo in un intorno di t0 = π/2, vale
la rappresentazione cartesiana
                                 p
                            y = 1 − x 2 , x ∈ [−1, 1]
mentre in un intorno di t0 = 0 vale la rappresentazione cartesiana
                               p
                           x = 1 − y 2 , y ∈ [−1, 1]
Diremo che la curva ammette delle rappresentazioni cartesiane locali

Vediamo con un esempio che l’equazione cartesiana può essere utile per disegnare
il sostegno di una curva




         L.Freddi                                              March 21, 2025   15 / 17
Esempio
Cerchiamo di disegnare il sostegno dell’arco di strofoide [dal greco strophos =
nastro]
                     φ(t) = (t 3 − t, t 2 − 1), t ∈ [−2, 2]
Si ha




         L.Freddi                                              March 21, 2025     16 / 17
Esempio
Cerchiamo di disegnare il sostegno dell’arco di strofoide [dal greco strophos =
nastro]
                     φ(t) = (t 3 − t, t 2 − 1), t ∈ [−2, 2]
Si ha
        φ(−2) = (−6, 3), φ(2) = (6, 3), quindi non è chiusa
        φ(0) = (0, −1), φ(−1) = φ(1) = (0, 0), quindi non è semplice




           L.Freddi                                             March 21, 2025    16 / 17
Esempio
Cerchiamo di disegnare il sostegno dell’arco di strofoide [dal greco strophos =
nastro]
                     φ(t) = (t 3 − t, t 2 − 1), t ∈ [−2, 2]
Si ha
        φ(−2) = (−6, 3), φ(2) = (6, 3), quindi non è chiusa
        φ(0) = (0, −1), φ(−1) = φ(1) = (0, 0), quindi non è semplice
Dalle equazioni parametriche
                          (
                           x = t3 − t
                                            ,   t ∈ [−2, 2]
                           y = t2 − 1
cerchiamo di eliminare il parametro t. Dalla seconda equazione si ha
                                      t2 = y + 1




           L.Freddi                                             March 21, 2025    16 / 17
Esempio
Quindi conviene studiare separatamente le due curve
           (                                    (
             x = t3 − t                           x = t3 − t
      φ1 )                 , t ∈ [−2, 0]   φ2 )                  , t ∈ [0, 2]
             y = t2 − 1                           y = t2 − 1
e poi unirle.




          L.Freddi                                             March 21, 2025   17 / 17
Esempio
Quindi conviene studiare separatamente le due curve
             (                                   (
              x = t3 − t                           x = t3 − t
       φ1 )                , t ∈ [−2, 0]   φ 2 )               , t ∈ [0, 2]
              y = t2 − 1                           y = t2 − 1
                                           √
e poi unirle. Cominciamo da φ2 , in cui t = y + 1 e y ∈ [−1, 3].




         L.Freddi                                             March 21, 2025   17 / 17
Esempio
Quindi conviene studiare separatamente le due curve
             (                                   (
              x = t3 − t                           x = t3 − t
       φ1 )                 , t ∈ [−2, 0]  φ 2 )               , t ∈ [0, 2]
              y = t2 − 1                           y = t2 − 1
                                           √
e poi unirle. Cominciamo da φ2 , in cui t = y + 1 e y ∈ [−1, 3]. Sostituendo
nella prima equazione si ha
                                  p
                           x = y y + 1, y ∈ [−1, 3]




        L.Freddi                                            March 21, 2025     17 / 17
Esempio
Quindi conviene studiare separatamente le due curve
             (                                   (
              x = t3 − t                           x = t3 − t
       φ1 )                 , t ∈ [−2, 0]  φ 2 )               , t ∈ [0, 2]
              y = t2 − 1                           y = t2 − 1
                                           √
e poi unirle. Cominciamo da φ2 , in cui t = y + 1 e y ∈ [−1, 3]. Sostituendo
nella prima equazione si ha
                                  p
                           x = y y + 1, y ∈ [−1, 3]
che è la rappresentazione cartesiana della curva e può essere studiata con i
metodi dell’Analisi 1.




         L.Freddi                                               March 21, 2025   17 / 17
Esempio
Quindi conviene studiare separatamente le due curve
             (                                   (
              x = t3 − t                           x = t3 − t
       φ1 )                 , t ∈ [−2, 0]  φ 2 )               , t ∈ [0, 2]
              y = t2 − 1                           y = t2 − 1
                                           √
e poi unirle. Cominciamo da φ2 , in cui t = y + 1 e y ∈ [−1, 3]. Sostituendo
nella prima equazione si ha
                                  p
                           x = y y + 1, y ∈ [−1, 3]
 che è la rappresentazione cartesiana della curva e può essere studiata con i
metodi dell’Analisi
         √          1. Il grafico è come in figura. La curva φ1 , di equazione
x = −y y + 1, y ∈ [−1, 3], è semplicemente ribaltata




         L.Freddi                                                March 21, 2025   17 / 17
