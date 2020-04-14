import pygame as pg
import functions
import settings

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.bg = pg.image.load('assets/imgs/sidebar.png').convert()
        self.health = 100
        self.money = 0
        self.score = 0
        self.level = 1
    
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
            settings.WIDTH - 150, 150
        )
        self.screen.blit(text, rect)

        text, rect = functions.draw_text(
            f'Score: {self.score}', 'assets/fonts/BRLNSDB.TTF', 
            26, (255, 255, 255), 
            settings.WIDTH - 150, 200
        )
        self.screen.blit(text, rect)

    def draw(self):
        self.sidebar()