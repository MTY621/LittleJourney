from menus.story_menus.story_menu import StoryMenu
from characters.npcs.chill_npcs import chill_npcs
from characters.npcs.fighting_npcs import fighting_npcs

menus = []

menu_3 = StoryMenu(fighting_npcs[0], [None])
menu_3.add_button("Attack NPC", 0, menu_3.fight)
menus.append(menu_3)

menu_2 = StoryMenu(fighting_npcs[0], [None, menu_3])
menu_2.add_text_display(["Thank you"], 0)
menu_2.add_button("Leave", 1, menu_2.do_nothing)
menus.append(menu_2)

menu_1 = StoryMenu(chill_npcs[0], [None, menu_2, menu_3])
menu_1.add_text_display(["Welcome whoever you are", "Do you have any spare change"], 0)
menu_1.add_button("Yes [Give 1 coin]", 1, menu_1.give_coins, 1)
menu_1.add_button("No [Leave]", 2, menu_1.do_nothing)
menus.append(menu_1)

# menu_2 = StoryMenu(fighting_npcs[0], [None])
# menu_2.add_button("Attack NPC", 0, menu_2.fight)
# menus.append(menu_2)
#
# menu_1 = StoryMenu(chill_npcs[0], [None, menu_2])
# menu_1.add_text_display(["Welcome to the story menu"], 0)
# menu_1.add_button("Attack NPC", 1, menu_1.fight)
# menus.append(menu_1)
