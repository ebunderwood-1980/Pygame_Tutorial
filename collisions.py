import pygame
import keyboard
import random

# Initiate Pygame
pygame.init()

# Create the game window
W = 1600
H = 1200
B = (0, 0, 0)
game_board = pygame.display.set_mode((W, H))
pygame.display.set_caption("Collision Detection")

# Set game constants
V = 5
FPS = 60
clock = pygame.time.Clock()

# Load the dragon image to the middle of the game board
dragon = pygame.image.load('dragon_right.png')
dragon_rect = dragon.get_rect()
dragon_rect.centerx = W//2
dragon_rect.centery = H//2

# Load the coin image on to the game board
coin = pygame.image.load('coin.png')
coin_rect = coin.get_rect()
coin_rect.centerx = 1200
coin_rect.centery = 1000

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keyboard.is_pressed('q'):
            running = False

    # Get list of all keys currently being held
    keys = pygame.key.get_pressed()

    # Move the dragon continuously using arrow keys or W, A, S, D
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_rect.left > 0:
        dragon_rect.x -= V
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_rect.right < W:
        dragon_rect.x += V
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_rect.top > 0:
        dragon_rect.y -= V
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_rect.bottom < H:
        dragon_rect.y += V

    # Fill the display surface to cover up old images
    game_board.fill(B)

    # Check for collision between two rect's and move coin to new location if there is a hit
    if dragon_rect.colliderect(coin_rect):
        print("HIT")
        coin_rect.x = random.randint(0, W-32)
        coin_rect.y = random.randint(0, H-32)
        

    # Draw the rectangles to represent the rect's of each object
    pygame.draw.rect(game_board, (255, 0, 0), dragon_rect, 1)
    pygame.draw.rect(game_board, (255, 255, 0), coin_rect, 1)

    # Blit the assets to the game board
    game_board.blit(dragon, dragon_rect)
    game_board.blit(coin, coin_rect)

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)

# Close Pygame
pygame.quit()
