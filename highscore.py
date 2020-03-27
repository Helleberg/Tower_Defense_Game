import sqlite3
import pygame as pg
import functions
import settings

connection = sqlite3.connect('db/game.db')
cursor = connection.cursor()

def showHighscores():
    # Select all from db
    cursor.execute("SELECT * FROM highscore ORDER BY SCORE DESC;")
    result = cursor.fetchall()
    
    return result

def saveHighscore():
    pass

def highscores(screen):
    highscores = showHighscores()[:-1]
        
    text, rect = functions.draw_text(
        'Highscores', 
        'assets/fonts/PressStart2P.ttf', 
        26, (255, 255, 255),
        settings.WIDTH // 2, settings.HEIGHT - (settings.HEIGHT - 100)
    )
    screen.blit(text, rect)

    text_offset = 160
    for score in highscores:
        text, rect = functions.draw_text(
            f"Points: {score[1]} | Level: {score[2]}", 
            'assets/fonts/PressStart2P.ttf', 
            20, (255, 255, 255), 
            settings.WIDTH // 2, settings.HEIGHT - (settings.HEIGHT - text_offset)
        )
        screen.blit(text, rect)
        text_offset += 60
    pg.display.update()
