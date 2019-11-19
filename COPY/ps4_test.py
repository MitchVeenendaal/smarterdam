# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:44:27 2019

@author: juuls
"""



import pygame

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
                if event.axis == 3:
                    if event.value < -0.09:
                        self.ps4_speed = (( event.value * -1) * 3)

                        
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 1:
                    print ("wow pressed the X button")
            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 1:
                    print ("he-yump")
                    




#if __name__ == "__main__":
while True:
    ps4 = PS4Controller()
    ps4.listen()
    if ps4.ps4_speed == 0:
        pass
    else:
        print ('speed', ps4.ps4_speed)
    
    