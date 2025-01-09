import pygame
import pygame_menu

import glob
from glob import used_save_slots, get_key_at_index
from menus.settings_menu import settings
from menus.starting_menu import set_save_attr, starting_menu
from menus.sure_menu import sure

pygame.init()
screen = pygame.display.set_mode((glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT))

# Load and scale the background image
background = pygame.image.load('background/normal/3_mountain.png').convert()
background = pygame.transform.scale(background, (glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT))


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
        pygame.event.post(pygame.event.Event(glob.EXIT_MENU))


def new_game():
    glob.can_continue = True
    main_menu._open(starting_menu)
    # main_menu._open(new_game_menu)


def continue_game():
    if glob.can_continue:
        pygame.event.post(pygame.event.Event(glob.EXIT_MENU))


def loading_menu():
    main_menu._open(loading)
    pygame.time.set_timer(update_loading, 10)


def drop_loading_menu(value=None, index=None, widget=None):
    loading_menu()


def load_save():
    main_menu._open(load_save_menu)


def settings_menu_call():
    settings(main_menu, pygame.mixer)


def credits_menu_call():
    main_menu._open(credits_menu)


# Create menus
main_menu = pygame_menu.Menu(
    'Main menu', glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT, theme=glob.custom_theme)
main_menu.add.button('New game', new_game)
main_menu.add.button('Continue', continue_game)
# main_menu.add.button('Load', load_save)
main_menu.add.button('Settings', settings_menu_call)
main_menu.add.button('Credits', credits_menu_call)
main_menu.add.button('Exit', pygame_menu.events.EXIT)


new_game_menu = pygame_menu.Menu('New game', glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT,
    theme=glob.custom_theme)
new_game_menu.add.dropselect("Select a save slot", [(get_key_at_index(0), 0), (get_key_at_index(1), 1),
                        (get_key_at_index(2), 2), (get_key_at_index(3), 3), (get_key_at_index(4), 4)],
                         onchange=drop_new_game_menu)


loading = pygame_menu.Menu('Loading the Game...', glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT,
    theme=glob.custom_theme)
loading.add.progress_bar("Progress", progressbar_id="1", default=0, width=200)


load_save_menu = pygame_menu.Menu('Load game', glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT,
    theme=glob.custom_theme)
load_save_menu.add.dropselect("Select a save slot", [(get_key_at_index(0), 0), (get_key_at_index(1), 1),
                        (get_key_at_index(2), 2), (get_key_at_index(3), 3), (get_key_at_index(4), 4)],
                         onchange=drop_loading_menu)


credits_menu = pygame_menu.Menu('Credits', glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT,
    theme=glob.custom_theme)
# Add text to the credits menu
credits_menu.add.label('Game developed by\nBelciug Matei\nBigan Radu-Cristin\n')
credits_menu.add.label('Background images from\nwww.craftpix.net\n')
credits_menu.add.label('Character graphics from\nwww.opengameart.org\nwww.craftpix.net\n')
credits_menu.add.label('Item images from\nwww.craftpix.net\n')
credits_menu.add.label('Background music from\nwww.opengameart.org\n')
credits_menu.add.label('Sound effects from\nwww.opengameart.org\n')
credits_menu.add.label('Text font from\nwww.1001fonts.com\n')


left_arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))
right_arrow = pygame_menu.widgets.RightArrowSelection(arrow_size=(10, 15))

update_loading = pygame.USEREVENT + 0
# exit_menu = pygame.USEREVENT + 1


# Main menu loop
def main_menu_start():
    # Load background music
    pygame.mixer.init()
    pygame.mixer.music.load(glob.MAIN_MENU_SONG)
    pygame.mixer.music.set_volume(0.3)  # Set volume (0.0 to 1.0)

    if glob.music_is_on:
        pygame.mixer.music.play(-1)

    main_menu.enable()
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

            if event.type == glob.EXIT_MENU:
                main_menu.disable()
                pygame.mixer.music.stop()
                return glob.EXIT_MENU

            if event.type == glob.GAME_ENDED:
                main_menu.disable()
                pygame.mixer.music.stop()
                return glob.GAME_ENDED

            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                pygame.quit()
                exit()

        # Handle the active menu
        if main_menu.is_enabled():  # Otherwise, handle the main menu
            screen.blit(background, (0, 0))  # Ensure the background is drawn before the menu
            main_menu.update(events)  # Update menu widgets
            main_menu.draw(screen)  # Draw menu widgets on top
            if main_menu.get_current().get_selected_widget():
                left_arrow.draw(screen, main_menu.get_current().get_selected_widget())
                right_arrow.draw(screen, main_menu.get_current().get_selected_widget())

        pygame.display.update()

# Run the menu function
# menu()
