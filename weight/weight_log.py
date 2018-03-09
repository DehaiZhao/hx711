import requests
import time
import json

weight_ip = 'http://192.168.2.88:8888/debug/'

while True:
    f = open('wt.txt','a')
    w = []
    w_o = []
    tm = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    weight = json.loads(requests.get(weight_ip).content)['res']
#    for i in range(6):
#        w.append(weight[i])
    weight_o = json.loads(requests.get(weight_ip).content)['res_o']
#    for i in range(6):
#        w_o.append(weight_o[i])
    ti = json.loads(requests.get(weight_ip).content)['ti']
    tc = json.loads(requests.get(weight_ip).content)['tc']
    print tm,str(weight),str(weight_o),str(ti),str(tc)
    f.write(tm+' '+str(weight) + ' ' + str(weight_o) + ' ' + str(ti) + ' ' + str(tc) +'\n')
    f.close()
    time.sleep(600)




