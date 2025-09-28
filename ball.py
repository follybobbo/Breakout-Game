import pygame
DISTANCE = 100


class Ball:

    def __init__(self, screen, color, ball_pos, radius, dt, speed):
        self.surface = screen
        self.color = color
        self.ball_pos = pygame.Vector2(ball_pos)
        self.rad = radius
        self.dt = dt
        self.speed = speed




    #draws circle on screen, which is the ball
    def draw_ball(self):
        ball_rect = pygame.draw.circle(self.surface, self.color, self.ball_pos, self.rad)
        return ball_rect

    #changes the ball position in both x and y direction
    def move_ball(self):
        self.ball_pos.y -= self.speed[1]
        self.ball_pos.x += self.speed[0]

    #inverts the y direction of the ball
    def bounce_y(self):
       self.speed[1] *= -1

    def bounce_x(self):
       self.speed[0] *= -1

    def speed_up(self):
        self.speed[0] *= 1.08
        self.speed[1] *= 1.08

    # def paddle_bounce(self):
    #     self.speed[1] *= -1
    #
    #     self.speed[0] *= -1

    def reset_ball(self):
        self.speed[1] *= -1


