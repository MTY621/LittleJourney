import pygame
from menus.story_menus.story_menu import StoryMenu
from characters.npcs import fighting_npcs, chill_npcs
import extra_info



menu_2 = StoryMenu(fighting_npcs.fighting_1, [None])
menu_2.add_button("Attack NPC", menu_2.player_attack, 0)

menu_1 = StoryMenu(chill_npcs.chill_1, [None, menu_2])
menu_1.add_text_display(["Welcome to the story menu"], 0)
menu_1.add_button("Attack NPC", menu_1.player_attack, 1)


# Main menu loop
def gameplay_menu(story_menu):
    menu = story_menu.menu
    menu.enable()
    while True:
        events = pygame.event.get()

        # Handle the active menu
        extra_info.screen.blit(extra_info.background, (0, 0))  # Ensure the background is drawn before the menu
        menu.update(events)  # Update menu widgets
        menu.draw(extra_info.screen)  # Draw menu widgets on top

        pygame.display.update()

        for event in events:
            # check if enter key was pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    menu.disable()
                    return story_menu.next_menu

            # check if mouse was clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check if a menu item was clicked
                if event.button == 1 and menu.get_selected_widget().get_rect().collidepoint(event.pos):
                    menu.get_selected_widget().apply()
                    menu.disable()
                    return story_menu.next_menu
