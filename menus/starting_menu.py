import pygame
import pygame_menu

import globals
from globals import used_save_slots

pygame.init()
surface = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))

global index, player_name_widget, save_slot_widget, player_race_widget
index = 0


def save_attr():
    # Get the values from the text inputs
    player_name = player_name_widget.get_value()
    save_slot_name = save_slot_widget.get_value()
    if player_race_widget.get_index() == -1:
        player_race = 'Human'
    else:
        player_race = player_race_widget.get_value()

    # Set the player name in globals
    globals.player_name = player_name

    # Set the player race in globals
    globals.player_race = player_race

    # Delete the old save slot name in globals
    del used_save_slots[globals.def_names[index]]
    globals.def_names[index] = save_slot_name

    # Set the save slot name in globals
    used_save_slots[save_slot_name] = 1

    print(globals.player_name)
    print(globals.player_race)
    print(used_save_slots)


def set_save_attr(menu, given_index):
    global index
    index = given_index
    menu._open(starting_menu)


starting_menu = pygame_menu.Menu('New game', globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT,
    theme=globals.custom_theme)
save_slot_widget = starting_menu.add.text_input('Save slot name: ', default=globals.def_names[index])
player_name_widget = starting_menu.add.text_input('Name: ', default='Little John')
player_race_widget = starting_menu.add.dropselect("Select a race", [('Human', 0), ('Elf', 1), ('Orc', 2)])
starting_menu.add.button('Continue', save_attr)