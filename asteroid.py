import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x,y,radius):
        super().__init__(x,y,radius)
        self.score = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) 

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: 
            self.score = 1
            return
      
        random_angle = random.uniform(20,50)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_radius).velocity = vector1 *1.2
        Asteroid(self.position.x, self.position.y, new_radius).velocity = vector2 *1.2