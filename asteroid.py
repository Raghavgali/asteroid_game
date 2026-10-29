import random
import pygame 
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", center=[self.position.x, self.position.y], radius=self.radius, width=LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            first_velocity = self.velocity.rotate(angle)
            second_velocity = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(x=self.position.x, y=self.position.y, radius=new_radius)
            second_asteroid = Asteroid(x=self.position.x, y=self.position.y, radius=new_radius)
            first_asteroid.velocity = first_velocity
            second_asteroid.velocity = second_velocity
