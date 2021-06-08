from Cmax import CMAX
import numpy as np
from copy import copy
from operator import attrgetter


def insert_(pi,ob,ind):
    pi.insert(ind,ob)
    C = CMAX(pi)
    return C


k = 1
pi = []
pi2 = []
w = []

def NEH(zadania):
    w = copy(zadania)
    w.sort(key=attrgetter('w'),reverse=True)

    pi.append(w[0])
    w.pop(0)
    pi2 = copy(pi)
    k = 2

    while w:
        ob = w[0]
        tab = []
        for l in range(k):
            tab.append(insert_(copy(pi),ob,l))
        
        min_ = min(tab)
        #print(tab)
        ind = tab.index(min_)
        pi.insert(ind,ob)
        w.pop(0)
        k += 1

    return pi

