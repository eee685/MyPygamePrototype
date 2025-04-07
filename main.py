import pygame
pygame.init() #import and initialise pygame

screen = pygame.display.set_mode((800, 800))  #screen size, width, height
pygame.display.set_caption("Maze game")    #what the game window is called

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

#create list of enemies
enemies = [
    enemy(700, 700, 40, 40, 3)  #enemy 1, x_position, y_position, width, length, speed
]

endpoints = [
    endpoint(700, 700, 40, 40)  #level endpoint for player to reach, x_position, y_position, width, length
]

#create wall objects and store in list
walls = [
    wall(400, 200, 100, 50),  #test wall; x_axis, y_axis, length, width
    wall(0, 0, 800, 10),  #top border wall
    wall(0, 0, 10, 800),  #left border wall
    wall(790, 0, 10, 800),  #right border wall
    wall(0, 790, 800, 10),  #right border wall
    wall(35, 0, 10, 500), 
    wall(70, 35, 10, 500), 
]

#list of pushable blocks
pushable_blocks = [
    pushable(100, 100, 100, 100, 1),  #test block 1; x_axis, y_axis, length, width, speed
    pushable(200, 200, 50, 50, 1),  #test block 2
    pushable(35, 520, 10, 10, 1),   #test block 3
]

#create player object
player_instance = player(10, 10, 25, 25, 5)  #x_position, y_position, width, length, speed

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

    #PLAYER SPRITE STUFF
    #bring walls list to player_class when drawing the player
    player_instance.draw(screen, walls=walls)

    for w in walls:
        w.draw(screen)#draw walls
        if w.check_for_collision(player_instance):#calls the collision function
            #print("Collision detected")#will only print when overlapping, but shouldn't overlap, so if printing then error
            player_instance.__playerspeed = 0 
        else:
            #print("no collision")
            pass

    #STUFF FOR THE PUSHABLE BLOCKS
    #checks for keys getting pressed
    keys = pygame.key.get_pressed()
    #direction = (0, 0)  #default direction of block
    if keys[pygame.K_UP]:
        direction = (0, -1) #moving up towards 0
    elif keys[pygame.K_DOWN]:
        direction = (0, 1) #moving down towards max number
    elif keys[pygame.K_LEFT]:
        direction = (-1, 0) #moving left towards 0
    elif keys[pygame.K_RIGHT]:
        direction = (1, 0) #moving right towards max number
    #else:
    #   print("keyboard not working") #will continually print the message as long as arrow keys arent pressed

    #collisions and movement for pushable blocks
    for block in pushable_blocks:
        #gets the list of blocks, then excludes the block so the original block doesn't collide with itself
        #create the sprites list: player + walls + all other blocks (excluding the current block)
        sprites = [player_instance] + walls + [b for b in pushable_blocks if b != block]
        if block.check_for_collision(player_instance):  #if player collides with block
            print("got block collision")
            print(f"Direction: {direction}")
            
            block.push(direction, sprites=sprites)
        block.draw(screen)#draw blocks
        #print(f"sprites: {sprites}")#list of sprites that are drawn/existing

        #ENEMY STUFF
    for enemy_instance in enemies:
        enemy_instance.draw(screen, player_instance, walls, pushable_blocks)  #move and draw enemy
        #check for collision with player sprite, if colliding with player then:
        if enemy_instance.check_for_collision(player_instance):
            print("game over")#need to add code to send player back to menu
            running = False  # Exit the game loop
            
        #ENDPOINT STUFF
    for endpoint_sprite in endpoints:
        endpoint_sprite.draw(screen)#draw walls
        if endpoint_sprite.check_for_collision(player_instance):#calls the collision function
            print("you win")#need to add code to send player back to menu
            running = False  # Exit the game loop
        else:
            #print("no collision")
            pass
    #for debugging
    #print(f"Player position: {player_instance.x_position}, {player_instance.y_position}")
    #print(f"Block position after: {block.x_position}, {block.y_position}")
    #print(f"Direction: {direction}")
    
    #update display
    pygame.display.flip()

    clock.tick(60)  #limit frame rate to 60 fps
pygame.quit()  #quit pygame

