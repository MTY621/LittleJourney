import pygame
import pygame_menu

import glob
from glob import used_save_slots

pygame.init()
surface = pygame.display.set_mode((glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT))

global index, player_name_widget, save_slot_widget, player_race_widget
index = 0


def save_attr():
    # Get the values from the text inputs
    player_name = player_name_widget.get_value()
    # save_slot_name = save_slot_widget.get_value()
    if player_race_widget.get_index() == -1:
        player_race = 'Human'
    else:
        player_race = player_race_widget.get_value()[0][0]

    # Set the player name in glob
    glob.player_name = player_name

    # Set the player race in glob
    glob.player_race = player_race

    # Delete the old save slot name in glob
    # del used_save_slots[glob.def_names[index]]
    # glob.def_names[index] = save_slot_name

    # Set the save slot name in glob
    # used_save_slots[save_slot_name] = 1

    print("ok")
    print(glob.player_name)
    print(glob.player_race)
    print(used_save_slots)

    pygame.event.post(pygame.event.Event(glob.EXIT_MENU))
    starting_menu.reset(1)


def set_save_attr(menu, given_index):
    global index
    index = given_index
    menu._open(starting_menu)


starting_menu = pygame_menu.Menu('New game', glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT,
    theme=glob.custom_theme)
# save_slot_widget = starting_menu.add.text_input('Save slot name: ', default=glob.def_names[index])
player_name_widget = starting_menu.add.text_input('Name: ', default='Little John')
player_race_widget = starting_menu.add.dropselect("Select a race", [('Human', 0), ('Elf', 1), ('Orc', 2)])
starting_menu.add.button('Continue', save_attr)