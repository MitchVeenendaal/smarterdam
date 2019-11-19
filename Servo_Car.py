import RPi.GPIO as GPIO
import time as tm

GPIO.setmode (GPIO.BOARD)

GPIO.setup (7,GPIO.OUT)

onePulseCounter = 0
brakeCounter = 0

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
    
    if joystick.get_button (0) == 1:
        onePulseCounter += 1

    
    if joystick.get_button (0) == 0 and onePulseCounter >= 1:
        brakeCounter += 1
        onePulseCounter= 0
        
    if brakeCounter == 1:
        brakeActivation = 0.0001
    if brakeCounter == 2:
        brakeActivation = 0.002
        brakeCounter = 0
    
    GPIO.output (7,1)
    time.sleep (brakeActivation)

    GPIO output (7,0)
    
    time.sleep (0.1)