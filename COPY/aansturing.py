# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:15:22 2019

@author: juuls
"""

import RPi.GPIO as GPIO
import pygame
import time as tm

class PS4Controller(object):
    """Class representing the PS4 controller. Pretty straightforward functionality."""

    controller = None
    axis_data = None
    button_data = None


    def __init__(self):
        """Initialize the joystick components"""
        
        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()
        self.ps4_speed = 0
        self.stop = 0

    def listen(self):
        """Listen for events to happen"""
        
        if not self.axis_data:
            self.axis_data = {}

        if not self.button_data:
            self.button_data = {}
            for i in range(self.controller.get_numbuttons()):
                self.button_data[i] = False

        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    if event.value > 0.1:
                        print (event.value)
                    if event.value < -0.1:
                        print (event.value)
                if event.axis == 4:
                    if event.value > -1:
                        self.ps4_speed = ( (event.value + 1)*49) 
                        print ('input' , self.ps4_speed)
                        
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 1:
                    self.stop = event.value
            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 1:
                    print ("he-yump")
                    



GPIO.setwarnings(False)           #do not show any warnings
GPIO.setmode (GPIO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
GPIO.setup(21,GPIO.OUT)           # initialize GPIO19 as an output.
p = GPIO.PWM(21,10)          #GPIO19 as PWM output, with 100Hz frequency
p.start(0)  

while True:                               #execute loop forever
    ps4 = PS4Controller()
    ps4.listen()
    x = ps4.ps4_speed
    print (x)#execute loop for 50 times, x being incremented from 0 to 49.
    if x > 0:
        p.ChangeDutyCycle(x)
    #change duty cycle for varying the brightness of LED.
    tm.sleep (0.01)
    if ps4.stop == 1:
        print('stopped')
        break


    