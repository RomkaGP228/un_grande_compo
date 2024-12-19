import pygame
from math import pi, tan
window_width = 1200
window_height = 700
black = pygame.Color("Black")
white = pygame.Color("White")
wall_size = 100

player_pos = (window_width // 2, window_height // 2)
player_angle = 0
player_speed = 2

#ray casting params
view_field = pi / 3
view_field_half = view_field / 2
nums_rays = 120
d_rays = view_field / nums_rays
draw_distance = 1200
distance_to_wall = nums_rays / tan(view_field_half)
scale = window_width / nums_rays
