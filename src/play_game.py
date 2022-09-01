# Importing libraries
import time
import pygame
import sys

# Importing files
import main as m
import obs as o
import menu_screens as menu

""" Global varaibles """
# Title size
title_size = int(85 * m.norm)
title_depth = 0

# Sub title sizes
sub_title_size = int(50 * m.norm)

# Question font
question_font = "mathjaxmath"

def play_screen():
    # Instantiate text to screen
    # OOP - inherit the text class to make a question class? Then can programme generating questions with the correct fonts etc
    # TODO
    # Making question 
    q = o.Question.make_question()
    
    # TODO - generalize the spacing between questions and the title spacing for different resolutions
    question1 = o.Question(str(q[2]), font_size=menu.title_size) 
    question2 = o.Question("x", font_size=menu.title_size, font=question_font) 
    question3 = o.Question((" + "+str(q[1])+" = "+str(q[0])), font_size=menu.title_size)

    # Layout calculations
    total_width = question1.size_of_message()[0] + question2.size_of_message()[0] + question3.size_of_message()[0]
    question_x_coord1 = (m.display_width / 2) - total_width/2
    question_x_coord2 = (m.display_width / 2) - total_width/2 + question1.size_of_message()[0]  
    question_x_coord3 = (m.display_width / 2) - total_width/2 + question2.size_of_message()[0]

    play_screen_loop = True
    while play_screen_loop:
        # Mouse button click
        Click = False

        # Checking if quit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_screen_loop = False
                pygame.display.quit()
                pygame.quit()
                sys.exit("Game Quit: x-button pressed (0)")
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    question1.make_question()
                    play_screen_loop = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit("Game Quit: temp exit (0)")


        # Filling background colour
        m.gameDisplay.fill(m.white)

        # Displaying messages
        question1.message_to_screen(question_x_coord1, title_depth)
        # + 35 is temp buffer TODO
        question2.message_to_screen(question_x_coord2, title_depth + 35)
        question3.message_to_screen(question_x_coord3, title_depth)

        pygame.display.update()
        m.clock.tick(m.FPS)
