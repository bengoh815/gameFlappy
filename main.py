import pygame
import sys

pygame.init()
screen = pygame.display.set_mode(size=(900, 500))

clock = pygame.time.Clock()

# imports
# background
bg = pygame.image.load("./static_images/bg.png")
bg1 = pygame.image.load("./static_images/bg.png")

# bird
bird = pygame.image.load("./static_images/bird.png")
bird_hitbox = bird.get_rect(topleft=(100, 200))
bird_velocity_i_y = 0



# pipe
pipe = pygame.image.load("./static_images/pipe.png")
pipe_hitbox = pipe.get_rect(topleft=(650, 300))


pygame.event.clear()
while True:
    # rendering
    # bg
    screen.blit(bg, (0, 0))
    # bird
    screen.blit(bird, bird_hitbox)
    # pipe
    screen.blit(pipe, pipe_hitbox)

    pygame.display.update()
    clock.tick(60)

    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            print("game started")


