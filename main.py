import pygame
pygame.init()
#print (x)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('ARBOK')

grey_blue = (171, 186, 209)
black = (0 , 0 , 0)

gameExit = False

clock = pygame.time.Clock()

lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0


while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -5
            if event.key == pygame.K_RIGHT:
                lead_x_change = 5
            if event.key == pygame.K_UP:
                lead_y_change = -5
            if event.key == pygame.K_DOWN:
                lead_y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                lead_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                lead_y_change = 0
        
        #print(event)
    lead_x += lead_x_change
    lead_y += lead_y_change

    gameDisplay.fill(grey_blue)
    pygame.draw.rect(gameDisplay , black , [lead_x , lead_y , 10 , 10])
    pygame.display.update()

    clock.tick(10)

pygame.quit()
