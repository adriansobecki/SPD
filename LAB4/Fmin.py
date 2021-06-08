def FMIN(pi):
    C = []  # czasy zakonczenia zadan
    T = []  # czasy opoznien zadan
    F = []  # opoznienia
    Fmin = 0
    C.append(pi[0].p)
    
    for i in range(1,len(pi)):
        C.append(pi[i].p + C[i-1])

    for i in range(len(pi)):
        T.append(max(C[i]-pi[i].d,0))

    for i in range(len(pi)):
        F.append(T[i]*pi[i].w)

    Fmin = sum(F)

    return Fmin