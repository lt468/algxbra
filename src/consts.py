# Importing libraries
import pygame

""" Constants """

# Colours
white = (255, 255, 255)
black = (0, 0, 0)

# FPS
FPS = 30

# Display size
display_width_default = 854 
display_height_default = 480

display_width = 845
display_height = 480
dim = (display_width, display_height)

# Creating screen  
screen = pygame.display.set_mode(dim)

# Font sizes (default is for 854px x 480px)
title_size_factor = (display_width / display_width_default)
title_size = 100 * (display_width/display_width_default)  
title_depth = 0

