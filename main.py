import pygame
pygame.init() #import and initialise pygame

screen = pygame.display.set_mode((800, 800))  #screen size, width, height
pygame.display.set_caption("Maze game")    #what the game window is called

#import wall class
from wall_class import wall

#create wall objects
walls = [
    wall(400, 200, 100, 50)  #test wall; x_axis, y_axis, length, width
]

#to control framerate
clock = pygame.time.Clock()

#main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #set running to false when quitting, stopps while running loop
            running = False

    screen.fill((200, 255, 200))  #make the screen RGB COLOUR, is green for now
    pygame.display.flip()   #update display

    for w in walls:
        w.draw(screen)  #draw walls

    #update display
    pygame.display.flip()

    clock.tick(60)  #limit frame rate to 60 fps
pygame.quit()  #quit pygame
