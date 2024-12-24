from time import sleep

import pygame
import random

from glob import CHARACTER_WIDTH, CHARACTER_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, DEATH


# Initialize Pygame
pygame.init()

class ChillNpc:
    def __init__(self, sprite_name, min_hp, max_hp, min_def, max_def, min_money, max_money, name, items, drop_chance):

        self.sprite_name = sprite_name
        path = "characters/character_images/" + sprite_name + "/"
        self.sprite = pygame.image.load(path + "default.png").convert_alpha()
        self.sprite = self.scale(self.sprite)
        self.attack_sprite = pygame.image.load(path + "attack.png").convert_alpha()
        self.attack_sprite = self.scale(self.attack_sprite)
        self.damaged_sprite = pygame.image.load(path + "damaged.png").convert_alpha()
        self.damaged_sprite = self.scale(self.damaged_sprite)
        self.death_sprite = pygame.image.load(path + "death.png").convert_alpha()
        self.death_sprite = self.scale(self.death_sprite)

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
        self.type = 'chill'
        self.game = None


    def __copy__(self):
        return ChillNpc(self.sprite_name, self.min_hp, self.max_hp, self.min_def, self.max_def, self.min_money,
                        self.max_money, self.name, self.items, self.drop_chance)


    def scale(self, image):
        # Extract a specific frame (e.g., top-left frame)
        frame = image.subsurface(pygame.Rect(0, 0, CHARACTER_WIDTH, CHARACTER_HEIGHT))

        # Scale the frame to make it larger (e.g., 8x size)
        scale_factor = 10
        scaled_width = CHARACTER_WIDTH * scale_factor
        scaled_height = CHARACTER_HEIGHT * scale_factor
        image = pygame.transform.scale(frame, (scaled_width, scaled_height))
        return image


    def action_effects(self, sprite):
        if sprite:
            if sprite == self.death_sprite:
                self.game.screen.blit(self.game.background, (0, 0))
                self.game.display.update()
                # draw health bar
                self.game.screen.blit(sprite, (SCREEN_WIDTH - SCREEN_WIDTH * 3 // 20, SCREEN_HEIGHT * 4 // 5 - CHARACTER_HEIGHT + 70))
            else:
                # draw health bar
                self.game.screen.blit(sprite, (SCREEN_WIDTH - SCREEN_WIDTH * 3 // 20, SCREEN_HEIGHT * 4 // 5 - CHARACTER_HEIGHT))


    def draw(self, sprite):
        # healthbar
        self.action_effects(sprite)
        self.game.display.update()
        sleep(0.5)

        if sprite != self.death_sprite:
            self.game.screen.blit(self.sprite, (SCREEN_WIDTH - SCREEN_WIDTH * 3 // 20, SCREEN_HEIGHT * 4 // 5 - CHARACTER_HEIGHT))
            self.game.display.update()
            sleep(0.5)


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
            self.draw(self.death_sprite)
            return DEATH

        # damage taken effects
        self.draw(self.damaged_sprite)
        return 0