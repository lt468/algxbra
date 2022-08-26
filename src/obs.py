# Importing libraries
import pygame

# Importing files
import consts as c

# Message to Screen class
class Text:
    # Constructor
    def __init__(self, msg:str, font_size=25, font="mathjaxmath", colour=(c.black), aa=True, screen=c.screen):
        # Assigning variables to self object
        self.msg = msg
        self.__font_size = font_size
        self.__font = pygame.font.SysFont(font, self.__font_size)
        self.color = colour
        self.__aa = aa
        self.__screen = screen

    # Make font a read only variable
    @property
    def font(self):
        return self.__font

    # Make font_size a read only variable
    @property
    def font_size(self):
        return self.__font_size

    # Make aa a read only variable
    @property
    def aa(self):
        return self.__aa

    # Make screen a read only variable
    @property
    def screen(self):
        return self.__screen

    # Method to send the message to the screen
    def message_to_screen(self, x, y):
        self.screen_text = self.__font.render(self.msg, self.__aa, self.color)
        self.__screen.blit(self.screen_text, (x, y)) 

    # Size of message function
    def size_of_message(self):
        return(self.__font.size(self.msg))

