import copy
import operator
from Cmax import *

Ub=10000
pi=[]
pi_optymalne=[]
n=0
m=0

def bf(j,N,pi):
    global Ub
    global pi_optymalne
    pi.append(j)
    N.remove(j)
    if N:
        for j in N:
            bf(j,copy.copy(N),copy.copy(pi))
    else:
         Cmax=CMAX(pi,n,m)
         #print(Cmax)
         if Cmax<Ub:
            Ub=Cmax
            pi_optymalne=copy.copy(pi)

            

def bf_algorithm(zadania,nn,mm):
    N=copy.copy(zadania)
    global n
    global m
    n=nn
    m=mm

    for j in N:
        bf(j,copy.copy(N),copy.copy(pi))

    return pi_optymalne
