from max6675 import MAX6675
from machine import Pin
import time

sck = Pin(2, Pin.OUT)  # Initialize the clock pin (SCK) as an output pin
cs = Pin(7, Pin.OUT)   # Initialize the chip select pin (CS) as an output pin
so = Pin(16, Pin.IN)    # Initialize the data input pin (SO) as an input pin

sensor = MAX6675(sck, cs, so)  # Create an instance of the MAX6675 class with the specified pins

while True:
    print("Temperature =", sensor.read())  # Read and print the temperature value from the sensor
    time.sleep(1)  # Pause for 1 second
