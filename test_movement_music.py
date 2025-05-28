import pygame

# Initialize Pygame
pygame.init()

# Set up the game board
W = 1600
H = 1200
BLACK = (0, 0, 0)
game_board = pygame.display.set_mode((W,H))
pygame.display.set_caption("Keyboard Movement with Sound")

# Set the velocity in which my dragon moves
V = 15

# Load in Dragon image
dragon = pygame.image.load("dragon_right.png")
dragon_rect = dragon.get_rect()
dragon_rect.centerx = W//2
dragon_rect.bottom = H//2

# Load in sound assets
sound = pygame.mixer.Sound('sound_1.wav')

# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exiting")
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Moving Left")
                dragon_rect.x -= V
            if event.key == pygame.K_RIGHT:
                print("Moving right")
                dragon_rect.x += V
            if event.key == pygame.K_UP:
                print("Moving up")
                dragon_rect.y -= V
            if event.key == pygame.K_DOWN:
                print("Moving down")
                dragon_rect.y += V
            else:
                print("Unknown key pressed")

# If x is greater than 900 or y is greater than 700 play sound 
    if dragon_rect.x >= 900 or dragon_rect.y >= 700:
        sound.play()

# Fill display surface to cover up old images
    game_board.fill(BLACK)

# Blit the assets to the screen
    game_board.blit(dragon, dragon_rect)

# Update the display
    pygame.display.update()

# Exit Pygame
pygame.quit()
