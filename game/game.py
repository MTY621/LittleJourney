from time import sleep

import pygame

import glob
from characters.player import Player
import glob
from glob import SCREEN_WIDTH, SCREEN_HEIGHT
from menus.pause_menu import pause

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (200, 0, 0)

class Game:
    def __init__(self, sprite_name, player_name, curr_menu, song):
        self.player = Player(sprite_name, 100, player_name, [], self)
        self.player_name = player_name
        self.song = song
        pygame.mixer.music.set_volume(0.5)
        if glob.music_is_on:
            pygame.mixer.music.load(self.song)
            pygame.mixer.music.play(-1)
        self.current_menu = curr_menu
        self.background = pygame.image.load('background/castle/1_garden.png').convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.display = pygame.display
        self.pause_button_rect = pygame.Rect(SCREEN_WIDTH - 100, 20, 80, 40)
        self.scroll_x = 0
        self.moving = 0
        self.show_menu = 1

    def draw_pause_button(self):
        """Draw the pause button on the screen."""
        pygame.draw.rect(self.screen, BUTTON_COLOR, self.pause_button_rect)
        font = pygame.font.Font(None, 24)
        text = font.render("Pause", True, WHITE)
        text_rect = text.get_rect(center=self.pause_button_rect.center)
        self.screen.blit(text, text_rect)

    def start(self):
        while True:
            self.screen.blit(self.background, (0, 0))
            #self.draw_pause_button()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.pause_button_rect.collidepoint(event.pos):
                        self.screen.blit(self.background, (0, 0))
                        pause()
            if self.show_menu == 1:
                new_menu = self.current_menu.gameplay_menu(events)
                if new_menu is None:
                    break
                elif new_menu != glob.CONTINUE:
                    self.current_menu = new_menu
                    self.moving = 1
                    self.player.walk(SCREEN_WIDTH // 5)
                    self.show_menu = 0

            if self.moving == 1:
                self.scroll_x -= 5
                self.screen.blit(self.background, (self.scroll_x, 0))
                self.screen.blit(self.background, (self.scroll_x + SCREEN_WIDTH, 0))
                pygame.display.flip()
                if self.scroll_x <= -SCREEN_WIDTH:
                    self.moving = 0
                    self.moving = 0;
                    self.show_menu = 1
            self.draw_pause_button()
            self.player.draw(self.player.sprite, None)
            pygame.display.flip()
            clock.tick(60)

        sleep(2)
        pygame.mixer.quit()
        pygame.quit()
