import numpy as np

#for i in range(1,5):
#    print(i)
def CMAX(pi):  #dziala dla 2 na pewno
    n = len(pi)
    m = len(pi[0].czasy)

    #print(n,m)
    C=np.zeros((m,n),int)
    #print(C)
    C[0,0]=pi[0].czasy[0]

    for i in range(1,m):
        #C[0,i]=C[0,i-1]+pi[0].czasy[i]
        C[i,0]=C[i-1,0]+pi[0].czasy[i]
        #C[0,1]=C[0,0]+pi[0].czasy[1]
        
    for i in range(1,n):
        C[0,i]=C[0,i-1]+pi[i].czasy[0]
        #C[i,0]=C[i-1,0]+pi[i].czasy[0]

        
        #for i in range(1,n):
        #    C[i,1]=max(C[i-1,1],C[i,0])+pi[i].czasy[1]

    for k in range(1,m):
        for i in range(1,n):
            C[k,i]=max(C[k,i-1],C[k-1,i])+pi[i].czasy[k]
            #C[i,k]=max(C[i-1,k],C[i,k-1])+pi[i].czasy[k]

    return int(C[m-1,n-1])

"""

def CMAX(pi):
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

    return int(C[n-1,m-1])
"""