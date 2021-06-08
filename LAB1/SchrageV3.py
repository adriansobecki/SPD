import math
import operator
import copy
import heapq
from TaskClass import single_task
from sc import sc


def Schrage_v3(tasks):
    #print("\n"+"Cmax po algorytmie Schrage pmtn:")
    Cmax = 0
    G = []
    N = copy.copy(tasks)
    t = 0
    l = single_task(0)
    l.add_q(1_000_000)

    while G or N:
        while N and min(N,key=operator.attrgetter("r")).r <= t:
            ob = min(N,key=operator.attrgetter("r"))
            G.append(ob)
            N.remove(ob)
            if ob.q > l.q:
                l.p = t - ob.r
                t = ob.r
                if l.p > 0:
                    G.append(l)
        if not G:
            t = min(N,key=operator.attrgetter("r")).r
        else:
            ob = max(G,key=operator.attrgetter("q"))
            G.remove(ob)
            l = ob
            t = t + ob.p
            Cmax = max(Cmax,t+ob.q)
    
    #print("Cmax = ", Cmax)
    return Cmax
