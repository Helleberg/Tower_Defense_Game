import pygame as pg
import functions
import settings

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.bg = pg.image.load('assets/imgs/bg.png').convert()
        self.buttons = [
            Button('assets/imgs/play_btn.png', 300),
            Button('assets/imgs/highscore_btn.png', 400),
            Button('assets/imgs/quit_btn.png', 500),
        ]

    def draw(self):
        self.screen.blit(self.bg, [0,0])
        text, rect = functions.draw_text('FRONTLINE DEFENCE', 'assets/fonts/BRLNSDB.TTF', 50, (255, 255, 255), settings.WIDTH // 2, 200)
        self.screen.blit(text, rect)

        # Buttons
        for btn in self.buttons:
            img, rect = btn.draw()
            self.screen.blit(img, rect)
        pg.display.update()

class Button:
    def __init__(self, image, offset):
        self.img = pg.image.load(image).convert()
        self.width, self.height = self.img.get_rect().size
        self.rect = self.img.get_rect()
        self.rect.center = (settings.WIDTH // 2, offset)
    
    def draw(self):
        return [self.img, self.rect]