import pygame

# Initialize pygame
pygame.init()

# Create game window
WIDTH = 800
HEIGHT = 600
game_board = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Discrete Movement")

# Set game values
VELO = 10

# Load in images
dragon = pygame.image.load("dragon_right.png")
dragon_rect = dragon.get_rect()
dragon_rect.centerx = WIDTH//2
dragon_rect.bottom = HEIGHT

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x -= VELO
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dragon_rect.x += VELO
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dragon_rect.y -= VELO
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                dragon_rect.y += VELO
                
# Fill display surfact to cover up old images
    game_board.fill((0,0,0)) 
             
# Blit (copy) assets to screen
    game_board.blit(dragon, dragon_rect)

# Update the display
    pygame.display.update()

# Exit pygame
pygame.quit()
