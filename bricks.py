import pygame




class Bricks:

    def __init__(self, screenwidth):
        self.brick_list = []
        self.screen_width = screenwidth
        self.brick_width = 80
        self.no_of_brick = self.screen_width/self.brick_width



    def create_rect(self):
        x = 0
        y = 0
        for times in range(int(self.no_of_brick)):
            rect = pygame.Rect((x, y), (self.brick_width, 30))
            self.brick_list.append(rect)
            x += self.brick_width + 1


    # def create_bricks(self, surface, colour, ):
    #     # x = 0
    #     # no_bricks = self.screen_width/brick_width
    #     # brick_width = 40
    #
    #     pygame.draw.rect(surface=surface, color=colour, rect=rect)
    #
    #     # #store in list so maybe in the future we can do brick dissapearance with list.pop()
    #     self.brick_list.append(rect)
    #
    #     # return self.rect
