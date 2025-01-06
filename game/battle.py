import pygame
import pygame_menu

import glob
from characters.chill_npc import ChillNpc
from characters.fighting_npc import FightingNpc


def player_attack(player, npc):
    print("Attack command")
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
    print("CG11")
    count = 0
    while True:
        count += 1
        if player_attack(player, npc) == glob.DEATH:
            return count

        count += 1
        if npc_attack(player, npc) == glob.DEATH:
            return count
