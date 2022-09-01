# Importing libraries
import re
import pygame
import random
from random import randrange

# Importing files
import main as m

""" Message to screen class """
class Text:
    """ Constructor """
    def __init__(self, msg:str, font_size=25, font="mathjaxmath", colour=(m.black), aa=True, screen=m.gameDisplay):
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
    def __init__(self, msg: str, font_size=25, font="mathjaxmain", colour=m.black, aa=True, screen=m.gameDisplay):
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




