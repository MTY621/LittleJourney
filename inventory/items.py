from inventory.item import Item

items = []

# edibles

# drinks
#0
items.append(Item("Beer", "beer", True, [1]))

#1
items.append(Item("Wine", "wine", True, [10]))

# food
#2
items.append(Item("Cheese", "cheese", True, [8]))

#3
items.append(Item("Chicken", "chicken",  True, [9]))

#4
items.append(Item("Potato", "potato", True, [3]))

#5
items.append(Item("Pretzel", "pretzel", True, [7]))

#6
items.append(Item("Turnip", "turnip", True, [2]))

#7
items.append(Item("Watermelon", "watermelon", True, [6]))

# potions
#8
items.append(Item("Attack potion", "potions/attack_potion", True, [10]))

#9
items.append(Item("Defense potion", "potions/defense_potion", True, [2]))

#10
items.append(Item("HP potion", "potions/hp_potion", True, [15]))


# swords
#11
items.append(Item("Rusty sword", "sword1", False, [12]))

#12
items.append(Item("Iron sword", "sword2", False, [18]))

#13
items.append(Item("Templar sword", "sword3", False, [23]))

#14
items.append(Item("Knight sword", "sword4", False, [27]))

#15
items.append(Item("Dark Lord sword", "sword5", False, [30]))


# shields
#16
items.append(Item("Wooden shield", "shield1", False, [3]))

#17
items.append(Item("Iron shield", "shield2", False, [6]))

#18
items.append(Item("Templar shield", "shield3", False, [9]))

#19
items.append(Item("Knight shield", "shield4", False, [12]))

#20
items.append(Item("Dark Lord shield", "shield5", False, [15]))


# others
#21
items.append(Item("Boomerang", "boomerang", False, []))

#22
items.append(Item("Pickaxe", "pickaxe",  False,[]))

#23
items.append(Item("Happy Pig", "pig_head",  False,[]))

#24
items.append(Item("Boxer Glove", "glove", False, []))