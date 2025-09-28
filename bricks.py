import pygame




class Bricks:

    def __init__(self, screenwidth):
        self.brick_list = []
        self.screen_width = screenwidth
        self.brick_width = 80
        self.no_of_brick = self.screen_width/self.brick_width



    def create_rect(self):
        x = 0  # x starting point
        y = 120  # y starting point

        row = 4
        brick_row = row * self.no_of_brick
        for times in range(int(brick_row)):
            if x >= 1280:
                x = 0
                y += 30 + 1
            rect = pygame.Rect((x, y), (self.brick_width, 30))
            self.brick_list.append(rect)
            x += self.brick_width + 1

    def time_to_speedup(self):
        destroyed_count = 0
        for rect in self.brick_list:
            if rect == "":
                destroyed_count += 1

        percentage_destroyed = (destroyed_count/64) * 100
        # print(destroyed_count)
        if destroyed_count == 15:
            return True
        elif destroyed_count == 30:
            return True
        elif destroyed_count == 45:
            return True
        else:
            return False




