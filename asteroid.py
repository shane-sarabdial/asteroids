import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(selfs,x , y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, color="green", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

