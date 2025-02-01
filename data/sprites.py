import math
import pathlib
import os
import sys
import pygame
from data.params import *

def load_image(name, colorkey=None):
    fullname = os.path.join('sprites', name)
    image = pygame.image.load(fullname)
    # если файл не существует, то выходим
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

class SpriteClass:
    def __init__(self):
        self.sprites_list = {'barrel': load_image('test/img.png'),
                             'guy': [load_image(f"guy/{i}.png", -1) for i in range(8)],
                             'portal': load_image(f'portal/portal.png', -1)}
        self.obj_list = [SpriteObjClass(self.sprites_list['portal'], True, (8.7, 12.5), -3, 0.4)]



class SpriteObjClass:
    def __init__(self, object, static, pos, shift, scale):
        self.object = object
        self.static = static
        self.shift = shift
        self.scale = scale
        self.pos = self.x, self.y = pos[0] * wall_size, pos[1] * wall_size
        if not static:
            self.sprite_angles = [frozenset(range(i, i + 45)) for i in range(0, 368, 45)]
            self.sprite_pos = {angle: pos for angle, pos in zip(self.sprite_angles, self.object)}

    def object_locate(self, player, walls):
        fake_walls0 = [walls[0] for i in range(fake_rays)]
        fake_walls1 = [walls[-1] for i in range(fake_rays)]
        fake_walls = fake_walls0 + walls + fake_walls1
        dx, dy = self.x - player.x, self.y - player.y
        distance_to_sprite = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
        phi = math.atan2(dy, dx)
        gamma = phi - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += double_pi

        delta_rays = int(gamma / d_rays)
        cur_ray = center_ray + delta_rays
        distance_to_sprite *= math.cos(view_field_half - cur_ray * d_rays)

        fake_ray = cur_ray + fake_rays
        if 0 <= fake_ray <= nums_rays - 1 + 2 * fake_rays and distance_to_sprite < fake_walls[fake_ray][0]:
            proj_height = int(coeff / distance_to_sprite * self.scale)
            shift = proj_height // 2 * self.shift

            if not self.static:
                if phi < 0:
                    phi += double_pi
                phi = 360 - int(math.degrees(phi))

                for i in self.sprite_angles:
                    if phi in i:
                        self.object = self.sprite_pos[i]
                        break

            sprite_pos = (cur_ray * scale - proj_height // 2, window_height // 2 - proj_height // 2 + shift)
            sprite = pygame.transform.scale(self.object, (proj_height, proj_height * 4))
            return (distance_to_sprite, sprite, sprite_pos)
        else:
            return (False,)




