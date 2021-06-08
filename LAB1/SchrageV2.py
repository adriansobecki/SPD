import math
import operator
import copy
import heapq
from sc import sc

def Schrage_v2(tasks,NUMBER):
    #print("\n"+"Kolejnosc po algorytmie Schrage kolejkowanym:")
    k = 1
    N = copy.copy(tasks)
    G = []
    pi = [] # prawidlowa kolejnosc

    N=sorted(N,key=operator.attrgetter("r"),reverse=True)
    t = N[NUMBER-1].r

   #print(t)
    while G or N:
        while N and N[len(N)-1].r <= t:
            ob = N.pop()
            heapq.heappush(G,ob)
        if G:
            ob = heapq.heappop(G)
            pi.append(ob)
            t += ob.p
            k += 1
        else:
            t = N[len(N)-1].r

    sc(pi)
    return pi