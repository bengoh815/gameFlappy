import pygame
import sys
from math import floor

pygame.init()
screen = pygame.display.set_mode(size=(900, 500))

clock = pygame.time.Clock()

# imports & initialization
game_started = False
score = 0
object_move_speed = 2

# background
bg_x = 0
bg1_x = 900
bg = pygame.image.load("./static_images/bg.png")

# bird
bird = pygame.image.load("./static_images/bird.png")
bird_hitbox = bird.get_rect(topleft=(100, 200))
bird_velocity_i_y = 0
bird_jumping = False
bird_jump = 11
bird_jump_variable = 0

# pipe
pipe = pygame.image.load("./static_images/pipe.png")
pipe1 = pygame.image.load("./static_images/pipe_upsideDown.png")
pipe_hitbox = pipe.get_rect(topleft=(650, 300))
pipe1_hitbox = pipe.get_rect(bottomleft=(pipe_hitbox.x, (pipe_hitbox.y - 175)))
added_score = False

# gravity
gravity = 1

# function
# check background
def bg_move(x):
    if abs(x) >= 900 and x < 0:
        return 900
    return x

pygame.event.clear
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_jump_variable = bird_jump


    # objects moving left
    bg_x -= object_move_speed
    bg1_x -= object_move_speed
    pipe_hitbox.x -= object_move_speed
    pipe1_hitbox.x =pipe_hitbox.x

    # rendering
    # bg
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg1_x, 0))
    # bird
    screen.blit(bird, bird_hitbox)
    # pipe
    screen.blit(pipe, pipe_hitbox)
    screen.blit(pipe1, pipe1_hitbox)

    # gravity
    bird_hitbox.y -= bird_jump_variable
    bird_jump_variable -= gravity

    # check background
    bg_x = bg_move(bg_x)
    bg1_x = bg_move(bg1_x)

    # check death
    if bird_hitbox.colliderect(pipe_hitbox) or bird_hitbox.colliderect(pipe1_hitbox) or (bird_hitbox.y >= 480):
        print('Game over~')
        sys.exit()

    pygame.display.update()
    clock.tick(20)

    # check points
    if ((bird_hitbox.x + bird_hitbox.width) > (pipe_hitbox.x  + (pipe_hitbox.width / 2))) and added_score == False:
        added_score = True
        score += 1
        print(score)