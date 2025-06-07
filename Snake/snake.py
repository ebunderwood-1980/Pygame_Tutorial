import pygame
import random

# Initialize Pygame
pygame.init()

# Create the gameboard
W = 1000
H = 800
game_board = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")

# Set the FPS and the Clock
FPS = 20
clock = pygame.time.Clock()

# Set game values
score = 0
SNAKE_SIZE = 20

head_x = W // 2
head_y = H // 2 + 100 
apple_x = 100
apple_y = 250

snake_dx = 0
snake_dy = 0

# Set colors
RED = (255, 0, 0)
DRED = (150, 0, 0)
GREEN = (0, 255, 0)
DGREEN = (0, 100, 0)
WHITE = (255, 255, 255)

# Set fonts
font = pygame.font.SysFont('IoevkaTermNerdFontMono-Thin.ttf', 48)

# Render text
score_text = font.render("Score:  " + str(score), True, RED, WHITE)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = font.render("SNAKE", True, RED, WHITE)
title_rect = title_text.get_rect()
title_rect.center = (W//2, H//2)

game_over_text = font.render("Game Over", True, DGREEN, WHITE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (W//2, H//2)

play_again_text = font.render("Hit any key to play again", True, DGREEN, WHITE)
play_again_rect = play_again_text.get_rect()
play_again_rect.center = (W//2, H//2 + 100)

# Set sounds and music
chomp = pygame.mixer.Sound('pick_up_sound.wav')
chomp.set_volume(0.3)

# Create the snake and the apple
apple_coord = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(game_board, RED, apple_coord)
head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(game_board, GREEN, head_coord)

body_coords = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -1 * SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -1 * SNAKE_SIZE
            if event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = SNAKE_SIZE

    # Add the head coord into the first index of the body coord to move entire snake.
    # Update the x, y position of the snake head 
    body_coords.insert(0, head_coord)
    body_coords.pop()
    
    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

    # Check for game over by going off of screen
    if head_rect.left < 0 or head_rect.right > W or head_rect.top < 0 or head_rect.bottom > H or head_coord in body_coords:
        game_board.blit(game_over_text, game_over_rect)
        game_board.blit(play_again_text, play_again_rect)
        pygame.display.update()

        # Pause game until player presses key.
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    head_x = W//2
                    head_y = H//2 + 100
                    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
                    body_coords = []
                    snake_dx = 0
                    snake_dy = 0
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    # Check for collisions
    if head_rect.colliderect(apple_rect):
        score += 1
        chomp.play()
        apple_x = random.randint(0, W-SNAKE_SIZE)
        apple_y = random.randint(0, H-SNAKE_SIZE)
        apple_coord = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)

        # Add to the body
        body_coords.append(head_coord)

    # Check for Q to end game
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False

    # Fill the screen
    game_board.fill(WHITE)

    # Update HUD
    score_text = font.render("Score:  " + str(score), True, RED, WHITE)
     
    # Blit the Score and Title
    game_board.blit(score_text, score_rect)
    game_board.blit(title_text, title_rect)

    # Blit the snake and the apple
    apple_rect = pygame.draw.rect(game_board, RED, apple_coord)
    head_rect = pygame.draw.rect(game_board, GREEN, head_coord)
    for body in body_coords:
        pygame.draw.rect(game_board, DGREEN, body)

  # Update game and tick clock
    pygame.display.update()
    clock.tick(FPS)

# End game
pygame.quit()


