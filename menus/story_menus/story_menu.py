import copy

import pygame
import pygame_menu
import glob
from game.battle import fight


# Initialize Pygame
pygame.init()

class StoryMenu:
    def __init__(self, npc, next_menus):
        self.npc = npc
        self.menu = pygame_menu.Menu("", glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT, theme=glob.custom_play_theme,
                                     center_content=False)
        self.menus = next_menus
        self.next_menu = None
        self.game = None
        self.transition = False
        self.next_background = None
        self.next_bar_color = None
        self.next_music = None
        self.next_walking_effect = None
        self.action_duration = 0
        self.in_action = 1 / glob.ACTION_FRAMES


    # def player_attack(self):
    #     print(11)
    #     self.game.player.attack()
    #     self.npc.take_damage(self.game.player.atk)
    #
    #
    # def npc_attack(self):
    #     self.npc.attack()
    #     self.game.player.take_damage(self.npc.atk)

    # def show_error(self, label):
    #     global error_menu
    #     error_menu = StoryMenu(self.npc, [self])
    #     error_menu.add_text_display([label])
    #     error_menu.add_button("OK", error_menu.set_menu, 0)

    def show_error(self, label):
        error_menu = pygame_menu.Menu('Error!', glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT, theme=glob.custom_play_theme)
        error_menu.add.label(label)
        error_menu.add.button('OK', lambda: setattr(self, 'showing_error', False))

        self.showing_error = True
        while self.showing_error:
            self.game.screen.blit(self.game.background, (0, 0))  # Draw the game background
            error_menu.update(pygame.event.get())
            error_menu.draw(self.game.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and error_menu.get_selected_widget().get_rect().collidepoint(event.pos):
                        error_menu.get_selected_widget().apply()
        pygame.time.wait(100)
        pygame.event.clear()


    def heal(self, index, amount):
        self.next_menu = self.menus[index]
        if self.game.player.hp + amount > self.game.player.total_hp:
            self.game.player.hp = self.game.player.total_hp
        else:
            self.game.player.hp += amount
        self.game.player.health_bar_hp = self.game.player.hp


    def take_damage(self, index, amount):
        self.next_menu = self.menus[index]

        if self.game.player.hp - amount < 0:
            self.game.player.hp = 0
        else:
            self.game.player.hp -= amount

        if self.game.player.hp == 0:
            glob.can_continue = False
            self.set_transition(0, "background/castle/1_garden.png",
                                glob.VILLAGE_FOUNTAIN_COLOUR, glob.VILLAGE_MUSIC, glob.VILLAGE_WALK)


    def fight(self, index, transition_back=False):
        self.next_menu = self.menus[index]
        self.in_action = fight(self.game.player, self.npc)

        if self.game.player.hp == 0:
            glob.can_continue = False
            self.set_transition(0, "background/castle/1_garden.png",
                                glob.VILLAGE_FOUNTAIN_COLOUR, glob.VILLAGE_MUSIC, glob.VILLAGE_WALK)
        elif transition_back:
            self.set_transition(index, "background/castle/1_garden.png",
                                glob.VILLAGE_FOUNTAIN_COLOUR, glob.VILLAGE_MUSIC, glob.VILLAGE_WALK)

        # if self.game.player.hp <= 0:
        #     return glob.DEATH
        # return 0


    def get_items(self, index, items):
        self.next_menu = self.menus[index]
        for i in range(len(items)):
            rc = self.game.player.inventory.add_item(items[i])
            if rc != 1:
                for j in range(i):
                    self.game.player.inventory.remove_item(items[j])
                self.show_error("Not enough space in inventory!")
                self.next_menu = self
                return


    def give_items(self, index, items):
        self.next_menu = self.menus[index]
        for item in items:
            if not self.game.player.inventory.has_item(item):
                self.show_error("Missing items!")
                self.next_menu = self
                return
        for item in items:
            self.game.player.inventory.remove_item(item)


    def get_money(self, index, amount, transition_back=False, next_background=None, next_bar_color=None,
                  next_music=None, next_walking_effect=None):
        self.next_menu = self.menus[index]
        self.game.player.money += amount

        if (transition_back):
            self.set_transition(index, next_background, next_bar_color, next_music, next_walking_effect)


    def give_money(self, index, amount):
        if self.game.player.money >= amount:
            self.next_menu = self.menus[index]
            if amount == -1:
                self.game.player.money = 0
            else:
                self.game.player.money -= amount
        else:
            self.show_error("Not enough coins!")
            self.next_menu = self


    def give_sword(self):
        self.next_menu = self
        if self.game.player.money >= glob.swords[self.game.next_sword][1]:
            if self.game.player.inventory.add_item(glob.swords[self.game.next_sword][0]):
                self.game.player.money -= glob.swords[self.game.next_sword][1]
                self.game.next_sword = min(self.game.next_sword + 1, len(glob.swords) - 1)
            else:
                self.show_error("Not enough space in inventory!")
        else:
            self.show_error("Not enough coins!")
        pygame.time.wait(100)
        pygame.event.clear()


    def give_shield(self):
        self.next_menu = self
        if self.game.player.money >= glob.shields[self.game.next_shield][1]:
            if self.game.player.inventory.add_item(glob.shields[self.game.next_shield][0]):
                self.game.player.money -= glob.swords[self.game.next_shield][1]
                self.game.next_shield = min(self.game.next_shield + 1, len(glob.shields) - 1)
            else:
                self.show_error("Not enough space in inventory!")
        else:
            self.show_error("Not enough coins!")
        pygame.time.wait(100)
        pygame.event.clear()


    def set_transition(self, index, next_background, next_bar_color, next_music, next_walking_effect):
        self.next_menu = self.menus[index]
        self.transition = True
        self.next_background = next_background
        self.next_bar_color = next_bar_color
        self.next_music = next_music
        self.next_walking_effect = next_walking_effect
        pygame.time.wait(100)


    def buy_item(self, methods_with_args):
        method1, args1 = methods_with_args[0]
        method2, args2 = methods_with_args[1]

        if self.game.player.money < args2[1]:
            self.show_error("Not enough coins!")
            self.next_menu = self
            return

        method1(*args1)
        method2(*args2)
        self.next_menu = self


    def set_menu(self, index):
        self.next_menu = self.menus[index]


    def add_text_display(self, labels):
        for label in labels:
            self.menu.add.label(label)


    def add_button(self, text, method, args=None, args_func=None):
        if args is None:
            args = []
        if args_func:
            self.menu.add.button(text, lambda: method(*args_func()))
        else:
            self.menu.add.button(text, lambda: method(*args))

    # def add_button(self, text, index, method, *args):
    #     def button_action():
    #         method(index, *args)  # Call the method with index and additional arguments
    #
    #     self.menu.add.button(text, button_action)

    # def deselect_all_widgets(self):
    #     # Iterate over all widgets in the menu and deselect them
    #     for widget in self.menu.get_widgets():
    #         if widget.is_selectable:
    #             widget._selected = False  # Deselect all widgets

    # story menu loop
    def gameplay_menu(self, events):
        menu = self.menu

        # Handle the active menu
        if self.action_duration == 0:
            if not menu.is_enabled():
                menu.enable()
            menu.update(events)  # Update menu widgets
            menu.draw(self.game.screen)  # Draw menu widgets on top
        self.npc.draw()

        if self.action_duration > 1:
            if menu.enable():
                menu.disable()
            self.action_duration -= 1
            return glob.CONTINUE
        elif self.action_duration == 1:
            if self.next_menu is not None and self.next_menu.npc.name == self.npc.name:
                glob.same_npc = True
            elif self.next_menu is not None and self.next_menu.npc.name != self.npc.name:
                glob.same_npc = False

            self.in_action = 1 / glob.ACTION_FRAMES
            self.npc.reset()
            self.action_duration = 0

            if self.next_menu is None:
                return None

            # Create deep copies of the values
            next_menu_copy = self.next_menu
            transition_copy = self.transition
            next_background_copy = self.next_background
            next_bar_color_copy = self.next_bar_color
            next_music_copy = self.next_music
            next_walking_effect_copy = self.next_walking_effect

            # Reset the original values in self
            self.next_menu = None
            self.transition = False
            self.next_background = None
            self.next_bar_color = None
            self.next_music = None
            self.next_walking_effect = None

            # Return the deep copies
            return [next_menu_copy, transition_copy, next_background_copy, next_bar_color_copy, next_music_copy,
                    next_walking_effect_copy]

        for event in events:
            # check if enter key was pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    menu.disable()
                    self.action_duration = glob.ACTION_FRAMES * self.in_action
                    #return self.next_menu

            # check if mouse was clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check if a menu item was clicked
                if event.button == 1 and menu.get_selected_widget().get_rect().collidepoint(event.pos):
                    menu.get_selected_widget().apply()
                    menu.disable()
                    self.action_duration = glob.ACTION_FRAMES * self.in_action
                    #return self.next_menu
        return glob.CONTINUE