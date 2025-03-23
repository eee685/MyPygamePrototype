import pygame
pygame.init()
from wall_class import wall#import wall class to inherit

class enemy(wall): #inherits methods and attributes from wall class
    def __init__(self, x_position, y_position, width, length, speed):
        #initialise parent wall class
        super().__init__(x_position, y_position, width, length)
        self.__enemy_speed = speed#enemy speed

    def get_rect(self):  #overriding wall class get_rect method, polymorphism
        return pygame.Rect(self.x_position, self.y_position, self.width, self.length)

    def __enemy_move(self, player_instance, walls, pushable_blocks):
        #get direction to move towards player
        #x axis movement
        if player_instance.x_position > self.x_position:#if player x position is more than enemy position (player is right)
            x_move = self.__enemy_speed#set direction to right movement
        else:#else player x position is less than enemy position (player is left)
            x_move = -self.__enemy_speed#set direction of movement to left
            #y axis movement
        if player_instance.y_position > self.y_position:#if player y position is more than enemy position (player is above)
            y_move = self.__enemy_speed#set direction of movement to up
        else:#else player y position is less than enemy position (player is below)
            y_move = -self.__enemy_speed#set direction of movement to down

        #x-axis movement
        self.x_position += x_move
        for sprite in walls + pushable_blocks:#get walls and blocks for collision check
            if self.check_for_collision(sprite):#if collision happens:
                self.x_position -= x_move#undo movement
                break

        #y-axis movement
        self.y_position += y_move
        for sprite in walls + pushable_blocks:#get walls and blocks for collision check
            if self.check_for_collision(sprite):#if collision happens:
                self.y_position -= y_move#undo movement
                break

    def check_for_collision(self, other):#collision function
        return super().check_for_collision(other)#collision detected

    def draw(self, screen, player_instance, walls, pushable_blocks, color=(255, 0, 0)):#draw function for enemy, is red
        self.__enemy_move(player_instance, walls, pushable_blocks)#moves the enemy
        pygame.draw.rect(screen, color, self.get_rect())#draw enemy