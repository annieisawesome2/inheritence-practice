
import pygame
import random

class Window:
    """Create the window that will load pygame
    """
    def __init__(self, TITLE, WIDTH = 800, HEIGHT=600, FPS=30):
        self.__TITLE = TITLE
        self.__FPS = FPS #frames per second the window will refresh
        self.__WIDTH = WIDTH #width of the window
        self.__HEIGHT = HEIGHT #height of the window
        self.__SCREEN_DIM = (self.__WIDTH, self.__HEIGHT) #screen dimention
        self.__BG_COLOR = (50, 50, 50) #uses the format (R, G, B)
        self.__FRAME = pygame.time.Clock()
        self.__SURFACE = pygame.display.set_mode(self.__SCREEN_DIM) #surface object in pygame. Every item in your program will overlay on top of a surface object
        self.__SURFACE.fill(self.__BG_COLOR)
        pygame.display.set_caption(self.__TITLE) 

    # -- MODIFIER METHODS -- #
    def updateFrame(self):  
        """updating the window object based on the FPS that we have set
        """
        self.__FRAME.tick(self.__FPS) #waits for the appropriate time based on the set FPS
        pygame.display.flip() #updates the window with the new frame
    
    def clearScreen(self):
        """fill the screen with the background color
        """
        self.__SURFACE.fill(self.__BG_COLOR)


    # -- ACCESSOR METHODS -- #
    def getSurface(self):
        return self.__SURFACE
    
    def getWidth(self):
        return self.__WIDTH
    
    def getHeight(self):
        return self.__HEIGHT

class Text:
    """creates a text object to be placed on a surface
    """
    def __init__(self, TEXT):
        self.__TEXT = TEXT
        self.__COLOR = (255, 255, 255) #white
        self.__FONT = pygame.font.SysFont("Ariel", 36)
        self.__SURFACE = self.__FONT.render(self.__TEXT, True, self.__COLOR)
        self.__X = 0
        self.__Y = 0
        self.__POS = (self.__X, self.__Y)
        self.__SPD = 5
        self.__DIR_X = 1
        self.__DIR_Y = 1

    # -- MODIFIER METHODS -- #
    def setPOS(self, TUPLE):
        self.__X = TUPLE[0]
        self.__Y = TUPLE[1]
        self.__POS = (self.__X, self.__Y)

    
    def bounceX(self, SCREEN_WIDTH_MAX, SCREEN_WIDTH_MIN=0):
        self.__X += self.__DIR_X * self.__SPD
        if self.__X > SCREEN_WIDTH_MAX - self.getWidth():
            self.__DIR_X = -1 #reverse
            self.setColor((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))

        elif self.__X < SCREEN_WIDTH_MIN:
            self.__DIR_X = 1 
            self.setColor((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))

        self.__POS = (self.__X, self.__Y)


    def bounceY(self, SCREEN_HEIGHT_MAX, SCREEN_HEIGHT_MIN=0):
        self.__Y += self.__DIR_Y * self.__SPD
        self.POS = (self.__X, self.__Y)

        if self.__Y > SCREEN_HEIGHT_MAX - self.getHeight():
            self.__DIR_Y = -1 #reverse
            self.setColor((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))

        elif self.__Y < SCREEN_HEIGHT_MIN:
            self.__DIR_Y = 1 
            self.setColor((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))


        self.POS = (self.__X, self.__Y)
    
    def setColor(self, TUPLE):
        self.__COLOR = TUPLE
        self.__SURFACE = self.__FONT.render(self.__TEXT, True, self.__COLOR)



    # -- ACCESSOR METHODS -- #
    def getPOS(self):
        return self.__POS

    def getSurface(self):
        return self.__SURFACE
    
    def getWidth(self):
        return self.__SURFACE.get_width()
    
    def getHeight(self):
        return self.__SURFACE.get_height()



if __name__ == "__main__":
    # main program code
    pygame.init()

    WINDOW = Window("template", 800, 600, 30)
    TEXT = Text("Hello World")
    TEXT.setPOS((WINDOW.getWidth()//2 - TEXT.getWidth()//2, WINDOW.getHeight()//2 - TEXT.getHeight()//2))
    TEXT.setColor((0, 255, 0))

    while True:
        # -- INPUTS -- #
        # Allow the x in the title bar to work 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        TEXT.bounceX(WINDOW.getWidth())
        TEXT.bounceY(WINDOW.getHeight())

            
        # -- OUTPUTS -- # 
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(TEXT.getSurface(), TEXT.getPOS())  
        WINDOW.updateFrame() #like the sync function so do it at the end
