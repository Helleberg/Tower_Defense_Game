import pygame as pg
import settings
import sys

from highscore import highscores

pg.init()

# Game class
class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True
        self.state = 'highscores'
        
    # Run game - state machine
    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            elif self.state == 'highscores':
                highscores(self.screen)

            elif self.state == 'game over':
                # Game over state
                pass
            else:
                self.running = False
            self.clock.tick(settings.FPS)
        pg.quit()
        sys.exit()
    
    ###############################
    #       HELPER FUNCTIONS      #
    ###############################

    # Reset Game Screen
    def screen_reset(self):
        self.screen.fill((0,0,0))
    
    # Grid draw function
    def draw_grid(self):
        for x in range(0, settings.WIDTH, settings.TILESIZE):
            pg.draw.line(self.screen, (200, 200, 200), (x, 0), (x, settings.HEIGHT))
        for y in range(0, settings.HEIGHT, settings.TILESIZE):
            pg.draw.line(self.screen, (200, 200, 200), (0, y), (settings.WIDTH, y))

    ###############################
    #       START FUNCTIONS       #
    ###############################

    # Player inputs
    def start_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.state = 'playing'

    def start_update(self):
        pass

    # Draw start screen
    def start_draw(self):
        # Reset screen
        self.screen_reset()
        # Start screen text
        text, rect = self.draw_text('Press space to continue', 'assets/fonts/PressStart2P.ttf', 32, (255, 255, 255), settings.WIDTH // 2, settings.HEIGHT // 2)
        self.screen.blit(text, rect)
        # self.start_background = pg.image.load('imgs/start_bg.png')
        # self.screen.blit(self.start_background, (0, 0))
        pg.display.update()

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
        pass

    # Draw background, text, player and enemies
    def playing_draw(self):
        # Reset screen
        self.screen_reset()
        # Draw grid
        self.draw_grid()
        # text, rect = self.draw_text('Welcome to the game', 'fonts/PressStart2P.ttf', 32, (255, 255, 255), self.config["width"] // 2, self.config["height"] // 2)
        # self.screen.blit(text, rect)
        pg.display.update()