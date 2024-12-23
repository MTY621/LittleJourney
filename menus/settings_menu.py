import pygame
import pygame_menu

import glob

pygame.init()
surface = pygame.display.set_mode((glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT))

global music_option_widget, sound_effects_option_widget, mixer


def settings(menu, given_mixer):
    global mixer
    mixer = given_mixer
    menu._open(settings_menu)


def sound_selector(value, index, widget=None):
    global music_option_widget, mixer
    if music_option_widget.get_index() == 0:
        mixer.music.unpause()
        glob.music_is_on = True
    else:
        mixer.music.pause()
        glob.music_is_on = False


def effect_selector(value, index, widget=None):
    global sound_effects_option_widget, mixer
    if sound_effects_option_widget.get_index() == 0:
        glob.sound_effects_are_on = True
    else:
        glob.sound_effects_are_on = False


settings_menu = pygame_menu.Menu('Settings', glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT,
    theme=glob.custom_theme)
music_option_widget = settings_menu.add.selector('Sound :', [('ON', 1), ('OFF', 2)], onchange=sound_selector)
sound_effects_option_widget = settings_menu.add.selector('Sound effects:', [('ON', 1), ('OFF', 2)],
                                                         onchange=effect_selector)