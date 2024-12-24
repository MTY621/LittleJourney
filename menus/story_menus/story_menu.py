import pygame
import pygame_menu

import glob
import extra_info


# Initialize Pygame
pygame.init()


class StoryMenu:
    def __init__(self, npc, next_menus):
        self.npc = npc
        self.menu = pygame_menu.Menu("", glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT, theme=glob.custom_play_theme)
        self.menus = next_menus
        self.next_menu = None


    def player_attack(self):
        print(11)
        extra_info.player.attack()
        self.npc.take_damage(extra_info.player.atk)


    def npc_attack(self):
        self.npc.attack()
        extra_info.player.take_damage(extra_info.player.atk)


    def get_items(self, items):
        for item in items:
            #add to inventory
            pass


    def add_text_display(self, labels, index):
        for label in labels:
            self.menu.add.label(label)
        self.next_menu =  self.menus[index]


    def add_button(self, text, function, index):
        self.menu.add.button(text, function)
        self.next_menu = self.menus[index]

