# Importing libraries
import time
import pygame
import sys
# The only way I can get tkinter to work
from tkinter import *

# Importing files
import main as m
import obs as o
import play_game as play

""" Global varaibels - used by all functions in menu_screens.py """
""" Font sizes (default is for 854px x 480px) """
# Title size
title_size = int(85 * m.norm)
title_depth = 0

# Sub title sizes
sub_title_size = int(50 * m.norm)

# Title font
title_font = "conthrax"

""" Menu screen function """
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

    main_menu_loop = True
    while main_menu_loop:
        # Mouse button click
        Click = False

        # Checking if quit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu_loop = False
                quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Click = True

        # Filling background colour
        m.gameDisplay.fill(m.white)

        # Displaying messages
        title.message_to_screen(title_x_coord, title_depth)
        play_rect = play_sub_title.message_to_screen(play_x_coord, play_y_coord)
        options_rect = options_sub_title.message_to_screen(options_x_coord, options_y_coord)
        quit_rect = quit_sub_title.message_to_screen(quit_x_coord, quit_y_coord)

        if play_rect.collidepoint(pygame.mouse.get_pos()):
            play_sub_title.color = m.gray
            if Click:
                play_confir()
        else:
            play_sub_title.color = m.black

        if options_rect.collidepoint(pygame.mouse.get_pos()):
            options_sub_title.color = m.gray
        else:
            options_sub_title.color = m.black

        if quit_rect.collidepoint(pygame.mouse.get_pos()):
            quit_sub_title.color = m.gray
            if Click:
                quit_confir()
        else:
            quit_sub_title.color = m.black

        pygame.display.update()
        m.clock.tick(m.FPS)
        
""" Quit confirmation box """ 
def quit_confir():
    # So it can be accessed in other functions
    global root
    r_w = int(m.display_width/3)
    r_h = int(m.display_height/3)

    # Dimensions of box, w, h, x_coord, y_coord
    dim_string = f"{r_w}x{r_h}+{r_w}+{r_h}"
    root = Tk()
    
    # Hiding title bar
    root.overrideredirect(True)
    root.geometry(dim_string)
    root.config(bg="white")

    # Setting box attributes - TODO: make this more dynamic/varaible
    w = Label(root, text="Are you sure \nyou want to quit?", font=(title_font, 20), bg="white")
    w.pack(pady=20)

    # Buttons
    back_button = Button(root, text="Back", command=(lambda: root.destroy()), bg="black", fg="white", font=(title_font, 15))
    back_button.pack(pady=50, padx=50, side=LEFT)

    quit_button = Button(root, text="Quit", command=quit_game, bg="black", fg="white", font=(title_font, 15))
    quit_button.pack(pady=50, padx=50, side=RIGHT)

    root.mainloop()

""" Play confirmation box """ 
def play_confir():
    # So it can be accessed in other functions
    global root2
    global cease
    cease = False
    r_w = int(m.display_width/3)
    r_h = int(m.display_height/3)

    # Dimensions of box, w, h, x_coord, y_coord
    dim_string = f"{r_w}x{r_h}+{r_w}+{r_h}"
    root2 = Tk()
    
    # Hiding title bar
    root2.overrideredirect(True)
    root2.geometry(dim_string)
    root2.config(bg="white")

    # Setting box attributes - TODO: make this more dynamic/varaible
    w = Label(root2, text="Get ready...", font=(title_font, 25), bg="white")
    w.pack(pady=20, side=TOP)

    # Buttons
    back_button = Button(root2, text="Back", command=(lambda: play_back()), bg="black", fg="white", font=(title_font, 15))
    back_button.pack(pady=50, padx=50, side=BOTTOM)

    # Timer functionality
    t = 5
    start = time.time()
    t_label = Label(root2, text=count_down(t), font=(title_font, 33), bg="white", fg="red")
    t_label.pack(side=TOP)

    # TODO - maybe make this a bit more tidier
    t_label.after(1000, lambda:t_label.config(text=count_down(4)))
    t_label.after(2000, lambda:t_label.config(text=count_down(3)))
    t_label.after(3000, lambda:t_label.config(text=count_down(2)))
    t_label.after(4000, lambda:t_label.config(text=count_down(1)))
    t_label.after(5000, lambda:t_label.config(text="GO!", fg="green"))

    while not cease:
        root2.update_idletasks()
        root2.update()
        end = time.time()
        if (end - start) >= 6:
            print("Play")
            play_go()


""" Play/Back button functionality"""
def play_go():
    global cease
    cease = True
    # Fixes bug where main menu would show for a short time
    m.gameDisplay.fill(m.white)
    pygame.display.update()
    m.clock.tick(m.FPS)
    root2.destroy()
    # Calls the game
    play.play_screen()


""" Play/Back button functionality"""
def play_back():
    global cease
    cease = True
    root2.destroy()

""" Count down timer funciton """
def count_down(t):
    return("{:01d}".format(t))

""" General quit game function """
def quit_game():
    pygame.display.quit()
    pygame.quit()
    sys.exit("Game Quit (0)")

