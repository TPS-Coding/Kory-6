from settings import * 
from random import choice, uniform

class Paddle(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)


    ## image
        self.image = pygame.Surface(SIZE['paddle'])
        self.image.fill(COLORS['paddle'])

    ## rect and movement
        self.rect = self.image.get_frect(center=POS['player'])
        self.old_rect = self.rect.copy()
        self.direction = 0

    def move(self, dt):
        self.rect.centery += self.direction * self.speed * dt
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top
        self.rect.bottom = WINDOW_HEIGHT if self.rect.bottom > WINDOW_HEIGHT else self.rect.bottom
        

    def update(self, dt):
        self.old_rect = self.rect.copy() ## updated old position
        self.get_direction()
        self.move(dt)


class Player(Paddle):
    def __init__(self,groups):
        super().__init__(groups)

        #rect and movement

        ## image and rect inherited from Paddle class
        
        self.speed = SPEED['player']
    
    
    def get_direction(self):
        keys = pygame.key.get_pressed()
        self.direction = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])


class Ball(pygame.sprite.Sprite):
    def __init__(self, groups, paddle_sprites):
        super().__init__(groups)

        self.paddle_sprites = paddle_sprites

        ##image
        self.image = pygame.Surface(SIZE["ball"], pygame.SRCALPHA)
        #self.image.fill(COLORS["ball"])
        pygame.draw.circle(self.image,COLORS["ball"], (SIZE['ball'][0]/2,SIZE['ball'][1]/2),SIZE['ball'][0]/2)

        ## rect 
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        ## ther uniform didn't need the []
        self.direction = pygame.Vector2(choice([1,-1]), uniform(0.7, 0.8)*choice([-1.1]))

    def move(self, dt): ## <--- this was missing
        ### This didn't work because you had deleted the def move() function definition
        self.rect.center += self.direction * SPEED['ball'] * dt 
        self.collision("horizontal") ## A call to the collision function
    
    
    def wall_collision(self):
        ## y direction
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y *= -1
        
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            self.direction.y *= -1

        

    def collision(self, direction):
        for sprite in self.paddle_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == "horizontal":
                    if self.rect.right >= sprite.rect.left and self.direction.x == 1:
                        self.rect.right = sprite.rect.left
                    if self.rect.left <= sprite.rect.right and self.direction.x == -1:
                        self.rect.left = sprite.rect.right
                    
                    self.direction.x *= -1 
   
    def update(self, dt):
        self.move(dt)
        self.wall_collision()    


class Opponent(Paddle):
    def __init__(self, groups, ball):
        super().__init__(groups)


        self.speed = SPEED['opponent']
        self.rect.center = POS['opponent']## make sure we use a string and spell correctly
        ### the below code was missing
        self.ball = ball

    def get_direction(self):
        self.direction = 1 if self.ball.rect.centery > self.rect.centery else -1