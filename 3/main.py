
from RandomNumberGenerator import *
from BF import *
from Cmax import *
from BnB import *
from Johnson import *

n=6  #zadania
m=2  #maszyny
Z=1

rand=RandomNumberGenerator(Z)


class zadanie:
    def __init__(self,numer):
        self.numer=numer
        self.czasy=[]
        for i in range(m):
            self.czasy.append(rand.nextInt(1,29))

zadania=[]
for k in range(n):
    zadania.append(zadanie(k))
    

print("Algorytm Johnsona:")
pi = Johnson(zadania)
print([pi[k].numer+1 for k in range(0,len(pi))])
Cmax, C = CMAX(pi,n,m)
print("Cmax: " + str(Cmax) + "\n")

pi_optymalne=bf_algorithm(zadania,n,m)
print("Algorytm BF:\npi: ",end = " ")
print([pi_optymalne[k].numer+1 for k in range(0,len(pi_optymalne))])
Cmax, C = CMAX(pi_optymalne,n,m)
print("Cmax: " + str(Cmax) + "\n")

pi_optymalne=bnb_algorithm(zadania,n,m)
print("Algorytm BnB:\npi: ",end = " ")
print([pi_optymalne[k].numer+1 for k in range(0,len(pi_optymalne))])
Cmax, C = CMAX(pi_optymalne,n,m)
print("Cmax: " + str(Cmax) + "\n")