import pygame as pg
import functions
import settings

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.bg = pg.image.load('assets/imgs/bg.png').convert()
        self.buttons = [
            [Button('assets/imgs/play_btn.png').draw(), 260],
            [Button('assets/imgs/highscore_btn.png').draw(), 320],
            [Button('assets/imgs/quit_btn.png').draw(), 380],
        ]

    def draw(self):
        self.screen.blit(self.bg, [0,0])
        text, rect = functions.draw_text('FRONTLINE DEFENCE', 'assets/fonts/Gotu-Regular.ttf', 32, (255, 255, 255), settings.WIDTH // 2, 200)
        self.screen.blit(text, rect)

        # Buttons
        for btn in self.buttons:
            self.screen.blit(btn[0], (settings.WIDTH // 2 - btn[0].get_rect().size[0]//2, btn[1]))
        pg.display.update()

    def events(self):
        # Detect button clicks
        pass

class Button:
    def __init__(self, image):
        self.btn = pg.image.load(image).convert()
    
    def draw(self):
        return self.btn