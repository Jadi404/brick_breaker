from settings import *

class Paddle():
    def __init__(self, x:int,y:int):
        self.rect = pygame.Rect(x,y,PADDLE_WIDTH,PADDLE_HEIGHT)
    
    def draw(self, window:pygame.Surface):
        pygame.draw.rect(window,GRAY,self.rect)

    def move_right(self):
        self.rect.x += PADDLE_SPEED
        if self.rect.right> WIDTH:
            self.rect.right = WIDTH

    def move_left(self):
        self.rect.x -= PADDLE_SPEED
        if self.rect.left < 0:
            self.rect.left = 0

    def reset(self):
        self.rect.x = WIDTH//2 - PADDLE_WIDTH//2
        self.rect.y = HEIGHT - 20 - PADDLE_HEIGHT