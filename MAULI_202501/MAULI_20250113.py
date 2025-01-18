"""
Measuring Aquatic Ultrasonic Level Instrument (MAULI)

    Author: maki-makirou
    License: MIT license
    URL: https://github.com/maki-makirou/Measuring_Aquatic_Ultrasonic_Level_Instrument
"""


### Parameter settings ###
# Program version
VERSION ='0.9.0'

## Start mode
# Time to display settings
NUM_DISPLAY = 20    # Unit: Number of times, Range: 1 to 40
# Time to display measurement settings
SET_DISPLAY_TIME = 4    # Unit: seconds, Range: 1 to 30
# Number of measured values ​​displayed
DISPLAY_TIME = 2    # Unit: seconds, Range: 0.5 to 4

## Distance measurement mode
# Record start time after the power is turned on
RECORD_START_TIME = 60    # Unit: seconds, Range: 60 to 600
# Measurement interval at the time of log recording
INTERVAL_TIME = 60    # Unit: seconds, Range: 10 to 600
# Number of re-measurement at the time of abnormal value measurement
NUM_RETRY = 2    # Unit: Number of times, Range: 0 to 10
# Interval time of re-measurement
RETRY_TIME = 10    # Unit: seconds, Range: 1 to 10
# Time to light up led
LED_TIME = 0.05    # Unit: seconds, Range: 0 to 1
# Upper Limit value for re-measurement
UPPER_LIMIT = 0.2    # Unit: meter, Range: 0.1 to 1
# Lower Limit vue for re-measurement
LOWER_LIMIT = -0.2    # Unit: meter, Range: -0.1 to -1
# Turn on or turn off the power saving mode
POWER_SAVING_MODE = 1    # 0: OFF, 1: ON


### Main code　###
import utime, os
from machine import I2C, Pin, ADC, SPI
from pico_i2c_lcd import I2cLcd

start_time = utime.time()
trigger = Pin(0, Pin.OUT)
echo = Pin(1, Pin.IN)
led = Pin(25, Pin.OUT)
i2c = I2C(0, sda = Pin(16), scl = Pin(17), freq = 400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
lcd.putstr('Ver:' + str(VERSION) + '\n' + 'Interval:' + str(int(INTERVAL_TIME))+ 'sec')
utime.sleep(SET_DISPLAY_TIME)
lcd.clear()


def get_temp():
    sensor_temp = ADC(4)
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree.
    temperature = 27 - (reading - 0.706)/0.001721
    return round(temperature, 2)


def get_dist(temp):
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = round(((timepassed / 1000000) * (331.50 + (0.606681 * temp)))/ 2, 3)
    return distance, timepassed


def display_LCD():
    temp = get_temp()
    lcd.putstr('Dist: ' + f'{get_dist(temp)[0]:.3f}' + ' m\n' + 'Temp: ' + f'{temp:.2f}' + ' ' + 'C')
    utime.sleep(DISPLAY_TIME)
    lcd.clear()


def csv_data_conv(i, time, distance, temperature, timepassed, retry):
    time_4 = f'{time[4]:02}'
    time_5 = f'{time[5]:02}'
    date_time = f'{time[0]}/{time[1]}/{time[2]} {time[3]}:{time_4}:{time_5}'
    output = f'{i},{date_time},{distance},{temperature},{timepassed},{retry if retry else ""}'
    return output


## Start mode
i = 1
while True:
    now_time = utime.time()
    if now_time - start_time <= RECORD_START_TIME - 7:
        if i <= NUM_DISPLAY:
            display_LCD()
            i += 1
    else:
        lcd.putstr('will start recording soon...')
        utime.sleep(4)
        lcd.clear()
        lcd.backlight_off()
        break
    utime.sleep(0.1)


## Distance measurement mode
with open('log.csv', 'a') as f:
    output = 'No,time,distance(m),temperature(c),timepassed(u_sec),retry'
    print(output, file=f)
    f.close()
    print(output)
i = 1
pre_dist = 0.0
while True:
    time = utime.localtime()
    now_time = utime.time()
    if (now_time - start_time) % INTERVAL_TIME == 0:
        led.value(1)
        utime.sleep(LED_TIME)
        led.value(0)
        max_dist = 0.0
        for retry in range(0, NUM_RETRY + 1):
            if retry > 0:
                if POWER_SAVING_MODE == 1: 
                    machine.lightsleep(int(RETRY_TIME * 1000) - 500)
                else:
                    utime.sleep(int(RETRY_TIME) - 0.5)
            temp = get_temp()
            dist = get_dist(temp)
            print('    ' + str(dist[0]))
            if retry == 0:
                max_dist = dist[0]
                max_temperature = temp
                max_timepassed = dist[1]
                if (dist[0] - pre_dist) >= UPPER_LIMIT or (dist[0] - pre_dist) <= LOWER_LIMIT:
                    pass
                else:
                    break
            else:
                if (dist[0] - max_dist) >= UPPER_LIMIT or (dist[0] - max_dist) <= LOWER_LIMIT:
                    if dist[0] > max_dist:
                        max_dist = dist[0]
                        max_temperature = temp
                        max_timepassed = dist[1]
                else:
                    if dist[0] > max_dist:
                        max_dist = dist[0]
                        max_temperature = temp
                        max_timepassed = dist[1]
                    break
        pre_dist = max_dist
        output = csv_data_conv(i, time, max_dist, max_temperature, max_timepassed, retry)
        with open('log.csv', 'a') as f:
            print(output, file=f)
            f.close()
            print(output)
        i += 1
        pre_dist = max_dist
        if POWER_SAVING_MODE == 1:        
            machine.lightsleep(int(((INTERVAL_TIME - (RETRY_TIME * retry)) * 1000) - 500))
        else:
            utime.sleep(((INTERVAL_TIME - (RETRY_TIME * retry))) - 0.5)
    utime.sleep(0.1)
    
    
    