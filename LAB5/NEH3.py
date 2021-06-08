from Cmax import CMAX
import numpy as np
from copy import copy
from operator import attrgetter
from sciezka_krytyczna import *

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

def NEH_v3(zadania):
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
        #tab = []
        #tab=copy.copy(pi)
        nrzadania=sciezka(pi,ob.numer)  #zwrot numeru zadania ktore sie pojawia najczesciej na sciezce krytycznej

        for i in pi:
            if i.numer+1==nrzadania:
                ob=i

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

