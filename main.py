import pygame
from constants import * #Import game constants
from player import *
from asteroid import *
from AsteroidField import AsteroidField

def main():
    pygame.init()
#Opening info:
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

#Setting up the Screen Variable
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#Time clock object:
    clock = pygame.time.Clock()
    dt = 0

#groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable,drawable)

#Spawn Player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)


#Infinite Loop for the Game:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Player refresh
        for obj in updatable: 
            obj.update(dt)

                  #Screen Draw
        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)

        #flip After all drawing is done
        pygame.display.flip()

        #Making it 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()