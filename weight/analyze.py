import numpy as np
import matplotlib.pyplot as plt

#plt.axis([0,10,0,1])
plt.ion()
y=[]
x=[]
i=0
while True:
    if i>5:
        del x[0]
        del y[0]

    y.append(np.random.random())
    x.append(i)
    i+=1
    plt.plot(x,y,color='red')
    plt.pause(0.1)

