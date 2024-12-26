from menu import Menu
import pygame
import sys


class GameOverScreen(Menu):
    def __init__(self, screen, score):
        super().__init__(screen)
        self.title_font = pygame.font.SysFont(None, 80)
        self.score = score

        screen_width, screen_height = self.screen.get_size()
        button_width, button_height = 200, 50

        # A list with two buttons
        self.buttons = [
            {
                "label": "Restart",
                "rect": pygame.Rect(
                    (screen_width - button_width) // 2,
                    (screen_height // 2) - button_height + 20,
                    button_width,
                    button_height,
                ),
            },
            {
                "label": "Exit",
                "rect": pygame.Rect(
                    (screen_width - button_width) // 2,
                    (screen_height // 2) + 40,
                    button_width,
                    button_height,
                ),
            },
        ]

    def draw(self):
        self.screen.fill(self.bg_color)

        screen_width, screen_height = self.screen.get_size()

        title_text = self.title_font.render("Game Over", True, self.text_color)
        title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 4))
        self.screen.blit(title_text, title_rect)

        score_text = self.font.render(f"Score: {self.score}", True, self.text_color)
        score_rect = score_text.get_rect(center=(screen_width // 2, screen_height // 4 + 60))
        self.screen.blit(score_text, score_rect)

        for button in self.buttons:
            pygame.draw.rect(self.screen, self.button_color, button["rect"], border_radius=15)
            text_surface = self.font.render(button["label"], True, self.text_color)
            text_rect = text_surface.get_rect(center=button["rect"].center)
            self.screen.blit(text_surface, text_rect)

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # If the user clicks the mouse, it checks whether the cursor is over the button
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button["rect"].collidepoint(event.pos):
                        return button["label"]
        return None
