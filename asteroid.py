from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if(self.radius < ASTEROID_MIN_RADIUS):
            return
        angle = random.uniform(20,50)
        new_angle_1 = self.velocity.rotate(angle)
        new_angle_2 = self.velocity.rotate(angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteriod_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteriod_1.velocity = new_angle_1 * 1.2
        asteriod_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteriod_2.velocity = new_angle_2
