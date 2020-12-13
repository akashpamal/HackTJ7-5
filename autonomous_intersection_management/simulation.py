import pygame as pg
#import numpy as np
from car import Directions, AssetManager, Car

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 800

BLACK = (0, 0, 0)
# BACKGROUND = pg.image.load('./res/Intersection.png')
BACKGROUND = pg.image.load('./res/ExpandedIntersection.png')

def quitGame(): #Quits Pygame and Python
    pg.quit()
    quit()

def backgroundInputCheck(eventList): # Constantly checks for quits and enters
    for event in eventList:
            if event.type == pg.QUIT:
                quitGame()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    quitGame()
                     
def main():
    BACKGROUND.convert()
    car = Car(screen, 1)
    
    while True:
        deltaTime = clock.get_time()
        backgroundInputCheck(pg.event.get())
        
        #Update all cars
        #spawn new cars
        
        screen.fill(BLACK)
        screen.blit(BACKGROUND, (0, 0))
        car.draw(screen)
        #playerCar.draw(screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
         
        clock.tick(60)
        pg.display.flip()
    
    
if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pg.display.set_caption("Autonomous Intersection Management Software")
    clock = pg.time.Clock()
    main()