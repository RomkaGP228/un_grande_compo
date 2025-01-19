import pathlib

import pygame
from params import *

def load_image(image, colorkey=-1):
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

class Sprite:
    def __init__(self):
        self.sprites = pygame.sprite.Group()
        barrel = pygame.sprite.Sprite()
        barrel.image = load_image(pathlib.PurePath("sprites/"))
        barrel.rect = barrel.image.get_rect()
        self.sprites.add(barrel)


class SpriteObject:
    pass