import pygame
pygame.init() #import and initialise pygame

screen = pygame.display.set_mode((800, 800))  #screen size, width, height
pygame.display.set_caption("Maze game")    #what the game window is called

#import wall class
from wall_class import wall

#import player class
from player_class import player

#create wall objects and store in list
walls = [
    wall(400, 200, 100, 50)  #test wall; x_axis, y_axis, length, width
]

#create player object
player_instance = player(50, 50, 40, 40, 5)  #x_position, y_position, width, length, speed

#to control framerate
clock = pygame.time.Clock()

#main loop
running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:#set running to false when quitting, stops the while loop
            running = False

    pygame.display.flip() #update screen

    screen.fill((200, 255, 200))  #make the screen RGB COLOUR, is green for now, is in main loop to make screen keep reloading to stop the player from leaving a trail on the screen

    #bring walls list to player_class when drawing the player
    player_instance.draw(screen, walls=walls)

    for w in walls:
        w.draw(screen)#draw walls
        if w.check_for_collision(player_instance):#calls the collision function
            print("Collision detected")#will only print when overlapping, but shouldn't overlap, so if printing then error
            player_instance.__playerspeed = 0 
        else:
            print("no collision")

    #update display
    pygame.display.flip()

    clock.tick(60)  #limit frame rate to 60 fps
pygame.quit()  #quit pygame

