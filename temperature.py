from w1thermsensor import W1ThermSensor
import time

sensor = W1ThermSensor()
def get_temperature_in_celsius():
    temperature_in_celsius = sensor.get_temperature()
    return temperature_in_celsius

if __name__ == '__main__':
    while True:
        print get_temperature_in_celsius()
        time.sleep(1)
