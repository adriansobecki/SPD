import copy
import time
from Fmin import *

Ub=10000
pi=[]
pi_optymalne=[]
n=0

def bf(j,N,pi):
    global Ub
    global pi_optymalne
    pi.append(j)
    N.remove(j)
    if N:
        for j in N:
            bf(j,copy.copy(N),copy.copy(pi))
    else:
         Fmin = FMIN(pi)
         if Fmin<Ub:
            Ub=Fmin
            pi_optymalne=copy.copy(pi)


def bf_algorithm(zadania,nn):
    start = time.time()
    N=copy.copy(zadania)
    global n
    n=nn

    for j in N:
        bf(j,copy.copy(N),copy.copy(pi))

    czas = time.time() - start
    return pi_optymalne, czas