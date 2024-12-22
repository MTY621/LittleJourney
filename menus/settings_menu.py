import pygame
import pygame_menu

import globals

pygame.init()
surface = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))


def settings(menu):
    menu._open(settings_menu)


settings_menu = pygame_menu.Menu('Settings', globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT,
    theme=globals.custom_theme)
settings_menu.add.selector('Sound :', [('ON', 1), ('OFF', 2)])