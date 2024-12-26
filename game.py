import pygame
import sys

from snake import Snake
from food import Food, SuperFood
from game_over_screen import GameOverScreen
from colour_picker import ColorPicker

from settings import HEIGHT, GAME_SPEED


class Game:
    def __init__(self, screen, snake_color=(0, 255, 0)):
        self.screen = screen
        self.snake = Snake(100, 100, color=snake_color)
        self.food = Food()
        self.clock = pygame.time.Clock()

        self.super_food = None

        # Width of the scoreboard and playing field
        self.panel_width = 150
        self.field_width = 500

        self.screen = pygame.display.set_mode((650, 500))
        pygame.display.set_caption("Snake game")

        pygame.font.init()

        # Initial level and score settings
        self.level = 1
        self.score = 0

        # Font settings
        self.font = pygame.font.SysFont("Arial", 25, bold=True)
        self.level_font = pygame.font.SysFont("Arial", 25, bold=True)

        self.text_color = (255, 255, 255)  # White text
        self.bg_color = (0, 0, 0)  # Background for the playing field
        self.panel_color = (11, 21, 107)  # Text panel color

    def increase_level(self):
        if self.score % 5 == 0 and self.score != 0:
            self.level += 1
            return True
        return False

    def draw_text(self, text, font, color, x, y, bg_color=None):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)

        if bg_color:
            pygame.draw.rect(self.screen, bg_color, text_rect)

        self.screen.blit(text_surface, text_rect)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Controlling the snake's movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.snake.change_direction("UP")
            if keys[pygame.K_DOWN]:
                self.snake.change_direction("DOWN")
            if keys[pygame.K_LEFT]:
                self.snake.change_direction("LEFT")
            if keys[pygame.K_RIGHT]:
                self.snake.change_direction("RIGHT")

            self.snake.move()

            # Checking for food intake
            if (self.snake.body[0][0] == self.food.x and
                    self.snake.body[0][1] == self.food.y):
                self.snake.grow()
                self.food.spawn()
                self.score += 1

                if self.increase_level():
                    print(f"Level up! Now level up is {self.level}")
                    self.super_food = SuperFood()

            if (self.super_food and self.snake.body[0][0] == self.super_food.x and
                    self.snake.body[0][1] == self.super_food.y):
                self.snake.grow()
                self.score += 3
                self.super_food = None

            if self.snake.check_collision():
                print("Game over!")
                game_over_screen = GameOverScreen(self.screen, self.score)
                while True:
                    game_over_screen.draw()
                    action = game_over_screen.handle_events()
                    if action == "Restart":
                        # Back to choosing the color of the snake
                        color_picker = ColorPicker(self.screen)
                        selected_color = None

                        # Waiting for the user to choose a color
                        while selected_color is None:
                            color_picker.draw()
                            selected_color = color_picker.handle_events()

                        # Creating a new game with the selected color
                        game = Game(self.screen, snake_color=selected_color)
                        game.run()

                    elif action == "Exit":
                        pygame.quit()
                        sys.exit()

            # Game speed updates depending on level
            self.clock.tick(GAME_SPEED + self.level)

            # Drawing on the screen
            self.screen.fill(self.bg_color)
            # Draw the panel on the left
            pygame.draw.rect(self.screen, self.panel_color, (0, 0, self.panel_width, HEIGHT))
            # Drawing the playing field on the right (500x500) shifted to the right
            pygame.draw.rect(self.screen, (0, 0, 0),
                             (self.panel_width, 0, self.field_width, HEIGHT))

            self.snake.draw(self.screen, self.panel_width)
            self.food.draw(self.screen, self.panel_width)
            if self.super_food:
                self.super_food.draw(self.screen, self.panel_width)

            self.draw_text(f"Level: {self.level}", self.level_font,
                           self.text_color, 10, 10, bg_color=(70, 130, 180))

            self.draw_text(f"Scores: {self.score}", self.font, self.text_color, 10, 50,
                           bg_color=(70, 130, 180))

            pygame.display.flip()   # The screen content is updated
