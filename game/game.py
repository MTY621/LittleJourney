from time import sleep

import pygame

from characters.player import Player
from glob import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

class Game:
    def __init__(self, sprite_name, player_name, curr_menu):
        self.player = Player(sprite_name, 100, player_name, [], self)
        self.current_menu = curr_menu
        self.background = pygame.image.load('background/castle/1_garden.png').convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.display = pygame.display

    def start(self):
        while True:
            self.screen.blit(self.background, (0, 0))
            self.current_menu = self.current_menu.gameplay_menu()
            if self.current_menu is None:
                break
            clock.tick(60)

        sleep(2)
        pygame.mixer.quit()
        pygame.quit()
