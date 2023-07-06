""" The file that runs the main menu screen and other screens for now"""

# Importing libraries
import pygame as pg
import sys
import time
import csv

# Importing files
import math_questions as mq

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
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Fonts and sizes (everything based off of 1280x720)
main_font = "../mda/conthrax-sb.otf"
title_size = 96
sub_title_size = 72

# FPS
FPS = 30

# Default Display size
display_width_default = 1280
display_height_default = 720

# Gets the native display width and height
display_w_native, display_h_native = pg.display.Info().current_w, pg.display.Info().current_h

# Creating screen 
screen_display = pg.display.set_mode((1280,720))

# Dimensions of the screen into a list - Maybe redundant - TODO
dim = list(screen_display.get_size())

# Target width and heighgts, will be the native ones in the future - TODO
target_width = display_width_default
target_height = display_height_default

# Scaling factors
width_scaling_factor = target_width / 1280
height_scaling_factor = target_height / 720
average_scaling_factor = (width_scaling_factor + height_scaling_factor) / 2

# Setting title_text and icon
pg.display.set_caption("algxbra") 
icon = pg.image.load("../mda/algxbra_icon.png") 
pg.display.set_icon(icon)

# Clock
clock = pg.time.Clock()

""" Non-screen funcitons"""
def render_text(font_path, size, text, color, center, scaling_factor=1.0):
    font_size = int(size * average_scaling_factor * scaling_factor)
    font = pg.font.Font(font_path, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    screen_display.blit(text_surface, text_rect)
    return text_rect

""" Screen functions"""
def menuScreen():
    # Main menu loop
    main_menu_loop = True
    # List to track the rectangles of each button
    button_rects = []
    # Sets the colour first to black
    button_colour_play = black
    button_colour_opt = black
    button_colour_quit = black

    while main_menu_loop:
        # Mouse button click variable
        click = False

        # Filling background color
        screen_display.fill(white)

        # Title text
        render_text(main_font, title_size, "algxbra", black, (dim[0] // 2, dim[1] // 8))

        # Render the subtitles
        play_rect = render_text(main_font, sub_title_size, "play", button_colour_play, (dim[0] // 2, (dim[1]*2/3 - (3/2 * sub_title_size)) ))
        button_rects.append(play_rect)

        options_rect = render_text(main_font, sub_title_size, "options", button_colour_opt, (dim[0] // 2, (dim[1]*2/3) ))
        button_rects.append(options_rect)

        quit_rect = render_text(main_font, sub_title_size, "quit", button_colour_quit, (dim[0] // 2, (dim[1]*2/3 + (3/2 * sub_title_size)) ))
        button_rects.append(quit_rect)

        # Buton interactivity

        # Checking if x-button pressed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                main_menu_loop = False
                pg.display.quit()
                pg.quit()
                sys.exit("Game Quit: X-button clicked (0)")
            # If mouse button is clicked then change click to true
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Play button
        if play_rect.collidepoint(pg.mouse.get_pos()):
            button_colour_play = gray
            if click:
                pass
        else:
            button_colour_play = black

        # Options button
        if options_rect.collidepoint(pg.mouse.get_pos()):
            button_colour_opt = gray
        else:
            button_colour_opt = black

        # Quit button
        if quit_rect.collidepoint(pg.mouse.get_pos()):
            button_colour_quit = gray
            if click:
                main_menu_loop = False
                pg.display.quit()
                pg.quit()
                sys.exit("Game Quit: quit button clicked (0)")
        else:
            button_colour_quit = black


        # Updating screen
        pg.display.update()
        clock.tick(FPS)

# Run programme
if __name__ == "__main__":
    menuScreen()
