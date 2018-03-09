import multiprocessing
import time
import RPi.GPIO as GPIO
import sys
from hx711 import HX711
import config

Channels = config.Channels
unit = config.unit
#unit = [1,1,1,1,1,1]
offset = []
HX = []
result = [0]*6

def cleanAndExit(cindex):
    print 'Cleaning {}...'.format(cindex)
    GPIO.cleanup()

def set_tare(channel):
    hx = HX711(channel[0],channel[1])
    tare = hx.get_tare()
    offset.append(tare)
    print 'initialize {} done!,offset is {}'.format(Channels.index(channel),tare)

def init_pin(channel,offset,unit):
    init_hx = HX711(channel[0],channel[1])
    init_hx.set_reading_format('LSB','MSB')
    init_hx.set_reference_unit(unit)
    init_hx.reset()
    init_hx.set_offset(offset)
    HX.append(init_hx)

def get_weight(hx):
    try:
        val = hx.get_weight(1)
        result[HX.index(hx)] = float('%.1f'%(val*-0.10))
        hx.power_down()
        hx.power_up()
        time.sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit(Channels.index(channel))
    return result
i=0
for channel in Channels:
    set_tare(channel)
    init_pin(Channels[i],offset[i],unit[i])
    i += 1
print "init done"

def get_result():
    for hx in HX:
        res = get_weight(hx)
    return res     

if __name__ == '__main__':
    while True:
        print "===res:", get_result()
        time.sleep(0.2)
