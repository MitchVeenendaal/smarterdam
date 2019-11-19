'''
Vooruit achteruit
Moeten bepaalde fases worden omgedraaid
'''

import time as tm
import matplotlib.pyplot as plt
import pygame

pygame.init()

done = False

pygame.joystick.init()

velocityData = []
timeData = []
distanceData = []

plt.subplot(2, 1, 1)

plt.title('Distance/Speed - time')
plt.ylabel('Distance (m)')

plt.subplot(2, 1, 2)

plt.xlabel('Time (s)')
plt.ylabel('Speed (m/s)')

plt.ion ()
plt.show ()


class Timer:
    def __init__ (self):
        self.time = tm.time ()
        
    def tick (self):
        self.oldTime = self.time
        self.time = tm.time ()
        self.deltaT = self.time - self.oldTime
        

timer = Timer ()

totalTime = 0
distance = 0 
velocityWheel = 0
reverseCounter = 0
graphResetCounter = 0
onePulseCounter = 0

deceleration = 6
acceleration = 0

wagonReverse = False
stateRelais = 'backwards'


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    joystick_count = pygame.joystick.get_count()


    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()


        name = joystick.get_name()


        axes = joystick.get_numaxes()

        for i in range(axes):
            axis = joystick.get_axis(i)

        buttons = joystick.get_numbuttons()

        for i in range(buttons):
            button = joystick.get_button(i)


        hats = joystick.get_numhats()


        for i in range(hats):
            hat = joystick.get_hat(i)




    print (f'Mijn snelheid is: {velocityWheel:4.2f} Mijn afgelegde afstand is: {distance:4.2f} Tijd: {totalTime:4.2f}')
    print (stateRelais)
    timer.tick ()
    
    if wagonReverse:
        if velocityWheel <= 0:
            if stateRelais == 'forward':
                stateRelais = 'backwards'
                #relais gaat nu naar achteren
            else:
                print ('Ik ga nu achteruit')
                velocityWheel -= acceleration * timer.deltaT
        
        else:
            print ('Remmen, Ik ga nu vooruit! Ik wil achteruit!')
            velocityWheel -= deceleration * timer.deltaT
            #Voertuig is nu aan het remmen
        
    else:
        if velocityWheel >= 0:
            if stateRelais == 'backwards':
                stateRelais = 'forward'
                #relais gaat nu naar voren
            else:    
                print ('Ik ga nu vooruit')
                velocityWheel += acceleration * timer.deltaT
            
        else:
            print ('Remmen, Ik ga nu achteruit! Ik wil vooruit!')
            velocityWheel += deceleration * timer.deltaT
            #Voertuig is nu aan het remmen
    
    distance += velocityWheel * timer.deltaT
    distanceData.append (distance)
    velocityData.append (velocityWheel)
    
    totalTime += timer.deltaT 
    timeData.append (totalTime)    
    
    graphResetCounter += 1
    if graphResetCounter >= 50 and timer.deltaT >= 0.09:
        plt.close ()
        graphResetCounter = 0
        
    
    plt.subplot(2, 1, 1)
    plt.plot(timeData, distanceData, 'b')
    
    plt.subplot(2, 1, 2)
    plt.plot(timeData, velocityData, 'r')
    
    plt.pause (0.0000002)
    
    #tm.sleep (0.01)
    if joystick.get_button (7) == 1:
        acceleration = ((joystick.get_axis (4)+1)*2) 
    elif joystick.get_button (6) == 0:
        acceleration = 0
    
    if joystick.get_button (6) == 1:
        if velocityWheel >= 0.5 or velocityWheel <= -0.5:
            acceleration = -((joystick.get_axis (3)+1)*2)
            
        else:
            acceleration = 0
  
    
    
    if joystick.get_button (0) == 1:
        onePulseCounter += 1

    
    if joystick.get_button (0) == 0 and onePulseCounter >= 1:
        reverseCounter += 1
        onePulseCounter= 0
    
        
    if reverseCounter == 1:
        wagonReverse = True
    if reverseCounter == 2:
        wagonReverse = False
        reverseCounter = 0
    
    if joystick.get_button (9) == 1:
        break
        
    if velocityWheel >= 0:
        velocityWheel -= (velocityWheel*velocityWheel)/200
    if velocityWheel <= 0:
        velocityWheel += (velocityWheel*velocityWheel)/200
    print (timer.deltaT)


pygame.quit()
        