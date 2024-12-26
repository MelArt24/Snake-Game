import pygame
import sys
from menu import Menu


class ColorPicker(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.title_font = pygame.font.SysFont(None, 60)

        self.colors = {
            "Green": (0, 255, 0),
            "Yellow": (255, 255, 0),
            "White": (255, 255, 255),
            "Blue": (0, 191, 255),
            "Orange": (255, 165, 0),
        }

        # Buttons creation
        screen_width, screen_height = self.screen.get_size()
        button_width, button_height = 200, 50
        button_spacing = 20
        self.buttons = []
        for i, (label, color) in enumerate(self.colors.items()):
            rect = pygame.Rect(
                (screen_width - button_width) // 2,
                (screen_height // 2) - ((button_height + button_spacing) * 2) + i * (button_height + button_spacing),
                button_width,
                button_height,
            )
            self.buttons.append({"label": label, "color": color, "rect": rect})

    def draw(self):
        self.screen.fill(self.bg_color)
        screen_width, screen_height = self.screen.get_size()

        title_text = self.title_font.render("Choose Snake Color", True, self.text_color)
        title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 4 - 60))
        self.screen.blit(title_text, title_rect)    # a method that transfers images and text to the screen

        for button in self.buttons:
            button_color = button["color"]
            pygame.draw.rect(self.screen, button_color, button["rect"], border_radius=15)

            text_color = (0, 0, 0) if button_color == (255, 255, 255) else self.text_color  # (255, 255, 255) = white

            text_surface = self.font.render(button["label"], True, text_color)
            text_rect = text_surface.get_rect(center=button["rect"].center)
            self.screen.blit(text_surface, text_rect)

        pygame.display.flip()   # The screen content is updated

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # If the user clicks the mouse, it checks whether the cursor is over the button
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button["rect"].collidepoint(event.pos):
                        return button["color"]
        return None
