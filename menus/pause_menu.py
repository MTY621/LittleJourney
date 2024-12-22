import pygame
import pygame_menu

import globals
from settings_menu import settings_menu

pygame.init()
surface = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))


def resume_game():
    pygame.event.post(pygame.event.Event(resume))


def settings_menu_call():
    settings_menu(pause_menu)


# Create menus
pause_menu = pygame_menu.Menu(
    'Pause', globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT, theme=globals.custom_theme)
pause_menu.add.button('Continue', resume_game)
pause_menu.add.button('Settings', settings_menu_call)
pause_menu.add.button('Main menu', pygame_menu.events.EXIT)


left_arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))
right_arrow = pygame_menu.widgets.RightArrowSelection(arrow_size=(10, 15))

resume = pygame.USEREVENT + 1


# Pause menu loop
def pause_menu():
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == resume:
                return 0

            if event.type == pygame.QUIT:
                return 1

        # Handle the main menu
        if pause_menu.is_enabled():
            pause_menu.update(events)  # Update menu widgets
            pause_menu.draw(surface)  # Draw menu widgets on top
            if pause_menu.get_current().get_selected_widget():
                left_arrow.draw(surface, pause_menu.get_current().get_selected_widget())
                right_arrow.draw(surface, pause_menu.get_current().get_selected_widget())

        pygame.display.update()