""" The file that runs the main menu screen and other screens for now"""
# Importing libraries
import pygame as pg
import sys
import time
import sqlite3

# Importing files
import math_questions as mq

# Initializing pygame
pg.init()

""" Global variables """

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
 
# Difficulty
difficulty = "easy"

# Default Display size
display_width_default = 1280
display_height_default = 720

# Test display sizes
display_w_test = 854
display_h_test = 480

# Display resolutions
# 2160p: 3840×2160
# 1440p: 2560×1440
# 1080p: 1920×1080
# 720p: 1280×720
# 480p: 854×480
# 360p: 640×360
# 240p: 426×240

# Gets the native display width and height
display_w_native, display_h_native = pg.display.Info().current_w, pg.display.Info().current_h
# Dimensions of the screen into a list 
dim = [display_w_native, display_h_native]

# Creating screen 
screen_display = pg.display.set_mode((display_w_native, display_h_native))

# Scaling factors
width_scaling_factor = display_w_native / display_width_default
height_scaling_factor = display_h_native / display_height_default
average_scaling_factor = (width_scaling_factor + height_scaling_factor) / 2

# Setting title_text and icon
pg.display.set_caption("algxbra") 
icon = pg.image.load("../mda/algxbra_icon.png") 
pg.display.set_icon(icon)

# Fonts and sizes (everything based off of 1280x720)
main_font = "../mda/conthrax-sb.otf"
# Calculate the scaled font sizes for title and subtitle
title_size = int(112 * average_scaling_factor)
sub_title_size = int(86 * average_scaling_factor)
answer_size = sub_title_size
small_title_size = int(48 * average_scaling_factor)

# Clock
clock = pg.time.Clock()

""" Non-screen funcitons"""
def render_text(font_path, size, text, color, center):
    font_size = int(size * average_scaling_factor)
    font = pg.font.Font(font_path, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    screen_display.blit(text_surface, text_rect)
    return text_rect

def resetHighScores():
    # Get user high score from SQL database
    conn = sqlite3.connect("../data/highscores.db") # Connect to SQL DB
    cursor = conn.cursor() # Create a cursor
    cursor.execute(f"UPDATE highscores SET Easy=0, Medium=0, Hard=0 WHERE Name='guest'; ") # Execture a command

    # Commit and close connection to SQL DB
    conn.commit()
    cursor.close()
    conn.close()

""" Screen functions"""
def menuScreen():
    # Main menu loop
    main_menu_loop = True
    # Sets the colour first to black
    button_colour_play = black
    button_colour_opt = black
    button_colour_quit = black

    while main_menu_loop:
        # Mouse button click variable
        click = False

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

        # Filling background color
        screen_display.fill(white)

        # Title text
        render_text(main_font, title_size, "algxbra", black, (dim[0] // 2, dim[1] // 8))

        # Render the subtitles, put the center of the group of subtitles two thirds down the screen
        play_rect = render_text(main_font, sub_title_size, "play", button_colour_play, (dim[0] // 2, (dim[1]*2/3 - (3/2 * sub_title_size)) ))
        options_rect = render_text(main_font, sub_title_size, "options", button_colour_opt, (dim[0] // 2, (dim[1]*2/3) ))
        quit_rect = render_text(main_font, sub_title_size, "quit", button_colour_quit, (dim[0] // 2, (dim[1]*2/3 + (3/2 * sub_title_size)) ))

        # Play button
        if play_rect.collidepoint(pg.mouse.get_pos()):
            button_colour_play = gray
            if click:
                main_menu_loop = False
                playGame()
        else:
            button_colour_play = black

        # Options button
        if options_rect.collidepoint(pg.mouse.get_pos()):
            button_colour_opt = gray
            if click:
                main_menu_loop = False
                optionsScreen()
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

def optionsScreen():
    # Options screen loop
    options_screen_loop = True

    # Screen variables
    easy_but_colour = black
    med_but_colour = black
    hard_but_colour = black
    reset_but_colour = black
    back_but_colour = black

    # Get difficulty from SQL database
    conn = sqlite3.connect("../data/highscores.db") # Connect to SQL DB
    cursor = conn.cursor() # Create a cursor
    cursor.execute(f"SELECT * FROM mode;") # Execture a command

    global difficulty
    difficulty = cursor.fetchall()[0][0]

    # Close connection to SQL DB
    cursor.close()
    conn.close()

    match difficulty:
        case "easy":
            easy_but_colour = green
        case "medium":
            med_but_colour = green
        case "hard":
            hard_but_colour = green

    while options_screen_loop:
        # Loop variables
        click = False

        # Checking if x-button pressed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                options_screen_loop = False
                pg.display.quit()
                pg.quit()
                sys.exit("Game Quit: X-button clicked (0)")
            # If mouse button is clicked then change click to true
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Filling background colour
        screen_display.fill(white)

        # Options page text
        render_text(main_font, title_size, "options", black, (dim[0] // 2, dim[1] //8))
        
        # Difficulty
        render_text(main_font, sub_title_size, "select difficulty", black, (dim[0] // 2, 3 * dim[1]  // 8))

        easy_but = render_text(main_font, small_title_size, "easy", easy_but_colour, (dim[0] // 6, dim[1] // 2))
        med_but = render_text(main_font, small_title_size, "medium", med_but_colour, (3 * dim[0] // 6, dim[1] // 2))
        hard_but = render_text(main_font, small_title_size, "hard", hard_but_colour, (5 *dim[0] // 6, dim[1] // 2))

        # Reset highscores
        reset_but = render_text(main_font, small_title_size, "click to reset highscores", reset_but_colour, (dim[0] // 2, 11 * dim[1]  // 16))

        # Back button
        back_but = render_text(main_font, sub_title_size, "back", back_but_colour, (dim[0] // 2, (dim[1]*2/3 + (3/2 * sub_title_size)) ))

        # Buton interactivity
        if easy_but.collidepoint(pg.mouse.get_pos()):
            easy_but_colour = gray
            if click:
                difficulty = "easy"
        elif difficulty == "easy":
            easy_but_colour = green
            med_but_colour = black
            hard_but_colour = black

        if med_but.collidepoint(pg.mouse.get_pos()):
            med_but_colour = gray
            if click:
                difficulty = "medium"
        elif difficulty == "medium":
            med_but_colour = green
            easy_but_colour = black
            hard_but_colour = black

        if hard_but.collidepoint(pg.mouse.get_pos()):
            hard_but_colour = gray
            if click:
                difficulty = "hard"
        elif difficulty == "hard":
            hard_but_colour = green
            easy_but_colour = black
            med_but_colour = black

        if reset_but.collidepoint(pg.mouse.get_pos()):
            reset_but_colour = gray
            if click:
                options_screen_loop = False
                resetConfirmation()
        else:
            reset_but_colour = black

        if back_but.collidepoint(pg.mouse.get_pos()):
            back_but_colour = gray
            if click:
                options_screen_loop = False
                menuScreen()
        else:
            back_but_colour = black

        # Updating screen
        pg.display.update()
        clock.tick(FPS)

def resetConfirmation():
    # Reset confirmation screen loop
    reset_conf = True

    yes_but_colour = red
    no_but_colour = black

    reset_done = False
    
    while reset_conf:
        # Loop variables
        click = False

        # Checking if x-button pressed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                reset_conf = False
                pg.display.quit()
                pg.quit()
                sys.exit("Game Quit: X-button clicked (0)")
            # If mouse button is clicked then change click to true
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Filling background colour
        screen_display.fill(white)
        
        # Confirmation
        render_text(main_font, small_title_size, "are you sure you want", black, (dim[0] // 2, 3 * dim[1]  // 8))
        render_text(main_font, small_title_size, "to reset all highscores?", black, (dim[0] // 2, 4 * dim[1]  // 8))

        yes_but = render_text(main_font, small_title_size, "reset", yes_but_colour, (dim[0] // 6, 2 * dim[1] // 3))
        no_but = render_text(main_font, small_title_size, "back", no_but_colour, (5 *dim[0] // 6, 2 * dim[1] // 3))

        # Buton interactivity
        if yes_but.collidepoint(pg.mouse.get_pos()):
            yes_but_colour = gray
            if click:
                reset_done = True
                resetHighScores()
        elif reset_done:
            yes_but_colour = green
        else:
            yes_but_colour = red

        if no_but.collidepoint(pg.mouse.get_pos()):
            no_but_colour = gray
            if click:
                reset_conf = False
                optionsScreen()
        else:
            no_but_colour = black

        # Updating screen
        pg.display.update()
        clock.tick(FPS)

def playGame():
    # Play game loop
    play_game_loop = True

    # Sets the colour first to black of the buttons
    ans_one_colour = black
    ans_two_colour = black
    ans_three_colour = black
    ans_four_colour = black
    timer_colour = black

    # Game variables
    new_question = True
    score = 0
    game_length = 10

    # Get the question data - get one first no matter the loop
    # Formt is (x, y, ans, opts): (int, int, int, list[4])
    x, y, ans, opts = mq.question_generator_easy()

    # Time for the game length
    time_start = int(time.time())
    time_end = time_start + game_length

    while play_game_loop:
        # Loop variables
        click = False

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

        # Timer text
        time_now = int(time.time())
        time_remaining = str(int(time_end - time_now))

        if int(time_remaining) <= 0:
            play_game_loop = False
            gameOver(score)
        elif int(time_remaining) <= 5:
            timer_colour = red

        if new_question:
            new_question = False
            x, y, ans, opts = mq.question_generator_easy()

        # Filling background colour
        screen_display.fill(white)

        # Question text
        question_string = f"x + {y} = {ans}"
        render_text(main_font, title_size, question_string, black, (dim[0] // 2, dim[1] //8))
        
        # Answers text (from the bottom up)
        ans_four_string = f"x = {opts[3]}"
        ans_four_rect = render_text(main_font, answer_size, ans_four_string, ans_four_colour, (dim[0] // 2, (dim[1] * 13) // 16))
        ans_three_string = f"x = {opts[2]}"
        ans_three_rect = render_text(main_font, answer_size, ans_three_string, ans_three_colour, (dim[0] // 2, (dim[1] * 13) // 16 - (3 // 2 * answer_size) - ans_four_rect.height // 3))
        ans_two_string = f"x = {opts[1]}"
        ans_two_rect = render_text(main_font, answer_size, ans_two_string, ans_two_colour, (dim[0] // 2, (dim[1] * 13) // 16 - (3 // 2 * answer_size * 2) - 2 * ans_four_rect.height // 3))
        ans_one_string = f"x = {opts[0]}"
        ans_one_rect = render_text(main_font, answer_size, ans_one_string, ans_one_colour, (dim[0] // 2, (dim[1] * 13) // 16 - (3 // 2 * answer_size * 3) - 3 * ans_four_rect.height // 3))
        
        # Score text - do it in two parts so the text stops jumping every time the score changes
        score_static_rect = render_text(main_font, small_title_size, f"score: ", black, (dim[0] * 2 // 15, dim[1]*13//14))
        render_text(main_font, small_title_size, f"   {score}", black, (score_static_rect.x + score_static_rect.width, dim[1]*13//14))

        # Timer string - do it in two parts so the text stops jumping every second
        # The score rect should be the same(ish) size to the timer rect
        timer_static_rect = render_text(main_font, small_title_size, f"timer: ", black, (dim[0] - score_static_rect.width, dim[1]*13//14))
        render_text(main_font, small_title_size, f"   {time_remaining[:2]}", timer_colour, (timer_static_rect.x + timer_static_rect.width, dim[1]*13//14))

        # Buton interactivity
        if ans_one_rect.collidepoint(pg.mouse.get_pos()):
            ans_one_colour = gray
            if click:
                if opts[0] == x:
                    score += 1
                    new_question = True
                else:
                    score -= 1
        else:
            ans_one_colour = black

        if ans_two_rect.collidepoint(pg.mouse.get_pos()):
            ans_two_colour = gray
            if click:
                if opts[1] == x:
                    score += 1
                    new_question = True
                else:
                    score -= 1
        else:
            ans_two_colour = black

        if ans_three_rect.collidepoint(pg.mouse.get_pos()):
            ans_three_colour = gray
            if click:
                if opts[2] == x:
                    score += 1
                    new_question = True
                else:
                    score -= 1
        else:
            ans_three_colour = black

        if ans_four_rect.collidepoint(pg.mouse.get_pos()):
            ans_four_colour = gray
            if click:
                if opts[3] == x:
                    score += 1
                    new_question = True
                else:
                    score -= 1
        else:
            ans_four_colour = black

        # Updating screen
        pg.display.update()
        clock.tick(FPS)

def gameOver(user_score):
    # Game over screen loop
    game_over_loop = True

    # Variables for the screen
    score_colour = black
    button_colour_play_again = black
    button_colour_main_menu = black

    # Get user high score from SQL database
    conn = sqlite3.connect("../data/highscores.db") # Connect to SQL DB
    cursor = conn.cursor() # Create a cursor
    cursor.execute(f"SELECT {difficulty} FROM highscores WHERE Name='guest';") # Execture a command
    result = cursor.fetchall()
    highscore = result[0][0]

    # Seeing if user beat highscore and changes colour of text accordingly
    if user_score > highscore:
        highscore = user_score
        cursor.execute(f"UPDATE highscores SET {difficulty} = ? WHERE Name = 'guest';", (highscore,))
        score_colour = green
    elif user_score == highscore:
        score_colour = blue

    # Commit and close connection to SQL DB
    conn.commit()
    cursor.close()
    conn.close()

    while game_over_loop:
        # Loop variables
        click = False

        # Checking if x-button pressed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over_loop = False
                pg.display.quit()
                pg.quit()
                sys.exit("Game Quit: X-button clicked (0)")
            # If mouse button is clicked then change click to true
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Filling background colour
        screen_display.fill(white)

        # Game over text
        render_text(main_font, title_size, "Game over", black, (dim[0] // 2, dim[1] // 8))

        # Score and high score text
        render_text(main_font, sub_title_size, f"score: {user_score}", score_colour, (dim[0] // 2, 3*dim[1] // 8))
        render_text(main_font, answer_size, f"high score: {highscore}", blue, (dim[0] // 2, dim[1] // 2))

        play_again_rect = render_text(main_font, sub_title_size, "play again", button_colour_play_again, (dim[0] // 2, (dim[1]*2/3)))
        menu_screen_rect = render_text(main_font, sub_title_size, "main menu", button_colour_main_menu, (dim[0] // 2, (dim[1]*2/3 + (3/2 * sub_title_size))))

        # Play again button
        if play_again_rect.collidepoint(pg.mouse.get_pos()):
            button_colour_play_again = gray
            if click:
                game_over_loop = False
                playGame()
        else:
            button_colour_play_again = black

        # Main menu button
        if menu_screen_rect.collidepoint(pg.mouse.get_pos()):
            button_colour_main_menu = gray
            if click:
                game_over_loop = False
                menuScreen()
        else:
            button_colour_main_menu = black

        # Updating screen
        pg.display.update()
        clock.tick(FPS)


""" Run programme"""
if __name__ == "__main__":
    menuScreen()
