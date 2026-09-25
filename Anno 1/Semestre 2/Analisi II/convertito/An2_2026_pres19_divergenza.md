---
fonte: "An2_2026_pres19_divergenza.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Teoremi della divergenza e del rotore

                  L.Freddi


                April 27, 2026




L.Freddi                           April 27, 2026   1 / 23
Formule di Gauss-Green
Esercizio (Formule di Gauss-Green)
Sia A un sottoinsieme compatto di R2 e sia f ∈ C 1 (B) con B aperto di R2
contenente A. Dimostrare che
  1   se A è normale e C 1 (a tratti) rispetto all’asse x1 allora vale la formula
                              Z                    Z
                                  ∂f
                                       dx1 dx2 =        f ν2 ds,
                               A ∂x2                 ∂A

  2   se A è normale e C 1 (a tratti) rispetto all’asse x2 allora vale la formula
                              Z                    Z
                                  ∂f
                                        dx1 dx2 =       f ν1 ds
                                A ∂x1                ∂A


dove ν = (ν1 , ν2 ) è il versore normale esterno alla frontiera di A.




          L.Freddi                                                  April 27, 2026   2 / 23
Formule di Gauss-Green
Dimostriamo che se A è normale rispetto all’asse x1 allora vale la formula
                         Z                  Z
                            ∂f
                                dx1 dx2 =        f ν2 ds,
                          A ∂x2               ∂A

Siccome A è normale rispetto all’asse x1 , esistono α, β ∈ C 1 ([a, b]) tali che
              A = {(x1 , x2 ) ∈ R2 : a ≤ x1 ≤ b, α(x1 ) ≤ y ≤ β(x1 )}
Allora si ha
                        Z b                 p                              Z b
                                                  1 + β ′ (x1 )2
   Z
        f ν2 ds     =         f (x1 , β(x1 )) p                    dx1 −         f (x1 , α(x1 )) dx1
    ∂A                   a                        1 + β ′ (x1 )2            a
                        Z b
                                                                
                    =          f (x1 , β(x1 )) − f (x1 , α(x1 )) dx1
                         a
                        Z b  Z β(x1 )
                                          ∂f     
                    =                         dx2 dx1
                         a       α(x1 )   ∂x2
                        Z
                           ∂f
                    =          dx1 dx2
                         A ∂x2


         L.Freddi                                                                 April 27, 2026       3 / 23
Teorema della divergenza
Esercizio (Teorema della divergenza su un insieme normale)
Sia A un sottoinsieme di R2 normale rispetto a entrambi gli assi coordinati e sia
F ∈ C 1 (B; R2 ) con B aperto di R2 contenente A. Allora vale la formula
                 Z                          Z
                     ∂F1    ∂F2 
                         +        dx1 dx2 =     F1 ν1 + F2 ν2 ds,
                  A ∂x1     ∂x2              ∂A

dove ν è il versore normale esterno alla frontiera di A.




         L.Freddi                                              April 27, 2026   4 / 23
Teorema della divergenza
Esercizio (Teorema della divergenza su un insieme normale)
Sia A un sottoinsieme di R2 normale rispetto a entrambi gli assi coordinati e sia
F ∈ C 1 (B; R2 ) con B aperto di R2 contenente A. Allora vale la formula
                 Z                          Z
                     ∂F1    ∂F2 
                         +        dx1 dx2 =     F1 ν1 + F2 ν2 ds,
                  A ∂x1     ∂x2              ∂A

dove ν è il versore normale esterno alla frontiera di A.
Dimostrazione Basta considerare le formule di Gauss-Green
                     Z                  Z
                         ∂f
                             dx1 dx2 =       f ν1 ds
                      A ∂x1               ∂A
                     Z                  Z
                         ∂f
                             dx1 dx2 =       f ν2 ds
                      A ∂x2               ∂A
e poi sommarle prendendo f = F1 nella prima e f = F2 nella seconda.



         L.Freddi                                              April 27, 2026   4 / 23
Teorema della divergenza
Esercizio (Teorema della divergenza su un insieme normale)
Sia A un sottoinsieme di R2 normale rispetto a entrambi gli assi coordinati e sia
F ∈ C 1 (B; R2 ) con B aperto di R2 contenente A. Allora vale la formula
                 Z                          Z
                     ∂F1    ∂F2 
                         +        dx1 dx2 =     F1 ν1 + F2 ν2 ds,
                  A ∂x1     ∂x2              ∂A

dove ν è il versore normale esterno alla frontiera di A.
Dimostrazione Basta considerare le formule di Gauss-Green
                     Z                  Z
                         ∂f
                             dx1 dx2 =       f ν1 ds
                      A ∂x1               ∂A
                     Z                  Z
                         ∂f
                             dx1 dx2 =       f ν2 ds
                      A ∂x2               ∂A
e poi sommarle prendendo f = F1 nella prima e f = F2 nella seconda.

Il teorema si estende facilmente alle unioni finite di insiemi normali rispetto ad
entrambi gli assi.
         L.Freddi                                                 April 27, 2026     4 / 23
Aperti regolari
Definizione
Un aperto limitato A di Rn si dice con frontiera regolare (o brevemente aperto
regolare) se esiste una funzione G ∈ C 1 (Rn ) tale che
  1   A = {x ∈ Rn : G(x) < 0};
  2   ∂A = {x ∈ Rn : G(x) = 0};
  3   ∇G(x) ̸= 0 ∀ x ∈ ∂A.

Ad esempio




         L.Freddi                                             April 27, 2026     5 / 23
Aperti regolari
Definizione
Un aperto limitato A di Rn si dice con frontiera regolare (o brevemente aperto
regolare) se esiste una funzione G ∈ C 1 (Rn ) tale che
  1   A = {x ∈ Rn : G(x) < 0};
  2   ∂A = {x ∈ Rn : G(x) = 0};
  3   ∇G(x) ̸= 0 ∀ x ∈ ∂A.

Ad esempio
      la palla {(x, y, z) ∈ R3 : x2 + y 2 + z 2 < 1} è un aperto regolare di R3




          L.Freddi                                               April 27, 2026    5 / 23
Aperti regolari
Definizione
Un aperto limitato A di Rn si dice con frontiera regolare (o brevemente aperto
regolare) se esiste una funzione G ∈ C 1 (Rn ) tale che
  1   A = {x ∈ Rn : G(x) < 0};
  2   ∂A = {x ∈ Rn : G(x) = 0};
  3   ∇G(x) ̸= 0 ∀ x ∈ ∂A.

Ad esempio
      la palla {(x, y, z) ∈ R3 : x2 + y 2 + z 2 < 1} è un aperto regolare di R3
      il quadrato {(x, y) ∈ R2 : |x| + |y| < 1} è aperto ma non è regolare




          L.Freddi                                               April 27, 2026    5 / 23
Aperti regolari e versore normale esterno
Inoltre,
     per il teorema della funzioni implicite, se A è regolare allora ∂A è una
     ipersuperficie regolare (una curva se n = 2, una superficie se n = 3)




           L.Freddi                                               April 27, 2026   6 / 23
Aperti regolari e versore normale esterno
Inoltre,
     per il teorema della funzioni implicite, se A è regolare allora ∂A è una
     ipersuperficie regolare (una curva se n = 2, una superficie se n = 3)
     la frontiera di A è una ipersuperficie di livello di G




           L.Freddi                                               April 27, 2026   6 / 23
Aperti regolari e versore normale esterno
Inoltre,
     per il teorema della funzioni implicite, se A è regolare allora ∂A è una
     ipersuperficie regolare (una curva se n = 2, una superficie se n = 3)
     la frontiera di A è una ipersuperficie di livello di G
     il gradiente di G è ortogonale alle ipersuperfici di livello (già visto nel caso
     n = 2; dimostrarlo per esercizio nel caso n = 3),




           L.Freddi                                                 April 27, 2026    6 / 23
Aperti regolari e versore normale esterno
Inoltre,
     per il teorema della funzioni implicite, se A è regolare allora ∂A è una
     ipersuperficie regolare (una curva se n = 2, una superficie se n = 3)
     la frontiera di A è una ipersuperficie di livello di G
     il gradiente di G è ortogonale alle ipersuperfici di livello (già visto nel caso
     n = 2; dimostrarlo per esercizio nel caso n = 3),
Allora
                                             ∇G(x)
                                   ν(x) =
                                            |∇G(x)|
è il versore normale a ∂A nel punto x.




           L.Freddi                                                 April 27, 2026    6 / 23
Aperti regolari e versore normale esterno
Inoltre,
     per il teorema della funzioni implicite, se A è regolare allora ∂A è una
     ipersuperficie regolare (una curva se n = 2, una superficie se n = 3)
     la frontiera di A è una ipersuperficie di livello di G
     il gradiente di G è ortogonale alle ipersuperfici di livello (già visto nel caso
     n = 2; dimostrarlo per esercizio nel caso n = 3),
Allora
                                             ∇G(x)
                                   ν(x) =
                                            |∇G(x)|
è il versore normale a ∂A nel punto x.
Siccome ∇G(x) indica la direzione di massima pendenza del grafico di G, allora,
per la 1




           L.Freddi                                                 April 27, 2026    6 / 23
Aperti regolari e versore normale esterno
Inoltre,
     per il teorema della funzioni implicite, se A è regolare allora ∂A è una
     ipersuperficie regolare (una curva se n = 2, una superficie se n = 3)
     la frontiera di A è una ipersuperficie di livello di G
     il gradiente di G è ortogonale alle ipersuperfici di livello (già visto nel caso
     n = 2; dimostrarlo per esercizio nel caso n = 3),
Allora
                                             ∇G(x)
                                   ν(x) =
                                            |∇G(x)|
è il versore normale a ∂A nel punto x.
Siccome ∇G(x) indica la direzione di massima pendenza del grafico di G, allora,
per la 1
     il versore ν è orientato verso l’esterno di ∂A,




           L.Freddi                                                 April 27, 2026    6 / 23
Aperti regolari e versore normale esterno
Inoltre,
     per il teorema della funzioni implicite, se A è regolare allora ∂A è una
     ipersuperficie regolare (una curva se n = 2, una superficie se n = 3)
     la frontiera di A è una ipersuperficie di livello di G
     il gradiente di G è ortogonale alle ipersuperfici di livello (già visto nel caso
     n = 2; dimostrarlo per esercizio nel caso n = 3),
Allora
                                             ∇G(x)
                                   ν(x) =
                                            |∇G(x)|
è il versore normale a ∂A nel punto x.
Siccome ∇G(x) indica la direzione di massima pendenza del grafico di G, allora,
per la 1
     il versore ν è orientato verso l’esterno di ∂A,
ed è perciò detto versore normale esterno alla frontiera di A nel punto x.



           L.Freddi                                                 April 27, 2026    6 / 23
Teorema della divergenza
Definizione
Sia A un aperto di Rn . Dato un campo vettoriale F ∈ C 1 (A, Rn ), si definisce
divergenza di W la funzione scalare
                                         n
                                         X ∂Fi
                                divF =
                                         i=1
                                               ∂xi




         L.Freddi                                              April 27, 2026     7 / 23
Teorema della divergenza
Definizione
Sia A un aperto di Rn . Dato un campo vettoriale F ∈ C 1 (A, Rn ), si definisce
divergenza di W la funzione scalare
                                            n
                                            X ∂Fi
                                 divF =
                                            i=1
                                                  ∂xi

Si usa anche il simbolo alternativo ∇ · F




         L.Freddi                                              April 27, 2026     7 / 23
Teorema della divergenza
Definizione
Sia A un aperto di Rn . Dato un campo vettoriale F ∈ C 1 (A, Rn ), si definisce
divergenza di W la funzione scalare
                                            n
                                            X ∂Fi
                                  divF =
                                            i=1
                                                  ∂xi

Si usa anche il simbolo alternativo ∇ · F

Teorema (della divergenza per gli aperti regolari)
Sia A un aperto regolare di Rn e sia F ∈ C 1 (B, Rn ) con B aperto di Rn
contenente la chiusura di A. Allora vale la formula
                      Z                 Z
                          divF (x) dx =       F (x) · ν(x) dσ,
                        A                   ∂A

dove ν è il versore normale esterno alla frontiera di A in x.


         L.Freddi                                                April 27, 2026   7 / 23
Teorema della divergenza
Definizione
Sia A un aperto di Rn . Dato un campo vettoriale F ∈ C 1 (A, Rn ), si definisce
divergenza di W la funzione scalare
                                            n
                                            X ∂Fi
                                  divF =
                                            i=1
                                                  ∂xi

Si usa anche il simbolo alternativo ∇ · F

Teorema (della divergenza per gli aperti regolari)
Sia A un aperto regolare di Rn e sia F ∈ C 1 (B, Rn ) con B aperto di Rn
contenente la chiusura di A. Allora vale la formula
                      Z                 Z
                          divF (x) dx =       F (x) · ν(x) dσ,
                        A                   ∂A

dove ν è il versore normale esterno alla frontiera di A in x.
Dimostrazione Fusco, Marcellini, Sbordone. Analisi Matematica due
         L.Freddi                                                April 27, 2026   7 / 23
Teorema della divergenza e formule di Gauss-Green
Osservazioni:
     nel caso n = 2, prendendo campi vettoriali con una delle due componenti
     uguale a zero, si ottengono le formule
                             Z                 Z
                                ∂f
                                     dx1 dx2 =     f ν1 ds,
                              A ∂x1             ∂A
                             Z                 Z
                                ∂f
                                     dx1 dx2 =     f ν2 ds.
                              A ∂x2             ∂A

     che valgono per ogni f ∈ C 1 (B)




         L.Freddi                                            April 27, 2026    8 / 23
Teorema della divergenza e formule di Gauss-Green
Osservazioni:
     nel caso n = 2, prendendo campi vettoriali con una delle due componenti
     uguale a zero, si ottengono le formule di Gauss-Green
                             Z                 Z
                                ∂f
                                     dx1 dx2 =     f ν1 ds,
                              A ∂x1             ∂A
                             Z                 Z
                                ∂f
                                     dx1 dx2 =     f ν2 ds.
                              A ∂x2             ∂A

     che valgono per ogni f ∈ C 1 (B)




         L.Freddi                                            April 27, 2026    8 / 23
Teorema della divergenza e formule di Gauss-Green
Osservazioni:
     nel caso n = 2, prendendo campi vettoriali con una delle due componenti
     uguale a zero, si ottengono le formule di Gauss-Green
                             Z                 Z
                                ∂f
                                     dx1 dx2 =     f ν1 ds,
                              A ∂x1             ∂A
                             Z                 Z
                                ∂f
                                     dx1 dx2 =     f ν2 ds.
                              A ∂x2             ∂A

     che valgono per ogni f ∈ C 1 (B)
     nel teorema della divergenza
                       Z                     Z
                           divF (x) dx   =         F (x) · ν(x) dσ
                        A                     ∂A
          divergenza totale di F in A    =   flusso totale di F attraverso ∂A




         L.Freddi                                                April 27, 2026   8 / 23
Teorema della divergenza e formule di Gauss-Green
Osservazioni:
     nel caso n = 2, prendendo campi vettoriali con una delle due componenti
     uguale a zero, si ottengono le formule di Gauss-Green
                             Z                 Z
                                ∂f
                                     dx1 dx2 =     f ν1 ds,
                              A ∂x1             ∂A
                             Z                 Z
                                ∂f
                                     dx1 dx2 =     f ν2 ds.
                              A ∂x2             ∂A

     che valgono per ogni f ∈ C 1 (B)
     nel teorema della divergenza
                       Z                      Z
                           divF (x) dx    =          F (x) · ν(x) dσ
                         A                      ∂A
          divergenza totale di F in A     =   flusso totale di F attraverso ∂A
     se il flusso totale attraverso la frontiera è nullo, cioè il flusso uscente
     (positivo) bilancia quello entrante (negativo), allora la divergenza totale è
     nulla, cioè, complessivamente il campo “non diverge da A”

         L.Freddi                                                  April 27, 2026     8 / 23
Potenziale vettore
I campi a divergenza nulla (divF = 0) sono detti solenoidali.




         L.Freddi                                               April 27, 2026   9 / 23
Potenziale vettore
I campi a divergenza nulla (divF = 0) sono detti solenoidali. Esempio: il campo
magnetico generato da un solenoide (bobina) percorso da corrente.




         L.Freddi                                            April 27, 2026   9 / 23
Potenziale vettore
I campi a divergenza nulla (divF = 0) sono detti solenoidali. Esempio: il campo
magnetico generato da un solenoide (bobina) percorso da corrente.
Esercizio
Sia Ω un aperto di R3 e sia A ∈ C 2 (Ω; R3 ) un campo vettoriale. Allora
  1   B = ∇ × A è un campo vettoriale di classe C 1 (Ω; R3 )
  2   ∇ · B = 0 (cioè B è solenoidale)
  3   il flusso di B attraverso la frontiera di qualunque aperto regolare è nullo




          L.Freddi                                                April 27, 2026     9 / 23
Potenziale vettore
I campi a divergenza nulla (divF = 0) sono detti solenoidali. Esempio: il campo
magnetico generato da un solenoide (bobina) percorso da corrente.
Esercizio
Sia Ω un aperto di R3 e sia A ∈ C 2 (Ω; R3 ) un campo vettoriale. Allora
  1   B = ∇ × A è un campo vettoriale di classe C 1 (Ω; R3 )
  2   ∇ · B = 0 (cioè B è solenoidale)
  3   il flusso di B attraverso la frontiera di qualunque aperto regolare è nullo
  4   A è detto un potenziale vettore di B




          L.Freddi                                                April 27, 2026     9 / 23
Potenziale vettore
I campi a divergenza nulla (divF = 0) sono detti solenoidali. Esempio: il campo
magnetico generato da un solenoide (bobina) percorso da corrente.
Esercizio
Sia Ω un aperto di R3 e sia A ∈ C 2 (Ω; R3 ) un campo vettoriale. Allora
  1   B = ∇ × A è un campo vettoriale di classe C 1 (Ω; R3 )
  2   ∇ · B = 0 (cioè B è solenoidale)
  3   il flusso di B attraverso la frontiera di qualunque aperto regolare è nullo
  4   A è detto un potenziale vettore di B (per distinguerlo dal potenziale scalare
      che sarebbe una funzione scalare V tale che B = ∇V )




          L.Freddi                                                April 27, 2026     9 / 23
Campi conservativi, solenoidali e armonici
Un campo F di classe C 1 si dice
     campo gradiente (o conservativo) se ∃ un potenz. scalare V t.c. F = ∇V .




        L.Freddi                                            April 27, 2026   10 / 23
Campi conservativi, solenoidali e armonici
Un campo F di classe C 1 si dice
     campo gradiente (o conservativo) se ∃ un potenz. scalare V t.c. F = ∇V .
     Proprietà:




        L.Freddi                                            April 27, 2026   10 / 23
Campi conservativi, solenoidali e armonici
Un campo F di classe C 1 si dice
     campo gradiente (o conservativo) se ∃ un potenz. scalare V t.c. F = ∇V .
     Proprietà:
       ▶ F campo gradiente =⇒ ∇ × F = 0 (irrotazionale)




        L.Freddi                                            April 27, 2026   10 / 23
Campi conservativi, solenoidali e armonici
Un campo F di classe C 1 si dice
     campo gradiente (o conservativo) se ∃ un potenz. scalare V t.c. F = ∇V .
     Proprietà:
       ▶ F campo gradiente =⇒ ∇ × F = 0 (irrotazionale)

     Esempi:
       ▶ il campo gravitazionale g o il il campo elettrico E




        L.Freddi                                            April 27, 2026   10 / 23
Campi conservativi, solenoidali e armonici
Un campo F di classe C 1 si dice
     campo gradiente (o conservativo) se ∃ un potenz. scalare V t.c. F = ∇V .
     Proprietà:
       ▶ F campo gradiente =⇒ ∇ × F = 0 (irrotazionale)

     Esempi:
       ▶ il campo gravitazionale g o il il campo elettrico E

     campo rotore se ∃ un potenz. vettore A t.c. F = ∇ × A.




        L.Freddi                                              April 27, 2026   10 / 23
Campi conservativi, solenoidali e armonici
Un campo F di classe C 1 si dice
     campo gradiente (o conservativo) se ∃ un potenz. scalare V t.c. F = ∇V .
     Proprietà:
       ▶ F campo gradiente =⇒ ∇ × F = 0 (irrotazionale)

     Esempi:
       ▶ il campo gravitazionale g o il il campo elettrico E

     campo rotore se ∃ un potenz. vettore A t.c. F = ∇ × A.
     Proprietà:
       ▶ F campo rotore =⇒ ∇ · F = 0 (solenoidale)




        L.Freddi                                              April 27, 2026   10 / 23
Campi conservativi, solenoidali e armonici
Un campo F di classe C 1 si dice
     campo gradiente (o conservativo) se ∃ un potenz. scalare V t.c. F = ∇V .
     Proprietà:
       ▶ F campo gradiente =⇒ ∇ × F = 0 (irrotazionale)

     Esempi:
       ▶ il campo gravitazionale g o il il campo elettrico E

     campo rotore se ∃ un potenz. vettore A t.c. F = ∇ × A.
     Proprietà:
       ▶ F campo rotore =⇒ ∇ · F = 0 (solenoidale)

     Esempi:




        L.Freddi                                              April 27, 2026   10 / 23
Campi conservativi, solenoidali e armonici
Un campo F di classe C 1 si dice
     campo gradiente (o conservativo) se ∃ un potenz. scalare V t.c. F = ∇V .
     Proprietà:
       ▶ F campo gradiente =⇒ ∇ × F = 0 (irrotazionale)

     Esempi:
       ▶ il campo gravitazionale g o il il campo elettrico E

     campo rotore se ∃ un potenz. vettore A t.c. F = ∇ × A.
     Proprietà:
       ▶ F campo rotore =⇒ ∇ · F = 0 (solenoidale)

     Esempi:
       ▶ il campo di induzione magnetica B (generato da un solenoide)




        L.Freddi                                            April 27, 2026   10 / 23
Campi conservativi, solenoidali e armonici
Un campo F di classe C 1 si dice
     campo gradiente (o conservativo) se ∃ un potenz. scalare V t.c. F = ∇V .
     Proprietà:
       ▶ F campo gradiente =⇒ ∇ × F = 0 (irrotazionale)

     Esempi:
       ▶ il campo gravitazionale g o il il campo elettrico E

     campo rotore se ∃ un potenz. vettore A t.c. F = ∇ × A.
     Proprietà:
       ▶ F campo rotore =⇒ ∇ · F = 0 (solenoidale)

     Esempi:
       ▶ il campo di induzione magnetica B (generato da un solenoide)

       ▶ il campo di velocità u di un fluido incomprimibile




        L.Freddi                                            April 27, 2026   10 / 23
Campi conservativi, solenoidali e armonici
Un campo F di classe C 1 si dice
     campo gradiente (o conservativo) se ∃ un potenz. scalare V t.c. F = ∇V .
     Proprietà:
       ▶ F campo gradiente =⇒ ∇ × F = 0 (irrotazionale)

     Esempi:
       ▶ il campo gravitazionale g o il il campo elettrico E

     campo rotore se ∃ un potenz. vettore A t.c. F = ∇ × A.
     Proprietà:
       ▶ F campo rotore =⇒ ∇ · F = 0 (solenoidale)

     Esempi:
       ▶ il campo di induzione magnetica B (generato da un solenoide)

       ▶ il campo di velocità u di un fluido incomprimibile

     armonico se è sia gradiente che rotore ( =⇒ solenoidale e conservativo).




        L.Freddi                                              April 27, 2026     10 / 23
Campi conservativi, solenoidali e armonici
Un campo F di classe C 1 si dice
     campo gradiente (o conservativo) se ∃ un potenz. scalare V t.c. F = ∇V .
     Proprietà:
       ▶ F campo gradiente =⇒ ∇ × F = 0 (irrotazionale)

     Esempi:
       ▶ il campo gravitazionale g o il il campo elettrico E

     campo rotore se ∃ un potenz. vettore A t.c. F = ∇ × A.
     Proprietà:
       ▶ F campo rotore =⇒ ∇ · F = 0 (solenoidale)

     Esempi:
       ▶ il campo di induzione magnetica B (generato da un solenoide)

       ▶ il campo di velocità u di un fluido incomprimibile

     armonico se è sia gradiente che rotore ( =⇒ solenoidale e conservativo).
     Esempi:



        L.Freddi                                              April 27, 2026     10 / 23
Campi conservativi, solenoidali e armonici
Un campo F di classe C 1 si dice
     campo gradiente (o conservativo) se ∃ un potenz. scalare V t.c. F = ∇V .
     Proprietà:
       ▶ F campo gradiente =⇒ ∇ × F = 0 (irrotazionale)

     Esempi:
       ▶ il campo gravitazionale g o il il campo elettrico E

     campo rotore se ∃ un potenz. vettore A t.c. F = ∇ × A.
     Proprietà:
       ▶ F campo rotore =⇒ ∇ · F = 0 (solenoidale)

     Esempi:
       ▶ il campo di induzione magnetica B (generato da un solenoide)

       ▶ il campo di velocità u di un fluido incomprimibile

     armonico se è sia gradiente che rotore ( =⇒ solenoidale e conservativo).
     Esempi:
       ▶ il campo elettrico E in regioni dello spazio prive di cariche




        L.Freddi                                              April 27, 2026     10 / 23
Campi conservativi, solenoidali e armonici
Un campo F di classe C 1 si dice
     campo gradiente (o conservativo) se ∃ un potenz. scalare V t.c. F = ∇V .
     Proprietà:
       ▶ F campo gradiente =⇒ ∇ × F = 0 (irrotazionale)

     Esempi:
       ▶ il campo gravitazionale g o il il campo elettrico E

     campo rotore se ∃ un potenz. vettore A t.c. F = ∇ × A.
     Proprietà:
       ▶ F campo rotore =⇒ ∇ · F = 0 (solenoidale)

     Esempi:
       ▶ il campo di induzione magnetica B (generato da un solenoide)

       ▶ il campo di velocità u di un fluido incomprimibile

     armonico se è sia gradiente che rotore ( =⇒ solenoidale e conservativo).
     Esempi:
       ▶ il campo elettrico E in regioni dello spazio prive di cariche

     Proprietà:
        L.Freddi                                              April 27, 2026     10 / 23
Campi conservativi, solenoidali e armonici
Un campo F di classe C 1 si dice
     campo gradiente (o conservativo) se ∃ un potenz. scalare V t.c. F = ∇V .
     Proprietà:
       ▶ F campo gradiente =⇒ ∇ × F = 0 (irrotazionale)

     Esempi:
       ▶ il campo gravitazionale g o il il campo elettrico E

     campo rotore se ∃ un potenz. vettore A t.c. F = ∇ × A.
     Proprietà:
       ▶ F campo rotore =⇒ ∇ · F = 0 (solenoidale)

     Esempi:
       ▶ il campo di induzione magnetica B (generato da un solenoide)

       ▶ il campo di velocità u di un fluido incomprimibile

     armonico se è sia gradiente che rotore ( =⇒ solenoidale e conservativo).
     Esempi:
       ▶ il campo elettrico E in regioni dello spazio prive di cariche

     Proprietà: F armonico =⇒ F = ∇V e ∇ · ∇V = 0
        L.Freddi                                              April 27, 2026     10 / 23
Funzioni armoniche
I potenziali scalari V dei campi armonici sono detti funzioni armoniche e
soddisfano l’equazione di Laplace
                                  div(∇V ) = 0




         L.Freddi                                              April 27, 2026   11 / 23
Funzioni armoniche
I potenziali scalari V dei campi armonici sono detti funzioni armoniche e
soddisfano l’equazione di Laplace
                                   div(∇V ) = 0

che si può anche scrivere
                                      ∆V = 0
dove
                                          ∂2   ∂2 ∂2
                         ∆ := ∇ · ∇ =       2
                                              + 2+ 2
                                          ∂x   ∂y ∂z
è l’operatore di Laplace o Laplaciano.




         L.Freddi                                              April 27, 2026   11 / 23
Funzioni armoniche
I potenziali scalari V dei campi armonici sono detti funzioni armoniche e
soddisfano l’equazione di Laplace
                                   div(∇V ) = 0

che si può anche scrivere
                                      ∆V = 0
dove
                                          ∂2   ∂2 ∂2
                         ∆ := ∇ · ∇ =       2
                                              + 2+ 2
                                          ∂x   ∂y ∂z
è l’operatore di Laplace o Laplaciano.
Esercizio
Dimostrare che la funzione f (x, y) = ekx sen(ky) è armonica.




         L.Freddi                                                April 27, 2026   11 / 23
Teorema della divergenza
Il teorema della divergenza
     vale anche in aperti A meno regolari,




         L.Freddi                            April 27, 2026   12 / 23
Teorema della divergenza
Il teorema della divergenza
     vale anche in aperti A meno regolari,
     purché esista il vettore normale alla frontiera con l’eccezione di un insieme
     abbastanza piccolo di punti singolari tale da non costituire un problema ai
     fini dell’integrazione




         L.Freddi                                                April 27, 2026   12 / 23
Teorema della divergenza
Il teorema della divergenza
     vale anche in aperti A meno regolari,
     purché esista il vettore normale alla frontiera con l’eccezione di un insieme
     abbastanza piccolo di punti singolari tale da non costituire un problema ai
     fini dell’integrazione
        ▶ ad esempio, se A è la parte interna di un insieme decomponibile

           nell’unione finita di insiemi normali (in tal caso l’insieme dei punti
           singolari è finito).




         L.Freddi                                                April 27, 2026   12 / 23
Teorema della divergenza
Il teorema della divergenza
     vale anche in aperti A meno regolari,
     purché esista il vettore normale alla frontiera con l’eccezione di un insieme
     abbastanza piccolo di punti singolari tale da non costituire un problema ai
     fini dell’integrazione
        ▶ ad esempio, se A è la parte interna di un insieme decomponibile

           nell’unione finita di insiemi normali (in tal caso l’insieme dei punti
           singolari è finito).
     ma, in generale, questi concetti trovano la loro formalizzazione nella teoria
     della misura e nell’integrale di Lebesgue




         L.Freddi                                                April 27, 2026   12 / 23
Teorema della divergenza
Il teorema della divergenza
     vale anche in aperti A meno regolari,
     purché esista il vettore normale alla frontiera con l’eccezione di un insieme
     abbastanza piccolo di punti singolari tale da non costituire un problema ai
     fini dell’integrazione
        ▶ ad esempio, se A è la parte interna di un insieme decomponibile

           nell’unione finita di insiemi normali (in tal caso l’insieme dei punti
           singolari è finito).
     ma, in generale, questi concetti trovano la loro formalizzazione nella teoria
     della misura e nell’integrale di Lebesgue
     Ennio De Giorgi, ha dimostrato nella prima metà degli anni ’60 che la più
     ampia classe di insiemi A per cui vale il teorema della divergenza, è quella
     degli insiemi di perimetro finito (che comprende, ad esempio, i sottoinsiemi
     aperti del piano la cui frontiera è una curva rettificabile)




         L.Freddi                                                April 27, 2026   12 / 23
Teorema della divergenza
Il teorema della divergenza
     vale anche in aperti A meno regolari,
     purché esista il vettore normale alla frontiera con l’eccezione di un insieme
     abbastanza piccolo di punti singolari tale da non costituire un problema ai
     fini dell’integrazione
        ▶ ad esempio, se A è la parte interna di un insieme decomponibile

           nell’unione finita di insiemi normali (in tal caso l’insieme dei punti
           singolari è finito).
     ma, in generale, questi concetti trovano la loro formalizzazione nella teoria
     della misura e nell’integrale di Lebesgue
     Ennio De Giorgi, ha dimostrato nella prima metà degli anni ’60 che la più
     ampia classe di insiemi A per cui vale il teorema della divergenza, è quella
     degli insiemi di perimetro finito (che comprende, ad esempio, i sottoinsiemi
     aperti del piano la cui frontiera è una curva rettificabile)
     gli insiemi di perimetro finito sono stati introdotti negli anni ’50 da un’altro
     grande matematico italiano del ’900, Renato Caccioppoli.

         L.Freddi                                                 April 27, 2026   12 / 23
Frontiere orientate
Siano
    A un aperto regolare
    φ : [a, b] → R2 una curva C 1 regolare e chiusa con φ([a, b]) = ∂A
    ν(t) il versore normale esterno a ∂A nel punto φ(t)




        L.Freddi                                             April 27, 2026   13 / 23
Frontiere orientate
Siano
       A un aperto regolare
       φ : [a, b] → R2 una curva C 1 regolare e chiusa con φ([a, b]) = ∂A
       ν(t) il versore normale esterno a ∂A nel punto φ(t)
La curva φ assegna un’orientazione a ∂A, indicata dal verso di φ′ .
(                               f ( t)                              (
    x = cos t                            n( t)            n( t)      x = cos t
                                A                 A
    y = sen t                                                        y = − sen t
                                                        f ( t)

φ′ (t) = (− sen t, cos t)                                         φ′ (t) = (− sen t, − cos t)




           L.Freddi                                                    April 27, 2026   13 / 23
Frontiere orientate
Siano
       A un aperto regolare
       φ : [a, b] → R2 una curva C 1 regolare e chiusa con φ([a, b]) = ∂A
       ν(t) il versore normale esterno a ∂A nel punto φ(t)
La curva φ assegna un’orientazione a ∂A, indicata dal verso di φ′ .
(                               f ( t)                              (
    x = cos t                            n( t)            n( t)      x = cos t
                                A                  A
    y = sen t                                                        y = − sen t
                                                        f ( t)

φ′ (t) = (− sen t, cos t)                                         φ′ (t) = (− sen t, − cos t)

Poiché ν(t) e φ′ (t) sono ortogonali, detto θ l’angolo contato in senso antiorario
da ν(t) verso φ′ (t), si possono verificare solo due casi
          π
     θ=
          2
            π
     θ=−
             2
           L.Freddi                                                    April 27, 2026   13 / 23
Frontiere orientate
Siano
       A un aperto regolare
       φ : [a, b] → R2 una curva C 1 regolare e chiusa con φ([a, b]) = ∂A
       ν(t) il versore normale esterno a ∂A nel punto φ(t)
La curva φ assegna un’orientazione a ∂A, indicata dal verso di φ′ .
(                               f ( t)                              (
    x = cos t                            n( t)            n( t)      x = cos t
                                A                  A
    y = sen t                                                        y = − sen t
                                                        f ( t)

φ′ (t) = (− sen t, cos t)                                         φ′ (t) = (− sen t, − cos t)

Poiché ν(t) e φ′ (t) sono ortogonali, detto θ l’angolo contato in senso antiorario
da ν(t) verso φ′ (t), si possono verificare solo due casi
          π
     θ = orientazione positiva
          2
            π
     θ=−
             2
           L.Freddi                                                    April 27, 2026   13 / 23
Frontiere orientate
Siano
       A un aperto regolare
       φ : [a, b] → R2 una curva C 1 regolare e chiusa con φ([a, b]) = ∂A
       ν(t) il versore normale esterno a ∂A nel punto φ(t)
La curva φ assegna un’orientazione a ∂A, indicata dal verso di φ′ .
(                               f ( t)                              (
    x = cos t                            n( t)            n( t)      x = cos t
                                A                  A
    y = sen t                                                        y = − sen t
                                                        f ( t)

φ′ (t) = (− sen t, cos t)                                         φ′ (t) = (− sen t, − cos t)

Poiché ν(t) e φ′ (t) sono ortogonali, detto θ l’angolo contato in senso antiorario
da ν(t) verso φ′ (t), si possono verificare solo due casi
          π
     θ = orientazione positiva
          2
            π
     θ = − orientazione negativa
             2
           L.Freddi                                                    April 27, 2026   13 / 23
Frontiere orientate
Definizione
Si dice che φ orienta ∂A positivamente se in ogni punto di ∂A l’angolo formato
dal versore normale esterno con il vettore tangente alla curva è π/2.

                     f ( t)

                              n( t)                             n( t)

                    A                                   A

                                                              f ( t)




        L.Freddi                                             April 27, 2026   14 / 23
Frontiere orientate
Definizione
Si dice che φ orienta ∂A positivamente se in ogni punto di ∂A l’angolo formato
dal versore normale esterno con il vettore tangente alla curva è π/2.

                       f ( t)

                                n( t)                           n( t)

                      A                                 A

                                                              f ( t)




La frontiera di A verrà indicata con
     ∂A+ se orientata positivamente
     ∂A− se orientata negativamente




         L.Freddi                                            April 27, 2026   14 / 23
Frontiere orientate
Definizione
Si dice che φ orienta ∂A positivamente se in ogni punto di ∂A l’angolo formato
dal versore normale esterno con il vettore tangente alla curva è π/2.

                       f ( t)

                                n( t)                             n( t)

                      A                                    A

                                                                f ( t)




La frontiera di A verrà indicata con
     ∂A+ se orientata positivamente
     ∂A− se orientata negativamente

Intuitivamente, ∂A è orientata positivamente se percorrendola si lascia A alla
propria sinistra.



         L.Freddi                                               April 27, 2026    14 / 23
Ascissa curvilinea




      L.Freddi       April 27, 2026   15 / 23
Ascissa curvilinea
Esercizio
Sia φ : [a, b] → Rn una curva regolare. Dimostrare che il cambiamento di
parametro                           Z    t
                                s=           |φ′ (τ )| dτ,
                                     a

detto ascissa curvilinea, trasforma φ in una curva equivalente ψ : [0, ℓ(φ)] → Rn
tale che |ψ ′ (s)| = 1 per ogni s.




         L.Freddi                                              April 27, 2026   15 / 23
Ascissa curvilinea
Esercizio
Sia φ : [a, b] → Rn una curva regolare. Dimostrare che il cambiamento di
parametro                           Z           t
                                     s=             |φ′ (τ )| dτ,
                                            a

detto ascissa curvilinea, trasforma φ in una curva equivalente ψ : [0, ℓ(φ)] → Rn
tale che |ψ ′ (s)| = 1 per ogni s.
                     Rt
     Posto g(t) :=   a
                          |φ′ (τ )| dτ si ha che g ′ (t) = |φ′ (t)|.




         L.Freddi                                                      April 27, 2026   15 / 23
Ascissa curvilinea
Esercizio
Sia φ : [a, b] → Rn una curva regolare. Dimostrare che il cambiamento di
parametro                           Z           t
                                     s=             |φ′ (τ )| dτ,
                                            a

detto ascissa curvilinea, trasforma φ in una curva equivalente ψ : [0, ℓ(φ)] → Rn
tale che |ψ ′ (s)| = 1 per ogni s.
                     Rt
     Posto g(t) :=   a
                          |φ′ (τ )| dτ si ha che g ′ (t) = |φ′ (t)|.
     Poiché la curva è regolare si ha g ′ (t) > 0 per ogni t ∈ (a, b). Ne consegue
     che g è strettamente crescente, invertibile e con inversa continua. Allora la
     curva ψ = φ ◦ g −1 è equivalente a φ.




         L.Freddi                                                      April 27, 2026   15 / 23
Ascissa curvilinea
Esercizio
Sia φ : [a, b] → Rn una curva regolare. Dimostrare che il cambiamento di
parametro                           Z           t
                                     s=             |φ′ (τ )| dτ,
                                            a

detto ascissa curvilinea, trasforma φ in una curva equivalente ψ : [0, ℓ(φ)] → Rn
tale che |ψ ′ (s)| = 1 per ogni s.
                     Rt
     Posto g(t) :=   a
                          |φ′ (τ )| dτ si ha che g ′ (t) = |φ′ (t)|.
     Poiché la curva è regolare si ha g ′ (t) > 0 per ogni t ∈ (a, b). Ne consegue
     che g è strettamente crescente, invertibile e con inversa continua. Allora la
     curva ψ = φ ◦ g −1 è equivalente a φ.
     Poiché g(a) = 0, g(b) = ℓ(φ) allora ψ ha dominio [0, ℓ(φ)]. Inoltre
                                     φ′ (g −1 (s))     φ′ (g −1 (s))
                      |ψ ′ (s)| =                   =                 =1
                                     g ′ (g −1 (s))   |φ′ (g −1 (s))|


         L.Freddi                                                      April 27, 2026   15 / 23
Frontiere orientate
Supponiamo ora che φ orienti ∂A positivamente e che, inoltre, |φ′ (t)| = 1, cosa
sempre possibile parametrizzando la curva con l’ascissa curvilinea. Allora
                                 ν = (φ′2 , −φ′1 )




         L.Freddi                                             April 27, 2026   16 / 23
Frontiere orientate
Supponiamo ora che φ orienti ∂A positivamente e che, inoltre, |φ′ (t)| = 1, cosa
sempre possibile parametrizzando la curva con l’ascissa curvilinea. Allora
                                  ν = (φ′2 , −φ′1 )
Per definizione di integrale lungo una curva:
   Z              Z b
        f ν1 ds =     f (φ(t)) φ′2 (t) dt
    ∂A              a




         L.Freddi                                             April 27, 2026   16 / 23
Frontiere orientate
Supponiamo ora che φ orienti ∂A positivamente e che, inoltre, |φ′ (t)| = 1, cosa
sempre possibile parametrizzando la curva con l’ascissa curvilinea. Allora
                                   ν = (φ′2 , −φ′1 )
Per definizione di integrale lungo una curva:
   Z              Z b                     Z
                                ′
        f ν1 ds =     f (φ(t)) φ2 (t) dt = (0, f ) · dx
    ∂A              a                      φ




         L.Freddi                                             April 27, 2026   16 / 23
Frontiere orientate
Supponiamo ora che φ orienti ∂A positivamente e che, inoltre, |φ′ (t)| = 1, cosa
sempre possibile parametrizzando la curva con l’ascissa curvilinea. Allora
                                  ν = (φ′2 , −φ′1 )
Per definizione di integrale lungo una curva:
   Z              Z b                     Z               Z
                                ′
        f ν1 ds =     f (φ(t)) φ2 (t) dt = (0, f ) · dx =   f dx2
    ∂A              a                     φ              φ




         L.Freddi                                              April 27, 2026   16 / 23
Frontiere orientate
Supponiamo ora che φ orienti ∂A positivamente e che, inoltre, |φ′ (t)| = 1, cosa
sempre possibile parametrizzando la curva con l’ascissa curvilinea. Allora
                                 ν = (φ′2 , −φ′1 )
Per definizione di integrale lungo una curva:
   Z              Z b                     Z               Z         Z
                                ′
        f ν1 ds =     f (φ(t)) φ2 (t) dt = (0, f ) · dx =   f dx2 =             f dx2
    ∂A              a                    φ               φ             ∂A+




         L.Freddi                                              April 27, 2026           16 / 23
Frontiere orientate
Supponiamo ora che φ orienti ∂A positivamente e che, inoltre, |φ′ (t)| = 1, cosa
sempre possibile parametrizzando la curva con l’ascissa curvilinea. Allora
                                  ν = (φ′2 , −φ′1 )
Per definizione di integrale lungo una curva:
   Z              Z b                     Z               Z         Z
                                ′
        f ν1 ds =     f (φ(t)) φ2 (t) dt = (0, f ) · dx =   f dx2 =                 f dx2
    ∂A              a                     φ                  φ              ∂A+

e, analogamente,
     Z               Z b                        Z                       Z
                                   ′
         f ν2 ds = −     f (φ(t)) φ1 (t) dt = −         (f, 0) · dx =         f dx1
      ∂A                a                         ∂A+                   ∂A−




         L.Freddi                                                  April 27, 2026           16 / 23
Frontiere orientate
Supponiamo ora che φ orienti ∂A positivamente e che, inoltre, |φ′ (t)| = 1, cosa
sempre possibile parametrizzando la curva con l’ascissa curvilinea. Allora
                                   ν = (φ′2 , −φ′1 )
Per definizione di integrale lungo una curva:
   Z              Z b                     Z               Z         Z
                                ′
        f ν1 ds =     f (φ(t)) φ2 (t) dt = (0, f ) · dx =   f dx2 =                  f dx2
    ∂A              a                      φ                  φ              ∂A+

 e, analogamente,
      Z               Z b                        Z                       Z
                                    ′
          f ν2 ds = −     f (φ(t)) φ1 (t) dt = −         (f, 0) · dx =         f dx1
       ∂A               a                          ∂A+                   ∂A−
Quindi le formule di Gauss-Green si possono anche scrivere nella forma seguente
                 Z                  Z
                      ∂f
                         dx1 dx2 =       f dx2
                   A ∂x1             ∂A+
                 Z                    Z            Z
                      ∂f
                         dx1 dx2 = −       f dx1 =        f dx1 .
                   A ∂x2               ∂A+           ∂A−
in cui gli integrali a secondo membro sono del secondo tipo
         L.Freddi                                                   April 27, 2026           16 / 23
Misura di un insieme come integrale sulla frontiera
Un’utile applicazione delle formule di Gauss-Green
                          Z                 Z
                              ∂f
                                  dx1 dx2 =      f dx2
                           A ∂x1             ∂A+
                          Z                   Z
                              ∂f
                                  dx1 dx2 = −      f dx1
                           A ∂x2               ∂A+
si ottiene ponendo f = x1 nella prima formula e f = x2 nella seconda, e
ottenendo cosı̀ le relazioni
                         Z             Z             Z
               m(A) =        dx1 dx2 =    x1 dx2 = −       x2 dx1
                        A             ∂A+              ∂A+
o anche (prendendo la media)
                       Z
                     1
            m(A) =         (x1 dx2 − x2 dx1 )
                     2 ∂A+




         L.Freddi                                            April 27, 2026   17 / 23
Misura di un insieme come integrale sulla frontiera
Un’utile applicazione delle formule di Gauss-Green
                          Z                 Z
                              ∂f
                                  dx1 dx2 =      f dx2
                           A ∂x1             ∂A+
                          Z                   Z
                              ∂f
                                  dx1 dx2 = −      f dx1
                           A ∂x2               ∂A+
si ottiene ponendo f = x1 nella prima formula e f = x2 nella seconda, e
ottenendo cosı̀ le relazioni
                         Z             Z             Z
               m(A) =        dx1 dx2 =    x1 dx2 = −       x2 dx1
                        A             ∂A+              ∂A+
o anche (prendendo la media)
                       Z                          Z
                     1                          1
            m(A) =         (x1 dx2 − x2 dx1 ) =       det(x, dx).
                     2 ∂A+                      2 ∂A+




         L.Freddi                                            April 27, 2026   17 / 23
Misura di un insieme come integrale sulla frontiera
Un’utile applicazione delle formule di Gauss-Green
                          Z                 Z
                              ∂f
                                  dx1 dx2 =      f dx2
                           A ∂x1             ∂A+
                          Z                   Z
                              ∂f
                                  dx1 dx2 = −      f dx1
                           A ∂x2               ∂A+
si ottiene ponendo f = x1 nella prima formula e f = x2 nella seconda, e
ottenendo cosı̀ le relazioni
                         Z             Z             Z
               m(A) =        dx1 dx2 =    x1 dx2 = −       x2 dx1
                        A             ∂A+               ∂A+
o anche (prendendo la media)
                       Z                          Z
                     1                          1
            m(A) =         (x1 dx2 − x2 dx1 ) =       det(x, dx).
                     2 ∂A+                      2 ∂A+
 Queste formule riconducono il calcolo della misura dell’insieme A ad un integrale
su ∂A (anzichè su A)



         L.Freddi                                              April 27, 2026   17 / 23
Misura di un insieme come integrale sulla frontiera
Esempio
Calcoliamo l’area racchiusa dalla cardioide di equazione polare

                           ρ = 1 − cos θ, 0 ≤ θ ≤ 2π.




          L.Freddi                                                April 27, 2026   18 / 23
Misura di un insieme come integrale sulla frontiera
Esempio
Calcoliamo l’area racchiusa dalla cardioide di equazione polare

                           ρ = 1 − cos θ, 0 ≤ θ ≤ 2π.

Una rappresentazione parametrica di ∂A è
                       
                          x(θ) = ρ(θ) cos θ
                    φ:                      ,     θ ∈ [0, 2π].
                          y(t) = ρ(θ) sen θ




          L.Freddi                                                April 27, 2026   18 / 23
Misura di un insieme come integrale sulla frontiera
Esempio
Calcoliamo l’area racchiusa dalla cardioide di equazione polare

                           ρ = 1 − cos θ, 0 ≤ θ ≤ 2π.

Una rappresentazione parametrica di ∂A è
                       
                          x(θ) = ρ(θ) cos θ
                    φ:                      ,     θ ∈ [0, 2π].
                          y(t) = ρ(θ) sen θ
Si vede subito che φ orienta A positivamente.




          L.Freddi                                                April 27, 2026   18 / 23
Misura di un insieme come integrale sulla frontiera
Esempio
Calcoliamo l’area racchiusa dalla cardioide di equazione polare

                           ρ = 1 − cos θ, 0 ≤ θ ≤ 2π.

Una rappresentazione parametrica di ∂A è
                       
                          x(θ) = ρ(θ) cos θ
                    φ:                      ,     θ ∈ [0, 2π].
                          y(t) = ρ(θ) sen θ
Si vede subito che φ orienta A positivamente. Si ha allora
                                      1 2π
                Z                      Z
              1                                                       3
     m(A) =          (x dy − y dx) =       (1 + cos2 θ − 2 cos θ) dθ = π.
              2 ∂A+                   2 0                             2




          L.Freddi                                                April 27, 2026   18 / 23
Teorema del Rotore e formula di Stokes
Siano
    D un compatto di R2 chiusura di un aperto connesso
    φ : D → R3 una superficie regolare semplice
                                                                        ◦
    A un aperto di R2 con frontiera regolare e chiusura contenuta in D
    S := φ(A).




        L.Freddi                                            April 27, 2026   19 / 23
Teorema del Rotore e formula di Stokes
Siano
     D un compatto di R2 chiusura di un aperto connesso
     φ : D → R3 una superficie regolare semplice
                                                                         ◦
     A un aperto di R2 con frontiera regolare e chiusura contenuta in D
     S := φ(A).
Chiamiamo bordo di S, indicandolo con ∂S, l’immagine della frontiera di A
                                 ∂S = φ(∂A).




        L.Freddi                                             April 27, 2026   19 / 23
Teorema del Rotore e formula di Stokes
Siano
      D un compatto di R2 chiusura di un aperto connesso
      φ : D → R3 una superficie regolare semplice
                                                                          ◦
      A un aperto di R2 con frontiera regolare e chiusura contenuta in D
      S := φ(A).
Chiamiamo bordo di S, indicandolo con ∂S, l’immagine della frontiera di A
                                  ∂S = φ(∂A).




Sia
      γ una parametrizzazione di ∂A+
La curva φ ◦ γ ha come sostegno ∂S, e ne individua un’orientazione positiva che
indichiamo con ∂S + .
         L.Freddi                                             April 27, 2026   19 / 23
Teorema del Rotore e formula di Stokes
Sia ora F un campo vettoriale in R3 definito in un intorno della superficie S.
Teorema (di Stokes)
Sia S una superficie di classe C 2 . Si ha
                        Z                  Z
                            ∇ × F · ν dσ =            F (x) · dx
                          S                    ∂S +

            ∂u φ ∧ ∂v φ
dove ν =                 è il versore normale a S.
           |∂u φ ∧ ∂v φ|




         L.Freddi                                                  April 27, 2026   20 / 23
Flusso e circuitazione
Nella Zformula di Stokes
             F (x) · dx è la circuitazione del campo F sul bordo di S
      ∂S +
     Z
          ∇ × F · ν dσ è il flusso del rotore del campo F attraverso la superficie S
      S
Notiamo che
     se F è irrotazionale, cioè ∇ × F = 0 allora dal teorema di Stokes si ha che
                                    Z
                                         F (x) · dx = 0
                                     ∂S +
     che caratterizza la conservatività del campo se S è una superficie piana
     semplicemente connessa
     il teorema precisa il legame esistente tra flusso e circuitazione.




          L.Freddi                                                April 27, 2026   21 / 23
Esercizio
Esercizio (per casa)
Calcolare la circuitazione del campo vettoriale

                             F (x, y, z) = (x2 z, y, −yz)

lungo il bordo della superficie di equazioni
                          
                          x = u − v
                          
                            y=u                u2 + v 2 ≤ 1
                          
                            z = u2 + v 2
                          




         L.Freddi                                             April 27, 2026   22 / 23
Esercizio
Esercizio (per casa)
Calcolare la circuitazione del campo vettoriale

                             F (x, y, z) = (x2 z, y, −yz)

lungo il bordo della superficie di equazioni
                          
                          x = u − v
                          
                            y=u                u2 + v 2 ≤ 1
                          
                            z = u2 + v 2
                          

Si tratta di un paraboloide circolare. Per la formula di Stokes si ha
Z                              Z                  Z
      x2 z dx + y dy − yz dz =     ∇ × F · ν dσ =         ∇ × F · (∂u φ × ∂v φ) dudv
 ∂S +                           S                   B(0,1)

dove abbiamo usato la definizione di integrale di superficie e il fatto che
                                      ∂u φ × ∂v φ
                                ν=
                                     |∂u φ × ∂v φ|
         L.Freddi                                                April 27, 2026   22 / 23
Esercizio
Poiché φ(u, v) = (u − v, u, u2 + v 2 ), si ha
                      ∂u φ = (1, 1, 2u), ∂v φ = (−1, 0, 2v),
                                         
                               e1 e2 e3
          ∂u φ × ∂v φ = det  1      1 2u = 2ve1 − 2(u + v)e2 + e3
                              −1 0 2v
D’altra parte
                                
                 e1 e2       e3
 ∇ × F = det  ∂x ∂y ∂z  = −ze1 + x2 e2 = −(u2 + v 2 )e1 + (u − v)2 e2
                x2 z y −yz
e quindi
∇ × F · (∂u φ × ∂v φ) = −(u2 + v 2 )2v − (u − v)2 2(u + v) = 2u(v 2 − u2 + 2uv)
Infine
     Z                                        Z
               ∇ × F · (∂u φ × ∂v φ) dudv =               2u(v 2 − u2 + 2uv) dudv = 0
      B(0,1)                                     B(0,1)

come si verifica passando a coordinate polari.
           L.Freddi                                                    April 27, 2026   23 / 23
