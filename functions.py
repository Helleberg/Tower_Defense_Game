import pygame as pg

# Text draw function
def draw_text(text, text_font, size, color, pos_x, pos_y):
    font = pg.font.Font(text_font, size)
    text = font.render(text, True, color)
    
    return text, text_rect(text, pos_x, pos_y)

def text_rect(text, pos_x, pos_y):
        textRect = text.get_rect()
        textRect.center = (pos_x, pos_y)
        return textRect