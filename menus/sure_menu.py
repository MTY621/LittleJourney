import pygame
import pygame_menu

import globals

pygame.init()
surface = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))


def sure(menu, label, next_menu):
    sure_menu = pygame_menu.Menu(label, globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT,
                                 theme=globals.custom_theme)
    sure_menu.add.button('Yes', lambda: sure_menu._open(next_menu))
    sure_menu.add.button('No', lambda: sure_menu.reset(1))

    menu._open(sure_menu)