import numpy as np
import operator


def PD(J):
    order=[]
    lenght=2**len(J)
    memory=np.full(lenght,0)

    for D in range(1,lenght):
        sum,indexs=func(J,D)
        
        memory[D]=func2(J,D,sum,indexs,memory,order)
    
    return memory[lenght-1],order_fun(order,len(J))

    

def func(J,D):
    lenght=len(J)
    tasks=bin(D)[2:].zfill(lenght)

    sum=0
    indexs=[]
    for i,x in enumerate(tasks):
        if x == '1':
            sum+=J[lenght-i-1].p
            indexs.append(lenght-i-1)  # numer zadania ktore wystepuje w odpowienym zapisie binarnym (do sumy wszystko)
    
    return sum, indexs

def func2(J,D,sum,indexs,memory,order):

    maxes={}
    for index in indexs:
        x=2**index
        maxes[index]=max(sum-J[index].d,0)*J[index].w+memory[D-x]
    
    minimum=min(maxes.items(), key=operator.itemgetter(1))
    
    order.append(minimum[0])
    return minimum[1]


def order_fun(order,lenght):
    x=[]
    l=len(order)-1
    x.append(order[l]+1)

    for i in range(lenght-1):
        l-=2**(x[i]-1)
        x.append(order[l]+1)

    return x