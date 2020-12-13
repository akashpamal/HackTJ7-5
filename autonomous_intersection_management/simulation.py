import pygame as pg
#import numpy as np
from car import Directions, AssetManager, Car
import random
import time

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 800
SPAWN_RATE = 2 #0.25 cars per second, or 1 car every four seconds

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
    start = time.perf_counter()
    BACKGROUND.convert()
    current_cars = []
    
    while True:
        deltaTime = clock.get_time()
        backgroundInputCheck(pg.event.get())
        
        if (time.perf_counter() - start) > (1/SPAWN_RATE):
            current_cars.append(Car(screen, random.randrange(2)))
            start = time.perf_counter()
        
        screen.fill(BLACK)
        screen.blit(BACKGROUND, (0, 0))
        for car in current_cars:
            if car.completion_check():
                current_cars.remove(car)
                print("Removed car")
            else:
                car.update(deltaTime)
                car.draw(screen)
                
        if len(current_cars) > 0:        
            print(current_cars[0].velocity)
            
        clock.tick(60)
        pg.display.flip()
    
if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pg.display.set_caption("Autonomous Intersection Management Software")
    clock = pg.time.Clock()
    main()