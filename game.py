import pygame as pg
import tilemap
import settings
import functions
import enemies
import sys

from highscore import highscores
from menu import Menu

pg.init()

# Game class
class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.clock = pg.time.Clock()
        self.menu = Menu(self.screen)
        self.running = True
        self.state = 'highscores'
        self.map = tilemap.Map('assets/maps/map_0.tmx')
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        
    # Run game - state machine
    def run(self):
        # initialize all variables and do all the setup for the games startup
        self.all_sprites = pg.sprite.Group()
        self.enemies_sprites = pg.sprite.Group()
        self.enemies = enemies.spawn(self, (-32, 96), self.map.path)

        # Run the game
        while self.running:
            if self.state == 'start':
                self.menu.draw()
                self.menuControls()
            elif self.state == 'playing':
                self.playing_events()
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
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.state = 'playing'

    ###############################
    #       HELPER FUNCTIONS      #
    ###############################
    # Grid draw function
    def draw_grid(self):
        for x in range(0, settings.WIDTH, settings.TILESIZE):
            pg.draw.line(self.screen, (200, 200, 200), (x, 0), (x, settings.HEIGHT))
        for y in range(0, settings.HEIGHT, settings.TILESIZE):
            pg.draw.line(self.screen, (200, 200, 200), (0, y), (settings.WIDTH, y))

    ###############################
    #      PLAYING FUNCTIONS      #
    ###############################

    # Get player inputs
    def playing_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False

    # Update player and enemies on the screen
    def playing_update(self):
        # Move enemy
        self.all_sprites.update()

    # Draw background, text, player and enemies
    def playing_draw(self):
        # Reset
        functions.screen_reset(self.screen)
        # Draw map
        self.screen.blit(self.map_img, (0, 0))
        # Draw grid
        # self.draw_grid()
        # Draw all sprites
        for sprite in self.all_sprites:
            # Draw enemies health
            if isinstance(sprite, enemies.Enemy):
                sprite.draw_health()
            self.screen.blit(sprite.image, sprite.pos)

        pg.display.update()