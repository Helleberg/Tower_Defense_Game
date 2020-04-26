import pygame as pg
import tilemap
import settings
import functions
import sys

from tower_foundation import TowerFoundation
from enemies import Enemy
from highscore import highscores
from menu import Menu
from player import Player
from waves.waves import WaveCounter

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
        self.map = tilemap.Map(self, 'assets/maps/map_0.tmx')
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

    # Run game - state machine
    def run(self):
        # initialize all variables and do all the setup for the games startup
        self.all_sprites = pg.sprite.Group()
        self.enemies_sprites = pg.sprite.Group()
        self.tower_sprites = pg.sprite.Group()
        self.tower_foundation_sprites = pg.sprite.Group()
        self.enemy = Enemy(self, (-32, 96), self.map.path)
        for pos in self.map.tower_foundations_pos:
            TowerFoundation(self, pos)

        # Run the game
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
            # Towers Buttons
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                for btn in self.player.buttons:
                    if btn.rect.collidepoint(x,y):
                        btn.pressed_event(btn.event)

    ###############################
    #      PLAYING FUNCTIONS      #
    ###############################

    # Update sprites on the screen
    def playing_update(self):
        # Update al sprites
        self.all_sprites.update()

    # Draw sprites on the screen
    def playing_draw(self):
        # Reset
        functions.screen_reset(self.screen)
        # Draw map
        self.screen.blit(self.map_img, (0, 0))
        self.player.draw()
        # Draw grid
        # self.draw_grid()
        # Draw all sprites
        for sprite in self.all_sprites:
            # Draw enemies health
            if isinstance(sprite, Enemy):
                sprite.draw_health()
            self.screen.blit(sprite.image, sprite.pos)

        pg.display.update()