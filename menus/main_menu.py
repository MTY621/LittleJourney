import pygame
import pygame_menu

import globals
from globals import used_save_slots, get_key_at_index
from menus.settings_menu import settings
from menus.starting_menu import set_save_attr, starting_menu
from menus.sure_menu import sure

pygame.init()
surface = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))

# Load and scale the background image
background = pygame.image.load('../background/normal/3_mountain.png').convert()
background = pygame.transform.scale(background, (globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))


def drop_new_game_menu(value, index, widget=None):
    selected_key = get_key_at_index(index)

    if selected_key not in used_save_slots:
        new_game_menu.add.label("Invalid save slot selected")  # Handle invalid keys gracefully
        return

    if used_save_slots[selected_key] == 1:
        starting_menu.index = index
        sure(new_game_menu, "Are you sure you want to overwrite this save?", starting_menu)
    else:
        set_save_attr(new_game_menu, index)


def new_game():
    main_menu._open(new_game_menu)


def old_game():
    print("old game")


def loading_menu():
    main_menu._open(loading)
    pygame.time.set_timer(update_loading, 10)


def drop_loading_menu(value=None, index=None, widget=None):
    loading_menu()


def load_save():
    main_menu._open(load_save_menu)


def settings_menu_call():
    settings(main_menu)


def credits_menu_call():
    main_menu._open(credits_menu)


# Create menus
main_menu = pygame_menu.Menu(
    'Main menu', globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT, theme=globals.custom_theme)
main_menu.add.button('New game', new_game)
main_menu.add.button('Continue', old_game)
main_menu.add.button('Load', load_save)
main_menu.add.button('Settings', settings_menu_call)
main_menu.add.button('Credits', credits_menu_call)
main_menu.add.button('Exit', pygame_menu.events.EXIT)


new_game_menu = pygame_menu.Menu('New game', globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT,
    theme=globals.custom_theme)
new_game_menu.add.dropselect("Select a save slot", [(get_key_at_index(0), 0), (get_key_at_index(1), 1),
                        (get_key_at_index(2), 2), (get_key_at_index(3), 3), (get_key_at_index(4), 4)],
                         onchange=drop_new_game_menu)


loading = pygame_menu.Menu('Loading the Game...', globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT,
    theme=globals.custom_theme)
loading.add.progress_bar("Progress", progressbar_id="1", default=0, width=200)


load_save_menu = pygame_menu.Menu('Load game', globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT,
    theme=globals.custom_theme)
load_save_menu.add.dropselect("Select a save slot", [(get_key_at_index(0), 0), (get_key_at_index(1), 1),
                        (get_key_at_index(2), 2), (get_key_at_index(3), 3), (get_key_at_index(4), 4)],
                         onchange=drop_loading_menu)


credits_menu = pygame_menu.Menu('Credits', globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT,
    theme=globals.custom_theme)
# Add text to the credits menu
credits_menu.add.label('Game developed by\nBelciug Matei\nBigan Radu Cristin\n')
credits_menu.add.label('Graphics by\n')
credits_menu.add.label('Music by\n')


left_arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))
right_arrow = pygame_menu.widgets.RightArrowSelection(arrow_size=(10, 15))

update_loading = pygame.USEREVENT + 0


# Main menu loop
def menu():
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == update_loading:
                progress = loading.get_widget("1")
                progress.set_value(progress.get_value() + 1)

                if progress.get_value() == 100:
                    pygame.time.set_timer(update_loading, 0)  # Stop the timer
                    progress.set_value(0)  # Reset the progress bar

                    # Ensure the loading menu is properly closed and main_menu is active
                    loading.disable()  # Disable the loading menu
                    loading.reset(1)  # Reset loading menu widgets for safety
                    main_menu.enable()  # Enable the main menu

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Handle the active menu
        if main_menu.is_enabled():  # Otherwise, handle the main menu
            surface.blit(background, (0, 0))  # Ensure the background is drawn before the menu
            main_menu.update(events)  # Update menu widgets
            main_menu.draw(surface)  # Draw menu widgets on top
            if main_menu.get_current().get_selected_widget():
                left_arrow.draw(surface, main_menu.get_current().get_selected_widget())
                right_arrow.draw(surface, main_menu.get_current().get_selected_widget())

        pygame.display.update()

# Run the menu function
menu()
