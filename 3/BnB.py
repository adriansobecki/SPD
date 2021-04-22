
import copy
import operator
from Cmax import *
import numpy as np

Ub=10000
pi=[]
pi_optymalne=[]
m=0
n=0

def bound(pi,N):
    Cmax, C = CMAX(pi,n,m)
    LB0=Cmax+sum([N[i].czasy[m-1] for i in range(0,len(N))])
    return int(LB0)

def bound3(pi,N):   
    i = len(pi[0].czasy)     # uzyskanie liczby maszyn ze zbioru zadan
    LB = np.zeros((i,1),dtype=int)  # wektor do policzenia wartosci max  
    x = len(pi)      # liczba uszeregowanych zadan
    Cmax, C = CMAX(pi,len(pi),len(pi[0].czasy))

    for ind in range(i):    # petla dla kazdej maszyny
        LB[ind] = C[x-1,ind] + sum([N[a].czasy[ind] for a in range(len(N))])
        min_w = 0
        for k in range(ind+1,i):
            min_w += min([N[a].czasy[k] for a in range(len(N))])
        LB[ind] += min_w

    return int(max(LB))





def bnb(j,N,pi):
    global Ub
    global pi_optymalne
    pi.append(j)
    N.remove(j)
    #print([N[k].numer for k in range(0,len(N))])
    if N:
        LB=bound3(pi,N)
        #print(LB)
        if LB<Ub:
            for j in N:
                bnb(j,copy.copy(N),copy.copy(pi))
    else:
         Cmax,C=CMAX(pi,n,m)
         #print(Cmax)
         if Cmax<Ub:
            Ub=Cmax
            pi_optymalne=copy.copy(pi)
            #print(pi)
    #print(pi_optymalne)
    #return(pi_optymalne)



def bnb_algorithm(zadania,nn,mm):
    N=copy.copy(zadania)
    global m
    global n
    m=mm
    n=nn
    for j in N:
        bnb(j,copy.copy(N),copy.copy(pi))

    return pi_optymalne