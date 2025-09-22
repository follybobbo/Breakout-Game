import pygame
from ball import Ball
from paddle import Paddle
from bricks import Bricks
from random import Random

rand = Random()


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

running = True
#intitial frame per second definition
dt = clock.tick(60)/1000

#Defines initial ball position
ball_pos = pygame.Vector2(screen.get_width()/2, 620)

#Creates rectangle.
rect = pygame.Rect((580, 700), (100, 100))

#Creates the paddle instance from the Paddle class
paddle = Paddle(screen, "blue", rect, 40)

speed = [2, 2]
#creates the ball instance from the Ball class
ball = Ball(screen, "red", ball_pos, 10, dt, speed)

#brick rect




destructible_brick = Bricks(screen.get_width())

destructible_brick.create_rect()
# print(len(destructible_brick.brick_list))
# for rect in destructible_brick.brick_list:
#     print(rect)


color_list = ["red", "blue", "green"]




"""TODO2: Create Destructible bricks."""
while running:
    # poll for events-+
    # pygame.QUIT event means the user clicked X to close your window
    # print(ball.ball_pos.y)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        """TODO: OTHER CONDITION FOR GAME OVER HERE"""



    # fill the screen with a color to wipe away anything from last frame

    screen.fill("black")
    # RENDER YOUR GAME HERE



    ball.draw_ball()

    ball.move_ball()


    paddle.create_paddle()

    """MOVE PADDLE WITH USER INPUT"""
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        #Limits the movement of paddle, so it won't move beyond screen
        if rect.x <= 1175:
            rect.x += 300 * dt
    if keys[pygame.K_LEFT]:
        if rect.x >= 4:
            rect.x -= 300 * dt



    """TODO1: DEFINE CONDITIONS & LOGIC FOR BALL BOUNCE AGAINST PADDLE AND WALL"""
    if ball.ball_pos.y <= 4:
        ball.bounce_y()
    if ball.ball_pos.x <= 0 or ball.ball_pos.x >= screen.get_width():
        ball.bounce_x()


    if (rect.y - ball.ball_pos.y) < 10 and (rect.x - ball.ball_pos.x) < abs(10):
        ball.bounce_y()

    for brick in destructible_brick.brick_list:
        # color = rand.choice(color_list)
        pygame.draw.rect(screen, "red", brick, destructible_brick.brick_width)











    """TODO3: DEFINE LOGIC AND CONDITIONS FOR DESTRUCTION OF BRICK UPON IMPACT WITH BALL AND THEN BOUNCE"""




    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60)/1000  # limits FPS to 60

pygame.quit()