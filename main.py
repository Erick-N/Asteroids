import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, drawable, updatable)
    newPlayer = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    newAsteroidField = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for thing in asteroids:
            if thing.collides_with(newPlayer):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for current_asteroid in asteroids:
            for current_shot in shots:
                if current_shot.collides_with(current_asteroid):
                    log_event("asteroid_shot")
                    current_asteroid.split()
                    current_shot.kill()
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
