import pygame
import random

# Set up Pygame
pygame.init()

# Set up the surface display
WIDTH = 1200
HEIGHT = 1000
surface_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Burger Dog")

# Set up the FPS and the Clock
FPS = 60
clock = pygame.time.Clock()

# Set up constant values for game reset
START_LIVES = 1
START_BOOST = 100
STARTING_BURGER_VELOCIY = 3
STARTING_DOG_VELOCITY = 5
BOOST_ACCEL = 10

# Set up game values
burger_points = 0
score = 0
burgers_eaten = 0
current_burger_velocity = STARTING_BURGER_VELOCIY
current_dog_velocity = STARTING_DOG_VELOCITY
lives = START_LIVES
boost = START_BOOST

# Set up game colors
DARK_YELLOW = (186, 142, 35)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up game font
font = pygame.font.Font("WashYourHand.ttf", 32)

# Render HUD texts
burger_points_text = font.render(
    "Burger Points:  " + str(burger_points), True, DARK_YELLOW
)
burger_points_rect = burger_points_text.get_rect()
burger_points_rect.topleft = (10, 10)

game_name_text = font.render("Burger Dog", True, DARK_YELLOW)
game_name_rect = game_name_text.get_rect()
game_name_rect.centerx = WIDTH // 2
game_name_rect.top = 10

lives_text = font.render("Lives:  " + str(lives), True, DARK_YELLOW)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WIDTH - 10, 10)

score_text = font.render("Score:  " + str(score), True, DARK_YELLOW)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 50)

burgers_eaten_text = font.render(
    "Burgers Eaten:  " + str(burgers_eaten), True, DARK_YELLOW
)
burgers_eaten_rect = burgers_eaten_text.get_rect()
burgers_eaten_rect.centerx = WIDTH // 2
burgers_eaten_rect.top = 50

game_over_text = font.render("GAME OVER!!!", True, DARK_YELLOW)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WIDTH // 2, HEIGHT // 2 - 32)

play_again_text = font.render("Press any key to play again", True, DARK_YELLOW)
play_again_rect = play_again_text.get_rect()
play_again_rect.center = (WIDTH // 2, HEIGHT // 2 + 32)

boost_text = font.render("Boost:  " + str(boost), True, DARK_YELLOW)
boost_text_rect = boost_text.get_rect()
boost_text_rect.topright = (WIDTH - 10, 50)

# Set background music
background_music = pygame.mixer.music.load("bd_background_music.wav")
pygame.mixer.music.set_volume(0.3)

# Set up sounds
bark_sound = pygame.mixer.Sound("bark_sound.wav")
bark_sound.set_volume(0.3)
miss_sound = pygame.mixer.Sound("miss_sound.wav")
miss_sound.set_volume(0.3)

# Add the Puppy Dog Image
dog = pygame.image.load("dog_right.png")
dog_rect = dog.get_rect()
dog_rect.x = WIDTH // 2
dog_rect.bottom = HEIGHT - 10

# Add the first burger at the top at a random location
burger = pygame.image.load("burger.png")
burger_rect = burger.get_rect()
burger_rect.x = random.randint(33, WIDTH - 33)
burger_rect.top = -50

# Main game loop
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # jget a list of all keys currently held
    keys = pygame.key.get_pressed()

    # Check to see if q to quit has been pressed
    if keys[pygame.K_q]:
        running = False

    # Move the burger
    burger_rect.y += current_burger_velocity
    burger_points = HEIGHT - burger_rect.centery
    burger_points_text = font.render(
        "Burger Points:  " + str(burger_points), True, DARK_YELLOW
    )

    # Check to see if the burger hits the bottom
    if burger_rect.bottom >= HEIGHT:
        lives -= 1
        lives_text = font.render("Lives:  " + str(lives), True, DARK_YELLOW)
        burger_rect.top = -50
        burger_rect.x = random.randint(33, WIDTH - 33)

    # Check to see if the dog eats the burger
    if dog_rect.colliderect(burger_rect):
        burgers_eaten += 1
        burgers_eaten_text = font.render(
            "Burgers Eaten:  " + str(burgers_eaten), True, DARK_YELLOW
        )
        burger_rect.top = -50
        burger_rect.x = random.randint(33, WIDTH - 33)
        score += burger_points
        score_text = font.render("Score:  " + str(score), True, DARK_YELLOW)
        current_burger_velocity += 0.5

    # Move the doggo
    if keys[pygame.K_UP] and dog_rect.top > 85:
        dog_rect.y -= current_dog_velocity
    if keys[pygame.K_DOWN] and dog_rect.bottom < HEIGHT:
        dog_rect.y += current_dog_velocity
    if keys[pygame.K_LEFT] and dog_rect.left > 0:
        dog_rect.x -= current_dog_velocity
    if keys[pygame.K_RIGHT] and dog_rect.right < WIDTH:
        dog_rect.x += current_dog_velocity

    # Check for boost
    if keys[pygame.K_SPACE] and boost > 0:
        boost -= 1
        boost_text = font.render("Boost:  " + str(boost), True, DARK_YELLOW)
        current_dog_velocity = BOOST_ACCEL
    else:
        current_dog_velocity = STARTING_DOG_VELOCITY

    # Update the HUD
    score_text = font.render("Score:  " + str(score), True, DARK_YELLOW)
    lives_text = font.render("Lives:  " + str(lives), True, DARK_YELLOW)
    burgers_eaten_text = font.render(
        "Burgers Eaten:  " + str(burgers_eaten), True, DARK_YELLOW
    )

    # Check to see if game is over
    if lives == 0:
        surface_display.blit(game_over_text, game_over_rect)
        surface_display.blit(play_again_text, play_again_rect)
        pygame.display.update()

        # Pause game until user hits a button or use quits
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.music.play(-1, 0.0)
                    lives = START_LIVES
                    boost = START_BOOST
                    current_burger_velocity = STARTING_BURGER_VELOCIY
                    score = 0
                    burgers_eaten = 0
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    # Fill the gameboard to cover up old images
    surface_display.fill(BLACK)

    # Draw a white line under the HUD
    pygame.draw.line(surface_display, WHITE, (0, 85), (WIDTH, 85), 3)

    # Blit HUD assets to the display surface
    surface_display.blit(burger_points_text, burger_points_rect)
    surface_display.blit(game_name_text, game_name_rect)
    surface_display.blit(lives_text, lives_rect)
    surface_display.blit(score_text, score_rect)
    surface_display.blit(burgers_eaten_text, burgers_eaten_rect)
    surface_display.blit(boost_text, boost_text_rect)

    # Blit image assets to the screen
    surface_display.blit(dog, dog_rect)
    surface_display.blit(burger, burger_rect)

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)

# End the game
pygame.quit()
