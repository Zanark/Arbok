import pygame   #importing package
pygame.init()   #initialising class
#print (x)

gameDisplay = pygame.display.set_mode((800,600))    #Game screen
pygame.display.set_caption('ARBOK')                 #Game Title

grey_blue = (171, 186, 209)                         #Grey blue color constant
black = (0 , 0 , 0)                                 #Black color constant

gameExit = False                          #Boolean value to determine when to exit the Game

clock = pygame.time.Clock()                         #for fps

lead_x = 300                #x head
lead_y = 300                #y head
lead_x_change = 0           #change in x
lead_y_change = 0           #change in y


while not gameExit:         #game loop
    for event in pygame.event.get():            #fetching events
        if event.type == pygame.QUIT:           #if the cross button is clicked
            gameExit = True                     #exit
        if event.type == pygame.KEYDOWN:        #If any key is pressed
            if event.key == pygame.K_LEFT:      #If LEFT ARROW KEY is pressed
                lead_x_change = -5              #go left by 5 pixels
                lead_y_change = 0               #change in y direction should be zero or else we will have diagonal movement
            elif event.key == pygame.K_RIGHT:   #If RIGHT ARROW KEY is pressed
                lead_x_change = 5               #go right by 5 pixels
                lead_y_change = 0               #---same---
            elif event.key == pygame.K_UP:      #If UP ARROW KEY is pressed
                lead_y_change = -5              #go up by 5 pixels
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:    #If DOWN ARROW KEY is pressed
                lead_y_change = 5               #go down by 5 pixels
                lead_x_change = 0
        '''if event.type == pygame.KEYUP:       #If pressed key has been lifted
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:   #if its the left or right arrow key
                lead_x_change = 0   #zero cahnge in distance
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN: #similarly here
                lead_y_change = 0'''

    lead_x += lead_x_change     #final chnage in x
    lead_y += lead_y_change     #final change in y

    if lead_x >= 790 or lead_x <= 1 or lead_y >= 590 or lead_y <= 1:    #to check if the dot exceeds or touches the boundaries
        gameExit = True

    gameDisplay.fill(grey_blue)     #making the background grey-blue
    pygame.draw.rect(gameDisplay , black , [lead_x , lead_y , 10 , 10])     #Drawing a rectangle
    pygame.display.update()     #updating the screen

    clock.tick(20)  #fps

pygame.quit()   #package quit
