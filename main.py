import sys
import pygame
from constants import * #Import game constants
from player import *
from asteroid import *
from AsteroidField import AsteroidField
from shot import Shot


def main():
    pygame.init()

    is_paused = False
    
    #Optiona, I want to define a scoreboard:
    pygame.font.init()
    font = pygame.font.SysFont("Arial",30)
    font2 = pygame.font.SysFont("Times New Roman",50)

    score = 0
    score_surface = font.render(f'Score: {score}', True, (255, 255, 255)) # White color text
    score_surface2 = font.render(f'"ASTEROIDS! by M.O."', True, (255, 255, 255))

#Opening info:
    print("Starting asteroids!")
    print("Press the ESC key to exit.")
    print('Press "P" key to pause.')
    print("Move with W,A,S,D and shot with SPACE.")
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
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, drawable, updatable)
    Shot.containers = (shots, updatable, drawable)
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
                print(f"Your score is: {score}")
                print("Thank you for Playing.") 
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # P key toggle
                    is_paused = not is_paused

            
        if player.exit == True:
                print(f"Your score is: {score}")
                print("Thank you for Playing.") 
                sys.exit()

            #Pause Screen
        if is_paused == True:
            pause_surface = font2.render('PAUSE', True, (255, 0, 0))  # Red text
            center_x = (SCREEN_WIDTH - pause_surface.get_width()) // 2
            center_y = (SCREEN_HEIGHT - pause_surface.get_height()) // 2
            screen.blit(pause_surface, (center_x, center_y))
            pygame.display.flip()
          
        if not is_paused:
        #Player refresh
            for obj in updatable: 
                obj.update(dt)

            for obj in asteroids:
                if player.collision(obj):
                    print("Game over!") 
                    print(f"Your score is: {score}")
                    print("Thank you for Playing.") 

                    sys.exit()
                for s in shots:
                    if obj.collision(s):
                        obj.split()
                        score += obj.score
                        s.kill()
                    
        #Screen Draw
        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)

        #Score
        if score % 15 == 0 and score !=0: score_surface2 = font2.render(f'GOOD JOB!', True, (50, 205, 50))
        else: score_surface2 = font.render(f'ASTEROIDS! by M.O. (Boot.Dev Course)', True, (255, 255, 255))
 

        score_surface = font.render(f'Score: {score}', True, (255, 255, 255))
        

        center_x = ((SCREEN_WIDTH - score_surface2.get_width()) //2)
        screen.blit(score_surface, (0, 0))
        screen.blit(score_surface2, (center_x, 0))

       #flip After all drawing is done
        if is_paused == False: pygame.display.flip()

        #Making it 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()