import pygame
import data.params as pr


class ButtonClass:
    def __init__(self, screen, x, y, width, height, image_path, text, font, after_image_path=None, sound_path=None):
        # main params
        self.screen = screen
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.text = text
        self.font = font
        # image params
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        # if cursor pointed on button we show after_image
        self.after_image = self.image
        if after_image_path:
            self.after_image = pygame.image.load(after_image_path)
            self.after_image = pygame.transform.scale(self.after_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        # if button clicked we play click_sound
        self.click_sound = None
        if sound_path:
            self.click_sound = pygame.mixer.Sound(sound_path)
        self.pointed = False

    def draw(self):
        # image blit
        curr_image = self.after_image if self.pointed else self.image
        self.screen.blit(curr_image, self.rect.topleft)
        # text params
        text_render = self.font.render(self.text, 0, pr.white)
        text_rect = text_render.get_rect(center=self.rect.center)
        self.screen.blit(text_render, text_rect)

    def check_point(self, curr_pos):
        # checking that curr on button surface
        self.pointed = self.rect.collidepoint(curr_pos)

    def event_handler(self, event):
        # checking event and checking that left button clicked and curr on button surface
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.pointed:
            if self.click_sound:
                self.click_sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
