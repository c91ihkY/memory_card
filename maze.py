from pygame import *

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'), (win_width,win_height))


x1 = 100
y1 = 300

x2 = 300
y2 = 300

cyborg = transform.scale(image.load('cyborg.png'),(100, 100))
hero = transform.scale(image.load('hero.png'),(100, 100))
speed = 10

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

hero = GameSprite('hero.png', 5, win_height - 80, 4)
cyborg = GameSprite('cyborg.png', win_width - 80, 280, 2)
final = GameSprite ('treasure.png', win_width - 120, win_height - 80, 0)

        

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0, 0))

    hero.reset()
    cyborg.reset()
    final.reset()

    display.update()
    clock.tick(FPS)



