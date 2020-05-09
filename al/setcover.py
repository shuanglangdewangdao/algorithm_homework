import random
from scipy import optimize as op
import numpy as np
from pulp import *
def buildxset(n):
    s = set()
    while len(s) < n:
      s.add(random.randint(0,10000))
    return s


def buildsubset(s):
    subsetlist = []
    xs = s | set()
    s0 = set()
    lisxs = list(xs)
    while len(s0) < 20 :
        s0.add(random.choice(lisxs))
    subsetlist.append(s0)
    xs = xs - s0
    while len(xs) >= 20:
        lisxs=list(xs)
        s1 = set()
        n = random.randint(1,20)
        x = random.randint(1,n)
        while len(s1) < x :
            s1.add(random.choice(lisxs))
        liss0 = list(s0)
        while len(s1) < n:
            s1.add(random.choice(liss0))
        subsetlist.append(s1)
        xs = xs - s1
        s0 = s1 | s0
    subsetlist.append(xs)
    zs = s | set()
    while len(subsetlist)<len(s):
        s1 = set()
        n = random.randint(1,len(zs))
        liszs = list(zs)
        while len(s1) < n:
            s1.add(random.choice(liszs))
        subsetlist.append(s1)
    return subsetlist

def greedy_set_cover(x,f):
    u = x | set()
    c = set()
    tf = []
    for i in range(len(f)):
        tf.append(f[i])
    cover = []
    while len(u)!=0:
        max = 0
        for i in range(len(tf)):
            if len(tf[i]|u) > len(tf[max]|u) :
                max = i
        u = u - tf[max]
        c = c | tf[max]
        cover.append(max)
        tf.pop(max)
    # print(c)
    return cover
def line_set_cover(x,f):
    a = np.ones((1,len(f)),dtype = np.int)
    c = np.ones((1,len(x)),dtype = np.int)
    # res = op.linprog(a,A_ub=f,b_ub=c,bounds=(0,1))
    # re = []
    # for i in range(len(res.x)):
    #     if res.x[i]>0.5:
    #         re.append(i)
    # return ressetcover
    # print(c)
    PB = LpProblem ( 'setcover' , LpMinimize )
    xs = []
    for i in range(0, len(f), 1):
        xs.append(LpVariable("e"+str(i), lowBound =0, cat = LpInteger))
    # print(xs)

    PB+= lpSum([a[0,i]*xs[i] for i in range(len(f))])
    for i in range(len(x)):
        for j in range(len(f)):
            PB+= lpSum([f[i,j]*xs[j] for j in range(len(f))]) >= c[0,j]
    status = PB.solve()
    # print ( "objective=", value(PB.objective) )
    # print(PB.variables)
    if status == 1:
        re = []
        i=0
        for v in PB.variables():
            if v.varValue.real >=1:
                re.append(i)
            i=i+1
        return re

    else:
        return None
     

import time

if __name__ == "__main__":
    nls = [100,1000,5000]
    for n in nls:
        ls = []
        out = []

        s = buildxset(n)
        ls = buildsubset(s)

        es = np.zeros((len(s),len(ls)),dtype = np.int)

        liss = list(s)
        for i in range(len(liss)):
            for j in range(len(ls)):
                if liss[i] in ls[j] :
                    es[i,j] = 1
        start=time.time()
        out = greedy_set_cover(s,ls)
        end = time.time()
        print("greed_set_cover:",end-start)
        start=time.time()
        line_set_cover(s,es)
        end = time.time()
        print("linesetcover:",end-start)


    
    