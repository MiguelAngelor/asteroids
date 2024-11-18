from circleshape import *
from constants import *
from shot import Shot


class Player(CircleShape):
    def __init__(self, x,y,radius=PLAYER_RADIUS*0.5): #0.5 to fix hitbox, it was too big
        super().__init__(x,y,radius)
        self.rotation = 0
        self.shot_timer = 0
    
    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(), width=2)     
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        if self.shot_timer <0: self.shot_timer = 0
        self.shot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def triangle(self):
    #this was given to me by the boot.dev course
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * (self.radius*2) / 1.5
        a = self.position + forward * (self.radius*2) #Multiplied *2 to compensate
        b = self.position - forward * (self.radius*2) - right
        c = self.position - forward * (self.radius*2) + right
        return [a, b, c]
    
    def shoot(self):
        if self.shot_timer > 0:
                return
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x,self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            