import pygame as pg
from pygame import freetype

class WaveCounter(pg.sprite.Sprite):
    def __init__(self, time_until, action, *grps):
        super().__init__(grps)
        self.image = pg.Surface((300, 50))
        self.image.fill((3,2,1))
        self.image.set_colorkey((3,2,1))
        self.rect = self.image.get_rect(topleft=(10,10))
        WaveCounter.font = pg.freetype.SysFont(None, 32)
        WaveCounter.font.render_to(self.image, (0, 0), f'new wave in {time_until}', (255, 255, 255))
        self.timer = time_until * 1000
        self.action = action
    
    def update(self, dt):
        self.timer -= dt

        self.image.fill((3,2,1))
        WaveCounter.font.render_to(self.image, (0, 0), f'new wave in {int(self.timer / 1000) + 1}', (255, 255, 255))

        if self.timer <= 0:
            self.action()
            self.kill()