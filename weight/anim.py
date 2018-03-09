import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import requests
import time
import json

weight_ip = 'http://192.168.2.88:8888/'
y=[[0]*100,[0]*100,[0]*100,[0]*100,[0]*100,[0]*100]

fig,ax=plt.subplots(2,3)

line,=ax[0][0].plot(np.random.random(100))
ax[0][0].set_ylim(-1,2000)


line1,=ax[0][1].plot(np.random.random(100))
ax[0][1].set_ylim(-1,2000)

line2,=ax[0][2].plot(np.random.random(100))
ax[0][2].set_ylim(-1,2000)

line3,=ax[1][0].plot(np.random.random(100))
ax[1][0].set_ylim(-1,2000)

line4,=ax[1][1].plot(np.random.random(100))
ax[1][1].set_ylim(-1,2000)

line5,=ax[1][2].plot(np.random.random(100))
ax[1][2].set_ylim(-1,2000)


def update(data):
    line.set_ydata(data[0])
    line1.set_ydata(data[1])
    line2.set_ydata(data[2])
    line3.set_ydata(data[3])
    line4.set_ydata(data[4])
    line5.set_ydata(data[5])
    return line,line1,line2,line3,line4,line5,


def data_gen():
    for i in range(6):
        y[i].append(json.loads(requests.get(weight_ip).content)['res'][i])
    if len(y[i])>100:
        for i in range(6):
            del y[i][0]
    yield y
    
ani = animation.FuncAnimation(fig,update,data_gen,interval=200,blit=True)
plt.show()
