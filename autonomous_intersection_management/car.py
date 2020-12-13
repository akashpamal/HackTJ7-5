import random
import pygame as pg
import copy
from enum import Enum

class Directions():
    right = (1, 0)
    left = (-1, 0)
    up = (0, 1)
    down = (0, -1)
     
    directions = [up, down, left, right]

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
    def __init__(self, screen, lane, max_acceleration = 0.0001):
        # Physics
        self.direction = random.choice(Directions.directions)
        self.position = self.gen_pos_lane(lane, self.direction)
        self.velocity = pg.math.Vector2(0.0, 0.0)
        self.acceleration = 0.0
        
        # Graphics
        pg.sprite.Sprite.__init__(self)
        image = random.choice(AssetManager.cars)
        self.image = image.convert_alpha() # This gets the clear image backgrounds
        self.image = pg.transform.scale(self.image, (200, 200))
        # self.image = self.rotate_image(screen, self.image)
        
        # Characteristics
        self.length = self.image.get_size()[0]
        self.width = self.image.get_size()[1]
        self.image = pg.transform.scale(self.image, (int(self.length/2), int(self.width/2)))
        self.max_acceleration = max_acceleration # Default is 0.001
        self.max_velocity = 0.8
        self.brake_deceleration = 5.0
        self.free_deceleration = 0.5
        
        # Copies
        self.OG_velocity = copy.copy(self.velocity)
        # self.acclertion_change = 
        
        
        
        
        # self.pos = self.generate_pos_from_lane()
        # self.direction = random.choice(Directions.directions)
        # #(0, 1), (0, -1), (1, 0), (0, 1) 
        # self.velocity = random.randrange(30, 60)

        
        
        
    def set_accel(self, new_accel):
        pass

    def update(self, dt):
        self.velocity += (self.acceleration * dt, 0)
        self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))
    
    def draw(self, screen):
        screen.blit(self.image, (self.velocity.x, self.velocity.y))
        
    def gen_pos_lane(self, lane, dir):
        return pg.math.Vector2(0, 0)
    
    def rotate_image(self, screen, old_image):
        if self.direction == Directions.right:
            rotated = pg.transform.rotate(old_image, 180)
            rect = rotated.get_rect()
            screen.blit(rotated, (middleX - rect.width / 2, middleY - rect.height / 2))