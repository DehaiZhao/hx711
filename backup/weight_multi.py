import multiprocessing
import time
import RPi.GPIO as GPIO
import sys
from hx711 import HX711
import config

Channels = config.Channels
unit = config.unit
#unit = [1,1,1,1,1]
offset = []

def cleanAndExit(cindex):
    print 'Cleaning {}...'.format(cindex)
    GPIO.cleanup()

def set_tare(channel):
    hx = HX711(channel[0],channel[1])
    hx.set_reading_format('LSB','MSB')
    tare = hx.get_tare()
    offset.append(tare)
    print 'initialize {} done!,offset is {}'.format(Channels.index(channel),tare)

def get_weight(channel,offset,unit):
    val = []
    hx = HX711(channel[0],channel[1])
    hx.set_reading_format('LSB','MSB')
    hx.set_reference_unit(unit)
    hx.reset()
    hx.set_offset(offset)
    while True:
        try:
            for i in range(3):
                val.append(hx.get_weight(1))
            del val[val.index(max(val))]
            del val[val.index(min(val))]
            result[Channels.index(channel)] = float('%.1f'%val[0])
            val = []
            hx.power_down()
            hx.power_up()
            time.sleep(0.2)
        except (KeyboardInterrupt, SystemExit):
            cleanAndExit(Channels.index(channel))
    return result[:]
for channel in Channels:
    set_tare(channel)
result = multiprocessing.Array('d',range(len(Channels)))
i = 0
pool = multiprocessing.Pool(processes = len(Channels))
for channel in Channels:
    pool.apply_async(get_weight,(channel,offset[i],unit[i],))
    i += 1
print "init done"

def get_result():
    return result[:]        

if __name__ == '__main__':
    while True:
        print get_result()
        time.sleep(0.2)
