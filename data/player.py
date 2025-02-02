from math import sin, cos

from data.params import *
from data.map import collision_walls
from data.saver import upload_settings


class Player:
    """Класс для всего связанного с игроком"""
    def __init__(self):
        # основные параметры
        self.x, self.y = player_pos
        self.angle = player_angle
        self.sense = 0.00006 * (float(upload_settings()[-1]) + 1)
        self.side = 50
        self.rect = pygame.Rect(*player_pos, self.side, self.side)

    @property
    def pos(self):
        # для возврата текущей позиции
        return (int(self.x), int(self.y))

    def set_pos(self, position_x, position_y):
        # для установки новой позиции
        self.x, self.y = position_x, position_y

    def set_angle(self, angle):
        self.angle = angle

    def detected_collision(self, dx, dy):
        # для нахождения коллизий
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hitted = next_rect.collidelistall(collision_walls)
        if len(hitted):
            delta_x, delta_y = 0, 0
            for i in hitted:
                rect_hitted = collision_walls[i]
                if dx > 0:
                    delta_x += next_rect.right - rect_hitted.left
                else:
                    delta_x += rect_hitted.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - rect_hitted.top
                else:
                    delta_y += rect_hitted.bottom - next_rect.top
            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_x < delta_y:
                dx = 0
        self.x += dx
        self.y += dy

    def movement(self):
        # для осуществления движения
        self.keys_movement()
        self.mouse_movement()
        self.rect.center = self.x, self.y
        self.angle %= pi * 2

    def keys_movement(self):
        # для отработки клавишь и мышки при перемещении
        keykaps = pygame.key.get_pressed()
        if keykaps[pygame.K_w]:
            dx = player_speed * cos(self.angle)
            dy = player_speed * sin(self.angle)
            self.detected_collision(dx, dy)
        if keykaps[pygame.K_a]:
            dx = player_speed * sin(self.angle)
            dy = -player_speed * cos(self.angle)
            self.detected_collision(dx, dy)
        if keykaps[pygame.K_s]:
            dx = -player_speed * cos(self.angle)
            dy = -player_speed * sin(self.angle)
            self.detected_collision(dx, dy)
        if keykaps[pygame.K_d]:
            dx = -player_speed * sin(self.angle)
            dy = player_speed * cos(self.angle)
            self.detected_collision(dx, dy)
        if keykaps[pygame.K_LEFT]:
            self.angle -= 0.05
        if keykaps[pygame.K_RIGHT]:
            self.angle += 0.05
        self.angle %= double_pi

    def mouse_movement(self):
        if pygame.mouse.get_focused():
            diff_mouse = pygame.mouse.get_pos()[0] - (window_width // 2)
            pygame.mouse.set_pos((window_width // 2, window_height // 2))
            self.angle += diff_mouse * self.sense

    def update(self):
        self.sense = 0.00006 * (float(upload_settings()[-1]) + 1)
