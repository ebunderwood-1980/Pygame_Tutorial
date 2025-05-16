import pygame

#Initialize Pygame
pygame.init()

#Create a display surface and set its caption
WIDTH = 600
HEIGHT = 300
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello World")

#Define colors as RGB tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

#Give a background color to the display
display_surface.fill(GREEN)

#Draw various shapes on the display surface
#Line(surface, color, starting point, ending point, thickness)
pygame.draw.line(display_surface, RED, (0,0), (90, 90), 5)
#Circle(surface, color, center, radius, thickness 0 for fill)
pygame.draw.circle(display_surface, YELLOW, (WIDTH//2, HEIGHT//2), 60, 0)  #Filled circle
pygame.draw.circle(display_surface, WHITE, (100, 100), 50, 5)  #Circle with 5pt. white line

#Main game loop
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    #Update the display, always should happen at the end of the game loop
    pygame.display.update()

#End the game
pygame.quit()
