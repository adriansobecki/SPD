import copy
from operator import attrgetter
from RandomNumberGenerator import *
from BF import *
from Cmax import *
from BnB import *
import numpy as np


def Johnson(zadania):
    n = len(zadania)
    m = len(zadania[0].czasy)
    pi = np.zeros((n,1),dtype=int)
    l = 0
    k = n - 1
    N = copy.copy(zadania)  # zadania do uszeregowania
    pi = copy.copy(zadania) # zbior zadan uszeregowanych

    while N:
        nr_zadania = min(N,key=attrgetter("czasy")) # zadanie o min czasie p
        nr_maszyny = nr_zadania.czasy.index(min(nr_zadania.czasy))  # nr maszyny
        if nr_zadania.czasy[0] < nr_zadania.czasy[m-1]:     # mozliwe dla liczby maszyn > 2
            pi[l] = copy.copy(nr_zadania) # modyfikacja kolejnosci pi
            l += 1
        else:
            pi[k] = copy.copy(nr_zadania) # modyfikacja kolejnosci pi
            k -= 1

        N.remove(nr_zadania)    # usuwanie obiektu
    
    return pi