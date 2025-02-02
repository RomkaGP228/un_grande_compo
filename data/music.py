from random import choice
import pathlib
import pygame
from data.saver import upload_settings


def play_track():
    # для проигрывания треков, рандомный выбор без повторений
    bimbo = ''
    lst = ['song_1', 'song_2', 'song_3']
    track = choice(lst)
    while track == bimbo:
        track = choice(lst)
    bimbo = track
    pygame.mixer.music.load(pathlib.PurePath(f"sounds/{track}.mp3"))
    pygame.mixer.music.set_volume(float(upload_settings()[0]) / 100)
    pygame.mixer.music.play()


def volume_change(volume):
    print(volume)
    pygame.mixer.music.set_volume(float(volume) / 100)
