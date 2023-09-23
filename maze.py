#створи гру "Лабіринт"!
import pygame


WIDTH = 1300
HEIGHT = 700
FPS = 60

w = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("ТОП ГРА ДЛЯ СПРАВЖНІХ МУЖИКІВ")

background = pygame.transform.scale(
    pygame.image.load("background.jpg"),(WIDTH,HEIGHT)
)
clock = pygame.time.Clock()
#музика
pygame.mixer.init()
pygame.mixer.music.load("jungles.ogg")
pygame.mixer.music.play()

class GameSpirite(pygame.sprite.Sprite):
    def __init__(self,filename, x,y, speed  ):
        super().__init__()
        self.image = pygame.transform.scale(
                    pygame.image.load(filename),(65,65))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        w.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSpirite):
    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -=self.speed
        if key_pressed[pygame.K_DOWN] and self.rect.y < HEIGHT-70:
            self.rect.y +=self.speed
        if key_pressed[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -=self.speed
        if key_pressed[pygame.K_RIGHT] and self.rect.x < WIDTH-70:
            self.rect.x +=self.speed

class Enemy(GameSpirite):
    dererectori = "left"

    def update(self):
        if self.rect.x < WIDTH/2:
            self.dererectori = "right"
        elif self.rect.x > WIDTH - 65:
            self.dererectori = "left"

        if self.dererectori == "right":
            self.rect.x += self.speed
        elif self.dererectori == "left":
            self.rect.x -= self.speed

class Wall(pygame.sprite.Sprite):
    def __init__(self,cord,size,color ):
        super().__init__()
        self.rect = pygame.Rect(cord,size)
        self.color = color
    def draw_wall(self):
        pygame.draw.rect(w,self.color,self.rect)

walls = [
        Wall((10,10),(WIDTH/2,10),(255,0,0)),
        Wall((WIDTH-10,10),(10,HEIGHT-20),(255,0,0)),
        Wall((10,10),(10,HEIGHT-20),(255,0,0)),
        Wall((10,10),(100,10),(255,0,0)),
        Wall((WIDTH/2,HEIGHT/2),(10,500),(255,0,0)),
]

player = Player('hero.png',50,HEIGHT-50,5)
enemy = Enemy('cyborg.png',WIDTH/2+100,HEIGHT/3,4)
gold = GameSpirite('treasure.png',1200,600,0  )





game = True
fin = False
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
    if not fin:
        w.blit(background, (0,0))
        player.reset()
        player.update()
        gold.reset()

        enemy.reset()
        enemy.update()
        if pygame.sprite.collide_rect(player,enemy):
            fin = True
            sfx = pygame.mixer.Sound("kick.ogg")
            sfx.play()
            pygame.font.init()
            font = pygame.font.Font(None,70) 
            text = font.render("lol",True,(250,0,0))
            w.blit(text,(WIDTH/2,HEIGHT/2))
        if pygame.sprite.collide_rect(player,gold):
            fin = True
            sfx = pygame.mixer.Sound("money.ogg")
            sfx.play()
            pygame.font.init()
            font = pygame.font.Font(None,70) 
            text = font.render("WIN",True,(0,250,0))
            w.blit(text,(WIDTH/2,HEIGHT/2))

    pygame.display.update()
    clock.tick(FPS)





