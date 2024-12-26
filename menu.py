import pygame
import abc


class Menu(abc.ABC):
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 40)
        self.bg_color = (11, 21, 107)
        self.button_color = (70, 130, 180)
        self.text_color = (255, 255, 255)

    @abc.abstractmethod
    def draw(self):
        pass

    @abc.abstractmethod
    def handle_events(self):
        pass
