---
fonte: "digitale_con_soluz_19_09_2024.pdf"
metodo: "ocr"
da_rivedere: true
---

Prova scritta di Fondamenti di Elettronica Digitale
19 settembre 2024

INGUNGSe sae tous sets sca aes sys Canoe Slviissrsrcnveraw eee Matricola: . 306.5...
Punti Assegnati: ...... arate Yiencay Aeacaus Hiden eteaees femmes

Sia Vpp=1.5V, si considerino esauriti i transitori al 90% dell’escursione di tensione, e si assumano i
seguenti parametri tecnologici per i MOSFET:

Parametro | n-MOSFET | p-MOSFET

Vro 0.35 —0.35
150 75

Latin x 0.1
Coe 13
Cesa iB 0.6

 

 

 

A— 01

os

. CL

0 02 far
So

Nella figura sopra riportata i gate sono realizzati con circuiti di tipo CMOS che devono avere ritardi
di salita e discesa uguali. La capacita di carico vale Cp=18fF. In relazione al circuito di figura si
risponda ai seguenti quesiti.

 

2. Supponendo inoltre che i transistori n-MOS dei gate NOR e NAND abbiano dimé
Sn=1, si calcolino le capacité C4, Cg, Co, Cp agli ingressi A, B, C e D. (4 punti)

3. Supponendo che le capacitdé ai nodi O1 ed 02 coincidano con le capacité di ingresso del gate a
valle ed indicando con Sx il dimensionamento dei transistori n-MOS del gate XOR, si esprima ‘
funzione di Sx il ritardo di commutazione a fronte della transizione dell’ingresso B da 0 a 1 (con
A=1,C=1,D= 0) e si determini il valore di Sx che minimizza tale ritardo ed il valore del
ritardo stesso. (12 punti)

4. Con i dimensionamenti del punto precedente, si calcoli il ritardo a
dell’ingresso C da 0 a 1 (con A= 1, B=0, D =0). (6 punti)

5. Supponendo che gli ingressi A, B, C e D siano sta
che la frequenza di lavoro del circuito sia f=1.3
circuito. (6 punti)

 

!
1. Si indichi la funzione logica F(A,B,C,D) realizzata al nodo di uscita Out. (2 punti) |

    
 
 
 
  


---

  
 
   
     
 
 
 
  
   
    
 
 
  
 
 
 
 
   
  
  
   

Soluzione
19 Settembre 2024

1, Siccome la funzione logica al nodo O1 vale Fo:=AB ed al nodo 02
= vale Fon2=C +D, al
funzione logica sul nodo di uscita sara F(A,B,C,D)=AB(C + D) + AB(C + D). aan
2. La capacité agli ingressi Ae Bala capacita di ingresso C,,
la capacita di ingresso Cyoy del NOR. Siccome i transisto
minimo ed i ritardi di salita e discesa dei gate devono

and del NAND mentre agli ingressi Ce De
ri n-MOS dei gate hanno dimensionamento
essere uguali avremo:

Cnand = (1+ €/2)Cayy = O.751fF Cror = (1+ 2€)O yy, = 1.878 fF
con Cyn=(CorLigry+2L ern Caso]=0.376f F.

3. Le capacitd ai nodi 01, 02 Possono essere stimate come la capacité di ingresso del gate XOR.
Tenuto conto della sua topologia abbiamo quindi

 

Cor = Co2 = Sx(1+€)Cxn

A fronte della transizione (A, B,C, D)=(1, 0, 1,0)-+(1, 1, 1,0) si ha una commutazione del NAND e
quindi nel nodo di uscita, mentre il NOR non commuta. Il ritardo & quindi il ritardo dall’ingresso
B all'uscita e pud essere espresso come

2Sx(1 +2)Cur 2C;, ty

= oF (Ve/V; ooo FF Ver /V; = 19; ——
°° Brandl?) By Von V/V) + e570) Br pg F Ve! Von) = Sx + =
dove Spand=1 é il dimensionamento nel pull-down del NAND ed abbiamo introdotto i due tempi

— 4 +¢)Cany a — ACL _ Ses
t= ~Bi.Vpp 1 (t/Von) = 42.75ps tg = Be Ven F(Vr/Vpp) 682.7ps

Il ritardo pud essere minimizzato annullando la derivata di ty rispetto a Sy, che fornisce

a cui corrisponde un ritardo t)=341.7ps.

4. Il ritardo a fronte della transizione (A, B,C, D)=(1,0,1,0)-+(1,0,0,0) @ quello che corrsponde alla
commutazione del NOR e, in particolare, é il ritardo dall’ingresso C all'uscita. Considerando che il
gate NOR ha lo stesso dimensionamento S,=1 del gate NAND per i transistori n-MOS, il ritardo
si pud calcolare come

 

= a 2 _ 9569
tp= gx + 5. .2ps
aol c . a ied. ; i padtidat
Siccome gli ingressi sono indipendenti ed equiprobabili, le attivita di commutazione ai nodi
c ee cae ottenute semplicemente analizzando le tabelle di verita delle funzioni logiche
‘computate ai nodi 01, 02 ed Out. Il computo delle configurazioni di ingresso che portano ad
" un’uscita pari a uno fornisce
3 al _ 10
mes oS Fos 5
possiamo calcolare la potenza dinamica come

$eVBp [Pou(t ~ Pos)Cox + Foa(t — Pos) Con + Pow(t ~ Pow)Ct] = 17.284
