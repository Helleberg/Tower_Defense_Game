import pygame as pg
import tilemap
import settings

class TowerFoundation(pg.sprite.Sprite):
    def __init__(self, game, pos):
        self.groups = game.all_sprites, game.tower_foundation_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load("assets/imgs/tower_foundation.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = self.pos