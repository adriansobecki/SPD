from generatory import RandomNumberGenerator
import math
import operator
import copy
import heapq

NUMBER = 10  # ilosc zadan do wykonania
SEED = 1
MAX = 29


class task:
    def __init__(self,i):
        self.id = i

    def add_r(self,r_time):
        self.r = r_time

    def add_p(self,p_time):
        self.p = p_time

    def add_q(self,q_time):
        self.q = q_time
    
    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return other.q < self.q


def print_list(list):
    print("nr: ",[i.id for i in list])
    print("r: ",[i.r for i in list])
    print("p: ",[i.p for i in list])
    print("q: ",[i.q for i in list])


def sc(list):
    s.append(list[0].r)
    c.append(s[0]+list[0].p)
    Cmax = c[0] + list[0].q
    cq.append(c[0] + list[0].q)
    for i in range(1,len(list)):
        s.append(max(list[i].r,c[i-1]))
        c.append(s[i] + list[i].p)
        cq.append(c[i] + list[i].q)
        Cmax = max(Cmax,(c[i] + list[i].q))
    
    print("pi: ",[i.id for i in list])
    print("s: ",s)
    print("c: ",c)
    print("cq: ",cq)
    print("Cmax: ",Cmax)
    return Cmax, c



generator = RandomNumberGenerator.RandomNumberGenerator(SEED)
s = []  # moment rozpoczecia zadania
c = []  # moment zakonczenia zadania
cq = [] # moment oddania zadania
Cmax = 0

list = []
A = 0   # suma czasow r

for i in range(NUMBER):
    list.append(task(i+1))
    list[i].add_p(generator.nextInt(1,MAX))
    A += list[i].p

for i in range(NUMBER):
    list[i].add_r(generator.nextInt(1,A))

for i in range(NUMBER):
    list[i].add_q(generator.nextInt(1,A))

print_list(list)
print("\n"+"Permutacja naturalna:")
sc(list)


# algorytm Schrage

def Schrage():
    print("\n"+"Kolejnosc po algorytmie Schrage:")
    k = 1
    N = copy.copy(list) # zbior zadan nieuszeregowanych
    G = []  # zbior zadan gotowych do realizacji
    pi = [] # prawidlowa kolejnosc
    t = min(N,key=operator.attrgetter("r")).r

    while G or N:
        while N and min(N,key=operator.attrgetter("r")).r <= t:
            ob = min(N,key=operator.attrgetter("r"))
            G.append(ob)
            N.remove(ob)
        if G:
            ob = max(G,key=operator.attrgetter("q"))
            G.remove(ob)
            pi.append(ob)
            t += ob.p
            k += 1
        else:
            t = min(N,key=operator.attrgetter("r")).r

    s.clear()
    c.clear()
    cq.clear()
    [Cmax,c] = sc(pi)

    return pi, Cmax, c


def Schrage_v2():
    print("\n"+"Kolejnosc po algorytmie Schrage kolejkowanym:")
    k = 1
    N = copy.copy(list)
    G = []
    pi = [] # prawidlowa kolejnosc

    N=sorted(N,key=operator.attrgetter("r"),reverse=True)
    t = N[NUMBER-1].r
   #print(t)
    while G or N:
        while N and N[len(N)-1].r <= t:
            ob = N.pop()
            heapq.heappush(G,ob)
        if G:
            ob = heapq.heappop(G)
            pi.append(ob)
            t += ob.p
            k += 1
        else:
            t = N[len(N)-1].r

    s.clear()
    c.clear()
    cq.clear()
    sc(pi)


def Schrage_v3():
    print("\n"+"Cmax po algorytmie Schrage pmtn:")
    Cmax = 0
    G = []
    N = copy.copy(list)
    t = 0
    l = task(0)
    l.add_q(1_000_000)

    while G or N:
        while N and min(N,key=operator.attrgetter("r")).r <= t:
            ob = min(N,key=operator.attrgetter("r"))
            G.append(ob)
            N.remove(ob)
            if ob.q > l.q:
                l.p = t - ob.r
                t = ob.r
                if l.p > 0:
                    G.append(l)
        if not G:
            t = min(N,key=operator.attrgetter("r")).r
        else:
            ob = max(G,key=operator.attrgetter("q"))
            G.remove(ob)
            l = ob
            t = t + ob.p
            Cmax = max(Cmax,t+ob.q)
    
    print("Cmax = ", Cmax)

UB = 1_000_000
def Carlier():
    (U,Cmax,c) = Schrage()
    if Cmax < UB:
        UB = Cmax
        pi = copy.copy(U)
    b = 0
    for i in list:
        C = i.q + c[i.id-1] 
        if C > b:
            b = C  

    a = 1_000_000
    suma = 0
    for i in list:
        C = i.r + list[b-1].q
        for j in range(i.id-1,b):
            suma += list[j]
        C += suma



#Schrage()
#Schrage_v2()
#Schrage_v3()
Carlier()
