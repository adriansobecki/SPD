import math
import operator
import copy
import heapq
from sc import sc
from SchrageV3 import Schrage_v3
from SchrageV1 import Schrage

ub = 1000000
pi=[]
def Carlier(tasks,NUMBER):
    U,pi_optymalne = Schrage(tasks)
    #print_list(pi_optymalne)
    #U=21
    #pi_optymalne=copy.copy(tasks)
    global ub

    if U < ub:
        ub = U
        pi = copy.copy(pi_optymalne)

    b=max(pi,key=operator.attrgetter('cq'))
    b_index=pi.index(b)
    a=[pi[i].r+b.q+sum([pi[k].p for k in range(i,pi.index(b)+1)]) for i in range(0,NUMBER)]
    #print(a)
    a_index=a.index(U)
    #a_index=max(a)
    c=[]
    for j in range(a_index,b_index):
        if pi[j].q<pi[b_index].q:
            c.append(j)
    
    try:
        c_index=max(c)
    except:
        return pi

    
    K=[]
    for i in range(c_index+1,b_index+1):
        K.append(pi[i])
    
    r=min([j.r for j in K])
    q=min([j.q for j in K])
    p=sum([j.p for j in K])

    r_pi=pi[c_index].r
    r_pi_old=r_pi

    pi[c_index].r=max(r_pi,r+p)

    LB=Schrage_v3(tasks)
    if LB<ub:
        Carlier(tasks,NUMBER)


    pi[c_index].r=r_pi_old

    q_pi=pi[c_index].q
    q_pi_old=q_pi
    pi[c_index].q=max(q_pi,q+p)

    LB=Schrage_v3(tasks)

    if LB<ub:
        Carlier(tasks,NUMBER)
    
    pi[c_index].q=q_pi_old


    return pi

