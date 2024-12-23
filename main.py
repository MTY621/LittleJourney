from time import sleep

import pygame

from characters.player import Player
from menus.main_menu import menu
from glob import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

if __name__ == '__main__':
    menu()
    background = pygame.image.load('background/castle/1_garden.png').convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    i = 4
    player = Player("Human", 100, "Player", [])
    clock = pygame.time.Clock()
    while i > 0:
        screen.blit(background, (0, 0))
        i -= 1

        player.attack(screen, pygame.display, background)
        sleep(0.5)
        player.take_damage(screen, 25, pygame.display, background)
        sleep(0.5)

        clock.tick(60)

    sleep(2)
    pygame.mixer.quit()
    pygame.quit()

# setari efecte oprit pornit
# npc update suport spriteuri si sunete
# tranzitie fundal