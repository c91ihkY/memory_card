from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'), (700,500))

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

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0, 0))
    window.blit(cyborg, (x1, y1))
    window.blit(hero, (x2, y2))
    display.update()
    clock.tick(FPS)



