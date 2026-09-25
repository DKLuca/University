---
fonte: "soltsce06_09.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Traccia Soluzioni

Domanda

La relazione ingresso/uscita è                   Z
                                         y(t) =           d⌧ x(⌧ ) h(t, ⌧ ), t 2 U.
                                                      I
Per un filtro                                     Z
                                         y(t) =           d⌧ x(⌧ ) g(t   ⌧ ), t 2 I.,
                                                      I
quindi un filtro è una tf lineare con nucleo h(t, ⌧ ) = g(t ⌧ ).
   La tf y(t) =Im[x(t)] non è omogenea e dunque non è lineare, in quanto, per ↵ numero complesso
generico, Im[↵x(t)]6= ↵ Im[x(t)]. Infatti, il termine a sinistra è reale, mentre quello a destra è complesso.
Se ↵ = ↵R + j↵I , x(t) = xR (t) + jxI (t), Im[↵x(t)]=↵R xI (t) + ↵I xR (t), valore reale.

Es 1.                             Z +1
                                          sinc(3(t          1/3)) sinc(2(t    3/2))dt =
                                     1

(Parseval, nel prodotto, occorre tenere conto del coniugato nell’espressione della trasformata, che è
complessa)           Z   +1
                              (1/3) rect(f /3) e j2⇡f /3 (1/2) rect(f /2) e+j2⇡3f /2 df =
                          1
                             Z +1
                     (1/3)          (1/2) rect(f /2) e+j2⇡f (3/2 1/3) df = (1/3) sinc(7/3).
                               1
