import numpy as np
"""
    n = len(pi)
    m = len(pi[0].czasy)
    C = np.zeros((n,m),dtype=int) # tablica zadania x maszyny

    C[0,0] = pi[0].czasy[0]
    for i in range(1,m) :
        C[0,i] = C[i-1,0] + pi[0].czasy[i]     # pierwszy wiersz macierzy C

    for i in range(1,n):        # pierwsza kolumna
        C[i,0] = C[i-1,0] + pi[i].czasy[0]

    for i in range(1,n):        # reszta macierzy
        for j in range(1,m):
            C[i,j] = max(C[i-1,j],C[i,j-1]) + pi[i].czasy[j]
"""

def sciezka(pi,index):
    n = len(pi)
    m = len(pi[0].czasy)

    C=np.zeros((m,n),int)
    C[0,0]=pi[0].czasy[0]

    for i in range(1,m):
        C[i,0]=C[i-1,0]+pi[0].czasy[i]
        
    for i in range(1,n):
        C[0,i]=C[0,i-1]+pi[i].czasy[0]

    for k in range(1,m):
        for i in range(1,n):
            C[k,i]=max(C[k,i-1],C[k-1,i])+pi[i].czasy[k]

    
    zadania=[]
    maszyny=[]
    zadania.append(pi[n-1].numer+1)
    maszyny.append(m)


    aktualnyczas=C[m-1,n-1]
    czas_wykonania=pi[n-1].czasy[m-1]
    for k in range(m-1,-1,-1):
        for i in range(n-1,-1,-1):
            if C[k,i]==aktualnyczas-czas_wykonania:
                zadania.append(pi[i].numer+1)
                maszyny.append(k+1)
                aktualnyczas=C[k,i]
                czas_wykonania=pi[i].czasy[k]

    #print(zadania)
    maxilosc=0
    indexzadania=0
    for i in range(1,n+1):
        ilosc=zadania.count(i)
        if ilosc>=maxilosc and index!=i:
            maxilosc=ilosc
            indexzadania=i
    #print(maszyny)
    #print(indexzadania)

    return indexzadania