---
fonte: "dft_fft.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Uso della DFT e FFT
In questa lezione vengono proposti alcuni semplici esercizi riguardanti l’uso della FFT
per il calcolo della trasformata di Fourier di segnali a tempo discreto e a tempo continuo.
    Si ricorda che se x(t), t ∈ Z(T )/Z(N T ) è un segnale a tempo discreto di periodo
N T , la sua trasformata di Fourier ha l’espressione
                                   N
                                   X −1
                                                          nk           1
                      X(kF ) = T          x(nT )e−j2π N ,       F =      .             (1)
                                                                      NT
                                   n=0

La trasformata di Fourier X(kF ) risulta essere definita su Z(F )/Z(N F ) ed è quindi
completamente specificata dagli N valori assunti nell’insieme f ∈ {0, ..., (N − 1)F }. Il
segnale x(nT ) viene recuperato da X(kF ) mediante la formula di inversione
                                            N
                                            X −1
                                                                nk
                             x(nT ) = F              X(nF )ej2π N .                    (2)
                                            n=0

    L’algoritmo di FFT permette di calcolare, a partire dai valori {x(0), ...., x((N −
1)T )}, la sommatoria (1) in modo efficiente. In particolare, se N è una potenza di 2,
la (1) viene calcolata in O(N log2 N ) operazioni, il che consente una riduzione drastica
rispetto al calcolo diretto che richiede O(N 2 ) operazioni.
    La procedura MATLAB X=fft(x,N) calcola mediante un algoritmo di FFT la som-
matoria
                                         N
                                         X −1
                                                            nk
                             X(k + 1) =       x(n + 1)e−j2π N
                                           n=0
a partire da un vettore di ingresso x. Il risultato viene posto nel vettore di uscita X, di
dimensione N , che non è vincolato a essere una potenza di 2. Se il vettore di ingresso
ha dimensione minore di N , esso viene esteso aggiungendo in coda valori nulli. Si noti
che l’algoritmo di MATLAB suppone T =1, e che occorre in generale premoltiplicare
l’ingresso per T , ponendo x(n + 1) = T x(nT ).
    Per l’antitrasformata, si può usare la procedura MATLAB x=ifft(X), che calcola
in modo efficiente la sommatoria
                                             N −1
                                       1 X              nk
                            x(k + 1) =     X(n + 1)ej2π N
                                       N
                                             n=0

a partire dal vettore X di dimensione N . Nel caso T 6= 1, occorre porre X(n + 1) =
X(nF )/T .
    L’algoritmo di FFT può dunque essere utilizzato per il calcolo della trasformata di
Fourier di segnali a tempo discreto e periodici. Vedremo di seguito la possibilità di
utilizzarla per il calcolo della trasformata di segnali a tempo discreto non periodici e di
segnali continui.

    La Fast Fourier Transform (FFT). Come detto, la FFT è un algoritmo veloce
per il calcolo della DFT. Supponendo N pari, essa si basa sul fatto che la sommatoria
che calcola la DFT in (1) può essere scomposta in una coppia di DFT che coinvolgono
solo la metà dei valori x(kT ), ricomponendo opportunamente i risultati. Questo, come

                                                 1
vedremo, porta ad una riduzione della complessità. Supponendo che N sia una potenza
di due, possiamo inoltre ripetere il ragionamento e suddividere ulteriormente le DFT.
Procedendo in questo modo, come accennato, passiamo da una complessità pari a
O(N 2 ) ad una complessità pari a O(N log2 N ). La riduzione di complessità può essere
drammatica: ad es., già con N = 1024, la complessità si riduce di circa un fattore 100.
    La tecnica rientra nel principio generale denominato “divide and conquer” (dalla
locuzione latina “divide et impera” esplicitata per la prima volta per descrivere una
tecnica socio-politica romana per il governo dei territori conquistati) che, in Computer
Science, descrive algoritmi che operano ricorsivamente, suddividendo un problema in
sotto problemi di struttura simile ma più facili da risolvere.
    Algoritmo di decimazione nel tempo. Con riferimento all’Eq. (1), useremo
nel seguito la notazione semplificata xn ≡ T x(nT ), Xk ≡ X(kF ). L’algoritmo di FFT
qui presentato, dovuto a J. W. Cooley e J. W. Tukey1 , viene detto a “decimazione nel
tempo”, in quanto esegue il calcolo suddividendo l’insieme degli xn nei due sottoinsiemi
corrispondenti agli indici pari e dispari. Definiamo inoltre WN = e−j2π/N .
    Usando (1) e suddividendo la sommatoria, si ottiene
                                N/2−1                    N/2−1
                                 X                        X
                                             kn
                     Xk =               x2n WN/2 + WNk                  kn
                                                                 x2n+1 WN/2                    (3)
                                 n=0                      n=0
                           = Ek + WNk Ok ,

dove abbiamo sfruttato il fatto che WN2kn = WN/2      kn . La (3) appare come la somma

delle DFT calcolate sugli N/2 valori x0 , x2 , ..., xN −2 , e x1 , x3 , ..., xN −1 , combinate uti-
lizzando i cosiddetti “twiddle factor” WNk . Questa operazione ci permette di passare
da una complessità O(N 2 ) ad una complessità minore O(2(N/2)2 + N ), dove il costo
proporzionale a N corrisponde alle moltiplicazioni con i twiddle factor e alle somme
necessarie per ricombinare i risultati.
                       k+N/2
    Osservando che WN        = −WNk , e date le periodicità Ek = Ek+N/2 , Ok = Ok+N/2 ,
possiamo anche scrivere

                          Xk = Ek + WNk Ok , k = 0, 1, ..., N/2 − 1,                           (4)
                     Xk+N/2 =        Ek − WNk Ok ,   k = 0, 1, ..., N/2 − 1.

    La Fig. 1 mostra in forma grafica la procedura di calcolo corrispondente, nel caso
N = 8, in cui la somma e sottrazione presenti nell’Eq. (4) corrispondono ad una tipica
struttura denominata “farfalla” (butterfly in inglese).
    Come anticipato, il procedimento di suddivisione può essere iterato su ciascuna
delle sottosequenze di N/2 valori, suddividendole in due sottosequenze lunghe N/4
corrispondenti ai valori nelle posizioni pari e dispari, e combinando i risultati. Conti-
nuando in questo modo, si arriva al calcolo di N/2 DFT su due soli valori, che in base
alla definizione (1) si riducono alla semplice somma e differenza dei valori di ingresso.
Il grafo completo per il calcolo della FFT per N = 8 è mostrato in Fig. 2.
    Indicando con C(p) la complessità relativa al calcolo della FFT su N = 2p valori,
le considerazioni precedenti ci permettono di concludere che vale la seguente relazione
  1
   Cooley, James W.; Tukey, John W. (1965). “An algorithm for the machine calculation of complex
Fourier series”. Math. Comput. 19: 297301.


                                                2
           x[0]

           x[2]
                          N/2 point DFT
           x[4]

           x[6]

           x[1]

           x[3]
                          N/2 point DFT
           x[5]

           x[7]




Figure 1: Grafo della suddivisione della DFT in due DFT su N/2 valori (N = 8,
decimazione nel tempo).




     Figure 2: Grafo per il calcolo della FFT(N = 8, decimazione nel tempo).




                                       3
                                x[0]   000             000    x[0]
                                x[1]   001             100    x[4]
                                x[2]   010             010    x[2]
                                x[3]   011             110    x[6]
                                x[4]   100             001    x[1]
                                x[5]   101             101    x[5]
                                x[6]   110             011    x[3]
                                x[7]   111             111    x[7]


                        Figure 3: Ordinamento bit reverse (N = 8).


di ricorrenza
                             C(p) = 2C(p − 1) + 2p ,      C(1) = 2.
Posto S(p) = C(p)/2p , possiamo scrivere

                               S(p) = S(p − 1) + 1,      S(1) = 1,

che ha la ovvia soluzione S(p) = p, per cui C(p) = p2p . Essendo p = log2 N , la
complessità della FFT risulta dunque, come anticipato, pari a O(N log2 N ).
     Nell’implementazione dell’algoritmo di FFT in un linguaggio di programmazione, i
calcoli possono essere organizzati con riferimento ad un grafo del tipo di quello mostrato
in Fig. 2 per N = 8, con un ciclo interno per il calcolo di butterfly e moltiplicazioni
con i twiddle factor, ed uno esterno per i log2 N stadi della FFT. Per semplificare
l’accesso ai dati, il vettore di ingresso viene tipicamente pre-ordinato, come premessa al
calcolo vero e proprio, in modo da contenere i valori nell’ordine richiesto dall’algoritmo,
corrispondente alla suddivisione ricorsiva degli indici nelle posizione pari e dispari. La
Fig. 2 mostra l’ordine di caricamento richiesto, [x0 , x4 , x2 , x6 , x1 , x5 , x3 , x7 ], nel caso
N = 8.
     Nel caso generale, l’ordinamento può essere effettuato con complessità O(N ) sulla
base del seguente ragionamento. Se pensiamo di rappresentare gli indici con notazione
binaria, la prima suddivisione corrisponderà ad avere nelle prime N/2 posizioni gli indici
pari, il cui bit meno significativo è 0, mentre nelle posizioni da N/2 a N − 1 avremo
gli indici dispari, il cui bit meno significativo è 1. Considerando poi ciascun insieme
degli N/2 indici pari o dispari, la successiva suddivisione posizionerà nelle prime N/4
posizioni gli indici in cui il secondo bit meno significativo è 0, mentre nelle successive
N/4 posizioni dovranno essere collocati gli indici il cui secondo bit è 1. La procedura
continua fino a considerare insiemi di due indici, ed è esemplificata per N = 8 in
Fig. 3. Si osserva (vedi Fig. 3) che la procedura suddetta corrisponde ad una inversione
dei bit (bit reverse) degli indici originari, in quanto può essere ottenuta, a partire
dall’indice 0, sommando 1 al bit più significativo e propagando l’eventuale riporto verso
destra anziché verso sinistra come avviene nell’usuale operazione di somma. Dato che
è sufficiente fare tale operazione una sola volta per il calcolo dell’indice successivo, e
spostare il dato del vettore originario, la procedura di bit reverse ha come anticipato
complessità O(N ).
     Algoritmo di decimazione in frequenza. Una procedura alternativa a quella
vista in precedenza, consiste nel suddividere la sommatoria (1) calcolando prima i

                                                4
                                                                        dispari.scrivere   In questo caso, dato                          Xche la suddivisione in indici                             X pari e dispari vie
                                                                        valori        della       trasformata,          X2k si     = opera         = una0N/2cosiddetta1
                                                                                                                                                                        xn WN/2    k
                                                                                                                                                                                           n+
                                                                                                                                                                                           “decimazione      = 0N/2in 1frequenza”xn+N/2 W
                                                           X2k , quindi corrispondenti ad indicinpari, e poi i valoriN/2                                                                 X2k+1  1 n
                                                                                                                                                                                                         corrispondenti                  agli in
                                                                                                                                                                                                                                     N/2 1
                                                           dispari.scrivere In questo caso, dato                       Xche la suddivisione in hindici                             X    X pari e dispari viene                         Xfatt
                                                                                                                                                                                                              kn                 k
                                                                                                      X2kindici   = opera         = una 0eN/2    X2k+1
                                                                                                                                                     1              =
                                                                                                                                                                    k       W+N              = 0xN/2  n WN/2   1            WN k n, x
                                              X2k , quindi valoricorrispondenti
                                                                       della trasformata,             ad          si          pari,            poi     ixvalori
                                                                                                                                                           n WN/2X
                                                                                                                                                  cosiddetta              n
                                                                                                                                                                          “decimazione
                                                                                                                                                                      N/2 2k+1 1        corrispondenti
                                                                                                                                                                                        n=0
                                                                                                                                                                                                                 xn+N/2
                                                                                                                                                                                                          in frequenza”.
                                                                                                                                                                                                                      N/2  agli1Windici
                                                                                                                                                                                                                                     N/2 Possi
                                                                                                                                                                                                                                       n=0
                                                                                                                           n                                            X n                                               X
                                              dispari.scrivere
                                                             In questo caso, dato                     X      che la suddivisione
                                                                                                                               X2k+1               =       in     indici
                                                                                                                                                                  h X
                                                                                                                                                            WN= Ek x+          pari        e   dispari
                                                                                                                                                                                               kn
                                                                                                                                                                                               k               viene
                                                                                                                                                                                                                 k            fatta     sui
                                                                                                                                                                                     n WN/2   N1 Ok , WN k                         x2n+1 WN
                                  X2k , quindivaloricorrispondenti
                                                         della trasformata,           X2kindici
                                                                                      ad        = opera
                                                                                                si               =una
                                                                                                             pari,    0N/2
                                                                                                                         e poi
                                                                                                                                     1
                                                                                                                                       ixvalori
                                                                                                                                cosiddettan WN/2X
                                                                                                                                                   k
                                                                                                                                                          n + n=0
                                                                                                                                                         “decimazione       = 0N/2
                                                                                                                                                                         corrispondenti          xn+N/2
                                                                                                                                                                                          in frequenza”.   agli1WindiciN/2    n,
                                                                                                                                                                                                                            Possiamo
                                                                                                                                                                                                                          n=0
                                                                                                                                                     N/2 2k+1   1                                     N/2
                                  dispari.scrivereIn questo caso, dato               Xche la suddivisione
                                                                                                          n
                                                                                                                                                   X
                                                                                                                                           in hindici   X pari        n k                               Xfatta sui
                                                                                                       N/2    X2k+11              = nW
                                                                                                                                  k
                                                                                                                                                   =        Ek x+       WeNkn
                                                                                                                                                                      n WN/2
                                                                                                                                                                     N/2
                                                                                                                                                                               dispari
                                                                                                                                                                                 O , viene
                                                                                                                                                                              1 k WN k
                                                                                                                                                                                                 k
                                                                                                                                                                                                                   x2n+1 WN/2        kn
                                                                      X         =             =     0                x     W                  +  N          =     0              x               W            n,
                                  valoricorrispondenti
                       X2k , quindi          della trasformata,       ad2kindici si opera  pari,una    e poi    cosiddetta
                                                                                                                     i valori
                                                                                                                        n N/2X                 X[0]
                                                                                                                                          “decimazione
                                                                                                                                            2k+1              X[2]
                                                                                                                                                        corrispondenti    in  X[4]
                                                                                                                                                                               frequenza”.
                                                                                                                                                                                   n+N/2   agliX[6] indici
                                                                                                                                                                                                       N/2    X[1]
                                                                                                                                                                                                            Possiamo           X[3]         X[5
                                                                                        n                                           N/2 1 nn=0                                       N/2 1              n=0
                       dispari.scrivere
                                     In questo caso, dato             X    che      la    suddivisione                   in      indici X
                                                                                                                                   X Ek x       pari      e   kdispari         viene    X     fatta       sui
                                                                                                                                 h=                +nW        knOk ,             k                                    kn
                                                          X2kindici
                                                                  = opera       =una0eN/2   X     1
                                                                                                 2k+1            =
                                                                                                                 k
                                                                                                                        nWX[0]              =X[2]
                                                                                                                             +N corrispondenti    0N/2  WinN   1
                                                                                                                                                              X[4]         WX[6]NW k Possiamo  X[1]x2n+1X[3]    WN/2           X[5] X[7
                       valoricorrispondenti
                                della trasformata,               si                                ixvalori
                                                                                             cosiddettan WN/2X         “decimazione                               xn+N/2
                                                                                                                                                               frequenza”.                     n,
                                                                                                                                                             N/2
               X2k , quindi                              ad                pari,           poi                    Segnali  2k+1
                                                                                                                   N/2 1 nn=0            a    tempo              discreto.agli
                                                                                                                                                                      N/2 1
                                                                                                                                                                                   indici
                                                                                                                                                                                      N/2Se
                                                                                                                                                                                        n=0     x(nT        ),  t   2     Z(T ) è un seg
                       scrivere
               dispari. In questo caso, dato che laN/2   X          N/2  n
                                                                                point
                                                                          suddivisione           DFT    in       X   X
                                                                                                                indici pari               e kn                          X
                                                                                                         generale               non           kdispari viene
                                                                                                                                          periodico,              con        fatta sui contenuta                            in {0, ...,
                                                                                                                                                                       k estensione                                                     (5)(N
                                                                                                               h
                                             X2k si  = opera        0 X
                                                                = una             1
                                                                                 2k+1
                                                                                    xn WN/2   =k
                                                                                                      nW+     N= E            k0x
                                                                                                                          =X[2]   + n WN/2
                                                                                                                                   N/2       N1 x Ok , WNkW                  n,   x2n+1 WN/2          kn
               valori della trasformata,                                     cosiddetta                  FFTX[0]
                                                                                                      “decimazione
                                                                                                Segnali               a
                                                                                                                      per   tempo        in
                                                                                                                                 calcolare    X[4]
                                                                                                                                               frequenza”.
                                                                                                                                                    n+N/2
                                                                                                                                                discreto.
                                                                                                                                                      i       X[6]N/2
                                                                                                                                                         campioni        Se   X[1]
                                                                                                                                                                           Possiamo
                                                                                                                                                                               x(nT
                                                                                                                                                                               della        ),
                                                                                                                                                                                            suaX[3]
                                                                                                                                                                                                t  2    Z(T   X[5]
                                                                                                                                                                                                     trasformata  )   è   un  X[7]
                                                                                                                                                                                                                                 segnale
                                                                                                                                                                                                                                 di  Fourier   a
                                                           n                                     N/2 1 nn=0                                          N/2 1 n=0
               scrivere                      X                                          generale
                                                                                               X    X    di   non       periodico,
                                                                                                                 trasformata,
                                                                                                                            kkn                 sicon   X  estensione
                                                                                                                                                     ottiene                       contenuta               in    {0,      ...,  (N       1)T    }
                                                                                             h=         Ek +         W 1 O k , WN k              k                                   kn
                                X2k =               = 0N/2X2k+1   1
                                                                    xn WN/2    k= WN
                                                                                     nFFT +
                                                                                          X[0]      per  =X[2]  0xN/2
                                                                                                                    n WN
                                                                                                               calcolare    N/2 xn+N/2
                                                                                                                             X[4]    i   campioniWN/2 n,
                                                                                                                                               X[6]            della
                                                                                                                                                              X[1]
                                                                                                                                                                    x2n+1 WN/2
                                                                                                                                                                            sua
                                                                                                                                                                              X[3]  trasformataX[5]              di
                                                                                                                                                                                                              X[7]
                                                                                                                                                                                                                           (5)
                                                                                                                                                                                                                       Fourier.          Infatt
                                                                                Segnali
                                                                                 N/2 1               a tempo discreto.
                                                                                                    n=0                             N/2 1 +1             Se x(nT ), t 2 Z(T ) è un
                                                                                                                                                        n=0                                                  N   segnale a tempo
                                               n                                    X   dinon     n
                                                                                              trasformata,                     si       X X
                                                                                                                                    ottiene                                                                  X1
                                                                        generale
                                                                             h                        periodico,
                                                                                                            kn
                                                                                                            k                   kcon      estensione                contenuta
                                                                                                                                                                      kn          j2⇡fin    nT {0, ..., (N                  1)T)e  }, possia
                                                                                                                                                                                                                                        j2⇡f nT
                                                  X2k+1 = W                 N   =       E  k  x+ n  W      N k
                                                                                                          N/2   O    ,  X(f
                                                                                                                         W     N   )   =     T     x 2n+1      x(kT
                                                                                                                                                                W    N/2   )e                     =     T (5)          x(nT
                                                                          X[0]n=0
                                                                        FFT         per   X[2]
                                                                                             calcolare      X[4]i campioni   X[6]             X[1]
                                                                                                                                               della          X[3]
                                                                                                                                                            sua               X[5]
                                                                                                                                                                     trasformata               X[7]
                                                                                                                                                                                                 di    Fourier.             Infatti,      dalla
                                                                 Segnali
                                                                  N/2 1              a tempo discreto.             N/2 1 X          +1   Se x(nT
                                                                                                                                        n=0       n= 1      ), t 2 Z(T ) è un               NX  segnale
                                                                                                                                                                                                    1        n=0a tempo discret
                                                                    X   di    trasformata,k                   si     X
                                                                                                                   ottiene                                         j2⇡f nT                                                 j2⇡f nT
                                     X2k+1 = W             generale
                                                               h= Eknon
                                                                              x+n W W     knOk , X(f
                                                                                      periodico,
                                                                                         N              W         ) =estensione
                                                                                                               kcon        T x                 x(kT  kn )e
                                                                                                                                                   contenuta
                                                                                                                                                Wrelazione                 in {0, =T    ...,
                                                                                                                                                                                          (5)(N        x(nT1)T)e    }, possiamo        , usa  f2
                                                               N
                                                             X[0]          X[2]          N/2
                                                                                           X[4]          Se   Ncalcoliamo
                                                                                                            X[6]
                                                                                                                                     2n+1   laX[3]  N/2                 precedente                per f = kF , dove F =
                                                           FFT
                                                     Segnali        per
                                                                     a tempo
                                                                    n=0      calcolare            i campioni
                                                                                            discreto.             +1  Se X[1]
                                                                                                                     n=0      della
                                                                                                                                 n= 1
                                                                                                                              x(nT         sua
                                                                                                                                           ),           Z(TX[5]
                                                                                                                                                t 2trasformata    ) è unNX[7]   di   Fourier.
                                                                                                                                                                                 segnale
                                                                                                                                                                                   1
                                                                                                                                                                                              n=0  a tempo Infatti,          dalla definiz
                                                                                                                                                                                                                         discreto,        in
                                                                                                                  X                                                          X
                                              generale
                                                    = E    dinon    N/2   k point
                                                                trasformata,
                                                                      periodico,
                                                              k + WN Ok , X(f           Se      )DFT
                                                                                            siconottiene
                                                                                                   =estensione
                                                                                               calcoliamo T                la x(kTcontenuta
                                                                                                                                          )e j2⇡f
                                                                                                                                  relazione
                                                                                                                                                           nT {0, ..., (N
                                                                                                                                                           in
                                                                                                                                                        precedente = T per            x(nT 1)T)e
                                                                                                                                                                                            f = kF
                                                                                                                                                                                                   },NX  possiamo
                                                                                                                                                                                                          j2⇡f1 nT
                                                                                                                                                                                                            , dove, F f=j2⇡
                                                                                                                                                                                                                               usare21/N  la
                                                                                                                                                                                                                                        R/Z(
                                                                                                                                                                                                                                         nk T ,
                                                X[0]
                                              FFT per        X[2]
                                                               calcolare  X[4]            X[6]
                                                                                  i campioni                X[1]
                                                                                                             della       sua X[3]  trasformataX[5]            X[7]
                                                                                                                                                                 di         X(kF
                                                                                                                                                                      Fourier.            )Infatti,
                                                                                                                                                                                              = T discreto, dallax(nT        )e
                                                                                                                                                                                                                          definizione     N ,
                                         Segnali        a tempo             discreto.            +1  Se         n= 1
                                                                                                              x(nT        ),   t  2     Z(T       )  è   un N   segnale     n=0a tempo                                      in
                                              dinon trasformata,            siconottiene        X                                                            X1                               1 nT n=0 usare la
                                  generale               periodico,    X(f       )  =  estensione
                                                                                         T                   x(kT contenuta
                                                                                                                         )e       j2⇡fin   nT {0, ..., (N
                                                                                                                                                   =    T             x(nT 1)T)e   },NX  possiamo
                                                                                                                                                                                           j2⇡f
                                                                                                                                                                                                        , F f=j2⇡    2 R/Z(1/T
                                                                                                                                                                                                                            nk              ).
                                    X[0]        X[2]         X[4]       SeX[6]  calcoliamoX[1]            laX[3] relazione   X[5]       precedente
                                                                                                                                              X[7]          X(kF  per    ) f==TkF , dove         x(nT       )e 1/N           N ,T , ottenia
                                  FFT per
                            Segnali         a tempocalcolare       i campioni
                                                              discreto.          +1 Se x(nTdella
                                                                                              n= 1      sua
                                                                                                        ),
                                                                                                         che  t 2trasformata
                                                                                                                     Z(T
                                                                                                                    ha       la  ) stessa
                                                                                                                                    è un   N    di1struttura
                                                                                                                                                      Fourier.
                                                                                                                                                 segnale     n=0   a tempo Infatti,
                                                                                                                                                                           della             dalla
                                                                                                                                                                                       discreto,
                                                                                                                                                                                         (1).            definizione
                                                                                                                                                                                                            in
                                                                                                                                                                                                      Dunque,               N     campion
                                                                                X                                                           X
                                                                                                                                                                                  nT n=0usare la
                       generaledinon    trasformata,
                                             periodico,  X(f  sicon
                                                                 )ottiene
                                                                    =estensione
                                                                         T                 x(kTcontenuta
                                                                                                       )eX(kF    j2⇡fin
                                                                                                                       ),nTk{0,   =T
                                                                                                                                  =     ...,   (N(N
                                                                                                                                         0, ...,     x(nT  1)T)e    },NX
                                                                                                                                                                   1)F   possiamo
                                                                                                                                                                         j2⇡f
                                                                                                                                                                           , 1possono   , fessere    2 R/Z(1/T
                                                                                                                                                                                                           nk calcolati        ). usando
                       FFT per         calcolare           Se
                                                      i campioni calcoliamo             la    relazione               precedente                  per      f    =     kF    ,  dove         F)e =j2⇡   1/N N ,T , otteniamo pro
                   Segnali     a tempo            discreto.       +1 Se della
                                                                           x(nT
                                                                             n= 1      sua t 2trasformata
                                                                                       ),che      haZ(T     la) stessa
                                                                                                         siamo     è un        di
                                                                                                                          infittire
                                                                                                                           N
                                                                                                                                     Fourier.
                                                                                                                                segnale
                                                                                                                                   1
                                                                                                                                           X(kF
                                                                                                                                   strutturan=0          )Infatti,
                                                                                                                                               i acampioni
                                                                                                                                                      tempo  = T discreto,
                                                                                                                                                            della         indalla
                                                                                                                                                                         (1).   x(nT    definizione
                                                                                                                                                                                 cuiDunque,
                                                                                                                                                                                          viene
                                                                                                                                                                                             in calcolata  N       campioni             in un
                                                                                                                                                                                                                               la trasform
                                                                  X                                                         X
               generaledinon
                           trasformata,
                                periodico,   X(f
                                                  sicon
                                                     ottiene
                                                     )  = estensione
                                                            T               x(kT        X(kF
                                                                                contenuta
                                                                                       )e      j2⇡f),  in
                                                                                                        nT  k{0, = ...,
                                                                                                         aumentando
                                                                                                                 =    0, ...,
                                                                                                                      T      (N(N    x(nT 1)T     1)F
                                                                                                                                          la dimensione
                                                                                                                                                   },NX
                                                                                                                                                  )e     possiamo
                                                                                                                                                          j2⇡f     nTn=0da
                                                                                                                                                           , 1possono   ,         essere
                                                                                                                                                                               usare
                                                                                                                                                                                f   2        laa calcolati
                                                                                                                                                                                      NR/Z(1/T     M >). Nusando          : in tale    la FFT cas
Figure 4: Grafo      della suddivisione
               FFT per calcolare i campioni
                                                         della
                                              Se calcoliamo
                                                             della
                                                                      DFT
                                                                        la relazione
                                                                        sua
                                                                                      insiamo
                                                                                 trasformata
                                                                                              due        x(N
                                                                                                             DFT
                                                                                                    precedente
                                                                                                        infittire
                                                                                                              di    T  ),
                                                                                                                    Fourier.
                                                                                                                              su
                                                                                                                              i
                                                                                                                             ...,
                                                                                                                          X(kF
                                                                                                                                 perN/2
                                                                                                                                  campioni
                                                                                                                                    x((M )
                                                                                                                                          f = kF
                                                                                                                                          Infatti,
                                                                                                                                            =     T
                                                                                                                                                     valori
                                                                                                                                                      1)T in
                                                                                                                                                            , dove(N
                                                                                                                                                               )
                                                                                                                                                            dallacuida
                                                                                                                                                                 x(nT
                                                                                                                                                                           F ==
                                                                                                                                                                         viene
                                                                                                                                                                          usare
                                                                                                                                                                        definizione
                                                                                                                                                                            )e     j2⇡1/N
                                                                                                                                                                                       per
                                                                                                                                                                                            8,
                                                                                                                                                                                            nk  T , otteniamo proprio
                                                                                                                                                                                        calcolata
                                                                                                                                                                                            N ,il calcolo     la     trasformata
                                                                                                                                                                                                                      usando          la   (1) Xs
                                                     +1
                                                     X          n= 1    che ha la stessa                 NX1struttura       n=0            della (1). Dunque, N campioni in un period
decimazione indi frequenza).                                                            aumentando                       la      dimensione                   da      N      a     M         >
                  trasformata,       si
                                X(f ) = Tottiene             x(kT )e          j2⇡f nT
                                                                        X(kF ), k =                      a
                                                                                               = T0, ..., (N   zero.x(nT )e      1)F NX
                                                                                                                                         j2⇡f     nT
                                                                                                                                          , 1possono   n=0
                                                                                                                                                        , fessere    2 R/Z(1/T   calcolati     ). usando la FFT. Si ca
                                                                                                                                                                                                   N    :     in      tale       caso,      i  no
                                  Se calcoliamo            la   relazione           precedente
                                                                                        x(N       T   ),X(kF...,perx((M
                                                                                                                  Se  )  f
                                                                                                                         il
                                                                                                                          =    =    kF
                                                                                                                              segnale
                                                                                                                                 T    1)T   ,  )dove
                                                                                                                                                   da
                                                                                                                                                  x(nT
                                                                                                                                                x(nT        F
                                                                                                                                                          usare
                                                                                                                                                             )
                                                                                                                                                            )e   =
                                                                                                                                                                 ha j2⇡1/N
                                                                                                                                                                       per
                                                                                                                                                                           nk
                                                                                                                                                                        durata ,T
                                                                                                                                                                                il ,   otteniamo
                                                                                                                                                                                    calcolo
                                                                                                                                                                                         finita       D proprio
                                                                                                                                                                                                      usando     N Tla, (1)   maX(f sono
                                                                                                                                                                                                                                    la sua    evi
                                                                                                                                                                                                                                                e
                                         +1
                                                   n= 1                 siamo
                                                           che ha la stessa            infittire
                                                                                        N
                                                                                                          n=0i   campioni                in      cui     viene
                                                                                               1struttura della (1). Dunque, N campioni in un periodo di X              calcolata
                                                                                                                                                                           N
                                                                                                                                                                                               la   trasformata                          )   sem
                                         X                                              aX  zero.        nel       periodo            n=0{0,     ..., (N              1)T    },     occorre             osservare              che     ai   fini
                      X(f
valori X2k , corrispondenti ) = Tagli indici   lax(kT     )e
                                                           X(kF
                                                           pari       ),aumentando
                                                                j2⇡f nT
                                                                     dellak=    = Ttrasformata,
                                                                                     0, ...,per   x(nT
                                                                                                 (N    la dimensione
                                                                                                             =)e1)F N  j2⇡f       nT
                                                                                                                         ,, 1possono    ,F   da     2N
                                                                                                                                                f=essere     aX
                                                                                                                                                         R/Z(1/T    M >).,Ncor-
                                                                                                                                                                  calcolati             : in tale
                                                                                                                                                                                      usando            la FFT. caso, Sii campioninoti che
                       Se calcoliamo                relazione       precedente
                                                                        x(N       T  ),   ...,
                                                                                       X(kF
                                                                                                Se
                                                                                                 x((M )
                                                                                                       filX(kF
                                                                                                          =      T
                                                                                                                   kF
                                                                                                             segnale X
                                                                                                                    1)T),e    )
                                                                                                                                poi
                                                                                                                             kdove
                                                                                                                                 x(nT
                                                                                                                                  =
                                                                                                                                  da
                                                                                                                                x(nT
                                                                                                                                           i...,
                                                                                                                                             ) valori
                                                                                                                                        0,usare
                                                                                                                                            )e
                                                                                                                                                 ha(N 1/N
                                                                                                                                                    j2⇡per
                                                                                                                                                           nk T
                                                                                                                                                        durata   1)F, 2k+1
                                                                                                                                                                       otteniamo
                                                                                                                                                                        finita
                                                                                                                                                                         , possiamo  D proprio  Nconsiderare
                                                                                                                                                            N ,il calcolo usando la (1) sono evidentem
                                                                                                                                                                                                       T , ma la sua               estensio
                                                                                                                                                                                                                               la versione
                                       n= 1   chequesto    siamo
                                                      ha la stessa      infittire
                                                                                struttura  i   campioni della          in
                                                                                                                      (1).      cui      viene
                                                                                                                                    Dunque,             calcolata
                                                                                                                                                           N},indici
                                                                                                                                                                   campioni   la    trasformata
                                                                                                                                                                                          ine un periodo         X(f        )   semplicem
                                                                                                                                                                                                                             difini
                                                                                                                                                                                                                                  X(f  del), ca
                                                                                         n=0
rispondenti agli indici dispari. In                                caso,a
                                                                                 dato
                                                                             zero.      nel che  periodo dilaingresso
                                                                                                                   suddivisione
                                                                                                                      {0,       ...,  (N             1)Tin
                                                                                                                     n=0da N a M > N : in tale caso, i campioni aggiu
                                                                                                                                                                     occorre    pari   osservare              che        ai
                                              X(kF       ),aumentando
                                                             k  =    0,   ...,   (N    la 1)F     N
                                                                                              dimensione
                                                                                                   X   ,   1possono              essere          calcolati            usando            la     FFT.         Si     noti       che     pos-
dispari viene fatta   sui valori
               Se calcoliamo             della trasformata,
                                  la relazione          precedente            persi)filopera
                                                                                Se         =TkF ,una
                                                                                        X(kF
                                                                                        =segnale
                                                                                                      ),    kdove=
                                                                                                               x(nT  cosiddetta
                                                                                                                     0,    ...,
                                                                                                                         F)e
                                                                                                                           ) ha    (N
                                                                                                                                =j2⇡ 1/N  nk 1)F
                                                                                                                                                     “decimazione
                                                                                                                                                         ,
                                                                                                                                          N ,T , otteniamo
                                                                                                                                       durata               possiamo
                                                                                                                                                        finita        D proprio N Tp ,in
                                                                                                                                                                                  considerare
                                                                                                                                                                                   x      (nT     )
                                                                                                                                                                                              maX(f   =    per
                                                                                                                                                                                                      la sua  la   Nversione
                                                                                                                                                                                                                           x(nT
                                                                                                                                                                                                                    estensione
                                                                                                                                                                                                                       T            ).periodi
                                                                                                                                                                                                                                          non
                                  che hasiamo    la stessainfittireT ),X(kF
                                                           x(Nstruttura   ...,   x((M
                                                                           i campioni  della       1)Tin )x(nT
                                                                                                     (1).     cuida    usare
                                                                                                                       viene
                                                                                                                   Dunque,            per  N},ilcampioni
                                                                                                                                      calcolata     calcolo           usando
                                                                                                                                                                          in un laperiodo
                                                                                                                                                              la trasformata                  (1)    sono        evidentemente
                                                                                                                                                                                                           )disemplicemente
                                                                                                                                                                                                                    X(f       ), calcolo ug
frequenza”.                                                             nel      periododi ingresso  {0,      ...,  (N              1)T             occorre            osservare               che      ai    fini       del                   d
                                                                                                   n=0   Infatti,   N asecalcolati x(nT    >) N    ha: estensione                  contenuta                in {n0 aggiuntivi
                                                                                                                                                                                                                           T, (n0 + 1)T,
                                                 k = 0,a...,
                                  X(kF ),aumentando            zero.
                                                                  (NlaX(kF   dimensione
                                                                              1)F  N
                                                                                   X ),, 1kpossono
                                                                                              =     0,
                                                                                                           daessere
                                                                                                          ...,    (N
                                                                                                                                  M
                                                                                                                        nk 1)F , possiamo             usando in xtale
                                                                                                                                                                       pla
                                                                                                                                                                         (nT
                                                                                                                                                                   considerare
                                                                                                                                                                               caso,
                                                                                                                                                                              FFT.) = per    Sii campioni
                                                                                                                                                                                               la  notiT x(nT
                                                                                                                                                                                                    versione  che).pos-  periodicizzata
    Possiamo scrivere                         x(Nstruttura
                                                      T ),X(kF
                                                            ..., Se  )il
                                                                  x((M   =segnale
                                                                              T 1)T          x(nT         ) ha perj2⇡durata             finita       Din un     N Tlaperiodo
                                                                                                                                                                          , (1)
                                                                                                                                                                             ma sono la sua       N
                                                                                                                                                                                                    estensione               nonuguali
                                                                                                                                                                                                                                     è conte
                       che ha siamo la stessa infittire      i campionidella
                                                                        di ingresso  in )x(nT
                                                                                    (1).      da
                                                                                             cui      usare
                                                                                                 Dunque, )e
                                                                                                      viene              N ,il calcolo
                                                                                                                     calcolata
                                                                                                                         N        campioni           usando
                                                                                                                                              la trasformata         n0 X+N X(f    1
                                                                                                                                                                                                evidentemente
                                                                                                                                                                                            )disemplicemente
                                                                                                                                                                                                   X(f       ),                      NX    1
                                              a   zero.    nel    periodo            {0,
                                                                                   n=0  Infatti,
                                                                                            ...,   (N       se x(nT1)T      }, ) haoccorreestensione  osservare     contenuta che       ai  infini{n0del  T,
                                                                                                                                                                                                          j2⇡nT(ncalcolo
                                                                                                                                                                                                                     0kF + 1)T,   dei ...,camp
                                                                                                                                                                                                                                            (n0
                       X(kF ),aumentando    0, ..., (N la 1)F
                                    k = N/2−1                   dimensione
                                                                       , possono N/2−1    daessereN a calcolati  M > Nusando            :X(kF in xtale )la =     caso,
                                                                                                                                                              FFT.
                                                                                                                                                                 T          Sii   campioni
                                                                                                                                                                                  notix(nT    che )e      aggiuntivi
                                                                                                                                                                                                       pos-                  =    T           xp (
                                             X Se ilX(kF     segnale  ),  k   =
                                                                             x(nT   X
                                                                                    0,   ...,  (N
                                                                                         ) ha calcolata
                                                                                                   durata      1)F     ,
                                                                                                                     finitapossiamo D       NnTla+N  p  (nT
                                                                                                                                                   considerare
                                                                                                                                                         , ma     )   =
                                                                                                                                                                     lan=n per
                                                                                                                                                                           suala  N       x(nT
                                                                                                                                                                                   versione           ).
                                                                                                                                                                                   estensione nonuguali
                                                                                                                                                                                      T                 periodicizzata èN contenuta   del    seg
               che ha siamo       x(Nstruttura
                                 infittire T ), ...,
                                                 i   x((M
                                                    campioni       1)T
                                                                  kn  in   )cui da    usare
                                                                                     viene         per        ilcampioni
                                                                                                                   calcolo  la       usando
                                                                                                                             kn trasformata                  (1)X(f 1sono  )    0evidentemente
                                                                                                                                                                               semplicemente                                  1       n=0
                        X2k =
                        la   stessa                    x  ndiW
                                                          della
                                                     periodo {0,
                                              neldimensione
                                                                    (1).
                                                                ingresso   +...,N
                                                                                 Dunque,
                                                                                   (N ase M      x      N
                                                                                                    n+N/2
                                                                                                 1)T>},) N           W
                                                                                                                  occorre            ,   in
                                                                                                                                      osservare
                                                                                                                                                un     0periodo
                                                                                                                                                         X    che x(nT
                                                                                                                                                                            di
                                                                                                                                                                       aiinfini
                                                                                                                                                                                  X(f         ),                         X
                                                                                                                                                                                       0del      calcolo          Tdei...,campioni
                                                                 N/2    Infatti,                x(nT              ha        N/2
                                                                                                                         estensione                                              {n
                        k = 0,a...,
               X(kF ),aumentando      zero.
                                         (Nla       1)F , possonodaessere                    calcolati               : X(kF
                                                                                                                    usando  in tale   )la=FFT.  T contenuta
                                                                                                                                                caso,       Sii campioni
                                                                                                                                                                   notix(nT  che  )e pos- T,
                                                                                                                                                                                          j2⇡nT (n
                                                                                                                                                                                          aggiuntivi 0kF+=   1)T,              (n     + N)e
                                                                                                                                                                                                                                 xp0(nT
                                             n=0
                                              X(kF       ), k) x(nT
                                                                =   0,usare
                                                                         ...,       n=01)F
                                                                                (Nper                    Nel usando
                                                                                                     , possiamo    calcolo         xTla
                                                                                                                                      p (nT
                                                                                                                                      dei
                                                                                                                                  considerare     ) sono
                                                                                                                                                     =n=n
                                                                                                                                               campioni    per        della
                                                                                                                                                              la0evidentemente
                                                                                                                                                                    versione         ).periodicizzata
                                                                                                                                                                                  trasformata                 tramite            la (1) occ
                                                                                                                                                                                                                         del segnale
                       x(N    T ),  ...,
               siamo infittire i campioniSe
                                         x((M il  segnale
                                                       1)T      da       )   ha     durata  il
                                                         in cui viene calcolata la trasformata       finita
                                                                                                calcolo             D           N       ,  ma
                                                                                                                                            (1)      la    sua     N estensione
                                                                                                                                                                      T                      non       è
                                                                                                                                                                                                  uguali   contenuta     n=0
                                            N/2−1                                                        valoriosservarenel periodo n0 X +N X(f    1 {0,) ..., semplicemente NX1
                                                                                                                                                                    (Ndel 1)T             } deldei     segnale            periodicizzato
                       a zero.laneldimensioneXdi ingresso
                                          periodo       {0,                       1)T>},) N
               aumentando                                   da...,N
                                                           Infatti,(Nase M      x(nT
                                                                                        Nel
                                                                                                occorre
                                                                                               ha
                                                                                               kn   :  estensione
                                                                                                      X(kF
                                                                                                  calcolo  in      tale
                                                                                                                     )
                                                                                                                    dei =          contenuta
                                                                                                                               caso,
                                                                                                                               T
                                                                                                                              campioni
                                                                                                                                              che
                                                                                                                                              i         aiinfini
                                                                                                                                                  campioni
                                                                                                                                                     x(nT
                                                                                                                                                     della
                                                                                                                                                                  {n
                                                                                                                                                                  )e      T,
                                                                                                                                                                       0j2⇡nT  (ncalcolo
                                                                                                                                                                          aggiuntivi
                                                                                                                                                                  trasformata
                                                                                                                                                                                    0kF +=    1)T,T ..., (n
                                                                                                                                                                                               tramite
                                                                                                                                                                                                            campioni
                                                                                                                                                                                                                xlap0(nT + N)e j2⇡
                                                                                                                                                                                                                        (1)
                                                                                                                                                                                                                                      1)Tnk},. s
                                                                                                                                                                                                                                occorreN du
                            Se   il=
                                  X(kF
                                     segnale ),  k  =
                                                   x(nT(x
                                                        0, )
                                                           n   +
                                                            ...,
                                                               ha(N x
                                                                    durata
                                                                       n+N/2 1)F     ,)Wpossiamo
                                                                                    finita       D      ,
                                                                                                              N  xTp (nT
                                                                                                                 considerare
                                                                                                                       ,   ma    )  =
                                                                                                                                    la    per
                                                                                                                                          sua la         x(nT
                                                                                                                                                    versione
                                                                                                                                                  Nestensione
                                                                                                                                                     T               ). periodicizzata
                                                                                                                                                                            non       è   contenuta    del     segnale
               x(N T ), ..., x((M 1)T ) da usare per il calcolo                                N/2
                                                                                                 usando             la+N  (1) 1sono     n=n0evidentemente uguali                                       n=0
               a zero. nel periodo          {0,
                                  di ingresson=0  ..., (N se x(nT
                                              Infatti,            1)T },) ha    occorre valori
                                                                                      estensione
                                                                                                       nel periodo
                                                                                                   osservare       n0 X
                                                                                                                 contenuta  che {0,   aiin...,fini  (N calcolo
                                                                                                                                                  {n0del T,
                                                                                                                                                         j2⇡nT
                                                                                                                                                                 1)T } deldei
                                                                                                                                                               (n0kF+ 1)T,
                                                                                                                                                                                      segnale
                                                                                                                                                                                      NX      1
                                                                                                                                                                                       ...,campioni
                                                                                                                                                                                               (n0 + N
                                                                                                                                                                                                        periodicizzato.
                                                                                                                                                                                                             5 j2⇡       1)Tnk  }, si ha
                                                                                     X(kF          )
                                                                                                xTdei  =      T                      x(nT         )e                        =     T             xla (1) )e
                                                                                                                                                                                                   p  (nT                     N .
                   Se ilX(kF
                         segnale), k x(nT
                                        = 0, ...,
                                               ) ha(Ndurata   1)Ffinita
                                                                     , Nel
                                                                        possiamo  calcolo
                                                                                  D                p (nT
                                                                                        Nconsiderare , ma       ) la
                                                                                                                    = sua
                                                                                                             campioni    per         T x(nT
                                                                                                                            la Nversione
                                                                                                                                    della
                                                                                                                                   estensione        ).periodicizzata
                                                                                                                                                  trasformata
                                                                                                                                                            non       è      tramite
                                                                                                                                                                          contenuta     del segnale            occorre dunque                   c
                                                                                                n0 X +N 1 {0,        n=n0                                             N      1         n=0
                       di ingresso
               nel periodo     {0,    ..., (N        1)T    },   occorrevaloriosservare
                                                                                      nel periodo           che      ai    ...,
                                                                                                                             fini  (Ndel calcolo 1)T } deldei          Xcampioni
                                                                                                                                                                      segnale                 5
                                                                                                                                                                                        periodicizzato.
                                  Infatti,
                                      N/2−1se x(nT ) haX(kF            estensione  )N/2−1
                                                                                      =     T)contenuta             x(nT  in )e  {n0j2⇡nTT, (n0kF+=          1)T, T ..., (n    xp0(nT  + N)e j2⇡        1)TN},. si ha
                                                                                                                                                                                                             nk
                                        X 1)F , possiamo   Nel                  xpdei X
                                                                                     (nT         = per              T x(nT          ).periodicizzata
               X(kF ), k = 0, ..., (N                       n calcolo
                                                                    kn considerare         campioni                della
                                                                                                            la Nversione         trasformata
                                                                                                                                 n         kn                 tramite            la (1) occorre dunque consider
                                                                                                                                                                        del segnale
                                                                       nel −
                                                                                                    n=n
               diX            =                    xn Wvalori
                                                           N WN/2                                   xn+N/2               WN         W}N/2     del, segnale
                                                                                 n0 X+N 1 {0,                 0
                                                                                                                                                      N      1         n=0
                    2k+1
                  ingresso
                       Infatti, se x(nT ) ha              estensione           periodo
                                                                                contenuta               in...,{n  (N             1)T                   X
                                                                                                                                                       ..., (n0 +periodicizzato.
                                                                                                                                                                             5 1)Tnk}, si ha
                                                                                                                     0 T,
                                                                                                                       j2⇡nT  (n   0kF + 1)T,                               N         j2⇡ N
                                        n=0Nel calcolo   X(kF       )
                                                                 xdei  =
                                                                   p (nT
                                                                            T         n=0
                                                                              ) = perNdella       x(nT          )e                          = tramite x
                                                                                                                                                  T              lap (nT
                                                                                                                                                                      (1) )e                      .
                                                                           campioni               T x(nT           ).
                                                                                                                trasformata                                                    occorre dunque                       considerare i
                                      N/2−1                          +N 1 n=n0
                                                                  n0 X                                                               NX     1          n=0
               Infatti, se x(nT ) ha          valori     nel    periodo
                                        Xestensione contenuta in {n0 j2⇡nT        {0,    ...,  (N              1)T
                                                                                                      T, (n0kF+ =      }    del
                                                                                                                           1)T,      segnale            periodicizzato.
                                                                                                                                                             5         1)TN},. si ha
                                                                                                                                                                            nk
                                            X(kF ) = T                            x(nT  n )e kn                                  T ..., (n      xp0(nT+ N)e j2⇡
                              = Nel calcolo       (xndei − campioni
                                                              xn+N/2 )W           dellaN    W trasformata
                                                                                                  N/2        .               tramite             la   (1)      occorre           dunque considerare i
                                                                    n=n0                                                              n=0
                                  valori             n0 X
                                        n=0nel periodo  +N 1 {0, ...,           (Nj2⇡nT      1)T      }     del     N
                                                                                                                    X1
                                                                                                                    segnale             periodicizzato.
                                                                                                 kF
                                                                                                                                            5        j2⇡     nk
                                X(kF dei
                       Nel calcolo         ) = campioni
                                                  T                x(nT )e
                                                                  della       trasformata=tramite               T              xlap (nT
                                                                                                                                     (1) )e    occorreN dunque    .                considerare i
Dunque, i valori X2kvaloridella neltrasformata
                                        periodo {0, ...,vengono
                                                       n=n    0
                                                                 (N 1)T calcolati    } del segnale              conperiodicizzato.
                                                                                                                    n=0    una
                                                                                                                           5
                                                                                                                                         DFT,             su      N/2          valori,
della sequenzaNel
                pncalcolo
                    = xndei
                          + campioni
                              xn+N/2 , della
                                          mentre   i valoritramite
                                              trasformata    X2k+1lasi(1)ottengono   con considerare
                                                                          occorre dunque una DFT,i
ancora su N/2valori
                valori, della  sequenza    q   =  (x  −  x       )W  n . La procedura è mostrata
                    nel periodo {0, ..., (N n 1)T } del
                                                     n segnale
                                                          n+N/2  5 N
                                                               periodicizzato.
per N = 8 in Fig. 4, dove si evidenzia la butterfly utilizzata per il calcolo di pn e qn .
    Procedendo con le suddivisioni come nel caso della    5     decimazione nel tempo, si arriva
al calcolo di N/2 DFT su due campioni, come mostrato in Fig. 5 nel caso N = 8. Si
noti che, se i calcoli vengono implementati seguendo la struttura del grafo di Fig. 5,
nel vettore finale i valori della trasformata appaiono in ordine bit reverse, per cui è

                                                                                               5
     Figure 5: Grafo per il calcolo della FFT (N = 8, decimazione in frequenza).


necessario ordinarli con una procedura analoga a quella utilizzata nella decimazione
nel tempo. Anche in questo caso, la complessità dell’algoritmo risulta O(N log2 N ).

    Segnali a tempo discreto. Se x(nT ), t ∈ Z(T ) è un segnale a tempo discreto, in
generale non periodico, con estensione contenuta in {0, ..., (N − 1)T }, possiamo usare la
FFT per calcolare i campioni della sua trasformata di Fourier. Infatti, dalla definizione
di trasformata, si ottiene
                  +∞
                  X                            N
                                               X −1
      X(f ) = T          x(kT )e−j2πf nT = T          x(nT )e−j2πf nT ,   f ∈ R/Z(1/T ).
                  n=−∞                         n=0

Se calcoliamo la relazione precedente per f = kF , dove F = 1/N T , otteniamo proprio
                                           N
                                           X −1
                                                               nk
                              X(kF ) = T           x(nT )e−j2π N ,
                                           n=0

che ha la stessa struttura della (1). Dunque, N campioni in un periodo di X(f ),
X(kF ), k = 0, ..., (N − 1)F , possono essere calcolati usando la FFT. Si noti che pos-
siamo infittire i campioni in cui viene calcolata la trasformata X(f ) semplicemente
aumentando la dimensione da N a M > N : in tale caso, i campioni aggiuntivi
x(N T ), ..., x((M − 1)T ) da usare per il calcolo usando la (1) sono evidentemente uguali
a zero.
    Se il segnale x(nT ) ha durata finita D ≤ N T , ma la sua estensione non è contenuta
nel periodo {0, ..., (N − 1)T }, occorre osservare che ai fini del calcolo dei campioni
X(kF ), k = 0, ..., (N − 1)F , possiamo considerare la versione periodicizzata del segnale
di ingresso
                                  xp (nT ) = perN T x(nT ).


                                               6
Infatti, se x(nT ) ha estensione contenuta in {n0 T, (n0 + 1)T, ..., (n0 + N − 1)T }, si ha
                                  +N −1
                               n0 X                                N
                                                                   X −1
                                                                                         nk
                X(kF ) = T                x(nT )e−j2πnT kF = T            xp (nT )e−j2π N .
                                 n=n0                               n=0

Nel calcolo dei campioni della trasformata tramite la (1) occorre dunque considerare i
valori nel periodo {0, ..., (N − 1)T } del segnale periodicizzato.
    Infine, se il segnale x(nT ) ha durata praticamente limitata, è possibile considerarlo
nullo entro una precisione prefissata al di fuori di un certo intervallo I0 . Questo equivale
in effetti a moltiplicare il segnale di ingresso per una finestra che vale 1 per t ∈ I0 e
0 altrove. I valori calcolati dei campioni della trasformata saranno pertanto relativi
alla convoluzione tra la trasformata di Fourier del segnale di ingresso con quella della
finestra.

     Stima della trasformata per segnali a tempo continuo. Supponiamo di
avere un segnale a tempo continuo x(t), t ∈ R e di volere calcolare una stima della sua
trasformata di Fuorier X(f ), f ∈ R. Per potere utilizzare a tale scopo un algoritmo
numerico, e in particolare la FFT, occorre dapprima campionare il segnale di ingresso,
ponendo xc (t) = x(t), t ∈ Z(T ). La scelta di T deve essere fatta in modo da limitare
l’aliasing, e in generale deve essere Fc = 1/T > B, dove B è la larghezza di banda
del segnale2 . Una volta campionato, il segnale ha una trasformata di Fourier periodica
Xc (f ) = repFc X(f ), f ∈ R/Z(Fc ) i cui campioni in un periodo possono essere stimati
mediante un algoritmo di FFT, secondo quanto esposto relativamente ai segnali a tempo
discreto. Se non si conosce a priori la larghezza di banda B del segnale, occorrerà
procedere per tentativi, valutando se le stime che si ottengono variano entro la precisione
desiderata al variare di T .
     Se il segnale x(t) è reale, la sua trasformata di Fourier ha simmetria hermitiana ed
estensione spettrale simmetrica [−B/2, B/2]. L’algoritmo di FFT fornisce i campioni
della trasformata periodica Xc (f ) = repFc X(f ) relativamente al periodo [0, Fc ], mentre
il confronto con X(f ) è più significativo se si considera il periodo [−Fc /2, Fc /2]. Posto
F = Fc /N , una volta calcolati i valori Xc (0), ..., Xc ((N − 1)F ) con un algoritmo di
FFT, converrà dunque riferirsi al vettore
                                                                             
          N              N                                                     N
    Xc       F , Xc          + 1 F , ..., Xc ((N − 1) F ) , Xc (0), ..., Xc      −1 F       ,
           2              2                                                    2
per N pari, e a
                                                                          
     N +1             N +1                                                   N −1
 Xc         F , Xc         + 1 F , ..., Xc ((N − 1) F ) , Xc (0), ..., Xc          F   ,
        2               2                                                      2
per N dispari, che contengono la sequenza dei campioni relativi al periodo [−Fc /2, Fc /2].
Tale operazione di ordinamento degli elementi del vettore di uscita può ottenersi con
la funzione MATLAB fftshift.

                                                 Esempi
    2
      Si definisce in queste note la larghezza di banda come la lunghezza dell’intervallo che definisce
l’estensione spettrale del segnale, ovvero l’insieme E tale che X(f ) = 0 per f 6∈ E. Se il segnale è reale,
l’estensione spettrale è un intervallo simmetrico [−B/2, B/2], dove B/2 è la banda del segnale.


                                                     7
Dalle relazioni precedenti, dovrebbe essere chiaro che, se vogliamo calcolare N campioni
in un periodo della trasformata di Fourier X(f ), f ∈ R/Z(1/T ), di un segnale a tempo
discreto x(nT ), kT ∈ Z(T ), qualunque sia la sua estensione, possiamo pensare di
periodicizzarlo con periodo N T , ottenendo
                                              +∞
                                              X
                              xp (nT ) =               x(nT − kN T ).
                                             k=−∞

Tale segnale, definito su Z(T )/Z(N T ), ha trasformata di Fourier Xp (f ), f ∈ Z(F )/Z(N F ),
F = 1/(N T ), i cui valori coincidono con i campioni della trasformata di Fourier X(f )
che vogliamo calcolare (si ricorda infatti che il duale della periodicizzazione è il campio-
namento). I valori Xp (nF ) = X(nF ), k = 0, ..., N − 1, possono essere dunque calcolati
mediante la DFT
                                      N
                                      X −1
                                                             nk          1
                       Xp (kF ) = T          xp (nT )e−j2π N ,    F =
                                                                        NT
                                      n=0

a partire dai valori di xp (t) nel periodo t ∈ {0, T, ..., (N − 1)T }.

   1. Si vogliano calcolare N campioni della trasformata di Fourier del segnale a tempo
      discreto x(nT ), T = 0.1, con valori x(0) = x(2T ) = 1, x(T ) = 2, x(nT ) = 0
      altrove. La trasformata di Fourier risulta, come è immediato verificare,

                     X(f ) = T e−j2πf T (2 + 2 cos(2πf T )),        f ∈ R/Z(1/T ).

      Per calcolare, ad esempio, N = 128 campioni della trasformata nel periodo f ∈
      [0, 1/T ) è sufficiente calcolare la DFT del segnale periodicizzato con periodo N T .
      Si noti che, essendo l’estensione del segnale contenuta in {0, ..., (N − 1)T }, la
      periodicizzazione non richiede alcun calcolo specifico. Possiamo dunque scrivere
      il seguente codice MATLAB per il calcolo (vedi Fig. 6)

      T=0.1;
      N=128;
      x=[1 2 1];
      X=T*fft(x,N); % La FFT viene calcolata su N punti,
                            % aggiungendo 0 in coda al vettore

      f=(0:N-1)/(N*T);
      figure(1); stem(f,abs(X),’r’); % plot(f,abs(X)) per rappresentazione
                                                  % a frequenze continue
      figure(2); stem(f,angle(X),’r’); % plot(f,angle(X)) per rappresentazione
                                                  % a frequenze continue


      % confronto con la trasformata teorica, che calcoliamo su M=512 punti

      M=512;
      f=(0:M-1)/(M*T);

                                                   8
                                                                                        4
              0.4


                                                                                        3
             0.35



              0.3                                                                       2



             0.25                                                                       1




                                                                         angle(X(f))
 abs(X(f))




              0.2                                                                       0



             0.15                                                                      !1



              0.1                                                                      !2



             0.05                                                                      !3



               0                                                                       !4
                    0     1   2   3   4       5     6   7   8   9   10                      0   1    2   3   4       5     6   7   8   9   10
                                           f (Hz)                                                                 f (Hz)


                                          (a)                                                                    (b)


Figure 6: Andamento della trasformata di Fourier e i valori calcolati mediante FFT
per i segnali dell’esempio 1.


                        figure(1);
                        hold on;
                        plot(f, abs(T*exp(-j*2*pi*f*T).*(2+2*cos(2*pi*f*T))));
                        hold off;

                        figure(2);
                        hold on;
                        plot(f, angle(T*exp(-j*2*pi*f*T).*(2+2*cos(2*pi*f*T))));
                        hold off;


             2. Si vogliano calcolare N = 128 campioni della trasformata di Fourier del segnale
                a tempo discreto x(nT ), T = 0.1, con valori x(−T ) = x(T ) = 1, x(0) = 2,
                x(nT ) = 0 altrove. La trasformata di Fourier risulta, come è immediato verificare,

                                             X(f ) = T (2 + 2 cos(2πf T )),                         f ∈ R/Z(1/T ).

                        Il procedimento è analogo a quello visto al punto precedente, con l’avvertenza che
                        i valori del segnale periodicizzato, nel periodo {0, ..., (N − 1)T } sono anticipati di
                        un campione. Dobbiamo pertanto fare attenzione nel caricamento del vettore che
                        dovrà contenere i valori del segnale nel periodo t ∈ {0, T, ..., (N − 1)T }. Possiamo
                        dunque scrivere il seguente programma MATLAB (vedi Fig. 7)

                        T=0.1;
                        N=128;
                        x=[2 1 zeros(1,N-3) 1];
                        X=T*fft(x); % La FFT viene calcolata
                                           % su un numero di punti pari
                                           % alla lunghezza del vettore


                                                                     9
              0.4                                                                      1


                                                                                      0.8
             0.35

                                                                                      0.6
              0.3
                                                                                      0.4

             0.25
                                                                                      0.2
 abs(X(f))




                                                                         abs(X(f))
              0.2                                                                      0


                                                                                     !0.2
             0.15

                                                                                     !0.4
              0.1
                                                                                     !0.6

             0.05
                                                                                     !0.8


               0                                                                      !1
                    0     1   2   3   4       5     6   7   8   9   10                      0   1   2   3   4       5     6   7   8   9   10
                                           f (Hz)                                                                f (Hz)


                                          (a)                                                                   (b)


Figure 7: Andamento della trasformata di Fourier e i valori calcolati mediante FFT
per i segnali dell’esempio 2.



                        f=(0:N-1)/(N*T);
                        figure(1); stem(f,abs(X),’r’); % plot(f,abs(X)) per rappresentazione
                                                                    % a frequenze continue
                        figure(2); stem(f,angle(X),’r’); % plot(f,angle(X)) per rappresentazione
                                                                    % a frequenze continue

                        % confronto con la trasformata teorica, calcolata su M=512 punti

                        M=512;
                        f=(0:M-1)/(M*T);
                        figure(1);
                        hold on;
                        plot(f, abs(T*(2+2*cos(2*pi*f*T))));
                        hold off;

                        figure(2);
                        hold on;
                        plot(f, angle(T*(2+2*cos(2*pi*f*T))));
                        hold off;


             3. Supponiamo di raccogliere N valori consecutivi ottenuti per campionamento, con
                periodo T = 1/Fs , di una sinusoide a tempo continuo di frequenza f0 . Cosa
                rappresenta la FFT (calcolata eventualmente su un numero M ≥ N di valori)
                del vettore di valori cosı̀ ottenuti? Per fissare le idee, supponiamo T = 0.1 e,
                senza perdita di generalità, f0 < Fs /2. Si ricorda infatti che, a seguito del cam-
                pionamento e al fenomeno dell’aliasing, una sinusoide campionata di frequenza
                maggiore di Fs /2, assume gli stessi valori di una corrispondente sinusoide cam-


                                                                    10
             1.6                                                                      1.6



             1.4                                                                      1.4



             1.2                                                                      1.2



              1                                                                        1
 abs(X(f))




                                                                          abs(X(f))
             0.8                                                                      0.8



             0.6                                                                      0.6



             0.4                                                                      0.4



             0.2                                                                      0.2



              0                                                                        0
                   0     1   2   3   4       5     6   7    8   9   10                      0   1   2   3   4       5     6   7   8   9   10
                                          f (Hz)                                                                 f (Hz)


                                         (a)                                                                    (b)


Figure 8: Andamento della trasformata di Fourier e i valori calcolati mediante FFT
per un segnale sinusoidale (a) con frequenza f0 = 0.25, T = 0.1, N = 32, M = 256, (b)
con frequenza f0 = 7/(N T ) , T = 0.1, N = M = 32, dell’esempio 3.


                       pionata di frequenza minore di Fs /2.
                       Sulla base delle considerazioni precedenti, mediante la FFT, viene calcolata la
                       trasformata di Fourier della periodicizzazione, con periodo M T , del segnale x(nT ),
                       nT ∈ Z(T ),                 
                                                      cos(2πf0 nT ), n = 0, ..., N − 1,
                                         x(nT ) =
                                                      0,              altrimenti.
                       Tale segnale corrisponde, nel dominio del tempo, al prodotto della sinusoide
                       s(nT ) = cos(2πf0 nT ) con il segnale finestra p(nT ) che vale 1 per nT = 0, ..., (N −
                       1)T e 0 altrove. La sua trasformata di Fourier X(f ) risulta quindi pari alla con-
                       voluzione fra la trasformata della sinusoide
                                                 1                      1
                                          S(f ) = δR/Z(1/T ) (f − f0 ) + δR/Z(1/T ) (f + f0 )
                                                 2                      2
                       e la trasformata

                                                   P (f ) = N T e−j2π(N −1)f T /2 sincN (f N T ),

                       risultando

                                     X(f ) = 0.5N T e−j2π(N −1)(f −f0 )T /2 sincN ((f − f0 )N T )+

                                               0.5N T e−j2π(N −1)(f +f0 )T /2 sincN ((f + f0 )N T )
                       Mediante la FFT su M ≥ N valori, si calcolano dunque i campioni X(kF ),
                       F = 1/(M T ), k = 0, ..., M − 1. Verifichiamo con MATLAB (vedi Fig. 8.a)

                       T=0.1;
                       f0=2.5;
                       N=32;

                                                                     11
k=0:N-1;
x=cos(2*pi*f0*k*T);

M=256;
X=T*fft(x,M);      % La FFT viene calcolata su M punti

f=(0:M-1)/(M*T);
figure(1); plot(f,abs(X));

% confronto con la trasformata teorica, calcolata su M1=1024 punti

figure(1);
M1=1024;
f=(0:M1-1)/(M1*T);
hold on;
plot(f, abs( ...
0.5*N*T*exp(-j*2*pi* (N-1)* (f-f0)* T/2).* sinc_n(N,(f-f0)*N*T) + ...
0.5*N*T*exp(-j*2*pi* (N-1)* (f+f0)* T/2).*sinc_n(N,(f+f0)*N*T) ...
),’*r’);
hold off;


Si noti che l’effetto della convoluzione con la trasformata di Fourier della finestra si
verifica ogni qualvolta si prelevi un blocco di segnale costituito da un insieme finito
di valori consecutivi ai fini del calcolo della sua trasformata. Come visto, l’uso
di una finestra rettagolare, come il segnale p(nT ) considerato precedentemente,
corrisponde alla convoluzione con una trasformata con andamento tipo sincN , che
presenta lobi laterali di ampiezza non trascurabile rispetto al lobo principale. Per
mitigare l’effetto dei lobi nella convoluzione, in molte applicazioni si utilizzano
finestre con forma diversa dalla rettangolare, come ad esempio le finestre di Ham-
ming, di Hanning o di Blackman (vedi la documentazione in MATLAB relativa
ai comandi hamming, hann, blackman).
Per quanto riguarda il caso della sinusoide, si noti che, se si pone M = N e se f0
è multiplo di 1/(N T ), allora il periodo N T contiene un numero intero di periodi
della sinusoide. Il segnale periodicizzato, di cui si calcola la DFT, risulta pertanto
una sinusoide definita su Z(T )/Z(N T ), la cui trasformata di Fourier è una coppia
di impulsi discreti periodici, con area 0.5, posizionati alle frequenze f0 e Fs − f0 .
Questa situazione corrisponde, nell’espressione procedente, a campionare i segnali
sincN in corrispondenza dei punti in cui si annullano, eccetto che per le frequenze
f = f0 , f = Fs − f0 . Verifichiamo con MATLAB (vedi Fig. 8.b)

T=0.1;

N=32;
f0=7/(N*T);


                                       12
                                    2


                                   1.8


                                   1.6


                                   1.4


                                   1.2




                      real(X(f))
                                    1


                                   0.8


                                   0.6


                                   0.4


                                   0.2


                                    0
                                    !8   !6    !4   !2         0     2    4   6    8
                                                            f (Hz)




Figure 9: Andamento della trasformata di Fourier e della sua stima mediante FFT, del
segnale a tempo continuo x(t) = e−|t| dell’esempio 4.


     k=0:N-1;
     x=cos(2*pi*f0*k*T);

     X=T*fft(x);

     f=(0:N-1)/(N*T);
     figure(1); stem(f,abs(X),’r’);

     % confronto con la trasformata teorica, calcolata su M1=1024 punti

     figure(1);
     M1=1024;
     f=(0:M1-1)/(M1*T);
     hold on;
     plot(f, abs( ...
     0.5*N*T*exp(-j*2*pi* (N-1)* (f-f0)* T/2).* sinc_n(N,(f-f0)*N*T) + ...
     0.5*N*T*exp(-j*2*pi* (N-1)* (f+f0)* T/2).*sinc_n(N,(f+f0)*N*T) ...
     ));
     hold off;


  4. Si voglia stimare, usando la FFT, la trasformata di Fourier del segnale a tempo
     continuo x(t) = e−|t| , t ∈ R. La trasformata di Fourier, come in questo caso è
     facile calcolare, risulta
                                                             2
                                              X(f ) =                 ,   f ∈ R.
                                                         1 + 4π 2 f 2
     Consideriamo per X(f ) una banda convenzionale secondo le ampiezze a 60 dB,
     determinando la frequenza B alla quale |X(f )| si riduce definitivamente di un
     fattore 0.001 (60 dB di attenuazione in ampiezza) rispetto al valore massimo di

                                                          13
      |X(f )|, che si ottiene per f = 0 e risulta pari a 2. Si ottiene3 B ' 7 Hz. La
      frequenza di campionamento risulta dunque Fc = 2B = 14 campioni/s. Per
      il segnale, possiamo definire una estensione convenzionale [−t0 , t0 ] (il segnale è
      pari), al di fuori della quale il segnale sia attenuato di almeno 60 dB rispetto al
      valore massimo. Risulta anche in questo caso t0 ' 7. Possiamo dunque riferirci al
      seguente codice MATLAB per il calcolo e i confronti con l’espressione teorica della
      trasformata (vedi Fig. 9: come si vede, i grafici sono praticamente sovrapposti).

      % Banda convenzionale B=7
      % Estensione convenzionale E=[-t0,t0]=[-7 7]; durata D=14.

      B=7;
      Fc=2*B;
      T=1/Fc;

      t0=7;
      t=-t0:T:t0;
      x=exp(-abs(t)); % risultano 197 valori del segnale,
                                 % pari a circa 2*B*D

      % Calcola la DFT del segnale periodicizzato su M=512 campioni
      M=512;

      x1=[x(99:end), zeros(1,M-length(x)), x(1:98)];
      X=T*fft(x1);

      % Confronto con la trasformata teorica, calcolata negli stessi punti
      % M pari

      f=(-M/2:M/2-1)/(M*T);

      plot(f,fftshift(real(X)),’-’, f, 2./(1+4*pi^2*f.^2),’:’)


                                            Esercizi
1. Si consideri il segnale x(t), t ∈ Z(T ), T = 2, con x(0) = 1, x(±T ) = 2, x(±2T ) = 3
   e x(nT ) = 0 altrove. Si calcoli in forma chiusa la trasformata di Fourier X(f ), f ∈
   R/Z(1/T ). Si calcolino inoltre N campioni della trasformata in un periodo usando
   un algoritmo di FFT, per N = 8, 16, 256, e si verifichi in un grafico la coincidenza
   fra i campioni calcolati e l’espressione teorica.
      Si valuti inoltre approssimativamente il numero di operazioni richieste per il cal-
      colo degli N campioni della trasformata usando la FFT ed il calcolo diretto. Si
      tenga presente che il segnale di ingresso ha solamente 5 campioni diversi da zero.
      Nota: X(f ) è in generale una funzione complessa, ed occorre considerarne di
      volta in volta la parte reale e immaginaria, oppure il modulo e la fase.
3
    In questo esempio, indichiamo con B la banda, con 2B la larghezza di banda.


                                               14
2. Si calcoli la DFT dei seguenti segnali, definiti su Z(T ), e si disegni il grafico del
   modulo, cercando di spiegarne le caratteristiche. Sia F = 1/T = 8 kHz.

     a. Trasformata su N = 512 punti. Segnale di ingresso

                                   x(nT ) = 1, 0 ≤ n ≤ 63
                                   0,          altrove.

     b. Trasformata su N = 256 punti. Segnale di ingresso
                                                        
                                  2πn               2πn
               x(nT ) = 0.5 sin       9 + 0.7 sin       100 , 0 ≤ n ≤ 255.
                                  256               256

     c. Trasformata su N = 256 punti. Segnale di ingresso
                                                           
                                2πn 100               2πn 200
             x(nT ) = 0.5 sin             + 0.7 sin             , 0 ≤ n ≤ 255.
                                256 3                 256 3

3. Una sinusoide di frequenza 50 Hz viene campionata con 500 campioni al secondo
   e analizzata usando una FFT su 64 campioni.

     a. Quale campione della trasformata sarà maggiore in modulo?
     b. Quale campione della trasformata avrà un’ampiezza immediatamente infe-
        riore a quella del campione di modulo maggiore, e qual’è l’ampiezza relativa
        dei due campioni (esprimere il risulatato in dB)?

   Si verifichino i risultati con MATLAB.

4. Siano dati i seguenti segnali, definiti su Z(T ) per T = 1.
                             
     a. x(nT ) = sin 2πn
                      256 172 ,
     b. x(nT ) = sin(n).

   Si analizzino i due segnali mediante FFT su 256 punti. Si preveda quale sarà
   il coefficiente della trasformata più grande in modulo nei due casi, e l’ampiezza
   relativa di tali campioni della trasformata. Si verifichi il risultato con MATLAB.

5. Questo esercizio mostra come occorra fare attenzione nell’uso della FFT per il
   calcolo della trasformata di Fourier di segnali sinusoidali. Si consideri il segnale
   x(t) = cos 2πf0 t, t ∈ Z(T ), T = 1 f0 = 0.25 e si costruisca il vettore MATLAB

                           x(n + 1) = x(nT ),   n = 0, ..., N − 1

   per N = 32 e N = 64. Si calcoli poi la FFT di x nei due casi su N punti e la
   si disegni usando la funzione stem. Si discuta il risultato ottenuto. Si ripeta lo
   stesso esperimento per f0 = 0.254 e si discuta il risultato ottenuto. Si risolva
   inoltre l’esercizio per via analitica e si confronti con la soluzione trovata per via
   numerica.
   Nota: per f0 = 0.25 e i due valori di N considerati, x(t) è periodico di periodo
   N T . Per f0 = 0.254, x(t) non è periodico di periodo N T .

                                         15
6. Si scriva una procedura analoga alla procedura MATLAB freqz, usando la FFT.

7. Dati i segnali x(nT ) con estensione 0, ..., (N −1)T e h(nT ) con estensione 0, ..., (M −
   1)T , si scriva una procedura MATLAB che calcola la convoluzione y(nT ) =
   h ∗ x(nT ) mediante l’uso della FFT. Si confronti il risultato con quello for-
   nito dalla funzione MATLAB y=T*conv(h,x), in cui si pone x(n + 1) = x(nT ),
   nT = 0, ..., (N − 1)T , e h(n + 1) = h(nT ), nT = 0, ..., (M − 1)T . Si scriva
   un programma che calcola la convoluzione di due segnali generici con estensioni
   −5T, ..., 4T e 3T, ..., 5T .
   Soluzione proposta per la prima parte:

   function y=convv(T,x,h);

   N=length(x); M=length(h);

   L=N+M-1;

   X=T*fft(x,L); H=T*fft(h,L);

   Y=X.*H;

   y=ifft(Y)/T;

   % Se x e h sono reali, y e‘ reale. Si pu\‘o eliminare
   % l’eventuale parte immaginaria, non identicamente nulla a causa
   % degli errori di calcolo.

   if (isreal(x) & isreal(h)) y=real(y);

   end;

8. Metodo Overlap-Add. Con riferimento all’esercizio precedente, se il segnale x(t), t ∈
   Z(T ) ha una durata N T molto più grande di quella M T di h(t), non è efficiente
   calcolare direttamente la convoluzione usando la FFT, che deve essere valutata
   per entrambi i segnali su almeno M + N − 1 punti. È conveniente allora suddi-
   videre il segnale di ingresso in blocchi non sovrapposti lunghi L,
                                 
                                    x(nT ), n = iL, ..., iL + L − 1,
                      xi (nT ) =
                                    0,       altrove

   ponendo                                     X
                                    x(nT ) =       xi (nT ).
                                               i

   Il risultato della convoluzione viene ottenuto sommando le uscite xi ∗ h(nT ),
   ciascuna delle quali può essere calcolata usando la FFT. Si noti che le uscite
   xi ∗ h(nT ) risultano sovrapposte di M − 1 campioni.



                                          16
    Si scriva un programma MATLAB che calcola la convoluzione di due segnali con
    il metodo Overlap-Add, ponendo M = 4 e N = 64, e si confronti il risultato con
    il metodo diretto e quello dell’esercizio 7.
 9. Dati due segnali x1 (t) e x2 (t), t ∈ Z(T ) a durata limitata LT , è possibile
    considerarne le ripetizioni periodiche x1,p (t) = repLT x1 (t), t ∈ Z(T )/Z(LT ) e
    x2,p (t) = repLT x2 (t), t ∈ Z(T )/Z(LT ), senza perdita di informazione. Dimostrare
    e verificare su un esempio sviluppato con MATLAB che la convoluzione ciclica
    yp (nT ) = x1,p ∗ x2,p (nT ) è uguale alla ripetizione periodica della convoluzione
    y(nT ) = x1 ∗ x2 (nT ), ovvero yp (nT ) = repLT y(nT ).
10. Metodo Overlap-Save. Si considerino, come nell’Esercizio 8, due segnali x(t), t ∈
    Z(T ) e h(t) con estensione [0, ..., (N − 1)T ] e [0, ..., (M − 1)T ], rispettivamente,
    e N  M . Nel metodo Overlap-Save per il calcolo della convoluzione, il segnale
    x(nT ) viene suddiviso in blocchi xk (nT ) lunghi L campioni. Il metodo consiste
    nel calcolare una convoluzione ciclica (vedi Esercizio 9) tra h(nT ) e xk (nT ), iden-
    tificando quella parte della convoluzione ciclica che corrisponde alla normale con-
    voluzione. In particolare, supponendo L ≥ M , nella convoluzione ciclica di h(nT )
    e xk (nT ) calcolata su L punti, risulta che i primi M − 1 non sono corretti, men-
    tre i rimanenti punti sono gli stessi che otterremmo dalla normale convoluzione
    (perchè? Vedi l’Esercizio 9). Conviene dunque sezionare x(nT ) in segmenti di
    lunghezza L in modo che ogni segmento si sovrapponga al precedente per M − 1
    punti.
    Dopo avere definito i segmenti xk (nT ) nel modo seguente
                   xk (nT ) = x((n + k(L − M + 1))T ), 0 ≤ n ≤ L − 1,
    si calcola pertanto la convoluzione ciclica yk (nT ) = h ∗ xk (nT ) su L punti e se ne
    scartano i primi M − 1. I rimanenti punti di ogni sottosequenza yk (nT ) vengono
    giustapposti gli uni di seguito agli altri, fino ad ottenere l’uscita filtrata finale.
    Si scriva un programma MATLAB che calcola la convoluzione di due segnali con
    il metodo Overlap-Save, ponendo M = 4 e N = 64, e si confronti il risultato con
    il metodo diretto e quello dell’Esercizio 7.
11. Si stimi la trasformata di Fourier del segnale a tempo continuo
                                    x(t) = e−|6t| ,     t ∈ R.

12. Si stimi la trasformata di Fourier del segnale a tempo continuo
                                  x(t) = e−|6(t−1)| ,    t ∈ R.

13. Si stimi la trasformata di Fourier del segnale a tempo continuo
                              x(t) = e−|6t| cos(2π0.5t),     t ∈ R.

14. Si stimi la trasformata di Fourier del segnale a tempo continuo
             sin(π(1 − r)t/T ) + 4r(t/T ) cos(π(1 + r)t/T )      t
    x(t) =                              2
                                                            rect ,     r = 0.125,    t ∈ R.
                          π[1 − (4rt/T ) ]t/T                   8T



                                           17
