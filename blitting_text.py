import pygame

# Initialize Pygame
pygame.init()

# Create a display surface
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption( "Blitting Text" )

# Define Colors
GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
BLACK = (0, 0, 0)

# See all available System Fonts
fonts = pygame.font.get_fonts()
for font in fonts:
    print(font)

# Define Fonts
system_font = pygame.font.SysFont('calibri', 64)
custom_font = pygame.font.Font('AttackGraffiti.ttf', 32)

# Define Text
system_text = system_font.render("Dragons Rule", True, GREEN, DARK_GREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

custom_text = custom_font.render("Move the dragon soon", True, GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit (copy) to display surface
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)

    # Update the display
    pygame.display.update()

# End the game
pygame.quit()
