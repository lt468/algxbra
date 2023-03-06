#Importing libraries
import pygame as pg
import math
import sys

# Initializing pygame
pg.init()

""" Global variables """
# Display resolutions
# 2160p: 3840×2160
# 1440p: 2560×1440
# 1080p: 1920×1080
# 720p: 1280×720
# 480p: 854×480
# 360p: 640×360
# 240p: 426×240

""" Constants """
# Colours
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)

# FPS
FPS = 30

# Fonts
title_font = pg.font.Font("../mda/conthrax-sb.otf", 92)
sub_title_font = pg.font.Font("../mda/conthrax-sb.otf", 64)
math_font_let = pg.font.Font("../mda/MathJax_Main-Regular.otf", 32)
math_font_let = pg.font.Font("../mda/MathJax_Math-Regular.otf", 32)

# Display size
display_width_default = 854 
display_height_default = 480

# Get the size of the monitor
fetch_dim = pg.display.Info()

display_width_native = fetch_dim.current_w # Gets the width
display_height_native = fetch_dim.current_h # Gets the height

# Sets the display width and heigth to the default values
# Replace with native to have fullscreen windowed mode
display_width = display_width_default 
display_height = display_height_default
#test

# Dimensions
dim = (display_width, display_height)
dim_halved = ((display_width // 2), (display_height // 2))
mid_of_screen = (int((display_width_native / 2)), int((display_height_native / 2)))
sub_titles_dim = (dim_halved[1], dim_halved[1] + (dim_halved[1] // 3), dim_halved[1] + (dim_halved[1]*2 // 3) )


# Normalization - TODO with magnitudes and vector normalization
# mag = math.sqrt(((display_width / display_width_default) ** 2) + ((display_height / display_height_default) ** 2))

# Creating screen 
game_display = pg.display.set_mode(dim)

# Setting title_text and icon
pg.display.set_caption("algxbra") 
icon = pg.image.load("../mda/algxbra_icon.png") # TODO: can round off logo to make it more aesthetic in the future
pg.display.set_icon(icon)

# Clock
clock = pg.time.Clock()

""" Menu screen function """
def menuScreen():
    # Title text
    title_text = title_font.render("algxbra", True, black)
    title_rect = title_text.get_rect()
    title_rect.center = (display_width // 2, display_height // 8)

    # Play text
    play_text = sub_title_font.render("play", True, black)
    play_rect = play_text.get_rect()
    play_rect.center = (display_width // 2, sub_titles_dim[0])

    # options text
    options_text = sub_title_font.render("options", True, black)
    options_rect = options_text.get_rect()
    options_rect.center = (display_width // 2, sub_titles_dim[1])

    # quit text
    quit_text = sub_title_font.render("quit", True, black)
    quit_rect = quit_text.get_rect()
    quit_rect.center = (display_width // 2, sub_titles_dim[2])

    # Main menu loop
    main_menu_loop = True
    while main_menu_loop:
        # Mouse button click
        Click = False

        # Checking if quit button pressed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                main_menu_loop = False
                pg.display.quit()
                pg.quit()
                sys.exit("Game Quit: X-button clicked (0)")
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Click = True

        # Filling background colour
        game_display.fill(white)

        # Title and texts display
        game_display.blit(title_text, title_rect)
        game_display.blit(play_text, play_rect)
        game_display.blit(options_text, options_rect)
        game_display.blit(quit_text, quit_rect)

        # Updating screen
        pg.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    menuScreen()
