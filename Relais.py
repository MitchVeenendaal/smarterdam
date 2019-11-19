'''
Vooruit achteruit
Moeten bepaalde fases worden omgedraaid
'''


import time as tm
import matplotlib.pyplot as plt
import pygame


# Define some colors.
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')


# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


pygame.init()

# Set the width and height of the screen (width, height).
screen = pygame.display.set_mode((500, 700))

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

# Initialize the joysticks.
pygame.joystick.init()

# Get ready to print.
textPrint = TextPrint()

# -------- Main Program Loop -----------
while not done:
    #
    # EVENT PROCESSING STEP
    #
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
    # JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    #
    # DRAWING STEP
    #
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()

    textPrint.tprint(screen, "Number of joysticks: {}".format(joystick_count))
    textPrint.indent()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        textPrint.tprint(screen, "Joystick {}".format(i))
        textPrint.indent()

        # Get the name from the OS for the controller/joystick.
        name = joystick.get_name()
        textPrint.tprint(screen, "Joystick name: {}".format(name))

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        textPrint.tprint(screen, "Number of axes: {}".format(axes))
        textPrint.indent()

        for i in range(axes):
            axis = joystick.get_axis(i)
            textPrint.tprint(screen, "Axis {} value: {:>6.3f}".format(i, axis))
        textPrint.unindent()

        buttons = joystick.get_numbuttons()
        textPrint.tprint(screen, "Number of buttons: {}".format(buttons))
        textPrint.indent()

        for i in range(buttons):
            button = joystick.get_button(i)
            textPrint.tprint(screen,
                             "Button {:>2} value: {}".format(i, button))
        textPrint.unindent()

        hats = joystick.get_numhats()
        textPrint.tprint(screen, "Number of hats: {}".format(hats))
        textPrint.indent()

        # Hat position. All or nothing for direction, not a float like
        # get_axis(). Position is a tuple of int values (x, y).
        for i in range(hats):
            hat = joystick.get_hat(i)
            textPrint.tprint(screen, "Hat {} value: {}".format(i, str(hat)))
        textPrint.unindent()

        textPrint.unindent()
        
    print (joystick.get_axis (4))
        


    #
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    #

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second.
    clock.tick(20)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

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
velocityWheel = -20

deceleration = 10
acceleration = 2

wagonReverse = False
stateRelais = 'backwards'


while True:
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
    
    plt.subplot(2, 1, 1)
    plt.plot(timeData, distanceData, 'b')
    
    plt.subplot(2, 1, 2)
    plt.plot(timeData, velocityData, 'r')
    
    plt.pause (0.00002)
    tm.sleep (0.05)
    

   
        