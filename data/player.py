from math import sin, cos, pi


from data.params import *
class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.sense = 0.005

    @property
    def pos(self):
        return (int(self.x), int(self.y))

    def movement(self):
        self.keys_movement()
        self.mouse_movement()
        self.angle %= pi * 2

    def keys_movement(self):
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

    def mouse_movement(self):
        if pygame.mouse.get_focused():
             diff_mouse = pygame.mouse.get_pos()[0] - (window_width // 2)
             pygame.mouse.set_pos((window_width // 2, window_height // 2))
             self.angle += diff_mouse * self.sense