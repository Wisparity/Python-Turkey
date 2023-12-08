import pygame
   

pygame.init()
pygame.display.set_caption("Turkey")
screen = pygame.display.set_mode((1000,1000))

BROWN = (110,70,0)
CINNAMON = (99,42,13)
PURPLE = (100,10,40)
MAGENTA = (100,10,100)
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW =(255,255,50)
while(1):
    #render section
    screen.fill((0,0,0)) #wipe screen black
    pygame.draw.rect(screen,(YELLOW), (420,700,30,200))
    pygame.draw.rect(screen,(YELLOW), (550,700,30,200))
    pygame.draw.circle(screen, (MAGENTA), (500,200),100)
    pygame.draw.circle(screen, (MAGENTA), (750,300),100)
    pygame.draw.circle(screen, (MAGENTA), (250,300),100)
    pygame.draw.circle(screen, (MAGENTA), (225,550),100)
    pygame.draw.circle(screen, (MAGENTA), (625,500),100)
    pygame.draw.circle(screen, (PURPLE), (650,250),100)
    pygame.draw.circle(screen, (PURPLE), (250,400),100)
    pygame.draw.circle(screen, (PURPLE), (350,250),100)
    pygame.draw.circle(screen, (BROWN),(500, 500),250)
    pygame.draw.ellipse(screen,(CINNAMON),(400,150,200,300))  
    pygame.draw.circle(screen, (WHITE), (550,250),35)
    pygame.draw.circle(screen, (BLACK), (550,250),15)
    pygame.draw.circle(screen, (WHITE), (450,250),35)
    pygame.draw.circle(screen, (BLACK), (450,250),15)
    pygame.draw.polygon(screen,(YELLOW),((475,350),(550,350),(450,300)))

    pygame.display.flip() #draws ALL the shapes at once to the screen
    
    
                       
            
    
