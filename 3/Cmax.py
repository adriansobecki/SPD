import numpy as np


def CMAX(pi,n,m):  #dziala dla 2 na pewno
    
    C=np.zeros((len(pi),m),int)
    C[0,0]=pi[0].czasy[0]
    C[0,1]=C[0,0]+pi[0].czasy[1]
    
    for i in range(1,len(pi)):
        C[i,0]=C[i-1,0]+pi[i].czasy[0]

    for i in range(1,len(pi)):
        C[i,1]=max(C[i-1,1],C[i,0])+pi[i].czasy[1]

    return int(C[len(pi)-1,m-1])