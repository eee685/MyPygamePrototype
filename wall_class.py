import pygame
pygame.init() #import and initialise pygame

class wall:
    def __init__(self, x_position, y_position, width, length):
        #initialize the wall's position and size
        self.x_position = x_position  #x-axis position
        self.y_position = y_position  #y-axis position
        self.width = width            #wall width
        self.length = length          #wall length

    def get_rect(self):
        # Calculate the wall's rectangle representation
        return pygame.Rect(self.x_position, self.y_position, self.width, self.length)

    def draw(self, screen):
        #draw the wall
        rectangle = self.get_rect()  #get the wall's rectangle
        pygame.draw.rect(screen, (20, 20, 20), rectangle)  #draw wall with color (RGB) and shape

    def check_for_collision(self, other):
        # Check for collision with another object
        return self.get_rect().colliderect(other.get_rect())