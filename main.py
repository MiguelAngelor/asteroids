import pygame
from constants import * #Import game constants

def main():
#Opening info:
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

#Setting up the Screen Variable
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#Infinite Loop for the Game:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    main()