import pygame
import pygame_menu

import glob

pygame.init()
screen = pygame.display.set_mode((glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT))


def sure(menu, label, next_menu):
    sure_menu = pygame_menu.Menu(label, glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT,
                                 theme=glob.custom_theme)
    sure_menu.add.button('Yes', lambda: sure_menu._open(next_menu))
    sure_menu.add.button('No', lambda: sure_menu.reset(1))

    menu._open(sure_menu)