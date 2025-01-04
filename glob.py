import pygame_menu
from pygame import Color
from pygame_menu.utils import widget_terminal_title

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1200
CHARACTER_WIDTH = 32
CHARACTER_HEIGHT = 32
ACTION_FRAMES = 60

MAIN_MENU_SONG = 'music/little_town_reinstrumented.ogg'
CURRENT_GAME_SONG = 'music/battle-march.wav'

#return codes
MAIN_MENU = 1
CONTINUE = 2
DEATH = 3

used_save_slots = {"Slot 1" : 0, "Slot 2" : 0, "Slot 3" : 0, "Slot 4" : 0, "Slot 5" : 0}
def_names = ["Slot 1", "Slot 2", "Slot 3", "Slot 4", "Slot 5"]
player_name = "Alex"
player_race = "Human"
music_is_on = True
sound_effects_are_on = True

custom_theme = pygame_menu.themes.Theme(
    background_color = (0, 0, 0, 0),  # Fully transparent background
    title_font = pygame_menu.font.FONT_8BIT,
    title_font_size = 50,
    widget_font = pygame_menu.font.FONT_8BIT,
    widget_font_color = Color('#404040'),
    widget_box_arrow_color = Color('#404040'),
    widget_font_shadow = True,
    widget_font_shadow_color = (0, 0, 0),
    widget_font_shadow_offset = 2,
)

custom_play_theme = pygame_menu.themes.Theme(
    background_color = (0, 0, 0, 0),  # Fully transparent background
    title = False,  # Disable the title
    title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE,  # No title bar
    title_font = pygame_menu.font.FONT_8BIT,
    title_font_size = 50,
    widget_font = pygame_menu.font.FONT_8BIT,
    widget_font_color = Color('#404040'),
    widget_font_shadow = True,
    widget_font_shadow_color = (0, 0, 0),
    widget_font_shadow_offset = 2,
)

# Function to get the key at a given index
def get_key_at_index(index):
    keys = list(used_save_slots.keys())  # Convert keys to a list
    return keys[index]
