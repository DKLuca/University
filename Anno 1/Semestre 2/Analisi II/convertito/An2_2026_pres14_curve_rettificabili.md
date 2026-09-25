---
fonte: "An2_2026_pres14_curve_rettificabili.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Lunghezza di una curva

                   L.Freddi


                 April 16, 2026




L.Freddi                            April 16, 2026   1 / 11
Lunghezza di una curva
Sia φ : [a, b] → Rn una curva.
Problema: come definirne la lunghezza?




         L.Freddi                        April 16, 2026   2 / 11
Lunghezza di una curva
Sia φ : [a, b] → Rn una curva.
Problema: come definirne la lunghezza?
                                                                       .                   .
Ad ogni partizione di [a, b]                        .        f( t 1
                                                                   )
                                                                       f(t2 )
                                                                                          f(t3)


                                                         -
                                                      t)
 a = t0 < t1 < · · · < tN = b                       f( 2



possiamo associare la curva
                                         . f( t1)


poligonale p di vertici
φ(a), φ(t1 ),. . . , φ(tN ).
                                  .f(t0)




         L.Freddi                                                               April 16, 2026    2 / 11
Lunghezza di una curva
Sia φ : [a, b] → Rn una curva.
Problema: come definirne la lunghezza?
                                                                                  .                   .
Ad ogni partizione di [a, b]                                   .        f( t 1
                                                                              )
                                                                                  f(t2 )
                                                                                                     f(t3)


                                                                    -
                                                                 t)
 a = t0 < t1 < · · · < tN = b                                  f( 2



possiamo associare la curva
                                                  .   f( t1)


poligonale p di vertici
φ(a), φ(t1 ),. . . , φ(tN ).
                                          .   f(t0)


La lunghezza della poligonale è data da
                                        N
                                        X
                               ℓ(p) =         |φ(ti ) − φ(ti−1 )|.
                                        i=1




         L.Freddi                                                                          April 16, 2026    2 / 11
Lunghezza di una curva
Sia φ : [a, b] → Rn una curva.
Problema: come definirne la lunghezza?
                                                                                  .                   .
Ad ogni partizione di [a, b]                                   .        f( t 1
                                                                              )
                                                                                  f(t2 )
                                                                                                     f(t3)


                                                                    -
                                                                 t)
 a = t0 < t1 < · · · < tN = b                                  f( 2



possiamo associare la curva
                                                  .   f( t1)


poligonale p di vertici
φ(a), φ(t1 ),. . . , φ(tN ).
                                          .   f(t0)


La lunghezza della poligonale è data da
                                        N
                                        X
                               ℓ(p) =         |φ(ti ) − φ(ti−1 )|.
                                        i=1

Essa fornisce un’approssimazione per difetto della “lunghezza” (non ancora
definita) della curva φ, che sarà tanto migliore quanto più fine sarà la partizione.

         L.Freddi                                                                          April 16, 2026    2 / 11
Lunghezza di una curva

Definizione
Sia φ : [a, b] → Rn una curva. Si definisce lunghezza di φ l’estremo superiore
della lunghezza delle poligonali associate alla curva,




         L.Freddi                                              April 16, 2026    3 / 11
Lunghezza di una curva

Definizione
Sia φ : [a, b] → Rn una curva. Si definisce lunghezza di φ l’estremo superiore
della lunghezza delle poligonali associate alla curva, cioè, in formule:
                      N
                      X
       ℓ(φ) := sup{         |φ(ti ) − φ(ti−1 )| : a = t0 < t1 < · · · < tN = b}
                      i=1

Se ℓ(φ) < +∞ la curva si dice rettificabile.




         L.Freddi                                                  April 16, 2026   3 / 11
Esempio di curva non rettificabile

La poligonale φ : [0, 1] → R2 che congiunge gli infiniti punti
                     1 1        1 1      1 1         1         1
           (1, 1), ( , − ), ( , ), ( , − ), . . . , ( , (−1)n+1 ), . . .
                     2 2        3 3      4 4         n         n
e φ(0) = 0, è un curva (verificare la continuità)


    1                   .
  1/3
  1/5     ..
  -1/4
         ..1/3 1/2       1


  -1/2              .
         L.Freddi                                               April 16, 2026   4 / 11
Esempio di curva non rettificabile

La poligonale φ : [0, 1] → R2 che congiunge gli infiniti punti
                     1 1        1 1      1 1            1          1
           (1, 1), ( , − ), ( , ), ( , − ), . . . , ( , (−1)n+1 ), . . .
                     2 2        3 3      4 4           n           n
e φ(0) = 0, è un curva (verificare la continuità) di lunghezza infinita.


    1                    .

          ..
                                                            ∞
                                                            X 1
  1/3                                                  ℓ≥              = +∞
                                                            n=1
                                                                  n
  1/5


  -1/4
         ..1/3 1/2       1


  -1/2              .
         L.Freddi                                                     April 16, 2026   4 / 11
Lunghezza delle curve di classe C 1

Teorema (di rettificabilità delle curve C 1 )
Se φ : [a, b] → Rn è una curva di classe C 1 allora φ è rettificabile e la sua
lunghezza è
                                        Z b
                               L(φ) =       |φ′ (t)| dt.
                                          a




         L.Freddi                                                  April 16, 2026   5 / 11
Lunghezza delle curve di classe C 1

Teorema (di rettificabilità delle curve C 1 )
Se φ : [a, b] → Rn è una curva di classe C 1 allora φ è rettificabile e la sua
lunghezza è
                                        Z b
                               L(φ) =       |φ′ (t)| dt.
                                          a

Osserviamo che




         L.Freddi                                                  April 16, 2026   5 / 11
Lunghezza delle curve di classe C 1

Teorema (di rettificabilità delle curve C 1 )
Se φ : [a, b] → Rn è una curva di classe C 1 allora φ è rettificabile e la sua
lunghezza è
                                        Z b
                               L(φ) =       |φ′ (t)| dt.
                                          a

Osserviamo che
     è facile vedere che la formula vale se la curva è un segmento




         L.Freddi                                                  April 16, 2026   5 / 11
Lunghezza delle curve di classe C 1

Teorema (di rettificabilità delle curve C 1 )
Se φ : [a, b] → Rn è una curva di classe C 1 allora φ è rettificabile e la sua
lunghezza è
                                        Z b
                               L(φ) =       |φ′ (t)| dt.
                                          a

Osserviamo che
     è facile vedere che la formula vale se la curva è un segmento
     idea della dimostrazione: suddividere [a, b] in n parti uguali e approssimare
     con la poligonale, applicare la formula ad ogni segmentino e passare al limite
     per n → ∞




         L.Freddi                                                  April 16, 2026   5 / 11
Lunghezza di alcune curve C 1

   (circonferenza unitaria) φ(t) = (cos t, sen t), t ∈ [0, 2π].




       L.Freddi                                                   April 16, 2026   6 / 11
Lunghezza di alcune curve C 1

   (circonferenza unitaria) φ(t) = (cos t, sen t), t ∈ [0, 2π].
   Si ha φ′ (t) = (− sen t, cos t) e dunque |φ′ (t)| = 1, quindi
                                Z 2π               Z 2π
                      L(φ) =         |φ′ (t)| dt =      1 dt = 2π.
                                0                  0




       L.Freddi                                                  April 16, 2026   6 / 11
Lunghezza di alcune curve C 1

   (circonferenza unitaria) φ(t) = (cos t, sen t), t ∈ [0, 2π].
   Si ha φ′ (t) = (− sen t, cos t) e dunque |φ′ (t)| = 1, quindi
                                Z 2π               Z 2π
                      L(φ) =         |φ′ (t)| dt =      1 dt = 2π.
                                0                  0


   (circonferenza unitaria percorsa due volte) φ(t) = (cos t, sen t), t ∈ [0, 4π].




       L.Freddi                                                  April 16, 2026   6 / 11
Lunghezza di alcune curve C 1

   (circonferenza unitaria) φ(t) = (cos t, sen t), t ∈ [0, 2π].
   Si ha φ′ (t) = (− sen t, cos t) e dunque |φ′ (t)| = 1, quindi
                                Z 2π               Z 2π
                      L(φ) =         |φ′ (t)| dt =      1 dt = 2π.
                                0                        0


   (circonferenza unitaria percorsa due volte) φ(t) = (cos t, sen t), t ∈ [0, 4π].
   Si ha                      Z     4π         Z             4π
                      L(φ) =             |φ′ (t)| dt =            1 dt = 4π.
                                0                        0
   La curva ha lo stesso sostegno (immagine) della precedente ma lunghezza
   doppia.




       L.Freddi                                                            April 16, 2026   6 / 11
Lunghezza di alcune curve C 1

   (circonferenza unitaria) φ(t) = (cos t, sen t), t ∈ [0, 2π].
   Si ha φ′ (t) = (− sen t, cos t) e dunque |φ′ (t)| = 1, quindi
                                Z 2π               Z 2π
                      L(φ) =         |φ′ (t)| dt =      1 dt = 2π.
                                 0                        0


   (circonferenza unitaria percorsa due volte) φ(t) = (cos t, sen t), t ∈ [0, 4π].
   Si ha                      Z      4π        Z              4π
                      L(φ) =              |φ′ (t)| dt =            1 dt = 4π.
                                 0                        0
   La curva ha lo stesso sostegno (immagine) della precedente ma lunghezza
   doppia.
   (curva grafico) Sia f ∈ C 1 ([a, b]) e sia φ(t) = (t, f (t)) la curva grafico.




       L.Freddi                                                             April 16, 2026   6 / 11
Lunghezza di alcune curve C 1

   (circonferenza unitaria) φ(t) = (cos t, sen t), t ∈ [0, 2π].
   Si ha φ′ (t) = (− sen t, cos t) e dunque |φ′ (t)| = 1, quindi
                                Z 2π               Z 2π
                      L(φ) =         |φ′ (t)| dt =      1 dt = 2π.
                                0                        0


   (circonferenza unitaria percorsa due volte) φ(t) = (cos t, sen t), t ∈ [0, 4π].
   Si ha                      Z     4π         Z             4π
                      L(φ) =             |φ′ (t)| dt =            1 dt = 4π.
                                0                        0
   La curva ha lo stesso sostegno (immagine) della precedente ma lunghezza
   doppia.
   (curva grafico) Sia f ∈ C 1 ([a, b]) e sia φ(t) = (t, f (t)) la curva grafico. Si
   ha                                 Z bp
                           L(φ) =            1 + |f ′ (t)|2 dt
                                           a


       L.Freddi                                                            April 16, 2026   6 / 11
Esercizio (per casa)
Sia φ(t) = (rt cos t, rt sen t), t ∈ [0, 2π] (spirale di Archimede). Dimostrare che
                           r      p                       p          
                 ℓ(φ) = 2π 1 + 4π 2 + log(2π + 1 + 4π 2 )
                           2

Esercizio (per casa)
Studiare la regolarità, disegnare il sostegno e calcolare la lunghezza della curva
                                                 2
φ(t) = (t3 , t2 ), t ∈ [−1, 1]. Risulta: L(φ) = 27 (133/2 − 8).




         L.Freddi                                                 April 16, 2026      7 / 11
Esercizio (per casa)
Sia φ(t) = (rt cos t, rt sen t), t ∈ [0, 2π] (spirale di Archimede). Dimostrare che
                           r      p                       p          
                 ℓ(φ) = 2π 1 + 4π 2 + log(2π + 1 + 4π 2 )
                           2

Esercizio (per casa)
Studiare la regolarità, disegnare il sostegno e calcolare la lunghezza della curva
                                                 2
φ(t) = (t3 , t2 ), t ∈ [−1, 1]. Risulta: L(φ) = 27 (133/2 − 8).

Si ha
                                  φ′ (t) = (3t2 , 2t)
e φ′ (t) = 0 ⇐⇒ t = 0. Dunque φ(0) è un punto singolare. Per disegnarla è
utile cercare di scriverne l’equazione cartesiana eliminando il parametro t dalle
equazioni parametriche. Posto x = t3 e y = t2 si può ricavare t dalla prima
equazione t = x1/3 e sostituirlo nella seconda ottenendo
                                      y = x2/3 .
Il grafico di questa funzione ha una cuspide in corrispondenza ad x = 0.


         L.Freddi                                                 April 16, 2026      7 / 11
Curve equivalenti
Le curve
    φ(t) = (cos t, sen t), t ∈ [0, 2π]
    ψ(s) = (cos 2s, sen 2s), s ∈ [0, π]




           L.Freddi                       April 16, 2026   8 / 11
Curve equivalenti
Le curve
    φ(t) = (cos t, sen t), t ∈ [0, 2π]
    ψ(s) = (cos 2s, sen 2s), s ∈ [0, π]
    hanno lo stesso sostegno e sono semplici,




           L.Freddi                             April 16, 2026   8 / 11
Curve equivalenti
Le curve
    φ(t) = (cos t, sen t), t ∈ [0, 2π]
    ψ(s) = (cos 2s, sen 2s), s ∈ [0, π]
    hanno lo stesso sostegno e sono semplici,
    hanno la stessa lunghezza ma la seconda è percorsa con velocità doppia,
    infatti
                          |φ′ (t)| = 1 mentre |ψ ′ (s)| = 2




           L.Freddi                                           April 16, 2026    8 / 11
Curve equivalenti
Le curve
    φ(t) = (cos t, sen t), t ∈ [0, 2π]
    ψ(s) = (cos 2s, sen 2s), s ∈ [0, π]
    hanno lo stesso sostegno e sono semplici,
    hanno la stessa lunghezza ma la seconda è percorsa con velocità doppia,
    infatti
                          |φ′ (t)| = 1 mentre |ψ ′ (s)| = 2
    le due curve differiscono solo per il cambiamento di parametro
                                     t = 2s =: g(s);




           L.Freddi                                           April 16, 2026    8 / 11
Curve equivalenti
Le curve
    φ(t) = (cos t, sen t), t ∈ [0, 2π]
    ψ(s) = (cos 2s, sen 2s), s ∈ [0, π]
    hanno lo stesso sostegno e sono semplici,
    hanno la stessa lunghezza ma la seconda è percorsa con velocità doppia,
    infatti
                          |φ′ (t)| = 1 mentre |ψ ′ (s)| = 2
    le due curve differiscono solo per il cambiamento di parametro
                                     t = 2s =: g(s);
    si ha infatti ψ(s) = φ(2s), s ∈ [0, π],




           L.Freddi                                           April 16, 2026    8 / 11
Curve equivalenti
Le curve
    φ(t) = (cos t, sen t), t ∈ [0, 2π]
    ψ(s) = (cos 2s, sen 2s), s ∈ [0, π]
    hanno lo stesso sostegno e sono semplici,
    hanno la stessa lunghezza ma la seconda è percorsa con velocità doppia,
    infatti
                          |φ′ (t)| = 1 mentre |ψ ′ (s)| = 2
    le due curve differiscono solo per il cambiamento di parametro
                                     t = 2s =: g(s);
    si ha infatti ψ(s) = φ(2s), s ∈ [0, π], ovvero ψ = φ ◦ g
                                             φ
                                   [0, 2π] - Rn
                                     g 6       ψ
                                              

                                         [0, π]

           L.Freddi                                            April 16, 2026   8 / 11
Curve equivalenti
Definizione
Due curve φ : [a, b] → Rn , ψ : [c, d] → Rn si dicono equivalenti, e si scrive
φ ∼ ψ, se esiste una funzione biiettiva g : [c, d] → [a, b], continua e strettamente
crescente, tale che ψ = φ ◦ g

                                               φ-
                                      [a, b]      Rn
                                      g 6      ψ

                                      [c, d]




         L.Freddi                                                April 16, 2026   9 / 11
Curve equivalenti
Definizione
Due curve φ : [a, b] → Rn , ψ : [c, d] → Rn si dicono equivalenti, e si scrive
φ ∼ ψ, se esiste una funzione biiettiva g : [c, d] → [a, b], continua e strettamente
crescente, tale che ψ = φ ◦ g

                                                 φ-
                                        [a, b]      Rn
                                 g −1 ?
                                      g 6        ψ

                                        [c, d]
Nelle ipotesi della definizione si ha
     g −1 : [a, b] → [c, d] è continua, crescente, e tale che φ = ψ ◦ g −1 ;




         L.Freddi                                                   April 16, 2026   9 / 11
Curve equivalenti
Definizione
Due curve φ : [a, b] → Rn , ψ : [c, d] → Rn si dicono equivalenti, e si scrive
φ ∼ ψ, se esiste una funzione biiettiva g : [c, d] → [a, b], continua e strettamente
crescente, tale che ψ = φ ◦ g

                                                 φ-
                                        [a, b]      Rn
                                 g −1 ?
                                      g 6        ψ

                                        [c, d]
Nelle ipotesi della definizione si ha
     g −1 : [a, b] → [c, d] è continua, crescente, e tale che φ = ψ ◦ g −1 ;
     g e g −1 si possono scambiare tra di loro;




         L.Freddi                                                   April 16, 2026   9 / 11
Curve equivalenti
Definizione
Due curve φ : [a, b] → Rn , ψ : [c, d] → Rn si dicono equivalenti, e si scrive
φ ∼ ψ, se esiste una funzione biiettiva g : [c, d] → [a, b], continua e strettamente
crescente, tale che ψ = φ ◦ g

                                                 φ-
                                        [a, b]      Rn
                                 g −1 ?
                                      g 6        ψ

                                        [c, d]
Nelle ipotesi della definizione si ha
     g −1 : [a, b] → [c, d] è continua, crescente, e tale che φ = ψ ◦ g −1 ;
     g e g −1 si possono scambiare tra di loro; nel senso che si può scrivere la
     definizione precendente sostituendo g con g −1 e scambiando i ruoli di φ e ψ;




         L.Freddi                                                   April 16, 2026   9 / 11
Curve equivalenti
Definizione
Due curve φ : [a, b] → Rn , ψ : [c, d] → Rn si dicono equivalenti, e si scrive
φ ∼ ψ, se esiste una funzione biiettiva g : [c, d] → [a, b], continua e strettamente
crescente, tale che ψ = φ ◦ g

                                                 φ-
                                        [a, b]      Rn
                                 g −1 ?
                                      g 6        ψ

                                        [c, d]
Nelle ipotesi della definizione si ha
     g −1 : [a, b] → [c, d] è continua, crescente, e tale che φ = ψ ◦ g −1 ;
     g e g −1 si possono scambiare tra di loro; nel senso che si può scrivere la
     definizione precendente sostituendo g con g −1 e scambiando i ruoli di φ e ψ;
     l’equivalenza di curve è una relazione di equivalenza (riflessiva, simmetrica e
     transitiva).

         L.Freddi                                                   April 16, 2026   9 / 11
Cammini e parametrizzazioni
Data una curva φ, l’insieme
                    γ = [φ] := {ψ : ψ è una curva equivalente a φ}
è detto un cammino. Ogni funzione ψ ∈ γ (quelle che fino ad ora sono state
chiamate curve) è detta una rappresentazione parametrica o parametrizzazione
del cammino γ.




         L.Freddi                                               April 16, 2026   10 / 11
Cammini e parametrizzazioni
Data una curva φ, l’insieme
                    γ = [φ] := {ψ : ψ è una curva equivalente a φ}
è detto un cammino. Ogni funzione ψ ∈ γ (quelle che fino ad ora sono state
chiamate curve) è detta una rappresentazione parametrica o parametrizzazione
del cammino γ.

È facile vedere che, se φ ∼ ψ, cioè φ e ψ sono parametrizzazioni dello stesso
cammino, allora
     hanno gli stessi estremi e in particolare:
                                φ è chiusa ⇐⇒ ψ è chiusa




         L.Freddi                                               April 16, 2026    10 / 11
Cammini e parametrizzazioni
Data una curva φ, l’insieme
                    γ = [φ] := {ψ : ψ è una curva equivalente a φ}
è detto un cammino. Ogni funzione ψ ∈ γ (quelle che fino ad ora sono state
chiamate curve) è detta una rappresentazione parametrica o parametrizzazione
del cammino γ.

È facile vedere che, se φ ∼ ψ, cioè φ e ψ sono parametrizzazioni dello stesso
cammino, allora
     hanno gli stessi estremi e in particolare:
                                φ è chiusa ⇐⇒ ψ è chiusa
     sono percorse nello stesso verso




         L.Freddi                                               April 16, 2026    10 / 11
Cammini e parametrizzazioni
Data una curva φ, l’insieme
                    γ = [φ] := {ψ : ψ è una curva equivalente a φ}
è detto un cammino. Ogni funzione ψ ∈ γ (quelle che fino ad ora sono state
chiamate curve) è detta una rappresentazione parametrica o parametrizzazione
del cammino γ.

È facile vedere che, se φ ∼ ψ, cioè φ e ψ sono parametrizzazioni dello stesso
cammino, allora
     hanno gli stessi estremi e in particolare:
                                φ è chiusa ⇐⇒ ψ è chiusa
     sono percorse nello stesso verso
     hanno lo stesso sostegno




         L.Freddi                                               April 16, 2026    10 / 11
Cammini e parametrizzazioni
Data una curva φ, l’insieme
                    γ = [φ] := {ψ : ψ è una curva equivalente a φ}
è detto un cammino. Ogni funzione ψ ∈ γ (quelle che fino ad ora sono state
chiamate curve) è detta una rappresentazione parametrica o parametrizzazione
del cammino γ.

È facile vedere che, se φ ∼ ψ, cioè φ e ψ sono parametrizzazioni dello stesso
cammino, allora
     hanno gli stessi estremi e in particolare:
                                φ è chiusa ⇐⇒ ψ è chiusa
     sono percorse nello stesso verso
     hanno lo stesso sostegno
     hanno la stessa lunghezza




         L.Freddi                                               April 16, 2026    10 / 11
Cammini e parametrizzazioni
Data una curva φ, l’insieme
                    γ = [φ] := {ψ : ψ è una curva equivalente a φ}
è detto un cammino. Ogni funzione ψ ∈ γ (quelle che fino ad ora sono state
chiamate curve) è detta una rappresentazione parametrica o parametrizzazione
del cammino γ.

È facile vedere che, se φ ∼ ψ, cioè φ e ψ sono parametrizzazioni dello stesso
cammino, allora
     hanno gli stessi estremi e in particolare:
                                φ è chiusa ⇐⇒ ψ è chiusa
     sono percorse nello stesso verso
     hanno lo stesso sostegno
     hanno la stessa lunghezza
Osserviamo che due circonferenze percorse un numero diverso di volte non hanno
la stessa lunghezza, quindi non sono equivalenti e non rappresentano lo stesso
cammino
         L.Freddi                                               April 16, 2026    10 / 11
Cammini e parametrizzazioni

L’osservazione giustifica la seguente terminologia. Sia γ un cammino e φ ∈ γ
  1   primo estremo di γ := primo estremo di φ
  2   secondo estremo di γ := secondo estremo di φ
  3   γ si dice chiuso : ⇐⇒ φ è chiusa
  4   ℓ(γ) := ℓ(φ)




         L.Freddi                                            April 16, 2026    11 / 11
Cammini e parametrizzazioni

L’osservazione giustifica la seguente terminologia. Sia γ un cammino e φ ∈ γ
  1   primo estremo di γ := primo estremo di φ
  2   secondo estremo di γ := secondo estremo di φ
  3   γ si dice chiuso : ⇐⇒ φ è chiusa
  4   ℓ(γ) := ℓ(φ)

Intuitivamente, un cammino (o curva orientata) può essere pensato come il
sostegno di una curva in cui
      è fissato un verso di percorrenza
      è fissato il numero di volte in cui il sostegno viene percorso




          L.Freddi                                                 April 16, 2026   11 / 11
