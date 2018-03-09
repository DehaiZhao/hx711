import numpy as np

w = [[] for i in range(6)]
t = []
r = []

f = open('logs.txt','r')
lines = f.readlines()
for line in lines:
    line = line.strip()[1:-1]
    for i in range(6):
        w[i].append(float(line.split(',')[i]))
    t.append(float(line.split(',')[6]))
for i in range(6):
    r.append(np.polyfit(t,w[i],1)[0])
print str(r)[1:-1]
