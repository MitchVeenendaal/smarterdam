import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

while True:
    print('start')
    GPIO.output(18,GPIO.HIGH)
    
    
    
