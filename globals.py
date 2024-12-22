import pygame_menu
from pygame import Color

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1200

used_save_slots = {"Slot 1" : 0, "Slot 2" : 0, "Slot 3" : 0, "Slot 4" : 0, "Slot 5" : 0}
def_names = ["Slot 1", "Slot 2", "Slot 3", "Slot 4", "Slot 5"]
player_name = ""
player_race = ""

custom_theme = pygame_menu.themes.Theme(
    background_color = (0, 0, 0, 0),  # Fully transparent background
    title_font = pygame_menu.font.FONT_8BIT,
    widget_font = pygame_menu.font.FONT_8BIT,
    widget_font_color = Color('#69696E'),
    title_font_size = 50,
)


# Function to get the key at a given index
def get_key_at_index(index):
    keys = list(used_save_slots.keys())  # Convert keys to a list
    return keys[index]
