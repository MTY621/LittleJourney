from menus.story_menus.story_menu import StoryMenu
from characters.npcs import fighting_npcs, chill_npcs

menus = []

menu_2 = StoryMenu(fighting_npcs.fighting_npcs[0], [None])
menu_2.add_button("Attack NPC", menu_2.fight, 0)
menus.append(menu_2)

menu_1 = StoryMenu(chill_npcs.chill_npcs[0], [None, menu_2])
menu_1.add_text_display(["Welcome to the story menu"], 0)
menu_1.add_button("Attack NPC", menu_1.fight, 1)
menus.append(menu_1)
