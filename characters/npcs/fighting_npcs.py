from characters.fighting_npc import FightingNpc


def init_fighting_npcs():
    fighting_npcs = []

# forest enemies
# 0
    fighting_npcs.append(FightingNpc("big_bloated", 7, 11, 10, 10, 0,
                         2, 3, 10, "Bloated mutant", [], 0))
# 1
    fighting_npcs.append(FightingNpc("centipede", 8, 13, 12, 16, 1,
                         2, 5, 12, "Centipede", [], 0))
# 2
    fighting_npcs.append(FightingNpc("battle_turtle", 10, 15, 12, 20, 4,
                         4, 12, 18, "Armored turtle", [], 0))

# desert enemies
# 3
    fighting_npcs.append(FightingNpc("deceased", 15, 25, 20, 30, 3,
                         5, 10, 20, "Old Bob", [], 0))
# 4
    fighting_npcs.append(FightingNpc("hyena", 25, 30, 18, 20, 2,
                         2, 10, 20, "Hyena", [], 0))
# 5
    fighting_npcs.append(FightingNpc("mummy", 20, 30, 25, 35, 6,
                         8, 25, 30, "Mummy", [], 0))

# ice enemies
# 6
    fighting_npcs.append(FightingNpc("vulture", 25, 30, 30, 35, 4,
                         9, 30, 30, "Hungry Vulture", [], 0))
# 7
    fighting_npcs.append(FightingNpc("samurai", 32, 40, 35, 45, 6,
                        9, 35, 35, "Samurai Shan", [], 0))
# 8
    fighting_npcs.append(FightingNpc("snake", 35, 45, 30, 35, 9,
                         12, 40, 45, "Snake", [], 0))

# extras
# 9
    fighting_npcs.append(FightingNpc("trader", 100, 100, 100, 100, 10,
                         10, 100, 100, "The Trader", [], 0))
    return fighting_npcs