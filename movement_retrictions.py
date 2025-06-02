import pygame 
import keyboard

# Initiate Pygame
pygame.init()

# Create the game window
W = 1600
H = 1200
B = (0,0,0)
game_board = pygame.display.set_mode((W, H))
pygame.display.set_caption("Movement Restrictions")

# Set game constants
V = 5
FPS = 60
clock = pygame.time.Clock()

# Load dragon image
dragon = pygame.image.load('dragon_right.png')
dragon_rect = dragon.get_rect()
dragon_rect.centerx = W//2
dragon_rect.centery = H//2

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keyboard.is_pressed('q'):
            running = False

    # Get a list of all keys currently being held
    keys = pygame.key.get_pressed()

    # Move the dragon continuously
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_rect.left > 0: 
        dragon_rect.x -= V
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_rect.right < W:
        dragon_rect.x += V
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_rect.top > 0:
        dragon_rect.y -= V
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_rect.bottom < H:
        dragon_rect.y += V


    # Fill display surface to cover up old images
    game_board.fill(B)

    # Blit the image to the game board
    game_board.blit(dragon, dragon_rect)

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
