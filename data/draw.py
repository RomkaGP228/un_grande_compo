import pathlib
import sys
import pygame.font

from data.ray_casting import ray_casting
from data.params import *
from data.button import ButtonClass
class Draw:
    def __init__(self, screen, world_map):
        self.screen = screen
        self.world_map = world_map
        self.font = pygame.font.SysFont('Tahoma', 36, bold=True)
        self.menu_trigger = True
        self.menu_picture = pygame.image.load(pathlib.PurePath('images/menu_image.jpg')).convert()

    def draw_world(self, player_pos, player_angle):
        ray_casting(self.screen, player_pos, player_angle)

    def draw_fps(self, clock):
        fps = str(int(clock.get_fps()))
        fps_render = self.font.render(fps, 0, pygame.Color('red'))
        self.screen.blit(fps_render, (window_width - 55, 0))

    def menu(self):
        x = 0
        button_font = pygame.font.Font('fonts/rafale_ru.otf', 70)
        label_font = pygame.font.Font('fonts/mneb.otf', 145)
        start_button = ButtonClass(self.screen, 420, 380, width= 400, height=100,
                            image_path=pathlib.PurePath('images/button_start_image.png'), text='START', font=button_font)
        exit_button = ButtonClass(self.screen, 420, 500, width=400, height=100,
                            image_path=pathlib.PurePath('images/button_start_image.png'), text='EXIT', font=button_font)
        while self.menu_trigger:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.menu_picture, (0, 0), (30, 0, window_width, window_height))
            start_button.draw()
            exit_button.draw()
            label = label_font.render('Un grande compo', 1, pygame.Color('orange'))
            self.screen.blit(label, (100, 50))
            curr_pos = pygame.mouse.get_pos()
            curr_click = pygame.mouse.get_pressed()
            if start_button.rect.collidepoint(curr_pos):
                if curr_click[0]:
                    self.menu_trigger = False
            elif exit_button.rect.collidepoint(curr_pos):
                if curr_click[0]:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()





