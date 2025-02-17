import os
import pathlib
import sys
import pygame.font

from data.params import *
from data.button import ButtonClass
from data.slider import Slider
from data.saver import settings_saver, upload_settings, time_finder, saver
from data.music import volume_change


class Draw:
    """Класс для отрисовки окон и взаимодействий"""
    def __init__(self, screen, world_map, player, map_name):
        # основные параметры
        self.screen = screen
        self.map_name = map_name
        self.player = player
        self.world_map = world_map
        self.font = pygame.font.SysFont('Tahoma', 36, bold=True)
        self.menu_trigger = False
        self.pause_trigger = False
        self.settings_trigger = False
        self.win_trigger = False
        self.about_trigger = False
        self.win_picture = pygame.image.load(pathlib.PurePath('images/end_image.jpg')).convert()
        self.pause_picture = pygame.image.load(pathlib.PurePath('images/pause_image.png')).convert()
        self.about_window_picture = pygame.image.load(pathlib.PurePath('images/about_window_image.png')).convert()
        self.menu_picture = pygame.image.load(pathlib.PurePath('images/menu_image.jpg')).convert()
        self.qr_code_picture = pygame.image.load(pathlib.PurePath('images/qr_code_image.png')).convert()
        self.textures = {1: pygame.image.load(pathlib.PurePath("textures/texture_1.jpg")).convert(),
                         2: pygame.image.load(pathlib.PurePath("textures/texture_2.jpg")).convert(),
                         3: pygame.image.load(pathlib.PurePath("textures/texture_3.jpg")).convert(),
                         4: pygame.image.load(pathlib.PurePath("textures/texture_4.jpg")).convert(),
                         5: pygame.image.load(pathlib.PurePath("textures/texture_5.jpg")).convert(),
                         6: pygame.image.load(pathlib.PurePath("textures/texture_6.jpg")).convert()}

    def draw_world(self, world_objs):
        # для отрисовки мира
        for i in sorted(world_objs, key=lambda x: x[0], reverse=True):
            if i[0]:
                _, obj, obj_pos = i
                self.screen.blit(obj, obj_pos)

    def draw_fps(self, clock):
        # для отрисовки фпс
        fps = str(int(clock.get_fps()))
        fps_render = self.font.render(fps, 0, pygame.Color('red'))
        self.screen.blit(fps_render, (window_width - 55, 0))

    def menu(self):
        # для отрисовки главного меню игры
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
            label = label_font.render('UN GRANDE COMPO', 1, pygame.Color('orange'))
            self.screen.blit(label, (20, 30))
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
        # для отрисовки меню паузы
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
        about_button = ButtonClass(self.screen, 575, 600, width=100, height=95,
                                   image_path=pathlib.PurePath('images/about_image.png'), text='',
                                   font=button_font)
        while self.pause_trigger:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    saver(self.player.pos, self.player.angle, self.map_name)
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.pause_picture, (0, 0), (-415, -137, window_width, window_height))
            self.screen.blit(self.pause_picture, (0, 0), (-415, -400, window_width, window_height))
            continue_button.draw()
            exit_button.draw()
            menu_button.draw()
            save_button.draw()
            about_button.draw()
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
                    saver(self.player.pos, self.player.angle, self.map_name)
                    pygame.quit()
                    sys.exit()
            elif menu_button.rect.collidepoint(curr_pos):
                if curr_click[0]:
                    self.menu_trigger = True
                    self.menu()
                    return
            elif about_button.rect.collidepoint(curr_pos):
                if curr_click[0]:
                    self.about()
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
        # для отрисовки меню настроек
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
                    saver(self.player.pos, self.player.angle, self.map_name)
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
                    volume_change(volume_slider.get_value())
                    self.player.update()
                    return
            elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.settings_trigger = False
            pygame.display.flip()

    def win(self):
        # для отрисовки окна после прохождения
        self.win_trigger = True
        button_font = pygame.font.Font('fonts/rafale_ru.otf', 70)
        text_font = pygame.font.Font('fonts/mneb.otf', 50)
        label_font = pygame.font.Font('fonts/mneb.otf', 145)
        exit_button = ButtonClass(self.screen, 420, 500, width=400, height=100,
                                  image_path=pathlib.PurePath('images/button_start_image.png'), text='EXIT',
                                  font=button_font)
        time_delta = time_finder()
        while self.win_trigger:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.win_picture, (0, 0), (0, 0, window_width, window_height))
            exit_button.draw()
            label = label_font.render('Y0U 3SC4P3D', 1, pygame.Color('orange'))
            time_played = text_font.render(f"Total gameplay time: {time_delta} hours", 1, pygame.Color("orange"))
            self.screen.blit(time_played, (250, 270))
            self.screen.blit(label, (200, 50))
            curr_pos = pygame.mouse.get_pos()
            curr_click = pygame.mouse.get_pressed()
            if exit_button.rect.collidepoint(curr_pos):
                if curr_click[0]:
                    pygame.quit()
                    os.remove(pathlib.PurePath("db/database.db"))
                    os.rmdir(pathlib.PurePath("db"))
                    sys.exit()
            pygame.display.flip()

    def about(self):
        # для отрисовки меню справки
        self.about_trigger = True
        label_font = pygame.font.Font('fonts/mneb.otf', 120)
        button_font = pygame.font.Font('fonts/rafale_ru.otf', 60)
        text_font = pygame.font.Font('fonts/mneb.otf', 50)
        text_font_1 = pygame.font.Font('fonts/mneb.otf', 30)
        exit_button = ButtonClass(self.screen, 800, 600, width=400, height=100,
                                  image_path=pathlib.PurePath('images/button_start_image.png'), text='EXIT',
                                  font=button_font)
        while self.about_trigger:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.about_window_picture, (0, 0), (0, 0, window_width, window_height))
            self.screen.blit(self.qr_code_picture, (0, 0), (0, -455, window_width, window_height))
            exit_button.draw()
            label = label_font.render('About', 1, pygame.Color('orange'))
            repo_label = text_font.render('Repo', 1, black)
            plot_label = text_font.render('Goals', 1, black)
            control_text_1 = text_font_1.render('wasd buttons - Base character control.', 1, black)
            control_text_2 = text_font_1.render('Mouse or arrows buttons - camera control.', 1, black)
            plot_text = text_font_1.render('Your main goal is to find the goal and the military', 1, white)
            control_label = text_font.render('Control', 1, black)
            self.screen.blit(repo_label, (70, 400))
            self.screen.blit(plot_label, (230, 150))
            self.screen.blit(plot_text, (20, 230))
            self.screen.blit(control_label, (830, 150))
            self.screen.blit(label, (470, 0))
            self.screen.blit(control_text_1, (670, 230))
            self.screen.blit(control_text_2, (670, 300))
            curr_pos = pygame.mouse.get_pos()
            curr_click = pygame.mouse.get_pressed()
            if exit_button.rect.collidepoint(curr_pos):
                if curr_click[0]:
                    self.about_trigger = False
            elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.about_trigger = False
            pygame.display.flip()
