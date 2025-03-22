import pygame
pygame.init()
from wall_class import wall

#define player class, inherits from wall class
class player(wall):
    def __init__(self, x_position, y_position, width, length, speed):
        #initialize parent wall class
        super().__init__(x_position, y_position, width, length)
        self.__playerspeed = speed  #player speed, pixels per frame

    def get_rect(self):#overriding the wall class' get_rect method, polymorphism
        return pygame.Rect(self.x_position, self.y_position, self.width, self.length)

    def __player_move(self, walls):
        #handle player movement based on user input, detects keyboard being pressed
        keys = pygame.key.get_pressed()

        #position is that top left of the screen = 0, and increases as going up or right
        #x position move is 0 until key is pressed
        x_move=0
        #y position move is 0 until key is pressed
        y_move=0
        #when up key is pressed, negative vertical player speed
        if keys[pygame.K_UP]:
            y_move = -self.__playerspeed
        #when down key is pressed, positive vertical player speed
        elif keys[pygame.K_DOWN]:
            y_move = self.__playerspeed
        #when left key is pressed, negative horizontal player speed
        if keys[pygame.K_LEFT]:
            x_move = -self.__playerspeed
        #when right key is pressed, positive horizontal player speed
        if keys[pygame.K_RIGHT]:
            x_move = self.__playerspeed
#       else:
#            print("Error: Arrow key input went wrong")  #for unexpected cases
        #temporarily move player by player speed (in x_move and y_move)
        self.x_position += x_move
        self.y_position += y_move
        for wall in walls:
                if wall.check_for_collision(self):  #if collision detected, do this:
                    self.x_position -= x_move  #undo horizontal movement
                    self.y_position -= y_move  #undo vertical movement
                    break  #exit for loop once a collision is detected



    def check_for_collision(self, other):
        #call parent collision detection
        return super().check_for_collision(other)

    def draw(self, screen, walls, color=(255, 255, 255)):
        #update player position and draw on the screen
        self.__player_move(walls)  #moves the player and also bring the walls list from main loop to player_class, lets class check for collisions
        pygame.draw.rect(screen, color, pygame.Rect(self.x_position, self.y_position, self.width, self.length))
