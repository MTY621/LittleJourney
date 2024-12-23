import glob
from time import sleep

import pygame
import random

from glob import CHARACTER_WIDTH, CHARACTER_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, DEATH

# Initialize Pygame
pygame.init()
pygame.mixer.init()

class Player:
    def __init__(self, sprite_name, hp, name, inventory):

        path = "characters/character_images/main_character/" + sprite_name + "/"
        self.sprite = pygame.image.load(path + "default.png").convert_alpha()
        self.sprite = self.scale(self.sprite)
        self.attack_sprite = pygame.image.load(path + "attack.png").convert_alpha()
        self.attack_sprite = self.scale(self.attack_sprite)
        self.damaged_sprite = pygame.image.load(path + "damaged.png").convert_alpha()
        self.damaged_sprite = self.scale(self.damaged_sprite)
        self.death_sprite = pygame.image.load(path + "death.png").convert_alpha()
        self.death_sprite = self.scale(self.death_sprite)

        path = "sound_effects/main_character/"
        self.sound = path + "step_dirt_1.wav"
        self.attack_sound = path + "whoosh.wav"
        self.damaged_sound = path + "pain.wav"
        self.death_sound = path + "death.wav"

        self.atk = 1
        self.defense = 0
        self.hp = hp
        self.total_hp = hp
        self.money = 0
        self.name = name
        self.inventory = inventory


    def scale(self, image):
        # Extract a specific frame (e.g., top-left frame)
        frame = image.subsurface(pygame.Rect(0, 0, CHARACTER_WIDTH, CHARACTER_HEIGHT))

        # Scale the frame to make it larger (e.g., 8x size)
        scale_factor = 10
        scaled_width = CHARACTER_WIDTH * scale_factor
        scaled_height = CHARACTER_HEIGHT * scale_factor
        image = pygame.transform.scale(frame, (scaled_width, scaled_height))
        return image


    def action_effects(self, screen, display, background, sprite, sound):
        if sprite:
            if sound == self.death_sound:
                screen.blit(background, (0, 0))
                display.update()
                # draw health bar
                screen.blit(sprite, (SCREEN_WIDTH * 3 // 20, SCREEN_HEIGHT * 4 // 5 - CHARACTER_HEIGHT + 70))
            else:
                #draw health bar
                screen.blit(sprite, (SCREEN_WIDTH * 3 // 20, SCREEN_HEIGHT * 4 // 5 - CHARACTER_HEIGHT))
        if sound and glob.sound_effects_are_on == True:
            pygame.mixer.music.load(sound)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(50)


    def draw(self, screen, display, background, sprite, sound):
        # draw inventory
        # healthbar
        self.action_effects(screen, display, background, sprite, sound)
        display.update()
        sleep(0.5)
        #play music if on
        pygame.mixer.music.stop()

        if sound != self.death_sound:
            screen.blit(self.sprite, (SCREEN_WIDTH * 3 // 20, SCREEN_HEIGHT * 4 // 5 - CHARACTER_HEIGHT))
            display.update()


    def take_damage(self, screen, damage, display, background):
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
            self.draw(screen, display, background, self.death_sprite, self.death_sound)
            return DEATH

        #damage taken effects
        self.draw(screen, display, background, self.damaged_sprite, self.damaged_sound)
        return 0


    def attack(self, screen, display, background):
        self.draw(screen, display, background, self.attack_sprite, self.attack_sound)
