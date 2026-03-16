from settings import * 

class Ball():
    def __init__(self, x:int,y:int):
        self.rect = pygame.Rect(x,y, BALL_RADIUS *2, BALL_RADIUS *2  )
        self.dx = BALL_SPEED
        self.dy = -BALL_SPEED

    def bounce_x (self):
        self.dx *=-1

    def bounce_y(self):
        self.dy *=-1

    def reset(self):
        self.rect.x = WIDTH//2 - BALL_RADIUS
        self.rect.y = HEIGHT-100
        self.dx = BALL_SPEED
        self.dy = -BALL_SPEED

    def update (self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def draw(self, window: pygame.Surface):
        center = pygame.Vector2(self.rect.x +BALL_RADIUS, self.rect.y + BALL_RADIUS)
        pygame.draw.circle(window, RED, center, BALL_RADIUS)