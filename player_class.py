#import wall class from wall_class.py
from wall_class import wall
#import pygame
import pygame

class player(wall): #inherit from wall
    def __init__(self, speed, x_position, y_position, width, length):
        super().__init__(x_position, y_position, width, length)#attributes for sprite inherited from wall class, initialised
        self.__PlayerSpeed = speed  #private attribute for player speed, used by player class only

    def move(self, keys):
        #arrow key inputs change player speed
        if keys[pygame.K_UP]:
            self.y_position -= self.__PlayerSpeed#up
        if keys[pygame.K_DOWN]:
            self.y_position += self.__PlayerSpeed#down
        if keys[pygame.K_LEFT]:
            self.x_position -= self.__PlayerSpeed#left
        if keys[pygame.K_RIGHT]:
            self.x_position += self.__PlayerSpeed#right

    def draw(self, screen):
        #draw player
        rectangle = self.get_rect()
        pygame.draw.rect(screen, (0, 0, 0), rectangle) #screen. rgb colour, shape
