---
fonte: "An2_2026_pres09_max_min.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Problemi di massimo e minimo
                 (ottimizzazione)

                      L.Freddi


                    April 7, 2026




L.Freddi                             April 7, 2026   1 / 36
Punti di massimo e minimo locale
Sia f : D → R, D insieme non vuoto di Rn (non necessariamente aperto). Diamo
alcune definizioni che estendono quelle già date in Analisi 1 per le funzioni di una
sola variabile.
Definizione
Un punto x0 ∈ D si dice
   - di minimo locale o relativo per f se esiste un intorno U di x0 tale che

                              f (x0 ) ≤ f (x) ∀ x ∈ U ∩ D;

   - di massimo locale o relativo per f se esiste un intorno U di x0 tale che

                              f (x0 ) ≥ f (x) ∀ x ∈ U ∩ D.




         L.Freddi                                                April 7, 2026    2 / 36
Punti di massimo e minimo locale
Sia f : D → R, D insieme non vuoto di Rn (non necessariamente aperto). Diamo
alcune definizioni che estendono quelle già date in Analisi 1 per le funzioni di una
sola variabile.
Definizione
Un punto x0 ∈ D si dice
   - di minimo locale o relativo per f se esiste un intorno U di x0 tale che

                              f (x0 ) ≤ f (x) ∀ x ∈ U ∩ D;

   - di massimo locale o relativo per f se esiste un intorno U di x0 tale che

                              f (x0 ) ≥ f (x) ∀ x ∈ U ∩ D.

Definizione
                    ◦
Un punto x0 ∈D è detto critico o stazionario



         L.Freddi                                                April 7, 2026    2 / 36
Punti di massimo e minimo locale
Sia f : D → R, D insieme non vuoto di Rn (non necessariamente aperto). Diamo
alcune definizioni che estendono quelle già date in Analisi 1 per le funzioni di una
sola variabile.
Definizione
Un punto x0 ∈ D si dice
   - di minimo locale o relativo per f se esiste un intorno U di x0 tale che

                              f (x0 ) ≤ f (x) ∀ x ∈ U ∩ D;

   - di massimo locale o relativo per f se esiste un intorno U di x0 tale che

                              f (x0 ) ≥ f (x) ∀ x ∈ U ∩ D.

Definizione
                    ◦
Un punto x0 ∈D è detto critico o stazionario se f è derivabile parzialmente in x0
e ∇f (x0 ) = 0.

         L.Freddi                                                April 7, 2026    2 / 36
Ricerca di massimi e minimi locali
Teorema (dei punti critici)
         ◦
Sia x0 ∈D un punto di massimo o minimo locale per f . Se f è derivabile
parzialmente in x0 allora ∇f (x0 ) = 0 (cioè x0 è un punto critico o stazionario).




         L.Freddi                                                 April 7, 2026    3 / 36
Ricerca di massimi e minimi locali
Teorema (dei punti critici)
         ◦
Sia x0 ∈D un punto di massimo o minimo locale per f . Se f è derivabile
parzialmente in x0 allora ∇f (x0 ) = 0 (cioè x0 è un punto critico o stazionario).

Dimostrazione Supponiamo, per fissare le idee, che x0 sia di minimo locale.




         L.Freddi                                                 April 7, 2026    3 / 36
Ricerca di massimi e minimi locali
Teorema (dei punti critici)
         ◦
Sia x0 ∈D un punto di massimo o minimo locale per f . Se f è derivabile
parzialmente in x0 allora ∇f (x0 ) = 0 (cioè x0 è un punto critico o stazionario).

Dimostrazione Supponiamo, per fissare le idee, che x0 sia di minimo locale.




         L.Freddi                                                 April 7, 2026    3 / 36
Ricerca di massimi e minimi locali
Teorema (dei punti critici)
         ◦
Sia x0 ∈D un punto di massimo o minimo locale per f . Se f è derivabile
parzialmente in x0 allora ∇f (x0 ) = 0 (cioè x0 è un punto critico o stazionario).

Dimostrazione Supponiamo, per fissare le idee, che x0 sia di minimo locale.
Consideriamo La funzione di una variabile
                                F (t) := f (x0 + tei )
definita in un intorno di t = 0 (poiché x0 è interno a D).




         L.Freddi                                                 April 7, 2026    3 / 36
Ricerca di massimi e minimi locali
Teorema (dei punti critici)
         ◦
Sia x0 ∈D un punto di massimo o minimo locale per f . Se f è derivabile
parzialmente in x0 allora ∇f (x0 ) = 0 (cioè x0 è un punto critico o stazionario).

Dimostrazione Supponiamo, per fissare le idee, che x0 sia di minimo locale.
Consideriamo La funzione di una variabile
                                F (t) := f (x0 + tei )
definita in un intorno di t = 0 (poiché x0 è interno a D).
     F ha in 0 un minimo locale




         L.Freddi                                                 April 7, 2026    3 / 36
Ricerca di massimi e minimi locali
Teorema (dei punti critici)
         ◦
Sia x0 ∈D un punto di massimo o minimo locale per f . Se f è derivabile
parzialmente in x0 allora ∇f (x0 ) = 0 (cioè x0 è un punto critico o stazionario).

Dimostrazione Supponiamo, per fissare le idee, che x0 sia di minimo locale.
Consideriamo La funzione di una variabile
                                F (t) := f (x0 + tei )
definita in un intorno di t = 0 (poiché x0 è interno a D).
     F ha in 0 un minimo locale
     Per il teorema dei punti critici in una variabile, si ha F ′ (0) = 0.




         L.Freddi                                                   April 7, 2026   3 / 36
Ricerca di massimi e minimi locali
Teorema (dei punti critici)
         ◦
Sia x0 ∈D un punto di massimo o minimo locale per f . Se f è derivabile
parzialmente in x0 allora ∇f (x0 ) = 0 (cioè x0 è un punto critico o stazionario).

Dimostrazione Supponiamo, per fissare le idee, che x0 sia di minimo locale.
Consideriamo La funzione di una variabile
                                F (t) := f (x0 + tei )
definita in un intorno di t = 0 (poiché x0 è interno a D).
     F ha in 0 un minimo locale
     Per il teorema dei punti critici in una variabile, si ha F ′ (0) = 0.
                             ∂f
     D’altra parte F ′ (0) =     (x0 ),
                             ∂xi




         L.Freddi                                                   April 7, 2026   3 / 36
Ricerca di massimi e minimi locali
Teorema (dei punti critici)
         ◦
Sia x0 ∈D un punto di massimo o minimo locale per f . Se f è derivabile
parzialmente in x0 allora ∇f (x0 ) = 0 (cioè x0 è un punto critico o stazionario).

Dimostrazione Supponiamo, per fissare le idee, che x0 sia di minimo locale.
Consideriamo La funzione di una variabile
                                F (t) := f (x0 + tei )
definita in un intorno di t = 0 (poiché x0 è interno a D).
     F ha in 0 un minimo locale
     Per il teorema dei punti critici in una variabile, si ha F ′ (0) = 0.
                             ∂f                  ∂f
     D’altra parte F ′ (0) =     (x0 ), e quindi     (x0 ) = 0.
                             ∂xi                 ∂xi




         L.Freddi                                                   April 7, 2026   3 / 36
Ricerca di massimi e minimi locali
Teorema (dei punti critici)
         ◦
Sia x0 ∈D un punto di massimo o minimo locale per f . Se f è derivabile
parzialmente in x0 allora ∇f (x0 ) = 0 (cioè x0 è un punto critico o stazionario).

Dimostrazione Supponiamo, per fissare le idee, che x0 sia di minimo locale.
Consideriamo La funzione di una variabile
                                 F (t) := f (x0 + tei )
definita in un intorno di t = 0 (poiché x0 è interno a D).
     F ha in 0 un minimo locale
     Per il teorema dei punti critici in una variabile, si ha F ′ (0) = 0.
                              ∂f                      ∂f
     D’altra parte F ′ (0) =       (x0 ), e quindi       (x0 ) = 0.
                              ∂xi                    ∂xi
Poiché ciò vale per ogni i = 1, . . . , n, allora ∇f (x0 ) = 0.



         L.Freddi                                                   April 7, 2026   3 / 36
Ricerca di massimi e minimi locali
Eventuali punti di massimo o minimo locale per f vanno ricercati
     tra i punti stazionari interni al dominio (teorema dei punti critici)
     sulla frontiera del dominio
Inoltre




          L.Freddi                                                April 7, 2026   4 / 36
Ricerca di massimi e minimi locali
Eventuali punti di massimo o minimo locale per f vanno ricercati
     tra i punti stazionari interni al dominio (teorema dei punti critici)
     sulla frontiera del dominio
Inoltre
     i punti cosı̀ trovati soddisfano solo una condizione necessaria per essere di
     massimo o minimo locale




          L.Freddi                                                April 7, 2026      4 / 36
Ricerca di massimi e minimi locali
Eventuali punti di massimo o minimo locale per f vanno ricercati
     tra i punti stazionari interni al dominio (teorema dei punti critici)
     sulla frontiera del dominio
Inoltre
     i punti cosı̀ trovati soddisfano solo una condizione necessaria per essere di
     massimo o minimo locale
     se si è interessati a trovare punti di massimo o minimo assoluti allora basta
     confrontare tra di loro i valori assunti dalla funzione in tali punti




          L.Freddi                                                April 7, 2026      4 / 36
Ricerca di massimi e minimi locali
Eventuali punti di massimo o minimo locale per f vanno ricercati
     tra i punti stazionari interni al dominio (teorema dei punti critici)
     sulla frontiera del dominio
Inoltre
     i punti cosı̀ trovati soddisfano solo una condizione necessaria per essere di
     massimo o minimo locale
     se si è interessati a trovare punti di massimo o minimo assoluti allora basta
     confrontare tra di loro i valori assunti dalla funzione in tali punti
     se invece si vuole stabilire se essi siano di massimo o minimo locale allora si
     potrà procedere in due modi




          L.Freddi                                                April 7, 2026      4 / 36
Ricerca di massimi e minimi locali
Eventuali punti di massimo o minimo locale per f vanno ricercati
     tra i punti stazionari interni al dominio (teorema dei punti critici)
     sulla frontiera del dominio
Inoltre
     i punti cosı̀ trovati soddisfano solo una condizione necessaria per essere di
     massimo o minimo locale
     se si è interessati a trovare punti di massimo o minimo assoluti allora basta
     confrontare tra di loro i valori assunti dalla funzione in tali punti
     se invece si vuole stabilire se essi siano di massimo o minimo locale allora si
     potrà procedere in due modi
        1 studiare il comportamento locale della funzione in un intorno del punto

           (caso per caso → esercizi)
        2 servirsi di condizioni sufficienti di ottimalità (o estremalità) (cioè

           massimalità o minimalità) basate sulle derivate seconde che, nel caso di
           più variabili, costituiscono una matrice quadrata.


          L.Freddi                                                April 7, 2026      4 / 36
Forma quadratica associata a una matrice
Data una matrice quadrata H di dimensione n × n, si dice forma quadratica (o
bilineare) associata ad H la funzione
                                  q(x) = ⟨Hx, x⟩
dove ⟨·, ·⟩ denota il prodotto scalare in Rn e Hx è il prodotto righe per colonne.




         L.Freddi                                                April 7, 2026   5 / 36
Forma quadratica associata a una matrice
Data una matrice quadrata H di dimensione n × n, si dice forma quadratica (o
bilineare) associata ad H la funzione
                                  q(x) = ⟨Hx, x⟩
dove ⟨·, ·⟩ denota il prodotto scalare in Rn e Hx è il prodotto righe per colonne.
In componenti
                                         Xn
                                q(x) =       Hij xi xj
                                       i,j=1




         L.Freddi                                                April 7, 2026   5 / 36
Forma quadratica associata a una matrice
Data una matrice quadrata H di dimensione n × n, si dice forma quadratica (o
bilineare) associata ad H la funzione
                                  q(x) = ⟨Hx, x⟩
dove ⟨·, ·⟩ denota il prodotto scalare in Rn e Hx è il prodotto righe per colonne.
In componenti
                                         Xn
                                q(x) =       Hij xi xj
                                       i,j=1

Ad esempio, se                                    
                                           a   b
                                 H=
                                           c   d
si ha
                         q(x, y) = ax2 + (b + c)xy + dy 2




         L.Freddi                                                April 7, 2026   5 / 36
Matrici definite e semidefinite
Ricordiamo, dall’Algebra Lineare, che una matrice quadrata H (o la forma
quadratica associata) si dice
     definita positiva se il suo minimo autovalore è strettamente positivo.
     Equivalentemente, esiste m > 0 tale che
                                 ⟨Hx, x⟩ ≥ m|x|2 ∀ x                             (1)




         L.Freddi                                                April 7, 2026   6 / 36
Matrici definite e semidefinite
Ricordiamo, dall’Algebra Lineare, che una matrice quadrata H (o la forma
quadratica associata) si dice
     definita positiva se il suo minimo autovalore è strettamente positivo.
     Equivalentemente, esiste m > 0 tale che
                                 ⟨Hx, x⟩ ≥ m|x|2 ∀ x                             (1)
     definita negativa se il suo massimo autovalore è strettamente negativo.
     Equivalentemente, esiste M < 0 tale che
                                 ⟨Hx, x⟩ ≤ M |x|2 ∀ x




         L.Freddi                                                April 7, 2026   6 / 36
Matrici definite e semidefinite
Ricordiamo, dall’Algebra Lineare, che una matrice quadrata H (o la forma
quadratica associata) si dice
     definita positiva se il suo minimo autovalore è strettamente positivo.
     Equivalentemente, esiste m > 0 tale che
                                 ⟨Hx, x⟩ ≥ m|x|2 ∀ x                             (1)
     definita negativa se il suo massimo autovalore è strettamente negativo.
     Equivalentemente, esiste M < 0 tale che
                                 ⟨Hx, x⟩ ≤ M |x|2 ∀ x
     semidefinita positiva se
                                       ⟨Hx, x⟩ ≥ 0 ∀ x
     (gli autovalori sono tutti ≥ 0)




         L.Freddi                                                April 7, 2026   6 / 36
Matrici definite e semidefinite
Ricordiamo, dall’Algebra Lineare, che una matrice quadrata H (o la forma
quadratica associata) si dice
     definita positiva se il suo minimo autovalore è strettamente positivo.
     Equivalentemente, esiste m > 0 tale che
                                 ⟨Hx, x⟩ ≥ m|x|2 ∀ x                             (1)
     definita negativa se il suo massimo autovalore è strettamente negativo.
     Equivalentemente, esiste M < 0 tale che
                                 ⟨Hx, x⟩ ≤ M |x|2 ∀ x
     semidefinita positiva se
                                       ⟨Hx, x⟩ ≥ 0 ∀ x
     (gli autovalori sono tutti ≥ 0)
     semidefinita negativa se
                                       ⟨Hx, x⟩ ≤ 0 ∀ x
     (gli autovalori sono tutti ≤ 0)


         L.Freddi                                                April 7, 2026   6 / 36
Esempi
Ad esempio
                 
       H1 = 10 01 ,     q1 (x, y) = x2 + y 2
                 
     H2 = −1 0
                0
               −1   ,   q2 (x, y) = −x2 − y 2
                 
       H3 = 10 00 ,     q3 (x, y) = x2
                 
      H4 = 00 −1
               0
                    ,   q4 (x, y) = −y 2
                 
      H5 = 10 −1
               0
                    ,   q5 (x, y) = x2 − y 2




       L.Freddi                                 April 7, 2026   7 / 36
Esempi
Ad esempio
                 
       H1 = 10 01 ,     q1 (x, y) = x2 + y 2 è definita positiva
                 
     H2 = −1 0
                0
               −1   ,   q2 (x, y) = −x2 − y 2
                 
       H3 = 10 00 ,     q3 (x, y) = x2
                 
      H4 = 00 −1
               0
                    ,   q4 (x, y) = −y 2
                 
      H5 = 10 −1
               0
                    ,   q5 (x, y) = x2 − y 2




       L.Freddi                                       April 7, 2026   7 / 36
Esempi
Ad esempio
                 
       H1 = 10 01 ,     q1 (x, y) = x2 + y 2 è definita positiva
                 
     H2 = −1 0
                0
               −1   ,   q2 (x, y) = −x2 − y 2 è definita negativa
                 
       H3 = 10 00 ,     q3 (x, y) = x2
                 
      H4 = 00 −1
               0
                    ,   q4 (x, y) = −y 2
                 
      H5 = 10 −1
               0
                    ,   q5 (x, y) = x2 − y 2




       L.Freddi                                       April 7, 2026   7 / 36
Esempi
Ad esempio
                 
       H1 = 10 01 ,     q1 (x, y) = x2 + y 2 è definita positiva
                 
     H2 = −1 0
                0
               −1   ,   q2 (x, y) = −x2 − y 2 è definita negativa
                 
       H3 = 10 00 ,     q3 (x, y) = x2 è semidefinita positiva
                 
      H4 = 00 −1
               0
                    ,   q4 (x, y) = −y 2
                 
      H5 = 10 −1
               0
                    ,   q5 (x, y) = x2 − y 2




       L.Freddi                                       April 7, 2026   7 / 36
Esempi
Ad esempio
                 
       H1 = 10 01 ,     q1 (x, y) = x2 + y 2 è definita positiva
                 
     H2 = −1 0
                0
               −1   ,   q2 (x, y) = −x2 − y 2 è definita negativa
                 
       H3 = 10 00 ,     q3 (x, y) = x2 è semidefinita positiva
                 
      H4 = 00 −1
               0
                    ,   q4 (x, y) = −y 2 è semidefinita negativa
                 
      H5 = 10 −1
               0
                    ,   q5 (x, y) = x2 − y 2




       L.Freddi                                       April 7, 2026   7 / 36
Esempi
Ad esempio
                 
       H1 = 10 01 ,     q1 (x, y) = x2 + y 2 è definita positiva
                 
     H2 = −1 0
                0
               −1   ,   q2 (x, y) = −x2 − y 2 è definita negativa
                 
       H3 = 10 00 ,     q3 (x, y) = x2 è semidefinita positiva
                 
      H4 = 00 −1
               0
                    ,   q4 (x, y) = −y 2 è semidefinita negativa
                 
      H5 = 10 −1
               0
                    ,   q5 (x, y) = x2 − y 2 non è semidefinita




       L.Freddi                                       April 7, 2026   7 / 36
Esempi
Ad esempio
                 
       H1 = 10 01 ,             q1 (x, y) = x2 + y 2 è definita positiva
                 
     H2 = −1 0
                0
               −1   ,           q2 (x, y) = −x2 − y 2 è definita negativa
                 
       H3 = 10 00 ,             q3 (x, y) = x2 è semidefinita positiva
                 
      H4 = 00 −1
               0
                    ,           q4 (x, y) = −y 2 è semidefinita negativa
                 
      H5 = 10 −1
               0
                    ,           q5 (x, y) = x2 − y 2 non è semidefinita


    La forma quadratica associata alla matrice
                                              
                                  H = a0 0b

    è q(x, y) = ax2 + by 2 .



        L.Freddi                                              April 7, 2026   7 / 36
Esempi
Ad esempio
                 
       H1 = 10 01 ,                q1 (x, y) = x2 + y 2 è definita positiva
                 
     H2 = −1 0
                0
               −1   ,              q2 (x, y) = −x2 − y 2 è definita negativa
                 
       H3 = 10 00 ,                q3 (x, y) = x2 è semidefinita positiva
                 
      H4 = 00 −1
               0
                    ,              q4 (x, y) = −y 2 è semidefinita negativa
                 
      H5 = 10 −1
               0
                    ,              q5 (x, y) = x2 − y 2 non è semidefinita


    La forma quadratica associata alla matrice
                                              
                                  H = a0 0b

    è q(x, y) = ax2 + by 2 .
    Se b ≥ a > 0 allora q è definita positiva e si ha
                                 q(x, y) ≥ a(x2 + y 2 )
        L.Freddi                                                 April 7, 2026   7 / 36
Criterio della matrice hessiana
Teorema
Sia D ⊆ Rn , f ∈ C 2 (D), e sia x0 un punto critico di f interno a D.
  1   se x0 è di minimo (risp. massimo) locale allora ∇2 f (x0 ) è semidefinita
      positiva (risp. negativa);
  2   se ∇2 f (x0 ) è definita positiva (risp. negativa) allora x0 è di minimo (risp.
      massimo) locale.




          L.Freddi                                                   April 7, 2026        8 / 36
Criterio della matrice hessiana
Teorema
Sia D ⊆ Rn , f ∈ C 2 (D), e sia x0 un punto critico di f interno a D.
  1   se x0 è di minimo (risp. massimo) locale allora ∇2 f (x0 ) è semidefinita
      positiva (risp. negativa);
  2   se ∇2 f (x0 ) è definita positiva (risp. negativa) allora x0 è di minimo (risp.
      massimo) locale.

Osserviamo che




          L.Freddi                                                   April 7, 2026        8 / 36
Criterio della matrice hessiana
Teorema
Sia D ⊆ Rn , f ∈ C 2 (D), e sia x0 un punto critico di f interno a D.
  1   se x0 è di minimo (risp. massimo) locale allora ∇2 f (x0 ) è semidefinita
      positiva (risp. negativa);
  2   se ∇2 f (x0 ) è definita positiva (risp. negativa) allora x0 è di minimo (risp.
      massimo) locale.

Osserviamo che
      il criterio fornisce condizioni necessarie e condizioni sufficienti affinchè un
      punto sia di massimo o di minimo locale




          L.Freddi                                                   April 7, 2026        8 / 36
Criterio della matrice hessiana
Teorema
Sia D ⊆ Rn , f ∈ C 2 (D), e sia x0 un punto critico di f interno a D.
  1   se x0 è di minimo (risp. massimo) locale allora ∇2 f (x0 ) è semidefinita
      positiva (risp. negativa);
  2   se ∇2 f (x0 ) è definita positiva (risp. negativa) allora x0 è di minimo (risp.
      massimo) locale.

Osserviamo che
      il criterio fornisce condizioni necessarie e condizioni sufficienti affinchè un
      punto sia di massimo o di minimo locale
      esercizio: si dimostri, con opportuni esempi, che nessuna delle condizioni del
      teorema è sia necessaria che sufficiente (basta farlo nel caso di una sola
      variabile 1)




          L.Freddi                                                   April 7, 2026        8 / 36
Criterio della matrice hessiana
Teorema
Sia D ⊆ Rn , f ∈ C 2 (D), e sia x0 un punto critico di f interno a D.
  1   se x0 è di minimo (risp. massimo) locale allora ∇2 f (x0 ) è semidefinita
      positiva (risp. negativa);
  2   se ∇2 f (x0 ) è definita positiva (risp. negativa) allora x0 è di minimo (risp.
      massimo) locale.

Dimostrazione 1 Supponiamo che x0 sia di minimo, la dimostrazione
nell’altro caso essendo analoga.




          L.Freddi                                                   April 7, 2026        9 / 36
Criterio della matrice hessiana
Teorema
Sia D ⊆ Rn , f ∈ C 2 (D), e sia x0 un punto critico di f interno a D.
  1   se x0 è di minimo (risp. massimo) locale allora ∇2 f (x0 ) è semidefinita
      positiva (risp. negativa);
  2   se ∇2 f (x0 ) è definita positiva (risp. negativa) allora x0 è di minimo (risp.
      massimo) locale.

Dimostrazione 1 Supponiamo che x0 sia di minimo, la dimostrazione
nell’altro caso essendo analoga. Poiché ∇f (x0 ) = 0, la formula di Taylor di
centro x0 di f , di ordine 2 si riduce a
                             1
            f (x) = f (x0 ) + ⟨∇2 f (x0 )(x − x0 ), (x − x0 )⟩ + R2 (x, x0 ).  (2)
                             2




          L.Freddi                                                   April 7, 2026        9 / 36
Criterio della matrice hessiana
Teorema
Sia D ⊆ Rn , f ∈ C 2 (D), e sia x0 un punto critico di f interno a D.
  1   se x0 è di minimo (risp. massimo) locale allora ∇2 f (x0 ) è semidefinita
      positiva (risp. negativa);
  2   se ∇2 f (x0 ) è definita positiva (risp. negativa) allora x0 è di minimo (risp.
      massimo) locale.

Dimostrazione 1 Supponiamo che x0 sia di minimo, la dimostrazione
nell’altro caso essendo analoga. Poiché ∇f (x0 ) = 0, la formula di Taylor di
centro x0 di f , di ordine 2 si riduce a
                             1
            f (x) = f (x0 ) + ⟨∇2 f (x0 )(x − x0 ), (x − x0 )⟩ + R2 (x, x0 ).  (2)
                             2
 Sia v ∈ Rn . Ponendo x = x0 + tv, t ∈ R, si ha
                                     1
            f (x0 + tv) = f (x0 ) + t2 ⟨∇2 f (x0 )v, v⟩ + R2 (x0 + tv, x0 ),
                                     2


          L.Freddi                                                   April 7, 2026        9 / 36
Criterio della matrice hessiana
Teorema
Sia D ⊆ Rn , f ∈ C 2 (D), e sia x0 un punto critico di f interno a D.
  1   se x0 è di minimo (risp. massimo) locale allora ∇2 f (x0 ) è semidefinita
      positiva (risp. negativa);
  2   se ∇2 f (x0 ) è definita positiva (risp. negativa) allora x0 è di minimo (risp.
      massimo) locale.

Dimostrazione 1 Supponiamo che x0 sia di minimo, la dimostrazione
nell’altro caso essendo analoga. Poiché ∇f (x0 ) = 0, la formula di Taylor di
centro x0 di f , di ordine 2 si riduce a
                              1
             f (x) = f (x0 ) + ⟨∇2 f (x0 )(x − x0 ), (x − x0 )⟩ + R2 (x, x0 ). (2)
                              2
 Sia v ∈ Rn . Ponendo x = x0 + tv, t ∈ R, si ha
                                     1
             f (x0 + tv) = f (x0 ) + t2 ⟨∇2 f (x0 )v, v⟩ + R2 (x0 + tv, x0 ),
                                     2
                      2
 cioè, ricavando ⟨∇ f (x0 )v, v⟩,
          L.Freddi                                                   April 7, 2026        9 / 36
Criterio della matrice hessiana
Teorema
Sia D ⊆ Rn , f ∈ C 2 (D), e sia x0 un punto critico di f interno a D.
  1   se x0 è di minimo (risp. massimo) locale allora ∇2 f (x0 ) è semidefinita
      positiva (risp. negativa);
  2   se ∇2 f (x0 ) è definita positiva (risp. negativa) allora x0 è di minimo (risp.
      massimo) locale.

                                   f (x0 + tv) − f (x0 )    R2 (x0 + tv, x0 )
            ⟨∇2 f (x0 )v, v⟩ = 2                         −2                   .        (3)
                                            t2                     t2




          L.Freddi                                                     April 7, 2026   10 / 36
Criterio della matrice hessiana
Teorema
Sia D ⊆ Rn , f ∈ C 2 (D), e sia x0 un punto critico di f interno a D.
  1   se x0 è di minimo (risp. massimo) locale allora ∇2 f (x0 ) è semidefinita
      positiva (risp. negativa);
  2   se ∇2 f (x0 ) è definita positiva (risp. negativa) allora x0 è di minimo (risp.
      massimo) locale.

                               f (x0 + tv) − f (x0 )    R2 (x0 + tv, x0 )
            ⟨∇2 f (x0 )v, v⟩ = 2                     −2                   .       (3)
                                         t2                    t2
Poiché x0 è di minimo locale, allora per t abbastanza piccolo, diciamo |t| < δ, si
ha
                                f (x0 + tv) ≥ f (x0 ).




          L.Freddi                                                   April 7, 2026    10 / 36
Criterio della matrice hessiana
Teorema
Sia D ⊆ Rn , f ∈ C 2 (D), e sia x0 un punto critico di f interno a D.
  1   se x0 è di minimo (risp. massimo) locale allora ∇2 f (x0 ) è semidefinita
      positiva (risp. negativa);
  2   se ∇2 f (x0 ) è definita positiva (risp. negativa) allora x0 è di minimo (risp.
      massimo) locale.

                               f (x0 + tv) − f (x0 )    R2 (x0 + tv, x0 )
            ⟨∇2 f (x0 )v, v⟩ = 2                     −2                   .       (3)
                                         t2                    t2
Poiché x0 è di minimo locale, allora per t abbastanza piccolo, diciamo |t| < δ, si
ha
                                f (x0 + tv) ≥ f (x0 ).
Allora il primo termine a secondo membro della (3) è ≥ 0, sicchè
                                           R2 (x0 + tv, x0 )
                      ⟨∇2 f (x0 )v, v⟩ ≥ −2
                                                  t2
e la tesi si ottiene passando al limite per t → 0
          L.Freddi                                                   April 7, 2026    10 / 36
Criterio della matrice hessiana
Teorema
Sia D ⊆ Rn , f ∈ C 2 (D), e sia x0 un punto critico di f interno a D.
  1   se x0 è di minimo (risp. massimo) locale allora ∇2 f (x0 ) è semidefinita
      positiva (risp. negativa);
  2   se ∇2 f (x0 ) è definita positiva (risp. negativa) allora x0 è di minimo (risp.
      massimo) locale.

                               f (x0 + tv) − f (x0 )    R2 (x0 + tv, x0 )
            ⟨∇2 f (x0 )v, v⟩ = 2                     −2                   .       (3)
                                         t2                    t2
Poiché x0 è di minimo locale, allora per t abbastanza piccolo, diciamo |t| < δ, si
ha
                                f (x0 + tv) ≥ f (x0 ).
Allora il primo termine a secondo membro della (3) è ≥ 0, sicchè
                                           R2 (x0 + tv, x0 )
                      ⟨∇2 f (x0 )v, v⟩ ≥ −2                  →0
                                                  t2
e la tesi si ottiene passando al limite per t → 0
          L.Freddi                                                   April 7, 2026    10 / 36
Criterio della matrice hessiana
Teorema
Sia D ⊆ Rn , f ∈ C 2 (D), e sia x0 un punto critico di f interno a D.
  1   se x0 è di minimo (risp. massimo) locale allora ∇2 f (x0 ) è semidefinita
      positiva (risp. negativa);
  2   se ∇2 f (x0 ) è definita positiva (risp. negativa) allora x0 è di minimo (risp.
      massimo) locale.
 2 Supponiamo che ∇2 f (x0 ) sia definita positiva, la dimostrazione nell’altro caso

essendo analoga.




          L.Freddi                                                   April 7, 2026    11 / 36
Criterio della matrice hessiana
Teorema
Sia D ⊆ Rn , f ∈ C 2 (D), e sia x0 un punto critico di f interno a D.
  1   se x0 è di minimo (risp. massimo) locale allora ∇2 f (x0 ) è semidefinita
      positiva (risp. negativa);
  2   se ∇2 f (x0 ) è definita positiva (risp. negativa) allora x0 è di minimo (risp.
      massimo) locale.
 2 Supponiamo che ∇2 f (x0 ) sia definita positiva, la dimostrazione nell’altro caso

essendo analoga. Dalla formula di Taylor di centro x0 e ordine 2 si ha
                           1
          f (x) − f (x0 ) = ⟨∇2 f (x0 )(x − x0 ), (x − x0 )⟩ + R2 (x, x0 )
                           2




          L.Freddi                                                   April 7, 2026    11 / 36
Criterio della matrice hessiana
Teorema
Sia D ⊆ Rn , f ∈ C 2 (D), e sia x0 un punto critico di f interno a D.
  1   se x0 è di minimo (risp. massimo) locale allora ∇2 f (x0 ) è semidefinita
      positiva (risp. negativa);
  2   se ∇2 f (x0 ) è definita positiva (risp. negativa) allora x0 è di minimo (risp.
      massimo) locale.
 2 Supponiamo che ∇2 f (x0 ) sia definita positiva, la dimostrazione nell’altro caso

essendo analoga. Dalla formula di Taylor di centro x0 e ordine 2 si ha
                              1
           f (x) − f (x0 ) = ⟨∇2 f (x0 )(x − x0 ), (x − x0 )⟩ + R2 (x, x0 )
                              2
 e, detto m il più piccolo autovalore di ∇2 f (x0 ), si ha
                                       m
                      f (x) − f (x0 ) ≥ |x − x0 |2 + R2 (x, x0 ).
                                        2



          L.Freddi                                                   April 7, 2026    11 / 36
Criterio della matrice hessiana
Teorema
Sia D ⊆ Rn , f ∈ C 2 (D), e sia x0 un punto critico di f interno a D.
  1   se x0 è di minimo (risp. massimo) locale allora ∇2 f (x0 ) è semidefinita
      positiva (risp. negativa);
  2   se ∇2 f (x0 ) è definita positiva (risp. negativa) allora x0 è di minimo (risp.
      massimo) locale.
 2 Supponiamo che ∇2 f (x0 ) sia definita positiva, la dimostrazione nell’altro caso

essendo analoga. Dalla formula di Taylor di centro x0 e ordine 2 si ha
                              1
           f (x) − f (x0 ) = ⟨∇2 f (x0 )(x − x0 ), (x − x0 )⟩ + R2 (x, x0 )
                              2
 e, detto m il più piccolo autovalore di ∇2 f (x0 ), si ha
                                       m
                      f (x) − f (x0 ) ≥ |x − x0 |2 + R2 (x, x0 ).
Essendo                                 2
                                       R2 (x, x0 )
                                   lim             =0
                                  x→x0 |x − x0 |2

          L.Freddi                                                   April 7, 2026    11 / 36
Criterio della matrice hessiana
Teorema
Sia D ⊆ Rn , f ∈ C 2 (D), e sia x0 un punto critico di f interno a D.
  1   se x0 è di minimo (risp. massimo) locale allora ∇2 f (x0 ) è semidefinita
      positiva (risp. negativa);
  2   se ∇2 f (x0 ) è definita positiva (risp. negativa) allora x0 è di minimo (risp.
      massimo) locale.

esiste un intorno U di x0 tale che
                           |R2 (x, x0 )|   m
                                     2
                                         ≤       ∀x ∈ U ∩ D
                            |x − x0 |      2
per cui
                           f (x) − f (x0 ) ≥ 0   ∀x ∈ U ∩ D
cioè x0 è di minimo locale.




          L.Freddi                                                   April 7, 2026    12 / 36
Esempi
Consideriamo la funzione definita su R2 da
                               f (x, y) = x2 + y 2
Si ha che




         L.Freddi                                    April 7, 2026   13 / 36
Esempi
Consideriamo la funzione definita su R2 da
                                 f (x, y) = x2 + y 2
Si ha che
     (0, 0) è l’unico punto stazionario




         L.Freddi                                      April 7, 2026   13 / 36
Esempi
Consideriamo la funzione definita su R2 da
                                 f (x, y) = x2 + y 2
Si ha che
     (0, 0) è l’unico punto stazionario
     ∇2 f (0, 0) = 2I (I = matrice unità 2 × 2) che è definita positiva




         L.Freddi                                                 April 7, 2026   13 / 36
Esempi
Consideriamo la funzione definita su R2 da
                                 f (x, y) = x2 + y 2
Si ha che
     (0, 0) è l’unico punto stazionario
     ∇2 f (0, 0) = 2I (I = matrice unità 2 × 2) che è definita positiva
     quindi (0, 0) è di minimo locale




         L.Freddi                                                 April 7, 2026   13 / 36
Esempi
Consideriamo la funzione definita su R2 da
                                 f (x, y) = x2 + y 2
Si ha che
     (0, 0) è l’unico punto stazionario
     ∇2 f (0, 0) = 2I (I = matrice unità 2 × 2) che è definita positiva
     quindi (0, 0) è di minimo locale
     (0, 0) è di minimo assoluto perché f (0, 0) = 0 e f (x, y) > 0 ∀(x, y) ̸= 0




         L.Freddi                                                  April 7, 2026     13 / 36
Esempi
Consideriamo la funzione definita su R2 da
                                 f (x, y) = x2 + y 2
Si ha che
     (0, 0) è l’unico punto stazionario
     ∇2 f (0, 0) = 2I (I = matrice unità 2 × 2) che è definita positiva
     quindi (0, 0) è di minimo locale
     (0, 0) è di minimo assoluto perché f (0, 0) = 0 e f (x, y) > 0 ∀(x, y) ̸= 0
Il grafico è contenuto nel semispazio delle z ≥ 0. Per disegnarlo osserviamo che




         L.Freddi                                                  April 7, 2026     13 / 36
Esempi
Consideriamo la funzione definita su R2 da
                                 f (x, y) = x2 + y 2
Si ha che
     (0, 0) è l’unico punto stazionario
     ∇2 f (0, 0) = 2I (I = matrice unità 2 × 2) che è definita positiva
     quindi (0, 0) è di minimo locale
     (0, 0) è di minimo assoluto perché f (0, 0) = 0 e f (x, y) > 0 ∀(x, y) ̸= 0
Il grafico è contenuto nel semispazio delle z ≥ 0. Per disegnarlo osserviamo che
     le intersezioni con i piani paralleli al piano xy (di equazione z = 0), cioè i
     piani z = c, sono




         L.Freddi                                                  April 7, 2026     13 / 36
Esempi
Consideriamo la funzione definita su R2 da
                                 f (x, y) = x2 + y 2
Si ha che
     (0, 0) è l’unico punto stazionario
     ∇2 f (0, 0) = 2I (I = matrice unità 2 × 2) che è definita positiva
     quindi (0, 0) è di minimo locale
     (0, 0) è di minimo assoluto perché f (0, 0) = 0 e f (x, y) > 0 ∀(x, y) ̸= 0
Il grafico è contenuto nel semispazio delle z ≥ 0. Per disegnarlo osserviamo che
     le intersezioni con i piani paralleli al piano xy (di equazione z = 0), cioè i
     piani z = c, sono
        ▶ insiemi vuoti se c < 0,




         L.Freddi                                                  April 7, 2026     13 / 36
Esempi
Consideriamo la funzione definita su R2 da
                                 f (x, y) = x2 + y 2
Si ha che
     (0, 0) è l’unico punto stazionario
     ∇2 f (0, 0) = 2I (I = matrice unità 2 × 2) che è definita positiva
     quindi (0, 0) è di minimo locale
     (0, 0) è di minimo assoluto perché f (0, 0) = 0 e f (x, y) > 0 ∀(x, y) ̸= 0
Il grafico è contenuto nel semispazio delle z ≥ 0. Per disegnarlo osserviamo che
     le intersezioni con i piani paralleli al piano xy (di equazione z = 0), cioè i
     piani z = c, sono
        ▶ insiemi vuoti se c < 0,
        ▶ il solo punto (0, 0) se c = 0




         L.Freddi                                                  April 7, 2026     13 / 36
Esempi
Consideriamo la funzione definita su R2 da
                                 f (x, y) = x2 + y 2
Si ha che
     (0, 0) è l’unico punto stazionario
     ∇2 f (0, 0) = 2I (I = matrice unità 2 × 2) che è definita positiva
     quindi (0, 0) è di minimo locale
     (0, 0) è di minimo assoluto perché f (0, 0) = 0 e f (x, y) > 0 ∀(x, y) ̸= 0
Il grafico è contenuto nel semispazio delle z ≥ 0. Per disegnarlo osserviamo che
     le intersezioni con i piani paralleli al piano xy (di equazione z = 0), cioè i
     piani z = c, sono
        ▶ insiemi vuoti se c < 0,
        ▶ il solo punto (0, 0) se c = 0
                                    √
        ▶ circonferenze di raggio     c se c > 0 (di equazione x2 + y 2 = c).



         L.Freddi                                                  April 7, 2026     13 / 36
Esempi
Consideriamo la funzione definita su R2 da
                                 f (x, y) = x2 + y 2
Si ha che
     (0, 0) è l’unico punto stazionario
     ∇2 f (0, 0) = 2I (I = matrice unità 2 × 2) che è definita positiva
     quindi (0, 0) è di minimo locale
     (0, 0) è di minimo assoluto perché f (0, 0) = 0 e f (x, y) > 0 ∀(x, y) ̸= 0
Il grafico è contenuto nel semispazio delle z ≥ 0. Per disegnarlo osserviamo che
     le intersezioni con i piani paralleli al piano xy (di equazione z = 0), cioè i
     piani z = c, sono
        ▶ insiemi vuoti se c < 0,
        ▶ il solo punto (0, 0) se c = 0
                                    √
        ▶ circonferenze di raggio     c se c > 0 (di equazione x2 + y 2 = c).
     le intersezioni con i piani x = 0 e y = 0 sono parabole di equazione
     rispettivamente z = y 2 e z = x2 .
         L.Freddi                                                  April 7, 2026     13 / 36
Esempi
Con queste informazioni si può fare un disegno approssimativo del grafico che
rappresenta una superficie nello spazio detta paraboloide (circolare).




Se a > 0 e b > 0, f (x, y) = ax2 + by 2 è un paraboloide ellittico.
         L.Freddi                                                 April 7, 2026   14 / 36
Esempi
Consideriamo la funzione definita su R2 da
                               f (x, y) = x2 − y 2
Si ha che




         L.Freddi                                    April 7, 2026   15 / 36
Esempi
Consideriamo la funzione definita su R2 da
                                 f (x, y) = x2 − y 2
Si ha che
     (0, 0) è l’unico punto stazionario




         L.Freddi                                      April 7, 2026   15 / 36
Esempi
Consideriamo la funzione definita su R2 da
                                 f (x, y) = x2 − y 2
Si ha che
     (0, 0) è l’unico punto stazionario
     la matrice hessiana in (0, 0) è
                                                           
                                ∇2 f (0, 0) = 2 10     0
                                                       −1

     che non è semidefinita




         L.Freddi                                               April 7, 2026   15 / 36
Esempi
Consideriamo la funzione definita su R2 da
                                 f (x, y) = x2 − y 2
Si ha che
     (0, 0) è l’unico punto stazionario
     la matrice hessiana in (0, 0) è
                                                           
                                ∇2 f (0, 0) = 2 10     0
                                                       −1

     che non è semidefinita
     cioè (0, 0) non soddisfa una condizione necessaria per essere di massimo o
     minimo locale




         L.Freddi                                               April 7, 2026   15 / 36
Esempi
Consideriamo la funzione definita su R2 da
                                 f (x, y) = x2 − y 2
Si ha che
     (0, 0) è l’unico punto stazionario
     la matrice hessiana in (0, 0) è
                                                           
                                ∇2 f (0, 0) = 2 10     0
                                                       −1

     che non è semidefinita
     cioè (0, 0) non soddisfa una condizione necessaria per essere di massimo o
     minimo locale
     quindi (0, 0) è né di massimo né di minimo locale; un punto di questo tipo si
     dice punto di sella.




         L.Freddi                                                April 7, 2026   15 / 36
Esempi
Per disegnarne il grafico osserviamo che
     f (x, y) = 0 se e solo se
          x2 − y 2 = 0 ⇐⇒ (x − y)(x + y) = 0 ⇐⇒ y = x o y = −x
     cioè f si annulla sulle due rette bisettrici del piano z = 0




         L.Freddi                                                    April 7, 2026   16 / 36
Esempi
Per disegnarne il grafico osserviamo che
     f (x, y) = 0 se e solo se
          x2 − y 2 = 0 ⇐⇒ (x − y)(x + y) = 0 ⇐⇒ y = x o y = −x
     cioè f si annulla sulle due rette bisettrici del piano z = 0
     le intersezioni con i piani x = 0 e y = 0 sono le parabole di equazione
     rispettivamente z = −y 2 e z = x2 .




         L.Freddi                                                    April 7, 2026   16 / 36
Esempi
Per disegnarne il grafico osserviamo che
     f (x, y) = 0 se e solo se
          x2 − y 2 = 0 ⇐⇒ (x − y)(x + y) = 0 ⇐⇒ y = x o y = −x
     cioè f si annulla sulle due rette bisettrici del piano z = 0
     le intersezioni con i piani x = 0 e y = 0 sono le parabole di equazione
     rispettivamente z = −y 2 e z = x2 .
     le intersezioni con i piani z = c sono iperboli di equazione x2 − y 2 = c




         L.Freddi                                                    April 7, 2026   16 / 36
Esempi
Per disegnarne il grafico osserviamo che
     f (x, y) = 0 se e solo se
           x2 − y 2 = 0 ⇐⇒ (x − y)(x + y) = 0 ⇐⇒ y = x o y = −x
     cioè f si annulla sulle due rette bisettrici del piano z = 0
     le intersezioni con i piani x = 0 e y = 0 sono le parabole di equazione
     rispettivamente z = −y 2 e z = x2 .
     le intersezioni con i piani z = c sono iperboli di equazione x2 − y 2 = c
Il grafico che si ottiene è una superficie detta paraboloide iperbolico o a sella




         L.Freddi                                                    April 7, 2026   16 / 36
Esercizio
Esercizio (per casa)
Cercare eventuali punti di massimo o minimo locali della funzione

                            f (x, y) = y 2 − 3y 2 x + x3

sul suo dominio e poi il massimo e il minimo di f sull’insieme Q = [0, 1]2 .




         L.Freddi                                                April 7, 2026   17 / 36
Esercizio
Esercizio (per casa)
Cercare eventuali punti di massimo o minimo locali della funzione

                                f (x, y) = y 2 − 3y 2 x + x3

sul suo dominio e poi il massimo e il minimo di f sull’insieme Q = [0, 1]2 .

Si ha
                    ∂f                              ∂f
                         = −3y 2 + 3x2 ,                   = 2y(1 − 3x)
                    ∂x                              ∂y
quindi sono stazionari i punti (0, 0), ( 13 , 13 ) e ( 13 , − 31 ) Le derivate seconde sono
                     ∂2f            ∂2f                     ∂2f
                         = 6x,           = 2(1 − 3x)            = −6y
                     ∂x2            ∂y 2                   ∂x∂y




          L.Freddi                                                       April 7, 2026    17 / 36
Esercizio
Esercizio (per casa)
Cercare eventuali punti di massimo o minimo locali della funzione

                                  f (x, y) = y 2 − 3y 2 x + x3

sul suo dominio e poi il massimo e il minimo di f sull’insieme Q = [0, 1]2 .

Si ha
                    ∂f                              ∂f
                         = −3y 2 + 3x2 ,                   = 2y(1 − 3x)
                    ∂x                              ∂y
quindi sono stazionari i punti (0, 0), ( 13 , 13 ) e ( 13 , − 31 ) Le derivate seconde sono
                     ∂2f             ∂2f                      ∂2f
                         = 6x,            = 2(1 − 3x)             = −6y
                     ∂x2             ∂y 2                    ∂x∂y
Si ha dunque
                                      1 1   
                                                        −2
                                                                          1 1                   
∇2 f (0, 0) = 00      0
                      2       ,   ∇2 f ( , ) = −2
                                                2
                                                         0       ,   ∇2 f ( , − ) = 22        2
                                                                                              4
                                        3 3                                3 3


          L.Freddi                                                        April 7, 2026   17 / 36
Esercizio
Esercizio (per casa)
Cercare eventuali punti di massimo o minimo locali della funzione

                                  f (x, y) = y 2 − 3y 2 x + x3

sul suo dominio e poi il massimo e il minimo di f sull’insieme Q = [0, 1]2 .

Si ha
                    ∂f                              ∂f
                         = −3y 2 + 3x2 ,                   = 2y(1 − 3x)
                    ∂x                              ∂y
quindi sono stazionari i punti (0, 0), ( 13 , 13 ) e ( 13 , − 31 ) Le derivate seconde sono
                     ∂2f             ∂2f                      ∂2f
                         = 6x,            = 2(1 − 3x)             = −6y
                     ∂x2             ∂y 2                    ∂x∂y
Si ha dunque
                                      1 1   
                                                        −2
                                                                          1 1                   
∇2 f (0, 0) = 00      0
                      2       ,   ∇2 f ( , ) = −2
                                                2
                                                         0       ,   ∇2 f ( , − ) = 22        2
                                                                                              4
                                        3 3                                3 3
Concludere lo studio
          L.Freddi                                                        April 7, 2026   17 / 36
Esercizi
Esercizio
Cercare eventuali punti di massimo o minimo locali della funzione

                        f (x, y) = (y − x2 )(x2 + y 2 + 2y)

sul suo dominio e poi il massimo e il minimo di f sulla palla chiusa di centro
l’origine e raggio 2.




         L.Freddi                                               April 7, 2026    18 / 36
Esercizi
Esercizio
Cercare eventuali punti di massimo o minimo locali della funzione

                         f (x, y) = (y − x2 )(x2 + y 2 + 2y)

sul suo dominio e poi il massimo e il minimo di f sulla palla chiusa di centro
l’origine e raggio 2.

La funzione è definita su R2 che è aperto. È inoltre differenziabile in ogni punto.




         L.Freddi                                                  April 7, 2026   18 / 36
Esercizi
Esercizio
Cercare eventuali punti di massimo o minimo locali della funzione

                         f (x, y) = (y − x2 )(x2 + y 2 + 2y)

sul suo dominio e poi il massimo e il minimo di f sulla palla chiusa di centro
l’origine e raggio 2.

La funzione è definita su R2 che è aperto. È inoltre differenziabile in ogni punto.
Le derivate parziali risultano
                        fx (x, y) = −4x3 − 2xy 2 − 2xy

                        fy (x, y) = −x2 + 3y 2 + 4y − 2x2 y




         L.Freddi                                                  April 7, 2026   18 / 36
Esercizi
Esercizio
Cercare eventuali punti di massimo o minimo locali della funzione

                         f (x, y) = (y − x2 )(x2 + y 2 + 2y)

sul suo dominio e poi il massimo e il minimo di f sulla palla chiusa di centro
l’origine e raggio 2.

La funzione è definita su R2 che è aperto. È inoltre differenziabile in ogni punto.
Le derivate parziali risultano
                        fx (x, y) = −4x3 − 2xy 2 − 2xy

                        fy (x, y) = −x2 + 3y 2 + 4y − 2x2 y
e i punti stazionari sono le soluzioni del sistema
                                            −4x3 − 2xy 2 − 2xy = 0
          (                             (
             fx (x, y) = 0
                                ⇐⇒
             fy (x, y) = 0                  −x2 + 3y 2 + 4y − 2x2 y = 0

         L.Freddi                                                  April 7, 2026   18 / 36
Esercizi
Esercizio
Cercare eventuali punti di massimo o minimo locali della funzione

                         f (x, y) = (y − x2 )(x2 + y 2 + 2y)

sul suo dominio e poi il massimo e il minimo di f sulla palla chiusa di centro
l’origine e raggio 2.

La funzione è definita su R2 che è aperto. È inoltre differenziabile in ogni punto.
Le derivate parziali risultano
                        fx (x, y) = −4x3 − 2xy 2 − 2xy

                        fy (x, y) = −x2 + 3y 2 + 4y − 2x2 y
e i punti stazionari sono le soluzioni del sistema
                                            −4x3 − 2xy 2 − 2xy = 0
          (                             (
             fx (x, y) = 0
                                ⇐⇒
             fy (x, y) = 0                  −x2 + 3y 2 + 4y − 2x2 y = 0
che sono solamente due (0, 0) e (0, −4/3).
         L.Freddi                                                  April 7, 2026   18 / 36
Esercizi
Per applicare il criterio della matrice hessiana calcoliamo le derivate seconde, che
risultano
                         fxx (x, y) = −12x2 − 2y 2 − 2y

                       fyy (x, y) = 6y + 4 − 2x2

                       fxy (x, y) = fyx (x, y) = −4xy − 2x.




         L.Freddi                                                April 7, 2026   19 / 36
Esercizi
Per applicare il criterio della matrice hessiana calcoliamo le derivate seconde, che
risultano
                         fxx (x, y) = −12x2 − 2y 2 − 2y

                         fyy (x, y) = 6y + 4 − 2x2

                         fxy (x, y) = fyx (x, y) = −4xy − 2x.
Si ha dunque
                                                                               
                             0   0                                  −8/9    0
         ∇2 f (0, 0) =                   e   ∇2 f (0, −4/3) =
                             0   4                                   0      −4




         L.Freddi                                                      April 7, 2026   19 / 36
Esercizi
Per applicare il criterio della matrice hessiana calcoliamo le derivate seconde, che
risultano
                         fxx (x, y) = −12x2 − 2y 2 − 2y

                         fyy (x, y) = 6y + 4 − 2x2

                         fxy (x, y) = fyx (x, y) = −4xy − 2x.
Si ha dunque
                                                                               
                             0   0                                  −8/9    0
         ∇2 f (0, 0) =                   e   ∇2 f (0, −4/3) =
                             0   4                                   0      −4
La matrice hessiana




         L.Freddi                                                      April 7, 2026   19 / 36
Esercizi
Per applicare il criterio della matrice hessiana calcoliamo le derivate seconde, che
risultano
                         fxx (x, y) = −12x2 − 2y 2 − 2y

                         fyy (x, y) = 6y + 4 − 2x2

                         fxy (x, y) = fyx (x, y) = −4xy − 2x.
Si ha dunque
                                                                               
                             0   0                                  −8/9    0
         ∇2 f (0, 0) =                   e   ∇2 f (0, −4/3) =
                             0   4                                   0      −4
La matrice hessiana
     in (0, −4/3) è definita negativa, quindi il punto (0, −4/3) è di massimo
     relativo e f (0, −4/3) = 32/27




         L.Freddi                                                      April 7, 2026   19 / 36
Esercizi
Per applicare il criterio della matrice hessiana calcoliamo le derivate seconde, che
risultano
                         fxx (x, y) = −12x2 − 2y 2 − 2y

                         fyy (x, y) = 6y + 4 − 2x2

                         fxy (x, y) = fyx (x, y) = −4xy − 2x.
Si ha dunque
                                                                               
                             0   0                                  −8/9    0
         ∇2 f (0, 0) =                   e   ∇2 f (0, −4/3) =
                             0   4                                   0      −4
La matrice hessiana
     in (0, −4/3) è definita negativa, quindi il punto (0, −4/3) è di massimo
     relativo e f (0, −4/3) = 32/27
     in (0, 0) è semidefinita positiva, quindi è soddisfatta una condizione
     necessaria (ma non sufficiente) affinché il punto sia di minimo locale; poichè
     f (0, 0) = 0, può essere utile, per decidere se il punto è o meno di minimo,
     studiare il segno della funzione in un intorno dell’origine.

         L.Freddi                                                      April 7, 2026   19 / 36
Esercizi
Si ha f (x, y) > 0 se e solo se
                         y − x2 > 0 e x2 + y 2 + 2y > 0
oppure
                         y − x2 < 0 e x2 + y 2 + 2y < 0




         L.Freddi                                         April 7, 2026   20 / 36
Esercizi
Si ha f (x, y) > 0 se e solo se
                         y − x2 > 0 e x2 + y 2 + 2y > 0
oppure
                         y − x2 < 0 e x2 + y 2 + 2y < 0




         L.Freddi                                         April 7, 2026   20 / 36
Esercizi
Si ha f (x, y) > 0 se e solo se
                          y − x2 > 0 e x2 + y 2 + 2y > 0
oppure
                          y − x2 < 0 e x2 + y 2 + 2y < 0




In ogni intorno dell’origine ci sono sia punti in cui la funzione è positiva sia punti
in cui è negativa, quindi (0, 0) non è né di massimo né di minimo locale
         L.Freddi                                                   April 7, 2026   20 / 36
Esercizi
Si ha f (x, y) > 0 se e solo se
                          y − x2 > 0 e x2 + y 2 + 2y > 0
oppure
                          y − x2 < 0 e x2 + y 2 + 2y < 0




In ogni intorno dell’origine ci sono sia punti in cui la funzione è positiva sia punti
in cui è negativa, quindi (0, 0) non è né di massimo né di minimo locale
         L.Freddi                                                   April 7, 2026   20 / 36
Esercizi
Consideriamo ora il problema di determinare il max e min di f su
                       B = {(x, y) ∈ R2 : x2 + y 2 ≤ 4}




         L.Freddi                                             April 7, 2026   21 / 36
Esercizi
Consideriamo ora il problema di determinare il max e min di f su
                        B = {(x, y) ∈ R2 : x2 + y 2 ≤ 4}
Poiché B è chiuso e limitato, max e min esistono per il Teorema di Weierstrass.




         L.Freddi                                               April 7, 2026   21 / 36
Esercizi
Consideriamo ora il problema di determinare il max e min di f su
                        B = {(x, y) ∈ R2 : x2 + y 2 ≤ 4}
Poiché B è chiuso e limitato, max e min esistono per il Teorema di Weierstrass.

I punti di massimo e di minimo vanno ricercati




         L.Freddi                                               April 7, 2026   21 / 36
Esercizi
Consideriamo ora il problema di determinare il max e min di f su
                        B = {(x, y) ∈ R2 : x2 + y 2 ≤ 4}
Poiché B è chiuso e limitato, max e min esistono per il Teorema di Weierstrass.

I punti di massimo e di minimo vanno ricercati
     tra i punti stazionari interni a B (teorema dei punti critici)




         L.Freddi                                                 April 7, 2026   21 / 36
Esercizi
Consideriamo ora il problema di determinare il max e min di f su
                        B = {(x, y) ∈ R2 : x2 + y 2 ≤ 4}
Poiché B è chiuso e limitato, max e min esistono per il Teorema di Weierstrass.

I punti di massimo e di minimo vanno ricercati
     tra i punti stazionari interni a B (teorema dei punti critici)
     sulla frontiera di B




         L.Freddi                                                 April 7, 2026   21 / 36
Esercizi
Consideriamo ora il problema di determinare il max e min di f su
                        B = {(x, y) ∈ R2 : x2 + y 2 ≤ 4}
Poiché B è chiuso e limitato, max e min esistono per il Teorema di Weierstrass.

I punti di massimo e di minimo vanno ricercati
     tra i punti stazionari interni a B (teorema dei punti critici)
     sulla frontiera di B
I punti stazionari interni a B sono (0, −4/3) con valore f (0, −4/3) = 32/27 (max
locale) e (0, 0) che, però, abbiamo già dimostrato non essere né di max né di min.




         L.Freddi                                                 April 7, 2026   21 / 36
Esercizi
Consideriamo ora il problema di determinare il max e min di f su
                        B = {(x, y) ∈ R2 : x2 + y 2 ≤ 4}
Poiché B è chiuso e limitato, max e min esistono per il Teorema di Weierstrass.

I punti di massimo e di minimo vanno ricercati
     tra i punti stazionari interni a B (teorema dei punti critici)
     sulla frontiera di B
I punti stazionari interni a B sono (0, −4/3) con valore f (0, −4/3) = 32/27 (max
locale) e (0, 0) che, però, abbiamo già dimostrato non essere né di max né di min.
Studiamo la funzione sulla frontiera di B
                        ∂B = {(x, y) ∈ R2 ; x2 + y 2 = 4}




         L.Freddi                                                 April 7, 2026   21 / 36
Esercizi
Consideriamo ora il problema di determinare il max e min di f su
                        B = {(x, y) ∈ R2 : x2 + y 2 ≤ 4}
Poiché B è chiuso e limitato, max e min esistono per il Teorema di Weierstrass.

I punti di massimo e di minimo vanno ricercati
     tra i punti stazionari interni a B (teorema dei punti critici)
     sulla frontiera di B
I punti stazionari interni a B sono (0, −4/3) con valore f (0, −4/3) = 32/27 (max
locale) e (0, 0) che, però, abbiamo già dimostrato non essere né di max né di min.
Studiamo la funzione sulla frontiera di B
                        ∂B = {(x, y) ∈ R2 ; x2 + y 2 = 4}
La restrizione di f a ∂B
                         g := f|∂B = (y 2 + y − 4)(4 + 2y)
è una funzione continua della sola variabile y ∈ [−2, 2].

         L.Freddi                                                 April 7, 2026   21 / 36
Esercizi
Calcoliamo max e min di g in [−2, 2], che esistono per il Teorema di Weierstrass.




         L.Freddi                                              April 7, 2026   22 / 36
Esercizi
Calcoliamo max e min di g in [−2, 2], che esistono per il Teorema di Weierstrass.
Si ha
                           g ′ (y) = 2(3y 2 + 6y − 2)
da cui si ricava che
                                             p           p
                 g ′ (y) ≤ 0 ⇐⇒ y ∈ [−1 − 5/3, −1 + 5/3]
                p
e, poiché −1 − 5/3 < −2 abbiamo che
                                  p                         p
     g è decrescente in [−2, −1 + 5/3] e crescente in [−1 + 5/3, 2]
                                                      p
quindi ha punti di max relativo −2 e 2 e minimo −1 + 5/3 con valori
   g(−2) = f (0, −2) = 0, g(2) = f (0, 2) = 16,
          p                 p             p                 
   g(−1 + 5/3) = f (4/3 + 2 5/3, −1 + 5/3) = −4 2 + (5/3)3/2 < 0.




         L.Freddi                                              April 7, 2026   22 / 36
Esercizi
Calcoliamo max e min di g in [−2, 2], che esistono per il Teorema di Weierstrass.
Si ha
                           g ′ (y) = 2(3y 2 + 6y − 2)
da cui si ricava che
                                             p           p
                 g ′ (y) ≤ 0 ⇐⇒ y ∈ [−1 − 5/3, −1 + 5/3]
                p
e, poiché −1 − 5/3 < −2 abbiamo che
                                  p                         p
     g è decrescente in [−2, −1 + 5/3] e crescente in [−1 + 5/3, 2]
                                                      p
quindi ha punti di max relativo −2 e 2 e minimo −1 + 5/3 con valori
     g(−2) = f (0, −2) = 0, g(2) = f (0, 2) = 16,
            p                 p             p                 
     g(−1 + 5/3) = f (4/3 + 2 5/3, −1 + 5/3) = −4 2 + (5/3)3/2 < 0.
Confrontandoli col valore assunto dalla funzione nel max locale interno
(f (0, −4/3) = 32/27) si ha
                                             p          p
max f = f (0, 2) = 16 e min f = f (4/3+2 5/3, −1+ 5/3) = −4 2+(5/3)3/2 .
                                                                        
 B                         B


         L.Freddi                                              April 7, 2026   22 / 36
Esercizio
Esercizio (per casa)
Determinare i punti stazionari della seguente funzione e stabilire se sono di
massimo o minimo locale
                                f (x, y) = x2 y − xy




         L.Freddi                                                April 7, 2026   23 / 36
Esercizio
Esercizio (per casa)
Determinare i punti stazionari della seguente funzione e stabilire se sono di
massimo o minimo locale
                                f (x, y) = x2 y − xy

Si ha
            ∂f                                  ∂f
               = 2xy − y = (2x − 1)y,               = x2 − x = x(x − 1)
            ∂x                                  ∂y
quindi sono stazionari i punti (0, 0) e(1, 0). Le derivate seconde sono
                     ∂2f           ∂2f          ∂2f
                         = 2y,          =0          = 2x − 1
                     ∂x2           ∂y 2        ∂x∂y




         L.Freddi                                                April 7, 2026   23 / 36
Esercizio
Esercizio (per casa)
Determinare i punti stazionari della seguente funzione e stabilire se sono di
massimo o minimo locale
                                f (x, y) = x2 y − xy

Si ha
            ∂f                                  ∂f
               = 2xy − y = (2x − 1)y,               = x2 − x = x(x − 1)
            ∂x                                  ∂y
quindi sono stazionari i punti (0, 0) e(1, 0). Le derivate seconde sono
                     ∂2f              ∂2f           ∂2f
                         = 2y,             =0           = 2x − 1
                     ∂x2              ∂y 2         ∂x∂y
Si ha dunque
                                                                               
                                 0    −1                               0      1
             ∇2 f (0, 0) =                     e   ∇2 f (1, 0) =
                                 −1    0                               1      2




         L.Freddi                                                          April 7, 2026   23 / 36
Esercizio
Esercizio (per casa)
Determinare i punti stazionari della seguente funzione e stabilire se sono di
massimo o minimo locale
                                f (x, y) = x2 y − xy

Si ha
            ∂f                                  ∂f
               = 2xy − y = (2x − 1)y,               = x2 − x = x(x − 1)
            ∂x                                  ∂y
quindi sono stazionari i punti (0, 0) e(1, 0). Le derivate seconde sono
                     ∂2f              ∂2f           ∂2f
                         = 2y,             =0           = 2x − 1
                     ∂x2              ∂y 2         ∂x∂y
Si ha dunque
                                                                               
                                 0    −1                               0      1
             ∇2 f (0, 0) =                     e   ∇2 f (1, 0) =
                                 −1    0                               1      2
Concludere lo studio


         L.Freddi                                                          April 7, 2026   23 / 36
Criterio della matrice hessiana
Usando il teorema precedente, dimostrare, per esercizio, il seguente Criterio della
Matrice Hessiana per le funzioni di due variabili.
Proposizione (esercizio)
Sia D ⊆ R2 , f ∈ C 2 (D) e (x0 , y0 ) un punto interno a D. Se risulta

                      ∇f (x0 , y0 ) = 0 e det ∇2 f (x0 , y0 ) > 0

allora
  i) se fxx (x0 , y0 ) > 0 il punto è di minimo locale;
 ii) se fxx (x0 , y0 ) < 0 il punto è di massimo locale.
Se invece
                                 det ∇2 f (x0 , y0 ) < 0
allora il punto non è né di massimo né di minimo.




         L.Freddi                                                   April 7, 2026   24 / 36
Criterio della matrice hessiana
Dimostrare poi che il criterio non dice nulla sul caso
                                 det ∇2 f (x0 , y0 ) = 0
nel quale, infatti, può accadere che il punto sia di massimo o di minimo o anche
di sella. Si considerino ad esempio le funzioni f (x, y) = x2 y 2 , f (x, y) = −x2 y 2 ,
f (x, y) = x3 y.




          L.Freddi                                                   April 7, 2026    25 / 36
Esercizi (per casa)
Determinare i punti stazionari delle seguenti funzioni e stabilire se sono di
massimo o minimo locale
  1    f (x, y) = x2 + xy 2 ;
                      2         2
  2    f (x, y) = ex +2xy−3y ;
                                                 2
  3                2
       f (x, y) = y−1 [2(y − 1)2 + 1] + (x+1)
                                          x2 ;
  4    f (x, y) = arctan(x2 + 2y 2 ) − 2x2 − y 2 ;
  5    f (x, y) = 2xy 2 + x3 − y 3 ;
  6    f (x, y) = x2 − 2y 2 + √ 21           ;
                                    x +y 2
  7    f (x, y) = cos(x + y) + cos(x − y);
  8    f (x, y) = x2 log(x + y);
                  p
  9    f (x, y) = (x2 + y 2 ) − 3x − 6y;
  10   f (x, y) = |x|e−y .



           L.Freddi                                               April 7, 2026   26 / 36
Esercizi
Risposte ad alcuni degli esercizi precedenti:
                                                      √            √
  4. Sono critici i punti di coordinate (0, 0), (0, 1/ 2) e (0, −1/ 2). Il primo
     non è né di max né di min e gli altri due sono di minimo locale.
  5. (0, 0) è l’unico punto stazionario e non è né di massimo né di minimo locale.
  6. I punti (2−1/3 , 0) e (−2−1/3 , 0) sono stazionari ma non sono né di massimo
     né di minimo locale.




         L.Freddi                                                 April 7, 2026    27 / 36
Esercizi
Esercizio (per casa)
Si consideri la funzione f : R2 → R definita da
                                           2   2
                            f (x, y) = e−x +y (x2 + 2y)


  1   Determinare i punti stazionari di f e stabilire se sono massimi o minimi
      locali.
  2   Scegliere un punto stazionario (x0 , y0 ) (se esiste) che non sia nè di massimo
      nè di minimo locale e determinare un sottoinsieme D di R2 con parte interna
      non vuota tale che (x0 , y0 ) sia di massimo oppure di minimo per f su D.




          L.Freddi                                                April 7, 2026   28 / 36
Esercizi
Esercizio (per casa)
Data la funzione
                                            4
                               f (x, y) =     + y 2 + 2x
                                            x

  1   determinare gli eventuali punti di massimo e minimo relativo;
  2   calcolare il massimo e il minimo di f sul rettangolo [1, 2] × [−1, 1].




          L.Freddi                                                April 7, 2026   29 / 36
Esercizi
Esercizio (per casa)
Data la funzioneDeterminare massimi e minimi relativi della funzione

                               f (x, y) = x3 + x2 + y 2


  1   determinare eventuali massimi e minimi relativi;
  2   calcolare il massimo e il minimo di f sulla palla di centro l’origine e raggio 2.

Esercizio (per casa)
Determinare massimo e minimo della funzione

                              f (x, y) = (x2 + y 2 )ex−y

sull’insieme A = {(x, y) ∈ R2 : |x| + |y| ≤ 1}.



          L.Freddi                                                 April 7, 2026   30 / 36
Esercizi
Esercizio (per casa)
Discutere l’esistenza del massimo e del minimo della funzione
                                   
                                     xy log |x| se x ̸= 0
                        f (x, y) =
                                         0      se x = 0

sull’insieme Q = {(x, y) ∈ R2 : |x| ≤ 2, |y| ≤ 2}.

Esercizio (per casa)
Determinare massimo e minimo della funzione
                                              xy
                             f (x, y) =
                                          x2 + y 2 + 1

sull’insieme A = {(x, y) ∈ R2 : 1/4 ≤ x2 + y 2 ≤ 4, x ≥ 0}.




         L.Freddi                                               April 7, 2026   31 / 36
Regola dei segni di Cartesio
Data un’equazione algebrica di grado n
                       λn + an−1 λn−1 + · · · + a1 λ + a0 = 0                        (4)
con radici tutte reali, si potrebbe dimostrare che vale la seguente regola dei segni
di Cartesio
     le radici sono tutte negative se e solo se tutti i coefficienti ai sono positivi;
     le radici sono tutte positive se e solo se i coefficienti sono alternativamente
     negativi e positivi.

Esercizio
Dimostrare la regola di Cartesio prima nei casi n = 2 e n = 3 ed elaborare poi
una dimostrazione nel caso generale.

La regola si può applicare per stabilire se l’hessiana di una funzione di n variabili è
definita. In tal caso la (4) sarà l’equazione caratteristica della matrice che, nel
caso di funzioni C 2 , ha radici tutte reali perchè l’hessiana è simmetrica.



          L.Freddi                                                   April 7, 2026   32 / 36
Esercizi
Esercizio (per casa)
Determinare eventuali punti di massimo e di minimo relativo per la funzione

                       f (x, y, z) = x2 + y 3 + z 2 − xy − xz




         L.Freddi                                               April 7, 2026   33 / 36
Esercizi
Esercizio (per casa)
Determinare eventuali punti di massimo e di minimo relativo per la funzione

                         f (x, y, z) = x2 + y 3 + z 2 − xy − xz
                                      4 2 2
Sono stazionari i punti (0, 0, 0) e ( 27 , 9 , 27 ) e si ha
                  det ∇2 f (0, 0, 0) − λI = −λ3 + 4λ2 − 2λ − 2
                                             

pertanto, in base alla regola dei segni vi sono sia autovalori negativi che positivi,
quindi (0, 0, 0) non è né di massimo né di minimo relativo. Invece
                            4 2 2                       16      22
               det ∇2 f ( , , ) − λI = −λ3 + λ2 − λ + 2
                                            
                           27 9 27                       3       3
                                                                         4 2 2
quindi, per la regola dei segni, tutti gli autovalori sono positivi e ( 27 , 9 , 27 ) è un
punto di minimo relativo.




          L.Freddi                                                     April 7, 2026    33 / 36
Esercizi
Esercizio (per casa)
Determinare eventuali punti di massimo e di minimo relativo per la funzione
f (x, y, z) = 4xy + xz + 6y 2 + x2 z + 2xyz




         L.Freddi                                             April 7, 2026   34 / 36
Esercizi
Esercizio (per casa)
Determinare eventuali punti di massimo e di minimo relativo per la funzione
f (x, y, z) = 4xy + xz + 6y 2 + x2 z + 2xyz

f è definita su tutto R3 e ammette derivate parziali continue di ogni ordine,
quindi eventuali punti di massimo o minimo relativo vanno ricercati tra i punti
stazionari, cioè le soluzioni del sistema
                           
                            fx = 4y + z + 2xz + 2yz = 0
                              fy = 4x + 12y + 2xz = 0
                              fz = x + x2 + 2xy = 0.
                           

L’ultima equazione si può riscrivere nella forma
             x(1 + x + 2y) = 0 ⇐⇒ x = 0 oppure 1 + x + 2y = 0.
Se x = 0, sostituendo nella seconda equazione si ottiene y = 0 e sostituendo nella
prima si trova z = 0. Pertanto il punto (0, 0, 0) è stazionario.
Se invece 1 + x + 2y = 0 allora x = −1 − 2y e sostituendo nelle altre due
equazioni e risolvendo in y e z si trova che un’altra soluzione è (1, −1, 4).

         L.Freddi                                              April 7, 2026      34 / 36
Esercizi
Calcolando le derivate parziali seconde di f nei punti stazionari si trova che le
matrici hessiane in tali punti sono date da
                                                                          
                         0 4 1                                    8 12 1
    ∇2 f (0, 0, 0) =  4 12 0  e ∇2 f (1, −1, 4) =  12 12 2 
                         1 0 0                                    1 2 0
e i polinomi caratteristici delle due matrici sono rispettivamente
       P1 (λ) = −λ3 + 12λ2 + 17λ − 12, P2 (λ) = −λ3 + 20λ2 + 52λ + 4
che, per la regola dei segni hanno, ciascuno, sia zeri negativi che positivi. Ne
consegue che nessuno dei due punti stazionari può essere di massimo o di minimo
relativo.




         L.Freddi                                                 April 7, 2026     35 / 36
Esercizi
Esercizio (per casa)
Determinare eventuali punti di massimo e di minimo relativo per le seguenti
funzioni
  1   f (x, y) = x2 + y 2 − log(x2 + y)
  2   f (x, y, z, t) = x2 + 2y 2 + z 2 + 2t2 + yz − 2xt




          L.Freddi                                            April 7, 2026   36 / 36
