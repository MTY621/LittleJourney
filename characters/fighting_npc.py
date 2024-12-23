from time import sleep

import pygame
import random

from globals import SCREEN_WIDTH, SCREEN_HEIGHT, DEATH

# Initialize Pygame
pygame.init()

class FightingNpc:
    def __init__(self, sprite, attack_sprite, damaged_sprite, death_sprite, sound, attack_sound, damaged_sound,
                 death_sound, min_atk, max_atk, min_hp, max_hp, min_def, max_def, min_money, max_money, name, items,
                 drop_chance):

        self.sprite = sprite
        self.attack_sprite = attack_sprite
        self.damaged_sprite = damaged_sprite
        self.death_sprite = death_sprite

        self.sound = sound
        self.attack_sound = attack_sound
        self.damaged_sound = damaged_sound
        self.death_sound = death_sound

        self.min_atk = min_atk
        self.max_atk = max_atk
        self.atk = random.randint(min_atk, max_atk)

        self.min_hp = min_hp
        self.max_hp = max_hp
        self.hp = random.randint(min_hp, max_hp)
        self.total_hp = self.hp

        self.min_def = min_def
        self.max_def = max_def
        self.defense = random.randint(min_def, max_def)

        self.min_money = min_money
        self.max_money = max_money
        self.money = random.randint(min_money, max_money)

        self.name = name
        self.items = items
        self.drop_chance = drop_chance


    def __copy__(self):
        return FightingNpc(self.sprite, self.attack_sprite, self.damaged_sprite, self.death_sprite, self.sound,
                           self.attack_sound, self.damaged_sound, self.death_sound, self.min_atk, self.max_atk,
                           self.min_hp, self.max_hp, self.min_def, self.max_def, self.min_money, self.max_money,
                           self.name, self.items, self.drop_chance)


    def action_effects(self, sprite, sound):
        if sprite:
            pass
        if sound:
            pass


    def take_damage(self, damage):
        # Calculate the damage taken
        damage_taken = damage - self.defense
        if damage_taken < 0:
            damage_taken = 0
        elif damage_taken > self.hp:
            damage_taken = self.hp

        # Update the health
        self.hp -= damage_taken
        #draw health bar

        if self.hp == 0:
            #death effects
            self.action_effects(self.death_sprite, self.death_sound)

            #add player money
            got_loot = random.randint(1, 100)
            if got_loot <= self.drop_chance:
                item = random.choice(self.items)
                #add item to player inventory
            return DEATH

        #damage taken effects
        self.action_effects(self.damaged_sprite, self.damaged_sound)
        sleep(0.1)
        # draw sprite
        return 0


    def attack(self):
        self.action_effects(self.attack_sprite, self.attack_sound)
        sleep(0.1)
        #draw sprite
        return self.atk
