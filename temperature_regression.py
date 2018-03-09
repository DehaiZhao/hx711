import requests
import json
import numpy as np
import time
import warnings
import config
warnings.simplefilter('ignore',np.RankWarning)

weight_ip = 'http://localhost:8888/debug/'

w = [[] for i in range(len(config.Channels))]
t = []

def revise(temperature_offset):
    f = open('config.py','r')
    lines = f.readlines()
    f = open('config_n.py','w')
    lines[2] = 'temperature_offset = ' + str(temperature_offset)
    f.writelines(lines)

def t_regression():
    weight = json.loads(requests.get(weight_ip).content)['res_o']
    for i in range(len(config.Channels)):
        w[i].append(weight[i])
    t.append(json.loads(requests.get(weight_ip).content)['tc'][0])
    r = []
    for i in range(len(config.Channels)):
        r.append(np.polyfit(t,w[i],1)[0])
    revise(r)
    if len(t)>100:
        del t[0]
        for i in range(len(config.Channels)):
            del w[i][0]
    print r

if __name__ == '__main__':
    while True:
        t_regression()
        time.sleep(1800)
