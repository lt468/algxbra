# Importing libraries
import time
import pygame
import sys

# Importing files
import consts as c
import obs as o

# Initializing pygame
pygame.init()

""" Global variables """
# Creating screen 
gameDisplay = c.screen

# Setting title and icon
pygame.display.set_caption("algxbra")
icon = pygame.image.load("../mda/algxbra_icon.png")
pygame.display.set_icon(icon)

# Clock
clock = pygame.time.Clock()

""" Functions """
def main():
    menuScreen()

def menuScreen():
    # Title size - title size will change dependent on the scale of the width
    title_size = int(c.title_size)
    titles_font = "conthrax"
    sub_title_size = int(c.sub_title_size)

    # Instantiate text to screen
    title = o.Text("algxbra", font_size=title_size, font=titles_font) 
    play_sub_title = o.Text("play", font_size=sub_title_size, font=titles_font)
    quit_sub_title = o.Text("quit", font_size=sub_title_size, font=titles_font)
    options_sub_title = o.Text("options", font_size=sub_title_size, font=titles_font)

    # Layout calculations
    mid_x_coord_title = (c.display_width / 2) - title.size_of_message()[0]/2
    mid_x_coord_play = (c.display_width / 2) - play_sub_title.size_of_message()[0]/2
    mid_x_coord_quit = (c.display_width / 2) - quit_sub_title.size_of_message()[0]/2
    mid_x_coord_options = (c.display_width / 2) - options_sub_title.size_of_message()[0]/2

    # Layout calculations - y_coord spacing
    y_buff = 10 * c.norm
    num_sub_titles = 3
    y_available = (c.display_height - (c.title_depth + title.size_of_message()[1] + y_buff)) / num_sub_titles 
    y_coord_play = (c.title_depth + title.size_of_message()[1] + y_buff)
    y_coord_options = y_coord_play - y_buff + y_available
    y_coord_quit = y_coord_options - y_buff + y_available

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
        gameDisplay.fill(c.white)
        # Display title - makes it always be sat in the middle of the screen
        title.message_to_screen(mid_x_coord_title, c.title_depth)
        play_sub_title.message_to_screen(mid_x_coord_play, y_coord_play)
        options_sub_title.message_to_screen(mid_x_coord_options, y_coord_options)
        quit_sub_title.message_to_screen(mid_x_coord_quit, y_coord_quit)

        if play_sub_title.rect(mid_x_coord_play, y_coord_play).collidepoint(pygame.mouse.get_pos()):
            play_sub_title.color = c.gray
            if click[0] == 1:
                print("Play")
        else:
            play_sub_title.color = c.black

        if options_sub_title.rect(mid_x_coord_options, y_coord_options).collidepoint(pygame.mouse.get_pos()):
            options_sub_title.color = c.gray
        else:
            options_sub_title.color = c.black

        if quit_sub_title.rect(mid_x_coord_quit, y_coord_quit).collidepoint(pygame.mouse.get_pos()):
            quit_sub_title.color = c.gray
            if click[0] == 1:
                menuExit = True
                quit_confir()
        else:
            quit_sub_title.color = c.black

        pygame.display.update()
        clock.tick(c.FPS)
        
# Quit confirmation screen
def quit_confir():
    # Title size - title size will change dependent on the scale of the width
    title_size = int(c.title_size)
    titles_font = "conthrax"
    sub_title_size = int(c.sub_title_size)
    sub_title_size_2 = int(c.sub_title_size_2)

    # Instantiate text to screen
    title = o.Text("algxbra", font_size=title_size, font=titles_font) 
    conf_sub_title = o.Text("are you sure you want to quit?", font_size=sub_title_size_2, font=titles_font)
    quit_sub_title = o.Text("quit", font_size=sub_title_size, font=titles_font)
    back_sub_title = o.Text("back", font_size=sub_title_size, font=titles_font)

    # Layout calculations
    mid_x_coord_title = (c.display_width / 2) - title.size_of_message()[0]/2
    mid_x_coord_conf = (c.display_width / 2) - conf_sub_title.size_of_message()[0]/2
    mid_x_coord_quit = (c.display_width / 2) - quit_sub_title.size_of_message()[0]/2
    mid_x_coord_back = (c.display_width / 2) - back_sub_title.size_of_message()[0]/2

    # Layout calculations - y_coord spacing
    y_buff = 10 * c.norm
    num_sub_titles = 3
    y_available = (c.display_height - (c.title_depth + title.size_of_message()[1] + y_buff)) / num_sub_titles 
    y_coord_conf = (c.title_depth + title.size_of_message()[1] + y_buff)
    y_coord_back = y_coord_conf - y_buff + y_available
    y_coord_quit = y_coord_back - y_buff + y_available

    # TODO in future, fix this issue of the instant quit!
    time.sleep(1)
    quit_confExit = False
    while not quit_confExit:
        # Mouse button click
        click = pygame.mouse.get_pressed()

        # Checking if quit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_confExit = True
                pygame.display.quit()
                pygame.quit()
                sys.exit("Game Quit: x-button pressed (0)")

        # Filling background colour
        gameDisplay.fill(c.white)
        # Display title - makes it always be sat in the middle of the screen
        title.message_to_screen(mid_x_coord_title, c.title_depth)
        conf_sub_title.message_to_screen(mid_x_coord_conf, y_coord_conf)
        back_sub_title.message_to_screen(mid_x_coord_back, y_coord_back)
        quit_sub_title.message_to_screen(mid_x_coord_quit, y_coord_quit)

        if back_sub_title.rect(mid_x_coord_back, y_coord_back).collidepoint(pygame.mouse.get_pos()):
            back_sub_title.color = c.gray
            if click[0] == 1:
                menuScreen()
        else:
            back_sub_title.color = c.black

        if quit_sub_title.rect(mid_x_coord_quit, y_coord_quit).collidepoint(pygame.mouse.get_pos()):
            quit_sub_title.color = c.gray
            if click[0] == 1:
                quit_confExit = True
                pygame.display.quit()
                pygame.quit()
                sys.exit("Game Quit: quit button pressed (0)")
        else:
            quit_sub_title.color = c.black

        pygame.display.update()
        clock.tick(c.FPS)


# Starting program
if __name__ == "__main__":
    main()

