import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = uniform(20, 50)
        first_new_vector = self.velocity.rotate(angle)
        second_new_vector = self.velocity.rotate (0 - angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        firstAsteroid = Asteroid(self.position.x, self.position.y, new_radius)
        secondAsteroid = Asteroid(self.position.x, self.position.y, new_radius)
        firstAsteroid.velocity = first_new_vector * 1.2
        secondAsteroid.velocity = second_new_vector * 1.2