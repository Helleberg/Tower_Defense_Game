import pygame as pg
import functions
import settings
from towers.tower import Tower
from tower_foundation import TowerFoundation

class Player:
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen
        self.bg = pg.image.load('assets/imgs/sidebar.png').convert()
        self.health = 100
        self.money = 300
        self.score = 0
        self.level = 1
        self.buttons = [
            Button(self, self.game, 'assets/imgs/towers/tower_1_btn.jpg', 'assets/imgs/towers/tower_1_btn_active.jpg', 340, 300, 'buy')
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
                
    def buy_tower(self, btn):
        if btn.check_bal(self.money, btn.price) == True:
            btn.change_state()
    
    def place_tower(self):
        pass

    def draw(self):
        self.sidebar()

class Button:
    def __init__(self, player, game, image, image_ac, offset, tower_price, event):
        self.game = game
        self.player = player
        self.image = image
        self.image_ac = image_ac
        self.img = pg.image.load(image).convert()
        self.width, self.height = self.img.get_rect().size
        self.rect = self.img.get_rect()
        self.rect.center = (settings.WIDTH-150, offset)
        self.event = event
        self.active = False
        self.price = tower_price
    
    def check_bal(self, p_money, t_price):
        if p_money >= t_price:
            return True
        else:
            return False

    def change_state(self):
        if self.active:
            self.active = False
            self.img = pg.image.load(self.image).convert()
            for tower_foundation in self.game.map.tower_foundations:
                tower_foundation.image = pg.image.load("assets/imgs/towers/blank_foundation.png").convert_alpha()
        else:
            self.active = True
            self.img = pg.image.load(self.image_ac).convert()
            for tower_foundation in self.game.map.tower_foundations:
                tower_foundation.image = pg.image.load("assets/imgs/towers/tower_foundation.png").convert_alpha()
    
    def btn_pressed(self, event):
        if event == 'buy':
            self.player.buy_tower(self)

    def draw(self):
        return [self.img, self.rect]