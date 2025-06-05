import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display surface
W = 967
H = 655
game_board = pygame.display.set_mode((W, H))
pygame.display.set_caption("Catch the Clown")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Set game values
STARTING_LIVES = 5
CLOWN_STARTING_VELO = 5
CLOWN_ACCELERATION = 1
CLOWN_START = (900, 100)
STARTING_SCORE = 0
score = STARTING_SCORE
lives = STARTING_LIVES
clown_velo_x = CLOWN_STARTING_VELO 
clown_velo_y = CLOWN_STARTING_VELO

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
LT_BLUE = (173, 216, 230)

# Load sound effects and music
click = pygame.mixer.Sound('click_sound.wav')
miss = pygame.mixer.Sound('miss_sound.wav')
pygame.mixer.music.load('ctc_background_music.wav')
pygame.mixer.music.set_volume(0.3)
click.set_volume(0.2)
miss.set_volume(0.2)

# Load image assets
img_clown = pygame.image.load('clown.png')
img_clown_rect = img_clown.get_rect()
img_clown_rect.center = CLOWN_START

background = pygame.image.load('background.png')
background_rect = background.get_rect()
background_rect.topleft = (0, 0)

# Load font
font = pygame.font.Font('Franxurter.ttf', 32)

# Render game texts
left_text = font.render("CATCH THE CLOWN", True, LT_BLUE, YELLOW)
left_text_rect = left_text.get_rect()
left_text_rect.topleft = (10, 10)

score_text = font.render("SCORE:  " + str(score), True, YELLOW, LT_BLUE)
score_text_rect = score_text.get_rect()
score_text_rect.topright = (W - 10, 10)

lives_text = font.render("LIVES:  " + str(lives), True, YELLOW, LT_BLUE)
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (W - 10, 50)

# Main game loop
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get a list of all keys currently being held
    keys = pygame.key.get_pressed()

    # Search for Q to quit
    if keys[pygame.K_q]:
        running = False

    # Blit Assets to the game board
    game_board.blit(background, background_rect)
    game_board.blit(left_text, left_text_rect)
    game_board.blit(score_text, score_text_rect)
    game_board.blit(lives_text, lives_text_rect)
    game_board.blit(img_clown, img_clown_rect)

    # Move the clown around the board
    img_clown_rect.x -= clown_velo_x
    img_clown_rect.y += clown_velo_y
    if img_clown_rect.left <= 0 or img_clown_rect.right >= W:
        clown_velo_x = clown_velo_x * -1
    if img_clown_rect.top <= 0 or img_clown_rect.bottom >= H:
        clown_velo_y = clown_velo_y * -1

    # Check for mouse clicks and collisions with the clown
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseX = event.pos[0]
        mouseY = event.pos[1]
        if img_clown_rect.collidepoint(mouseX, mouseY):
            print("Hit")
        else:
            print("Miss")

    # Update the display
    pygame.display.update()
    
    clock.tick(FPS)
    
# Exit Pygame
pygame.quit()

