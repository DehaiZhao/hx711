import multiprocessing
import time
import RPi.GPIO as GPIO
import sys
from hx711 import HX711

Channels = [[5,6],[8,7],[20,21],[12,16],[23,24],[14,15]]

def cleanAndExit():
    print 'Cleaning...'
    GPIO.cleanup()
    print 'Bye!'
    sys.exit()

def set_tare(channel):
    hx = HX711(channel[0],channel[1])
    tare = hx.get_tare()
    return tare

if __name__=='__main__':
    pool = multiprocessing.Pool(processes = 4)
    result = []
    for channel in Channels:
        result.append(pool.apply_async(set_tare,(channel,)))
    pool.close()
    pool.join()
    f = file('offset.txt','w')
    for res in result:
        f.write(str(res.get())+'\n')
