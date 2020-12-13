import pygame as pg
from car import Directions, AssetManager, Car
import physics
import random
import time
from physics import get_acceleration_function

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 800
SPAWN_RATE = 2 #0.25 cars per second, or 1 car every four seconds
NUM_COLLISIONS = 0

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
    global NUM_COLLISIONS
    start = time.perf_counter()
    BACKGROUND.convert()
    current_cars = []
    
    while True:
        deltaTime = clock.get_time()
        backgroundInputCheck(pg.event.get())
        
        if (time.perf_counter() - start) > (1/SPAWN_RATE):
            new_car = Car(screen, random.randrange(2), initial_velocity = (random.randrange(4)*0.1) + 0.3)
            accel = get_acceleration_function(new_car.velocity.magnitude(), new_car.velocity.magnitude(), 10, 400)
            start = time.perf_counter()
            current_cars.append((new_car, accel, start))
            
           
        screen.fill(BLACK)
        screen.blit(BACKGROUND, (0, 0))
        for car in current_cars:
            if car[0].completion_check():
                current_cars.remove(car)
                print("Removed car")
            else:
                car[0].update(deltaTime)
                car[0].draw(screen)
                
                car_positions = get_predicted_position(car[0].position, car[0].velocity, 1, time.perf_counter(), time.perf_counter() + 5)
                for car2 in current_cars:
                    if car2 != car:
                        if Directions.opposite(car[0].direction, car2[0].direction):
                            continue
                        if car[0].direction == car2[0].direction and car[0].lane != car2[0].lane:
                            continue
                        other_car_positions = get_predicted_position(car2[0].position, car2[0].velocity, 1, time.perf_counter(), time.perf_counter() + 5)
                
                        for next_time in car_positions.keys():
                            if car_positions[next_time].distance_to(other_car_positions[next_time]) < 100:
                                print(car[0].direction, car[0].lane)
                                print(car2[0].direction, car2[0].lane)
                                car2[0].set_accel(-0.0003)
                                
                                #raise Exception("Car too close: ",)
                                NUM_COLLISIONS += 1
                                #time.sleep(1)

                # if car[0].completed_intersection is False:
                #     car[0].set_accel(car[1](time.perf_counter()-car[2])*0.000001)
                
        # if len(current_cars) > 0:        
        #     print(current_cars[0].velocity)
            
        clock.tick(60)
        pg.display.flip()

def get_predicted_position(position, velocity, deltat, start_t, end_t):
    positions = dict()
    #0.5, 1, 1.5
    loop_time = int(end_t - start_t)
    for deltat in range(0, loop_time, deltat):
        positions[deltat] = pg.math.Vector2(position + ((start_t + deltat) * velocity))
    
    #positions[1] s one second after
    return positions

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pg.display.set_caption("Autonomous Intersection Management Software")
    clock = pg.time.Clock()
    main()