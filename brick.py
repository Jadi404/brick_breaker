from settings import * 

class Brick:
    def __init__(self,x:int, y:int,color:tuple[int,int,int]):
        self.rect = pygame.Rect(x,y,BRICK_WIDTH, BRICK_HEIGHT)
        self.color = color
        self.active = True

    def draw(self, window:pygame.Surface):
        pygame.draw.rect(window,self.color, self.rect)