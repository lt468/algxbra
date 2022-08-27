# TODO which are actually global variables and are needed by all files
# Importing libraries
import math
import pygame

""" Constants """

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)

# FPS
FPS = 30

# Display size
display_width_default = 854 
display_height_default = 480

display_width = display_width_default
display_height = display_height_default
dim = (display_width, display_height)

# Creating screen  
screen = pygame.display.set_mode(dim)

""" Font sizes (default is for 854px x 480px) """
# Normalization constant
norm = math.sqrt(((display_width / display_width_default) ** 2) + ((display_height / display_height_default) ** 2))
# Title size
title_size = 85 * norm 
title_depth = 0

# Sub title sizes
sub_title_size = 50 * norm
sub_title_size_2 = 28 * norm

