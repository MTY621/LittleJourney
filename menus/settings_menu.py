import pygame
import pygame_menu

import globals

pygame.init()
surface = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))

global sound_option_widget, mixer


def settings(menu, given_mixer):
    global mixer
    mixer = given_mixer
    menu._open(settings_menu)


def sound_selector(value, index, widget=None):
    global sound_option_widget, mixer
    if sound_option_widget.get_index() == 0:
        mixer.music.unpause()
        globals.music_is_on = True
    else:
        mixer.music.pause()
        globals.music_is_on = False


settings_menu = pygame_menu.Menu('Settings', globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT,
    theme=globals.custom_theme)
sound_option_widget = settings_menu.add.selector('Sound :', [('ON', 1), ('OFF', 2)], onchange=sound_selector)