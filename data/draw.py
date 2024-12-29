import pygame.font

from data.ray_casting import ray_casting
from data.params import *
class Draw:
    def __init__(self, screen, world_map):
        self.screen = screen
        self.world_map = world_map
        self.font = pygame.font.SysFont('Tahoma', 36, bold=True)

    def draw_world(self, player_pos, player_angle):
        ray_casting(self.screen, player_pos, player_angle)

    def draw_fps(self, clock):
        fps = str(int(clock.get_fps()))
        fps_render = self.font.render(fps, 0, pygame.Color('red'))
        self.screen.blit(fps_render, (window_width - 55, 0))
