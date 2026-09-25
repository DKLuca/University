---
fonte: "note.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Note di Teoria della Probabilità.

In queste brevi note, si richiameranno alcuni risultati di Teoria della Probabilità, riguar-
danti le conseguenze elementari delle definizioni di probabilità e σ-algebra. Si ricordano
le definizioni fondamentali.


  1. Una σ-algebra F è una famiglia di sottoinsiemi di un insieme Ω che soddisfa le
     seguenti proprietà:

       (a) Ω ∈ F;
      (b) è chiusa rispetto al complemento: se A ∈ F, allora Ac ∈ F;
       (c) è chiusa rispetto all’unione numerabile: se Ai ∈ F, i = 1, 2, ..., allora
                                                 ∞
                                                 [
                                                       Ai ∈ F.
                                                 i=1

  2. Uno spazio di probabilità è una terna S = {Ω, F, P }, dove Ω, è un insieme generico
     denominato spazio campione, F è una σ-algebra di sottoinsiemi di Ω (denominati
     eventi), e P è una funzione definita sugli insiemi di F e a valori reali, che soddisfa
     i seguenti assiomi:

       (a) P [Ω] = 1;
      (b) per ogni A ∈ F, P [A] ≥ 0;
       (c) per ogni sequenza numerabile di insiemi Ai ∈ F, i = 1, 2, ..., a due a due
           disgiunti, Ai ∩ Aj = ∅ per i 6= j, si ha (σ-additività)
                                             ∞
                                             [            ∞
                                                          X
                                        P[       Ai ] =         P [Ai ].
                                           i=1            i=1

    Valgono i seguenti risultati, che possono essere dimostrati come semplici esercizi
(nella dimostrazione, occorre utilizzare solamente le definizioni e le proprietà enunciate
precedentemente). Nel seguito, denoteremo con F una σ-algebra di sottoinsiemi di
un insieme Ω, e con P [.] una funzione probabilità definita sugli elementi di F. Nel caso
Ω = R, denoteremo con B la σ-algebra di Borel, ovvero la minima σ-algebra che contiene
le semirette (−∞, a], con a ∈ R. La σ-algebra di Borel è minima, nel senso che una
qualsiasi σ-algebra che ha come elementi le semirette, deve comprendere tutti gli insiemi
che costituiscono la σ-algebra di Borel. Ad esempio, la classe di tutti i sottoinsiemi di
R è ovviamente una σ-algebra che contiene le semirette (perché?): essa è tuttavia più
ampia della σ-algebra di Borel, dato che è possibile descrivere sottoinsiemi di R che non
appartengono a B.
  1. Dimostrare che ∅ ∈ F.

      Prova. Le proprietà 1.(a) e 1.(b) assicurano che ∅ = Ωc ∈ F.

                                              1
2. Dimostrare che F è chiusa rispetto all’intersezione numerabile: se Ai ∈ F, i =
   1, 2, ..., allora
                                      ∞
                                      \
                                         Ai ∈ F.
                                           i=1

                                                                        T∞       c
   Prova.
   S∞ c Si ricorda, dalla teoria degli insiemi, la regola di De Morgan ( i=1 Ai ) =
    i=1 Ai . Si applicano poi le proprietà 1.(b) e 1.(c).

3. Dimostrare che F è chiusa rispetto all’unione finita di insiemi: se Ai ∈ F, i =
   1, 2, ..., N , allora
                                      N
                                      [
                                         Ai ∈ F.
                                           i=1



   Prova. È sufficiente considerare la sequenza infinita di insiemi Bi = Ai per i =
   1, ..., N , e Bi = AN , per i > N (si ripete dunque l’ultimo insieme). Ovviamente,
   Bi ∈ F per ogni i, e si ha dunque, per la 1.(c),
                                     N
                                     [            ∞
                                                  [
                                           Ai =         Bi ∈ F.
                                     i=1          i=1


4. Dimostrare che F è chiusa rispetto all’intersezione finita di insiemi: se Ai ∈ F,
   i = 1, 2, ..., N , allora
                                      N
                                      \
                                         Ai ∈ F.
                                           i=1



   Prova. È sufficiente usare la regola di De Morgan ( N
                                                       T         c
                                                                    SN    c
                                                         i=1 Ai ) =  i=1 Ai , la
   proprietà precedente e la 1.(b).

5. Si consideri la σ-algebra di Borel B. Si dimostri che essa contiene ad esempio,
   per a, b ∈ R, gli insiemi del tipo (a, +∞), (a, b], i punti isolati {a}, (a, b), [a, b],
   l’insieme dei numeri interi, naturali, razionali, irrazionali.

   Prova. Essendo per definizione B la più piccola σ-algebra che contiene le semirette
   (−∞, a], essa contiene (a, +∞) = {(−∞, a]}c . Contiene (a, b] = (−∞, b]∩(a, +∞).
   Contiene   i punti isolati, intersezione di un’infinità numerabile di intervalli {a} =
                                                 c
   T
     n (a−1/n, a]. Contiene (a, b) = (a, b]∩{b} . Contiene [a, b] = (a, b]∪{a}. L’insieme
   dei numeri interi, dei razionali, dei naturali, sono unioni numerabili di punti isolati.
   Gli irrazionali sono l’insieme complementare dei razionali. Dunque B contiene tutti
   gli irrazionali in un intervallo, tutti gli interi negativi, le unioni di intervalli, ecc.
   Una classe estremamente ricca, anche se, come ricordato, possono essere descritti
   sottoinsiemi di R che non appartengono a B.

                                             2
 6. Si consideri uno spazio di probabilità S = {Ω, F, P }. Dimostrare che P [∅] = 0.
    Prova. Nella dimostrazione, è necessario sfruttare i soli assiomi della probabilità.

    Si consideri la famiglia di insiemi B1 = Ω, Bi = ∅, i > 1. Ovviamente, Bi ∈ F e
    Bi ∩ Bj = ∅, per i 6= j. Per la 2.(a) e la 2.(c), si può scrivere
                                     [
                      1 = P [Ω] = P [ Bi ] = P [Ω] + P [∅] + P [∅] + ... .
                                             i

    Dunque
                                           0 = P [∅] + P [∅] + ... .
    La somma di infiniti termini uguali maggiori o uguali a 0 (proprietà 2.(b)) può
    essere nulla solamente se tutti i termini sono nulli. Dunque P [∅] = 0.

 7. Si consideri uno spazio di probabilità S = {Ω, F, P }. Dimostrare che la probabilità
    è semplicemente additiva, ovvero che, considerata la collezione finita di insieme
    A1 , ..., AN , a due a due disgiunti, Ai ∩ Aj = ∅ per i 6= j, si ha
                                                N
                                                [            N
                                                             X
                                           P[       Ai ] =         P [Ai ].
                                              i=1            i=1

     Prova. Si consideri la famiglia numerabile di insiemi Bi = Ai , i = 1, ..., N , e

    Bi = ∅, i > N . Si ha
                N
                [                ∞
                                 [                                                    N
                                                                                      X
           P[       Ai ] = P [       Bi ] = P [B1 ] + ... + P [BN ] + P [∅] + ... =         P [Ai ].
             i=1             i=1                                                      i=1

 8. Si consideri consideri un evento A ∈ F. Dimostrare che P [Ac ] = 1 − P [A].

    Prova. Si ha Ω = A ∪ Ac e A ∩ Ac = ∅. Per la proprietà precedente,

                                         1 = P [Ω] = P [A] + P [Ac ].

 9. Si consideri consideri un evento A ∈ F. Dimostrare che P [A] ≤ 1.

    Prova. Per la 2.(b), si ha P [Ac ] ≥ 0. Dalla relazione 0 ≤ P [Ac ] = 1 − P [A], si
    deduce P [A] ≤ 1.

10. Siano A e B due eventi con B ⊃ A. Dimostrare che P [B] ≥ P [A].

    Prova. Per note proprietà degli insiemi, si ha B = A ∪ (B ∩ Ac ) (ci si aiuti con i
    diagrammi di Venn per la rappresentazione degli insiemi). Essendo A∩(B∩Ac ) = ∅,
    si può scrivere
                           P [B] = P [A] + P [B ∩ Ac ] ≥ P [A].
    Nella relazione precedente, si è usata la 2.(b).

                                                     3
 11. Dimostrare che la probabilità è una funzione continua, nel senso che, data una
     successione crescente di eventi Ai , i = 1, 2, ..., (tale cioè che Ai+1 ⊃ Ai ), posto
                                                      +∞
                                                  ∆
                                                      [
                                       lim Ai =             Ai = A,
                                       i→+∞
                                                      i=1

     si ha
                                   lim P [Ai ] = P [ lim Ai ].
                                  i→+∞                      i→+∞
     Allo stesso modo, si può dimostrare che, data una successione decrescente di insiemi
     Ai (tale cioè che Ai+1 ⊂ Ai ), posto in questo caso
                                                      +∞
                                                  ∆
                                                      \
                                       lim Ai =             Ai = A,
                                       i→+∞
                                                      i=1

     si ha
                                   lim P [Ai ] = P [ lim Ai ].
                                  i→+∞                      i→+∞


     Prova. Dimostriamo la proprietà nel caso di una sequenza crescente di insiemi. Si
     consideri la Fig. 1.(a), dove sono rappresentati gli insiemi Ai e il loro limite A. Si
     consideri poi la famiglia di insiemi Bi , definiti ponendo B1 = A1 e Bi = Ai ∩ Aci−1
     per i > 1, mostrata in Fig. 1.(b). Ovviamente, i Bi sono a due a due disgiunti, e
     si ha
                                                 [n
                                          An =      Bi .
                                                      i=1




                                          A                                    A
                       A1         An                          B1         Bn


                                   A2                                     B2
                            (a)                                    (b)

Figura 1: Sequenza crescente degli insiemi Ai (a), e successione Bi dei corrispondenti
insiemi disgiunti (b).


     Possiamo scrivere

                    P [A] = P [ lim Ai ] = P [∪+∞
                                               i=1 Ai ]
                                   i→+∞


                                              4
                                                          +∞
                                                          X                       n
                                                                                  X
                                  =    P [∪+∞
                                           i=1 Bi ] =           P [Bi ] = lim           P [Bi ]
                                                                           n→+∞
                                                          i=1                     i=1
                                  =      lim P [∪ni=1 Bi ] = lim P [An ].                                  (1)
                                       n→+∞                         n→+∞


       Si consideri ora il caso di una successione decrescente di insiemi, Ai+1 ⊂ Ai ,
                                                              +∞
                                                          ∆
                                                              \
                                              lim Ai =              Ai = A.
                                            i→+∞
                                                              i=1

       Utilizzando la regola di De Morgan, possiamo scrivere Ac = ∪+∞        c        c
                                                                        i=1 Ai , con Ai+1 ⊃
         c
       Ai . Gli insiemi complementari costituiscono dunque una successione di insiemi
       crescente con limite Ac , e, applicando il risultato appena dimostrato, si ha dunque

                                             P [Ac ] = lim P [Acn ].
                                                          n→+∞

       Si ottiene pertanto

            P [A] = 1 − P [Ac ] = 1 − lim P [Acn ] = lim (1 − P [Acn ]) = lim P [An ].
                                           n→+∞                     n→+∞                    n→+∞


    Formalmente, una variabile aleatoria viene definita a partire da uno spazio di proba-
bilità S = {Ω, F, P } come una funzione x : Ω → R misurabile, ovvero tale che, per ogni
a ∈ R, l’insieme {ω : x(ω) ≤ a} deve appartenere a F. In altre parole, l’immagine inver-
sa, tramite x, della semiretta (−∞, a], deve essere un insieme appartenente a F. Non
sarebbe troppo difficile dimostrare che la misurabilità di x garantisce che {ω : x(ω) ∈ B}
appartiene a F non solo per le semirette B = (−∞, a], ma anche se B è un generico
insieme di Borel B ∈ B. Risulta dunque possibile, a partire da x, definire lo spazio di
probabilità indotto
                                     Sx = {R, B, Px },
dove si pone, per ogni B ∈ B, Px [B] = P [{ω : x(ω) ∈ B}], con P [.] la funzione probabilità
dello spazio di probabilità originario1 . Per indicare Px [B], si usa spesso la notazione
alternativa P [x ∈ B]. Ad esempio, per indicare Px [(−∞, a]], possiamo usare la notazione
P [x ∈ (−∞, a]] o anche P [x ≤ a].
    La descrizione statistica di una v.a. consiste in sostanza nello specificare la funzione
probabilità Px [B] per ogni insieme di Borel B. Fortunatamente, si può dimostrare2 , che
Px è univocamente determinata dai valori Px [(−∞, a]]. In altre parole, se conosciamo
le probabilità P [x ≤ a], a ∈ R, in linea di principio possiamo calcolare la probabilità
                                                                                                  ∆
P [x ∈ B] per ogni insieme di Borel B. La conoscenza della probabilità Fx (a) = P [x ≤ a],
a ∈ R, è dunque sufficiente per la descrizione statistica di una v.a.: alla funzione Fx (a)
si dà il nome di distribuzione della v.a. x.
   1
     Si potrebbe far vedere facilmente che lo spazio di probabilità indotto è ben definito e, in particolare,
che Px [.] soddisfa effettivamente gli assiomi della funzione probabilità.
   2
     La dimostrazione è data da un teorema del matematico greco Carathéodory (1873-1950).


                                                      5
    Si noti che la descrizione statistica di x può in realtà essere data senza avere cono-
scenza dello spazio di probabilità originario S, e senza neppure specificare esplicitamente
la funzione x(ω), come nell’esempio che segue.

Esempio. Si considerino due spazi di probabilità S1 = {Ω1 , F1 , P1 } e S2 = {Ω2 , F2 , P2 }.
Lo spazio S1 modella il lancio di una moneta. Indicando con T l’esito testa e con C l’esito
croce, si può porre
                                       Ω1 = {T, C},
                                 F1 = {{T, C}, {T }, {C}, ∅},
                  P1 [{T, C}] = 1, P1 [{T }] = P1 [{C}] = 0.5,       P1 [∅] = 0.
    Lo spazio S2 modella il lancio di una dado. Indicando con fi l’esito corrispondente
all’uscita della faccia i-esima, si può porre

                                      Ω2 = {f1 , f2 , ..., f6 }.

La σ-algebra F2 può essere scelta uguale alla classe dei 26 = 64 sottoinsiemi di Ω2 ,
ponendo, per ogni A = ∪K    k=1 {fik } ∈ F2 , P2 [A] = K/6 (ad esempio, la probabilità che
nel lancio del dado si osservi una delle facce {f1 , f4 , f5 } risulta P2 [{f1 , f4 , f5 }] = 3/6).
    Si consideri la v.a. x1 definita a partire da S1 e cosı̀ definita
                                             
                                               1, ω = T,
                                   x1 (ω) =
                                               0, ω = C.

    Si consideri poi x2 definita a partire da S2 e cosı̀ definita
                                      
                                         1, ω ∈ {f1 , f2 , f3 },
                             x2 (ω) =
                                         0, ω ∈ {f4 , f5 , f6 }.

Risulta immediato verificare che x1 e x2 hanno la stessa descrizione statistica e, in
particolare, hanno distribuzione
                                       
                                        0,   a < 0,
                              Fx (a) =   0.5, 0 ≤ a < 1,
                                         1,   a ≥ 1.
                                       

Si possono dimostrare facilemente le seguenti proprietà della distribuzione.

   1. La funzione Fx (a) è non descrescente, ovvero b ≥ a ⇒ Fx (b) ≥ Fx (a).

      Prova. Il risultato è una conseguenza del fatto che b ≥ a implica (−∞, b] ⊃
      (−∞, a] e delle proprietà della funzione probabilità.

   2. Si ha
                                  lim Fx (a) = 1,        lim Fx (a) = 0.
                                a→+∞                    a→+∞




                                                  6
     Prova. Per a → +∞, si ha (−∞, a] → (−∞, +∞) = R e dunque

              lim Fx (a) = lim Px [(−∞, a]] = Px [ lim (−∞, a]] = Px [R] = 1.
             a→+∞           a→+∞                      a→+∞

     Nella relazione precedente, si è sfruttata la continuità della funzione probabilità.
     Per a → −∞, si procede analogamente, osservando che (−∞, a] → ∅ e che P [∅] = 0.

  3. La Fx (a) è una funzione continua da destra, ovvero

                                    lim Fx (a + h) = Fx (a),
                                   h→0+

     dove la notazione h → 0+ indica che h tende a zero per valori positivi.

     Prova. È sufficiente osservare che (−∞, a + h] tende a (−∞, a] quando h tende a
     zero per valori positivi.

È inoltre possibile dimostrare che se una funzione F (a) soddisfa le proprietà indicate,
allora è possibile costruire una v.a. che ha F (a) come funzione distribuzione.




                                            7
