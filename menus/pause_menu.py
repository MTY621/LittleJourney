import pygame
import pygame_menu

import glob
from menus.settings_menu import settings

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT))


def resume_game():
    pygame.event.post(pygame.event.Event(resume))


def settings_menu_call():
    settings(pause_menu, pygame.mixer)


def return_to_main_menu():
    pygame.event.post(pygame.event.Event(main_menu_ret))


# Create menus
pause_menu = pygame_menu.Menu(
    'Pause', glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT, theme=glob.custom_theme)
pause_menu.add.button('Continue', resume_game)
pause_menu.add.button('Settings', settings_menu_call)
pause_menu.add.button('Main menu', return_to_main_menu)


left_arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))
right_arrow = pygame_menu.widgets.RightArrowSelection(arrow_size=(10, 15))

resume = pygame.USEREVENT + 0
main_menu_ret = pygame.USEREVENT + 1


# Pause menu loop
def pause(background):
    pygame.mixer.music.load('music/safe_room_theme.flac')
    pygame.mixer.music.set_volume(0.3)  # Set volume (0.0 to 1.0)

    if glob.music_is_on:
        pygame.mixer.music.play(-1)

    pause_menu.enable()
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == resume:
                pause_menu.disable()
                pygame.mixer.music.stop()
                return glob.CONTINUE

            if event.type == main_menu_ret:
                pause_menu.disable()
                pygame.mixer.music.stop()
                return glob.MAIN_MENU

        # Handle the main menu
        if pause_menu.is_enabled():
            screen.blit(background, (0, 0))  # Ensure the background is drawn before the menu
            pause_menu.update(events)  # Update menu widgets
            pause_menu.draw(screen)  # Draw menu widgets on top
            if pause_menu.get_current().get_selected_widget():
                left_arrow.draw(screen, pause_menu.get_current().get_selected_widget())
                right_arrow.draw(screen, pause_menu.get_current().get_selected_widget())

        pygame.display.update()