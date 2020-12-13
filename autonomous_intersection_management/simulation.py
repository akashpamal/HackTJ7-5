import pygame as pg
#import numpy as np
from car import Directions, AssetManager, Car
import random

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
    num = 1
    car = Car(screen, num)
    car2 = Car(screen, num)
    car3 = Car(screen, num)
    car4 = Car(screen, num)
    
    while True:
        deltaTime = clock.get_time()
        backgroundInputCheck(pg.event.get())
        
        #Update all cars
        #spawn new cars
        
        screen.fill(BLACK)
        screen.blit(BACKGROUND, (0, 0))
        car.update(deltaTime)
        car.draw(screen)
        car2.update(deltaTime)
        car2.draw(screen)
        car3.update(deltaTime)
        car3.draw(screen)
        car4.update(deltaTime)
        car4.draw(screen)
        #playerCar.draw(screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
         
        clock.tick(60)
        pg.display.flip()
    
    
if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pg.display.set_caption("Autonomous Intersection Management Software")
    clock = pg.time.Clock()
    main()