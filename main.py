import glob
from menus.main_menu import main_menu_start
from menus.story_menus.gameplay_menus import init_menus
from characters.npcs.chill_npcs import init_chill_npcs
from characters.npcs.fighting_npcs import init_fighting_npcs
from game.game import Game

def reset_game():
    chill_npcs_aux = init_chill_npcs()
    fighting_npcs_aux = init_fighting_npcs()
    all_menus = init_menus(chill_npcs_aux, fighting_npcs_aux)
    curr_game = Game(glob.player_race, glob.player_name, all_menus[len(all_menus) - 1], glob.CURRENT_GAME_SONG)

    for npc in chill_npcs_aux:
        npc.game = curr_game
    for npc in fighting_npcs_aux:
        npc.game = curr_game
    for curr_menu in all_menus:
        curr_menu.game = curr_game

    return curr_game

if __name__ == '__main__':
    glob.music_is_on = True
    main_menu_start()

    game = reset_game()
    while True:
        ret = game.start()
        ret2 = main_menu_start()
        if ret == glob.GAME_ENDED or ret2 == glob.GAME_ENDED:
            game = reset_game()
