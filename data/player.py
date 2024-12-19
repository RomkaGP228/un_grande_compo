import pygame
from math import sin, cos
from data.params import *


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    def move(self):
        keykaps = pygame.key.get_pressed()
        if keykaps[pygame.K_w]:
            self.x += player_speed * cos(self.angle)
            self.y += player_speed * sin(self.angle)
        if keykaps[pygame.K_a]:
            self.x += player_speed * sin(self.angle)
            self.y += -player_speed * cos(self.angle)
        if keykaps[pygame.K_s]:
            self.x += -player_speed * cos(self.angle)
            self.y += -player_speed * sin(self.angle)
        if keykaps[pygame.K_d]:
            self.x += -player_speed * sin(self.angle)
            self.y += player_speed * cos(self.angle)
        if keykaps[pygame.K_LEFT]:
            self.angle -= 0.05
        if keykaps[pygame.K_RIGHT]:
            self.angle += 0.05
    @property
    def pos(self):
        return (int(self.x), int(self.y))
