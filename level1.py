import pygame
pygame.init() #import and initialise pygame

screen = pygame.display.set_mode((800, 800))  #screen size, width, height
pygame.display.set_caption("Maze game")    #what the game window is called

#import wall class
from wall_class import wall

#import player class
from player_class import player

#create wall objects
walls = [
    wall(400, 200, 100, 50)  #test wall; x_axis, y_axis, length, width
]

# Create player object
player_instance = player(5, 50, 50, 40, 40)  #speed, x_position, y_position, width, length

#to control framerate
clock = pygame.time.Clock()

screen.fill((200, 255, 200))  #make the screen RGB COLOUR, is green for now
#main loop
running = True
while running:
    for event in pygame.event.get():
        #get pressed keys for player movement
        keys = pygame.key.get_pressed()
        player_instance.move(keys)#move player based on keys

        if event.type == pygame.QUIT:#set running to false when quitting, stops the while loop
            running = False

    pygame.display.flip()#update display

    for w in walls:
        w.draw(screen)#draw walls
        #draw player
        player_instance.draw(screen)

    #update display
    pygame.display.flip()

    clock.tick(60)  #limit frame rate to 60 fps
pygame.quit()  #quit pygame
