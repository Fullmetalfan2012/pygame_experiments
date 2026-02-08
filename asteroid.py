import random
from circleshape import *
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position +=  (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        split_path_one = self.velocity.rotate(angle)
        split_path_two = self.velocity.rotate(-angle)
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        split_asteroid_one = Asteroid(self.position.x, self.position.y, split_radius)
        split_asteroid_two = Asteroid(self.position.x, self.position.y, split_radius)
        split_asteroid_one.velocity = split_path_one * 1.2
        split_asteroid_two.velocity = split_path_two * 1.2
