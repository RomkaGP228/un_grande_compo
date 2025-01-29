import sqlite3
import pathlib
from datetime import datetime

def first_time():
    connection = sqlite3.connect(pathlib.PurePath("db/database.db"))
    cur = connection.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS base (
    pos   TEXT NOT NULL,
    angle NUMERIC NOT NULL,
    time  TEXT NOT NULL UNIQUE
);""")
    cur.execute("SELECT * FROM base ORDER BY time DESC LIMIT 1")
    data = cur.fetchall()
    if len(data) == 0:
        saver('(150, 150)', 90)
    connection.commit()
    connection.close()


def saver(player_position, player_anglenow):
    connection = sqlite3.connect(pathlib.PurePath("db/database.db"))
    cur = connection.cursor()
    cur.execute("INSERT INTO base(pos, angle, time) VALUES (?, ?, ?)", (str(player_position), player_anglenow, datetime.now()))
    connection.commit()
    connection.close()

def upload():
    connection = sqlite3.connect(pathlib.PurePath("db/database.db"))
    cur = connection.cursor()
    cur.execute("SELECT * FROM base ORDER BY time DESC LIMIT 1")
    data = cur.fetchall()
    print(data)
    player_pos_new = tuple(map(int, data[0][0][1:-1].split(', ')))
    print(player_pos_new)
    player_angle_new = data[0][1]
    return player_pos_new, player_angle_new

