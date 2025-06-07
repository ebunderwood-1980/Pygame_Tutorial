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
clown_dx = random.choice([-1, 1])
clown_dy = random.choice([-1, 1])

# Colors
BLACK = (0, 0, 0)
YELLOW = (248, 231, 28)
LT_BLUE = (1, 175, 209)

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
left_text = font.render("CATCH THE CLOWN", True, LT_BLUE)
left_text_rect = left_text.get_rect()
left_text_rect.topleft = (10, 10)

score_text = font.render("SCORE:  " + str(score), True, YELLOW)
score_text_rect = score_text.get_rect()
score_text_rect.topright = (W - 10, 10)

lives_text = font.render("LIVES:  " + str(lives), True, YELLOW)
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (W - 10, 50) 

game_over_text = font.render("GAME OVER", True, LT_BLUE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (W//4, H//2)

play_again_text = font.render("PRESS ANY KEY TO RESTART", True, YELLOW)
play_again_rect = play_again_text.get_rect()
play_again_rect.center = (3 * (W//4), H//2)

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
            score += 1
            score_text = font.render("Score:  " + str(score), True, YELLOW, LT_BLUE) 
            click.play()
        else:
            print("Miss")
            lives -= 1
            lives_text = font.render("Lives:  " + str(lives), True, YELLOW, LT_BLUE) 
            miss.play()

    # Check for endgame and handle if lives < 0
    if lives <= 0:
        game_board.blit(game_over_text, game_over_rect)
        game_board.blit(play_again_text, play_again_rect)
        pygame.display.update()

        # Pause game until user presses a key or quits the game
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    lives = STARTING_LIVES
                    score = STARTING_SCORE 
                    clown_velo_x = CLOWN_STARTING_VELO 
                    clown_velo_y = CLOWN_STARTING_VELO
                    img_clown_rect.center = CLOWN_START 
                    pygame.mixer.music.play(-1, 0.0)  
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False
                    
    # Update the display
    pygame.display.update()
    
    clock.tick(FPS)
    
# Exit Pygame
pygame.quit()

