from microbit import *

letter = 1

A = Image("05500:50050:55550:50050:50050")																				
B = Image("55500:50050:55500:50050:55500")																				
C = Image("05550:50000:50000:50000:05550")																				
D = Image("55500:50050:50050:50050:55500")																				
E = Image("55500:50000:55500:50000:55500")																				
F = Image("55500:50000:55500:50000:50000")																				
G = Image("05550:50000:50055:50005:05550")																				
H = Image("50050:50050:55550:50050:50050")																				
I = Image("55500:05000:05000:05000:55500")																				
J = Image("55555:00050:00050:50050:05500")																				
K = Image("50050:50500:55000:50500:50050")																				
L = Image("50000:50000:50000:50000:55550")																				
M = Image("50005:55055:50505:50005:50005")																				
N = Image("50005:55005:50505:50055:50005")																				
O = Image("05500:50050:50050:50050:05500")																				
P = Image("55500:50050:55500:50000:50000")																				
Q = Image("05500:50050:50050:05500:00550")																				
R = Image("55500:50050:55500:50050:50005")																				
S = Image("05550:50000:05500:00050:55500")																				
T = Image("55555:00500:00500:00500:00500")																				
U = Image("50050:50050:50050:50050:05500")																				
V = Image("50005:50005:50005:05050:00500")																				
W = Image("50005:50005:50505:55055:50005")																				
X = Image("50050:50050:05500:50050:50050")																				
Y = Image("50005:05050:00500:00500:00500")																				
Z = Image("55550:00500:05000:50000:55550")																				

while True:
    
    if pin0.is_touched():
        display.off()
        
    if pin1.is_touched():
        display.on()
        
    if button_a.was_pressed():
        letter = letter + 1

    if button_b.was_pressed():
        letter = letter - 1

    if letter == 1:
        display.show(A)
        
    if letter == 2:
        display.show(B)

    if letter == 3:
        display.show(C)

    if letter == 4:
        display.show(D)

    if letter == 5:
        display.show(E)

    if letter == 6:
        display.show(F)

    if letter == 7:
        display.show(G)

    if letter == 8:
        display.show(H)

    if letter == 9:
        display.show(I)

    if letter == 10:
        display.show(J)
        
    if letter == 11:
        display.show(K)

    if letter == 12:
        display.show(L)

    if letter == 13:
        display.show(M)
        
    if letter == 14:
        display.show(N)

    if letter == 15:
        display.show(O)

    if letter == 16:
        display.show(P)

    if letter == 17:
        display.show(Q)

    if letter == 18:
        display.show(R)

    if letter == 19:
        display.show(S)

    if letter == 20:
        display.show(T)

    if letter == 21:
        display.show(U)
        
    if letter == 22:
        display.show(V)

    if letter == 23:
        display.show(W)

    if letter == 24:
        display.show(X)

    if letter == 25:
        display.show(Y)

    if letter == 26:
        display.show(Z)

    if letter == 26 and button_a.is_pressed():
        letter = 0

    if letter == 1 and button_b.is_pressed():
        letter = 27
