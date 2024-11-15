import pygame
from constants import * #Import game constants
from player import *

def main():
#Opening info:
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

#Setting up the Screen Variable
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#Time clock object:
    Clock = pygame.time.Clock()
    dt = 0

#Spawn Player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)

#Infinite Loop for the Game:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Screen Draw
        screen.fill((0,0,0))

        #Player refresh
        player.draw(screen)

        #flip After all drawing is done
        pygame.display.flip()

        #Making it 60 fps
        dt = Clock.tick(60) / 1000


if __name__ == "__main__":
    main()