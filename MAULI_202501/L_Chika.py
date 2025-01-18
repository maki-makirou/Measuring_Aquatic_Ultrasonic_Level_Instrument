from machine import Pin 
from time import sleep
led = Pin(25,Pin.OUT)
n=0
while True:
    led.toggle()
    print("counter is {}".format(n))
    n=n+1
    sleep(1)
