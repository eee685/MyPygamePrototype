import pygame
pygame.init()
from wall_class import wall

#define pushable class, inherits from wall class
class pushable(wall):
    def __init__(self, x_position, y_position, width, length, speed):
        #initialize parent wall class
        super().__init__(x_position, y_position, width, length)
        self.is_pushed = False  #block isnt pushed yet, is set to false until it is pushed
        self.__block_speed = speed  #block speed

    def get_rect(self):#overriding the wall class' get_rect method, polymorphism
        try:
            return pygame.Rect(self.x_position, self.y_position, self.width, self.length)
        except AttributeError as e: #if get_rect method is missing or any of the attributes are missing, print an error "e"
            print(f"error in get_rect, reason: {e}")
            return None

    def push(self, direction, sprites):#block pushing method
        #to see if block has really been pushed
        #print("block has been pushed, push method works")
        #print(f"block position before push: {self.x_position}, {self.y_position}")
        x_move, y_move = direction
        # direction, x_move and y_move is change in block position, e.g. x_move=1, then it moves by block_speed amount of pixels one time, negative is reverse direction
        self.is_pushed = False#reset pushed boolean
        
        #save original position
        original_x = self.x_position
        original_y = self.y_position
        #temporarily move block, block_speed amount of pixels moved by x_move or y_move amount
        #block position after push for debugging
        #print(f"block position after push and before collision check: {self.x_position}, {self.y_position}")
        
        #check for collisions with sprites
        collision = False
        for sprite in sprites:
            if self.check_for_collision(sprite):
                print(f"Collision detected with {sprite}")
                #change position after collision
                self.x_position += x_move * self.__block_speed
                self.y_position += y_move * self.__block_speed
                print(f"This is x_position: {self.x_position}")
                print(f"This is y_position: {self.y_position}")
                #exit the loop on first collision
        #if no collisions happened, block was successfully pushed
        if not collision:
            self.is_pushed = True
        if not isinstance(direction, (tuple, list)) or len(direction) != 2: #check if direction is 2 elements (x axis and y axis)
            raise ValueError("direction must be a tuple or list with two elements (x-axis, y-axis)")
        if not isinstance(sprites, list): #checks if sprites list exists, if not then print an error
            raise ValueError("sprites must be a list")
        #for debigging
        #print(f"block position after push and after collision check): {self.x_position}, {self.y_position}")
        #print(f"Block speed: {self.__block_speed}")#to see if block speed is changing from 0
        #print(f"Sprites: {sprites}")#to see if it is loading sprites to collides


    def check_for_collision(self, other):
        try:
        #call parent collision detection
            return super().check_for_collision(other)
        except Exception as e:
            #handle unexpected errors during collision detection, if there is an error, print error "e"
            print(f"error in check_for_collision, reason: {e}")
            return False #to indicate that the method failed

    def draw(self, screen, color=(0, 0, 255)):
        #draw block on screen
        #print(f"block position: {self.x_position}, {self.y_position}") #to see if the block is drawn properly after moving position 
        pygame.draw.rect(screen, color, pygame.Rect(self.x_position, self.y_position, self.width, self.length))
