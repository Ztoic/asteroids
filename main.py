import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    # Creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    # To add instances to our group, we use static field  'containers'
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids_group)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shot_group)

                  # Setting our position like this, will draw de player on the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        screen.fill("black")
        for entity in drawable:
            entity.draw(screen)

        # This will update the content of entire display
        pygame.display.flip()

        # Stablish frames per second
        clock.tick(60)
        dt = clock.tick(60) / 1000

        for entity in updatable:
            entity.update(dt)
        
        for asteroid in asteroids_group:
            if asteroid.has_collision(player):
                print("Game Over!")
                exit()

        for asteroid in asteroids_group:
            for bullet in shot_group:
                if bullet.has_collision(asteroid):
                    bullet.kill()
                    asteroid.split()

if __name__ == "__main__":
    main()
