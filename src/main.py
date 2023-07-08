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

# FPS
FPS = 30

# Display size
display_width_default = 854 
display_height_default = 480

# Get the size of the monitor
fetch_dim = pg.display.Info()

display_width_native = fetch_dim.current_w # Gets the width
display_height_native = fetch_dim.current_h # Gets the height

# Sets the display width and heigth to the default values
# Replace with native to have fullscreen windowed mode
display_width = display_width_native
display_height = display_height_native

# Dimensions
dim = [display_width, display_height]
dim_halved = ((display_width // 2), (display_height // 2))
mid_of_screen = (int((display_width_native / 2)), int((display_height_native / 2)))
sub_titles_dim = (dim_halved[1], dim_halved[1] + (dim_halved[1] // 3), dim_halved[1] + (dim_halved[1]*2 // 3) )

# Scaling
width_scaling_factor = display_width_native / 480
height_scaling_factor = display_height_native / 854
average_scaling_factor = (width_scaling_factor + height_scaling_factor) / 2

# Fonts
title_font = pg.font.Font("../mda/conthrax-sb.otf", int(72 * average_scaling_factor))
title2_font = pg.font.Font("../mda/conthrax-sb.otf", int(48 * average_scaling_factor))
title3_font = pg.font.Font("../mda/conthrax-sb.otf", int(32 * average_scaling_factor))

# Creating screen 
screen_display = pg.display.set_mode((1280,720))

# Setting title_text and icon
pg.display.set_caption("algxbra") 
icon = pg.image.load("../mda/algxbra_icon.png") 
pg.display.set_icon(icon)

# Clock
clock = pg.time.Clock()

""" Menu screen function """
def menuScreen():
    # Sets the colour first to black
    sub_title_colour_play = black
    sub_title_colour_opt = black
    sub_title_colour_quit = black

    # Main menu loop
    main_menu_loop = True
    while main_menu_loop:
        # Mouse button click variable
        click = False

        # Title text
        title_text = title_font.render("algxbra", True, black)
        title_rect = title_text.get_rect()
        title_rect.center = (display_width // 2, display_height // 8)

        # Play text
        play_text = title2_font.render("play", True, sub_title_colour_play)
        play_rect = play_text.get_rect()
        play_rect.center = (display_width // 2, sub_titles_dim[0])

        # options text
        options_text = title2_font.render("options", True, sub_title_colour_opt)
        options_rect = options_text.get_rect()
        options_rect.center = (display_width // 2, sub_titles_dim[1])

        # quit text
        quit_text = title2_font.render("quit", True, sub_title_colour_quit)
        quit_rect = quit_text.get_rect()
        quit_rect.center = (display_width // 2, sub_titles_dim[2])

        # Filling background colour
        screen_display.fill(white)

        # Title and texts display
        screen_display.blit(title_text, title_rect)
        screen_display.blit(play_text, play_rect)
        screen_display.blit(options_text, options_rect)
        screen_display.blit(quit_text, quit_rect)

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

        # Buton interactivity
        # Play button
        if play_rect.collidepoint(pg.mouse.get_pos()):
            sub_title_colour_play = gray
            if click:
                main_menu_loop = False
                playGame()
        else:
            sub_title_colour_play = black
        # Options button
        if options_rect.collidepoint(pg.mouse.get_pos()):
            sub_title_colour_opt = gray
        else:
            sub_title_colour_opt = black
        # Quit button
        if quit_rect.collidepoint(pg.mouse.get_pos()):
            sub_title_colour_quit = gray
            if click:
                main_menu_loop = False
                pg.display.quit()
                pg.quit()
                sys.exit("Game Quit: quit button clicked (0)")
        else:
            sub_title_colour_quit = black

        # Updating screen
        pg.display.update()
        clock.tick(FPS)

def playGame():
    # Function variables
    answer_one_color = black
    answer_two_color = black
    answer_three_color = black
    answer_four_color = black

    new_question = True
    play_game_loop = True
    score = 0
    game_length = 10

    # Get the question data - get one first no matter the loop
    # Formt is (x, y, ans, opts): (int, int, int, list[4])
    x, y, ans, opts = mq.question_generator()

    time_start = int(time.time())
    time_end = time_start + game_length

    bottom_y_pad = int(20 * average_scaling_factor)

    while play_game_loop:
        # Timer text
        time_now = int(time.time())
        time_remaining = str(int(time_end - time_now))

        if int(time_remaining) <= 0:
            play_game_loop = False
            screen_display.fill(white)
            endScreen(score)

        if new_question:
            # Get the question data
            # Formt is (x, y, ans, opts): (int, int, int, list[4])
            new_question = False
            x, y, ans, opts = mq.question_generator()

        # Loop variables
        click = False

        # Title text
        question_string = f"x + {y} = {ans}"
        question_text = title_font.render(question_string, True, black)
        question_rect = question_text.get_rect()
        question_rect.center = (display_width // 2, display_height // 8)

        # Computing the available y-space
        bottom_y = question_rect[1] + question_rect[3] + int(bottom_y_pad * average_scaling_factor)
        spare_y = display_height - bottom_y
        y_locations = [bottom_y, bottom_y + ((spare_y // 4)*1), bottom_y + ((spare_y // 4)*2), bottom_y + ((spare_y // 4)*3)]

        # Answers text
        answer_one_string = f"x = {opts[0]}"
        answer_one_text = title2_font.render(answer_one_string, True, answer_one_color)
        answer_one_rect = answer_one_text.get_rect()
        answer_one_rect.center = (display_width // 2, y_locations[0])

        answer_two_string = f"x = {opts[1]}"
        answer_two_text = title2_font.render(answer_two_string, True, answer_two_color)
        answer_two_rect = answer_two_text.get_rect()
        answer_two_rect.center = (display_width // 2, y_locations[1])

        answer_three_string = f"x = {opts[2]}"
        answer_three_text = title2_font.render(answer_three_string, True, answer_three_color)
        answer_three_rect = answer_three_text.get_rect()
        answer_three_rect.center = (display_width // 2, y_locations[2])

        answer_four_string = f"x = {opts[3]}"
        answer_four_text = title2_font.render(answer_four_string, True, answer_four_color)
        answer_four_rect = answer_four_text.get_rect()
        answer_four_rect.center = (display_width // 2, y_locations[3])

        # Score text
        score_string = f"score: {score}"
        score_text = title3_font.render(score_string, True, black)
        score_rect = score_text.get_rect()
        score_rect.x, score_rect.y = 15, display_height - score_rect[3]

        timer_string1 = f"timer: "
        timer_text1 = title3_font.render(timer_string1, True, black)
        timer_rect1 = timer_text1.get_rect()
        timer_rect1.x, timer_rect1.y = display_width - (90 + timer_rect1[2]), display_height - timer_rect1[3]

        timer_string2 = f"{time_remaining[:2]}"
        timer_text2 = title3_font.render(timer_string2, True, black)
        timer_rect2 = timer_text2.get_rect()
        timer_rect2.x, timer_rect2.y = display_width - 90, display_height - timer_rect2[3]

        # Filling background colour
        screen_display.fill(white)

        # Title and texts display
        screen_display.blit(question_text, question_rect)
        screen_display.blit(answer_one_text, answer_one_rect)
        screen_display.blit(answer_two_text, answer_two_rect)
        screen_display.blit(answer_three_text, answer_three_rect)
        screen_display.blit(answer_four_text, answer_four_rect)
        screen_display.blit(score_text, score_rect)
        screen_display.blit(timer_text1, timer_rect1)
        screen_display.blit(timer_text2, timer_rect2)

        # Checking if x-button pressed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                play_game_loop = False
                pg.display.quit()
                pg.quit()
                sys.exit("Game Quit: X-button clicked (0)")
            # If mouse button is clicked then change click to true
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Buton interactivity
        if answer_one_rect.collidepoint(pg.mouse.get_pos()):
            answer_one_color = gray
            if click:
                if opts[0] == x:
                    score += 1
                    new_question = True
                else:
                    score -= 1
        else:
            answer_one_color = black

        if answer_two_rect.collidepoint(pg.mouse.get_pos()):
            answer_two_color = gray
            if click:
                if opts[1] == x:
                    score += 1
                    new_question = True
                else:
                    score -= 1
        else:
            answer_two_color = black

        if answer_three_rect.collidepoint(pg.mouse.get_pos()):
            answer_three_color = gray
            if click:
                if opts[2] == x:
                    score += 1
                    new_question = True
                else:
                    score -= 1
        else:
            answer_three_color = black

        if answer_four_rect.collidepoint(pg.mouse.get_pos()):
            answer_four_color = gray
            if click:
                if opts[3] == x:
                    score += 1
                    new_question = True
                else:
                    score -= 1
        else:
            answer_four_color = black

        pg.display.update()
        # Updating screen
        clock.tick(FPS)

def endScreen(user_score):

    # Translation factor for the score and high score text
    shift_y = int(20 * average_scaling_factor)
    bottom_y_pad = int(20 * average_scaling_factor)

    sub_title_colour_high_score = blue
    sub_title_colour_play_again = black
    sub_title_colour_main_menu = black
    
    highscore = getHighscore()

    # Changing the end colours on the screen and saving scores
    if user_score > highscore:
        sub_title_colour_score = green
        sub_title_colour_high_score = green
        highscore = user_score

        # Saving new highscore
        with open("highscores.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'score'])
            writer.writeheader()
            writer.writerows([{'name': 'anon', 'score': user_score}])

    elif user_score < highscore:
        sub_title_colour_score = red
    else:
        sub_title_colour_score = blue

    # End screen loop
    end_screen_loop = True
    while end_screen_loop:
        # Mouse button click variable
        click = False

        # Game over text
        title_text = title_font.render("game over!", True, black)
        title_rect = title_text.get_rect()
        title_rect.center = (display_width // 2, display_height // 8)

        # Computing the available y-space
        bottom_y = title_rect[1] + title_rect[3] + bottom_y_pad
        spare_y = display_height - bottom_y
        y_locations = [bottom_y, bottom_y + ((spare_y // 4)*1), bottom_y + ((spare_y // 4)*2), bottom_y + ((spare_y // 4)*3)]

        # Score text
        score_text = title2_font.render(f"score: {user_score}", True, sub_title_colour_score)
        score_rect = score_text.get_rect()
        score_rect.center = (display_width // 2, y_locations[0] - (int(1/2 * shift_y)))

        # High score text
        high_score_text = title2_font.render(f"high score: {highscore}", True, sub_title_colour_high_score)
        high_score_rect = high_score_text.get_rect()
        high_score_rect.center = (display_width // 2, y_locations[1] - (int(3/2 * shift_y)))

        # Play again text
        play_again_text = title2_font.render("play again", True, sub_title_colour_play_again)
        play_again_rect = play_again_text.get_rect()
        play_again_rect.center = (display_width // 2, y_locations[2])

        # Main menu text
        main_menu_text = title2_font.render("main menu", True, sub_title_colour_main_menu)
        main_menu_rect = main_menu_text.get_rect()
        main_menu_rect.center = (display_width // 2, y_locations[3])

        # Filling background colour
        screen_display.fill(white)

        # Game over title and texts display
        screen_display.blit(title_text, title_rect)
        screen_display.blit(score_text, score_rect)
        screen_display.blit(high_score_text, high_score_rect)
        screen_display.blit(play_again_text, play_again_rect)
        screen_display.blit(main_menu_text, main_menu_rect)

        # Checking if x-button pressed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                end_screen_loop = False
                pg.display.quit()
                pg.quit()
                sys.exit("Game Quit: X-button clicked (0)")
            # If mouse button is clicked then change click to true
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Buton interactivity
        # Play again button
        if play_again_rect.collidepoint(pg.mouse.get_pos()):
            sub_title_colour_play_again = gray
            if click:
                end_screen_loop = False
                playGame()
        else:
            sub_title_colour_play_again = black
        # Main menu button
        if main_menu_rect.collidepoint(pg.mouse.get_pos()):
            sub_title_colour_main_menu = gray
            if click:
                end_screen_loop = False
                menuScreen()
        else: sub_title_colour_main_menu = black

        # Updating screen
        pg.display.update()
        clock.tick(FPS)

def getHighscore():
    # Read data from the CSV file
    with open("highscores.csv", mode="r") as file:
        reader = csv.DictReader(file)
        first_row = next(reader)  # Get the first row
        # Extract and return the score value
        return int(first_row["score"])

if __name__ == "__main__":
    menuScreen()
