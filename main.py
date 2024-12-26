import pygame

from game import Game
from main_menu import MainMenu
from colour_picker import ColorPicker


def main():
    pygame.init()
    screen = pygame.display.set_mode((650, 500))
    pygame.display.set_caption("Snake game")
    menu = MainMenu(screen)

    while True:
        menu.draw()
        action = menu.handle_events()
        if action == "start":
            color_picker = ColorPicker(screen)
            selected_color = None

            while selected_color is None:
                color_picker.draw()
                selected_color = color_picker.handle_events()

            game = Game(screen, snake_color=selected_color)
            game.run()


if __name__ == "__main__":
    main()
