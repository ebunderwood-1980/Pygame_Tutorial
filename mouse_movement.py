import pygame

# Initialize Pygame
pygame.init()

# Create game window
W = 1600
H = 1200
C = (0, 0, 0)
game_board = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mouse Movement")

# Set game values
V = 20  

# Load images
dragon1 = pygame.image.load("dragon_right.png")
dragon_rect =dragon1.get_rect()
dragon_rect.centerx = W//2
dragon_rect.bottom = H//2

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

# Move the dragon to the point on the screen where the mouse clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            dragon_rect.centerx = mouseX
            dragon_rect.centery = mouseY

# Move the dragon to follow the mouse only if the left click is depressed
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            dragon_rect.centerx = mouseX
            dragon_rect.centery = mouseY
            
# Fill display surgace to cover up old images
    game_board.fill(C)

# Blit assets to the screen
    game_board.blit(dragon1, dragon_rect)
    
# Update the display
    pygame.display.update()

# Exit pygame
pygame.quit()
