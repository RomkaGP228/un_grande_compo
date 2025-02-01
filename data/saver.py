import sqlite3
import pathlib
from datetime import datetime
import os


def first_time():
    try:
        os.mkdir('db')
    except FileExistsError:
        print("Папка 'db' уже существует.")
    except OSError as error:
        print(f"Возникла ошибка при создании папки 'db': {error}")
    connection = sqlite3.connect(pathlib.PurePath("db/database.db"))
    cur = connection.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS base (
    pos   TEXT NOT NULL,
    angle NUMERIC NOT NULL,
    time  TEXT NOT NULL UNIQUE,
    map TEXT NOT NULL
);""")
    cur.execute("""CREATE TABLE IF NOT EXISTS settings (
        volume TEXT,
        sensitivity TEXT
    );""")
    cur.execute("SELECT * FROM base ORDER BY time DESC LIMIT 1")
    data = cur.fetchall()
    if len(data) == 0:
        saver('(150, 150)', 90, 'second_map')
    cur.execute("SELECT * FROM settings DESC LIMIT 1")
    data_set = cur.fetchall()
    if len(data_set) == 0:
        cur.execute("""INSERT INTO settings (volume, sensitivity) VALUES (?, ?)""", (10, 1))
    connection.commit()
    connection.close()


def saver(player_position, player_anglenow, map_now):
    connection = sqlite3.connect(pathlib.PurePath("db/database.db"))
    cur = connection.cursor()
    cur.execute("INSERT INTO base(pos, angle, time, map) VALUES (?, ?, ?, ?)",
                (str(player_position), player_anglenow, datetime.now(), map_now))
    connection.commit()
    connection.close()


def upload():
    connection = sqlite3.connect(pathlib.PurePath("db/database.db"))
    cur = connection.cursor()
    cur.execute("SELECT * FROM base ORDER BY time DESC LIMIT 1")
    data = cur.fetchall()
    player_pos_new = tuple(map(int, data[0][0][1:-1].split(', ')))
    player_angle_new = data[0][1]
    connection.close()
    return player_pos_new, player_angle_new


def upload_map():
    connection = sqlite3.connect(pathlib.PurePath("db/database.db"))
    cur = connection.cursor()
    cur.execute("SELECT * FROM base ORDER BY time DESC LIMIT 1")
    data = cur.fetchall()
    map_new = data[0][3]
    connection.close()
    return map_new


def settings_saver(volume, sense):
    connection = sqlite3.connect(pathlib.PurePath("db/database.db"))
    cur = connection.cursor()
    cur.execute("UPDATE settings SET volume = ?, sensitivity = ?",
                (volume, sense))
    connection.commit()
    connection.close()


def upload_settings():
    connection = sqlite3.connect(pathlib.PurePath("db/database.db"))
    cur = connection.cursor()
    cur.execute("SELECT * FROM settings DESC LIMIT 1")
    data = cur.fetchall()
    connection.close()
    return data[0][0], data[0][1]


def time_finder():
    connection = sqlite3.connect(pathlib.PurePath("db/database.db"))
    cur = connection.cursor()
    cur.execute("SELECT * FROM base ORDER BY time LIMIT 1")
    time_start = datetime.strptime(cur.fetchall()[0][2], "%Y-%m-%d %H:%M:%S.%f")
    total_hours = (datetime.now() - time_start).total_seconds() / 3600
    connection.close()
    return f"{total_hours:.2f}"
