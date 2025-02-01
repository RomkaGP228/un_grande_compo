import pathlib
import sys
import pygame.font

from data.params import *
from data.button import ButtonClass
from data.slider import Slider
from data.saver import settings_saver, upload_settings


class Draw:
    def __init__(self, screen, world_map, player, map_name):
        self.screen = screen
        self.map_name = map_name
        self.player = player
        self.world_map = world_map
        self.font = pygame.font.SysFont('Tahoma', 36, bold=True)
        self.menu_trigger = False
        self.pause_trigger = False
        self.settings_trigger = False
        self.win_trigger = False
        self.win_picture = pygame.image.load(pathlib.PurePath('images/end_image.jpg')).convert()
        self.pause_picture = pygame.image.load(pathlib.PurePath('images/pause_image.png')).convert()
        self.menu_picture = pygame.image.load(pathlib.PurePath('images/menu_image.jpg')).convert()
        self.textures = {1: pygame.image.load(pathlib.PurePath("textures/texture_1.jpg")).convert(),
                         2: pygame.image.load(pathlib.PurePath("textures/texture_2.jpg")).convert(),
                         3: pygame.image.load(pathlib.PurePath("textures/texture_3.jpg")).convert(),
                         4: pygame.image.load(pathlib.PurePath("textures/texture_4.jpg")).convert(),
                         5: pygame.image.load(pathlib.PurePath("textures/texture_5.jpg")).convert(),
                         6: pygame.image.load(pathlib.PurePath("textures/texture_6.jpg")).convert()}

    def draw_world(self, world_objs):
        for i in sorted(world_objs, key=lambda x: x[0], reverse=True):
            if i[0]:
                _, obj, obj_pos = i
                self.screen.blit(obj, obj_pos)

    def draw_fps(self, clock):
        fps = str(int(clock.get_fps()))
        fps_render = self.font.render(fps, 0, pygame.Color('red'))
        self.screen.blit(fps_render, (window_width - 55, 0))

    def menu(self):
        self.menu_trigger = True
        button_font = pygame.font.Font('fonts/rafale_ru.otf', 70)
        label_font = pygame.font.Font('fonts/mneb.otf', 145)
        start_button = ButtonClass(self.screen, 420, 380, width=400, height=100,
                                   image_path=pathlib.PurePath('images/button_start_image.png'), text='START',
                                   font=button_font)
        exit_button = ButtonClass(self.screen, 420, 500, width=400, height=100,
                                  image_path=pathlib.PurePath('images/button_start_image.png'), text='EXIT',
                                  font=button_font)
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

    def pause(self):
        self.pause_trigger = True
        label_font = pygame.font.Font('fonts/mneb.otf', 145)
        button_font = pygame.font.Font('fonts/rafale_ru.otf', 70)
        exit_button = ButtonClass(self.screen, 420, 500, width=400, height=100,
                                  image_path=pathlib.PurePath('images/button_start_image.png'), text='EXIT',
                                  font=button_font)
        continue_button = ButtonClass(self.screen, 420, 380, width=400, height=100,
                                      image_path=pathlib.PurePath('images/button_start_image.png'), text='CONTINUE',
                                      font=button_font)
        menu_button = ButtonClass(self.screen, 420, 260, width=400, height=100,
                                  image_path=pathlib.PurePath('images/button_start_image.png'), text='MENU',
                                  font=button_font)
        settings_button = ButtonClass(self.screen, 725, 600, width=100, height=100,
                                  image_path=pathlib.PurePath('images/settings_image.png'), text='',
                                  font=button_font)
        save_button = ButtonClass(self.screen, 420, 600, width=100, height=100,
                                  image_path=pathlib.PurePath('images/save_image.png'), text='',
                                  font=button_font)
        while self.pause_trigger:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.pause_picture, (0, 0), (-415, -137, window_width, window_height))
            self.screen.blit(self.pause_picture, (0, 0), (-415, -400, window_width, window_height))
            continue_button.draw()
            exit_button.draw()
            menu_button.draw()
            save_button.draw()
            settings_button.draw()
            label = label_font.render('Pause', 1, pygame.Color('orange'))
            self.screen.blit(label, (443, 100))
            curr_pos = pygame.mouse.get_pos()
            curr_click = pygame.mouse.get_pressed()
            if continue_button.rect.collidepoint(curr_pos):
                if curr_click[0]:
                    self.pause_trigger = False
                    return
            elif exit_button.rect.collidepoint(curr_pos):
                if curr_click[0]:
                    pygame.quit()
                    sys.exit()
            elif menu_button.rect.collidepoint(curr_pos):
                if curr_click[0]:
                    self.menu_trigger = True
                    self.menu()
                    return
            elif save_button.rect.collidepoint(curr_pos):
                if curr_click[0]:
                    saver(self.player.pos, self.player.angle, self.map_name)
                    return
            elif settings_button.rect.collidepoint(curr_pos):
                if curr_click[0]:
                    self.settings()
                    return
            elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.pause_trigger = False
                return
            pygame.display.flip()

    def settings(self):
        self.settings_trigger = True
        label_font = pygame.font.Font('fonts/mneb.otf', 120)
        button_font = pygame.font.Font('fonts/rafale_ru.otf', 60)
        text_font = pygame.font.Font('fonts/mneb.otf', 50)
        volume_slider = Slider(self.screen, 420, 350, 400, 50, 0, 100, upload_settings()[0])
        sense_slider = Slider(self.screen, 420, 450, 400, 50, 0, 100, upload_settings()[1])
        save_button = ButtonClass(self.screen, 420, 520, width=150, height=80,
                                  image_path=pathlib.PurePath('images/button_start_image.png'), text='SAVE',
                                  font=button_font)
        cancel_button = ButtonClass(self.screen, 670, 520, width=150, height=80,
                                  image_path=pathlib.PurePath('images/button_start_image.png'), text='QUIT',
                                  font=button_font)
        while self.settings_trigger:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                sense_slider.handle_event(event)
                volume_slider.handle_event(event)
            self.screen.blit(self.pause_picture, (0, 0), (-415, -137, window_width, window_height))
            self.screen.blit(self.pause_picture, (0, 0), (-415, -400, window_width, window_height))
            volume_slider.draw()
            sense_slider.draw()
            save_button.draw()
            cancel_button.draw()
            label = label_font.render('Settings', 1, pygame.Color('orange'))
            volume_label = text_font.render('Volume', 1, black)
            sensitivity_label = text_font.render('Sensitivity', 1, black)
            self.screen.blit(volume_label, (420, 300))
            self.screen.blit(sensitivity_label, (420, 400))
            self.screen.blit(label, (418, 115))
            curr_pos = pygame.mouse.get_pos()
            curr_click = pygame.mouse.get_pressed()
            if cancel_button.rect.collidepoint(curr_pos):
                if curr_click[0]:
                    self.settings_trigger = False
            elif save_button.rect.collidepoint(curr_pos):
                if curr_click[0]:
                    settings_saver(volume_slider.get_value(), sense_slider.get_value())
                    self.player.update()
                    return
            elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.settings_trigger = False
            pygame.display.flip()
    def win(self):
        print('you win')
        self.win_trigger = True
        button_font = pygame.font.Font('fonts/rafale_ru.otf', 70)
        label_font = pygame.font.Font('fonts/mneb.otf', 145)
        exit_button = ButtonClass(self.screen, 420, 500, width=400, height=100,
                                  image_path=pathlib.PurePath('images/button_start_image.png'), text='EXIT',
                                  font=button_font)
        while self.win_trigger:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.win_picture, (0, 0), (30, 0, window_width, window_height))
            exit_button.draw()
            label = label_font.render('Y0U 3SC4P3D', 1, pygame.Color('orange'))
            self.screen.blit(label, (100, 50))
            curr_pos = pygame.mouse.get_pos()
            curr_click = pygame.mouse.get_pressed()
            if exit_button.rect.collidepoint(curr_pos):
                if curr_click[0]:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()







