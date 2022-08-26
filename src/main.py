# Importing libraries
import pygame
import sys

# Importing files
import consts as c
import obs as o

# Initializing pygame
pygame.init()

# Variables
# Title size - title size will change dependent on the scale of the width
# TODO clean this up a little bit?
title_size_factor = (c.display_width / c.display_width_default)
title_size = int(c.title_size*title_size_factor)

# Creating screen 
gameDisplay = c.screen

# Setting title and icon
pygame.display.set_caption("algxbra")
icon = pygame.image.load("../mda/algxbra_icon.png")
pygame.display.set_icon(icon)

# Clcok
clock = pygame.time.Clock()

# Functions
def main():
    menuScreen()

def menuScreen():
    # Instantiate text to screen
    title = o.Text("algxbra", font_size=title_size, font="conthrax") 

    menuExit = False
    while not menuExit:

        # Checking if quit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menuExit = True
                sys.exit("Game Quit")

        # Filling background colour
        gameDisplay.fill(c.white)
        # Display title - maybe short out depth of title???
        title.message_to_screen(((c.display_width / 2) - title.size_of_message()[0]/2), c.title_depth)

        pygame.display.update()
        clock.tick(c.FPS)
        
# Starting program
if __name__ == "__main__":
    main()

# TODO add some comments and track things in the README file
