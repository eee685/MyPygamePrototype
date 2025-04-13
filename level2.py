import pygame
pygame.init() #import and initialise pygame

screen = pygame.display.set_mode((800, 500))  #screen size, width, height
pygame.display.set_caption("Level 2")    #what the game window is called

#import wall class
from wall_class import wall

#import player class
from player_class import player

#import pushable class
from pushable_block_class import pushable

#import enemy class
from enemy_class import enemy

#import endpoint class
from endpoint_class import endpoint

#import main running loop
from main_loop import main_loop

#create list of enemies
enemies = [
    enemy(700, 250, 50, 50, 3)  #enemy 1, x_position, y_position, width, length, speed
]

endpoints = [
    endpoint(440, 440, 50, 50)  #level endpoint for player to reach, x_position, y_position, width, length
]

#create wall objects and store in list
walls = [
    #wall(400, 200, 100, 50),  #test wall; x_axis, y_axis, length, width
    wall(0, 0, 800, 10),  #top border wall
    wall(0, 0, 10, 800),  #left border wall
    wall(790, 0, 10, 800),  #right border wall
    wall(0, 490, 800, 10),  #right border wall
    wall(60, 0, 10, 440), 
    wall(120, 60, 10, 200), 
    wall(120, 320, 10, 200), 
    wall(120, 320, 200, 10), 
    wall(200, 380, 300, 10), 
    wall(180, 0, 10, 200), 
    wall(240, 60, 10, 200), 
    wall(310, 90, 10, 200), 
    wall(380, 0, 10, 200), 
    wall(380, 60, 10, 200), 
]

#list of pushable blocks
pushable_blocks = [
#    pushable(100, 100, 100, 100, 1),  #test block 1; x_axis, y_axis, length, width, speed
 #   pushable(200, 200, 50, 50, 1),  #test block 2
  #  pushable(35, 520, 10, 10, 1),   #test block 3
]

#create player object
player_instance = player(10, 10, 50, 50, 5)  #x_position, y_position, width, length, speed

#to control framerate
clock = pygame.time.Clock()

main_loop(screen, clock, player_instance, walls, pushable_blocks, enemies, endpoints)