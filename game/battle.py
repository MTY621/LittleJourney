import pygame
import pygame_menu

import glob
from characters.chill_npc import ChillNpc
from characters.fighting_npc import FightingNpc


def player_attack(player, npc):
    player.attack()
    ret_code = npc.take_damage(player.atk)
    return ret_code


def npc_attack(player, npc):
    if npc is FightingNpc:
        npc.attack()
        ret_code = player.take_damage(npc.atk)
        return ret_code
    return 0


def fight(player, npc):
    while True:
        if player_attack(player, npc) == glob.DEATH:
            return 0
        if npc_attack(player, npc) == glob.DEATH:
            return glob.DEATH
