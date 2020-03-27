import sqlite3

connection = sqlite3.connect('db/game.db')
cursor = connection.cursor()

def showHighscores():
    # Select all from db
    cursor.execute("SELECT * FROM highscore ORDER BY SCORE DESC;")
    result = cursor.fetchall()
    
    return result