import pygame

# Initialize Pygame
pygame.init()

# Create the game window
W = 1600
H = 1200
B = (0, 0, 0)
game_board = pygame.display.set_mode((W, H))
pygame.display.set_caption("Continuous Keyboard Movement")

# Set game values
V = 5
FPS = 60
clock = pygame.time.Clock()

# Load keyboard images
dragon = pygame.image.load("dragon_right.png")
dragon_rect = dragon.get_rect()
dragon_rect.centerx = W//2
dragon_rect.centery = H//2

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get a list of all keys currently being held
    keys = pygame.key.get_pressed()

    # Move the dragon continuously
    if keys[pygame.K_LEFT]:
        dragon_rect.x -= V 
    if keys[pygame.K_RIGHT]:
        dragon_rect.x += V
    if keys[pygame.K_UP]:
        dragon_rect.y -= V
    if keys[pygame.K_DOWN]:
        dragon_rect.y += V

    # Fill display surface to cover up old images
    game_board.fill(B)

    # Blit assets to the screen
    game_board.blit(dragon, dragon_rect)  

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
