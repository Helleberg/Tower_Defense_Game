import pygame as pg
import functions
import settings

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.bg = pg.image.load('assets/imgs/menu_bg.jpg').convert()

    def draw(self):
        self.screen.blit(self.bg, [0,0])
        text, rect = functions.draw_text('Press space to continue', 'assets/fonts/PressStart2P.ttf', 32, (255, 255, 255), settings.WIDTH // 2, settings.HEIGHT // 2)
        self.screen.blit(text, rect)
        pg.display.update()
