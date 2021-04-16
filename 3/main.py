
from RandomNumberGenerator import *
from BF import *
from Cmax import *
from BnB import *

n=6  #zadania
m=2  #maszyny
Z=5

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



pi_optymalne=bf_algorithm(zadania,n,m)
print([pi_optymalne[k].numer for k in range(0,len(pi_optymalne))])
print(CMAX(pi_optymalne,n,m))


pi_optymalne=bnb_algorithm(zadania,n,m)
print([pi_optymalne[k].numer for k in range(0,len(pi_optymalne))])
print(CMAX(pi_optymalne,n,m))