---
fonte: "soluz_digitale_10_07_2023.pdf"
metodo: "ocr"
da_rivedere: true
---

one della prova scritta di Fondamenti di Elettronica
10 luglio 2023 parte digitale

La funzione logica pud essere ottenuta sintetizzando il pull-down e quindi ricavando i| pull-up per
dualita In questo modo si ottiene il circuito in figura.

 

 

 

 

VOD
2
He
B !
=q Me
p-
A-d F(A.B,C,D)
2/5)

 

 

 

 

A EP =o
4 C I a5
V7

Per calcolare il dimensionamento relativo de transistori nMOS e pMOS Gi deve prima determinare
il dimensonamento equivalente del pull-up e del pull-down per le transizioni di caso migliore. Per
il pull-up il caso migliore corrisponde a A= B= C=D=0 ed in tal sg ha:
‘lip ee al 1 =o
Som 5) Se Sy2 7 Pe Ge

Per il pull-down, invece, il caso migliore corrispondea A=B=C=D=1esi ha:

4 ‘lia 5
Snea= Sn+ [ + = Snei= 3S

S, 2S,
Per uguagliare i tempi di salita e discesa cosi individuati dobbiamo imporre Bf, Sp eq= Bs Sp.eq che
fornisce: S 25 6
a AGT,
Sr 9 Bf

Per quanto riguarda i dimensionamenti assoluti S, ed Sp, la specifica sul tempo di commutazione
puo essere imposta sulla transizione di discesa scrivendo:

fl 2C,

~ Voo Bh (5/3),
Sapendo che per Vr=0.35V eVpp=1.8V si haF (Vr/ Vpp )=1.98, si ricava subito il valore di S,~2.0
per garantire ty =25ps. Dal dimensionamento relativo a s deduce Ss=aS,~8.3.

Tf F(Vr/Vpp)

Nota la capacita al terminale di gate di un transistore ad area minima Cy 1=2Lmin Caso +
CoxL% | y = 0.382f F, la capacita di ingresso del gate vale Cj y=(1+ a)Cy1~1.97f F ed ela medes-
ima a tutti gli ingressi dd gate. Dalla tabella di verita della funzione logica vediamo che per 5
pattern di ingresso su 16 possbili |'uscita de gate @ pari ad uno. Segli ingressi sono equi-probabili
Pa=Ppg=Pc=Pp=0.5, allorala switching activity del gate vale
S) a
Poo i(F) i= Pa (iS P9)i= 76 76= 0.215
La potenza dinamica relativa alla commutazione del nodo di uscita vale
Pgin = Po1(F)f CL Von ~ 7.990W

La riduzione dela tensione di alimentazione aumenta i ritardi a parita di dimensionamento. II
valore S, che assicura di mantenere un tempo di discesa di caso migliore pari a 25ps si ottiene dalla
espressione del ritardo gia usata al punto (1), Considerando che per Vr=0.35V e Vpp=1,.4V si ha
F (Vr/Vop )=2.20, il nuovo valore di S, vale circa 2.57. La switching activity non @ influenzata dal
valore di Vpp e quindi la Pgi, pud essere calcolata usando I’ espressione del punto (2) e cambiando
soltanto il valore di Vpp. Cosi facendo si ottiene Pyj,~4.83uW.
