
def sc(tasks):
    tasks[0].s_time(tasks[0].r)
    tasks[0].c_time(tasks[0].s+tasks[0].p)
    Cmax = tasks[0].c + tasks[0].q
    tasks[0].cq_time(tasks[0].c+tasks[0].q)
    for i in range(1,len(tasks)):
        tasks[i].s_time(max(tasks[i].r,tasks[i-1].c))
        tasks[i].c_time(tasks[i].s+tasks[i].p)
        tasks[i].cq_time(tasks[i].c+tasks[i].q)
        Cmax = max(Cmax,(tasks[i].c + tasks[i].q))

    return Cmax

def print_sc(tasks):
    Cmax=sc(tasks)
    print("pi: ",[i.id for i in tasks])
    print("s: ",[i.s for i in tasks])
    print("c: ",[i.c for i in tasks])
    print("cq: ",[i.cq for i in tasks])
    print("Cmax: ",Cmax)