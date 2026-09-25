---
fonte: "An2_2026_pres18_superfici.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Superfici e integrali su superfici

                        L.Freddi


                      April 27, 2026




L.Freddi                                   April 27, 2026   1 / 15
Superfici regolari di R3
Definizione
Sia K un compatto di R2 , chiusura di un aperto connesso. Si chiama superficie
regolare semplice di R3 una funzione

                                     φ : K → R3
con le seguenti proprietà:
(a) φ è di classe C 1 (K);
(b) la restrizione di φ all’interno di K è iniettiva;
(c) la matrice jacobiana di φ ha rango 2 (max) in ogni punto (u, v) interno a K.




         L.Freddi                                            April 27, 2026   2 / 15
Superfici regolari di R3
Definizione
Sia K un compatto di R2 , chiusura di un aperto connesso. Si chiama superficie
regolare semplice di R3 una funzione

                                     φ : K → R3
con le seguenti proprietà:
(a) φ è di classe C 1 (K);
(b) la restrizione di φ all’interno di K è iniettiva;
(c) la matrice jacobiana di φ ha rango 2 (max) in ogni punto (u, v) interno a K.

     (b) è la condizione di semplicità




         L.Freddi                                            April 27, 2026   2 / 15
Superfici regolari di R3
Definizione
Sia K un compatto di R2 , chiusura di un aperto connesso. Si chiama superficie
regolare semplice di R3 una funzione

                                     φ : K → R3
con le seguenti proprietà:
(a) φ è di classe C 1 (K);
(b) la restrizione di φ all’interno di K è iniettiva;
(c) la matrice jacobiana di φ ha rango 2 (max) in ogni punto (u, v) interno a K.

     (b) è la condizione di semplicità
     (c) implica l’esistenza di un piano tangente alla superficie nel punto φ(u, v).




         L.Freddi                                               April 27, 2026   2 / 15
Superfici regolari di R3
Definizione
Sia K un compatto di R2 , chiusura di un aperto connesso. Si chiama superficie
regolare semplice di R3 una funzione

                                     φ : K → R3
con le seguenti proprietà:
(a) φ è di classe C 1 (K);
(b) la restrizione di φ all’interno di K è iniettiva;
(c) la matrice jacobiana di φ ha rango 2 (max) in ogni punto (u, v) interno a K.

     (b) è la condizione di semplicità
     (c) implica l’esistenza di un piano tangente alla superficie nel punto φ(u, v).
     La condizione analoga per le curve regolari richiede che φ′ sia diverso da
     zero (cioè abbia rango 1) e quindi esista la retta tangente.



         L.Freddi                                               April 27, 2026   2 / 15
Piano tangente e vettore normale
Data una superficie φ : K → R3 , la sua matrice jacobiana è
                                    ∂φ1 ∂φ1 
                                        ∂u    ∂v
                                                  
                             ∇φ =  ∂φ2      ∂φ2
                                                  
                                   ∂u        ∂v   
                                                   
                                       ∂φ3   ∂φ3
                                       ∂u     ∂v




         L.Freddi                                              April 27, 2026   3 / 15
Piano tangente e vettore normale
Data una superficie φ : K → R3 , la sua matrice jacobiana è
                                    ∂φ1 ∂φ1 
                                         ∂u     ∂v
                                                     
                              ∇φ =  ∂φ2        ∂φ2
                                                     
                                    ∂u          ∂v   
                                                      
                                         ∂φ3    ∂φ3
                                         ∂u      ∂v
cioè la matrice avente per colonne i due vettori derivati
                              ∂u φ = ( ∂φ 1 ∂φ2 ∂φ3
                                       ∂u , ∂u , ∂u )

                              ∂v φ = ( ∂φ 1 ∂φ2 ∂φ3
                                        ∂v , ∂v , ∂v )




         L.Freddi                                              April 27, 2026   3 / 15
Piano tangente e vettore normale
Data una superficie φ : K → R3 , la sua matrice jacobiana è
                                    ∂φ1 ∂φ1 
                                         ∂u     ∂v
                                                     
                              ∇φ =  ∂φ2        ∂φ2
                                                     
                                    ∂u          ∂v   
                                                      
                                         ∂φ3    ∂φ3
                                         ∂u      ∂v
cioè la matrice avente per colonne i due vettori derivati
                              ∂u φ = ( ∂φ 1 ∂φ2 ∂φ3
                                       ∂u , ∂u , ∂u )

                              ∂v φ = ( ∂φ 1 ∂φ2 ∂φ3
                                        ∂v , ∂v , ∂v )
Allora, la condizione (c)




         L.Freddi                                              April 27, 2026   3 / 15
Piano tangente e vettore normale
Data una superficie φ : K → R3 , la sua matrice jacobiana è
                                    ∂φ1 ∂φ1 
                                         ∂u     ∂v
                                                     
                              ∇φ =  ∂φ2        ∂φ2
                                                     
                                    ∂u          ∂v   
                                                      
                                         ∂φ3    ∂φ3
                                         ∂u      ∂v
cioè la matrice avente per colonne i due vettori derivati
                              ∂u φ = ( ∂φ 1 ∂φ2 ∂φ3
                                       ∂u , ∂u , ∂u )

                              ∂v φ = ( ∂φ 1 ∂φ2 ∂φ3
                                        ∂v , ∂v , ∂v )
Allora, la condizione (c)
     significa che i vettori ∂u φ e ∂v φ sono linearmente indipendenti (quindi
     individuano un piano)




         L.Freddi                                               April 27, 2026   3 / 15
Piano tangente e vettore normale
Data una superficie φ : K → R3 , la sua matrice jacobiana è
                                    ∂φ1 ∂φ1 
                                         ∂u      ∂v
                                                      
                              ∇φ =  ∂φ2         ∂φ2
                                                      
                                    ∂u           ∂v   
                                                       
                                         ∂φ3     ∂φ3
                                         ∂u       ∂v
cioè la matrice avente per colonne i due vettori derivati
                              ∂u φ = ( ∂φ 1 ∂φ2 ∂φ3
                                       ∂u , ∂u , ∂u )

                              ∂v φ = ( ∂φ 1 ∂φ2 ∂φ3
                                        ∂v , ∂v , ∂v )
Allora, la condizione (c)
     significa che i vettori ∂u φ e ∂v φ sono linearmente indipendenti (quindi
     individuano un piano)
     si potrebbe anche scrivere nella forma
                                                             ◦
                              ∂u φ ∧ ∂v φ ̸= 0    ∀(u, v) ∈K

         L.Freddi                                                April 27, 2026   3 / 15
Piano tangente e vettore normale
Fissato un punto (u0 , v0 ) ∈ K, le funzioni
                                      u 7→ φ(u, v0 )
                                      v 7→ φ(u0 , v)
sono curve dette linee coordinate sulla superficie passanti per il punto φ(u0 , v0 )



                                                         φ(u0 , v0 )
                                                 φ


                                (u0 , v0 )



                                             K




         L.Freddi                                                      April 27, 2026   4 / 15
Piano tangente e vettore normale
I vettori derivati
                          ∂u φ(u0 , v0 ),    ∂v φ(u0 , v0 )
sono i vettori tangenti a queste due curve




          L.Freddi                                            April 27, 2026   5 / 15
Piano tangente e vettore normale
I vettori derivati
                          ∂u φ(u0 , v0 ),    ∂v φ(u0 , v0 )
sono i vettori tangenti a queste due curve




Per la condizione (c), essi sono linearmente indipendenti e, pertanto, individuano
un piano detto piano tangente alla superficie nel punto φ(u0 , v0 ).




          L.Freddi                                             April 27, 2026   5 / 15
Piano tangente e vettore normale
I vettori derivati
                          ∂u φ(u0 , v0 ),      ∂v φ(u0 , v0 )
sono i vettori tangenti a queste due curve




Per la condizione (c), essi sono linearmente indipendenti e, pertanto, individuano
un piano detto piano tangente alla superficie nel punto φ(u0 , v0 ).

Il vettore
                            ∂u φ(u0 , v0 ) ∧ ∂v φ(u0 , v0 )
è ortogonale ai due vettori e quindi al piano tangente e si chiama vettore normale
alla superficie nel punto φ(u0 , v0 ).
             L.Freddi                                           April 27, 2026   5 / 15
Superfici orientate e non orientate
Definizione
Due superfici regolari φ : K → R3 e ψ : H → R3 si dicono equivalenti se esiste
un diffeomorfismo π : H → K che rende commutativo il diagramma
                                        φ
                                   K - R3
                                  π 6 ψ
                                   H




         L.Freddi                                             April 27, 2026     6 / 15
Superfici orientate e non orientate
Definizione
Due superfici regolari φ : K → R3 e ψ : H → R3 si dicono equivalenti se esiste
un diffeomorfismo π : H → K che rende commutativo il diagramma
                                        φ
                                   K - R3
                                  π 6 ψ
                                   H
cioè, tale che ψ = φ ◦ π.




         L.Freddi                                             April 27, 2026     6 / 15
Superfici orientate e non orientate
Definizione
Due superfici regolari φ : K → R3 e ψ : H → R3 si dicono equivalenti se esiste
un diffeomorfismo π : H → K che rende commutativo il diagramma
                                        φ
                                   K - R3
                                  π 6 ψ
                                    H
cioè, tale che ψ = φ ◦ π.

     Le classi di equivalenza si chiamano superfici (non orientate). Due superfici
     equivalenti hanno lo stesso sostegno.




         L.Freddi                                               April 27, 2026   6 / 15
Superfici orientate e non orientate
Definizione
Due superfici regolari φ : K → R3 e ψ : H → R3 si dicono equivalenti se esiste
un diffeomorfismo π : H → K che rende commutativo il diagramma
                                        φ
                                   K - R3
                                  π 6 ψ
                                    H
cioè, tale che ψ = φ ◦ π.

     Le classi di equivalenza si chiamano superfici (non orientate). Due superfici
     equivalenti hanno lo stesso sostegno.
     Si dice poi che le due superfici
        ▶ hanno la stessa orientazione se det(∇π) > 0
        ▶ hanno orientazione opposta se det(∇π) < 0




         L.Freddi                                               April 27, 2026   6 / 15
Superfici orientate e non orientate
Definizione
Due superfici regolari φ : K → R3 e ψ : H → R3 si dicono equivalenti se esiste
un diffeomorfismo π : H → K che rende commutativo il diagramma
                                        φ
                                   K - R3
                                  π 6 ψ
                                    H
cioè, tale che ψ = φ ◦ π.

     Le classi di equivalenza si chiamano superfici (non orientate). Due superfici
     equivalenti hanno lo stesso sostegno.
     Si dice poi che le due superfici
        ▶ hanno la stessa orientazione se det(∇π) > 0
        ▶ hanno orientazione opposta se det(∇π) < 0

     Ogni classe di equivalenza Σ di superfici non orientate si scinde quindi in
     due sottoclassi Σ+ e Σ− dette superfici orientate.
         L.Freddi                                               April 27, 2026     6 / 15
Area di una superficie
Definizione
Sia φ : K → R3 una superficie regolare. Si chiama area della superficie il numero
                                 Z
                       A(φ) =        |∂u φ ∧ ∂v φ| dudv.
                                     K


     dimostrare per esercizio che l’area di una superficie non dipende dalla
     parametrizzazione
     la definizione si potrebbe giustificare con ragionamenti del tipo di quelli fatti
     per la lunghezza di una curva, ma la situazione in questo caso è
     notevolmente più complicata e richiede ragionamenti più raffinati.




         L.Freddi                                                 April 27, 2026   7 / 15
Area di una superficie
Esempio
La superficie di equazioni parametriche
                       
                        x = sen u cos v
                                                     0≤u≤π
                           y = sen u sen v
                                                     0 ≤ v ≤ 2π
                           z = cos u
                       

è la sfera di centro l’origine e raggio 1 in R3 .

Il vettore normale risulta

                             |∂u φ ∧ ∂v φ| = sen u    ∀ (u, v).

Quindi                           Z 2π  Z π           
                        A(φ) =                sen u du dv = 4π.
                                   0      0




          L.Freddi                                                April 27, 2026   8 / 15
Area di una superficie
Esercizio
Determinare l’area della porzione di paraboloide circolare

                                   z = x2 + y 2

compresa nel cilindro
                                   x2 + y 2 ≤ 1.




         L.Freddi                                            April 27, 2026   9 / 15
Area di una superficie
Esercizio
Determinare l’area della porzione di paraboloide circolare

                                    z = x2 + y 2

compresa nel cilindro
                                    x2 + y 2 ≤ 1.

La superficie ha equazioni parametriche
                         
                          x=u
                     φ:     y=v                (u, v) ∈ B1 (0).
                            z = u2 + v 2 ,
                         

Si ha ∂u φ = (1, 0, 2u) e ∂v φ = (0, 1, 2v) e quindi
                            ∂u φ ∧ ∂v φ = (−2u, −2v, 1).




         L.Freddi                                                 April 27, 2026   9 / 15
Area di una superficie
Si ha pertanto                  Z        p
                       A(φ) =                1 + 4(u2 + v 2 ) dudv
                                B1 (0)
e, passando a coordinate polari,
           Z 2π  Z 1 p                    Z 1
                                              √
    A(φ) =                     2
                        1 + 4ρ ϱ dϱ dθ = π       1 + 4s ds = π(53/2 − 1)/6.
             0     0                                0




        L.Freddi                                                     April 27, 2026   10 / 15
Area delle superfici di rotazione
L’area di una superficie di rotazione Σ, ottenuta ruotando attorno all’asse z la
curva grafico x = f (z), a ≤ z ≤ b, si può calcolare parametrizzando la superficie
con le coordinate cilindriche



                                             
                                              x = f (z) cos θ
                                                                       a≤z≤b
                                          Σ:   y = f (z) sen θ
                                                                       0 ≤ θ ≤ 2π,
                                               z = z,
                                             




         L.Freddi                                                April 27, 2026   11 / 15
Area delle superfici di rotazione
L’area di una superficie di rotazione Σ, ottenuta ruotando attorno all’asse z la
curva grafico x = f (z), a ≤ z ≤ b, si può calcolare parametrizzando la superficie
con le coordinate cilindriche



                                                   
                                                    x = f (z) cos θ
                                                                              a≤z≤b
                                                Σ:   y = f (z) sen θ
                                                                              0 ≤ θ ≤ 2π,
                                                     z = z,
                                                   



e risulta                              Z b        p
                        A(Σ) = 2π            f (z) 1 + |f ′ (z)|2 dz;
                                        a
sviluppare i dettagli per esercizio.



            L.Freddi                                                    April 27, 2026   11 / 15
Area dei grafici
Se z = f (x, y), con f ∈ C 1 (K), allora il suo grafico è una superficie regolare Σ




Si ha                                  Z p
                           A(Σ) =            1 + |∇f |2 dxdy;
                                       K
sviluppare i dettagli per esercizio.




         L.Freddi                                                 April 27, 2026   12 / 15
Integrale di una funzione su una superficie
Definizione
Sia φ : K → R3 una superficie regolare semplice e f : A → R una funzione
continua definita in un aperto A di R3 contenente il sostegno di φ.
Si definisce integrale di f su Σ il numero
                     Z          Z
                        f dσ =      f (φ(u, v))|∂u φ ∧ ∂v φ| dudv.
                   Σ          K




        L.Freddi                                            April 27, 2026   13 / 15
Integrale di una funzione su una superficie
Definizione
Sia φ : K → R3 una superficie regolare semplice e f : A → R una funzione
continua definita in un aperto A di R3 contenente il sostegno di φ.
Si definisce integrale di f su Σ il numero
                     Z          Z
                        f dσ =      f (φ(u, v))|∂u φ ∧ ∂v φ| dudv.
                    Σ           K


     Si può dimostrare che, come per l’area, anche l’integrale ora definito non
     dipende dalla parametrizzazione della superficie Σ.




         L.Freddi                                               April 27, 2026     13 / 15
Integrale di una funzione su una superficie
Definizione
Sia φ : K → R3 una superficie regolare semplice e f : A → R una funzione
continua definita in un aperto A di R3 contenente il sostegno di φ.
Si definisce integrale di f su Σ il numero
                     Z          Z
                        f dσ =      f (φ(u, v))|∂u φ ∧ ∂v φ| dudv.
                     Σ           K


     Si può dimostrare che, come per l’area, anche l’integrale ora definito non
     dipende dalla parametrizzazione della superficie Σ.
     La definizione si può estendere a superfici regolari a tratti, cioè funzioni
     continue φ : K → R3 tali che K si può scrivere come unione finita
                                              N
                                              [
                                        K=          Ki
                                              i=1
     con Ki chiusura di un aperto connesso, i = 1, . . . , n e con parti interne due
     a due disgiunte, su ciascuno dei quali è regolare, spezzando l’integrale su K
     nella somma degli integrali su ciascun Ki .
         L.Freddi                                                   April 27, 2026    13 / 15
Esercizi per casa
Esercizio
Calcolare l’area delle seguenti superfici:
     
      x = cos u
                          0≤u≤π
  1      y = sen u
                          0 ≤ v ≤ 1,
         z = v,
     
          p
  2 z =      x2 + y 2 , 1 ≤ x2 + y 2 ≤ 2.
  3   la parte del piano passante per i punti (1, 0, 0), (0, 2, 0) e (0, 0, 3), contenuta
      nel primo ottante {(x, y, z) ∈ R3 : x ≥ 0, y ≥ 0, z ≥ 0}.

Esercizio
Calcolare l’area della catenoide, ottenuta ruotando attorno all’asse z la curva di
equazione
                                ez + e−z
                           x=            ,   −a ≤ z ≤ a.
                                    2


          L.Freddi                                                  April 27, 2026   14 / 15
Esercizi per casa
Esercizio
Calcolare                               Z
                                             x2 dσ,
                                         Σ
dove Σ è la porzione di superficie
                                                      y
                                      z = arctan
                                                      x
che si trova al di sopra dell’insieme

               K = {(x, y) ∈ R2 : x ≥ 0, y ≥ 0, 1 ≤ x2 + y 2 ≤ 2}.




         L.Freddi                                            April 27, 2026   15 / 15
