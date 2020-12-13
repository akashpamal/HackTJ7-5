####################################
# Created by Akash Pamal, Jack Blair, and Rahel Selemon
# HackTJ 2020 12/13/20
# MIT License
####################################
from car import Directions, AssetManager, Car
import pygame as pg
import random
import time

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 800
SPAWN_RATE = 2.5 #cars per second

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
    CENTER = pg.math.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    start = time.perf_counter()
    BACKGROUND.convert()
    current_cars = [] #Maintains a list of current cars in the scene
    to_accelerate = []
    
    while len(current_cars) < 100: #Loop until there is a possible traffic jam
        deltaTime = clock.get_time()
        backgroundInputCheck(pg.event.get())
        
        #Spawn in a new Car if it is time
        if (time.perf_counter() - start) > (1/SPAWN_RATE): 
            initial_velocity = (random.randrange(3)*0.1) + 0.2
            lane = random.randrange(2)
            new_car = Car(screen, lane, initial_velocity = initial_velocity)
            accel = None
            start = time.perf_counter()
            current_cars.append((new_car, accel, start))
            
        #Draw background and cars and apply background
        screen.blit(BACKGROUND, (0, 0))
        for current_index, car in enumerate(current_cars):
            if car[0].completion_check():
                #Remove a Car if it is off the screen
                current_cars.remove(car)
            else:
                #Otherwise, update the Car and apply the algorithm
                car[0].update(deltaTime)
                car[0].draw(screen)
                
                # if car[0].out_of_intersection():
                #     car[0].set_accel(0.0000)
                to_remove_from_to_accelerate = set()
                for elem in to_accelerate:
                    if elem[1] >= time.perf_counter():
                        closest_car.set_accel(0.0005)
                        to_remove_from_to_accelerate.add(elem)
                to_accelerate = [elem for elem in to_accelerate if elem not in to_remove_from_to_accelerate]

                car_positions = get_predicted_position(car[0].position, car[0].velocity, 1, time.perf_counter(), time.perf_counter() + 20)
                changed = False
                for car2 in current_cars[current_index : ]:
                    if car2 != car:
                        #If the car is traveling in an opposite diection, they cannot hit
                        if Directions.opposite(car[0].direction, car2[0].direction):
                            continue
                        #If a car is traveling in the same direction but different lane, they cannot hit
                        if car[0].direction == car2[0].direction and car[0].lane != car2[0].lane:
                            continue
                        
                        other_car_positions = get_predicted_position(car2[0].position, car2[0].velocity, 1, time.perf_counter(), time.perf_counter() + 20)
                        
                        #Determine which car is closer to the intersection
                        if car[0].position.distance_to(CENTER) < car2[0].position.distance_to(CENTER):
                            closest_car = car[0]
                            farthest_car = car2[0]
                        else:
                            closest_car = car2[0]
                            farthest_car = car[0]
                        
                        for next_time in car_positions.keys():
                            
                            #This will determine if two cars will come close together and hit eachother
                            if car_positions[next_time].distance_to(other_car_positions[next_time]) < 125:
                                tboned = Directions.perpendicular(car[0].direction, car2[0].direction)

                                #If there is a collision, we have to determine what type it is
                                if tboned: #If they are perpendicular, it is a TBone
                                    closest_car.set_accel(0.0005)
                                    farthest_car.set_accel(-0.01)
                                    to_accelerate.append((farthest_car, time.perf_counter() + 2))
                                else: #If it's a collision and not a TBone, it has to be a fender bender
                                    if closest_car.out_of_intersection():
                                        farthest_car.set_accel(0.0005)
                                        closest_car.set_accel(-0.01)
                                        to_accelerate.append((closest_car, time.perf_counter() + 2))
                                    else:
                                        closest_car.set_accel(0.0005)
                                        farthest_car.set_accel(-0.01)
                                        to_accelerate.append((farthest_car, time.perf_counter() + 2))
                                changed = True
                        
                # if car[0].completed_intersection is False:
                #     car[0].set_accel(car[1](time.perf_counter()-car[2])*0.000001)
                
                if changed is False:
                    car[0].set_accel(0.0003)
                    
        clock.tick(60)
        pg.display.flip()

def get_predicted_position(position, velocity, deltat, start_t, end_t):
    """
    Returns a list of the future positions of a car given the time interval and velocity
    """
    positions = dict()
    
    for deltat in range(0, int(end_t - start_t), deltat):
        positions[deltat] = pg.math.Vector2(position + ((start_t + deltat) * velocity))
    return positions

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pg.display.set_caption("Autonomous Intersection Management Software")
    clock = pg.time.Clock()
    main()