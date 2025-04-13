import pygame
pygame.init() #import and initialise pygame

def main_loop(screen, clock, player_instance, walls, pushable_blocks, enemies, endpoints):

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
            try:
                sprites = [player_instance] + walls + [b for b in pushable_blocks if b != block]
                if block.check_for_collision(player_instance):
                    block.push(direction, sprites=sprites)
                block.draw(screen)
            except AttributeError as e: #check if method or attribute is missing, if so, print the reason for the error
                print(f"error with block collisions or drawing the sprite, reason: {e}")

            #ENEMY STUFF
        for enemy_instance in enemies:
            enemy_instance.draw(screen, player_instance, walls, pushable_blocks)  #move and draw enemy
            #check for collision with player sprite, if colliding with player then:
            if enemy_instance.check_for_collision(player_instance):
                print("YOU LOSE")#need to add code to send player back to menu
                running = False  # Exit the game loop
            
            #ENDPOINT STUFF
        for endpoint_sprite in endpoints:
            endpoint_sprite.draw(screen)#draw walls
            if endpoint_sprite.check_for_collision(player_instance):#calls the collision function
                print("YOU WON")#need to add code to send player back to menu
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
