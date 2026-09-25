---
fonte: "filtrinumerici.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

III Lezione: Filtri numerici
In questa sezione, considereremo soprattutto alcuni esercizi relativi al filtraggio dei
segnali. L’attenzione verrà posta al filtraggio dei segnali a tempo discreto, e si supporrà
dunque di avere a che fare con segnali definiti su Z(T ).
    La relazione ingresso-uscita di un filtro definito su Z(T ) con risposta impulsiva
h(t), t ∈ Z(T ), risulta come noto data dall’operazione di convoluzione
                         +∞
                         X                                 +∞
                                                           X
           y(nT ) = T          h(kT )x(nT − kT ) = T             x(kT )h(nT − kT ).       (1)
                        k=−∞                              k=−∞

    Cominceremo con l’introdurre alcuni concetti fondamentali per la realizzazione e
la comprensione dei filtri a tempo discreto. Il lettore potrà rivelarne l’analogia con
concetti relativi ad altre discipline, in cui si considerano sistemi a tempo continuo.


1    Stabilità BIBO di un filtro numerico
Un filtro numerico si dice stabile in senso BIBO (Bounded Input-Bounded Output) se
l’uscita ad un ingresso limitato è anch’essa limitata. Si ricorda che il segnale x(nT ) è
limitato se esiste un numero finito M tale che

                              |x(t)| ≤ M,   per ogni t ∈ Z(T ).                           (2)

Vengono ora analizzate le condizioni per cui la traformazione lineare (1) risulta stabile
in senso BIBO. Come è logico attendersi, le condizioni riguardano la risposta impulsiva
h(nT ). Si ha infatti
                                       +∞
                                       X
                         |y(nT )| ≤         T |h(kT )||x(nT − kT )|
                                      k=−∞
                                         +∞
                                         X
                                   ≤M             T |h(kT )|,
                                          k=−∞

dove si è sfruttato il fatto che, per un ingresso limitato, vale la (2). Se dunque la
somma dei moduli della risposta impulsiva del filtro è finita, cosı̀ risulta l’uscita y(nT ).
La relazione precedente stabilisce una condizione sufficiente per la stabilità BIBO. Tale
condizione è anche necessaria: se infatti fosse
                                    +∞
                                    X
                                          T |h(kT )| = +∞                                 (3)
                                   k=−∞

e h(kT ) non fosse limitata, basterebbe prendere l’ingresso x(nT ) = δZ(T ) (nT ) per
ottenere un’uscita y(nT ) = h(nT ) non limitata. Se infine valesse la (3) e h(kT ) fosse
limitata, basterebbe prendere l’ingresso x(nT − kT ) = h∗ (kT )/|h(kT )|, per |h(kT )| =
                                                                                       6 0
e 0 altrove, per avere y(nT ) = +∞ all’istante nT . Possiamo dunque concludere con il
seguente Teorema.



                                              1
Teorema 1. Un filtro sui tempi discreti caratterizzato dalla risposta impulsiva h(t), t ∈
Z(T ) è stabile in senso BIBO se e solo se
                                  +∞
                                  X
                                          T |h(kT )| < +∞.
                                 k=−∞

   Dunque, un filtro risulta stabile in senso BIBO se la sua risposta impulsiva decade
in maniera sufficientemente rapida, per nT che tende a più o meno infinito, in modo
che valga la
                                 X+∞
                                       T |h(kT )| < +∞
                                 k=−∞

    Si introduce la seguente nomenclatura: un filtro a tempo discreto si dice di tipo FIR
(Finite Impulse Response) se la sua risposta impulsiva è di durata finita. Viceversa,
esso si dice di tipo IIR (Infinite Impulse Response) se la sua risposta impulsiva ha
durata non limitata.


2    Risposta in frequenza razionale
Una classe molto importante di filtri a tempo discreto è la classe dei filtri causali
a risposta in frequenza razionale, tali cioè che la trasformata di Fourier H(f ), f ∈
R/Z(1/T ), della risposta impulsiva h(t), t ∈ Z(T ), assume la forma

                                     T rk=0 bk e−j2πf kT
                                        P
                             H(f ) = Pq            −j2πf kT
                                                            ,                       (4)
                                          k=0 ak e

dove si può porre, senza perdita di generalità, a0 = 1. Nel caso infatti fosse a0 6= 1,
basterebbe dividere numeratore e denominatore per a0 . La risposta in frequenza H(f )
risulta, come è noto e come si vede immediatamente dalla (4), una funzione periodica
in f di periodo Fs = 1/T .
    Il termine razionale risulta più comprensibile se, anziché considerare la trasformata
di Fourier (4), ci riferiamo alla trasformata zeta della risposta impulsiva, detta anche
funzione di trasferimento del filtro,
                                             +∞
                                      ∆
                                             X
                               Hz (z) = T          h(nT )z −n ,
                                            n=−∞

la quale risulta un rapporto fra polinomi in z −1 . Infatti, ricordando che la trasformata
di Fourier si ottiene dalla trasformata zeta ponendo z = exp(j2πf T ), nell’ipotesi di
esistenza di entrambe, dalla (4) si ottiene

                                          T rk=0 bk z −k
                                            P
                                Hz (z) = Pq           −k
                                                          .                            (5)
                                             k=0 ak z

    Vedremo come la classe dei filtri a risposta in frequenza razionale possa essere
realizzata mediante algoritmi numerici estremamente semplici.
    Consideriamo dapprima alcuni semplici esempi.
Esempio 1. La sequenza esponenziale.


                                              2
      Consideriamo il filtro a tempo discreto con risposta impulsiva causale h(nT ) = pn 10 (nT ).
Il filtro è stabile in senso BIBO se risulta |p| < 1. In tali ipotesi, la risposta in frequenza è una
funzione razionale e risulta
                                              T
                             H(f ) =                  ,       f ∈ R/Z(1/T ).
                                        1 − pe−j2πf T
La trasformata zeta vale
                                                        T
                                          Hz (z) =                                                 (6)
                                                     1 − pz −1
e presenta un polo in z = p all’interno del cerchio unitario del piano complesso e uno zero
nell’origine. La regione di convergenza della trasformata zeta è la regione |z| > |p|.
    Consideriamo invece un filtro con risposta in frequenza
                                              T
                             H(f ) =                  ,       f ∈ R/Z(1/T ),
                                        1 − pe−j2πf T
dove però sia |p| > 1. In questo caso, l’antitrasformata risulta, come è immediato verificare, un
segnale anti-causale ed uguale a

                                      h(nT ) = −pn 10 (−nT − T ).

Si tratta anche in questo caso di un filtro stabile in senso BIBO. La trasformata zeta vale
                                                        T
                                          Hz (z) =
                                                     1 − pz −1
ma questa volta la regione di convergenza risulta |z| < |p|.
    Infine, un filtro con risposta impulsiva causale h(nT ) = pn 10 (nT ), con |p| ≥ 1, non è ovvia-
mente stabile in senso BIBO. La sua trasformata zeta assume ancora la forma (6) e converge
per |z| > |p|, mentre la sua trasformata di Fourier non esiste (almeno in senso ordinario).
    Un facile esercizio, risolvibile applicando più volte la regola di derivazione della trasformata
di Fourier, permetterebbe di stabilire che la sequenza causale
                                      (n + k − 1)! n
                          h(nT ) =                p 10 (nT ),        nT ∈ Z(T ),                   (7)
                                       n!(k − 1)!

stabile in senso BIBO per |p| < 1, ha trasformata di Fourier
                                              T
                            H(f ) =                       ,    f ∈ R/Z(1/T )                       (8)
                                      (1 − pe−j2πf T )k

e trasformata zeta, convergente per |z| > |p|,
                                                        T
                                        Hz (z) =                 .                                 (9)
                                                   (1 − pz −1 )k

    In conclusione, le (7)-(9), valide per k ≥ 1, forniscono il legame segnale-trasformata relativo
a sequenze causali e stabili con andamento esponenziale nel dominio del tempo e forma razionale
nel dominio della trasformata. In particolare, dato che ci limitiamo a considerare sequenze
causali, la trasformata zeta (9) ha un polo, di molteplicità k, all’interno del cerchio unitario e
uno zero di molteplicità k nell’origine.


    Consideriamo ora il caso della generica trasformata zeta razionale (5). Il calcolo
della antitrasformata è banale se q = 0. In tale caso, infatti, Hz (z) si riduce ad un
polinomio in z −1 e i coefficienti della risposta impulsiva risultano uguali a h(nT ) = bn

                                                     3
per n = 0, ..., r, e 0 altrove. La risposta impulsiva è dunque, in questo caso, di tipo
FIR.
   Nel caso q 6= 0, il modo di procedere è quello di sviluppare la (5) in frazioni parziali:
possiamo scrivere
                                          b0 + b1 z −1 + ... + br z −r
                          Hz (z) = T
                                          1 + a1 z −1 + ... + am z −q
                                                                                                    (10)
                                           b0 + b1 z −1 + ... + br z −r
                                    =T                                         ,
                                       (1 − p1 z −1 )m1 · · · (1 − ps z −1 )ms
dove pi è il polo i-esimo della trasformata zeta, e mi la rispettiva molteplicità, con
m1 + ... + ms = q. Supponendo r < q nella espressione della trasformata zeta1 , la (10)
può essere scritta nella forma
                                  m1                             m
                                                                 s
                                  X         A1j                 X      Asj
                      Hz (z) =                          + ... +                    ,                (11)
                                        (1 − p1 z −1 )j            (1 − ps z −1 )j
                                  j=1                           j=1

dove, come è noto,
                          1         1          dmi −j                       −1 mi
                                                                                   
             Aij =                                          Hz (z)(1 − p i z   )         .          (12)
                      (mi − j)! (−pi )mi −j d(z −1 )mi −j                           z=pi


Si noti che la derivata viene fatta rispetto alla variabile w = z −1 . Si noti inoltre che nel
caso di un polo pi con molteplicità unitaria, il coefficiente Ai1 si calcola semplicemente
dalla (12) valutando la funzione Hz (z)(1 − pi z −1 ) per z = pi .
    Possiamo calcolare l’antitrasformata di Hz (z) usando i risultati dell’esempio pre-
cedente. Se ne conclude che, se tutti i poli pi sono in modulo minori di 1, l’antitra-
sformata della Hz (z) corrisponde alla combinazione lineare di sequenze con andamento
esponenziale della forma (7). Nel caso fosse r ≥ q, alla combinazione di esponenziali si
aggiungerebbe nella risposta impulsiva un contributo di durata finita, corrispondente
all’antitrasformata di un polinomio in z −1 .
Esempio 2.
   Si consideri un filtro causale con funzione di trasferimento
                                                1.5 + 0.5z −1 + 0.2z −2
                                   Hz (z) = T                           .                           (13)
                                                 1 − 0.7z −1 + 0.1z −2
Si ricava facilmente che i poli di Hz (z) valgono z = 0.5 e z = 0.2 e sono quindi interni al cerchio
di raggio unitario. Se ne deduce che Hz (z) è la funzione di trasferimento di un filtro causale
e stabile. Applicando la scomposizione in frazioni parziali, dopo avere calcolato il resto della
divisione fra numeratore e denominatore, si trova
                                                                      
                                                 5.5            6
                           Hz (z) = T 2 +                −               .
                                             1 − 0.5z −1   1 − 0.2z −1
La risposta impulsiva del filtro risulta pertanto di tipo IIR
                     h(nT ) = 2T δZ(T ) (nT ) + 5.5 · 0.5n 10 (nT ) − 6 · 0.2n 10 (nT ).


   1
     Se cosı̀ non fosse, basterebbe prendere il resto della divisione del numeratore per il denominatore,
scomponendo Hz (z) nella somma di un polinomio in z −1 e di una funzione razionale della forma voluta.


                                                     4
3    Equazioni alle differenze
Si consideri un filtro con una risposta in frequenza razionale, come nell’equazione (4).
La relazione ingresso-uscita del filtro, espressa nel dominio della frequenza, risulta

                                Y (f ) = H(f )X(f ),      f ∈ R/Z(T ),                    (14)

dove Y (f ) e X(f ) sono la trasformata di Fourier dell’uscita e dell’ingresso, rispetti-
vamente. Moltiplicando entrambi i membri della (14) per il denominatore di H(f ) e
ricordando la regola di traslazione per la trasformata di Fourier, si ottiene nel dominio
del tempo la seguente relazione ricorsiva fra y(nT ) e x(nT )
                                  q
                                  X                           r
                                                              X
                   y(nT ) = −           ak y((n − k)T ) + T          bk x((n − k)T ).     (15)
                                  k=1                         k=0

L’equazione lineare alle differenze finite (15), corrispondente ad una funzione di tras-
ferimento razionale, può facilmente essere realizzata mediante un algoritmo numerico,
come esemplificato nello schema di Fig. 1.
                  x(n)                                                    x(n-r)
                              T              T                       T


                         b0             b1                    br-1            br



                                                  +

                                                                                   y(n)
                                                  +


                                                  +


                         -a q            -a q-1                -a 1


                              T              T                       T
                y(n-q)

        Figura 1: Schema per la realizzazione dell’equazione a differenze finite.

    La sua struttura suggerisce anche la forma normalizzata
                                   q
                                   X                         r
                                                             X
                    y(nT ) = −           ak y((n − k)T ) +         b0k x((n − k)T ),
                                   k=1                       k=0

in cui vengono definiti i coefficienti b0k = T bk .

                                                      5
Esempio 3. La funzione di trasferimento (13) corrisponde alla seguente equazione alle diffe-
renze

 y(nT ) = 0.7y((n−1)T )−0.1y((n−2)T )+1.5T x(nT )+0.5T x((n−1)T )+0.2T x((n−2)T ). (16)

Come si vede, l’uscita al tempo nT dipende dai valori precedenti dell’ingresso e dell’uscita. Se
però l’ingresso x(nT ) è nullo per nT < n0 T , anche l’uscita y(nT ) risulta nulla per nT < n0 T ,
dato che il filtro è causale e risulta h(nT ) = 0 per nT < 0. In tali ipotesi, il sistema (16) evolve
a partire da condizioni iniziali nulle a partire dall’istante n0 T .
    È possibile scrivere il seguente programma MATLAB per il calcolo dell’uscita da n0 T = 0
a nT = 100T corrispondente all’ingresso x(nT ) = sin(2πf0 nT )10 (nT ), con T = 1, f0 = 0.1T .

% condizioni iniziali -caricamento dello ‘‘stato’’ del filtro

xs=[0,0];
ys=[0,0];
r1=length(xs);
q1=length(ys);

% istante iniziale
n0=0;

n=n0;
T=1;

while (n>=n0 & n<=100),

% nuovo ingresso

  xnT=sin(2*pi*0.1*n);

% calcolo dell’uscita: l’indice n+1 e‘ relativo al campione y(nT)

  y(n+1)=[0.7 -0.1]*ys’ + [1.5 0.5 0.2]*[xnT xs]’;

% aggiornamento dello stato

  ys=[y(n+1),       ys(1:q1-1)];
  xs=[xnT,          xs(1:r1-1)];

  n=n+1;
end;



    Nell’esempio precedente abbiamo visto come possiamo utilizzare la (15) per il calcolo
dell’uscita di un filtro causale con funzione di trasferimento razionale quando l’ingresso
è nullo prima di un certo istante. Come possiamo calcolare l’uscita nel caso in cui
l’ingresso sia diverso da zero, in generale, da meno infinito a più infinito? Ovviamente,
saremo interessati dal punto di vista operativo a conoscere l’uscita a partire da un
certo istante t di osservazione. Per poter utilizzare la (15) dovremmo però conoscere le
condizioni iniziali, specificate anche dai valori precedenti dell’uscita, che purtroppo in
generale non conosciamo dato che stiamo cercando di calcolarla.


                                                  6
    La soluzione del problema si ottiene in maniera semplice se il segnale di ingresso
x(t), t ∈ Z(T ), ha una durata convenzionale praticamente limitata. In questo caso,
infatti, è sufficiente pensare che il segnale sia nullo al di fuori di un certo intervallo ed
usare la (15) per calcolare l’uscita del filtro con la precisione voluta.


                         h(kT )




                                               n1 T                                    kT


                         x(kT )



                                                                                       kT


                         xT (kT )



                                                      n0 T                             kT


                         h(n0 T + n1 T − kT )



                                                                                       kT

Figure 2: Nel calcolo della convoluzione, all’istante n0 T + n1 T le uscite corrispondenti
aFigura
  x(t) e 2:
         xT Nel
            (t) coincidono   (praticamente).
                 calcolo della convoluzione, all’istante n0 T + n1 T le uscite corrispondenti
 a x(t) e xT (t) coincidono (praticamente).
dipende dalla velocità di decadimento degli esponenziali, e quindi dal modulo dei poli
dellaNel    caso invece
        funzione            il segnale abbia
                    di trasferimento.          Piùuni andamento     persistente,
                                                       poli sono piccoli            come più
                                                                            in modulo,     ad esempio
                                                                                                velocementeavviene
                                                                                                                si
esaurisce la risposta impulsiva. Di conseguenza, se approssimiamo l’ingresso x(nTdei
 per  i  segnali sinusoidali,      il segnale    a gradino,   o  anche,  in generale,  per  le realizzazioni     )
 processi    aleatori,  è  utile  fare   la  seguente    osservazione.    Come    abbiamo
con una sua versione troncata xT (nT ) = x(nT )10 (nT − n0 T ), le uscite y(nT ) = x ∗        visto,   la risposta
 impulsiva
h(nT    ) e yTh(nT
                (nT )) =di xun ∗filtro
                                     h(nTcausale
                                            ) sono stabile     con risposta
                                                       praticamente     ugualiinper
                                                                                  frequenza
                                                                                      t ≥ n0 T razionale
                                                                                                  + n1 T ha     un
                                                                                                             (vedi
                               T
 andamento       dato  dalla     somma      di  una   sequenza    di durata   finita e di
Fig. 2). Il calcolo di yT (nT ) può dunque essere eﬀettuato utilizzando l’equazione alle  un  certo   numero    di
 sequenze esponenziali.
diﬀerenze     (15) a partire Nei         limiti di una
                                    da condizioni          precisione
                                                        iniziali  nulle: prefissata,  tale risposta
                                                                          dopo un numero                impulsiva
                                                                                               di campioni      di
 può   considerarsi    in    ogni    caso   trascurabile    a  partire   da un   certo
uscita pari a n1 T , ovvero dopo l’esaurimento del transitorio del filtro, i campioni    istante   t  =   n1 T che
                                                                                                                di
 dipende     dalla  velocità    di   decadimento       degli esponenziali,    e quindi
yT (nT ) coincidono praticamente con quelli che si sarebbero ottenuti filtrando l’ingressodal  modulo      dei poli
 della funzione
originario.          di trasferimento.
                Si dice    in questo casoPiù    che,i dopo
                                                        poli sono   piccoli in del
                                                               l’esaurimento    modulo,    più velocemente
                                                                                     transitorio,    l’uscita delsi
 esaurisce    la  risposta      impulsiva.       Di   conseguenza,     se  approssimiamo
filtro è in regime permanente. Si noti l’analogia con la nomenclatura ed i concetti usati,   l’ingresso    x(nT )
anche in altre discipline, per i segnali a tempo continuo.
                                                            7
con una sua versione troncata xT (nT ) = x(nT )10 (nT − n0 T ), le uscite y(nT ) = x ∗
h(nT ) e yT (nT ) = xT ∗ h(nT ) sono praticamente uguali per t ≥ n0 T + n1 T (vedi
Fig. 2). Il calcolo di yT (nT ) può dunque essere effettuato utilizzando l’equazione alle
differenze (15) a partire da condizioni iniziali nulle: dopo un numero di campioni di
uscita pari a n1 T , ovvero dopo l’esaurimento del transitorio del filtro, i campioni di
yT (nT ) coincidono praticamente con quelli che si sarebbero ottenuti filtrando l’ingresso
originario. Si dice in questo caso che, dopo l’esaurimento del transitorio, l’uscita del
filtro è in regime permanente. Si noti l’analogia con la nomenclatura ed i concetti usati,
anche in altre discipline, per i segnali a tempo continuo.


4       L’uso di MATLAB per il progetto dei filtri
Abbiamo visto nella sezione precedente come sia possibile realizzare tramite un algo-
ritmo numerico un filtro a tempo discreto con risposta in frequenza razionale. Esistono
in realtà dei criteri di organizzazione dei calcoli che rendono la realizzazione del filtro
più robusta, ad esempio qualora sia necessario utilizzare processori che utilizzano un’a-
ritmetica a precisione finita. Il programma MATLAB fornisce con il Signal Processing
Toolbox un insieme di procedure per il filtraggio a tempo discreto. In particolare, la
funzione filter(b,a,x), supponendo uguale ad 1 il primo elemento a(1) del vettore
a, filtra i dati contenuti nel vettore x di ingresso realizzando l’equazione alle differenze

y(n) = b(1)*x(n) + b(2)*x(n-1) + ... + b(nb+1)*x(n-nb)
                         - a(2)*y(n-1) - ... - a(na+1)*y(n-na).

Si noti che i coefficienti del vettore b(i) devono essere posti uguali a T bi−1 , secondo
quanto richiesto nella (15)2 .
    La funzione [H,f]=freqz(b,a,N,Fs) calcola N campioni complessi equispaziati fra
0 e Fs /2, con Fs = 1/T , della trasformata di Fourier corrispondente alla funzione di
trasferimento razionale
                                 b(1) + b(2)z −1 + ... + b(nb + 1)z −nb
                      Hz (z) =                                          .
                                  1 + a(2)z −1 + ... + a(na + 1)z −na

In particolare, gli N valori della risposta in frequenza vengono posti nel vettore H,
mentre i rispettivi valori della frequenza, in Hz, vengono posti nel vettore f. Si noti
che la trasformata di Fourier H(f ) = Hz (ej2πf T ) ha simmetria hermitiana, e quindi ci
si può limitare a specificarla tra 0 e Fs /2.
    Per l’analisi di una funzione di trasferimento, sono utili anche le procedure residuez
e roots che calcolano, rispettivamente, la scomposizione in frazioni parziali di un
rapporto di polinomi e le radici di un polinomio. Si consideri inoltre lo strumento
di visualizzazione fvtool, molto utile per l’analisi e la visualizzazione grafica delle
caratteristiche dei filtri.

    Un argomento di fondamentale importanza, cui qui accenneremo soltanto parzial-
mente, riguarda il progetto di filtri numerici. Il problema che qui ci si pone è il seguente:
assegnata una determinata risposta in frequenza del filtro, come è possibile determinare
    2
    Gli algoritmi di MATLAB assumono che T =1. Ci si può facilmente ricondurre al caso generale
supponendo di riferirci ai coefficienti normalizzati T bk .


                                               8
i coefficienti bi e ai di una risposta in frequenza razionale che approssimi l’andamento
voluto? Esistono a questo proposito molte tecniche di progetto, relative sia a filtri FIR
(q = 0 nella (5)), che a filtri IIR.
    Tipicamente, i filtri che si desidera realizzare hanno un andamento della risposta
in frequenza che approssima uno degli andamenti ideali di Fig. 3, relativi a filtri
passa-basso, passa-alto, passa-banda e elimina-banda, rispettivamente. Nella Fig. 3, le
frequenze sono normalizzate rispetto alla frequenza di campionamento Fs . Trattandosi
di filtri reali, è sufficiente rappresentare l’andamento della risposta in frequenza fra
f = 0 e f = Fs /2. Come vedremo, i vari metodi di progetto si limitano molto spesso a
specificare solamente il modulo della risposta in frequenza desiderata.


        H(f )      a)                                  H(f )   b)




                                        0.5    f                                   0.5   f

        H(f )      c)                                  H(f )   d)




                                        0.5    f                                   0.5   f


Figure 3: Andamento dei filtri ideali a) passa-basso, b) passa-alto, c) passa-banda e d)
Figura 3: Andamento dei filtri ideali a) passa-basso, b) passa-alto, c) passa-banda e d)
elimina-banda
elimina-banda
ascisse   è parametrizzato
     Trattandosi               rispetto
                    di un problema        a f /Fs ) di un tipico
                                       di approssimazione,        filtro numerico
                                                              occorrerà specificareche
                                                                                     nel approssima
                                                                                          progetto le
un filtro passa-basso
tolleranze                ideale.
              ammesse nella        I parametri
                              realizzazione    delda  considerare
                                                   filtro. A questosono:
                                                                     proposito, si consideri la Fig.
4. In essa, viene rappresentato il modulo della risposta in frequenza (l’asse delle ascisse
    1. la banda passante, specificata dalla frequenza Wp . Si richiede che il filtro abbia
è parametrizzato rispetto a f /(Fs /2)) di un tipico filtro         numerico che approssima un
       modulo della risposta in frequenza circa uguale ad 1 per 0 ≤ f ≤ Wp . Per un
filtro passa-basso ideale. I parametri da considerare sono:
       filtro passabanda, andrà in genere specificato un intervallo di frequenze entro il
       quale
    1. la      si desidera
            banda  passante,che  il filtro abbia
                              specificata   dallamodulo
                                                   frequenzadella
                                                               Wptrasformata
                                                                  . Si richiedediche
                                                                                  Fourier    unitario;
                                                                                      il filtro abbia
       modulo della risposta in frequenza circa uguale ad 1 per 0 ≤ f ≤ Wp . Per un
    2. la banda oscura, specificata in questo caso dalla frequenza Ws . Si richiede che il
       filtro passabanda, andrà in genere specificato un intervallo di frequenze entro il
       filtro abbia modulo della risposta in frequenza circa uguale a 0 per Wp ≤ f ≤
       quale si desidera che il filtro abbia modulo della trasformata di Fourier unitario;
       Fs /2. L’intervallo [Wp , Ws ] specifica la cosiddetta banda di transizione del filtro;
    2. la banda oscura, specificata in questo caso dalla frequenza Ws . Si richiede che il
    3. il ripple in banda passante, quantificato tramite il valore Rp (spesso espresso in
       filtro abbia modulo della risposta in frequenza circa uguale a 0 per Ws ≤ f ≤ Fs /2.
       dB) che permette di determinare l’errore rispetto all’andamento desiderato;
       L’intervallo [Wp , Ws ] specifica la cosiddetta banda di transizione del filtro;
    4. il ripple in banda attenuata, specificato tramite il valore massimo R del modulo
    3. il ripple in banda passante, quantificato tramite il valore Rp (spessos espresso in
       della risposta in frequenza del filtro in banda attenuata.
       dB) che permette di determinare l’errore rispetto all’andamento desiderato;

                                                   9
                  1.2



                    1
               Rp
                  0.8



                  0.6



                  0.4



                  0.2


                                                                                          Rs
                    0
                     0   0.10   0.2   0.30   0.4   0.50   0.6   0.70   0.8   0.90   1.0
                                             Wp           Ws

               Figure 4: Parametri di progetto di un filtro passa-basso.
               Figura 4: Parametri di progetto di un filtro passa-basso.


   4. il ripple in banda attenuata, specificato tramite il valore massimo Rs del modulo
      della risposta in frequenza del filtro in banda attenuata.

Progetto di filtri IIR in MATLAB. Il programma MATLAB fornisce varie pro-
cedure per il progetto di filtri IIR (q > 0 nella (5)). Considereremo in particolare il
caso dei filtri ellittici, i quali forniscono una approssimazione uniforme della risposta
in frequenza sia in banda passante che in banda oscura. Si può dimostrare che i filtri
ellittici sono ottimi, nel senso che, fissati i valori Wp , Rp e Rs , la banda di transizione
Ws − Wp è la minima possibile per un dato grado q del denominatore del filtro (q viene
detto l’ordine del filtro).
     Il progetto dei filtri ellittici passa-basso in MATLAB viene effettuato utilizzando
le due procedure ellipord e ellip del Signal Processing Toolbox. La sintassi di
ellipord è la seguente:

[N, Wn] = ellipord(Wp, Ws, RpdB, RsdB).
                                            10
In ingresso alla funzione vanno specificate le frequenze Wp e Ws (vedi Fig. 4), norma-
lizzate rispetto a Fs /2. Inoltre, occorre specificare i valori di Rp e Rs , in dB. L’uscita
della funzione fornisce il valore N dell’ordine q del filtro che soddisfa le specifiche, e il
valore della frequenza naturale Wn da usare per l’effettivo progetto del filtro, effettuato
con la procedura

[b,a] = ellip(N, RpdB, RsdB, Wn).

Nei vettori b ed a, si trovano i coefficienti del numeratore e denominatore della risposta
in frequenza razionale (5) che soddisfa le specifiche. Si noti che i valori nel vettore b
includono la moltiplicazione per il quanto temporale T . Il metodo di progetto con filtri
ellittici non permette di specificare la caratteristica di fase del filtro.


                                                   10
     Esempio 4. Supponiamo che la frequenza di campionamento del sistema numerico sia Fs = 8
     kHz, e si voglia progettare un filtro passa-basso con banda passante da 0 a 1.6 kHz e banda
     oscura da 2.4 kHz a 4 kHz=Fs /2. Si supponga di imporre Rp = 0.95 e Rs = 0.05. Il progetto
     e la visualizzazione della risposta in frequenza del filtro, mostrata nelle figure 5 e 6, viene
     effettuata con il seguente programma MATLAB.

     % Parametri di progetto

     Fs=8000;
     RpdB=-20*log10(0.95);
     RsdB=-20*log10(0.05);
     Wp=1600/Fs*2;
     Ws=2400/Fs*2;

     % Progetto del filtro

     [N,Wn]=ellipord(Wp, Ws, RpdB, RsdB);
     [b,a]=ellip(N, RpdB, RsdB, Wn);

     % Visualizzazione del filtro

     [H,f]=freqz(b,a,512,Fs);
     plot(f,abs(H));
     plot(f,angle(H));

     Si noti dalla Fig. 5 che il filtro soddisfa effettivamente le specifiche. Nella Fig. 6, si noti
     la discontinuità di π attorno alla frequenza 2.5 kHz, dovuta al cambiamento di segno di H(f )
     (corrispondente
(corrispondente        al punto
                   al punto       angolosonell’andamento
                               angoloso     nell’andamento del
                                                             delmodulo).
                                                                 modulo).LaLafase è rappresentata
                                                                                fase                modulo
                                                                                      è rappresentata modulo
2π. L’ordine del filtro è risultato q = 3, e quindi i vettori b e a hanno dimensione Il4.filtro
     2π.  L’ordine del  filtro è risultato q =  3, e quindi i vettori b e a hanno  dimensione   4.    Il filtro
     può essere utilizzato per l’elaborazione dell’ingresso posto nel vettore x mediante il comando
può essere utilizzato per l’elaborazione dell’ingresso posto nel vettore x mediante il comando
     filter(b,a,x).
filter(b,a,x).                                                                                              ✷

                             1

                            0.9

                            0.8

                            0.7

                            0.6

                            0.5

                            0.4

                            0.3

                            0.2

                            0.1

                             0
                              0    500   1000   1500   2000   2500   3000   3500   4000



        Figure 5: Modulo della risposta in frequenza del filtro ellittico (f in Hz).
            Figura 5: Modulo della risposta in frequenza del filtro ellittico (f in Hz).

                             4


                             3
                                                       11
                             2


                             1
                        0.1

                         0
                          0    500       1000   1500       2000   2500   3000   3500   4000



       Figure 5: Modulo della risposta in frequenza del filtro ellittico (f in Hz).


                         4


                         3


                         2


                         1


                         0


                        −1


                        −2


                        −3


                        −4
                          0    500       1000   1500       2000   2500   3000   3500   4000



   Figure 6: Fase (radianti) della risposta in frequenza del filtro ellittico (f in Hz)
        Figura 6: Fase (radianti) della risposta in frequenza del filtro ellittico (f in Hz)

    Le funzioni ellipord e ellip possono essere utilizzate per il progetto di filtri
        Le funzioni
passa-alto,           ellipord
             passa-banda        e ellip possono
                           e elimina-banda.       essere utilizzate
                                             Si considerino         per il progetto
                                                              in particolare          di filtri
                                                                               i seguenti esempi
     passa-alto, passa-banda e elimina-banda. Si considerino in particolare i seguenti esempi
esplicativi.
    esplicativi.
Esempio 5. Progetto di un filtro passa-alto (Fs = 8 kHz) con banda oscura [0,1.5] kHz e
    Esempio 5. Progetto di un filtro passa-alto (Fs = 8 kHz) con banda oscura [0,1.5] kHz e
banda passante
    banda        [2.5,4]
           passante      kHz,
                     [2.5,4]   RpR= =0.99
                             kHz,      0.99e eRRs =
                                                  = 0.01.
                                                    0.01.
                                     p                 s

% Parametri  di di
    % Parametri progetto
                   progetto

Fs=8000;
    Fs=8000;
    RpdB=-20*log10(0.99);
RpdB=-20*log10(0.99);
    RsdB=-20*log10(0.01);
RsdB=-20*log10(0.01);
    Wp=2500/Fs*2;
Wp=2500/Fs*2;
    Ws=1500/Fs*2;

    % Progetto del filtro
                                                           12
    [N,Wn]=ellipord(Wp, Ws, RpdB, RsdB);
    [b,a]=ellip(N, RpdB, RsdB, Wn, ’high’);


    Si noti che Wp > Ws e l’uso del parametro ’high’ nella chiamata a ellip. L’ordine del filtro
    è risultato q = 4.

    Esempio 6. Progetto di un filtro passa-banda (Fs = 8 kHz) con banda oscura negli intervalli
    [0,1] kHz e [3,4] kHz e banda passante [1.5,2.5] kHz, Rp = 0.95 e Rs = 0.01.

    % Parametri di progetto

    Fs=8000;
    RpdB=-20*log10(0.95);
    RsdB=-20*log10(0.01);
    Wp=[1500/Fs*2, 2500/Fs*2];
    Ws=[1000/Fs*2, 3000/Fs*2];


                                                           12
% Progetto del filtro

[N,Wn]=ellipord(Wp, Ws, RpdB, RsdB);
[b,a]=ellip(N, RpdB, RsdB, Wn);


Si noti che Wp e Ws sono dei vettori, con componenti le frequenze che delimitano la banda
passante e le bande oscure. L’ordine del filtro risulta pari a due volte il valore N ritornato da
ellipord. In questo caso, è risultato N=4 e q = 8.

Esempio 7. Progetto di un filtro stop-banda (Fs = 8 kHz) con banda oscura [1.5,2.5] kHz e
banda passante negli intervalli [0,1] kHz e [3,4] kHz, Rs = 0.95 e Rp = 0.01.
% Parametri di progetto

Fs=8000;
RpdB=-20*log10(0.95);
RsdB=-20*log10(0.01);
Wp=[1000/Fs*2, 3000/Fs*2];
Ws=[1500/Fs*2, 2500/Fs*2];

% Progetto del filtro

[N,Wn]=ellipord(Wp, Ws, RpdB, RsdB);
[b,a]=ellip(N, RpdB, RsdB, Wn, ’stop’);


Si noti che Wp e Ws sono dei vettori, con componenti le frequenze che delimitano le bande
passanti e la banda oscura. Si noti inoltre l’uso del parametro ’stop’ in ingresso alla procedura
ellip. L’ordine del filtro risulta anche in questo caso pari a due volte il valore N ritornato da
ellipord. È risultato in questo esempio N=4 e q = 8.
     Altre procedure per il progetto di filtri IIR disponibili in MATLAB sono butter,
cheby1, cheby2, besself, invfreqz. In particolare, invfreqz permette il progetto di
filtri di cui si specifica sia il modulo che la fase.

Progetto di filtri FIR in MATLAB. I filtri FIR hanno alcuni svantaggi rispetto
ai filtri IIR ma anche alcuni importanti vantaggi. In generale, l’ordine di un filtro FIR
(ovvero il parametro r nella (5)) risulta in generale molto più grande dell’ordine di un
filtro IIR che soddisfa le stesse specifiche. D’altro canto, la durata del transitorio di un
filtro FIR è finita e pari alla durata della risposta impulsiva del filtro. Inoltre, esistono
metodi di progetto efficienti che garantiscono che il filtro FIR abbia esattamente fase
lineare. Come è noto, questo garantisce che una sinusoide in ingresso al filtro subisce
in uscita un ritardo indipendente dalla frequenza. Se dunque la risposta in frequenza
del filtro ha l’espressione
                                    H(f ) = e−j2πf t0 H0 (f ),
dove H0 (f ) vale 1 nella banda passante, e 0 altrove3 e il segnale di ingresso ha un’e-
stensione spettrale contenuta nella banda passante, l’uscita ha trasformata di Fourier
                              Y (f ) = H(f )X(f ) = e−j2πf t0 X(f ).
   3
     Dovendo H(f ) essere periodica di periodo 1/T , questo può avvenire solamente se t0 è un multiplo
di T .


                                                  13
Nel dominio del tempo, risulta y(t) = x(t − t0 ) e l’uscita è una versione non distorta
(secondo Heaviside) del segnale di ingresso.
    Un filtro FIR causale di durata N T a fase lineare (a tratti) soddisfa la condizione

                    h(nT ) = h((N − 1 − n)T ),      n = 0, ..., (N − 1)T.

La risposta impulsiva è dunque simmetrica, come evidenziato nelle Fig. 7a e 7b nel
caso di N pari e N dispari, rispettivamente. In questo caso, la risposta in frequenza
del filtro
                                      N
                                      X −1
                            H(f ) = T      h(nT )e−j2πf nT
                                          n=0
risulta, come è immediato verificare
                                              N −3                               
                                                 2
                                  NT − T                                   N −1
                                                                            
                       N −1                     X
            T e−j2πf T 2 h
          
                                             +2      h(nT ) cos 2πf T n −           , N dispari,
          
          
                                     2                                       2
          
          
          
          
                                               n=0
H(f ) =
          
                             N −2                                  
                                 2
                                                             N −1
                                                               
               −j2πf T N 2−1 
          
                               X
           Te
          
                             2     h(nT ) cos 2πf T n −              , N pari.
                                                               2
          
                              n=0

La risposta in frequenza è dunque uguale al prodotto di una funzione reale per un
fattore a fase lineare. Eventuali discontinuità di π nella fase possono presentarsi in
corrispondenza di cambi di segno della funzione reale (da cui la dizione fase lineare a
tratti). Per N dispari, è possibile progettare i coefficienti h(nT ) in modo che la funzione
reale sia circa uguale ad 1 in un certo intervallo di frequenze e 0 altrove, cosicchè un
ingresso con estensione spettrale contenuta nella banda passante si ritrova ritardato in
uscita di (N − 1)/2 campioni e praticamente non distorto.
    Se N è pari, (N −1)/2 non è un numero intero e l’uscita non può essere in nessun caso
una semplice versione ritardata dell’ingresso a tempo discreto. Tuttavia, se l’ingresso
è ottenuto per campionamento su Z(T ) di una forma d’onda continua xa (t), t ∈ R,
nell’ipotesi in cui l’estensione spettrale del segnale campionato sia contenuta nella banda
passante del filtro, l’uscita risulta pari a y(nT ) = xa (nT − T (N − 1)/2). Essa si ottiene
dunque per campionamento della versione del segnale a tempo continuo ritardato di
t0 = T (N − 1)/2.

Nota. Se N è pari risulta in ogni caso H(Fs /2) = 0, Fs = 1/T . Infatti, H(Fs /2) risulta
uguale all’area del segnale
                                          Fs
                             h(nT )e−j2π 2 nT = (−1)n h(nT )

che risulta nulla, data la simmetria di h(nT ) (vedi Fig. 7a).
    Non è dunque conveniente cercare di progettare un filtro FIR passa-alto a fase
lineare con un numero pari di campioni.

    Un’altra classe di filtri FIR la cui risposta in frequenza presenta un fattore a fase
lineare è quella dei filtri antisimmetrici, la cui risposta impulsiva verifica la condizione

                               h(nT ) = −h((N − 1 − n)T ).

                                               14
  che risulta nulla, data la simmetria di h(nT ) (vedi Fig. 7a).
      Non è dunque conveniente cercare di progettare un filtro FIR passa-alto a fase
  lineare con un numero pari di campioni.




     h(nT )      a)                            h(nT )      b)




                                              nT                                       nT


     h(nT )      c)                            h(nT )      d)




                                              nT                                       nT



  Figure 7: Andamenti della risposta impulsiva di filtri FIR simmetrici e antisimmetrici.
Figura 7: Andamenti della risposta impulsiva di filtri FIR simmetrici e antisimmetrici.
      Un’altra classe di filtri FIR la cui risposta in frequenza presenta un fattore a fase
Gli  andamenti   tipici
  lineare è quella  dei sono
                         filtri mostrati   nelle Fig.
                                 antisimmetrici,        7c risposta
                                                   la cui   e 7d perimpulsiva
                                                                      N pari e verifica
                                                                               N dispari    rispetti-
                                                                                        la condizione
vamente.
    La risposta in frequenza risulta  h(nT ) = −h((N − 1 − n)T ).
                                    N −3                                       
  Gli andamenti
                   tipici sono    mostrati
                                         2   nelle  Fig. 7c e 7d per N pari
                                                                       N −1    e N dispari rispetti-
                      −j2πf T N 2−1 
                                      X
  vamente.   −jT   e                2      h(nT  ) sin   2πf  T   n −            , N dispari,
           
                                                                         2
           
           
           
           
                                      n=0
 H(f ) =
           
                                    N −2           15                         
                                         2
                                                                       N −1
                                                                           
                      −j2πf T N 2−1 
           
                                      X
            −jT e                   2      h(nT ) sin 2πf T n −
           
                                                                                 , N pari.
                                                                         2
           
                                     n=0

    La risposta in frequenza risulta dunque il prodotto di un fattore a fase lineare e di
una funzione puramente immaginaria. In particolare, il fattore −j contribuisce ad una
fase costante di −π/2.

     Nota. Data l’antisimmetria, l’area della risposta impulsiva è nulla e risulta dunque
H(0) = 0. Non è dunque conveniente progettare un filtro passa-basso utilizzando filtri
FIR antisimmetrici.
     Per N dispari, risulta anche H(Fs /2) = 0, per cui il progetto di filtri passa-alto non
è consigliabile in questo caso.

    Il progetto di filtri FIR simmetrici in MATLAB si effettua utilizzando la procedura
                                     b = firpm(r, f, M, w).
Tale filtro, fornito dall’algoritmo di Remez, particolarizzato da Parks e McClellan al
progetto di filtri FIR, è ottimo nel senso che minimizza il massimo errore di approssi-

                                                15
mazione nelle varie bande a parità di specifiche. La risposta in frequenza presenta una
oscillazione uniforme nelle varie bande (ed è dunque, come si dice, di tipo equiripple).
I parametri di ingresso alla procedura sono

   1. l’ordine r del filtro, la cui risposta impulsiva risulta pertanto di lunghezza N =
      r + 1 campioni;

   2. un vettore di frequenze f, normalizzate rispetto a F2 /2, Fs = 1/T , che specifica le
      frequenze che delimitano le bande attenuate e oscure della risposta in frequenza;

   3. un vettore M che specifica le ampiezze desiderate alle frequenze specificate nel
      vettore f;

   4. un vettore di pesi w che specifica il rapporto fra le ampiezze degli errori di appros-
      simazione nelle varie bande. Se il filtro non è soddisfacente in termini di errore
      assoluto, occorre aumentare l’ordine del filtro.

    Il vettore b di r+1 elementi contiene i coefficienti del filtro, che includono la mol-
tiplicazione per il quanto temporale T . Il filtro può essere utilizzato per l’elaborazione
dell’ingresso posto nel vettore x mediante il comando filter(b,1,x).
Esempio 8. Supponiamo che la frequenza di campionamento del sistema numerico sia Fs = 8
kHz, e si voglia progettare un filtro FIR simmetrico passa-basso di ordine r = 18 con banda
passante da 0 a 1.6 kHz e banda oscura da 2.4 kHz a 4 kHz=Fs /2. Detto δp il massimo errore nel
modulo della risposta in frequenza in banda passante e δs il massimo errore in banda oscura, si
desidera che δp /δs = 2, ovvero si tollera un errore doppio in banda passante rispetto alla banda
oscura.
    Il progetto e la visualizzazione del filtro possono essere ottenuti con i seguenti comandi
MATLAB.

% Specifiche di progetto.

Fs=8000;
f=[0, 1600, 2400 4000]*2/Fs;
M=[1, 1,    0,   0];
w=[1, 2];
r=18;

% Progetto del filtro

b=firpm(r,f,M,w);

% Visualizzazione del filtro

[H,f]=freqz(b,1,512,Fs);
figure;
plot(f,abs(H));
figure;
plot(f,angle(H));

Il modulo e la fase della risposta in frequenza del filtro ottenuto sono mostrati nelle Fig. 8 e
9. Si noti che la fase è rappresentata modulo 2π e che si hanno discontinuità di π in banda
attenuata, corrispondenti a cambi di segno della risposta in frequenza. Una stima approssimata


                                               16
Il modulo e la fase della risposta in frequenza del filtro ottenuto sono mostrati nelle Fig. 8 e
9. Si noti che la fase è rappresentata modulo 2π e che si hanno discontinuità di π in banda
attenuata, corrispondenti a cambi di segno della risposta in frequenza. Una stima approssimata
della lunghezza del filtro FIR con banda di transizione ν = Ws − Wp (espressa in termini di
frequenze normalizzate rispetto a Fs ) e con massimi errori δp e δs in banda passante e banda
    dellapuò
oscura,   lunghezza  del filtro FIR
              essere ottenuta   dallacon  banda di
                                       relazione   transizione
                                                 empirica       ν = Ws − Wp (espressa in termini di
                                                            [4],[5]
    frequenze normalizzate rispetto a Fs ) e con massimi errori δp e δs in banda passante e banda
    oscura, può essere ottenuta dalla relazione
                                          −10 logempirica
                                                    (δ δ )[4],[5]
                                                            − 15
                                                              p s
                                      N ≃ −10 log10(δ δ ) − 15 + 1.
                                       N'         14νp s
                                                 10
                                                            + 1.
                                                14ν
Si può altrimenti
    Si può         usare
            altrimenti     la laprocedura
                       usare      proceduraMATLAB firpmord.
                                           MATLAB firpmord.


                         1.2



                          1



                         0.8



                         0.6



                         0.4



                         0.2



                          0
                           0    500      1000   1500   2000     2500   3000   3500   4000



  Figure 8: Modulo della risposta in frequenza del filtro FIR simmetrico (f in Hz).
       Figura 8: Modulo della risposta in frequenza del filtro FIR simmetrico (f in Hz).

                                                       17
                          4


                          3


                          2


                          1


                          0


                         −1


                         −2


                         −3


                         −4
                           0    500     1000    1500   2000     2500   3000   3500   4000



Figure 9: Fase (radianti) della risposta in frequenza del filtro FIR simmetrico (f in
   Figura 9: Fase (radianti) della risposta in frequenza del filtro FIR simmetrico (f in
Hz).
    Hz).

                                                                                                     ✷
    Esempio 9. Progetto di un filtro passa-alto con r + 1 = 19 coefficienti (Fs = 8 kHz) con banda
Esempio    9. Progetto
    oscura [0,1.5]        di unpassante
                   kHz e banda  filtro passa-alto  con
                                         [2.5,4] kHz,   r+
                                                      con un1errore
                                                              = 19 massimo
                                                                    coeﬃcienti (Fs =passante
                                                                           in banda  8 kHz) uguale
                                                                                             con banda
oscura [0,1.5]inkHz
    a quello        e banda
                 banda oscura.passante [2.5,4] kHz, con un errore massimo in banda passante uguale
a quello in banda oscura.
% Specifiche di progetto.                              17

Fs=8000;
f=[0, 1500, 2500, 4000]*2/Fs;
% Specifiche di progetto.

Fs=8000;
f=[0, 1500, 2500, 4000]*2/Fs;
M=[0, 0,    1,   1];
w=[1, 1];
r=18;

% Progetto del filtro

b=firpm(r,f,M,w);



Esempio 10. Progetto di un filtro multi banda con r +1 = 52 (Fs = 8 kHz) con bande passanti
[0,1] kHz, [2,3] kHz e bande oscure [1.2,1.8] kHz, [3.2,4] kHz. Nella banda [0,1] kHz si tollera
un errore pari a 1/2 di quello nelle bande [2,3] kHz e [3.2,4] kHz. Nella banda [1.2,1.8] kHz si
tollera un errore pari a 1/3 di quello nelle bande [2,3] kHz e [3.2,4] kHz.

% Specifiche di progetto.

Fs=8000;
f=[0, 1000, 1200, 1800, 2000, 3000, 3200, 4000]*2/Fs;
M=[1, 1,    0,    0,    1,    1,    0,    0];
w=[2,       3,          1,          1];
r=51;

% Progetto del filtro

b= firpm(r,f,M,w);



   Il progetto di filtri antisimmetrici in MATLAB si effettua ancora con la procedura
firpm, usando il parametro ’Hilbert’. Si considerino i seguenti esempi.
Esempio 11. Progetto di un filtro passa-alto anti-simmetrico con r+1 = 18 coefficienti (Fs = 8
kHz) con banda oscura [0,1.5] kHz e banda passante [2.5,4] kHz, con un errore massimo in banda
passante uguale a quello in banda oscura. È opportuno scegliere una lunghezza pari del filtro,
trattandosi di un filtro passa-alto antisimmetrico.

% Specifiche di progetto.

Fs=8000;
f=[0, 1500, 2500, 4000]*2/Fs;
M=[0, 0,    1,   1];
w=[1, 1];
r=17;

% Progetto del filtro

b= firpm(r,f,M,w,’Hilbert’);




                                              18
Esempio 12. L’uso della parola ’Hilbert’ deriva dal fatto che la fase costante −π/2 dovuta
alla presenza del fattore −j nella risposta in frequenza rende i filtri antisimmetrici adatti al
progetto di filtri di Hilbert discreti, con risposta in frequenza di modulo unitario a tutte le
frequenze e fase −π/2 per 0 < f < Fs /2. Per il progetto di un filtro di Hilbert di ordine 30 si
possono utilizzare i seguenti comandi

Fs=8000;
r=30;

b= firpm(r,[.1 0.9],[1 1],’Hilbert’)

Il filtro che si ottiene, a parte l’introduzione di un ritardo di 15 campioni, realizza approssima-
tivamente la risposta in frequenza desiderata, come si può vedere con i seguenti comandi

N=r+1;
[H,f]=freqz(b,1,512,Fs);
figure;
plot(f,abs(H));

% Disegna la fase, compensando il fattore corrispondente al ritardo
% dell’uscita.

figure;
plot(f,angle(H.*exp(j*2*pi*f/Fs*(N-1)/2)));




                                                19
                                         Esercizi

1. Progettare un filtro passa-basso IIR ellittico che soddisfa le seguenti specifiche
   (Fs =2 Hz): Rp = 0.98, Rs = 0.05, Wp = 0.6 Hz, Ws = 0.8 Hz. Si scriva una
   procedura per il calcolo dell’uscita e la si testi con gli ingressi x(t) = δZ(T ) (t), t ∈
   Z(T ) e x(t) = cos(2π0.4t)10 (t), t ∈ Z(T ). Si confrontino i propri risultati con
   quelli ottenuti usando la procedura filter.

2. Progettare un filtro passa-basso FIR a fase lineare che soddisfa le seguenti spe-
   cifiche (Fs =2 Hz): Rp = 0.98, Rs = 0.05, Wp = 0.6 Hz, Ws = 0.8 Hz. Si
   provino vari ordini del filtro finché le specifiche non sono soddisfatte esattamen-
   te. Si scriva una procedura per il calcolo dell’uscita e la si testi con gli ingressi
   x(t) = δZ(T ) (t), t ∈ Z(T ) e x(t) = cos(2π0.4t)10 (t), t ∈ Z(T ). Si confrontino i
   propri risultati con quelli ottenuti usando la procedura filter.

3. Progettare un filtro passa-basso IIR ellittico che soddisfa le seguenti specifiche
   (Fs = 1/T = 8 kHz): Rp = 0.95, Rs = 0.02, Wp = 1.84 kHz, Ws = 2.48 kHz.
   Dopo avere calcolato i poli della funzione di trasferimento con la procedura roots,
   si stimi la durata convenzionale della risposta impulsiva all’1%. Si consideri
   l’ingresso x(nT ) = 2 sin(2πf0 nT ) + cos(2πf1 nT ), con f0 = 1 kHz e f1 = 3.2 kHz
   e si valuti la risposta a regime permanente del filtro. Si confronti l’uscita con il
   segnale x1 (nT ) = 2 sin(2πf0 nT ).

4. Importanza della fase lineare. Progettare un filtro passa-basso IIR ellittico che
   soddisfa le seguenti specifiche (Fs = 1/T = 8 kHz): Rp = 0.95, Rs = 0.02,
   Wp = 2.4 kHz, Ws = 2.8 kHz. Si consideri l’ingresso x(nT ) = 2 sin(2πf0 nT ) +
   cos(2πf1 nT ), con f0 = 2.35 kHz e f1 = 1.5 kHz e si valuti la risposta a regime
   permanente del filtro. Si progetti un filtro FIR simmetrico che soddisfa alle stesse
   specifiche. Dopo avere confrontato l’ordine dei due filtri, si consideri l’uscita in
   regime permanente all’ingresso x(nT ). Si confrontino fra loro le uscite ottenute
   dai due filtri e l’ingresso x(nT ).

5. Notch filter. Si consideri un filtro con funzione di trasferimento

                      1 − 2 cos(2πf0 T )z −1 + z −2            1 − 2ρ cos(2πf0 T ) + ρ2
       Hz (z) = C                                     ,   C=                            .
                    1 − 2ρ cos(2πf0 T )z −1 + ρ2 z −2             2 − 2 cos(2πf0 T )

   Si valutino in forma chiusa i poli e gli zeri della funzione di trasferimento. e si
   disegni il modulo e la fase della risposta in frequenza al variare di 0 < ρ < 1 e
   0 < f0 < Fs /2 con Fs = 1/T . In particolare, si valuti la frequenza in cui H(f )
   si annulla, e si considerino valori di ρ prossimi a 1. Sia Fs = 8 kHz. Si progetti
   un filtro che elimini un eventuale tono sinusoidale a 50 Hz sovrapposto al segnale
   utile. Tale disturbo potrebbe essere generato da interferenze con la tensione di
   rete.

6. Nel file

    frase_8192.mat



                                            20
   sono contenuti i campioni di segnale vocale relativi alla frase “E soprattutto,
   forse, ciò che gli occhi da soli non avrebbero potuto vedere.” La frequenza di
   campionamento è Fs = 8192 Hz. Il file può essere caricato con il comando load
   ed i campioni vengono posti nel vettore orig.
   Il segnale vocale è costituito da una successione di suoni elementari detti fonemi:
   ad esempio alla parola “fonemi” corrisponde la successione dei suoni elementari
   /f/ /o/ /n/ /e/ /m/ /i/. Inoltre le vocali (e in generale anche le consonanti voca-
   lizzate, tipo “l”, “m”) hanno tipicamente un andamento quasi periodico. Questo
   contrasta con l’andamento irregolare e rumoroso delle fricative, tipo la “s” o la
   “f”. Infine, le plosive, tipo la “p” o la “b”, sono precedute da una pausa prima
   dell’emissione del suono. Nella frase che stiamo esaminando, si possono osservare
   le caratteristiche dei vari segmenti del segnale con il comando plot. Se l’elabo-
   ratore è fornito di scheda audio, è possibile da MATLAB ascoltare la frase o una
   sua parte con il comando sound.
   Nel file

    frase_r330.mat

   è contenuta una versione della frase corrotta “in fase di registrazione” aggiungendo
   al segnale un fastidioso tono a 330 Hz. Progettare un filtro notch che elimini tale
   disturbo.

7. Con riferimento all’esercizio precedente, nel file

    frase_r.mat

   è contenuta una versione della frase corrotta in fase di registrazione con un tono
   di frequenza non nota. Usando una tecnica di stima spettrale (ad esempio, il
   periodogramma), si stimi la frequenza della sinusoide sovrapposta al segnale e la
   si elimini con un filtro notch. Nota: il filtro notch è molto selettivo, ed è quindi
   importante determinare accuratamente la frequenza della sinusoide per poterla
   cancellare efficacemente.

8. Per ragioni tecniche, si vuole convertire la frequenza di campionamento del se-
   gnale vocale dell’esercizio 6 da 8192 Hz alla frequenza doppia 16384 Hz. Si rea-
   lizzi il convertitore di frequenza mediante interpolazione seguita da oppourtuno
   filtraggio.

9. Il segnale telefonico viene usualmente campionato a Fs = 8 kHz, ma la sua esten-
   sione spettrale può essere limitata senza perdita di intelligibilità a [-3.33, 3.33]
   kHz. Si progetti uno schema di interpolazione/campionamento per passare dalla
   frequenza Fs = =8 kHz alla frequenza Fs0 = 6.66 kHz. Occorre dunque interpolare
   il segnale di un fattore 5 e sottocampionare di un fattore 6 (usando un prefiltro).
   Il file

    frase_8000.mat

   contiene la frase dell’esercizio 6 acquisita con Fs =8 KHz.

                                         21
                                   Bibliografia

[1] A. Oppenheim, R. Schafer, “Digital Signal Processing”.

[2] A. Peled, B. Liu, “Digital Signal Processing”.

[3] G.C. Temes, S.K. Mitra, “Modern Filter Theory and Design”.

[4] R. Crochiere, L. Rabiner, “Multirate Digital Signal Processing”.

[5] L. Rabiner et al., “Some Comparisons between FIR and IIR Digital Filters”, Bell
    Systems Technical Journal, vol. 53, Feb. 1974.

[6] M. Bellanger, “Digital Processing of Signals”.




                                        22
