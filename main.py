import pygame
from pygame import *
import time
from random import *
pygame.init()

pygame.mixer.music.load('sounds/music.wav') #добавление музыки фоновой в игру
pygame.mixer.music.play(-1) #безперерывная музыка
sound = pygame.mixer.Sound('sounds/button.mp3') #добавление звука пули в переменную

#цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# шрифт
font = pygame.font.SysFont("arialblack", 40)

fps = 50 #кадры в секунду
count = 0 #для анимации
left = False
right = False
lifes = 2

# параметры окна
window_width = 1280
window_height = 800

# создание окна
pygame.display.set_caption("GameSpace")
window = pygame.display.set_mode((window_width, window_height))
picture_menu = transform.scale(image.load('images/backgrounds/background.jpg'), (window_width, window_height))

#сохранение картинок в переменные и списки
win = transform.scale(image.load('images/backgrounds/trophy.png'), (window_width, window_height)) 
loose = transform.scale(image.load('images/backgrounds/fail.jpg'), (window_width, window_height))

level1 = transform.scale(image.load('images/backgrounds/level1.jpg'), (window_width, window_height))


walking_right = [
    image.load('images/rightwalking/right1.png'),
    image.load('images/rightwalking/right2.png'),
    image.load('images/rightwalking/right3.png'), 
    image.load('images/rightwalking/right4.png'),
    image.load('images/rightwalking/right5.png'),
    image.load('images/rightwalking/right6.png'),
    image.load('images/rightwalking/right7.png'),
    image.load('images/rightwalking/right8.png'),
    image.load('images/rightwalking/right9.png'), 
    image.load('images/rightwalking/right10.png')
]

walking_left = [
    image.load('images/leftwalking/left1.png'), 
    image.load('images/leftwalking/left2.png'),
    image.load('images/leftwalking/left3.png'), 
    image.load('images/leftwalking/left4.png'), 
    image.load('images/leftwalking/left5.png'), 
    image.load('images/leftwalking/left6.png'), 
    image.load('images/leftwalking/left7.png'), 
    image.load('images/leftwalking/left8.png'),
    image.load('images/leftwalking/left9.png'),
    image.load('images/leftwalking/left10.png')
]

clock = pygame.time.Clock()

class GameSprite(sprite.Sprite): #класс для неподвижных объектов
    def __init__(self, filename, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.count = 0
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(GameSprite): #класс для врагов
    def __init__(self, filename, x, y, width, height, speed):
        super().__init__(filename, x, y, width, height)
        self.speed = speed
        self.directions = ["left", "right", "up", "down"]
    def update(self):
        self.direction = randint(0, 3)
        if self.direction == 0 and self.rect.x > 5:
            self.rect.x += self.speed
        elif self.direction == 1 and self.rect.x < window_width - 100:
            self.rect.x -= self.speed
        elif self.direction == 2 and self.rect.y > 5:
            self.rect.y += self.speed
        elif self.direction == 3 and self.rect.y < window_width - 100:
            self.rect.y -= self.speed


class Player(GameSprite): #класс для героя
    def __init__(self, filename, x, y, width, height, x_speed, y_speed, count, left, right):
        super().__init__(filename, x, y, width, height)
        self.life = lifes
        self.count = count
        self.left = left
        self.right = right
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.y_speed = -5
            self.count = 0
            self.rect.y += self.y_speed
            self.left = False
            self.right = False
            self.up =   True
            self.down = False
        elif keys[K_DOWN]:
            self.y_speed = 5
            self.count = 0
            self.rect.y += self.y_speed
            self.left = False
            self.right = False
            self.up = False
            self.down = True
        elif keys[K_LEFT]:
            self.x_speed = -5
            self.rect.x += self.x_speed
            self.count = 0
            self.left = True
            self.right = False
            self.up = False
            self.down = False
        elif keys[K_RIGHT] and self.rect.x < window_width - 104:
            self.x_speed = 5
            self.rect.x += self.x_speed
            self.count = 0
            self.left = False
            self.right = True
            self.up = False
            self.down = False
        else:
            self.x_speed = 0
            self.y_speed = 0
            self.left = False
            self.right = False
            self.up = False
            self.down = False
        
        self.rect.x += self.x_speed
        platform_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platform_touched:
                self.rect.right = p.rect.left
        elif self.x_speed < 0:
            for p in platform_touched:
                self.rect.left = p.rect.right
        self.rect.y += self.y_speed
        platform_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platform_touched:
                self.rect.bottom = p.rect.top
        elif self.y_speed < 0:
            for p in platform_touched:
                self.rect.top = p.rect.bottom
    def animation(self):
        if self.count + 1 >= fps:
            self.count = 0
        if self.left == True:
            window.blit(walking_left[self.count // 1], (self.rect.x, self.rect.y))
            self.count += 1
        elif self.right == True:
            window.blit(walking_right[self.count // 5], (self.rect.x, self.rect.y))
            self.count += 1
        else:
            window.blit(self.image, (self.rect.x, self.rect.y))
    def fire(self):
        bullet = Bullet('images/bullet.png', self.rect.right, self.rect.centery, 10, 10)
        bullets.add(bullet)

class Bullet(GameSprite): #класс для пуль
    def __init__(self, filename, x, y, width, height):
        super().__init__(filename, x, y, width, height)
        self.speed = 10
    def update(self):
        self.rect.x += self.speed
        if self.rect.x + 10 > window_width:
            self.kill()


#объекты игры
hero = Player('images/hero.png', 600, 280, 104, 119, 0, 0, count, left, right)
extralife = GameSprite('images/extralife1.png', 1200 ,700, 70, 70)

endoflevel1 = GameSprite('images/endsoflevels/trophy.png', 1150, 20, 150, 150)
barrier1 = GameSprite('images/barriers/glove.png', 250 , 400, 500 , 200)
barrier2 = GameSprite('images/barriers/tool2.png', 740, 190, 39, 300)
barrier3 = GameSprite('images/barriers/iron.png', 100, 230, 171, 320)
barrier4 = GameSprite('images/barriers/sputnik.png', 730, 150, 636, 150 )
barrier5 = GameSprite('images/barriers/tool4.png', 500, 160, 250, 87)

barriers = sprite.Group()
barriers.add(barrier1)
barriers.add(barrier2)
barriers.add(barrier3)
barriers.add(barrier4)
barriers.add(barrier5)

enemy1diff1 = Enemy('images/enemies/enemy1.png', randint(0, 1200), randint(0, 750), 100, 100, 5)
enemy2diff1 = Enemy('images/enemies/enemy2.png', randint(0, 1200), randint(0, 750), 100, 100, 5)
enemy3diff1 = Enemy('images/enemies/enemy3.png',randint(0, 1200), randint(0, 750), 100, 100, 5)

enemiesdiff1 = sprite.Group()
enemiesdiff1.add(enemy1diff1)
enemiesdiff1.add(enemy2diff1)
enemiesdiff1.add(enemy3diff1)

bullets = sprite.Group()

finish = False
run = True

while run:
    for e in pygame.event.get():
        if e.type == QUIT: #закрытие программы
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.fire()

        if finish == False:
            window.blit(level1, (0, 0)) #отображение окна    
            hero.update()
            hero.animation()
            extralife.reset()
            endoflevel1.reset()
            barriers.draw(window)
            enemiesdiff1.draw(window)
            enemiesdiff1.update()
            bullets.draw(window)
            bullets.update()

        if sprite.collide_rect(hero, endoflevel1):
                window.fill(WHITE)
                window.blit(win, (0, 0))
                finish = True
        sprite.groupcollide(bullets, enemiesdiff1, True, True)
        sprite.groupcollide(bullets, barriers, True, False)
        if sprite.collide_rect(hero, extralife):
            lifes += 1
        if sprite.spritecollide(hero, enemiesdiff1, True):
            lifes -= 1
        if lifes == 0:
            finish = True
            window.blit(loose, (0, 0))
            
        pygame.display.update()
        clock.tick(fps)
pygame.quit()