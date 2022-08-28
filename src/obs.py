# Importing libraries
import pygame

# Importing files
import main as m

# Message to Screen class
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
    def message_to_screen(self, x, y, return_val=True):
        self.screen_text = self.__font.render(self.msg, self.__aa, self.color)
        self.__screen.blit(self.screen_text, (x, y)) 
        if return_val == True:
            return self.screen_text.get_rect(topleft=(x, y))
        else:
            return None

    # Method to get the size of the message
    def size_of_message(self):
        return (self.__font.size(self.msg))

