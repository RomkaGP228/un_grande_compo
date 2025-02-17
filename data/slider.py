import pygame


class Slider:
    """Класс реализующий ползунок (который в настройках)"""
    def __init__(self, screen, x, y, width, height, min_val, max_val, default_val):
        # основные параметры
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.knob = pygame.Rect(x, y, height, height)
        self.min_val = min_val
        self.max_val = max_val
        self.value = float(default_val)
        self.update_knob_position()
        self.dragging = False

    def update_knob_position(self):
        # для обновления текущего положения ползунка
        knob_x = self.rect.x + (self.value - self.min_val) / (self.max_val - self.min_val) * (
                self.rect.width - self.rect.height)
        self.knob.x = knob_x

    def draw(self):
        # для отрисовки ползунка
        pygame.draw.rect(self.screen, (200, 200, 200), self.rect)
        pygame.draw.rect(self.screen, (0, 0, 255), self.knob)

    def handle_event(self, event):
        # база
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.knob.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.knob.x = max(self.rect.left, min(event.pos[0], self.rect.right - self.rect.height))
                self.value = self.min_val + (self.knob.x - self.rect.x) / (self.rect.width - self.rect.height) * (
                        self.max_val - self.min_val)

    def get_value(self):
        # для возврата текущего значения ползунка
        return self.value
