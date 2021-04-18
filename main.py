import pygame
import sys
from math import floor

pygame.init()
screen = pygame.display.set_mode(size=(900, 500))

clock = pygame.time.Clock()

# imports & initialization
game_started = False
# background
bg = pygame.image.load("./static_images/bg.png")
bg1 = pygame.image.load("./static_images/bg.png")

# bird
bird = pygame.image.load("./static_images/bird.png")
bird_hitbox = bird.get_rect(topleft=(100, 200))
bird_velocity_i_y = 0
bird_jumping = False
bird_jump = 11
bird_jump_variable = 0

# pipe
pipe = pygame.image.load("./static_images/pipe.png")
pipe_hitbox = pipe.get_rect(topleft=(650, 300))

# gravity
gravity = 1



while True:
    # rendering
    # bg
    screen.blit(bg, (0, 0))
    # bird
    screen.blit(bird, bird_hitbox)
    # pipe
    screen.blit(pipe, pipe_hitbox)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('SPACEEEEEEEEE')
                bird_jump_variable = bird_jump

    bird_hitbox.y -= bird_jump_variable
    bird_jump_variable -= gravity

    print(bird_hitbox.y, bird_jump_variable)

    if bird_hitbox.y > 480:
            sys.exit()

    pygame.display.update()
    clock.tick(20)