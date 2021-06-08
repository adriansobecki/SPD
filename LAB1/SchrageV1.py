
import math
import operator
import copy
import heapq
from sc import sc

def Schrage(tasks):
    #print("\n"+"Kolejnosc po algorytmie Schrage:")
    k = 1
    N = copy.copy(tasks) # zbior zadan nieuszeregowanych
    G = []  # zbior zadan gotowych do realizacji
    pi = [] # prawidlowa kolejnosc
    t = min(N,key=operator.attrgetter("r")).r

    while G or N:
        while N and min(N,key=operator.attrgetter("r")).r <= t:
            ob = min(N,key=operator.attrgetter("r"))
            G.append(ob)
            N.remove(ob)
        if G:
            ob = max(G,key=operator.attrgetter("q"))
            G.remove(ob)
            pi.append(ob)
            t += ob.p
            k += 1
        else:
            t = min(N,key=operator.attrgetter("r")).r

    Cmax = sc(pi)
    
    return Cmax,pi