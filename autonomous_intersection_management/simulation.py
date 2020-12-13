import pygame as pg
from car import Directions, AssetManager, Car
import physics
import random
import time
# from physics import get_position_function

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 800
SPAWN_RATE = 2.5 # 0.25 cars per second, or 1 car every four seconds
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
    CENTER = pg.math.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    start = time.perf_counter()
    BACKGROUND.convert()
    current_cars = []
    # cars_dict = {}
    
    while len(current_cars) < 100:
        deltaTime = clock.get_time()
        backgroundInputCheck(pg.event.get())
        
        if (time.perf_counter() - start) > (1/SPAWN_RATE):
            initial_v = (random.randrange(3)*0.1) + 0.2
            new_car = Car(screen, random.randrange(2), initial_velocity = initial_v)
            # accel = get_acceleration_function(new_car.velocity.magnitude(), new_car.velocity.magnitude(), 10, 400)
            accel = None
            start = time.perf_counter()
            current_cars.append((new_car, accel, start))
            to_accelerate = []
            # get_position_function(initial_v, initial_v, start, )
            # (V0, Vf, spawn_time, intersect_time, deltax):
            # cars_dict[new_car] = 

           
        #screen.fill(BLACK)
        screen.blit(BACKGROUND, (0, 0))
        for current_index, car in enumerate(current_cars):
            if car[0].completion_check():
                current_cars.remove(car)
                #t("Removed car")
            else:
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
                        if Directions.opposite(car[0].direction, car2[0].direction):
                            continue
                        if car[0].direction == car2[0].direction and car[0].lane != car2[0].lane:
                            continue
                        
                        other_car_positions = get_predicted_position(car2[0].position, car2[0].velocity, 1, time.perf_counter(), time.perf_counter() + 20)
                        
                        if car[0].position.distance_to(CENTER) < car2[0].position.distance_to(CENTER):
                            closest_car = car[0]
                            farthest_car = car2[0]
                        else:
                            closest_car = car2[0]
                            farthest_car = car[0]
                        
                        for next_time in car_positions.keys():
                            
                            if car_positions[next_time].distance_to(other_car_positions[next_time]) < 125:
                                tboned = Directions.perpendicular(car[0].direction, car2[0].direction)
                            
                                if tboned: # TBone
                                    # decel = 
                                    closest_car.set_accel(0.0005)
                                    farthest_car.set_accel(-0.01)
                                    to_accelerate.append((farthest_car, time.perf_counter() + 2))
                                else: # From Behind aka bumper to bumper:) not in a weird way though
                                    # if it's a collision and not a tbone, it has to be a fender bender
                                    if closest_car.out_of_intersection():
                                        farthest_car.set_accel(0.0005)
                                        closest_car.set_accel(-0.01)
                                        to_accelerate.append((closest_car, time.perf_counter() + 2))
                                    else:
                                        closest_car.set_accel(0.0005)
                                        farthest_car.set_accel(-0.01)
                                        to_accelerate.append((farthest_car, time.perf_counter() + 2))
                                changed = True
                        
                            # if car.out_of_intersection
                            #     car.set_accel(0.0005)
                              #  
                            
                            
                            # else:
                            #     closest_car.set_accel(0.0002)
                                
                                #print(car[0].direction, car[0].lane)
                                #print(car2[0].direction, car2[0].lane)
                                # car2[0].set_accel(-0.002)
                                
                                #raise Exception("Car too close: ",)
                                NUM_COLLISIONS += 1
                                #time.sleep(1)

                # if car[0].completed_intersection is False:
                #     car[0].set_accel(car[1](time.perf_counter()-car[2])*0.000001)
                
                if changed is False:
                    car[0].set_accel(0.0003)
                    
                    
        clock.tick(60)
        pg.display.flip()

def get_predicted_position(position, velocity, deltat, start_t, end_t):
    positions = dict()
    
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