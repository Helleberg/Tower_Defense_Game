import pygame as pg
import functions
import settings

class Tower(pg.sprite.Sprite):
    def __init__(self, game, cost):
        self.groups = game.all_sprites, game.tower_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load("assets/imgs/towers").convert_alpha()
        self.cost = cost