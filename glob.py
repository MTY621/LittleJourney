import pygame
import pygame_menu
from pygame import Color

# walking bar colour codes
VILLAGE_FOUNTAIN_COLOUR = (172, 172, 172)
TEMPLE_COLOUR = (219, 194, 111)
DESERT_COLOUR = (214, 165, 85)
ICE_COLOUR = (177, 172, 194)

# backgrounds
VILLAGE_BACKGROUND = "background/castle/1_garden.png"

TEMPLE_BACKGROUND_1 = "background/temple/3_temple_entrance.png"
TEMPLE_BACKGROUND_2 = "background/temple/4_temple_ruin.png"
TEMPLE_BACKGROUND_3 = "background/temple/2_temple_structure.png"
TEMPLE_BACKGROUND_4 = "background/temple/1_temple.png"

DESERT_BACKGROUND_1 = "background/desert/3_oasis.png"
DESERT_BACKGROUND_2 = "background/desert/2_desert_lake.png"
DESERT_BACKGROUND_3 = "background/desert/1_waterfall_desert.png"
DESERT_BACKGROUND_4 = "background/desert/4_desert_river.png"

ICE_BACKGROUND_1 = "background/ice/1_snowy_rocks_hd.png"
ICE_BACKGROUND_2 = "background/ice/5_snowy_trees_hd.png"
ICE_BACKGROUND_3 = "background/ice/6_snow_forest_path_hd.png"
ICE_BACKGROUND_4 = "background/ice/3_frozen_lake_hd.png"
ICE_BACKGROUND_5 = "background/ice/4_ice_breaker_rock_hd.png"

# environment music
VILLAGE_MUSIC = "music/safe_room_theme.flac"
TEMPLE_MUSIC = "music/tribal.wav"
DESERT_MUSIC = "music/hold_the_line.flac"
ICE_MUSIC = "music/battle-march.wav"

# walking sound effects
VILLAGE_WALK = "step_stone_1.wav"
TEMPLE_WALK = "step_wood_1.wav"
DESERT_WALK = "step_dirt_7.wav"
ICE_WALK = "step_snow_2.wav"

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1200
CHARACTER_WIDTH = 170
CHARACTER_HEIGHT = 200
ACTION_FRAMES = 60

MAIN_MENU_SONG = 'music/little_town_reinstrumented.ogg'
CURRENT_GAME_SONG = VILLAGE_MUSIC

#return codes
EXIT_MENU = pygame.USEREVENT + 100
MAIN_MENU = 1
CONTINUE = 2
DEATH = 3
GAME_ENDED = 4

used_save_slots = {"Slot 1" : 0, "Slot 2" : 0, "Slot 3" : 0, "Slot 4" : 0, "Slot 5" : 0}
def_names = ["Slot 1", "Slot 2", "Slot 3", "Slot 4", "Slot 5"]
player_name = "Alex"
player_race = "Human"
music_is_on = True
sound_effects_are_on = True
same_npc = False
can_continue = False
swords = [("Rusty sword", 10), ("Iron sword", 70), ("Templar sword", 120) ,("Knight sword", 150), ("Dark Lord sword", 200)]
shields = [("Wooden shield", 10), ("Iron shield", 70), ("Templar shield", 120), ("Knight shield", 150), ("Dark Lord shield", 200)]

# Themes
custom_theme = pygame_menu.themes.Theme(
    background_color = (0, 0, 0, 0),  # Fully transparent background
    title_font_shadow_color = (0, 0, 0),
    title_font_shadow_offset = 2,
    title_font = "fonts/ByteBounce.ttf",
    title_font_size = 80,
    widget_font = "fonts/ByteBounce.ttf",
    widget_font_size = 70,
    widget_font_color = Color('#666666'),
    widget_box_arrow_color = Color('#666666'),
    widget_font_shadow = True,
    widget_font_shadow_color = (0, 0, 0),
    widget_font_shadow_offset = 2,
)

custom_play_theme = pygame_menu.themes.Theme(
    background_color = (0, 0, 0, 0),  # Fully transparent background
    title = False,  # Disable the title
    title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE,  # No title bar
    widget_font = "fonts/ByteBounce.ttf",
    widget_font_size = 70,
    widget_font_color = Color('#666666'),
    widget_font_shadow = True,
    widget_font_shadow_color = (0, 0, 0),
    widget_font_shadow_offset = 2,
    widget_offset = (0, 100)
)

# Function to get the key at a given index
def get_key_at_index(index):
    keys = list(used_save_slots.keys())  # Convert keys to a list
    return keys[index]
