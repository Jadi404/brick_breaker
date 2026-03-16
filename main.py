from settings import * 
from paddle import * 
from brick import *
from ball import * 

class Game: 
    def __init__(self):
        pygame.init()
        #Window 
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)

        #Setting various Game states
        self.running = True
        self.clock = pygame.time.Clock()
        self.score =0
        self.lives =3 
        self.is_game_over = False
        self.won = False

        self.font = pygame.font.SysFont('Montserrat',24)

        #Game objects 
        self.paddle = Paddle(WIDTH//2 - PADDLE_WIDTH,HEIGHT - 20 - PADDLE_HEIGHT)
        self.bricks = self.generate_bricks()
        self.ball = Ball(WIDTH//2 - BALL_RADIUS,HEIGHT-100)

    def generate_bricks(self):
        bricks =[]
        colors =[PINK,ORANGE,YELLOW, GREEN,BLUE,SKY]

        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                x = BRICK_OFFSET_X + col * (BRICK_WIDTH + BRICK_PADDING)
                y = BRICK_OFFSET_Y + row * (BRICK_HEIGHT + BRICK_PADDING)
                color = colors[row%len(colors)]
                brick = Brick (x,y,color)
                bricks.append(brick)

        return bricks
    

    def reset (self):
        self.score = 0
        self.lives = 3
        self.is_game_over = False
        self.won = False
        self.bricks = self.generate_bricks()
        self.paddle.reset()
        self.ball.reset()
    
    #Check various events
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.reset()
        
        keys = pygame.key.get_pressed()
        if self.is_game_over or self.won:
            return

        if keys[pygame.K_LEFT]:
            self.paddle.move_left()

        if keys[pygame.K_RIGHT]:
            self.paddle.move_right()
            

    def update(self):
        if self.is_game_over or self.won:
            return
        self.ball.update()

        #Implement Collisions 
        #1. Collision with Walls - keepo ball in window
        if self.ball.rect.left <0:
            self.ball.bounce_x()
            self.ball.rect.left = 0

        if self.ball.rect.right > WIDTH:
            self.ball.bounce_x()
            self.ball.rect.right = WIDTH
        
        if self.ball.rect.top <0:
            self.ball.bounce_y()
            self.ball.rect.top =0

        #2. Collison with bricks
        for brick in self.bricks:
            if brick.active and self.ball.rect.colliderect(brick.rect):
                brick.active = False
                self.score +=10
                self.ball.bounce_y()
                break


        #3. Collision with paddle
        if self.ball.rect.colliderect(self.paddle.rect):
            self.ball.bounce_y()
            offset = (self.ball.rect.centerx - self.paddle.rect.centerx) / (PADDLE_WIDTH//2)
            self.ball.dx = offset *BALL_SPEED

        #4. Ball below paddle
        if self.ball.rect.top > HEIGHT:
            self.lives -=1
            if self.lives<=0:
                self.is_game_over = True
            else:
                self.ball.reset()
                self.paddle.reset()
        

        #Check win state
        self.won = all(not brick.active for brick in self.bricks)


    def draw(self):
        pygame.display.update()
        self.window.fill(BLACK)   
        self.paddle.draw(self.window) 
        for brick in self.bricks:
            if brick.active:
                brick.draw(self.window)

        self.ball.draw(self.window)

        #Draw Score and Lives
        score_text = self.font.render(f"Scores: {self.score}", True, WHITE)
        lives_text = self.font.render(f"Lives: {self.lives}", True, WHITE)

        self.window.blit (score_text, (10,10))
        self.window.blit (lives_text, (WIDTH-10-lives_text.get_width(),10))

        if self.is_game_over:
            #Draw game over text
            game_over_text = self.font.render(f"Game Over! Score: {self.score}. Press enter to continue...", True,WHITE) 
            self.window.blit (game_over_text, (WIDTH//2 - game_over_text.get_width()// 2,
                                               HEIGHT//2  -game_over_text.get_height()//2))
        elif self.won:
            game_won_text = self.font.render(f"You Won! Score: {self.score}. Press enter to continue...", True,WHITE) 
            self.window.blit (game_won_text, (WIDTH//2 - game_won_text.get_width()// 2,
                                              HEIGHT//2 -game_won_text.get_height()//2))
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
