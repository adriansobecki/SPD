
import copy
import operator
from Cmax import *

Ub=10000
pi=[]
pi_optymalne=[]
m=0
n=0

def bound(pi,N):
    LB0=CMAX(pi,n,m)+sum([N[i].czasy[m-1] for i in range(0,len(N))])
    return int(LB0)




def bnb(j,N,pi):
    global Ub
    global pi_optymalne
    pi.append(j)
    N.remove(j)
    #print([N[k].numer for k in range(0,len(N))])
    if N:
        LB=bound(pi,N)
        #print(LB)
        if LB<Ub:
            for j in N:
                bnb(j,copy.copy(N),copy.copy(pi))
    else:
         Cmax=CMAX(pi,n,m)
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