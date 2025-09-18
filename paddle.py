import pygame

class Paddle:
    def __init__(self, surface, color, rect, width):
        starting_pos_x = 640
        starting_pos_y = 360
        self.surface = surface
        self.color = color
        self.rect = rect
        self.width = width



    def create_paddle(self):
        pygame.draw.rect(self.surface, self.color, self.rect, self.width)


    def move_paddle(self):
        pass