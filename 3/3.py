#import numpy as np
from RandomNumberGenerator import *
#import copy
#import operator
from BF import *
from Cmax import *
from BnB import *

n=6  #zadania
m=2  #maszyny
Z=5

rand=RandomNumberGenerator(Z)

J=np.zeros((n,m),int)




for i in range(n):
    for j in range(m):
        J[i,j]=rand.nextInt(1,29)

print(J)


l=0
k=n-1
N=copy.copy(J)
pi=np.zeros(n,int)

for q in range(n):
    min=N.argmin()
    indeks_maszyny=min%m  #0 -> 1  || 1 -> 2
    numer_zadania=int(min/2)

    N[numer_zadania,0]=10000000
    N[numer_zadania,1]=10000000

    if indeks_maszyny==0:
        pi[l]=numer_zadania+1
        l+=1
    else:
        pi[k]=numer_zadania+1
        k-=1

print(pi)























"""


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



def bound(pi,N):
    LB0=CMAX(pi)+sum([N[i].czasy[m-1] for i in range(0,len(N))])
    return int(LB0)



def CMAX(pi):  #dziala dla 2 na pewno
    
    C=np.zeros((len(pi),m),int)
    C[0,0]=pi[0].czasy[0]
    C[0,1]=C[0,0]+pi[0].czasy[1]
    
    for i in range(1,len(pi)):
        C[i,0]=C[i-1,0]+pi[i].czasy[0]

    for i in range(1,len(pi)):
        C[i,1]=max(C[i-1,1],C[i,0])+pi[i].czasy[1]

    return int(C[len(pi)-1,m-1])


zadania=[]
for k in range(n):
    zadania.append(zadanie(k))

N=copy.copy(zadania)
Ub=10000
pi=[]
pi_optymalne=[]



def bnb(j,N,pi):
    global Ub
    global pi_optymalne
    pi.append(j)
    N.remove(j)
    print([N[k].numer for k in range(0,len(N))])
    if N:
        LB=bound(pi,N)
        print(LB)
        if LB<Ub:
            for j in N:
                bnb(j,copy.copy(N),copy.copy(pi))
    else:
         Cmax=CMAX(pi)
         print(Cmax)
         if Cmax<Ub:
            UB=Cmax
            pi_optymalne=copy.copy(pi)
            #print(pi)
    #print(pi_optymalne)
    #return(pi_optymalne)
            


for j in N:
    bnb(j,copy.copy(N),copy.copy(pi))
            


print([pi_optymalne[k].numer for k in range(0,len(pi_optymalne))])
print(CMAX(pi_optymalne))
print(CMAX(zadania))

test=[]
test.append(zadania[0])
test.append(zadania[3])
test.append(zadania[5])
test.append(zadania[4])
test.append(zadania[1])
test.append(zadania[2])
print(CMAX(test))






def bnb_all(j,N,pi):
    global Ub
    global pi_optymalne
    pi.append(j)
    N.remove(j)
    if N:
        for j in N:
            bnb_all(j,copy.copy(N),copy.copy(pi))
    else:
         Cmax=CMAX(pi)
         print(Cmax)
         if Cmax<Ub:
            Ub=Cmax
            pi_optymalne=copy.copy(pi)

            


for j in N:
    bnb_all(j,copy.copy(N),copy.copy(pi))

print([pi_optymalne[k].numer for k in range(0,len(pi_optymalne))])

"""