from inventory.item import Item

items = []

# edibles

# drinks
#0
items.append(Item("Beer", "beer", 5, True, [1]))

#1
items.append(Item("Wine", "wine", 15, True, [10]))

# food
#2
items.append(Item("Cheese", "cheese", 8, True, [8]))

#3
items.append(Item("Chicken", "chicken",  12, True, [9]))

#4
items.append(Item("Potato", "potato", 2, True, [3]))

#5
items.append(Item("Pretzel", "pretzel", 15, True, [7]))

#6
items.append(Item("Turnip", "turnip", 1, True, [2]))

#7
items.append(Item("Watermelon", "watermelon", 9, True, [6]))

# potions
#8
items.append(Item("Attack potion", "potions/attack_potion", 20, True, [10]))

#9
items.append(Item("Defense potion", "potions/defense_potion", 20, True, [2]))

#10
items.append(Item("HP potion", "potions/hp_potion", 20, True, [15]))


# swords
#11
items.append(Item("Rusty sword", "sword1", 10, False, [12]))

#12
items.append(Item("Iron sword", "sword2", 70, False, [18]))

#13
items.append(Item("Templar sword", "sword3", 120, False, [23]))

#14
items.append(Item("Knight sword", "sword4", 150, False, [27]))

#15
items.append(Item("Dark Lord sword", "sword5", 200, False, [30]))


# shields
#16
items.append(Item("Wooden shield", "shield1", 10, False, [3]))

#17
items.append(Item("Iron shield", "shield2", 70, False, [6]))

#18
items.append(Item("Templar shield", "shield3", 120, False, [9]))

#19
items.append(Item("Knight shield", "shield4", 150, False, [12]))

#20
items.append(Item("Dark Lord shield", "shield5", 200, False, [15]))


# others
#21
items.append(Item("Boomerang", "boomerang", 4, False, []))

#22
items.append(Item("Pickaxe", "pickaxe", 30, False,[]))

#23
items.append(Item("Happy Pig", "pig_head", 100, False,[]))

#24
items.append(Item("Boxer Glove", "glove", 7, False, []))