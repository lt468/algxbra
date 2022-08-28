# Importing libraries
import pygame
import sys

# Importing files
import main as m
import obs as o

""" Global varaibels - used by all functions in menu_screens.py """
""" Font sizes (default is for 854px x 480px) """
# Title size
title_size = int(85 * m.norm)
title_depth = 0

# Sub title sizes
sub_title_size = int(50 * m.norm)

# Title font
title_font = "conthrax"

def menuScreen():
    # Instantiate text to screen
    title = o.Text("algxbra", font_size=title_size, font=title_font) 
    play_sub_title = o.Text("play", font_size=sub_title_size, font=title_font)
    options_sub_title = o.Text("options", font_size=sub_title_size, font=title_font)
    quit_sub_title = o.Text("quit", font_size=sub_title_size, font=title_font)

    # Layout calculations
    title_x_coord = (m.display_width / 2) - title.size_of_message()[0]/2
    play_x_coord = (m.display_width / 2) - play_sub_title.size_of_message()[0]/2
    options_x_coord = (m.display_width / 2) - options_sub_title.size_of_message()[0]/2
    quit_x_coord = (m.display_width / 2) - quit_sub_title.size_of_message()[0]/2

    # Layout calculations - y_coord spacing
    y_buff = int(10 * m.norm)
    num_sub_titles = 3
    available_y = (m.display_height - (title_depth + title.size_of_message()[1] + y_buff)) / num_sub_titles 
    play_y_coord = (title_depth + title.size_of_message()[1] + y_buff)
    options_y_coord = play_y_coord - y_buff + available_y
    quit_y_coord = options_y_coord - y_buff + available_y

    menuExit = False
    while not menuExit:
        # Mouse button click
        click = pygame.mouse.get_pressed()

        # Checking if quit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menuExit = True
                pygame.display.quit()
                pygame.quit()
                sys.exit("Game Quit: x-button pressed (0)")

        # Filling background colour
        m.gameDisplay.fill(m.white)

        # Displaying messages
        title.message_to_screen(title_x_coord, title_depth, return_val=False)
        play_rect = play_sub_title.message_to_screen(play_x_coord, play_y_coord)
        options_rect = options_sub_title.message_to_screen(options_x_coord, options_y_coord)
        quit_rect = quit_sub_title.message_to_screen(quit_x_coord, quit_y_coord)

        if play_rect.collidepoint(pygame.mouse.get_pos()):
            play_sub_title.color = m.gray
            if click[0] == 1:
                print("Play")
        else:
            play_sub_title.color = m.black

        if options_rect.collidepoint(pygame.mouse.get_pos()):
            options_sub_title.color = m.gray
        else:
            options_sub_title.color = m.black

        if quit_rect.collidepoint(pygame.mouse.get_pos()):
            quit_sub_title.color = m.gray
            if click[0] == 1:
                menuExit = True
                pygame.display.quit()
                pygame.quit()
                sys.exit("Game Quit: quit button pressed (0)")
        else:
            quit_sub_title.color = m.black

        pygame.display.update()
        m.clock.tick(m.FPS)
        

