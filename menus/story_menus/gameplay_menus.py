import random

from menus.story_menus.story_menu import StoryMenu
from characters.npcs.chill_npcs import chill_npcs
from characters.npcs.fighting_npcs import fighting_npcs
import glob

menus = []

menu_death = StoryMenu(fighting_npcs[9], [None])

menu_20 = StoryMenu(fighting_npcs[random.randint(0, 2)], [None])
menu_20.add_text_display(["Blarghhh."])
menu_20.add_button("Fight.", menu_20.fight, 0)
menus.append(menu_20)

menu_11 = StoryMenu(fighting_npcs[9], None)
menu_19 = StoryMenu(fighting_npcs[9], [None])
menu_19.add_text_display([menu_19.npc.name + ": " + "I am THE TRADER."])
menu_19.add_button("Ok... how can I earn some money?", menu_19.set_menu, 0)
menus.append(menu_19)


menu_18 = StoryMenu(fighting_npcs[9], [menu_20])
menu_18.add_text_display([menu_18.npc.name + ": " + "You insult me."])
menu_18.add_button("Whatever. [Go to the forest]", menu_18.set_transition, 0,
                   "background/temple/1_temple.png", glob.TEMPLE_COLOUR, glob.TEMPLE_MUSIC, glob.TEMPLE_WALK)
menus.append(menu_18)

menu_17 = StoryMenu(fighting_npcs[9], [menu_18, menu_20])
menu_17.add_text_display([menu_17.npc.name + ": " + "Never."])
menu_17.add_button("Stop lying.", menu_17.set_menu, 0)
menu_17.add_button("Whatever. [Go to the forest]", menu_17.set_transition, 1,
                   "background/temple/1_temple.png", glob.TEMPLE_COLOUR, glob.TEMPLE_MUSIC, glob.TEMPLE_WALK)
menus.append(menu_17)

menu_16 = StoryMenu(fighting_npcs[9], [menu_17, menu_20])
menu_16.add_text_display([menu_16.npc.name + ": " + "No."])
menu_16.add_button("Yes, you did.", menu_16.set_menu, 0)
menu_16.add_button("Whatever. [Go to the forest]", menu_16.set_transition, 1,
                   "background/temple/1_temple.png", glob.TEMPLE_COLOUR, glob.TEMPLE_MUSIC, glob.TEMPLE_WALK)
menus.append(menu_16)

menu_15 = StoryMenu(fighting_npcs[9], [menu_16, menu_20])
menu_15.add_text_display([menu_15.npc.name + ": " + "Hehehe... umm...", "You just need to believe in yourself."])
menu_15.add_button("So you just scammed me.", menu_15.set_menu, 0)
menu_15.add_button("I guess. [Go to the forest]", menu_15.set_transition, 1,
                   "background/temple/1_temple.png", glob.TEMPLE_COLOUR, glob.TEMPLE_MUSIC, glob.TEMPLE_WALK)
menus.append(menu_15)

menu_14 = StoryMenu(fighting_npcs[9], [menu_15, menu_20])
menu_14.add_text_display([menu_14.npc.name + ": " + "If you give me your money I can heal you."])
menu_14.add_button("Ok. [Give him your money]", menu_14.give_money, 0, -1)
menu_14.add_button("No. [Go to the forest]", menu_14.set_transition, 1,
                   "background/temple/1_temple.png", glob.TEMPLE_COLOUR, glob.TEMPLE_MUSIC, glob.TEMPLE_WALK)
menus.append(menu_14)

menu_13 = StoryMenu(fighting_npcs[9], [menu_20])
menu_13.add_text_display([menu_13.npc.name + ": " + "What a shame."])
menu_13.add_button("[Go to the forest]", menu_13.set_transition, 0,
                   "background/temple/1_temple.png", glob.TEMPLE_COLOUR, glob.TEMPLE_MUSIC, glob.TEMPLE_WALK)
menus.append(menu_13)

menu_12 = StoryMenu(fighting_npcs[9], [menu_14, menu_13])
menu_12.add_text_display([menu_12.npc.name + ": " + "Do you have any mental issues?"])
menu_12.add_button("Yes.", menu_12.set_menu, 0)
menu_12.add_button("No.", menu_12.set_menu, 1)
menus.append(menu_12)

menu_11.menus = [menu_20, menu_12]
menu_11.add_text_display([menu_11.npc.name + ": " + "Go to the forest and kill some monsters.",
                         "Don't forget to get some sleep too occasionally", "to restore your strength."])
menu_11.add_button("Ok. [Go to the forest]", menu_11.set_transition, 0,
                   "background/temple/1_temple.png", glob.TEMPLE_COLOUR, glob.TEMPLE_MUSIC, glob.TEMPLE_WALK)
menu_11.add_button("Ok, but how can I earn money?", menu_11.set_menu, 1)
menus.append(menu_11)

menu_10 = StoryMenu(fighting_npcs[9], [menu_11])
menu_10.add_text_display([menu_10.npc.name + ": " + "I am THE TRADER.",
                         "I do real business with real money."])
menu_10.add_button("Ok... how can I earn some money?", menu_10.set_menu, 0)
menus.append(menu_10)

menu_9 = StoryMenu(fighting_npcs[9], [menu_10, menu_19, menu_11])
menu_9.add_text_display(["Probable trader" + ": " + "A new client?", "You look poor.",
                         "Come back when you have some money."])
menu_9.add_button("But I have some money!", menu_9.set_menu, 0)
menu_9.add_button("So you are a trader?", menu_9.set_menu, 0)
menu_9.add_button("How can I earn some money?", menu_9.set_menu, 0)
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
menu_6.add_button("Thanks! <Get a turnip>", menu_6.get_items, 0, ["Turnip"])
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
menu_1.add_button("Yes. [Give 1 coin]", menu_1.give_money, 0, 1)
menu_1.add_button("No. [Leave]", menu_1.set_menu, 1)
menus.append(menu_1)

# traderul este scammer
# taranul e sarac si atotstiutor
# marry e bipolara
# betty e fomista si il place pe ahmet
# ahmet e religion freak si in rest usor manipulabil
# aaliya e sperioasa dar cu gura mare

# error_menu = StoryMenu(chill_npcs[0], [None])
# error_menu.add_text_display(["label"])
# error_menu.add_button("OK", error_menu.set_menu, 0)

# menu_1 = StoryMenu(fighting_npcs[1], [None])
# menu_1.add_text_display([menu_1.npc.name + ": " + "Welcome, whoever you are!", "Do you have any spare change?"])
# menu_1.add_button("Fight", menu_1.fight, 0)
# menus.append(menu_1)
