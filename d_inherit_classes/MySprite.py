from re import L
import pygame

class MySprite:
    """many of the common attributes and methods for sprites in pygame
    """
    def __init__(self, HEIGHT=0, WIDTH=0, X=0, Y=0, SPD=0, COLOR = (255, 255, 255)):
        self.__HEIGHT = HEIGHT
        self.__WIDTH = WIDTH
        self._DIM = (self.__WIDTH, self.__HEIGHT)
        self._SURFACE = pygame.Surface
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)
        self.__SPD = SPD
        self._COLOR = COLOR #white
        self.__DIR_X = 1
        self.__DIR_Y = 1

    # -- MODIFIER METHODS -- #
    def setWidth(self, WIDTH):
        self.__WIDTH = WIDTH
        self.__DIM = (self.__WIDTH, self.__HEIGHT)
    
    def setHeight(self, HEIGHT):
        self.__HEIGHT = HEIGHT
        self.__DIM = (self.__WIDTH, self.__HEIGHT)

    def setPosition(self, TUPLE):
        self.__X = TUPLE[0]
        self.__Y = TUPLE[1]
        self.__POS = (self.__X, self.__Y)
    
    def setColor(self, TUPLE):
        self._COLOR = TUPLE

    
    # -- ACCESSOR METHODS -- #
    def getWidth(self):
        return self._SURFACE.get_width()
    
    def getHeight(self):
        return self._SURFACE.get_height()

    def getDimensions(self):
        return self.__DIM
    
    def getPOS(self):
        return self.__POS
    
    def getSurface(self):
        return self._SURFACE

