from max6675 import MAX6675
from machine import Pin
import time

sck = Pin(2, Pin.OUT)  
cs = Pin(7, Pin.OUT)   
so = Pin(16, Pin.IN)    

sensor = MAX6675(sck, cs, so)  

while True:
    print("Temperatura =", sensor.read())  
    time.sleep(1)  
