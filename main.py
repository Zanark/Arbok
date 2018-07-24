import pygame   #importing package pygame
import time     #importing package time
import random   #importing package random

pygame.init()   #initialising class
#print (x)

#pygame.mixer.music.load("pallet_town.mp3") 
#pygame.mixer.music.play(-1,0.0)

snake_img_head = pygame.image.load('snake-head.png')
snake_img_body = pygame.image.load('snake_body.png')
snake_img_tail = pygame.image.load('snake_tail.png')
food_img = pygame.image.load('food.png')

display_width = 800     #width of the screen
display_height = 600    #height of the screen
fps  = 20               #fps

gameDisplay = pygame.display.set_mode((display_width,display_height))    #Game screen
pygame.display.set_caption('ARBOK')                 #Game Title

grey_blue = (171, 186, 209)                         #Grey blue color constant
black = (0 , 0 , 0)                                 #Black color constant
red = (255 , 0 , 0)                                 #Red color constant
white = (255 , 255 , 255)                           #White color constant
yellow = (249, 151, 48)
snake_green = (106,158,104)
direction = "none"

clock = pygame.time.Clock()                         #for fps

font = pygame.font.Font('Digital_tech.otf' , 30 )  #setting font for display message

def text_objects(message , color):
    textSurface = font.render(message , True , color)
    return textSurface , textSurface.get_rect()

def msg_display(text , color):          #function to display the passed on text on the screen
    textSurface , textRect = text_objects(text,color)
    textRect.center = (display_width/2) , (display_height/2)
    gameDisplay.blit(textSurface , textRect)
    #message = font.render(text , True , color)
    #gameDisplay.blit(message, [30 , display_height/2 - 10])

def snake(snake_width , snake_list, snake_length , direction , body_directions):

    if(direction == "right"):
        head = pygame.transform.rotate(snake_img_head , 270)
    elif(direction == "left"):
        head = pygame.transform.rotate(snake_img_head , 90)
    elif(direction == "up"):
        head = pygame.transform.rotate(snake_img_head , 0)
    elif(direction == "down"):
        head = pygame.transform.rotate(snake_img_head , 180)
    elif(direction == "none"):
        head = pygame.transform.rotate(snake_img_head , 0)

    gameDisplay.blit(head , (snake_list[-1][0] , snake_list[-1][1]))

    for point in snake_list[:-1]:

        for direc in body_directions[:-1]:
            if(direc == "right"):
                body = pygame.transform.rotate(snake_img_body , 270)
                tail = pygame.transform.rotate(snake_img_tail , 270)
            elif(direc == "left"):
                body = pygame.transform.rotate(snake_img_body , 90)
                tail = pygame.transform.rotate(snake_img_tail , 90)
            elif(direc == "up"):
                body = pygame.transform.rotate(snake_img_body , 0)
                tail = pygame.transform.rotate(snake_img_tail , 0)
            elif(direc == "down"):
                body = pygame.transform.rotate(snake_img_body , 180)
                tail = pygame.transform.rotate(snake_img_tail , 180)
            elif(direc == "none"):
                body = pygame.transform.rotate(snake_img_body , 0)
                tail = pygame.transform.rotate(snake_img_tail , 0)

        if(snake_list.index(point) == 0):
            gameDisplay.blit(tail , (point[0] , point[1]))
        else:
            gameDisplay.blit(body ,  (point[0] , point[1])) #Arbok
        #print(str(snake_list.index(point)))



def snake_food(food_x , food_y , food_width):
    gameDisplay.blit(food_img , (food_x , food_y)) #Food



def GameLoop():

    global direction                        #Direction variable
    gameExit = False                        #Boolean value to determine when to exit the Game
    gameOver = False                        #Boolean value for the game over screen display
    lead_x = display_width/2                #x head
    lead_y = display_height/2               #y head
    lead_x_change = 0                       #change in x
    lead_y_change = 0                       #change in y
    snake_width = 20                        #snake's width
    food_width = 30                         #food's width
    crawl_size = 20                          #crawl distance in each step
    food_x = round(random.randrange(30 , display_width-30))#/10.00)*10.00    #random coordinates for food location
    food_y = round(random.randrange(30 , display_height-30))#/10.00)*10.00
    snake_list = []
    snake_length = 1
    snake_body_directions = ['none']

    while not gameExit:         #game loop

        while gameOver == True:
            gameDisplay.fill(red)
            msg_display("GAME OVER MOFO!! Press R to Replay or Q to Quit" , white)
            pygame.display.update()     #updating the screen

            for event in pygame.event.get():
                if event.type == pygame.QUIT:           #if the cross button is clicked
                    gameOver = False
                    gameExit = True                     #exit
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
                if event.key == pygame.K_LEFT and direction != 'right':      #If LEFT ARROW KEY is pressed
                    lead_x_change = -crawl_size     #go left by 5 pixels
                    lead_y_change = 0               #change in y direction should be zero or else we will have diagonal movement
                    direction = 'left'              #rotating head of the snake
                elif event.key == pygame.K_RIGHT and direction != 'left':   #If RIGHT ARROW KEY is pressed
                    lead_x_change = crawl_size               #go right by 5 pixels
                    lead_y_change = 0               #---same---
                    direction = 'right'
                elif event.key == pygame.K_UP and direction != 'down':      #If UP ARROW KEY is pressed
                    lead_y_change = -crawl_size     #go up by 5 pixels
                    lead_x_change = 0
                    direction = 'up'
                elif event.key == pygame.K_DOWN and direction != 'up':    #If DOWN ARROW KEY is pressed
                    lead_y_change = crawl_size      #go down by 5 pixels
                    lead_x_change = 0
                    direction = 'down'

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
        snake_body_directions.append(direction)
                
        gameDisplay.fill(grey_blue)                     #making the background grey-blue
        #msg_display(str(food_x)+" , "+str(food_y) , black)
        snake_food(food_x , food_y , food_width)        #food drwaing function

        if(len(snake_list)>snake_length):
            del snake_list[0]
            del snake_body_directions[0]

        for body_part in snake_list[:-1]:
            if(body_part == snake_head):
                print("snake_head>>" + str(snake_head) + "\tbody part>>" + str(body_part))
                gameOver = True

        snake(snake_width , snake_list , snake_length , direction , snake_body_directions)            #snake drawing function
        pygame.display.update()                         #updating the screen

        '''if lead_x >= food_x and lead_x <= food_x + food_width:
                if lead_y >= food_y and lead_y <= food_y + food_width:
                    food_x = round(random.randrange(30 , display_width-30))#/10.00)*10.00    #random coordinates for food location
                    food_y = round(random.randrange(30 , display_height-30))#/10.00)*10.00
                    #snake_list.append([lead_x_change , lead_y_change])  
                    snake_length += 1'''

        if lead_x > food_x and lead_x < food_x + food_width or lead_x + snake_width > food_x and lead_x + snake_width < food_x + food_width:
            if lead_y > food_y and lead_y < food_y + food_width or lead_y + snake_width > food_y and lead_y + snake_width < food_y + food_width:
                food_x = round(random.randrange(30 , display_width-30))#/10.00)*10.00    #random coordinates for food location
                food_y = round(random.randrange(30 , display_height-30))#/10.00)*10.00
                #snake_list.append([lead_x_change , lead_y_change])  
                snake_length += 1

        


        clock.tick(fps)  #fps


    pygame.quit()   #package quit

GameLoop()