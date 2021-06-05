
from RandomNumberGenerator import *
from Cmax import *
import numpy as np
from NEH import *
import copy as copy

n = 10  #zadania
m = 10  #maszyny
Z = 350    # ziarno
q=7000  #ilosc iteracji
cadance=4

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



def TabuSearch(pi):
    n=len(pi)
    tabuList=np.zeros((n,n),int)
    #print(tabuList)
    pi_best=pi
    k_best=0
    j_best=0

    for it in range(q):
        C_best=10000000
        for j in range(0,n):
            for k in range(j+1,n):
                if tabuList[j,k]<it:
                    pi_new=replace(copy.copy(pi),j,k)
                    if(CMAX(pi_new))<C_best:
                        C_best=CMAX(pi_new)
                        j_best=j
                        k_best=k
        pi=replace(pi,j_best,k_best)
        tabuList[j_best,k_best]=it+cadance

        if(CMAX(pi)<CMAX(pi_best)):
            pi_best=pi
    return pi_best


def TabuSearch2(pi):
    n=len(pi)
    tabuList=np.zeros((n,n),int)
    #print(tabuList)
    pi_best=pi
    k_best=0
    j_best=0

    for it in range(q):
        C_best=10000000
        for j in range(0,n):
            for k in range(j+1,n):
                pi_new=replace(copy.copy(pi),j,k)
                if tabuList[j,k]<it or ((CMAX(pi_new)*0.99)<Cmax):
                    if(CMAX(pi_new))<C_best:
                        C_best=CMAX(pi_new)
                        j_best=j
                        k_best=k
        pi=replace(pi,j_best,k_best)
        tabuList[j_best,k_best]=it+cadance

        if(CMAX(pi)<CMAX(pi_best)):
            pi_best=pi
    return pi_best



def replace(pi,j,k):
    task1=pi[j]
    pi[j]=pi[k]
    pi[k]=task1
    return pi

#tabu_pi=TabuSearch(zadania)
#print(CMAX(tabu_pi))

print("Algorytm NEH:")
pi_N = NEH(zadania)
print([pi_N[k].numer+1 for k in range(0,len(pi_N))])
Cmax= CMAX(pi_N)
print("Cmax: " + str(Cmax) + "\n")

print("Algorytm TabuSearch:")
pi_T = TabuSearch(pi_N)
print([pi_T[k].numer+1 for k in range(0,len(pi_T))])
Cmax= CMAX(pi_T)
print("Cmax: " + str(Cmax) + "\n")

print("Algorytm TabuSearch2:")
pi = TabuSearch2(pi_N)
print([pi[k].numer+1 for k in range(0,len(pi))])
Cmax= CMAX(pi)
print("Cmax: " + str(Cmax) + "\n")
