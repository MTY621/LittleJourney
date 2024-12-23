import pygame
from inventory import Inventory
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50
FRAME_SIZE = 64
FRAMES_PER_ROW = 6

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

# Initialize the inventory
inventory = Inventory(SCREEN_WIDTH, SCREEN_HEIGHT)
inventory.add_player_item("Sword")
inventory.add_player_item("Pickaxe")
inventory.add_player_item("Beer")
inventory.add_player_item("Pretzel")
inventory.add_player_item("Bronze Axe")

# Pygame screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Inventory System")

# Main loop variables
running = True

while running:
    screen.fill(WHITE)

    # Draw the inventory
    inventory.draw(screen)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        inventory.handle_event(event)

    pygame.display.flip()

pygame.quit()