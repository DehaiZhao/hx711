import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711
import config

unit = config.unit

def cleanAndExit():
    print "Cleaning..."
    GPIO.cleanup()
    print "Bye!"
    sys.exit()

hx1 = HX711(8,7)
hx2 = HX711(20,21)
hx3 = HX711(12,16)
hx4 = HX711(23,24)
hx5 = HX711(14,15) 
# I've found out that, for some reason, the order of the bytes is not always the same between versions of python, numpy and the hx711 itself.
# Still need to figure out why does it change.
# If you're experiencing super random values, change these values to MSB or LSB until to get more stable values.
# There is some code below to debug and log the order of the bits and the bytes.
# The first parameter is the order in which the bytes are used to build the "long" value.
# The second paramter is the order of the bits inside each byte.
# According to the HX711 Datasheet, the second parameter is MSB so you shouldn't need to modify it.
hx1.set_reading_format("LSB", "MSB")
hx2.set_reading_format('LSB','MSB')
hx3.set_reading_format('LSB','MSB')
hx4.set_reading_format('LSB','MSB')
hx5.set_reading_format('LSB','MSB')
# HOW TO CALCULATE THE REFFERENCE UNIT
# To set the reference unit to 1. Put 1kg on your sensor or anything you have and know exactly how much it weights.
# In this case, 92 is 1 gram because, with 1 as a reference unit I got numbers near 0 without any weight
# and I got numbers around 184000 when I added 2kg. So, according to the rule of thirds:
# If 2000 grams is 184000 then 1000 grams is 184000 / 2000 = 92.
#hx.set_reference_unit(113)
hx1.set_reference_unit(unit[0])
hx2.set_reference_unit(unit[1])
hx3.set_reference_unit(unit[2])
hx4.set_reference_unit(unit[3])
hx5.set_reference_unit(unit[4])

hx1.reset()
hx1.tare()
hx2.reset()
hx2.tare()
hx3.reset()
hx3.tare()
hx4.reset()
hx4.tare()
hx5.reset()
hx5.tare()
while True:
    try:
        # These three lines are usefull to debug wether to use MSB or LSB in the reading formats
        # for the first parameter of "hx.set_reading_format("LSB", "MSB")".
        # Comment the two lines "val = hx.get_weight(5)" and "print val" and uncomment the three lines to see what it prints.
        #np_arr8_string = hx.get_np_arr8_string()
        #binary_string = hx.get_binary_string()
        #print binary_string + " " + np_arr8_string
        
        # Prints the weight. Comment if you're debbuging the MSB and LSB issue.
        val1 = hx1.get_weight(1)
        val2 = hx2.get_weight(1)
        val3 = hx3.get_weight(1)
        val4 = hx4.get_weight(1)
        val5 = hx5.get_weight(1)
        
        print 'val1:{},val2:{},val3:{},val4:{},val5:{}'.format(val1*-0.10,val2*-0.10,val3*-0.10,val4*-0.10,val5*-0.10)

        hx1.power_down()
        hx1.power_up()
        hx2.power_down()
        hx2.power_up()
        hx3.power_down()
        hx3.power_up()
        hx4.power_down()
        hx4.power_up()
        hx5.power_down()
        hx5.power_up()
        time.sleep(0.2)
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
