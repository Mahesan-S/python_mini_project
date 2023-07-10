import pygame
import random as r
# import game_obj as game

pygame.init()
# -----------------------------------------color function
rgb_list = [
    (255, 0, 0),    # Red
    (0, 0, 255),    # Blue
    (0, 255, 0),    # Green
    (255, 255, 0),  # Yellow
    (255, 165, 0),  # Orange
    (128, 0, 128),  # Purple
    (255, 192, 203),  # Pink
    (165, 42, 42),  # Brown
    (128, 128, 128),  # Gray
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Magenta
    (0, 128, 128),  # Teal
    (0, 0, 128),    # Navy
    (128, 128, 0),  # Olive
    (128, 0, 0),    # Maroon
    (255, 215, 0),  # Gold
    (192, 192, 192),  # Silver
    (75, 0, 130)    # Indigo
]
ran_valu = r.randint(0,17)
res = rgb_list[ran_valu]
# --------------------------------------------color
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (58, 166, 185)
PINK = (255, 68, 159)
SANDEL = (255, 132, 116)

# ----------------------------------consent width and height
WIDTH = int(400)
HEIGHT = int(600)
FPS = 60

# ----------------------------------paddle size
paddle_width = 50
paddle_height = 10
# ---------------------------------bullet size
BULLET_width = 10
BULLET_height = 10
# ---------------------------------brick size
COLS = 10
ROWS = 6
# ---------------------------------------------creating window screen
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('shoot game','shorting')
clock = pygame.time.Clock()

# ----------------------------------------paddle function using class
class Paddle():
    def __init__(self):
        self.pwidth = paddle_width
        self.pheight = paddle_height
        self.x = int(WIDTH/2) - int(self.pwidth/2)
        self.y = int(HEIGHT - 30)
        self.pmove_speed = 10
        self.rect =pygame.Rect(self.x,self.y,self.pwidth,self.pheight) #---- postion x,y 2nd -> size

    def draw_paddle(self):
        pygame.draw.rect(win,GREEN,self.rect) #-----draw win,color,objet

    # ----------------------------------------move function paddle
    def move_paddle(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.pmove_speed

        if key[pygame.K_RIGHT] and self.rect.x < WIDTH - 35:
            self.rect.x += self.pmove_speed
# -------------------------------------------create bullet call function
class Bullet():
    def __init__(self):
        self.bwidth = BULLET_width
        self.bheight = BULLET_height
        # self.x = paddle.rect.x + 20
        self.x = paddle.x + int(paddle_width/2) - 5
        self.y = paddle.y - paddle.pheight
        self.bmove = 10
        self.dcy = -3
        self.dcx =  3
        self.game_status = 0
        self.rect = pygame.Rect(self.x,self.y,self.bwidth,self.bheight)

    def draw_bullet(self):
        pygame.draw.rect(win,PINK,self.rect)

    def move_bullet(self):
        # if self.rect.right > WIDTH - 50: #--------- mistake
        #     self.rect.x *= -1
        # ------------------------------ wall collision
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.dcx *= -1

        if self.rect.top < 0:
            self.dcy *= -1

        if self.rect.bottom > HEIGHT:
            self.game_status = -1  # game over
        # -------------------------------paddle collision

        if self.rect.colliderect(paddle) and self.dcy > 0:
            # sound = pygame.mixer.Sound('pan.mpeg')
            # sound.play()
            self.dcy *= -1


        # ---------------------------------bricks collision
        all_done = True
        row_num = 0
        for row in bricks.main_brick:
            col_num = 0
            for br in row:
                if self.rect.colliderect(br):
                    # sound = pygame.mixer.Sound('shoot.mpeg')
                    # sound.play()
                    if abs(self.rect.bottom - br.top) < 5 and self.dcy > 0:
                        self.dcy *= -1

                    if abs(self.rect.top - br.bottom) < 5 and self.dcy < 0:
                        self.dcy *= -1

                    if abs(self.rect.left - br.right) < 5 and self.dcx > 0:
                        self.dcx *= -1

                    if abs(self.rect.right - br.left) < 5 and self.dcx < 0:
                        self.dcx *= -1

                    bricks.main_brick[row_num][col_num] = (0,0,0,0)
                if bricks.main_brick[row_num][col_num] != (0,0,0,0):
                    all_done = False
                col_num += 1
            row_num += 1

        if all_done:
            self.game_status = 1
        self.rect.x += self.dcx
        self.rect.y += self.dcy
        return self.game_status

# ----------------------------------brick class function
class Brick():
    def __init__(self):
        self.width = int(WIDTH/COLS)
        self.height = 20
    
#     ---------------------------------create brick
    def create_brick(self):
        self.main_brick = []
        for row in range(ROWS):
            row_brick = []
            for col in range(COLS):
                brick_x = col * self.width
                brick_y = row * self.height
                br = pygame.Rect(brick_x,brick_y,self.width,self.height)
                row_brick.append(br)
            self.main_brick.append(row_brick)

        # ---------------------------------draw bricks
    def draw_brick(self):
        for row in self.main_brick:
            for br in row:
                pygame.draw.rect(win,SANDEL,br)
                pygame.draw.rect(win, BLACK, br,2)

# --------------------create objet of games
paddle = Paddle()
bullet = Bullet()

bricks = Brick()
bricks.create_brick()

# --------------------------------------------update screen pre second
run = True
while run:
    clock.tick(FPS)
    # ----------------------fill bgcolor per sec
    win.fill('black')
    # -------------------------draw paddle function
    paddle.draw_paddle()
    # ---------------------------paddle move
    paddle.move_paddle()
    # ---------------------------draw bulet
    bullet.draw_bullet()
    # ---------------------------move bullet
    game_status = bullet.move_bullet()
    # -------------------------------draw bricks
    bricks.draw_brick()
    # ---------------------------------game over function
    if game_status == -1:
        win.fill(BLACK)
        font = pygame.font.SysFont(None, 50)
        text = font.render('GAME OVER', True, WHITE)
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        win.blit(text, text_rect)
        # ---------------------------------game win function
        if game_status == 1:
            win.fill(BLACK)
            font = pygame.font.SysFont(None, 50)
            text = font.render('WIN', True, WHITE)
            text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            win.blit(text, text_rect)
    # --------------------------quit even listion function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#     --------------------------------window update
    pygame.display.update()

pygame.quit()