from Cmax import CMAX
import numpy as np
from copy import copy
from operator import attrgetter


def insert_(pi,ob,ind):
    pi.insert(ind,ob)
    C = CMAX(pi)
    return C

def delete_(pi,ind):
    pi.pop(ind)
    C = CMAX(pi)
    return C


k = 1
pi = []
pi2 = []
w = []

def NEH_v2(zadania):
    w = copy(zadania)
    w.sort(key=attrgetter('w'),reverse=True)    # posortowanie zadan po w malejaco

    pi.append(w[0])
    w.pop(0)
    pi2 = copy(pi)
    k = 2

    while w:
        ob = w[0]
        tab = []
        for l in range(k):
            tab.append(insert_(copy(pi),ob,l))  # wstawianie
        min_ = min(tab) # najmniejsze Cmax
        ind = tab.index(min_)   # wiemy na jaka pozycje wstawic w oryginale
        pi.insert(ind,ob)   # wstawianie w oryginale
        tab=[]
        for i in range(len(pi)):
            if i != ind:
                tab.append(delete_(copy(pi),i)) # usuniecie zadania, zeby Cmax bylo jak najmniejsze
            else:
                tab.append(10_000)
        min_ = min(tab)
        ob = pi[tab.index(min_)]    # zadanie dla ktorego Cmax jest min po usunieciu
        pi.remove(ob)
        tab = []
        for l in range(k):
            tab.append(insert_(copy(pi),ob,l))
        min_ = min(tab)
        ind = tab.index(min_)
        pi.insert(ind,ob)
        w.pop(0)
        k += 1

    return pi

