import pygame
import random

# Initialize Pygame
pygame.init()

# Create display surfaces
W = 1900 
H = 1200
game_board = pygame.display.set_mode((W, H))
pygame.display.set_caption = "Feed the Dragon" 

# Define Colors
GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set game constants
V = 5
FPS = 60
clock = pygame.time.Clock()

# Load sound effects
successful_chomp = pygame.mixer.Sound('sound_1.wav')
missed_coin = pygame.mixer.Sound('sound_2.wav')
successful_chomp.set_volume(.2)
missed_coin.set_volume(.2)

# Load background music
music = pygame.mixer.music.load('music.wav')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1, 0.0)

# Define fonts
game_font = pygame.font.Font('AttackGraffiti.ttf', 32)

# Set up game texts
game_name = game_font.render("Feed the Dragon", True, GREEN, WHITE) 
game_name_rect = game_name.get_rect()
game_name_rect.center = (W//2, 50) 

score_text = game_font.render("Score:", True, GREEN, DARK_GREEN)
score_text_rect = score_text.get_rect()
score_text_rect.center = (100, 50) 

lives_text = game_font.render("Lives:", True, GREEN, DARK_GREEN)
lives_text_rect = lives_text.get_rect()
lives_text_rect.center = (W-150, 50)

actual_lives = 5
actual_lives_text = game_font.render(str(actual_lives), True, GREEN, DARK_GREEN)
actual_lives_rect = actual_lives_text.get_rect()
actual_lives_rect.center = (W-85, 50)

actual_score = 0
actual_score_text = game_font.render(str(actual_score), True, GREEN, DARK_GREEN)
actual_score_rect = actual_score_text.get_rect()
actual_score_rect.center = (185, 50)

# Add dragon image
dragon = pygame.image.load('dragon_right.png')
dragon_rect = dragon.get_rect()
dragon_rect.x = 50
dragon_rect.y = 120

# Add the first coin spawn on the right side of the board
coin = pygame.image.load('coin.png')
coin_rect = coin.get_rect()
coin_rect.x = W-40
coin_rect.y = random.randint(120, H-32) # Making sure the coin does not initially spawn off the board.

# Main game loop:
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get a list of all keys currently being held
    keys = pygame.key.get_pressed()

    # Quick check for Q to quit
    if keys[pygame.K_q]:
        running = False

    # Continuous Dragon Movement (up and down only)
    if keys[pygame.K_UP] and dragon_rect.top > 100:
        dragon_rect.y -= V
    if keys[pygame.K_DOWN] and dragon_rect.bottom < H:
        dragon_rect.y += V

    # Move the coin to the left of the board
    coin_rect.x -= V

    # Coin collision checks, both wall and dragon
    if dragon_rect.colliderect(coin_rect):
        actual_score += 1
        actual_score_text = game_font.render(str(actual_score), True, GREEN, DARK_GREEN)
        V += 2  # Increase velocity every time you successfully eat a coin
        successful_chomp.play()
        coin_rect.x = W-40
        coin_rect.y = random.randint(120, H-32)
        game_board.blit(actual_score_text, actual_score_rect)

    if coin_rect.left <= 0:
        actual_lives -= 1
        V = 5    # Reset the velocity once a wall has been struck.
        missed_coin.play()
        actual_lives_text = game_font.render(str(actual_lives), True, GREEN, DARK_GREEN)
        coin_rect.x = W-40 
        coin_rect.y = random.randint(120, H-32)

    # Fill the gameboard to cover up old images
    game_board.fill(BLACK)

    # Draw a line under the scoreboard
    pygame.draw.line(game_board, WHITE, (0, 100), (W, 100), 5)

    # Blit assets to display surface
    game_board.blit(game_name, game_name_rect)
    game_board.blit(score_text, score_text_rect)
    game_board.blit(lives_text, lives_text_rect)
    game_board.blit(dragon, dragon_rect)
    game_board.blit(actual_lives_text, actual_lives_rect)
    game_board.blit(actual_score_text, actual_score_rect)
    game_board.blit(coin, coin_rect)

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)

# End the game
pygame.quit()
            
