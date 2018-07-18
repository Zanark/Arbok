import pygame   #importing package pygame
import time     #importing package time
import random   #importing package random

pygame.init()   #initialising class
#print (x)

display_width = 800     #width of the screen
display_height = 600    #height of the screen
fps  = 35               #fps

gameDisplay = pygame.display.set_mode((display_width,display_height))    #Game screen
pygame.display.set_caption('ARBOK')                 #Game Title

grey_blue = (171, 186, 209)                         #Grey blue color constant
black = (0 , 0 , 0)                                 #Black color constant
red = (255 , 0 , 0)                                 #Red color constant
white = (255 , 255 , 255)                           #White color constant
yellow = (249, 151, 48)

clock = pygame.time.Clock()                         #for fps

font = pygame.font.SysFont(None , 40)  #setting font for display message

def msg_display(text , color):          #function to display the passed on text on the screen
    message = font.render(text , True , color)
    gameDisplay.blit(message, [30 , display_height/2 - 10])

def snake(snake_width , snake_list, snake_length):
    for point in snake_list:
        if(snake_list.index(point) == snake_length-1):
            b_color = yellow
        else:
            b_color = black
        pygame.draw.rect(gameDisplay , b_color , [point[0] , point[1] , snake_width , snake_width]) #Arbok
        #print(str(snake_list.index(point)))

def snake_food(food_x , food_y , food_width):
    pygame.draw.rect(gameDisplay , red , [food_x , food_y , food_width , food_width]) #Food



def GameLoop():

    gameExit = False                        #Boolean value to determine when to exit the Game
    gameOver = False                        #Boolean value for the game over screen display
    lead_x = display_width/2                #x head
    lead_y = display_height/2               #y head
    lead_x_change = 0                       #change in x
    lead_y_change = 0                       #change in y
    snake_width = 10                        #snake's width
    food_width = 20                         #food's width
    crawl_size = 10                          #crawl distance in each step
    food_x = round(random.randrange(30 , display_width-30)/10.00)*10.00    #random coordinates for food location
    food_y = round(random.randrange(30 , display_height-30)/10.00)*10.00
    snake_list = []
    snake_length = 1

    while not gameExit:         #game loop

        while gameOver == True:
            gameDisplay.fill(red)
            msg_display("GAME OVER MOFO!! Press R to Replay or Q to Quit" , white)
            pygame.display.update()     #updating the screen

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_r:
                        GameLoop()

        '''if gameExit == True:
            break'''

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
            gameOver = True

        #snake_list = []
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
                
        gameDisplay.fill(grey_blue)                     #making the background grey-blue
        #msg_display(str(food_x)+" , "+str(food_y) , black)
        snake_food(food_x , food_y , food_width)        #food drwaing function

        if(len(snake_list)>snake_length):
            del snake_list[0]

        for body_part in snake_list[:-1]:
            if(body_part == snake_head):
                print("snake_head>>" + str(snake_head) + "\tbody part>>" + str(body_part))
                gameOver = True

        snake(snake_width , snake_list , snake_length)            #snake drawing function
        pygame.display.update()                         #updating the screen

        if lead_x >= food_x and lead_x <= food_x + food_width:
            if lead_y >= food_y and lead_y <= food_y + food_width:
                food_x = round(random.randrange(30 , display_width-30)/10.00)*10.00    #random coordinates for food location
                food_y = round(random.randrange(30 , display_height-30)/10.00)*10.00
                #snake_list.append([lead_x_change , lead_y_change])  
                snake_length += 1

        clock.tick(fps)  #fps


    pygame.quit()   #package quit

GameLoop()