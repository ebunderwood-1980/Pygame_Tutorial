import pygame

# Initializing Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setting up the window
WIDTH = 800
HEIGHT = 600
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Test of Text and Images")
display_surface.fill(BLACK)

# Setting up the Dragon
dragon_image = pygame.image.load("dragon_left.png")
dragon_image_right = pygame.image.load("dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_right_rect = dragon_image_right.get_rect()
dragon_rect.center = (WIDTH//2 - 200, HEIGHT//2)
dragon_right_rect.center = (WIDTH//2 + 200, HEIGHT//2)

# Setting up the font
dragon_font = pygame.font.Font('AttackGraffiti.ttf', 45)
dragon_text = dragon_font.render("DRAGON RAGE", True, GREEN)
dragon_text_rect = dragon_text.get_rect()
dragon_text_rect.center = (WIDTH//2, HEIGHT//2)

# Setting up the rectangle
pygame.draw.rect(display_surface, BLUE, (WIDTH//2 - 260, HEIGHT//2 - 50, 520, 100))

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display text
    display_surface.blit(dragon_text, dragon_text_rect)
    
    # Display the dragon
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(dragon_image_right, dragon_right_rect)
        
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
