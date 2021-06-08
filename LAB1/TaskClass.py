


class single_task:
    def __init__(self,i):
        self.id = i

    def add_r(self,r_time):
        self.r = r_time

    def add_p(self,p_time):
        self.p = p_time

    def add_q(self,q_time):
        self.q = q_time

    def s_time(self, sTime):
        self.s=sTime
        
    def c_time(self, cTime):
        self.c=cTime

    def cq_time(self, cqTime):
        self.cq=cqTime
    
    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return other.q < self.q
