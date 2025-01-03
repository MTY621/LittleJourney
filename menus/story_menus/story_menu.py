import pygame
import pygame_menu

import glob


# Initialize Pygame
pygame.init()


class StoryMenu:
    def __init__(self, npc, next_menus):
        self.npc = npc
        self.menu = pygame_menu.Menu("", glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT, theme=glob.custom_play_theme)
        self.menus = next_menus
        self.next_menu = None
        self.game = None


    def player_attack(self):
        print(11)
        self.game.player.attack()
        self.npc.take_damage(self.game.player.atk)


    def npc_attack(self):
        self.npc.attack()
        self.game.player.take_damage(self.game.player.atk)


    def get_items(self, items):
        for item in items:
            #add to inventory
            pass


    def add_text_display(self, labels, index):
        for label in labels:
            self.menu.add.label(label)
        self.next_menu =  self.menus[index]


    def add_button(self, text, function, index):
        self.menu.add.button(text, function)
        self.next_menu = self.menus[index]

    # Main menu loop
    def gameplay_menu(self, events):
        menu = self.menu
        if not menu.is_enabled():
            menu.enable()

        # Handle the active menu
        menu.update(events)  # Update menu widgets
        menu.draw(self.game.screen)  # Draw menu widgets on top

        pygame.display.update()

        for event in events:
            # check if enter key was pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    menu.disable()
                    return self.next_menu

            # check if mouse was clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check if a menu item was clicked
                if event.button == 1 and menu.get_selected_widget().get_rect().collidepoint(event.pos):
                    menu.get_selected_widget().apply()
                    menu.disable()
                    return self.next_menu
        return glob.CONTINUE