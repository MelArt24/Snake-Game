import pygame
import random
from settings import SNAKE_SIZE, WIDTH, HEIGHT


class Food:
    def __init__(self):
        self.x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        self.y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE

    def spawn(self):
        # A random integer is generated from 0 to the maximum possible value
        self.x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        self.y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE

    def draw(self, screen, x_offset=0):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x + x_offset, self.y, SNAKE_SIZE, SNAKE_SIZE))


class SuperFood(Food):
    def draw(self, screen, x_offset=0):
        pygame.draw.rect(screen, (255, 215, 0), pygame.Rect(self.x + x_offset, self.y, SNAKE_SIZE, SNAKE_SIZE))
