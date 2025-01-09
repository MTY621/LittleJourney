from inventory.item import Item

items = []

# edibles

# drinks
#0
items.append(Item("Beer", "beer", "drink", 5, True, [1]))

#1
items.append(Item("Wine", "wine", "drink", 15, True, [10]))

# food
#2
items.append(Item("Cheese", "cheese", "food", 8, True, [8]))

#3
items.append(Item("Chicken", "chicken", "food", 12, True, [9]))

#4
items.append(Item("Potato", "potato", "food", 2, True, [3]))

#5
items.append(Item("Pretzel", "pretzel", "food", 15, True, [7]))

#6
items.append(Item("Turnip", "turnip", "food", 1, True, [2]))

#7
items.append(Item("Watermelon", "watermelon", "food", 9, True, [6]))

# potions
#8
items.append(Item("Attack potion", "potions/attack_potion", "potion", 20, True, [5]))

#9
items.append(Item("Defense potion", "potions/defense_potion", "potion", 20, True, [2]))

#10
items.append(Item("HP potion", "potions/hp_potion", "potion", 20, True, [15]))


# swords
#11
items.append(Item("Rusty sword", "sword1", "sword", 10, False, [7]))

#12
items.append(Item("Iron sword", "sword2", "sword", 70, False, [14]))

#13
items.append(Item("Templar sword", "sword3", "sword", 120, False, [21]))

#14
items.append(Item("Knight sword", "sword4", "sword", 160, False, [28]))

#15
items.append(Item("Dark Lord sword", "sword5", "sword", 200, False, [35]))


# shields
#16
items.append(Item("Wooden shield", "shield1", "shield", 10, False, [3]))

#17
items.append(Item("Iron shield", "shield2", "shield", 70, False, [6]))

#18
items.append(Item("Templar shield", "shield3", "shield", 120, False, [9]))

#19
items.append(Item("Knight shield", "shield4", "shield", 160, False, [12]))

#20
items.append(Item("Dark Lord shield", "shield5", "shield", 200, False, [15]))


# others
#21
items.append(Item("Boomerang", "boomerang", "other", 4, False, []))

#22
items.append(Item("Pickaxe", "pickaxe", "other", 30, False,[]))

#23
items.append(Item("Happy Pig", "pig_head", "other", 100, False,[]))

#24
items.append(Item("Boxer Glove", "glove", "other", 7, False, []))