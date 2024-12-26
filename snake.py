import pygame
from settings import SNAKE_SIZE, WIDTH, HEIGHT


class Snake:
    def __init__(self, x, y, color=(0, 255, 0)):
        # This is a list that stores the coordinates of the snake segments.
        # Initially, the snake consists of three segments arranged horizontally
        self.body = [(x, y), (x - SNAKE_SIZE, y), (x - 2 * SNAKE_SIZE, y)]
        self.direction = (SNAKE_SIZE, 0)  # Initial direction (right)
        self.color = color

    def move(self):
        # Calculates new coordinates of the snake's head, adding an offset in the direction of movement
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])

        # Screen-out check and teleportation
        if new_head[0] < 0:
            new_head = (WIDTH - SNAKE_SIZE, new_head[1])
        elif new_head[0] >= WIDTH:
            new_head = (0, new_head[1])
        if new_head[1] < 0:
            new_head = (new_head[0], HEIGHT - SNAKE_SIZE)
        elif new_head[1] >= HEIGHT:
            new_head = (new_head[0], 0)

        self.body = [new_head] + self.body[:-1]  # Move all the segments of the snake

    def grow(self):
        # Add a new segment to the end of the snake
        self.body.append(self.body[-1])

    # Changes the direction of the snake's movement, unless the new direction is opposite to the current one
    def change_direction(self, direction):
        if direction == "UP" and self.direction != (0, SNAKE_SIZE):
            self.direction = (0, -SNAKE_SIZE)
        elif direction == "DOWN" and self.direction != (0, -SNAKE_SIZE):
            self.direction = (0, SNAKE_SIZE)
        elif direction == "LEFT" and self.direction != (SNAKE_SIZE, 0):
            self.direction = (-SNAKE_SIZE, 0)
        elif direction == "RIGHT" and self.direction != (-SNAKE_SIZE, 0):
            self.direction = (SNAKE_SIZE, 0)

    def check_collision(self):
        return self.body[0] in self.body[1:]  # Checking for collision with body

    def draw(self, screen, x_offset=0):
        for segment in self.body:
            pygame.draw.rect(screen, self.color, (segment[0] + x_offset, segment[1], 10, 10))
