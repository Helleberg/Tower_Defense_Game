import sqlite3
connection = sqlite3.connect('game.db')

cursor = connection.cursor()

# delete
cursor.execute("""DROP TABLE highscore;""")

# Create table highscore
sql_command = """
    CREATE TABLE highscore(
        id INTEGER PRIMARY KEY,
        score FLOAT,
        level INTEGER,
        date_created DATE
    );
"""

cursor.execute(sql_command)

connection.commit()
connection.close()