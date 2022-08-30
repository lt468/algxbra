# Importing libraries
import pygame
import math

# Importing files
import menu_screens as menu

# Initializing pygame
pygame.init()

""" Global variables """
# Display size
display_width_default = 854 
display_height_default = 480

# Get the size of the monitor
fetchDim = pygame.display.Info()

display_width = fetchDim.current_w
display_height = fetchDim.current_h
dim = (display_width, display_height)

# Normalization constant
norm = math.sqrt(((display_width / display_width_default) ** 2) + ((display_height / display_height_default) ** 2))

# Creating screen 
gameDisplay = pygame.display.set_mode(dim, pygame.FULLSCREEN)

# Setting title and icon
pygame.display.set_caption("algxbra")
icon = pygame.image.load("../mda/algxbra_icon.png")
pygame.display.set_icon(icon)

# Clock
clock = pygame.time.Clock()

""" Constants """
# Colours
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)

# FPS
FPS = 30

def main():
    menu.menuScreen()

if __name__ == "__main__":
    main()
