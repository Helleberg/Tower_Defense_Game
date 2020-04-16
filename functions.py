import pygame as pg
import settings

# Text draw function
def draw_text(text, text_font, size, color, pos_x, pos_y):
    font = pg.font.Font(text_font, size)
    text = font.render(text, True, color)
    
    return text, text_rect(text, pos_x, pos_y)

def text_rect(text, pos_x, pos_y):
        textRect = text.get_rect()
        textRect.center = (pos_x, pos_y)
        return textRect

# Reset Game Screen
def screen_reset(screen):
    screen.fill((0,0,0))

# Grid draw function
def draw_grid(screen):
    for x in range(0, settings.WIDTH, settings.TILESIZE):
        pg.draw.line(screen, (200, 200, 200), (x, 0), (x, settings.HEIGHT))
    for y in range(0, settings.HEIGHT, settings.TILESIZE):
        pg.draw.line(screen, (200, 200, 200), (0, y), (settings.WIDTH, y))