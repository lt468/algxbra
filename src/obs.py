# Importing libraries
import pygame
import sys
import random
from random import randrange
# Only way I can get tkinter to work
from tkinter import *

# Importing files
import main as m

""" Message to screen class """
class Text:
    """ Constructor """
    def __init__(self, msg:str, font_size=25, font=m.title_font, colour=(m.black), aa=True, screen=m.gameDisplay) -> None:
        # Message that is displaye on screen
        self.msg = msg
        # Size of the font
        self.__font_size = font_size
        # Font type
        self.__font = pygame.font.SysFont(font, self.__font_size)
        # Font colour
        self.color = colour
        # Font anti-aliasing
        self.__aa = aa
        # Where to display font
        self.__screen = screen

    """ Private variables """
    @property
    def font(self):
        return self.__font
    @property
    def font_size(self):
        return self.__font_size
    @property
    def aa(self):
        return self.__aa
    @property
    def screen(self):
        return self.__screen

    # Method to send the message to the screen, returns a rectangele of its coordinates
    def message_to_screen(self, x, y):
        self.screen_text = self.__font.render(self.msg, self.__aa, self.color)
        self.__screen.blit(self.screen_text, (x, y)) 
        return self.screen_text.get_rect(topleft=(x, y))

    # Method to get the size of the message
    def size_of_message(self):
        return (self.__font.size(self.msg))


""" Question class, child of Text class """
class Question(Text):
    """ Constructor """
    def __init__(self, msg: str, font_size=25, font=m.math_font_let, colour=m.black, aa=True, screen=m.gameDisplay) -> None:
        super().__init__(msg, font_size, font, colour, aa, screen)

    """ Make a question method """
    @staticmethod
    def make_question():
        # Generate answer 
        ans = randrange(10, 20)
        # Generate additive constant
        cons = randrange(1,10)
        # Ensure result is always positive 
        result = ans - cons
        if result < 0:
            result = result * -1
        # Computing all factors of ans - cons
        factors = []
        for i in range(1, result+1):
            if result % i == 0:
                factors.append(i)

        # Choose random factor to be coefficient of x
        coeff = random.choice(factors)
        # Calculating x
        x = int(result / coeff)

        # Return a tuple (answer, constant, coefficient, x = )
        if coeff == 1:
            coeff = ""
        return ((ans, cons, coeff, x))

""" Tkinter GUI class """
class Tk_gui:
    """ Constructor """
    def __init__(self, label_text:str, no_title_bar=True, bg_col="white", fg_col="black", font=m.title_font) -> None:
        # Layout calculations
        self.r_w = int((m.display_width/3) * m.norm)
        self.r_h = int((m.display_height/3) * m.norm)
        self.r_x_coord = m.mid_of_screen[0] - int(self.r_w / 2) 
        self.r_y_coord = m.mid_of_screen[1] - int(self.r_h / 2)

        # Font and colours
        self.font = font
        self.bg_col = bg_col
        self.fg_col = fg_col

        # Dimensions of box, w, h, x_coord, y_coord
        self.dim_string = f"{self.r_w}x{self.r_h}+{self.r_x_coord}+{self.r_y_coord}"

        # Making the root box (the background)
        self.root = Tk()
        
        # Basic properties
        self.root.overrideredirect(no_title_bar)
        self.root.config(bg=self.bg_col)
        self.root.geometry(self.dim_string)

        # Setting up text of box
        self.w = Label(self.root, text=label_text, font=(self.font, int(15 * m.norm**1.5)), bg=self.bg_col, fg=self.fg_col, wraplength=self.r_w, justify=CENTER)
        self.w.pack(pady=int(10 * m.norm))

    """ Desgining buttons """
    def btn(self, button_text:str, cmd, bg_col="black", fg_col="white"):
        return Button(self.root, text=button_text, command=cmd, bg=bg_col, fg=fg_col, font=(self.font, int(12 * m.norm**1.5)))

    """ Packing buttons """
    def packing_btns(self, num_of_btns:int, btns_tuple:tuple):
        if num_of_btns == 1:
            btns_tuple[0].pack(pady=int(20 * m.norm), side=BOTTOM)
        elif num_of_btns == 2:
            btns_tuple[0].pack(pady=int(20 * m.norm), padx=int(30 * m.norm), side=LEFT)
            btns_tuple[1].pack(pady=int(20 * m.norm), padx=int(30 * m.norm), side=RIGHT)
        else:
            raise Exception(f"Support not yet available for {num_of_btns} butons")
        self.root.update()
        # Return a tuple of the first button width, height
        return ((btns_tuple[0].winfo_width(), btns_tuple[0].winfo_height()))

    """ Timer label """
    def timer(self, size):
        v = Label(self.root, text="5", font=(self.font, int(20 * m.norm**1.5)), bg=self.bg_col, fg="red")
        self.w.update()
        # TODO - is there an actual way to get this centred?
        pad_y = int((int(self.r_h / 2) - self.w.winfo_height() - size[1] - v.winfo_width()) / 2)
        v.pack(pady=pad_y, side=TOP)
        # TODO Main - finish timer then do rest of TODOs

    """ Main loop """
    def main_loop(self):
        self.root.mainloop()

    """ Detroy instance and quit game function """
    def destroy_root_quit_game(self):
        self.root.destroy()
        pygame.display.quit()
        pygame.quit()
        sys.exit("Game Quit: Via tk_gui Class (0)")





