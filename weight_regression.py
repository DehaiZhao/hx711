import requests
import json
import time
import os
import numpy as np
import config
import sys

weight_ip = 'http://localhost:8888/debug/'

Scales = [10,50,200,500]

def revise(ur):
    f = open('config.py','r')
    lines = f.readlines()
    f = open('config_n.py','w')
    lines[1] = 'unit = ' + str(ur) + '\n'
    f.writelines(lines)

def w_regression(scale):
    r = []
    for i in range(len(config.Channels)):
        w = []
        print 'Please put {}g on {} box and press enter'.format(scale,i)
        raw_input()
        print 'calculating...'
        for j in range(20):
            w.append(json.loads(requests.get(weight_ip).content)['res_o'][i])
        r.append(np.mean(w)/scale)
    return r                

def revise_s(ur, channel):
    f = open('config.py','r')
    lines = f.readlines()
    line_u = lines[1][8:-2].split(',')
    line = 'unit = ['
    for i in range(channel):
        line = line + line_u[i] + ','
    line = line + str(ur) + ','
    for i in range(channel+1,len(config.Channels)):
        line = line + line_u[i] + ','
    line = line[0:-1] + ']' + '\n'
    f = open('config_n.py','w')
    lines[1] = line
    f.writelines(lines)

def w_regression_s(scale, channel):
    r = 0
    w = []
    print 'Please put {}g on {} box and press enter'.format(scale,channel)
    raw_input()
    print 'calculating...'
    for j in range(20):
        w.append(json.loads(requests.get(weight_ip).content)['res_o'][channel])
    r = np.mean(w)/scale
    return r
       
if __name__ == '__main__':
    r = [[] for i in range(len(config.Channels))]
    unit = []
    ur = []
    if len(sys.argv) > 1:
        for scale in Scales:
            ur.append(w_regression_s(scale, int(sys.argv[1])))
        unit.append(np.mean(ur))
        revise_s(unit[0],int(sys.argv[1]))
        print sys.argv[1],'done!'
    else:
        for scale in Scales:
            ur = w_regression(scale)
            for i in range(len(config.Channels)):
                r[i].append(ur[i])
        for i in range(len(config.Channels)):
            unit.append(np.mean(r[i]))
        revise(unit)
        print 'All done!'
