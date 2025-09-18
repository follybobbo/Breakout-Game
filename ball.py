import pygame


class Ball():

    def __init__(self, screen, color, ball_pos, radius, dt):
        self.surface = screen
        self.color = color
        self.ball_pos = ball_pos
        self.rad = radius
        self.dt = dt



    def create_ball(self):
        pygame.draw.circle(self.surface, self.color, self.ball_pos, self.rad)

    def move_ball(self):
        self.ball_pos.y -= 100 * self.dt
        # self.ball_pos.x = 100 * self.dt
