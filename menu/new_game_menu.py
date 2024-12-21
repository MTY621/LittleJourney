from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes

import globals

pygame.init()
surface = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
background = pygame.image.load('background/cave/background4.png').convert()


def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)


def start_the_game():
    mainmenu._open(loading)
    pygame.time.set_timer(update_loading, 10)


def level_menu():
    mainmenu._open(level)


mainmenu = pygame_menu.Menu('New game', globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT, theme=themes.THEME_DARK)
mainmenu.add.text_input('Name: ', default='username')
mainmenu.add.button('Continue', start_the_game)
mainmenu.add.button('Cancel', pygame_menu.events.EXIT)

level = pygame_menu.Menu('Select a Difficulty', globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT, theme=themes.THEME_BLUE)
level.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)

loading = pygame_menu.Menu('Loading the Game...', globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT, theme=themes.THEME_DARK)
loading.add.progress_bar("Progress", progressbar_id="1", default=0, width=200, )

left_arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))
right_arrow = pygame_menu.widgets.RightArrowSelection(arrow_size=(10, 15))

update_loading = pygame.USEREVENT + 0

def menu():
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == update_loading:
                progress = loading.get_widget("1")
                progress.set_value(progress.get_value() + 1)
                if progress.get_value() == 100:
                    pygame.time.set_timer(update_loading, 0)
                    mainmenu.disable()
                    surface.blit(background, (0, 0))
            if event.type == pygame.QUIT:
                exit()

        if mainmenu.is_enabled():
            mainmenu.update(events)
            mainmenu.draw(surface)
            if (mainmenu.get_current().get_selected_widget()):
                left_arrow.draw(surface, mainmenu.get_current().get_selected_widget())
                right_arrow.draw(surface, mainmenu.get_current().get_selected_widget())

        pygame.display.update()