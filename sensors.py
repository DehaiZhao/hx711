import multiprocessing
import time
import RPi.GPIO as GPIO
import sys
from hx711 import HX711
import config
from temperature import get_temperature_in_celsius

Channels = config.Channels
unit = config.unit
temperature_offset = config.temperature_offset
offset = []
temperature_init = 0

def cleanAndExit(cindex):
    print 'Cleaning {}...'.format(cindex)
    GPIO.cleanup()

def set_tare(channel):
    hx = HX711(channel[0],channel[1])
    hx.set_reading_format('LSB','MSB')
    tare = hx.get_tare()
    offset.append(tare)
    print 'initialize channel {} done,offset is {}'.format(Channels.index(channel),tare)

def get_temperature():
    i = 0
    temperature_current[1] = get_temperature_in_celsius()
    while True:
        temperature_current[0] = get_temperature_in_celsius()
        i += 1
        if i > 3:
            temperature_current[1] = temperature_current[0]
            i = 0
        time.sleep(600)

def get_weight(channel,offset,unit,temperature_offset,temperature_init):
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
            result_o[Channels.index(channel)] = float('%.1f'%val[0])
            val[0] = val[0] - (temperature_current[1] - temperature_init)*temperature_offset
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
temperature_init = get_temperature_in_celsius()
print 'initialize temperature done,temperature is {}'.format(temperature_init)
result = multiprocessing.Array('d',range(len(Channels)))
result_o = multiprocessing.Array('d',range(len(Channels)))
temperature_current = multiprocessing.Array('d',range(2))
i = 0
pool = multiprocessing.Pool(processes = 12)
pool.apply_async(get_temperature,())
for channel in Channels:
    pool.apply_async(get_weight,(channel,offset[i],unit[i],temperature_offset[i],temperature_init,))
    i += 1
print 'init done!'

def get_result():
    return result[:]

def get_all():        
    return result[:],result_o[:],temperature_init,temperature_current[:]
if __name__ == '__main__':
    while True:
        print get_all()
        time.sleep(0.2)
