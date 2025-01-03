import glob
from time import sleep
from collections import deque
import pygame
import random

from characters.health import HealthBar
from glob import CHARACTER_WIDTH, CHARACTER_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, DEATH

# Initialize Pygame
pygame.init()
pygame.mixer.init()

class Player:
    def __init__(self, sprite_name, hp, name, inventory, game):

        path = "characters/character_images/main_character/" + sprite_name + "/"
        self.sprite = pygame.image.load(path + "default.png").convert_alpha()
        self.sprite = self.scale(self.sprite)
        self.attack_sprite = pygame.image.load(path + "attack.png").convert_alpha()
        self.attack_sprite = self.scale(self.attack_sprite)
        self.hurt_sprite = pygame.image.load(path + "hurt.png").convert_alpha()
        self.hurt_sprite = self.scale(self.hurt_sprite)
        self.death_sprite = pygame.image.load(path + "death.png").convert_alpha()
        self.death_sprite = self.scale(self.death_sprite)
        self.walking_sprite = pygame.image.load(path + "walking.png").convert_alpha()
        self.walking_sprite = self.scale(self.walking_sprite)
        self.current_sprite = self.sprite
        self.status = deque()
        self.last_song = None
        self.no_sound_effect = False

        path = "sound_effects/main_character/"
        self.sound = path + "step_dirt_1.wav"
        self.attack_sound = path + "whoosh.wav"
        self.hurt_sound = path + "pain.wav"
        self.death_sound = path + "death.wav"

        self.atk = 1
        self.defense = 0
        self.hp = hp
        self.total_hp = hp
        self.money = 0
        self.name = name
        self.inventory = inventory
        self.game = game
        self.health_bar = HealthBar(100, 170, 20)


    def scale(self, image):
        # Extract a specific frame (e.g., top-left frame)
        frame = image.subsurface(pygame.Rect(0, 0, CHARACTER_WIDTH, CHARACTER_HEIGHT))

        # Scale the frame to make it larger (e.g., 8x size)
        scale_factor = 10
        scaled_width = CHARACTER_WIDTH * scale_factor
        scaled_height = CHARACTER_HEIGHT * scale_factor
        image = pygame.transform.scale(frame, (scaled_width, scaled_height))
        return image


    def action_effects(self, sprite, sound):
        if sprite:
            if sound == self.death_sound:
                self.game.screen.blit(self.game.background, (0, 0))
                self.game.display.update()
                # draw health bar
                self.game.screen.blit(sprite, (SCREEN_WIDTH * 3 // 20, SCREEN_HEIGHT * 4 // 5 - CHARACTER_HEIGHT + 70))
            else:
                #draw health bar
                self.game.screen.blit(sprite, (SCREEN_WIDTH * 3 // 20, SCREEN_HEIGHT * 4 // 5 - CHARACTER_HEIGHT))
        if sound and glob.sound_effects_are_on == True:
            pygame.mixer.music.load(sound)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(50)


    def draw(self):
        #self.action_effects(sprite, sound)
        #self.game.display.update()
        #sleep(0.5)
        #play music if on
        if len(self.status) > 0:
            # draw health bar
            self.health_bar.draw(self.game.screen, self.status[0][2], SCREEN_WIDTH * 3 // 20,
                                 SCREEN_HEIGHT * 4 // 5 - CHARACTER_HEIGHT - 40)
            curr_song = self.status[0][1]
            if self.no_sound_effect and glob.sound_effects_are_on:
                pygame.mixer.music.load(curr_song)
                pygame.mixer.music.play(fade_ms=glob.ACTION_FRAMES)
                self.last_song = curr_song
                self.no_sound_effect = False

            curr_sprite = self.status[0][0]
            self.game.screen.blit(curr_sprite, (SCREEN_WIDTH * 3 // 20, SCREEN_HEIGHT * 4 // 5 - CHARACTER_HEIGHT))
            self.game.display.update()
            self.status[0][3] -= 1
            if self.status[0][3] == 0:
                self.status.popleft()
                self.no_sound_effect = True
        else:
            # draw health bar
            self.health_bar.draw(self.game.screen, self.hp, SCREEN_WIDTH * 3 // 20,
                                 SCREEN_HEIGHT * 4 // 5 - CHARACTER_HEIGHT - 40)
            self.game.screen.blit(self.sprite, (SCREEN_WIDTH * 3 // 20, SCREEN_HEIGHT * 4 // 5 - CHARACTER_HEIGHT))
            self.game.display.update()
            if glob.music_is_on and self.last_song != self.game.song:
                pygame.mixer.music.load(self.game.song)
                pygame.mixer.music.play(-1)
                self.last_song = self.game.song

        #if glob.music_is_on:
            #pygame.mixer.music.load(self.game.song)
            #.mixer.music.play(-1)

        #if sound != self.death_sound:
            #self.game.screen.blit(self.current_sprite, (SCREEN_WIDTH * 3 // 20, SCREEN_HEIGHT * 4 // 5 - CHARACTER_HEIGHT))
            #self.game.display.update()


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
            #self.draw(self.death_sprite, self.death_sound)
            self.status.append([self.death_sprite, self.death_sound, 0, glob.ACTION_FRAMES])
            return DEATH

        #damage taken effects
        #self.draw(self.hurt_sprite, self.hurt_sound)
        self.status.append([self.hurt_sprite, self.hurt_sound, self.hp, glob.ACTION_FRAMES])
        return 0


    def attack(self):
        #self.draw(self.attack_sprite, self.attack_sound)
        self.status.append([self.attack_sprite, self.attack_sound, self.hp, glob.ACTION_FRAMES])

    def walk(self):
        self.status.append([self.walking_sprite, self.game.song, self.hp, SCREEN_WIDTH // 5])
        if glob.music_is_on:
            pygame.mixer.music.load(self.game.song)
            pygame.mixer.music.play(-1, start=glob.ACTION_FRAMES / 1000)
            self.last_song = self.game.song

    def default(self):
        self.current_sprite = self.sprite
