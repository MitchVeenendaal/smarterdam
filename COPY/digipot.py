import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
print("Led on" )
GPIO.output(21, GPIO.HIGH)
time.sleep(10)
print ("Led off")
GPIO.output(21, GPIO.LOW)

