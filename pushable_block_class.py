import pygame
pygame.init()
from wall_class import wall

#define player class, inherits from wall class
class pushable(wall):
    def __init__(self, x_position, y_position, width, length, speed):
        #initialize parent wall class
        super().__init__(x_position, y_position, width, length)
        self.is_pushed = False  #block isnt pushed yet, is set to false until it is pushed
        self.__block_speed = speed  #block speed

    def get_rect(self):#overriding the wall class' get_rect method, polymorphism
        return pygame.Rect(self.x_position, self.y_position, self.width, self.length)

    def push(self, direction, sprites):#block pushing method
        #to see if block has really been pushed
        print("block has been pushed")
        x_move, y_move = direction
        # direction, x_move and y_move is change in block position, e.g. x_move=1, then it moves by block_speed amount of pixels one time, negative is reverse direction
        self.is_pushed = False#reset pushed boolean

        #temporarily move block, block_speed amount of pixels moved by x_move or y_move amount
        self.x_position += x_move * self.__block_speed
        self.y_position += y_move * self.__block_speed

        #check for collisions with sprites
        #x-axis movement
        for sprite in sprites:
            if self.check_for_collision(sprite):
                #revert x-axis movement if collision occurs
                self.x_position -= x_move * self.__block_speed
                break
        #y-axis movement
        for sprite in sprites:
            if self.check_for_collision(sprite):
                #revert y-axis movement if collision occurs
                self.y_position -= y_move * self.__block_speed
                break
        #if no collisions happened, block was successfully pushed
        else:
            self.is_pushed = True
        #for debigging
        print(f"Block speed: {self.__block_speed}")#to see if block speed is changing from 0
        print(f"Sprites: {sprites}")#to see if it is loading sprites to collides


    def check_for_collision(self, other):
        #call parent collision detection
        return super().check_for_collision(other)

    def draw(self, screen, color=(0, 0, 255)):
        #draw block on screen
        pygame.draw.rect(screen, color, pygame.Rect(self.x_position, self.y_position, self.width, self.length))
