import pygame
pygame.init()
from wall_class import wall

# Define the Player class, which inherits from the wall class
class player(wall):
    def __init__(self, x_position, y_position, width, length, speed):
        # Initialize parent wall class
        super().__init__(x_position, y_position, width, length)
        self.__playerspeed = speed  # Player speed, pixels per frame

    def __player_move(self):
        # Handle player movement based on user input
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.y_position -= self.__playerspeed
        elif keys[pygame.K_DOWN]:
            self.y_position += self.__playerspeed
        elif keys[pygame.K_LEFT]:
            self.x_position -= self.__playerspeed
        elif keys[pygame.K_RIGHT]:
            self.x_position += self.__playerspeed
#       else:
#            print("Error: Arrow key input went wrong")  # For unexpected cases

    def check_for_collision(self, other):
        # Call parent collision detection
        return super().check_for_collision(other)

    def draw(self, screen, color=(255, 255, 255)):
        # Update player position and draw on the screen
        self.__player_move()  # Move the player
        pygame.draw.rect(screen, color, pygame.Rect(self.x_position, self.y_position, self.width, self.length))
