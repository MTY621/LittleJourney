from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes

import globals

pygame.init()
surface = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))

# Load and scale the background image
background = pygame.image.load('../background/cave/background4.png').convert()
background = pygame.transform.scale(background, (globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))


def drop_loading_menu(value=None, index=None, widget=None):
    loading_menu()


def new_game():
    print("new game")


# Navigate to level menu
def loading_menu():
    mainmenu._open(loading)
    pygame.time.set_timer(update_loading, 10)


# Navigate to level menu
def load_save_menu():
    mainmenu._open(load_save)


def settings_menu():
    mainmenu._open(settings)


# Create menus
mainmenu = pygame_menu.Menu(
    'Main menu', globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT, theme=globals.custom_theme)
mainmenu.add.button('Play', new_game)
mainmenu.add.button('Load', load_save_menu)
mainmenu.add.button('Settings', settings_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)


load_save = pygame_menu.Menu('Load game', globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT,
    theme=globals.custom_theme)
load_save.add.dropselect("Select a save slot", [("Slot 1", 1), ("Slot 2", 2), ("Slot 3", 3), ("Slot 4", 4), ("Slot 5", 5)],
                         onchange=drop_loading_menu)


settings = pygame_menu.Menu('Settings', globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT,
    theme=globals.custom_theme)
settings.add.selector('Sound :', [('ON', 1), ('OFF', 2)])


loading = pygame_menu.Menu('Loading the Game...', globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT,
    theme=globals.custom_theme)
loading.add.progress_bar("Progress", progressbar_id="1", default=0, width=200)


left_arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))
right_arrow = pygame_menu.widgets.RightArrowSelection(arrow_size=(10, 15))

update_loading = pygame.USEREVENT + 0


# Main menu loop
def menu():
    i = 1
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == update_loading:
                print(i, 'ok1')
                i+=1
                progress = loading.get_widget("1")
                progress.set_value(progress.get_value() + 1)
                if progress.get_value() == 100:
                    print(i, 'ok2')
                    pygame.time.set_timer(update_loading, 0)  # Stop the timer
                    progress.set_value(0)  # Reset progress bar
                    loading.disable()  # Disable the loading menu
                    mainmenu.enable()  # Enable the main menu
                    surface.fill((0, 0, 0))  # Fill the surface with black
                    sleep(5)
            if event.type == pygame.QUIT:
                exit()

        # Handle the main menu
        if mainmenu.is_enabled():
            print(i, 'ok3', mainmenu.get_current().get_selected_widget())
            surface.blit(background, (0, 0))  # Ensure the background is drawn before the menu
            mainmenu.update(events)  # Update menu widgets
            mainmenu.draw(surface)  # Draw menu widgets on top
            if (mainmenu.get_current().get_selected_widget()):
                left_arrow.draw(surface, mainmenu.get_current().get_selected_widget())
                right_arrow.draw(surface, mainmenu.get_current().get_selected_widget())

        pygame.display.update()

# Run the menu function
menu()
