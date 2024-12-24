from time import sleep

import pygame

from characters.player import Player
from menus.main_menu import menu
from glob import SCREEN_WIDTH, SCREEN_HEIGHT
import menus.story_menus.story_menu
from menus.story_menus.gameplay_menus import gameplay_menu, menu_1
import extra_info

pygame.init()
pygame.mixer.init()
extra_info.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
extra_info.\
    display = pygame.display

if __name__ == '__main__':
    menu()
    extra_info.background = pygame.image.load('background/castle/1_garden.png').convert()
    extra_info.background = pygame.transform.scale(extra_info.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # i = 4
    clock = pygame.time.Clock()
    extra_info.player = Player("Human", 100, "Player", [])
    cur_menu = menu_1
    while True:
        extra_info.screen.blit(extra_info.background, (0, 0))
        cur_menu = gameplay_menu(cur_menu)
        if cur_menu is None:
            break
        # i -= 1
        #
        # player.attack(screen, pygame.display, background)
        # sleep(0.5)
        # player.take_damage(screen, 25, pygame.display, background)
        # sleep(0.5)

        clock.tick(60)

    sleep(2)
    pygame.mixer.quit()
    pygame.quit()

# npc update suport spriteuri si sunete
# tranzitie fundal