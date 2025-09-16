import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(selfs,x , y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, color="green", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            ast1= self.velocity.rotate(random_angle)
            ast2= self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_ast1.velocity = ast1 * 1.2
            new_ast2.velocity = ast2 * 1.2




