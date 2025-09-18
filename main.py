import pygame
from ball import Ball
from paddle import Paddle

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = clock.tick(60)/1000

ball_pos = pygame.Vector2(screen.get_width()/2, screen.get_height())
rect = pygame.Rect((580, 700), (100, 100))


ball = Ball(screen, "red", ball_pos, 10, dt)
paddle = Paddle(screen, "blue", rect, 40)

while running:
    # poll for events-+
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        """TODO: OTHER CONDITION FOR GAME OVER HERE"""



    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    """TODO: Game Logic Here"""
    # RENDER YOUR GAME HERE
    ball.create_ball()
    ball.move_ball()

    paddle.create_paddle()
    # flip() the display to put your work on screen
    pygame.display.flip()
    """Define dt here: seconds/frame."""
    dt = clock.tick(60)/1000  # limits FPS to 60

pygame.quit()