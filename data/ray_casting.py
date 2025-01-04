from math import sin, cos, pi

import pygame

from data.params import *
from data.map import *
def mapping(x, y):
    return (x // wall_size) * wall_size, (y // wall_size) * wall_size


def ray_casting(screen, player_pos, player_angle):
    angle = player_angle - view_field_half
    x0, y0 = player_pos
    xam, yam = mapping(x0, y0)
    for ray in range(nums_rays):
        sin_a = sin(angle)
        cos_a = cos(angle)

        if cos_a >= 0:
             x = xam + wall_size
             dx = 1
        else:
            x = xam
            dx = -1

        for _ in range(0, window_width, wall_size):
            dpth_vert = (x - x0) / cos_a
            y = y0 + dpth_vert * sin_a
            if mapping(x + dx, y) in world_map:
                break
            x += dx * wall_size
        if sin_a >= 0:
             y = yam + wall_size
             dy = 1
        else:
            y = yam
            dy = -1
        for _ in range(0, window_height, wall_size):
            dpth_hor = (y - y0) / sin_a
            x = x0 + dpth_hor * cos_a
            if mapping(x, y + dy) in world_map:
                break
            y += dy * wall_size
        if dpth_vert < dpth_hor:
            dpth = dpth_vert
        else:
            dpth = dpth_hor
        dpth *= cos(player_angle - angle)
        wall_ray_height = (distance_to_wall * wall_size) / dpth
        color = 255 / (dpth ** 2 * 0.00001 + 1)
        pygame.draw.rect(screen, (color, color, color), (
        ray * (window_width // nums_rays), (window_height // 2) - (wall_ray_height // 2), window_width // nums_rays,
        wall_ray_height))
        angle += d_rays



