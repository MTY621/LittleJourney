from time import sleep

import pygame
import time

from utils import get_audio_length
from characters.player import Player
import glob
from glob import SCREEN_WIDTH, SCREEN_HEIGHT
from menus.pause_menu import pause

pygame.init()
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (200, 0, 0)


class Game:
    def __init__(self, sprite_name, player_name, curr_menu, song):
        self.player = Player(sprite_name, 100, player_name, self)
        self.player_name = player_name

        self.song = song
        # Get the duration of the music
        self.music_duration = get_audio_length(self.song)

        self.current_menu = curr_menu

        # Adjust the background to leave space for the yellow rectangle
        self.background = pygame.image.load('background/castle/1_garden.png').convert()
        self.background_height = int(SCREEN_HEIGHT * 0.88)  # Adjusted to fit 80% of the screen
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, self.background_height))
        self.bottom_rectangle_color = glob.VILLAGE_FOUNTAIN_COLOUR

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.display = pygame.display
        self.pause_button_rect = pygame.Rect(SCREEN_WIDTH - 100, 20, 80, 40)
        self.scroll_x = 0
        self.moving = 0
        self.show_menu = 1
        self.next_sword = 0
        self.next_shield = 0

    def draw_pause_button(self):
        """Draw the pause button on the screen."""
        pygame.draw.rect(self.screen, BUTTON_COLOR, self.pause_button_rect)
        font = pygame.font.Font(None, 24)
        text = font.render("Pause", True, WHITE)
        text_rect = text.get_rect(center=self.pause_button_rect.center)
        self.screen.blit(text, text_rect)

    def draw_bottom_rectangle(self):
        """Draw a yellow rectangle at the bottom 20% of the screen."""
        rect_height = int(SCREEN_HEIGHT * 0.12)  # 20% of screen height
        rect_y = SCREEN_HEIGHT - rect_height  # Position it at the bottom
        pygame.draw.rect(self.screen, self.bottom_rectangle_color, (0, rect_y, SCREEN_WIDTH, rect_height))

    def start(self):
        # Load background music
        pygame.mixer.init()
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.set_volume(0.3)  # Set volume (0.0 to 1.0)

        if glob.music_is_on:
            pygame.mixer.music.play(-1)

        while True:
            # Draw the adjusted background and yellow rectangle
            self.screen.fill(BLACK)  # Clear the screen first
            self.screen.blit(self.background, (0, 0))
            self.draw_bottom_rectangle()
            self.draw_pause_button()

            events = pygame.event.get()
            for event in events:
                self.player.inventory.handle_event(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.pause_button_rect.collidepoint(event.pos):
                        pygame.mixer.music.pause()
                        music_pos = pygame.mixer.music.get_pos() / 1000
                        pygame.mixer.music.stop()

                        self.screen.blit(self.background, (0, 0))
                        pause_ret = pause(self.background)

                        if pause_ret == glob.MAIN_MENU:
                            return glob.MAIN_MENU

                        if glob.music_is_on:
                            pygame.mixer.music.load(self.song)
                            pygame.mixer.music.play(-1)

            if self.show_menu == 1:
                new_menu = self.current_menu.gameplay_menu(events)
                if new_menu is None:
                    return glob.GAME_ENDED
                elif new_menu != glob.CONTINUE:
                    self.current_menu = new_menu[0]
                    transition = new_menu[1]
                    if transition:
                        self.transition(new_menu[2], new_menu[3], new_menu[4], new_menu[5])
                    if not glob.same_npc and transition != 1:
                        self.moving = 1
                        self.player.walk()
                        self.show_menu = 0

            if self.moving == 1:
                self.scroll_x -= 5
                self.screen.blit(self.background, (self.scroll_x, 0))
                self.screen.blit(self.background, (self.scroll_x + SCREEN_WIDTH, 0))
                # pygame.display.update()
                if self.scroll_x <= -SCREEN_WIDTH:
                    self.moving = 0
                    self.show_menu = 1
                    self.scroll_x = 0

            self.draw_pause_button()
            self.player.draw()
            pygame.display.update()
            clock.tick(60)

    def transition(self, new_background_file, bar_color, new_song, new_walking_sound):
        new_background = pygame.image.load(new_background_file).convert()
        new_background = pygame.transform.scale(new_background, (SCREEN_WIDTH, SCREEN_HEIGHT * 0.88))
        black_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        black_surface.fill((0, 0, 0))

        # Dimensions for the blue bar
        bar_height = SCREEN_HEIGHT * 0.12

        # Transition step size
        step = 30

        # Black screen enters from the right
        for x in range(SCREEN_WIDTH, -1, -step):
            self.screen.blit(black_surface, (x, 0))  # Draw black surface moving in
            pygame.display.flip()
            clock.tick(60)  # Uncomment and replace fps if you want to limit frame rate

        # Background and blue bar enter from the left
        for x in range(0, SCREEN_WIDTH + 1, step):
            self.screen.fill((0, 0, 0))  # Clear screen to black

            # Draw part of the background
            self.screen.blit(new_background, (0, 0), (0, 0, x, SCREEN_HEIGHT - bar_height))

            # Draw the blue bar rolling in
            pygame.draw.rect(
                self.screen,
                bar_color,
                pygame.Rect(0, SCREEN_HEIGHT - bar_height, x, bar_height)
            )

            pygame.display.flip()
            clock.tick(60)
        self.background = new_background
        self.bottom_rectangle_color = bar_color
        self.song = new_song
        self.player.sound = 'sound_effects/main_character/steps/'+ new_walking_sound
        if glob.music_is_on:
            pygame.mixer.music.load(self.song)
            pygame.mixer.music.play(-1)

