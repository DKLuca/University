---
fonte: "I call 2022.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Course of Analog Electronics – 2021-2022

Prof. Simone Buso

Test #1: January 28th, 2022

E1

Consider the circuit in Fig. 1. The circuit parameters at T = 25°C are the following:

VDD = 10 V; RG1 = 150 k; RG2 = 100 k; RG3 = 100 k; RS1 = 1 k; RD2 = 15 k; RF = 15 k;
Rs = 1 k; Cs = 10 F; CG = 10 F; CS1 = 10 F.

M1 (E-NMOS): Vt1 = 2 V; IDSS1 = 2.4 mA; r0 = +∞;
M2 (E-PMOS): Vt2 = -3 V; IDSS2 = 3.6 mA; r0 = +∞;




                                 Fig. 1 – A case of two stage amplifier.

Considering all capacitors to be equivalent to open circuits, determine:
     1. the value of RD1 such that the voltage at the drain of M2 is VO = 2 V in the steady state;
     2. the operating points (VDS, IDS) of M1 and M2.
Assuming Cs, CS1 and CG to be equivalent to short circuits at the frequencies of interest (i.e. at mid-
band), determine also:
     3. the voltage gain Av = vo /vs of the amplifier;
     4. the input resistance indicated in the figure.

Applying the short circuit time constant method, determine, finally:
     5. the low frequency bandwidth limit fL of the amplifier.
Course of Analog Electronics – 2021-2022

Prof. Simone Buso

Test #1: January 28th, 2022

E2




               Fig. 2 – Partially compensated OpAmp with high pass frequency response.

Consider the operational amplifier configuration shown in Fig. 2. The circuit parameters are the
following:

R1 = 10 k; R2 = 220 k; C1 = 100 nF;

OpAmp: Ad0 = 105 [V/V]; 0 = 10 rad/s; 1 = 5000 rad/s.

Considering capacitor CC equivalent to an open circuit, determine:

     1.   the expression of the ideal circuit voltage gain Av(s)= vo /vs ;
     2.   an estimation of the circuit phase margin;
     3.   the complete block diagram of the amplifier, according to feedback theory;
     4.   the expression of the input scaling function ks(s) in the above diagram.

Then, define

     5. the maximum value of capacitor CC for which the amplifier maintains approximately the
        same frequency response of the original circuit up to the crossover frequency;
     6. the new phase margin of the circuit, considering capacitor CC equal to the value found at
        point 5. (hint: the compensated beta network shows a low frequency pole and a high
        frequency pole, the latter falling well above the crossover frequency ….)
