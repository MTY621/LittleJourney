from time import sleep

import pygame

import glob
from characters.player import Player
from menus.main_menu import menu
from glob import SCREEN_WIDTH, SCREEN_HEIGHT
import menus.story_menus.story_menu
from menus.story_menus.gameplay_menus import menus
from characters.npcs.chill_npcs import chill_npcs
from characters.npcs.fighting_npcs import fighting_npcs
from game.game import Game

# pygame.init()
# pygame.mixer.init()
# extra_info.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# extra_info.\
#     display = pygame.display

if __name__ == '__main__':
    menu()
    game = Game(glob.player_race, glob.player_name, menus[1])
    for chill_npc in chill_npcs:
        chill_npc.game = game
    for fighting_npc in fighting_npcs:
        fighting_npc.game = game
    for menu in menus:
        menu.game = game
    # extra_info.background = pygame.image.load('background/castle/1_garden.png').convert()
    # extra_info.background = pygame.transform.scale(extra_info.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    game.start()
    # i = 4
    # clock = pygame.time.Clock()
    # extra_info.player = Player("Human", 100, "Player", [])
    # cur_menu = menu_1
    # while True:
    #     extra_info.screen.blit(extra_info.background, (0, 0))
    #     cur_menu = gameplay_menu(cur_menu)
    #     if cur_menu is None:
    #         break
    #     # i -= 1
    #     #
    #     # player.attack(screen, pygame.display, background)
    #     # sleep(0.5)
    #     # player.take_damage(screen, 25, pygame.display, background)
    #     # sleep(0.5)
    #
    #     clock.tick(60)
    #
    # sleep(2)
    # pygame.mixer.quit()
    # pygame.quit()

# npc update suport spriteuri si sunete
# tranzitie fundal