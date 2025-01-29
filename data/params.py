import math

import pygame
from math import pi, tan
from data.saver import upload, first_time, saver

# window settings
window_width = 1200
window_height = 700

first_time()

# base colors
black = pygame.Color("Black")
white = pygame.Color("White")


# player params
player_pos, player_angle = upload()
player_speed = 3

# ray casting params
view_field = pi / 3
view_field_half = view_field / 2
nums_rays = 400
wall_size = 100
d_rays = view_field / nums_rays
fake_rays = 50
draw_distance = 100000
distance_to_wall = nums_rays / tan(view_field_half)
scale = window_width // nums_rays
coeff = 2 * distance_to_wall * wall_size
texture_width = 1200
texture_height = 1200
texture_scale = texture_width // wall_size

#sprite settings
double_pi = 2 * math.pi
center_ray = nums_rays // 2 - 1