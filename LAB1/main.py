from generatory import RandomNumberGenerator
import math
import operator
import copy
import heapq

from TaskClass import single_task
from SchrageV1 import Schrage
from SchrageV2 import Schrage_v2
from SchrageV3 import Schrage_v3
from carlier import Carlier
from sc import sc
from sc import print_sc

NUMBER = 8  # ilosc zadan do wykonania
SEED = 1
MAX = 29


def print_list(tasks):
    print("nr: ",[i.id for i in tasks])
    print("r: ",[i.r for i in tasks])
    print("p: ",[i.p for i in tasks])
    print("q: ",[i.q for i in tasks])



generator = RandomNumberGenerator.RandomNumberGenerator(SEED)
Cmax = 0

tasks = []
A = 0   # suma czasow r

for i in range(NUMBER):
    tasks.append(single_task(i+1))
    tasks[i].add_p(generator.nextInt(1,MAX))
    A += tasks[i].p

for i in range(NUMBER):
    tasks[i].add_r(generator.nextInt(1,A))

for i in range(NUMBER):
    tasks[i].add_q(generator.nextInt(1,A))

"""
tasks=[]
for i in range(6):
    tasks.append(single_task(i+1))
tasks[0].add_p(2)
tasks[0].add_r(1)
tasks[0].add_q(5)

tasks[1].add_p(3)
tasks[1].add_r(2)
tasks[1].add_q(4)

tasks[2].add_p(1)
tasks[2].add_r(8)
tasks[2].add_q(6)

tasks[3].add_p(2)
tasks[3].add_r(7)
tasks[3].add_q(3)

tasks[4].add_p(3)
tasks[4].add_r(6)
tasks[4].add_q(7)

tasks[5].add_p(4)
tasks[5].add_r(4)
tasks[5].add_q(1)
"""

print_list(tasks)
print("\n"+"Permutacja naturalna:")
print_sc(tasks)




cmax,pi=Schrage(tasks)
print("\n"+"Kolejnosc po algorytmie Schrage:")
print_sc(pi)

pi=Schrage_v2(tasks,NUMBER)
print("\n"+"Kolejnosc po algorytmie Schrage kolejkowanym:")
print_sc(pi)


cmax=Schrage_v3(tasks)
print("\n"+"Cmax po algorytmie Schrage pmtn:")
print(cmax)

pi=Carlier(tasks,NUMBER)
print("\n"+"Kolejnosc po algorytmie Carliera")
print_sc(pi)
