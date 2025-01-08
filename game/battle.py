import pygame
import pygame_menu
from time import sleep

import glob
from characters.chill_npc import ChillNpc
from characters.fighting_npc import FightingNpc


def player_attack(player, npc):
    player.attack()
    ret_code = npc.take_damage(player.atk)
    return ret_code


def npc_attack(player, npc):
    if isinstance(npc, FightingNpc):
        npc.attack()
        ret_code = player.take_damage(npc.atk)
        return ret_code
    return 0


def fight(player, npc):
    player.atk += player.bonus_atk
    player.defense += player.bonus_defense
    count = 0
    while True:
        count += 1
        if player_attack(player, npc) == glob.DEATH:
            player.reset_bonuses()
            return count

        sleep(0.1)

        count += 1
        if npc_attack(player, npc) == glob.DEATH:
            player.reset_bonuses()
            return count
