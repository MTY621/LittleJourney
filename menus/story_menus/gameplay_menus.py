from menus.story_menus.story_menu import StoryMenu
from characters.npcs.chill_npcs import chill_npcs
from characters.npcs.fighting_npcs import fighting_npcs

menus = []

menu_9 = StoryMenu(fighting_npcs[9], [None])
menu_9.add_text_display(["Probable trader" + ": " + "A new client?", "You look poor.", "Come back when you have some money."])
menu_9.add_button("But I have some money!", menu_9.set_menu, 0)
menu_9.add_button("So you are a trader?", menu_9.set_menu, 0)
menu_9.add_button("How can i earn some money?", menu_9.set_menu, 0)
menus.append(menu_9)

menu_8 = StoryMenu(chill_npcs[1], [menu_9])
menu_8.add_text_display(["Unknown girl" + ": " + "Fuck off!"])
menu_8.add_button("Ok", menu_8.set_menu, 0)
menus.append(menu_8)

menu_7 = StoryMenu(chill_npcs[1], [menu_8, menu_9])
menu_7.add_text_display(["Unknown girl" + ": " + "Deepshit!"])
menu_7.add_button("That's unexpected!", menu_7.set_menu, 0)
menu_7.add_button("Fair enough. [Continue]", menu_7.set_menu, 1)
menus.append(menu_7)

menu_6 = StoryMenu(chill_npcs[1], [menu_9])
menu_6.add_text_display(["Unknown girl" + ": " + "Beautiful singing!", "Have a turnip!"])
menu_6.add_button("Thanks! <Get a turnip>", menu_6.get_items, 0, [])######## turnip
menus.append(menu_6)

menu_5 = StoryMenu(chill_npcs[1], [menu_6, menu_9])
menu_5.add_text_display(["Unknown girl" + ": " + "La-la-la-la-la!"])
menu_5.add_button("La-la-la-la-la!", menu_5.set_menu, 0)
menu_5.add_button("[Continue]", menu_5.set_menu, 1)
menus.append(menu_5)

menu_4 = StoryMenu(chill_npcs[1], [menu_5, menu_9])
menu_4.add_text_display(["Unknown girl" + ": " + "La-la-la-la!"])
menu_4.add_button("La-la-la-la!", menu_4.set_menu, 0)
menu_4.add_button("[Continue]", menu_4.set_menu, 1)
menus.append(menu_4)

menu_3 = StoryMenu(chill_npcs[1], [menu_4, menu_7, menu_9])
menu_3.add_text_display(["Unknown girl" + ": " + "La-la-la!"])
menu_3.add_button("La-la-la!", menu_3.set_menu, 0)
menu_3.add_button("...", menu_3.set_menu, 2)
menu_3.add_button("Shut up!", menu_3.set_menu, 1)
menus.append(menu_3)

menu_2 = StoryMenu(chill_npcs[0], [menu_3, menu_9])
menu_2.add_text_display([menu_2.npc.name + ": " + "Thank you!", "If you want to buy new gear you can talk ",
                         "to the trader when you are in the village."])
menu_2.add_button("Thanks. [Continue]", menu_2.set_menu, 0)
menu_2.add_button("Thanks. [Visit the trader]", menu_2.set_menu, 1)
menus.append(menu_2)

menu_1 = StoryMenu(chill_npcs[0], [menu_2, menu_3])
menu_1.add_text_display([menu_1.npc.name + ": " + "Welcome, whoever you are!", "Do you have any spare change?"])
menu_1.add_button("Yes. [Give 1 coin]", menu_1.give_coins, 0, 1)
menu_1.add_button("No. [Leave]", menu_1.set_menu, 1)
menus.append(menu_1)

# error_menu = StoryMenu(chill_npcs[0], [None])
# error_menu.add_text_display(["label"])
# error_menu.add_button("OK", error_menu.set_menu, 0)

# menu_2 = StoryMenu(fighting_npcs[0], [None])
# menu_2.add_button("Attack NPC", 0, menu_2.fight)
# menus.append(menu_2)
#
# menu_1 = StoryMenu(chill_npcs[0], [None, menu_2])
# menu_1.add_text_display(["Welcome to the story menu"])
# menu_1.add_button("Attack NPC", 1, menu_1.fight)
# menus.append(menu_1)
