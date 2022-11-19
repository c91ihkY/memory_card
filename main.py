from pygame import *

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'), (win_width,win_height))

game = True
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d]  and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 450:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'

        if self.direction == 'left': 
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

hero = Player('hero.png', 5, win_height - 80, 4)
cyborg = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite ('chestt.png', win_width - 120, win_height - 80, 0)
w1 = Wall(154, 205, 50, 100, 20 , 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20 , 10, 380)
finish = False

font.init()
label_font = font.Font(None, 70)
win = label_font.render('YOU WIN!', True, (255, 255, 0))

lose = label_font.render('YOU LOSE!', True, (255, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background,(0, 0))
        hero.update()
        cyborg.update()

        hero.reset()
        cyborg.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()

        if sprite.collide_rect(hero, cyborg) or sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, w2) or sprite.collide_rect(hero, w3):
            finish = True
            window.blit(lose,(200, 200))
            kick.play()

        if sprite.collide_rect(hero, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()


    display.update()
    clock.tick(FPS)


