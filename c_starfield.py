import pygame
from a_window import Window
from b_box import Box
import random

if __name__ == "__main__":
    WINDOW = Window("Starfield")

    STARS = []
    for i in range(200):
        STAR_SIZE = random.randrange(1, 6)
        STARS.append(Box(STAR_SIZE, STAR_SIZE, random.randint(0, WINDOW.getWidth()-STAR_SIZE), random.randint(0, WINDOW.getHeight()-STAR_SIZE)))


    PLAYER = Box(50, 50, WINDOW.getWidth()//2, WINDOW.getHeight()//2 - 50//2)



    while True:
        # -- INPUTS -- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        PRESSED_KEYS = pygame.key.get_pressed()

        # -- PROCESSING -- #
        for star in STARS:
            #star.moveBox(PRESSED_KEYS)
            star.scrollX(WINDOW.getWidth())
            
        PLAYER.checkBoundaries(WINDOW.getWidth(), WINDOW.getHeight())
        

        # -- OUTPUTS -- #
        WINDOW.clearScreen()
        for star in STARS:
            WINDOW.getSurface().blit(star.getSurface(), star.getPOS())
        WINDOW.getSurface().blit(PLAYER.getSurface(), PLAYER.getPOS())
        
        WINDOW.updateFrame()



