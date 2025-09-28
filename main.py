import pygame
from ball import Ball
from paddle import Paddle
from bricks import Bricks
from random import Random
from score import Score
from image_icon import Image


# """TODO1 : Sound Effect"""
"""TODO2: Add pause and play feature"""
"""TODO3: REFLECT SCORE COUNT SOMEWHERE ON SCREEN"""




# """TODO4: add nice colors"""

rand = Random()
game_state = {}

#
destroyed_balls = []


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

running = True
#intitial frame per second definition
dt = clock.tick(60)/1000

#Defines initial ball position
ball_pos = pygame.Vector2(screen.get_width()/2, 620)

#Creates rectangle.
rect = pygame.Rect((580, 700), (200, 100))

#Creates the paddle instance from the Paddle class
paddle = Paddle(screen, "#BCA88D", rect, 40)

speed = [2, 2]
#creates the ball instance from the Ball class
ball = Ball(screen, "#F1F0E4", ball_pos, 10, dt, speed)






destructible_brick = Bricks(screen.get_width())
destructible_brick.create_rect()


#sound
pygame.mixer.init()
brick_bounce_sound = pygame.mixer.Sound("sound/impact_brick_hit_ground_004.mp3")
paddle_bounce_sound = pygame.mixer.Sound("sound/mixkit-basketball-ball-hard-hit-2093.wav")


color_list = ["red", "blue", "green"]
score = Score()

#initialize font for writing score.
font = pygame.font.SysFont("Arial", 40)

paused = False
frozen_frame = None


def next_stage():
    global ball
    #draw bricks
    destructible_brick.create_rect()

    #throw away ball and create new ball
    ball = Ball(screen, "#F1F0E4", ball_pos, 10, dt, speed)
    ball.speed_up()

    #reset paddle to centre of screen

#image buttons

# pause_img = pygame.image.load("images/pause-icon-13.png").convert_alpha()
# pause_img = pygame.transform.scale(pause_img, (64, 64))
#
# #button_rect
# pause_img_rect = pause_img.get_rect(center=(screen.get_width() * 0.8, 30))
#
# pause_hover_img = pygame.image.load("images/pause-icon-13.png").convert_alpha()
# pause_hover_img = pygame.transform.scale(pause_hover_img, (70, 70))
#
# pause_hover_img_rect = pause_hover_img.get_rect(center=(screen.get_width() * 0.8, 30))


pause_obj = Image("images/pause-icon-13.png")
pause_list = pause_obj.create_image(64, 64)

pause_img = pause_list[0]
pause_hover_img = pause_list[1]

rect_list = pause_obj.create_rect(screen.get_width() * 0.8, 33)

pause_img_rect = rect_list[0]
pause_hover_img_rect = rect_list[1]



play_obj = Image("images/play-icon-2.png")
play_list = play_obj.create_image(44, 44)

play_img = play_list[0]
play_hover_img = play_list[1]

play_rect_list = play_obj.create_rect(screen.get_width() * 0.9, 33)

play_img_rect = play_rect_list[0]
play_hover_img_rect = play_rect_list[1]




"""TODO2: Create Destructible bricks."""
while running:
    # poll for events-+
    # pygame.QUIT event means the user clicked X to close your window
    # print(ball.ball_pos.y)
    mouse_position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #key down event for pausing the game
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pause_img_rect.collidepoint(mouse_position):
                paused = True
                if paused:
                    frozen_frame = screen.copy()
        #keydown event for unpausing the game.
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_img_rect.collidepoint(mouse_position):
                paused = False

        """TODO: OTHER CONDITION FOR GAME OVER HERE"""



    # fill the screen with a color to wipe away anything from last frame
    if not paused:
        screen.fill("#44444E")

        #hover effect for button logic
        if pause_img_rect.collidepoint(mouse_position):
            screen.blit(pause_hover_img, pause_hover_img_rect)
        else:
            screen.blit(pause_img, pause_img_rect)

        if play_img_rect.collidepoint(mouse_position):
            screen.blit(play_hover_img, play_hover_img_rect)
        else:
            screen.blit(play_img, play_img_rect)
        # RENDER YOUR GAME HERE

        ball_rect = ball.draw_ball()

        ball.move_ball()


        paddle.create_paddle()


        """MOVE PADDLE WITH USER INPUT"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            #Limits the movement of paddle, so it won't move beyond screen
            if rect.x <= 1080:  #screen size minus width of paddle since x is wrp to top left of paddle
                rect.x += 300 * dt
        if keys[pygame.K_LEFT]:
            if rect.x >= 4:
                rect.x -= 300 * dt

        #SPPED UP BALL IF CONDITIONS ARE MET
        # speed_up = destructible_brick.time_to_speedup()
        # if speed_up:
        #     ball.speed_up()



        """TODO1: DEFINE CONDITIONS & LOGIC FOR BALL BOUNCE AGAINST PADDLE AND WALL"""
        if ball.ball_pos.y <= 4:
            ball.bounce_y()
            paddle_bounce_sound.play()
        elif ball.ball_pos.x <= 0 or ball.ball_pos.x >= screen.get_width():
            ball.bounce_x()
            paddle_bounce_sound.play()
        elif ball.ball_pos.y >= screen.get_height():
            print("out")
            # game_state["ball"] = pygame.Vector2(ball_pos.x, ball_pos.y)
            #save state of bricks
            game_state["brick"] = destructible_brick.brick_list

            #create new ball instance, and set position, speed of ball, and direction of ball.
            ball = Ball(screen, "#F1F0E4", ball_pos, 10, dt, speed)
            ball.ball_pos.y = rect.top - 10
            ball.ball_pos.x = rect.left + 100
            # speed = [2, 2]
            ball.reset_ball()




        # if (ball.ball_pos.x - rect.x) == 90 and (rect.y - ball.ball_pos.y) <= 6:
        #     ball.bounce_y()




        if rect.colliderect(ball_rect):
            ball.bounce_y()
            paddle_bounce_sound.play()
            #makes ball position outside the paddle so collision will only be detected once.
            ball.ball_pos.y = rect.top - 10


        #DRAW BRICKS ON WALL AND MAKE EACH LINE DIFFERENT COLOR

        # for brick in destructible_brick.brick_list:
        #     # color = rand.choice(color_list)
        #     pygame.draw.rect(screen, "red", brick, destructible_brick.brick_width)

        for index, brick in enumerate(destructible_brick.brick_list):
            color = ["#E43636", "#F4991A", "#E2DDB4", "#F6EFD2"]
            if brick == "":
                pass
            else:
                if index <= 15:
                    s_color = color[0]
                elif 15 < index <= 31:
                    s_color = color[1]
                elif 31 < index <= 47:
                    s_color = color[2]
                elif index > 47:
                    s_color = color[3]

                pygame.draw.rect(screen, s_color, brick, destructible_brick.brick_width)


        #CHECK FOR BALL COLLISION WITH BRICK, AND BRICK DISSAPPEAR.

        # for brick in destructible_brick.brick_list:
        #     if brick.colliderect(ball_rect):
        #         brick_index = destructible_brick.brick_list.index(brick)
        #         destructible_brick.brick_list.pop(brick_index)
        #         ball.bounce_y()
                # ball.bounce_x()

        for index, brick in enumerate(destructible_brick.brick_list):
            if brick == "":
                pass
            else:
                if brick.colliderect(ball_rect):
                    score.update_score(index)

                    destroyed_balls.append(brick)
                    print(len(destroyed_balls))
                    destructible_brick.brick_list[index] = ""
                    brick_bounce_sound.play()
                    ball.bounce_y()

                    # print(score.total_score)
        #writes score to screen.
        text = font.render(str(score.total_score), True, (255, 255, 255))
        text_score_rect = text.get_rect(center=(screen.get_width() / 2, 30))
        screen.blit(text, text_score_rect)



        if len(destroyed_balls) == 64:
            ball.ball_pos = [2000, 2000]
            print("finished")
            destructible_brick.brick_list.clear()
            next_stage()
            destroyed_balls.clear()






        """"""







    else:
        #renders when game is paused
        screen.blit(frozen_frame, (0,0))





    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60)/1000  # limits FPS to 60

pygame.quit()