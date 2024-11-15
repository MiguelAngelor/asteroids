from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x,y,radius=PLAYER_RADIUS):
        super().__init__(x,y,radius)
        self.rotation = 0
    
    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(), width=2)     
        

    def triangle(self):
    #this was given to me by the boot.dev course
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]