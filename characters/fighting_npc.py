from time import sleep
from collections import deque
import pygame
import random
import glob
from characters.health import HealthBar
from glob import CHARACTER_WIDTH, CHARACTER_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, DEATH, ACTION_FRAMES

class FightingNpc:
    def __init__(self, sprite_name, min_atk, max_atk, min_hp, max_hp, min_def, max_def, min_money, max_money, name,
                 items, drop_chance):

        self.sprite_name = sprite_name
        path = "characters/character_images/" + sprite_name + "/"
        self.sprite = pygame.image.load(path + "default.png").convert_alpha()
        self.sprite = self.scale(self.sprite)
        self.attack_sprite = pygame.image.load(path + "attack.png").convert_alpha()
        self.attack_sprite = self.scale(self.attack_sprite)
        self.hurt_sprite = pygame.image.load(path + "hurt.png").convert_alpha()
        self.hurt_sprite = self.scale(self.hurt_sprite)
        self.death_sprite = pygame.image.load(path + "death.png").convert_alpha()
        self.death_sprite = self.scale(self.death_sprite)
        self.current_sprite = self.sprite
        self.current_effect = None
        self.status = deque()
        self.last_song = None
        self.no_sound_effect = True
        self.count = 0

        self.min_atk = min_atk
        self.max_atk = max_atk
        self.atk = random.randint(min_atk, max_atk)

        self.min_hp = min_hp
        self.max_hp = max_hp
        self.hp = random.randint(min_hp, max_hp)
        self.health_bar_hp = self.hp
        self.total_hp = self.hp
        self.health_bar = HealthBar(self.hp, 170, 20)

        self.min_def = min_def
        self.max_def = max_def
        self.defense = random.randint(min_def, max_def)

        self.min_money = min_money
        self.max_money = max_money
        self.money = random.randint(min_money, max_money)

        self.name = name
        self.items = items
        self.drop_chance = drop_chance
        self.type = 'fighting'
        self.game = None


    def __copy__(self):
        return FightingNpc(self.sprite_name, self.min_atk, self.max_atk, self.min_hp, self.max_hp, self.min_def,
                           self.max_def, self.min_money, self.max_money, self.name, self.items, self.drop_chance)

    def scale(self, image):
        image = pygame.transform.scale(image, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
        return image

    def draw(self):
        # Draw the health bar
        self.health_bar.draw(self.game.screen, self.health_bar_hp, SCREEN_WIDTH - SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.88 - CHARACTER_HEIGHT - 40)

        if len(self.status) > 0:
            curr_status = self.status[0][0]
            if curr_status == "walk":
                if self.current_sprite != self.walking_sprite:
                    if self.count >= glob.ACTION_FRAMES / 3:
                        self.current_sprite = self.walking_sprite
                        self.count = 0
                else:
                    if self.count >= glob.ACTION_FRAMES / 3:
                        self.current_sprite = self.sprite
                        self.count = 0
                self.count += 1
            elif curr_status == "attack":
                if self.current_sprite != self.attack_sprite:
                    if self.count == 0:
                        self.current_sprite = self.attack_sprite
                else:
                    if self.count == glob.ACTION_FRAMES / 2:
                        self.current_sprite = self.sprite
                self.count += 1
            elif curr_status == "hurt":
                if self.current_sprite != self.hurt_sprite:
                    if self.count == 0:
                        self.current_sprite = self.hurt_sprite
                        self.health_bar_hp -= self.status[0][2]
                else:
                    if self.count == glob.ACTION_FRAMES / 2:
                        self.current_sprite = self.sprite
                self.count += 1
            elif curr_status == "death":
                self.current_sprite = self.death_sprite
                if self.count == 0:
                    self.health_bar_hp -= self.status[0][2]
                self.count += 1
            self.status[0][1] -= 1
            if self.status[0][1] == 0:
                self.status.popleft()
                self.count = 0
        else:
            self.current_sprite = self.sprite
        self.game.screen.blit(self.current_sprite, (SCREEN_WIDTH - SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.88 - CHARACTER_HEIGHT))


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
            # death effects
            self.status.append(['death', glob.ACTION_FRAMES, damage_taken])
            return DEATH

        # damage taken effects
        self.status.append(['hurt', glob.ACTION_FRAMES, damage_taken])
        return 0

    def attack(self):
        self.status.append(['attack', glob.ACTION_FRAMES])

    def reset(self):
        self.deque = deque()
        self.hp = random.randint(self.min_hp, self.max_hp)
        self.health_bar_hp = self.hp
        self.total_hp = self.hp
        self.health_bar = HealthBar(self.hp, 170, 20)

        self.min_def = self.min_def
        self.max_def = self.max_def
        self.defense = random.randint(self.min_def, self.max_def)

        self.min_money = self.min_money
        self.max_money = self.max_money
        self.money = random.randint(self.min_money, self.max_money)
