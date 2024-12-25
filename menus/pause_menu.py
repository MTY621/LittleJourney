import pygame
import pygame_menu

import glob
import game.game
from settings_menu import settings_menu

pygame.init()
pygame.mixer.init()
surface = pygame.display.set_mode((glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT))

pygame.mixer.music.load('music/safe_room_theme.flac')
pygame.mixer.music.set_volume(0.5)  # Set volume (0.0 to 1.0)


def resume_game():
    pygame.event.post(pygame.event.Event(resume))


def settings_menu_call():
    settings_menu(pause_menu, pygame.mixer)


# Create menus
pause_menu = pygame_menu.Menu(
    'Pause', glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT, theme=glob.custom_theme)
pause_menu.add.button('Continue', resume_game)
pause_menu.add.button('Settings', settings_menu_call)
pause_menu.add.button('Main menu', pygame_menu.events.EXIT)


left_arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))
right_arrow = pygame_menu.widgets.RightArrowSelection(arrow_size=(10, 15))

resume = pygame.USEREVENT + 1


# Pause menu loop
def pause_menu(game):
    pause_menu.enable()
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == resume:
                pause_menu.disable()
                pygame.mixer.music.load(game.song)
                pygame.mixer.music.play(-1)
                return glob.CONTINUE

            if event.type == pygame.QUIT:
                pause_menu.disable()
                pygame.mixer.music.load(glob.MAIN_MENU_SONG)
                pygame.mixer.music.play(-1)
                return glob.MAIN_MENU

        # Handle the main menu
        if pause_menu.is_enabled():
            pause_menu.update(events)  # Update menu widgets
            pause_menu.draw(surface)  # Draw menu widgets on top
            if pause_menu.get_current().get_selected_widget():
                left_arrow.draw(surface, pause_menu.get_current().get_selected_widget())
                right_arrow.draw(surface, pause_menu.get_current().get_selected_widget())

        pygame.display.update()