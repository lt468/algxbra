# Importing libraries
import pygame

# Initializing pygame
pygame.init()

# Creating screen of width 800px, height 600px
gameDisplay = pygame.display.set_mode((800, 600))

# Setting title and icon
pygame.display.set_caption("algxbra")
icon = pygame.image.load("../mda/algxbra_icon.png")
pygame.display.set_icon(icon)

menuScreen = True

while menuScreen:
    # Checking if quit button pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menuScreen = False
    pygame.display.update()
    pass
    

