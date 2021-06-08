from RandomNumberGenerator import *
from BF import *
from Fmin import *
from greedy import *
from PD import *

n = 8  # zadania
Z = 7242 # ziarno

rand=RandomNumberGenerator(Z)


class task:
    def __init__(self,i):
        self.id = i

    def add_p(self,p_time):
        self.p = p_time

    def add_w(self,weight):
        self.w = weight

    def add_d(self,d_time):
        self.d = d_time

tasks = []
A = 0

for i in range(n):
    tasks.append(task(i))
    tasks[i].add_p(rand.nextInt(1,29))
    A += tasks[i].p

for i in tasks:
    i.add_w(rand.nextInt(1,9))

for i in tasks:
    i.add_d(rand.nextInt(1,29))

print("Zadania:")
print("nr: ", end = " ")
print([tasks[k].id+1 for k in range(len(tasks))])
print("p: ", end = " ")
print([tasks[k].p for k in range(len(tasks))])
print("w: ", end = " ")
print([tasks[k].w for k in range(len(tasks))])
print("d: ", end = " ")
print([tasks[k].d for k in range(len(tasks))])
    

print()
pi_optymalne, czas = bf_algorithm(tasks,n)
print("Algorytm BF:\npi: ",end = " ")
print([pi_optymalne[k].id+1 for k in range(0,len(pi_optymalne))])
Fmin = FMIN(pi_optymalne)
print("Fmin: " + str(Fmin))
print("czas dzialanian programu: {0:02f}s\n".format(czas))

pi_optymalne, czas = greedy(tasks)
print("Algorytm greedy:\npi: ",end = " ")
print([pi_optymalne[k].id+1 for k in range(0,len(pi_optymalne))])
Fmin = FMIN(pi_optymalne)
print("Fmin: " + str(Fmin))
print("czas dzialanian programu: {0:02f}s\n".format(czas))

print("Algorytm PD:")
start = time.time()
result,order=PD(tasks)
czas = time.time() - start
order=list(reversed(order))
print("pi: ",order)
print("Fmin: ",result)
print("czas dzialanian programu: {0:02f}s\n".format(czas))