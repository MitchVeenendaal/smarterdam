import RPi.GPIO as GPIO
import time as tm

counter = 0
GPIO.setmode (GPIO.BOARD)
GPIO.setup (32, GPIO.OUT)
while True:
    counter +=1
    GPIO.output (32,GPIO.HIGH)
    tm.sleep (1)
    GPIO.output (32,GPIO.LOW)
    tm.sleep (2)
    if counter == 10:
        break
GPIO.cleanup ()