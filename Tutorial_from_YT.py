import pygame

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Movable object
player = pygame.Rect((300, 250, 50, 50))

# Game loop
run = True
while run:

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)

    # Boundary checks
    if player.left < 0:
        player.left = 0 # Left boundary, 10 to leave space
    if player.right > SCREEN_WIDTH:
        player.right = SCREEN_WIDTH # Right boundary, 790 to leave space
    if player.top < 0:
        player.top = 0 # Top boundary, 10 to leave space
    if player.bottom > SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT # Bottom boundary, 590 to leave space

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()