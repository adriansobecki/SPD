from RandomNumberGenerator import *
from Cmax import *
from NEH import *
from sciezka_krytyczna import *
from NEH3 import *
from NEH2 import *
from NEH import *
n = 5  #zadania
m = 10  #maszyny
Z = 350    # ziarno

rand=RandomNumberGenerator(Z)


class zadanie:
    def __init__(self,numer):
        self.numer=numer
        self.czasy=[]
        self.w = 0
        for i in range(m):
            self.czasy.append(rand.nextInt(1,29))
            self.w += self.czasy[i]

zadania=[]
for k in range(n):
    zadania.append(zadanie(k))
    
print("Algorytm NEH:")
pi = NEH(zadania)
print([pi[k].numer+1 for k in range(0,len(pi))])
Cmax= CMAX(pi)
print("Cmax: " + str(Cmax) + "\n")
#sciezka(pi,4)

"""
print("Algorytm NEH2:")
pi = NEH_v2(zadania)
print([pi[k].numer+1 for k in range(0,len(pi))])
Cmax= CMAX(pi)
print("Cmax: " + str(Cmax) + "\n")

print("Algorytm NEH3:")
pi = NEH_v3(zadania)
print([pi[k].numer+1 for k in range(0,len(pi))])
Cmax= CMAX(pi)
print("Cmax: " + str(Cmax) + "\n")
"""