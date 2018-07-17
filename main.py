import pygame   #importing package pygame
import time     #importing package time

pygame.init()   #initialising class
#print (x)

display_width = 800     #width of the screen
display_height = 600    #height of the screen
fps  = 25               #fps

gameDisplay = pygame.display.set_mode((display_width,display_height))    #Game screen
pygame.display.set_caption('ARBOK')                 #Game Title

grey_blue = (171, 186, 209)                         #Grey blue color constant
black = (0 , 0 , 0)                                 #Black color constant
red = (255 , 0 , 0)                                 #Red color constant

clock = pygame.time.Clock()                         #for fps

font = pygame.font.SysFont(None , 40)  #setting font for display message

def msg_display(text , color):          #function to display the passed on text on the screen
    message = font.render(text , True , color)
    gameDisplay.blit(message, [display_width/2 , display_height/2 - 10])

def GameLoop():

    gameExit = False                        #Boolean value to determine when to exit the Game
    lead_x = display_width/2                #x head
    lead_y = display_height/2               #y head
    lead_x_change = 0                       #change in x
    lead_y_change = 0                       #change in y
    snake_width = 10                        #snakes width
    crawl_size = 5                          #crawl distance in each step

    while not gameExit:         #game loop
        for event in pygame.event.get():            #fetching events
            if event.type == pygame.QUIT:           #if the cross button is clicked
                gameExit = True                     #exit
            if event.type == pygame.KEYDOWN:        #If any key is pressed
                if event.key == pygame.K_LEFT:      #If LEFT ARROW KEY is pressed
                    lead_x_change = -crawl_size     #go left by 5 pixels
                    lead_y_change = 0               #change in y direction should be zero or else we will have diagonal movement
                elif event.key == pygame.K_RIGHT:   #If RIGHT ARROW KEY is pressed
                    lead_x_change = crawl_size               #go right by 5 pixels
                    lead_y_change = 0               #---same---
                elif event.key == pygame.K_UP:      #If UP ARROW KEY is pressed
                    lead_y_change = -crawl_size     #go up by 5 pixels
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:    #If DOWN ARROW KEY is pressed
                    lead_y_change = crawl_size      #go down by 5 pixels
                    lead_x_change = 0
            '''if event.type == pygame.KEYUP:       #If pressed key has been lifted
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:   #if its the left or right arrow key
                    lead_x_change = 0   #zero cahnge in distance
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN: #similarly here
                    lead_y_change = 0'''

        lead_x += lead_x_change     #final chnage in x
        lead_y += lead_y_change     #final change in y

        if lead_x >= display_width - 10 or lead_x <= 2 or lead_y >= display_height - 10 or lead_y <= 2:    #to check if the dot exceeds or touches the boundaries
            gameExit = True

        gameDisplay.fill(grey_blue)     #making the background grey-blue
        pygame.draw.rect(gameDisplay , black , [lead_x , lead_y , snake_width , snake_width])     #Drawing a rectangle
        pygame.display.update()     #updating the screen

        clock.tick(fps)  #fps

    msg_display("Yo loose MOFO!" , red)     #GAME OVER message
    pygame.display.update()                 #updating screen
    time.sleep(1)                           #to pause the screen to show text
    pygame.quit()   #package quit

GameLoop()