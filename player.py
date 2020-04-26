import pygame as pg
import functions
import settings
from towers.tower import Tower


class Player:
    def __init__(self, screen):
        self.screen = screen
        self.bg = pg.image.load('assets/imgs/sidebar.png').convert()
        self.health = 100
        self.money = 39
        self.score = 0
        self.level = 1
        self.buttons = [
            Button('assets/imgs/towers/tower_1_btn.jpg', 340, 'buy_tower')
        ]
    
    def sidebar(self):
        self.screen.blit(self.bg, [settings.WIDTH-300,0])

        text, rect = functions.draw_text(
            'Game Stats', 'assets/fonts/BRLNSDB.TTF', 
            32, (255, 255, 255), 
            settings.WIDTH - 150, 50
        )
        self.screen.blit(text, rect)

        text, rect = functions.draw_text(
            f'{self.health} hp', 'assets/fonts/BRLNSDB.TTF', 
            26, (255, 255, 255), 
            settings.WIDTH - 150, 100
        )
        self.screen.blit(text, rect)

        text, rect = functions.draw_text(
            f'${self.money}', 'assets/fonts/BRLNSDB.TTF', 
            26, (255, 255, 255), 
            settings.WIDTH - 150, 140
        )
        self.screen.blit(text, rect)

        text, rect = functions.draw_text(
            f'Score: {self.score}', 'assets/fonts/BRLNSDB.TTF', 
            26, (255, 255, 255), 
            settings.WIDTH - 150, 180
        )
        self.screen.blit(text, rect)

        # Sidebar towers
        text, rect = functions.draw_text(
            f'Purchase Towers', 'assets/fonts/BRLNSDB.TTF', 
            22, (255, 255, 255), 
            settings.WIDTH - 150, 260
        )
        self.screen.blit(text, rect)

        # All towers
        for btn in self.buttons:
            img, rect = btn.draw()
            self.screen.blit(img, rect)
        pg.display.update()

    def draw(self):
        self.sidebar()

class Button:
    def __init__(self, image, offset, event):
        self.img = pg.image.load(image).convert()
        self.width, self.height = self.img.get_rect().size
        self.rect = self.img.get_rect()
        self.rect.center = (settings.WIDTH-150, offset)
        self.event = event
    
    def draw(self):
        return [self.img, self.rect]