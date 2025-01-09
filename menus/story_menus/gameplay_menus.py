import random

from menus.story_menus.story_menu import StoryMenu
from inventory.items import items
import glob

def init_menus(chill_npcs, fighting_npcs):
    menus = []

    # end game
    menu_death_4 = StoryMenu(fighting_npcs[9], [None])
    menu_death_4.add_text_display([menu_death_4.npc.name + ": " + ":()"])
    menu_death_4.add_button("[Continue]", menu_death_4.set_menu, [0])
    menus.append(menu_death_4)

    menu_death_3 = StoryMenu(fighting_npcs[9], [None])
    menu_death_3.add_text_display([menu_death_3.npc.name + ": " + "($_$)"])
    menu_death_3.add_button("[Continue]", menu_death_3.set_menu, [0])
    menus.append(menu_death_3)

    menu_death_2 = StoryMenu(fighting_npcs[9], [None])
    menu_death_2.add_text_display([menu_death_2.npc.name + ": " + ":("])
    menu_death_2.add_button("[Continue]", menu_death_2.set_menu, [0])
    menus.append(menu_death_2)

    menu_death_1 = StoryMenu(fighting_npcs[9], [None])
    menu_death_1.add_text_display([menu_death_1.npc.name + ": " + ":)"])
    menu_death_1.add_button("[Continue]", menu_death_1.set_menu, [0])
    menus.append(menu_death_1)

    menu_death = StoryMenu(fighting_npcs[9], [menu_death_1, menu_death_2, menu_death_3, menu_death_4])
    menu_death.add_text_display([menu_death.npc.name + ": " + "The game ended.", "Can I have your belongings?"])
    menu_death.add_button("Yes.", menu_death.set_menu, [0])
    menu_death.add_button("No.", menu_death.set_menu, [1])
    menu_death.add_button("Only the money.", menu_death.set_menu, [2])
    menu_death.add_button("Only the food.", menu_death.set_menu, [3])
    menus.append(menu_death)

    filthy_death = StoryMenu(chill_npcs[3], [None])
    filthy_death.add_text_display([filthy_death.npc.name + ": " + "The filthy one...", "Allah won't have mercy on you."])
    filthy_death.add_button("[Continue]", filthy_death.set_menu, [0])
    menus.append(filthy_death)

    slap_death_1 = StoryMenu(chill_npcs[2], [None])
    slap_death_1.add_text_display([slap_death_1.npc.name + ": " + "No promises."])
    slap_death_1.add_button("[Gulp]", slap_death_1.set_menu, [0])
    menus.append(slap_death_1)

    slap_death = StoryMenu(chill_npcs[2], [None, slap_death_1])
    slap_death.add_text_display([slap_death.npc.name + ": " + "Killed by a slap.",
                                 "I once got hit by a running horse and it broke its maxillary."])
    slap_death.add_button("Yeah... [This is pathetic.]", slap_death.set_menu, [0])
    slap_death.add_button("Just don't eat my corpse.", slap_death.set_menu, [1])
    menus.append(slap_death)

    happy_death_1 = StoryMenu(chill_npcs[2], [None])
    happy_death_1.add_text_display([happy_death_1.npc.name + ": " + "I can eat some of them.",
                                    "To help you with the stress."])
    happy_death_1.add_button("!!!", happy_death_1.set_menu, [0])
    menus.append(happy_death_1)

    happy_death = StoryMenu(chill_npcs[1], [None, happy_death_1])
    happy_death.add_text_display([happy_death.npc.name + ": " + "Let's have more kids!"])
    happy_death.add_button("Ok.", happy_death.set_menu, [0])
    happy_death.add_button("We already have 7!", happy_death.set_menu, [1])
    menus.append(happy_death)


    def generate_buy_food_args():
        idx = random.randint(0, 7)
        return [(menu_trader_temple.get_items, [0, [items[idx].name]]),
                (menu_trader_temple.give_money, [0, items[idx].price])]

    def generate_buy_potion_args():
        idx = random.randint(8, 10)
        return [(menu_trader_temple.get_items, [0, [items[idx].name]]),
                (menu_trader_temple.give_money, [0, items[idx].price])]

    # trader
    menu_51 = StoryMenu(fighting_npcs[random.randint(6, 7)], [None])
    menu_trader_ice_healed = StoryMenu(fighting_npcs[9], [None])
    menu_trader_ice_healed.menus = [menu_trader_ice_healed, menu_51]
    menu_trader_ice_healed.add_text_display([menu_trader_ice_healed.npc.name + ": " + "Stop sleeping.",
                                         "It will get you killed. Buy a drink instead."])
    menu_trader_ice_healed.add_button("[Buy a sword].", menu_trader_ice_healed.give_sword)
    menu_trader_ice_healed.add_button("[Buy a shield].", menu_trader_ice_healed.give_shield)
    menu_trader_ice_healed.add_button("[Buy a potion].", menu_trader_ice_healed.buy_item, [],
                                         lambda: [generate_buy_potion_args])
    menu_trader_ice_healed.add_button("[Buy food or drinks].", menu_trader_ice_healed.buy_item, [],
                                         lambda: [generate_buy_food_args])
    menu_trader_ice_healed.add_button("[Continue]", menu_trader_ice_healed.set_transition, [2,
                       "background/ice/5_snowy_trees_hd.png", glob.ICE_COLOUR, glob.ICE_MUSIC, glob.ICE_WALK])
    menus.append(menu_trader_ice_healed)

    menu_trader_ice = StoryMenu(fighting_npcs[9], [None])
    menu_trader_ice.menus = [menu_trader_ice, menu_trader_ice_healed, menu_51]
    menu_trader_ice.add_text_display([menu_trader_ice.npc.name + ": " + "You didn't die yet?",
                                         "It's really dangerous out there. Buy an expensive sword."])
    menu_trader_ice.add_button("[Buy a sword].", menu_trader_ice.give_sword)
    menu_trader_ice.add_button("[Buy a shield].", menu_trader_ice.give_shield)
    menu_trader_ice.add_button("[Buy a potion].", menu_trader_ice.buy_item, [],
                                  lambda: [generate_buy_potion_args])
    menu_trader_ice.add_button("[Buy food or drinks].", menu_trader_ice.buy_item, [],
                                  lambda: [generate_buy_food_args])
    menu_trader_ice.add_button("Sleep. [Heal]", menu_trader_ice.heal, [1, 100])
    menu_trader_ice.add_button("[Continue]", menu_trader_ice.set_transition, [2,
                       "background/ice/5_snowy_trees_hd.png", glob.ICE_COLOUR, glob.ICE_MUSIC, glob.ICE_WALK])
    menus.append(menu_trader_ice)



    menu_31 = StoryMenu(fighting_npcs[random.randint(3, 4)], [None])
    menu_trader_desert_healed = StoryMenu(fighting_npcs[9], [None])
    menu_trader_desert_healed.menus = [menu_trader_desert_healed, menu_31]
    menu_trader_desert_healed.add_text_display([menu_trader_desert_healed.npc.name + ": " + "Stop sleeping.",
                                         "It will get you killed. Buy a drink instead."])
    menu_trader_desert_healed.add_button("[Buy a sword].", menu_trader_desert_healed.give_sword)
    menu_trader_desert_healed.add_button("[Buy a shield].", menu_trader_desert_healed.give_shield)
    menu_trader_desert_healed.add_button("[Buy a potion].", menu_trader_desert_healed.buy_item, [],
                                         lambda: [generate_buy_potion_args])
    menu_trader_desert_healed.add_button("[Buy food or drinks].", menu_trader_desert_healed.buy_item, [],
                                         lambda: [generate_buy_food_args])
    menu_trader_desert_healed.add_button("[Continue]", menu_trader_desert_healed.set_transition, [1,
                       "background/desert/3_oasis.png", glob.DESERT_COLOUR, glob.DESERT_MUSIC, glob.DESERT_WALK])
    menus.append(menu_trader_desert_healed)

    menu_trader_desert = StoryMenu(fighting_npcs[9], [None])
    menu_trader_desert.menus = [menu_trader_desert, menu_trader_desert_healed, menu_31]
    menu_trader_desert.add_text_display([menu_trader_desert.npc.name + ": " + "You didn't die yet?",
                                         "It's really dangerous out there. Buy an expensive sword."])
    menu_trader_desert.add_button("[Buy a sword].", menu_trader_desert.give_sword)
    menu_trader_desert.add_button("[Buy a shield].", menu_trader_desert.give_shield)
    menu_trader_desert.add_button("[Buy a potion].", menu_trader_desert.buy_item, [],
                                  lambda: [generate_buy_potion_args])
    menu_trader_desert.add_button("[Buy food or drinks].", menu_trader_desert.buy_item, [],
                                  lambda: [generate_buy_food_args])
    menu_trader_desert.add_button("Sleep. [Heal]", menu_trader_desert.heal, [1, 100])
    menu_trader_desert.add_button("[Continue]", menu_trader_desert.set_transition, [2,
                       "background/desert/3_oasis.png", glob.DESERT_COLOUR, glob.DESERT_MUSIC, glob.DESERT_WALK])
    menus.append(menu_trader_desert)



    menu_20 = StoryMenu(fighting_npcs[random.randint(0, 1)], [None])
    menu_trader_temple_healed = StoryMenu(fighting_npcs[9], [None])
    menu_trader_temple_healed.menus = [menu_trader_temple_healed, menu_20]
    menu_trader_temple_healed.add_text_display([menu_trader_temple_healed.npc.name + ": " + "Sleepy adventurer.",
                                         "You could have bought something", "to restore your health."])
    menu_trader_temple_healed.add_button("[Buy a sword].", menu_trader_temple_healed.give_sword)
    menu_trader_temple_healed.add_button("[Buy a shield].", menu_trader_temple_healed.give_shield)
    menu_trader_temple_healed.add_button("[Buy a potion].", menu_trader_temple_healed.buy_item, [],
                                         lambda: [generate_buy_potion_args])
    menu_trader_temple_healed.add_button("[Buy food or drinks].", menu_trader_temple_healed.buy_item, [],
                                         lambda: [generate_buy_food_args])
    menu_trader_temple_healed.add_button("[Continue]", menu_trader_temple_healed.set_transition, [1,
                       "background/temple/1_temple.png", glob.TEMPLE_COLOUR, glob.TEMPLE_MUSIC, glob.TEMPLE_WALK])
    menus.append(menu_trader_temple_healed)

    menu_trader_temple = StoryMenu(fighting_npcs[9], [None])
    menu_trader_temple.menus = [menu_trader_temple, menu_trader_temple_healed, menu_20]
    menu_trader_temple.add_text_display([menu_trader_temple.npc.name + ": " + "Pick what you want.",
                                         "And pay. The more the better."])
    menu_trader_temple.add_button("[Buy a sword].", menu_trader_temple.give_sword)
    menu_trader_temple.add_button("[Buy a shield].", menu_trader_temple.give_shield)
    menu_trader_temple.add_button("[Buy a potion].", menu_trader_temple.buy_item, [],
                                  lambda: [generate_buy_potion_args])
    menu_trader_temple.add_button("[Buy food or drinks].", menu_trader_temple.buy_item, [],
                                  lambda: [generate_buy_food_args])
    menu_trader_temple.add_button("Sleep. [Heal]", menu_trader_temple.heal, [1, 100])
    menu_trader_temple.add_button("[Continue]", menu_trader_temple.set_transition, [2,
                       "background/temple/1_temple.png", glob.TEMPLE_COLOUR, glob.TEMPLE_MUSIC, glob.TEMPLE_WALK])
    menus.append(menu_trader_temple)



    # story
    menu_56 = StoryMenu(chill_npcs[0], [menu_death])
    menu_56.add_text_display([menu_56.npc.name + ": " + "At last complete victory!",
                              "The wind will speak of your bravery."])
    menu_56.add_button("hhhh.", menu_56.set_menu, [0])
    menu_56.add_button("h", menu_56.set_menu, [0])
    menu_56.add_button("h", menu_56.set_menu, [0])
    menus.append(menu_56)

    menu_55 = StoryMenu(fighting_npcs[8], [menu_death, menu_56, menu_trader_ice])
    menu_55.add_text_display([menu_55.npc.name + ": " + "Ssssssss!"])
    menu_55.add_button("[Fight]", menu_55.fight, [1, True])
    menu_55.add_button("[Return to the village]", menu_55.set_transition, [2,
                       "background/castle/1_garden.png", glob.VILLAGE_FOUNTAIN_COLOUR, glob.VILLAGE_MUSIC, glob.VILLAGE_WALK])
    menus.append(menu_55)

    menu_54 = StoryMenu(fighting_npcs[random.randint(6, 7)], [menu_death, menu_55, menu_trader_ice])
    menu_54.add_text_display([menu_54.npc.name + ": " + "Hakaaaaa!"])
    menu_54.add_button("[Fight]", menu_54.fight, [1])
    menu_54.add_button("[Return to the village]", menu_54.set_transition, [2,
                       "background/castle/1_garden.png", glob.VILLAGE_FOUNTAIN_COLOUR, glob.VILLAGE_MUSIC, glob.VILLAGE_WALK])
    menus.append(menu_54)

    menu_53 = StoryMenu(fighting_npcs[random.randint(6, 7)], [menu_death, menu_54, menu_trader_ice])
    menu_53.add_text_display([menu_53.npc.name + ": " + "Zzzzing!"])
    menu_53.add_button("[Fight]", menu_53.fight, [1])
    menu_53.add_button("[Return to the village]", menu_53.set_transition, [2,
                       "background/castle/1_garden.png", glob.VILLAGE_FOUNTAIN_COLOUR, glob.VILLAGE_MUSIC, glob.VILLAGE_WALK])
    menus.append(menu_53)

    menu_52 = StoryMenu(fighting_npcs[random.randint(6, 7)], [menu_death, menu_53, menu_trader_ice])
    menu_52.add_text_display([menu_52.npc.name + ": " + "Caw caw!"])
    menu_52.add_button("[Fight]", menu_52.fight, [1])
    menu_52.add_button("[Return to the village]", menu_52.set_transition, [2,
                       "background/castle/1_garden.png", glob.VILLAGE_FOUNTAIN_COLOUR, glob.VILLAGE_MUSIC, glob.VILLAGE_WALK])
    menus.append(menu_52)

    menu_51.menus = [menu_death, menu_52, menu_trader_ice]
    menu_51.add_text_display([menu_51.npc.name + ": " + "[Sobering silence]"])
    menu_51.add_button("[Fight]", menu_51.fight, [1])
    menu_51.add_button("[Return to the village]", menu_51.set_transition, [2,
                       "background/castle/1_garden.png", glob.VILLAGE_FOUNTAIN_COLOUR, glob.VILLAGE_MUSIC, glob.VILLAGE_WALK])
    menus.append(menu_51)

    menu_50 = StoryMenu(chill_npcs[1], [happy_death, menu_51])
    menu_50.add_text_display([menu_50.npc.name + ": " + "Listen....", "You can stay with me and forget adventure.",
                              "Let's have a life together."])
    menu_50.add_button("Deal!", menu_50.set_transition, [0,
                       "background/castle/1_garden.png", glob.VILLAGE_FOUNTAIN_COLOUR, glob.VILLAGE_MUSIC, glob.VILLAGE_WALK])
    menu_50.add_button("Adventure calls!", menu_50.set_transition, [1,
                       "background/ice/5_snowy_trees_hd.png", glob.ICE_COLOUR, glob.ICE_MUSIC, glob.ICE_WALK])
    menus.append(menu_50)

    menu_49 = StoryMenu(chill_npcs[1], [menu_50])
    menu_49.add_text_display([menu_49.npc.name + ": " + "Mmmmm, ok sexy hero!"])
    menu_49.add_button('[Go "swim"]', menu_49.set_transition, [0,
                       "background/desert/4_desert_river.png", glob.DESERT_COLOUR, glob.DESERT_MUSIC, glob.DESERT_WALK])
    menus.append(menu_49)

    menu_48 = StoryMenu(chill_npcs[1], [menu_51])
    menu_48.add_text_display([menu_48.npc.name + ": " + "Ahh I hate you!", "I won't look at your unholy body!"])
    menu_48.add_button("Damn it.", menu_48.set_transition, [0,
                       "background/ice/5_snowy_trees_hd.png", glob.ICE_COLOUR, glob.ICE_MUSIC, glob.ICE_WALK])
    menu_48.add_button("Fine!", menu_48.set_transition, [0,
                       "background/ice/5_snowy_trees_hd.png", glob.ICE_COLOUR, glob.ICE_MUSIC, glob.ICE_WALK])
    menus.append(menu_48)

    menu_47 = StoryMenu(chill_npcs[1], [menu_49, menu_48, menu_51])
    menu_47.add_text_display([menu_47.npc.name + ": " + "Her and her husband both.", "Are you coming?"])
    menu_47.add_button("Let's get undressed first.", menu_47.set_menu, [0])
    menu_47.add_button("I will get undressed first.", menu_47.set_menu, [1])
    menu_47.add_button("No. [Go to the icy forest]", menu_47.set_transition, [2,
                       "background/ice/5_snowy_trees_hd.png", glob.ICE_COLOUR, glob.ICE_MUSIC, glob.ICE_WALK])
    menus.append(menu_47)

    menu_46 = StoryMenu(chill_npcs[1], [menu_49, menu_48, menu_47])
    menu_46.add_text_display([menu_46.npc.name + ": " + "You are here so let's go in the water!"])
    menu_46.add_button("Let's get undressed first.", menu_46.set_menu, [0])
    menu_46.add_button("I will get undressed first.", menu_46.set_menu, [1])
    menu_46.add_button("Your friend is weird.", menu_46.set_menu, [1])
    menus.append(menu_46)

    menu_45 = StoryMenu(chill_npcs[4], [slap_death, menu_46])
    menu_45.add_text_display([menu_45.npc.name + ": " + "Don't be a hazz. [Slap]"])
    menu_45.add_button("[Get slapped]", menu_45.take_damage, [1, 5])
    menus.append(menu_45)

    menu_44 = StoryMenu(chill_npcs[4], [menu_46, menu_45])
    menu_44.add_text_display([menu_44.npc.name + ": " + "Ohh. You are Marry's hero.",
                              "You are pretty terrible for a hero.", "What hero would scare an innocent like this!?"])
    menu_44.add_button("I didn't do anything.", menu_44.set_menu, [0])
    menu_44.add_button("I'm sorry.", menu_44.set_menu, [0])
    menu_44.add_button("Who gets scared like that for no reason?", menu_44.set_menu, [1])
    menus.append(menu_44)

    menu_43 = StoryMenu(chill_npcs[4], [menu_44, menu_45])
    menu_43.add_text_display([menu_43.npc.name + ": " + "AAAAAAAAAAAAA!", "Run Marry, it's the mummy!"])
    menu_43.add_button("I'm not the mummy!", menu_43.set_menu, [0])
    menu_43.add_button("My hyenas already ate her.", menu_43.set_menu, [1])
    menus.append(menu_43)

    menu_40 = StoryMenu(chill_npcs[2], [None])
    menu_42 = StoryMenu(chill_npcs[1], [menu_43, menu_40])
    menu_42.add_text_display([menu_42.npc.name + ": " + "Marry.", "I will go bring Aaliya too. See you there."])
    menu_42.add_button("I can't wait!", menu_42.set_transition, [0,
                       "background/desert/4_desert_river.png", glob.DESERT_COLOUR, glob.DESERT_MUSIC, glob.DESERT_WALK])
    menu_42.add_button("Actually, I should continue my adventure.", menu_42.set_menu, [1])
    menus.append(menu_42)

    menu_41 = StoryMenu(chill_npcs[2], [menu_51])
    menu_41.add_text_display([menu_41.npc.name + ": " + "Yummy!"])
    menu_41.add_button("... [Go to the icy forest]", menu_41.set_transition, [0,
                       "background/ice/5_snowy_trees_hd.png", glob.ICE_COLOUR, glob.ICE_MUSIC, glob.ICE_WALK])
    menus.append(menu_41)

    menu_40.menus = [menu_51, menu_41]
    menu_40.add_text_display([menu_40.npc.name + ": " + "I'm Betty. You talked to Marry.",
                              "Did she tell you how to cook a snake?", "Bring me some from the south to eat..."])
    menu_40.add_button("Ok. [Go to the icy forest]", menu_40.set_transition, [0,
                       "background/ice/5_snowy_trees_hd.png", glob.ICE_COLOUR, glob.ICE_MUSIC, glob.ICE_WALK])
    menu_40.add_button("I will add some cockroaches too! [Laugh]", menu_40.set_menu, [1])
    menus.append(menu_40)

    menu_39 = StoryMenu(chill_npcs[1], [menu_40])
    menu_39.add_text_display(["Unknown girl" + ": " + "So focused...", "So driven... So sexy... [Runs away]"])
    menu_39.add_button("Wait!", menu_39.set_menu, [0])
    menu_39.add_button("[I really don't care]", menu_39.set_menu, [0])
    menus.append(menu_39)

    menu_38 = StoryMenu(fighting_npcs[9], [menu_death, menu_40])
    menu_38.add_text_display([menu_38.npc.name + ": " + "Filthy human!", "Now I have a legal excuse to rob you.",
                              "In the name of justice, for mon... um... Marry!"])
    menu_38.add_button("[Fight]", menu_38.fight, [1])
    menus.append(menu_38)

    menu_37 = StoryMenu(chill_npcs[1], [menu_40, menu_38])
    menu_37.add_text_display(["Unknown girl" + ": " + "Pervert!", "Stop making up excuses to follow me!"])
    menu_37.add_button("But I didn't! I meant it...", menu_37.set_menu, [0])
    menu_37.add_button("Ok... [What is wrong with her?]", menu_37.set_menu, [0])
    menu_37.add_button("Next time I will just *%#$@!& you!", menu_37.set_menu, [1])
    menus.append(menu_37)

    menu_36 = StoryMenu(chill_npcs[1], [menu_42, menu_37, menu_39])
    menu_36.add_text_display(["Unknown girl" + ": " + "You actually stopped the mummy!",
                              "Now I can go to the oasis safely.", "And I can bathe and have fun..."])
    menu_36.add_button("Sounds great! I would like to join you... [name?]", menu_36.set_menu, [0])
    menu_36.add_button("Great! I will come as well to make sure it is safe.", menu_36.set_menu, [1])
    menu_36.add_button("Ok. I will continue my exploring in the south.", menu_36.set_menu, [2])
    menus.append(menu_36)

    menu_35 = StoryMenu(fighting_npcs[5], [menu_death, menu_36, menu_trader_desert])
    menu_35.add_text_display([menu_35.npc.name + ": " + "Gravvve robbberrrr!"])
    menu_35.add_button("[Fight]", menu_35.fight, [1, True])
    menu_35.add_button("[Return to the village]", menu_35.set_transition, [2,
                       "background/castle/1_garden.png", glob.VILLAGE_FOUNTAIN_COLOUR, glob.VILLAGE_MUSIC, glob.VILLAGE_WALK])
    menus.append(menu_35)

    menu_34 = StoryMenu(fighting_npcs[random.randint(3, 4)], [menu_death, menu_35, menu_trader_desert])
    menu_34.add_text_display([menu_34.npc.name + ": " + "Hhhhhhh."])
    menu_34.add_button("[Fight]", menu_34.fight, [1])
    menu_34.add_button("[Return to the village]", menu_34.set_transition, [2,
                       "background/castle/1_garden.png", glob.VILLAGE_FOUNTAIN_COLOUR, glob.VILLAGE_MUSIC, glob.VILLAGE_WALK])
    menus.append(menu_34)

    menu_33 = StoryMenu(fighting_npcs[random.randint(3, 4)], [menu_death, menu_34, menu_trader_desert])
    menu_33.add_text_display([menu_33.npc.name + ": " + "Rargh!"])
    menu_33.add_button("[Fight]", menu_33.fight, [1])
    menu_33.add_button("[Return to the village]", menu_33.set_transition, [2,
                       "background/castle/1_garden.png", glob.VILLAGE_FOUNTAIN_COLOUR, glob.VILLAGE_MUSIC, glob.VILLAGE_WALK])
    menus.append(menu_33)

    menu_32 = StoryMenu(fighting_npcs[random.randint(3, 4)], [menu_death, menu_33, menu_trader_desert])
    menu_32.add_text_display([menu_32.npc.name + ": " + "Aauuughhh."])
    menu_32.add_button("[Fight]", menu_32.fight, [1])
    menu_32.add_button("[Return to the village]", menu_32.set_transition, [2,
                       "background/castle/1_garden.png", glob.VILLAGE_FOUNTAIN_COLOUR, glob.VILLAGE_MUSIC, glob.VILLAGE_WALK])
    menus.append(menu_32)

    menu_31.menus = [menu_death, menu_32, menu_trader_desert]
    menu_31.add_text_display([menu_31.npc.name + ": " + "[Sand noise]"])
    menu_31.add_button("[Fight]", menu_31.fight, [1])
    menu_31.add_button("[Return to the village]", menu_31.set_transition, [2,
                       "background/castle/1_garden.png", glob.VILLAGE_FOUNTAIN_COLOUR, glob.VILLAGE_MUSIC, glob.VILLAGE_WALK])
    menus.append(menu_31)

    menu_30 = StoryMenu(chill_npcs[3], [menu_31])
    menu_30.add_text_display([menu_30.npc.name + ": " + "Allah can kill you."])
    menu_30.add_button("You wish. [Go to the desert]", menu_30.set_transition, [0,
                       "background/desert/3_oasis.png", glob.DESERT_COLOUR, glob.DESERT_MUSIC, glob.DESERT_WALK])
    menus.append(menu_30)

    menu_29 = StoryMenu(chill_npcs[3], [menu_31])
    menu_29.add_text_display([menu_29.npc.name + ": " + "Really? Have my money."])
    menu_29.add_button("Ok. [Go to the desert]", menu_29.get_money, [0, 10, True,
                       "background/desert/3_oasis.png", glob.DESERT_COLOUR, glob.DESERT_MUSIC, glob.DESERT_WALK])
    menu_29.add_button("No thanks. [Go to the desert]", menu_29.set_transition, [0,
                       "background/desert/3_oasis.png", glob.DESERT_COLOUR, glob.DESERT_MUSIC, glob.DESERT_WALK])
    menus.append(menu_29)

    menu_28 = StoryMenu(chill_npcs[3], [menu_29, menu_30, menu_31])
    menu_28.add_text_display([menu_28.npc.name + ": " + "Hello. I am AHMET.", "Allah will save us."])
    menu_28.add_button("Allah sent me.", menu_28.set_menu, [0])
    menu_28.add_button("My god is better.", menu_28.set_menu, [1])
    menu_28.add_button("Ok. [Go to the desert]", menu_28.set_transition, [2,
                       "background/desert/3_oasis.png", glob.DESERT_COLOUR, glob.DESERT_MUSIC, glob.DESERT_WALK])
    menus.append(menu_28)

    menu_27 = StoryMenu(chill_npcs[0], [menu_28])
    menu_27.add_text_display([menu_27.npc.name + ": " + "That guy."])
    menu_27.add_button("[Continue]", menu_27.set_menu, [0])
    menus.append(menu_27)

    menu_26 = StoryMenu(chill_npcs[0], [menu_27, menu_28])
    menu_26.add_text_display([menu_26.npc.name + ": " + "Ahmet is very religious."])
    menu_26.add_button("Who is Ahmet?", menu_26.set_menu, [0])
    menu_26.add_button("I will be careful.", menu_26.set_menu, [1])
    menus.append(menu_26)

    menu_25 = StoryMenu(chill_npcs[0], [menu_26, menu_28])
    menu_25.add_text_display([menu_25.npc.name + ": " + "Wow, you killed them all!",
                              "Do you want to buy a potato or some advice?"])
    menu_25.add_button("Advice. [Give 1 coin]", menu_25.give_money, [0, 1])
    menu_25.add_button("Potato. [Give 2 coin]", menu_25.buy_item,
                       args=[[(menu_25.get_items, [1, ["Potato"]]), (menu_25.give_money, [1, 2])]])
    menu_25.add_button("No. [Continue]", menu_25.set_menu, [1])
    menus.append(menu_25)

    menu_24 = StoryMenu(fighting_npcs[2], [menu_death, menu_25, menu_trader_temple])
    menu_24.add_text_display([menu_24.npc.name + ": " + "Flop."])
    menu_24.add_button("[Fight]", menu_24.fight, [1, True])
    menu_24.add_button("[Return to the village]", menu_24.set_transition, [2,
                       "background/castle/1_garden.png", glob.VILLAGE_FOUNTAIN_COLOUR, glob.VILLAGE_MUSIC, glob.VILLAGE_WALK])
    menus.append(menu_24)

    menu_23 = StoryMenu(fighting_npcs[random.randint(0, 1)], [menu_death, menu_24, menu_trader_temple])
    menu_23.add_text_display([menu_23.npc.name + ": " + "Hhhhhuargh."])
    menu_23.add_button("[Fight]", menu_23.fight, [1])
    menu_23.add_button("[Return to the village]", menu_23.set_transition, [2,
                       "background/castle/1_garden.png", glob.VILLAGE_FOUNTAIN_COLOUR, glob.VILLAGE_MUSIC, glob.VILLAGE_WALK])
    menus.append(menu_23)

    menu_22 = StoryMenu(fighting_npcs[random.randint(0, 1)], [menu_death, menu_23, menu_trader_temple])
    menu_22.add_text_display([menu_22.npc.name + ": " + "Mumph."])
    menu_22.add_button("[Fight]", menu_22.fight, [1])
    menu_22.add_button("[Return to the village]", menu_22.set_transition, [2,
                       "background/castle/1_garden.png", glob.VILLAGE_FOUNTAIN_COLOUR, glob.VILLAGE_MUSIC, glob.VILLAGE_WALK])
    menus.append(menu_22)

    menu_21 = StoryMenu(fighting_npcs[random.randint(0, 1)], [menu_death, menu_22, menu_trader_temple])
    menu_21.add_text_display([menu_21.npc.name + ": " + "Brrrgh."])
    menu_21.add_button("[Fight]", menu_21.fight, [1])
    menu_21.add_button("[Return to the village]", menu_21.set_transition, [2,
                       "background/castle/1_garden.png", glob.VILLAGE_FOUNTAIN_COLOUR, glob.VILLAGE_MUSIC, glob.VILLAGE_WALK])
    menus.append(menu_21)

    menu_20.menus = [menu_death, menu_21, menu_trader_temple]
    menu_20.add_text_display([menu_20.npc.name + ": " + "Blarghhh."])
    menu_20.add_button("[Fight]", menu_20.fight, [1])
    menu_20.add_button("[Return to the village]", menu_20.set_transition, [2,
                       "background/castle/1_garden.png", glob.VILLAGE_FOUNTAIN_COLOUR, glob.VILLAGE_MUSIC, glob.VILLAGE_WALK])
    menus.append(menu_20)

    menu_11 = StoryMenu(fighting_npcs[9], None)
    menu_19 = StoryMenu(fighting_npcs[9], [menu_11])
    menu_19.add_text_display([menu_19.npc.name + ": " + "I am THE TRADER."])
    menu_19.add_button("Ok... how can I earn some money?", menu_19.set_menu, [0])
    menus.append(menu_19)


    menu_18 = StoryMenu(fighting_npcs[9], [menu_20])
    menu_18.add_text_display([menu_18.npc.name + ": " + "You insult me."])
    menu_18.add_button("Whatever. [Go to the temple]", menu_18.set_transition, [0,
                       "background/temple/1_temple.png", glob.TEMPLE_COLOUR, glob.TEMPLE_MUSIC, glob.TEMPLE_WALK])
    menus.append(menu_18)

    menu_17 = StoryMenu(fighting_npcs[9], [menu_18, menu_20])
    menu_17.add_text_display([menu_17.npc.name + ": " + "Never."])
    menu_17.add_button("Stop lying.", menu_17.set_menu, [0])
    menu_17.add_button("Whatever. [Go to the temple]", menu_17.set_transition, [1,
                       "background/temple/1_temple.png", glob.TEMPLE_COLOUR, glob.TEMPLE_MUSIC, glob.TEMPLE_WALK])
    menus.append(menu_17)

    menu_16 = StoryMenu(fighting_npcs[9], [menu_17, menu_20])
    menu_16.add_text_display([menu_16.npc.name + ": " + "No."])
    menu_16.add_button("Yes, you did.", menu_16.set_menu, [0])
    menu_16.add_button("Whatever. [Go to the temple]", menu_16.set_transition, [1,
                       "background/temple/1_temple.png", glob.TEMPLE_COLOUR, glob.TEMPLE_MUSIC, glob.TEMPLE_WALK])
    menus.append(menu_16)

    menu_15 = StoryMenu(fighting_npcs[9], [menu_16, menu_20])
    menu_15.add_text_display([menu_15.npc.name + ": " + "Hehehe... umm...", "You just need to believe in yourself."])
    menu_15.add_button("So you just scammed me.", menu_15.set_menu, [0])
    menu_15.add_button("I guess. [Go to the temple]", menu_15.set_transition, [1,
                       "background/temple/1_temple.png", glob.TEMPLE_COLOUR, glob.TEMPLE_MUSIC, glob.TEMPLE_WALK])
    menus.append(menu_15)

    menu_14 = StoryMenu(fighting_npcs[9], [menu_15, menu_20])
    menu_14.add_text_display([menu_14.npc.name + ": " + "If you give me your money I can heal you."])
    menu_14.add_button("Ok. [Give him your money]", menu_14.give_money, [0, -1])
    menu_14.add_button("No. [Go to the temple]", menu_14.set_transition, [1,
                       "background/temple/1_temple.png", glob.TEMPLE_COLOUR, glob.TEMPLE_MUSIC, glob.TEMPLE_WALK])
    menus.append(menu_14)

    menu_13 = StoryMenu(fighting_npcs[9], [menu_20])
    menu_13.add_text_display([menu_13.npc.name + ": " + "What a shame."])
    menu_13.add_button("[Go to the temple]", menu_13.set_transition, [0,
                       "background/temple/1_temple.png", glob.TEMPLE_COLOUR, glob.TEMPLE_MUSIC, glob.TEMPLE_WALK])
    menus.append(menu_13)

    menu_12 = StoryMenu(fighting_npcs[9], [menu_14, menu_13])
    menu_12.add_text_display([menu_12.npc.name + ": " + "Do you have any mental issues?"])
    menu_12.add_button("Yes.", menu_12.set_menu, [0])
    menu_12.add_button("No.", menu_12.set_menu, [1])
    menus.append(menu_12)

    menu_11.menus = [menu_20, menu_12]
    menu_11.add_text_display([menu_11.npc.name + ": " + "Go to the temple and kill some monsters.",
                             "Don't forget to get some sleep too occasionally", "to restore your strength."])
    menu_11.add_button("Ok. [Go to the temple]", menu_11.set_transition, [0,
                       "background/temple/1_temple.png", glob.TEMPLE_COLOUR, glob.TEMPLE_MUSIC, glob.TEMPLE_WALK])
    menu_11.add_button("Ok, but how can I earn money?", menu_11.set_menu, [1])
    menus.append(menu_11)

    menu_10 = StoryMenu(fighting_npcs[9], [menu_11])
    menu_10.add_text_display([menu_10.npc.name + ": " + "I am THE TRADER.",
                             "I do real business with real money."])
    menu_10.add_button("Ok... how can I earn some money?", menu_10.set_menu, [0])
    menus.append(menu_10)

    menu_9 = StoryMenu(fighting_npcs[9], [menu_10, menu_19, menu_11])
    menu_9.add_text_display(["Probable trader" + ": " + "A new client?", "You look poor.",
                             "Come back when you have some money."])
    menu_9.add_button("But I have some money!", menu_9.set_menu, [0])
    menu_9.add_button("So you are a trader?", menu_9.set_menu, [0])
    menu_9.add_button("How can I earn some money?", menu_9.set_menu, [0])
    menus.append(menu_9)

    menu_8 = StoryMenu(chill_npcs[1], [menu_9])
    menu_8.add_text_display(["Unknown girl" + ": " + "Fuck off!"])
    menu_8.add_button("Ok", menu_8.set_menu, [0])
    menus.append(menu_8)

    menu_7 = StoryMenu(chill_npcs[1], [menu_8, menu_9])
    menu_7.add_text_display(["Unknown girl" + ": " + "Deepshit!"])
    menu_7.add_button("That's unexpected!", menu_7.set_menu, [0])
    menu_7.add_button("Fair enough. [Continue]", menu_7.set_menu, [1])
    menus.append(menu_7)

    menu_6 = StoryMenu(chill_npcs[1], [menu_9])
    menu_6.add_text_display(["Unknown girl" + ": " + "Beautiful singing!", "Have a turnip!"])
    menu_6.add_button("Thanks! <Get a turnip>", menu_6.get_items, [0, ["Turnip"]])
    menus.append(menu_6)

    menu_5 = StoryMenu(chill_npcs[1], [menu_6, menu_9])
    menu_5.add_text_display(["Unknown girl" + ": " + "La-la-la-la-la!"])
    menu_5.add_button("La-la-la-la-la!", menu_5.set_menu, [0])
    menu_5.add_button("[Continue]", menu_5.set_menu, [1])
    menus.append(menu_5)

    menu_4 = StoryMenu(chill_npcs[1], [menu_5, menu_9])
    menu_4.add_text_display(["Unknown girl" + ": " + "La-la-la-la!"])
    menu_4.add_button("La-la-la-la!", menu_4.set_menu, [0])
    menu_4.add_button("[Continue]", menu_4.set_menu, [1])
    menus.append(menu_4)

    menu_3 = StoryMenu(chill_npcs[1], [menu_4, menu_7, menu_9])
    menu_3.add_text_display(["Unknown girl" + ": " + "La-la-la!"])
    menu_3.add_button("La-la-la!", menu_3.set_menu, [0])
    menu_3.add_button("...", menu_3.set_menu, [2])
    menu_3.add_button("Shut up!", menu_3.set_menu, [1])
    menus.append(menu_3)

    menu_2 = StoryMenu(chill_npcs[0], [menu_3, menu_9])
    menu_2.add_text_display([menu_2.npc.name + ": " + "Thank you!", "If you want to buy new gear you can talk ",
                             "to the trader when you are in the village."])
    menu_2.add_button("Thanks. [Continue]", menu_2.set_menu, [0])
    menu_2.add_button("Thanks. [Visit the trader]", menu_2.set_menu, [1])
    menus.append(menu_2)

    menu_1 = StoryMenu(chill_npcs[0], [menu_2, menu_3])
    menu_1.add_text_display([menu_1.npc.name + ": " + "Welcome, whoever you are!", "Do you have any spare change?"])
    menu_1.add_button("Yes. [Give 1 coin]", menu_1.give_money, [0, 1])
    menu_1.add_button("No. [Leave]", menu_1.set_menu, [1])
    menus.append(menu_1)

    return menus

    # traderul este scammer
    # taranul e sarac si atotstiutor
    # marry e bipolara
    # betty e fomista si il place pe ahmet
    # ahmet e religion freak si in rest usor manipulabil
    # aaliya e sperioasa dar cu gura mare
