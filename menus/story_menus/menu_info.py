import pygame
import pygame_menu

import glob
from glob import used_save_slots, get_key_at_index
from menus.settings_menu import settings
from menus.starting_menu import set_save_attr, starting_menu
from menus.sure_menu import sure
from characters.player import Player
from characters.chill_npc import ChillNpc
from characters.fighting_npc import FightingNpc

global player
# Initialize Pygame
pygame.init()


class StoryMenu:
    def __init__(self, npc):
        self.npc = npc

    def player_attack(self):
        player.attack()
        self.npc.take_damage(player.atk)

    def npc_attack(self):
        self.npc.attack()
        player.take_damage(player.atk)

    def text_display(self, text):
