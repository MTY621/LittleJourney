# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep

import pygame
from pygame_menu.examples.other.image_background import main_menu

from characters.player import Player
from menus.main_menu import menu
from globals import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

if __name__ == '__main__':
    menu()
    background = pygame.image.load('background/castle/1_garden.png').convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    i = 10
    player = Player("Human", 100, "Player", [])
    clock = pygame.time.Clock()
    while i > 0:
        screen.blit(background, (0, 0))
        i -= 1

        player.attack(screen, pygame.display)
        sleep(1)
        player.take_damage(screen, 10, pygame.display)

        clock.tick(60)

    pygame.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
