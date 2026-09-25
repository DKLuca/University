---
fonte: "gigio.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Formulario TSCE                                      Filtro Interpolatore                                     SSB                                               Tips and tricks                                           QAM→ 10bit
    parzival3, page 1 of 2                                                                                        Efficienza unitaria Λ = Λc                        Probabilità                                               Necessari 32000campioni/s e banda
                                                       a(kT )                                  y(t)
                                                                        x
                                                                                                                 Banda richiesta B                                 Esercizio                                                 1/T = 2fn = 32[KHz]
                                                                                                                  Segnale ricevuto s̃(t) = 1/4AT AM AR s(t)
                                                                        
Probabilità
                                                                        g
                                                                                                                                                                    P [y ≥ 0] con y = x1 · x2                                 Quantizzazione
                                                                                                                  Potenza del segnale ricevuto                      P [x1 ≥ 0]P [x2 ≥ 0] + P [x1 ≤ 0]P [x2 ≤ 0]               Calare esattamente triangle
Aspettazione                                                       P∞
                                                        x(t) = T    k=−∞ a(KT )g(t − KT )                         Ms̃ = 1/16A2T A2M A2R Ms
                                                                                                                                                                                                                                       RV                   RV
       R∞                                                                                                                                                           Esercizio                                                 Mx = 2 0 a2 fx (a)da = 2 0 a2 ( V1 − 12 a)da
E[x] = −∞ a f (a) da                                                                                                                                                P [3x(KT ) − x(KT − T ) ≥ 2]                                                                        V
                                                                          ∞                                       Potenza del rumore Mñ = 2B1/4R0 A2R =                                                                                RV
                                                                                                                                                                    y(KT ) = 3x(KT ) − x(KT − T )                             Me2 = 2 0 (a − V2 )2 ( V1 − a2 )da
       P
E[x] = ak ∈A ak pk (ak )
                                                                          X
                                                               mx (t) = T            E[a(kT )]g(t − KT )          1/2BR0 A2R                                        ottenuto da un filtro                                                                    V
Proprietà                                                                   k=−∞
                                                                                                                                                                                                                              SN R = 2R = 3dB
                                                                                                                  Potenza trasmessa MT = 1/4A2T Ms                  h(KT ) = 3δZ (KT ) − δZ (KT − T )                                    V /2
                                                                                                                                                                                                                              Me4 = 2 0 (a − V4 )2 ( V1 − a2 )da+
E[c] = c                                                                        ∞                                                                                   my = mx · H(0) = 0 Ry = Rx · |H(f )|2                                                      V
                                                                               X                                  Rapporto segnale rumore convenzionale
E[aX + b] = aE[x] + b                                                 = ma T            g(t − KT )
                                                                                                                                                                                                                               RV
                                                                                                                  Λc = MR /2BR0 = A2M MT /2BR0 = Λ                  σy2 = E[y 2 (KT )] = E[(3x(KT ) − x(KT −                  2 V /2 (a − 34 V )2 ( V1 − 12 )da
E[x + y] = E[x] + E[y]                                                           k=−∞                                                                                                                                                                   V
                                                                                                                  Rapporto segnale rumore                           T ))2 ] ⇒                                                 SN R = 8 = 9dB
                                                                                                                                                                                                                              Trapezio isoscele
                                                                                 |      {z            }
Variabili Indipendenti                                                                                                                                              σy2 = E[9x2 (KT ) − 6x(KT )x(KT − T ) + x2 (KT − T )] =
P [x1 ∈ B1 , x2 ∈ B2 ] = P [x1 ∈ B1 ] · P [x2 ∈ B2 ]
                                                                                 periodicizzazione                       1/16A2T A2M A2R Ms        1/4A2T A2M MS                                                              bm = V BM = 3V 3 livelli passo ∆ = V
                                                                                                                    Λ=                        =                     = 9rx (0) − 6rx (1 · T ) + rx (0) = 10rx (0) − 6rx (T )           R V /2
                                                                                                                                                                                                                                                1 (a − 0)2 + 2 3V /2 (− 1 a +
                                                                                                                                                                                                                                                                 R
Condizione sufficiente e necessaria                     Analisi spettrale Filtri                                             1/2BR0 A2R                  2BR0       Esercizio 2                                               Me = −V /2 2V                               2
fx (a1 , a2 ) = fx1 (a1 ) · fx2 (a2 )                                                                                                                                                                                                                              V /2
                                                                                                                                                                                                                                                                   2V
                                                                                                                                                                    a(KT ) indipendenti media nulla, varianza                  3 )(a − V 2 ) = V 2
Fx (a1 , a2 ) = Fx1 · Fx2                              x(t)                                    y(t)               Quantizzazione                                    σa2 .                                                     4V                12
                                                                      h(t)                                        Passo di quantizzazione ∆ = 2V /L                                                                                         R V /2
                                                                                                                                                                                                                                                    1 2
                                                                                                                                                                                                                                                           R 3V /2
                                                                                                                                                                                                                                                                     1·a
                                                                                                                                                                    Calcolare P [a(KT ) + a(KT − T ) ≥ 1]                     Mx = 2 0
Teorema fondamentale del aspettazione                                                                             Errore di quantizzazione ∆2 /12                                                                                                  2V a + 2 V /2 (− 2V 2   +
                                                                                                                                                                    Media E[a(KT )]E[a(KT − T ] = 0 Varianza
Se una v.a. y è funzione                                                                                                                                                                                                       3 )a2 5V 2
                      R +∞ di una v.a. x con            my = mx · |H(0)|                                          Rapporto segnale rumore 6 m[dB]
                                                                                                                                                                    E[a2 + 2a(KT                      2                  2
y = g(x) allora E[y] = −∞ g(a) fx (a) da                Ry (f ) = Rx (f ) · |H(f )|2 = Rx (f ) H(f ) · H ∗ (f )   Calcolo esatto della potenza del rumore                     p )a(KT + T ) + a (KT + T )] = 2σa              4V
                                                                                                                                                                                                                              PAM
                                                                                                                                                                                                                                      12
                                                                                                                                                                    P = Q(1/ (2)σa )                                          Reggiseno
Formule Probabilità                                     Desità media                                                        L−1
                                                                                                                            X Z ak +1                               Probabilità bit errato
          P [A B]                                                                                                                                                                                                                                                 2
                                                        R̃(f ) = Ra (f ) 12 |G(f )|2                                                                                                                                          H(f ) a coseno Rialzato |H(f )| = AT
                                                                                                                                                                                                                                                     R
P [A|B] = P [B]                                                          T                                           Me =               (ak + ∆/2 − a)2 fx (a) da   5bit consecutivi p probabilità di ricevere
K successi in N prove è uguale a                                R (f ) R             R (f )                                 K=0 ak                                  un bit errato, errori indipendenti Calcolare
                                                        M̃v = a 2        |G(f )|2 = a 2 Eg ←Parseval                                                                probabilità almeno 3 bit corretti
 N k        N −K →    n!                                        T                    T
 K p (1 − p)                                            Se i processi sono incorrelati                            PAM
                    (n−k)!k!                                                                                                                                        P = 53 (1 − p)3 p2 + 54 (1 − p)4 p + 55 (1 − p)5
                                                                                                                                                                                                             
                                                                                                                  Impulso equivalente C(f ) = G(f )L(f )H(f )
Se K è il numero di prove da fare prima che                                                                                               0                         Calcolo potenza sinusoide
si verifichi A, P [x = K] = p(1 − p)k                              Rx (f ) = σx2 T + m2x δ       R (f )           Elemento di decisione V0 = c(0) Variana del                                          1
                                                                                                                  rumore                                            x(t) = 2 cos(5t + φ),fx (φ) = 2π
                                                                                               Z( T1 )                       Z                 Z                          R 7π/4
Processo aleatorio gaussiano                                                                                         σn2 = R0 |H(f )|2 df = R0 |h(t)|2 dt           mx = −π/4 2 cos(5t + a) da = 0
                        1       1 a−m 2                 Rumore Termico                                                                                              σx2 = 4E[ 12 + 21 cos(10t + 2φ)] = 2
           fx (a) = √        e− 2 ( σ )                 Sono processi indipendenti                                Banda minima richiesta 1/2T pari alla             DSB
                        2πσ                                                                                       frequenza di Nyquist                              Esempio
                                                        vu (t) = y1 (t) + y2 (t)
idipendenti ⇐⇒ incorrelate                                                                                        Matched filter h(t) = k g̃(−t) con                AT = 2db/km , MT = 200V 2 , R0 = 10−18 ,
                                                        Rvu (f ) = |H1 (f )|2 Rv1 + |H2 (f )|2 Rv2 (f )           H(f ) = G(f )L(f )
E[x1 , x2 ] = E[x1 ] E[x2 ]                                                                                                                                         Λ = 50[dB]
mx = E[x] = m                                           dove Rv = 2KT R                                           Probabilità di errore per simboli equiproba-
                                                        Rapporto segnale rumore non dipende dal                                                                     Massima distanza in chilometri?
σx2 = E[(x − mx )2 ] = σ 2                                                                                        bili                                              −10 log1 0A2M = AT · L con L in Km
                                                        guadagno del amplificatore                                                        0 !
                                                                                                                                        V0
Variabile geometrica                                                                                              Mpari Pe = 2M−2
                                                                                                                                M     Q σ                           Attenuazione in potenza A2M = 10−2L/10
                                                                                                                                          n
p (K) = P [x = K] = p(1 − p)k                                  E[su2 (t)          r0 H02              r0                                                            Λ = MT A2M /2R0 B e L = 55[Km ]
Px∞                   1                                                     =                  =                                              0 !
                                                                                                                                             V0
  k=0 px (k) = p 1−(1−p) = 1                                   E[n2u (t)]       2KT RH02 B          2KT BR        Mdispari Pe = 2M−2 M  Q   2σ
                                                                                                                                                                    PSK
                                                                                                                                               n                    Esercizio
Correlazione                                                                                                                                                        Banda [300, 3200][Hz] posso trasmettere
rRxR(t, t + τ) = E[x(t + τ) x(t)] =                                                                               Probabilità simbolo corretto
                                                        DSB                                                       Pc = P [ak = ak̂ ] =                              1/T = 2900 simboli/s
     a b fx (t, t + τ) da db                            Segnale in uscita                                                         −V                 V              Per trasmetter almeno 19 kbit/s devo usare
 Proprietà                                                                                                        P [ak = −1] · P [ 2 0 ≤ ak + nk ≤ 20 ] =          almeno 7 bit e costellazione di 128
                                                        s̃(t) = 1/4AT AM AR s1 (t)                                   −V                              V
1) rx (0) = E[x2 (t)] = Mx ≥ 0                                                                                    P [ 2 0 ≤ ak + nk ] + P [ak + nk ≤ 20 ]           Esercizio
                                                        Potenza del segnale in uscita                                                                               Trasmissione 4Mbit/s con 4PSK, calcolare
 2) rx (τ) ∈ R                                          E[s̃2 (t)] = 1/4A2T A2M A2R · Ms                          QAM                                               banda minima
3) rx è pari e semidefinita positiva                                                                                                                                4PSK       quindi       2bit/s,   trasmettiamo
                                                        Potenza trasmessa MT = 1/2A2T MS                          Frequenza richiesta 1/T [Hz ] = 2fN [Hz ]
                                                                                                                                                                    4/2Msibol/s, necessari 2[MHz]
 Densità spettrale                                      Potenza del rumore                                        Con M simboli trasmetto log2 Mbit/simbolo         QAM
 Rx (f ) = F                                            Mñ = E[ñ(t)] = 2B 12 A2R R0 = BR0 A2R                   Probabilità di decisione corretta
            R [rx (τ)]                                                                                            Pc = PcI · PcQ = (PcP AM )2 =
                                                                                                                                                                    Esercizio
 Rx (f ) = rx (τ)e−j2πf τ dτ                            Potenza ricevuta MR = A2M MT                                                                                Sistema 16-QAM, Banda 20[Khz], m = 16 bit
                                                                                                                                     0 !!2                          Per Shennon devo aver 40[Khz], Devo
 Rx (f ) = T rx (KT )e−j2πf KT
              P                                         Rapporto segnale rumore                                                    V
                                                                                                                    1 − 2NN−2 Q Q σ0                                trasmettere 40 · 103 · 16 bit
 Proprietà                                              Λc = Λ = MR /2R0 B = A2M MT /2R0 B                                                                                                 3
                                                                                                                            √                                       Banda T1 = 16·40·10      = 160[kHz]
- rRx reale e pari ↔ Rx (f )reale e pari                Banda richiesta 2B                                        con N = M                                                            4
- Rx (f ) = rx (0) = Mx Potenza                         Rapporto segnale rumore                                   )                                                 Esercizio
                                                                                                                  PSk                                               x(t) uniforme Rx = R0 triangle(f /B),
- Rx (f ) ≥ 0                                                                              2    2       2                                                           B = 20[KHz], 1024QAM, SNR=45
                                                                      E[s̃(t)] 1/4AT AM AR Ms                     Fase di punti φk = 2π
 Ciclostazionario
        R 1/T                                                   Λ=             =                                                         MK                         Uniforme 6m → 8bit/simb, teorema
 σx2 = 0 Rx (f ) df                                                   E[ñ(t)]     BR0 A2           R             Banda necessario T1                               2B = 40000 campioni/s
                                                                                                                                                                    Flusso pari 8 · 40000 = 320000bit/s,
   Formulario TSCE                                    Fourier                                               Periodicizzazione                                     X(f ) = N T sincN (f N T )ej2πf (N −1/2)T
   parzival3, page 2 of 2
                                                                                                                                          P
                                                      X(f ) = I dtx(t) · e−j2πf t                            x(t)                             y(t − kTp )         X(f ) = N T sincN (f N T )
                                                             R
                                                                                                                           →                                      Trigonometric gin
Segnali                                                           I                Iˆ                        X(f )                        P
                                                                                                                                               X(f − Tk )                      1+cos(2a)                  1−cos2 (a)
                                                                  R                R                                                                    p         cos2 (a) =      2          sin2 (b) =      2
                                  h =  A  1 A 2 T min           Z(T )          R/Z(1/T )                      Modifica    il moudlo      del dominio
 y                                                          R/Z(Tp )            Z(1/Tp )                                                                          Spaghetti      integrali
       A                A             T1 − T2                                                                                                                     R      0             R 0
                                                         Z(T )/Z(N T )      Z(1/N T )/Z(1/T )                                     I0                                f ·g = f ·g − f ·g
                                                                                                               I = I0 U =                  h(t, τ) = δu (t − τ)   R                R
                                                     x Proprietà                                                                Z(T   p)                            cos = sin         sin = − cos
  −T        T −T           T                           1) linearità                                                                                               R
                                                                                                                                                                      x    x n+1    R
                                                                                                                                                                                          1 = 1 · arctan x
                  2        2                           2) se s(t) è reale s(t) = s∗ (t) allora ha Deperiodicizzazione                                               a = n+1                     a        a
                                                                                                                                                                                       a2 +x2
                                      T1 + T2          simmetria hermitiana S(f ) = S ∗ (−f )                                                                     Filtri Numerici
                                                                                                             x(τ)                             y(t)                      −2         −1
                                                                                                                                                                  0.2z + 0.5z + 1, 5
Formule di Eulero                                      3) s(−t) ↔ S(−f )
                                                            ∗ (t) ↔ S ∗ (−f )                                                  ←                                  divido 0.1z−1 − 0.7z−1 + 1
                                                       4) s
cos(x) = e +e
             ix −ix                  ix −ix
                         sin(x) = e −e                 5) x ∗ y(t) ↔ X(f ) · Y (f )                                                                               Quoziente 2, Resto 1.9z−1 − 0.5
               2                       2i                                                                     Ristruttura modulo del segnale                      radici 0.5; 0.2
eix = cos x + i sin x                                  6) s(t − t0 ) ↔ S(f )e−j2πf t0                                                                              R         A             B
                                                       7) S(0) = area[s(t)]                                                                                       D = 1−0.2z−1 + 1−0.5z−1
                                                                                                                      I0                                          con A = −6, B = 5.5
                                                       8) s(0) = area[S(f )]                                   I=              U = I0 h(t, τ) = δI (t − τ)
Proprietà dei segnali
                                                       Solo nel dominio reale                                       Z(T p)                                        h(nT ) = 2T δZ(T ) (nT )+5.5·0.5n 10 (nT )−
Valor Medio R                                          1) Cambo di scala s(at) ↔ 1/|a| ·                                                                          6 · 0.2n 10 (nT )
limT →∞ 2T    1 T s(t) dt                              S(f /a)a ∈ R                                           Filtro Interpolatore                                Il T va solo nella risposta FIR
                 −T
Energia    di un  segnale                                                   ds(t)                            x(τ)                             y(t)
                                                       2)  Derivazione        dt
                                                                                  ↔   j2πf   S(f   )                           x                                         Scomposizione di polinomi
Es = |s(t)|2 dt
      R                                                                                                                        
                                                                                                                                                                                                Ai
                                                                                          R                                    
                                                       3)   Integrazione        y(t)  =     x(u)    du     ↔                   g
                                                                                                                                                                          (x − ai )            x−a            i
Es = |s(t)|2 dt
      P
                                                       Y (f ) = 1/2X(0)δR (f ) + X(f )/(j2πf )                                                                                                   Ai,1       Ai,2
Potenza di un segnale                                                                                                                                                     (x − ai )n                   +
                                                                                                                                                                                                (x−ai ) (x−ai )2
                                                                                                                                  ∞
                   1 |s(t)|2 dt
                       R
                                                                                                                                                                                                     Ai x+Bi
                                                                                                                                 X
Ps = limT →∞ 2T                                        Teorema      di Parseval                                     y(t) = T            x(KT )g(t − KT )           (x2 + ai x + bi ) ∆ < 0
                                                       R                                                                                                                                           x2 +ai x+bi
                                                          dtx(t)y ∗ (t) = df X(f )Y ∗ (f )
                                                                          R
Se l’energia è costante la potenza è                                                                                           k=−∞                               2 fast 2 Fourier
uguale alla Es2                                                                                                                                                              Trasformate notevoli
                                                       Esponenziali complessi                                 Filtri Numerici                                         rect(t/T )           T sinc(f T )
Esponenziale complesso                                                                                       x(nt)                           y(nt)
                                                       Con x(t) = Ae     j2πf   t
                                                                               0 e filtro h(t)                                                                      triangle(t/T )        T sinc2 (f T )
s(t) = Aei2πf0 t                                                                                                             h(nT )                                                 j
                                                                                                                                                                      sin(2πf t)    2 [δ(f + f0 ) − δ(f − f0 )]
funzione periodica di periodo 1/f0 . Se y(t) = A0 |H(f0 )| cos(2πf0 t+φ+∠(H(f0 )))                                                                                                  1
A ∈ R si ha simmetria hermitiana                                                                              L’uscita del filtro è pari a                            cos(2πf t)    2 [δ(f + f0 ) + δ(f − f0 )]
s∗ (−t) = Ae−i2πf0 (−t) = Aei2πf0 t=s(t)               campionamento
                                                                                                                P ) = x ∗ h(nT ) =
                                                                                                              y(nT                                                    e−πt
                                                                                                                                                                               2
                                                                                                                                                                                          e−πf
                                                                                                                                                                                                          2

                                                         x(t)                           y(kT  p )            T ∞  k=−∞ x(KT )h(nT − KT )                         Ciano provemo a far na inversion?
                                                                           
Impulso di Dirac
                                                                           
                                                                           y                                  La risposta in frequenza razionale                       Duali trasformazioni elementari
                                                        X(f )                            Y ( TK )                         Pr
                                                                                                                                 bk z−k                                 Tempo               Frequenza
Proprietà                                                                                      p              H(Z) = T Pk=0  q
    R∞                                                                                                                                −k                            Campionamento           Periodicizzazione
1) ∞ s(d)δR (t − t0 ) dt = s(t0 )                      Cambia la periodicità del dominio                                     k=0 ak z
                                                                                                                                                                     Interpolazione        Deperiodicizzazione
2) s(t) · δR (t − t0 ) = s(t0 )δR (t − t0 )                                                                   Tips and tricks                                       Periodicizzazione       Campionamento
                                                                                                              Conversione decibel                                  Deperiodicizzazione       Interpolazione
                                                               R          Z(T )                               Rapport Potenze [db] = 10 log10 (·)                 ZZ Top
Convoluzione                                             I=         U=              h(t, τ) = δI (t − τ)
        R                                                      I1           I1                                Rapport Ampiezze [db] = 20 log10 (·)                             Traformate notevoli
z(t) = x(u)y(t − u) du                                                                                        Serie geometrica                                             1                pn 10 (nT )
Proprietà
                                                                                                              P k
                                                                                                                 p = 1−p 1      P k
                                                                                                                                   kp = 1 2                             1−pz−1
                                                                                                                                           (1−p)                          pz−1
1) Lineare                                             Interpolatore
                                                                                                              PN k 1−pN +1                                                                      npn 10 (nT )
                                                                                                                                                                       (1−pz−1 )2
2) Associativa                                          x(kTp )                                                 0 p = 1−p                                                  1                 (n + 1)pn 10 (nT )
                                                                                      P
                                                                            x       Tp x(KT )δu (t − kTP )
3) area[x ∗ y] = area[x] · area[y]                                                                           P∞        K −2kT = 1                                     (1−pz−1 )2
                                                                                                                0 (−1) e
                                                                            
                                                                                                                                                                                 ∗
4) z(t) = x(t − t0 ) ∗ y(t) = z(t − t0 )                X( TK )                     1      K           k
                                                                                                                                       1−e2T                          r    + r −1          2|r||pn |ejn∠p 10 (nT )
                                                                                      P
                                                                                   Tp X( Tp )δu (f − TP )
Esempio                                                       p                                               Eulero’s pizza                                        1−pz−1    1−pz
     2         2           πt 2                        La peridicità del dominio non cambia                   (−1)k = ejkπ = cos(kπ)
e−πt ∗ e−πt = √1 e− 2                                                                                         Werner
                      2
Convoluzione di segnali periodici                                                                             cos(a) cos(b) = 12 [cos(a + b) + cos(a − b)]
                                                               Z(T )          R
x(t), y(t), t ∈ R/Z(Tp )                                 I=            U=           h(t, τ) = δu (t − τ)      sin(a) sin(b) = 12 [cos(a − b) − cos(a + b)]
        R Tp                                                    I1            I1
z(t) = 0 x(u)y(t − u) du                                                                                      sin(a) cos(b) = 12 [sin(a + b) + sin(a − b)]
                                                                                                              Sinc discreto
