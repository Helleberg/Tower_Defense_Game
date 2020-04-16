import pygame as pg
import tilemap
import settings
import functions
import sys

from highscore import highscores
from menu import Menu
from player import Player

pg.init()

# Game class
class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.clock = pg.time.Clock()
        self.player = Player(self.screen)
        self.menu = Menu(self.screen)
        self.running = True
        self.state = 'start'
        self.map = tilemap.Map('assets/maps/map_0.tmx')
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        
    # Run game - state machine
    def run(self):
        while self.running:
            if self.state == 'start':
                self.menu.draw()
                self.menuControls()
            elif self.state == 'playing':
                self.playingControls()
                self.playing_update()
                self.playing_draw()
            elif self.state == 'highscores':
                highscores(self.screen)
                self.highscoreControls()

            elif self.state == 'game over':
                # Game over state
                pass
            else:
                self.running = False
            self.clock.tick(settings.FPS)
        pg.quit()
        sys.exit()
    

    ###############################
    #        GAME CONTROLS        #
    ###############################

    def highscoreControls(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.state = 'start'
    
    def menuControls(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                for btn in self.menu.buttons:
                    if btn.rect.collidepoint(x,y):
                        self.state = btn.event

    def playingControls(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False

    ###############################
    #      PLAYING FUNCTIONS      #
    ###############################

    # Update player and enemies on the screen
    def playing_update(self):
        pass

    # Draw background, text, player and enemies
    def playing_draw(self):
        # Reset
        functions.screen_reset(self.screen)
        # Draw map
        self.screen.blit(self.map_img, (0, 0))
        self.player.draw()
        # Draw grid
        # functions.draw_grid(self.screen)

        pg.display.update()