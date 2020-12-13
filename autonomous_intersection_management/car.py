import random
import pygame as pg
import copy
from enum import Enum

class Directions():
    right = (1, 0)
    left = (-1, 0)
    up = (0, -1)
    down = (0, 1)
     
    directions = [up, down, left, right]
        
    # def perpendicular(self, dir1, dir2):
    #     if dir1 == up:
    #         return dir2 == down
    #     elif dir1 == down:
    #         return dir2 == up
    #     elif dir1 == left:
    #         return dir2 == right
    #     elif dir1 == right:
    #         return dir2 == left
    
    def opposite(dir1, dir2):
        if dir1 == Directions.up:
            return dir2 == Directions.down
        elif dir1 == Directions.down:
            return dir2 == Directions.up
        elif dir1 == Directions.left:
            return dir2 == Directions.right
        elif dir1 == Directions.right:
            return dir2 == Directions.left

class AssetManager():
    lblue = pg.image.load('./res/BlueCar.png')
    blue = pg.image.load('./res/BlueSudan.png')
    yellow = pg.image.load('./res/YellowTruck.png')
    brown = pg.image.load('./res/BrownCar.png')
    grey = pg.image.load('./res/GreyCar.png')
    red = pg.image.load('./res/RedCar.png')
    purple = pg.image.load('./res/PurpleCar.png')
    green = pg.image.load('./res/GreenCar.png')
    cars = [lblue, blue, yellow, brown, grey, red, purple, green]
    
class Car:
    def __init__(self, screen, lane, max_acceleration = 0.0001, initial_velocity = 0.5):
        # Physics
        self.direction = random.choice(Directions.directions) 
        self.position = self.gen_pos_lane(lane, self.direction)
        self.velocity = pg.math.Vector2(self.direction[0] * initial_velocity, self.direction[1] * initial_velocity)
        self.acceleration = pg.math.Vector2(self.direction[0] * max_acceleration, self.direction[1] * max_acceleration)
        
        # Graphics
        image = random.choice(AssetManager.cars)
        self.image = image.convert_alpha() # This gets the clear image backgrounds
        self.image = self.rotate_image(screen, self.image)
        
        # Characteristics
        self.length = self.image.get_size()[0]
        self.width = self.image.get_size()[1]
        self.image = pg.transform.scale(self.image, (int(self.length/2), int(self.width/2)))
        self.max_acceleration = max_acceleration # Default is 0.001
        self.max_decceleration = 0.05
        self.max_velocity = 0.8
        self.completed_path = False
        self.completed_intersection = False
        self.lane = lane
        
    def set_accel(self, new_accel):
        if self.direction == Directions.left or self.direction == Directions.up:
            new_accel *= -1
            
        print("The AI has changed the Acceeration from " + str(self.acceleration) + " to " + str(new_accel))
        if new_accel > self.max_acceleration:
            print("Acceleration is not possible !!!!!!!! @AKASHHHH")
            
        if new_accel > -self.max_decceleration:
            print("Decceleration is too fast !!!!!!!! @AKASHHHH")
        
        if self.acceleration[0] == 0:
            self.acceleration = pg.math.Vector2(0, new_accel)
        else:
            self.acceleration = pg.math.Vector2(new_accel, 0)

    def update(self, dt):
        self.velocity += self.acceleration * dt
        
        if self.direction == Directions.right:
            if self.velocity[0] < 0:
                self.velocity.x = 0
        elif self.direction == Directions.left:
            if self.velocity[0] > 0:
                self.velocity.x = 0
        elif self.direction == Directions.up:
            if self.velocity[1] > 0:
                self.velocity.y = 0
        elif self.direction == Directions.down:
            if self.velocity[1] < 0:
                self.velocity.y = 0
                
        self.position += self.velocity * dt
        self.in_intersection()
        
    def completion_check(self):
        if self.direction == Directions.right:
            return self.position.x > 1540
        elif self.direction == Directions.left:
            return self.position.x < -100
        elif self.direction == Directions.up:
            return self.position.y < -100
        elif self.direction == Directions.down:
            return self.position.y > 900
    
    def draw(self, screen):
        screen.blit(self.image, (self.position.x, self.position.y))
        
    def gen_pos_lane(self, lane, direction):
        #Generates X and Y given lane and direction
        if direction == Directions.up:
            print("up", lane)
            if lane == 0: #Done
                return pg.math.Vector2(775, 900)
            if lane == 1:
                return pg.math.Vector2(831, 900)
        elif direction == Directions.down:
            print("down", lane)
            if lane == 0: #Done
                return pg.math.Vector2(717, -100)
            if lane == 1:
                return pg.math.Vector2(661, -100)
        elif direction == Directions.left:
            print("left", lane)
            if lane == 0:
                return pg.math.Vector2(1540, 367)
            if lane == 1:
                return pg.math.Vector2(1540, 318)
        elif direction == Directions.right:
            print("right", lane)
            if lane == 0:
                return pg.math.Vector2(-100, 462)
            if lane == 1:
                return pg.math.Vector2(-100, 509)
                
        return "Bruh"
    
    def gen_pos_lane_inclusive(self, lane, direction):
        #Generates X and Y given lane and direction
        if direction == Directions.up:
            print("up", lane)
            if lane == 0: #Done
                return pg.math.Vector2(775, 700)
            if lane == 1:
                return pg.math.Vector2(831, 700)
        elif direction == Directions.down:
            print("down", lane)
            if lane == 0: #Done
                return pg.math.Vector2(717, 100)
            if lane == 1:
                return pg.math.Vector2(661, 100)
        elif direction == Directions.left:
            print("left", lane)
            if lane == 0:
                return pg.math.Vector2(1340, 367)
            if lane == 1:
                return pg.math.Vector2(1340, 318)
        elif direction == Directions.right:
            print("right", lane)
            if lane == 0:
                return pg.math.Vector2(100, 462)
            if lane == 1:
                return pg.math.Vector2(100, 509)
                
        return "Bruh"
    
    
    def rotate_image(self, screen, old_image):
        
        if self.direction == Directions.right:
            rotated = pg.transform.rotate(old_image, 180)
            rect = rotated.get_rect()
            self.position.x -= rect.width / 2
            self.position.y -= rect.height / 2
        elif self.direction == Directions.up:
            rotated = pg.transform.rotate(old_image, 270)
            rect = rotated.get_rect()
            self.position.x -= rect.width / 2
            self.position.y -= rect.height / 2
        elif self.direction == Directions.down:
            rotated = pg.transform.rotate(old_image, 90)
            rect = rotated.get_rect()
            self.position.x -= rect.width / 2
            self.position.y -= rect.height / 2
        
        if self.direction == Directions.left:
            return old_image
        return rotated
    
    def in_intersection(self):
        if 820 > self.position.x > 620 and 500 > self.position.y > 300:
            self.completed_intersection = True
    