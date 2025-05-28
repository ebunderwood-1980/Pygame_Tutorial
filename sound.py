import pygame

# Initialize Pygame
pygame.init()

# Create a display surface
WIDTH = 800
HEIGHT = 600
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adding sounds!")

# Load sound effects
sound1 = pygame.mixer.Sound('sound_1.wav')
sound2 = pygame.mixer.Sound('sound_2.wav')

# Play the sound
sound1.play()
pygame.time.delay(2000)
sound2.play()
pygame.time.delay(2000)

# Change the volume of a sound effect
sound2.set_volume(.2)
sound2.play()

# Load background music
pygame.mixer.music.load('music.wav')

# Play and stop the music
pygame.mixer.music.play(-1, 0.0)  # -1 means play infinitely
pygame.time.delay(1000)
sound1.play()  # Plays the sound effect over the music
pygame.time.delay(5000)
pygame.mixer.music.stop()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# End the game
pygame.quit()
