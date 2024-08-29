import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x , y, radius):
        super().__init__(x ,y, radius)
        self.position = pygame.Vector2(x, y)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt 
