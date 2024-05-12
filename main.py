from pygame import *
from random import *

WIN_WIDTH = 1000
WIN_HEIGHT = 600

FPS = 120

plus_coins = 1
coins = 0
schot = 0
timerr = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        super().__init__()
        self.image = back = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def click(self):
        global plus_coins
        global coins
        global timerr
        coins += plus_coins
        timerr = True
        coin.image = back = transform.scale(image.load('coin.png'), (250, 250))
        coin.rect.x = 175
        coin.rect.y = 275
        print(coins)


window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))

coin = Player('coin.png', 150, 250, 300, 300)
menu = GameSprite('menu.png', 600, 0, 400, 600)

clock = time.Clock()

game = True

while game:
    window.fill((150,200,250))
    for e in event.get():
        if e.type == QUIT:
            game = False 
        if e.type == MOUSEBUTTONDOWN:
            pos = e.pos
            if coin.rect.collidepoint(pos):
                coin.click()
    if timerr:
        schot += 1

    if schot >= 10:
        schot = 0
        coin.image = back = transform.scale(image.load('coin.png'), (300, 300))
        coin.rect.x = 150
        coin.rect.y = 250
        timerr = False

    coin.reset()
    menu.reset()

    display.update()
    clock.tick(FPS)