from MySprite import MySprite
import pygame

class Text(MySprite):
    """concrete text sprite
    """

    def __init__(self, TEXT):
        MySprite.__init__(self)
        self.__TEXT = TEXT
        self.__FONT = pygame.font.SysFont("Ariel", 36)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)
        


