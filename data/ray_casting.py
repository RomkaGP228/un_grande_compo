from math import sin, cos

import pygame

from data.params import *
from data.map import *
def ray_casting(screen, player_pos, player_angle):
    angle = player_angle - view_field_half
    x, y = player_pos
    for ray in range(nums_rays):
        for dpth in range(1, draw_distance):
            xn = x + dpth * cos(angle)
            yn = y + dpth * sin(angle)
            # pygame.draw.line(screen, white, (x, y), (xn, yn), 2)
            if (xn // 100 * 100, yn // 100 * 100) in world_map:
                wall_ray_height = (distance_to_wall * wall_size) / dpth
                pygame.draw.rect(screen, white, (ray * window_width / nums_rays, (window_height // 2) - wall_ray_height // 2, window_width / nums_rays, wall_ray_height))
                break
        angle += d_rays
