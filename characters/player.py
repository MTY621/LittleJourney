import glob
from time import sleep
from collections import deque
import pygame
import random

from characters.health import HealthBar
from glob import CHARACTER_WIDTH, CHARACTER_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, DEATH
from inventory.inventory import Inventory


class Player:
    def __init__(self, sprite_name, hp, name, game):

        path = "characters/character_images/main_character/" + sprite_name + "/"
        self.sprite = pygame.image.load(path + "default.png").convert_alpha()
        print(self.sprite.get_size())
        self.sprite = self.scale(self.sprite)
        print(self.sprite.get_size())
        self.attack_sprite = pygame.image.load(path + "attack.png").convert_alpha()
        self.attack_sprite = self.scale(self.attack_sprite)
        self.hurt_sprite = pygame.image.load(path + "hurt.png").convert_alpha()
        self.hurt_sprite = self.scale(self.hurt_sprite)
        self.death_sprite = pygame.image.load(path + "death.png").convert_alpha()
        self.death_sprite = self.scale(self.death_sprite)
        self.walking_sprite = pygame.image.load(path + "walking.png").convert_alpha()
        self.walking_sprite = self.scale(self.walking_sprite)
        self.current_sprite = self.sprite
        self.current_effect = None
        self.status = deque()
        self.last_song = None
        self.no_sound_effect = True
        self.count = 0
        self.music_pos = 0

        path = "sound_effects/main_character/"
        self.sound = path + "steps/step_dirt_7.wav"
        self.attack_sound = path + "whoosh.wav"
        self.hurt_sound = path + "pain.wav"
        self.death_sound = path + "death.wav"

        self.coin_sprite = pygame.image.load("items/coin.png").convert_alpha()
        self.coin_sprite = pygame.transform.scale(self.coin_sprite, (70, 50))
        self.atk = 3
        self.defense = 0
        self.hp = hp
        self.health_bar_hp = hp
        self.total_hp = hp
        self.money = 10
        self.name = name
        self.inventory = Inventory(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.game = game
        self.health_bar = HealthBar(100, 170, 20)

    def scale(self, image):
        image = pygame.transform.scale(image, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
        return image

    def draw(self):
        self.draw_coins()
        self.inventory.draw(self.game.screen)
        self.health_bar.draw(self.game.screen, self.health_bar_hp, SCREEN_WIDTH * 0.13, SCREEN_HEIGHT * 0.88 - CHARACTER_HEIGHT - 40)
        if len(self.status) > 0:
            curr_status = self.status[0][0]
            if curr_status == "walk":
                self.current_effect = self.sound
                if self.current_sprite != self.walking_sprite:

                    if self.count >= glob.ACTION_FRAMES / 3:
                        self.current_sprite = self.walking_sprite
                        self.count = 0
                else:
                    if self.count >= 20:
                        self.current_sprite = self.sprite
                        self.count = 0
                self.count += 1
            elif curr_status == "attack":
                if self.current_sprite != self.sprite:
                    if self.count == glob.ACTION_FRAMES / 2:
                        self.current_sprite = self.sprite
                        self.count = 0
                else:
                    if self.count == glob.ACTION_FRAMES / 2:
                        self.current_sprite = self.attack_sprite
                        self.count = 0
                self.count += 1
                self.current_effect = self.attack_sound
            elif curr_status == "hurt":
                self.current_sprite = self.hurt_sprite
                self.current_effect = self.hurt_sound
                if self.count == 0:
                    self.health_bar_hp -= self.status[0][2]
                self.count += 1
            elif curr_status == "death":
                self.current_sprite = self.death_sprite
                self.current_effect = self.death_sound
                if self.count == 0:
                    self.health_bar_hp -= self.status[0][2]
                self.count += 1

            if self.no_sound_effect and glob.sound_effects_are_on:
                pygame.mixer.music.pause()
                self.music_pos = pygame.mixer.music.get_pos() / 1000
                pygame.mixer.music.load(self.current_effect)
                pygame.mixer.music.play(-1, fade_ms=int(self.status[0][1] * 1000 / 60))
                self.last_song = self.current_effect
                self.no_sound_effect = False

            self.status[0][1] -= 1
            if self.status[0][1] == 0:
                self.status.popleft()
                self.no_sound_effect = True
                self.count = 0
        else:
            self.current_sprite = self.sprite
            if glob.music_is_on and self.last_song != self.game.song:
                pygame.mixer.music.load(self.game.song)
                pygame.mixer.music.play(-1, start = self.music_pos)
                self.last_song = self.game.song
        self.game.screen.blit(self.current_sprite, (SCREEN_WIDTH * 0.13, SCREEN_HEIGHT * 0.88 - CHARACTER_HEIGHT))

    def draw_coins(self):
        # Define the font and size for the coin counter
        font = pygame.font.Font(None, 36)  # You can specify a custom font path if needed

        # Render the number of coins as text
        coin_text = font.render(str(self.money), True, (255, 255, 255))  # White color text

        # Position of the coin sprite and text
        coin_x = 10  # Left margin
        coin_y = 10  # Top margin
        text_x = coin_x + self.coin_sprite.get_width() + 10  # Slight margin between coin and text
        text_y = coin_y + (
                    self.coin_sprite.get_height() - coin_text.get_height()) // 2  # Center-align text vertically with the coin

        # Draw the coin sprite and the text on the screen
        self.game.screen.blit(self.coin_sprite, (coin_x, coin_y))
        self.game.screen.blit(coin_text, (text_x, text_y))


    def take_damage(self, damage):
        # Calculate the damage taken
        damage_taken = damage - self.defense
        if damage_taken < 0:
            damage_taken = 0
        elif damage_taken > self.hp:
            damage_taken = self.hp

        # Update the health
        self.hp -= damage_taken

        if self.hp == 0:
            #death effects
            self.status.append(["death", glob.ACTION_FRAMES, damage_taken])
            return DEATH

        #damage taken effects
        self.status.append(["hurt", glob.ACTION_FRAMES, damage_taken])
        return 0


    def attack(self):
        self.status.append(["attack", glob.ACTION_FRAMES])

    def walk(self):
        self.status.append(["walk", SCREEN_WIDTH // 5])
