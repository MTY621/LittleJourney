import pygame
import random
from item import Item


# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 100
FRAME_SIZE = 64
MAX_ITEMS = 8

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
ACTIVE_COLOR = (100, 150, 200)
INACTIVE_COLOR = GRAY

# Initialize Pygame
pygame.init()

# Load the sprite sheet
sprite_sheet = pygame.image.load("./../items/sword.png")
button_image = pygame.image.load("background.png")

# Define the dimensions of each sprite in the sheet
SPRITE_WIDTH = 16
SPRITE_HEIGHT = 16

# Randomly generate names and descriptions
ITEM_NAMES = [
    "Ruby Gem", "Emerald Shard", "Sapphire Stone", "Diamond Nugget",
    "Copper Ore", "Silver Ingot", "Gold Bar", "Platinum Chunk",
    "Iron Pickaxe", "Gold Sword", "Bronze Axe", "Crystal Blade"
]
ITEM_DESCRIPTIONS = [
    "A shiny and precious gem.", "A rare and valuable metal.",
    "An ancient tool forged by dwarves.", "A legendary weapon of heroes.",
    "A resource for crafting.", "A decorative artifact of great value."
]

def random_description():
    return random.choice(ITEM_DESCRIPTIONS)

class Inventory:
    def __init__(self, screen_width, screen_height):
        self.available_items = {}
        self.player_items = []
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.selected_item = None

        # Inventory button setup
        self.button_rect = pygame.Rect(10, screen_height - BUTTON_HEIGHT - 10, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.font = pygame.font.Font(None, 36)
        self.show_inventory = False

        self.initialize_available_items()

    def initialize_available_items(self):
        index = 0
        for row in range(sprite_sheet.get_height() // SPRITE_HEIGHT):
            for col in range(sprite_sheet.get_width() // SPRITE_WIDTH):
                if index >= len(ITEM_NAMES):
                    break
                rect = pygame.Rect(
                    0, 0, SPRITE_WIDTH, SPRITE_HEIGHT
                )
                sprite = sprite_sheet.subsurface(rect)
                name = ITEM_NAMES[index]
                description = random_description()
                item = Item(name, description, sprite)
                self.available_items[name] = item
                index += 1

    def add_player_item(self, name):
        if name in self.available_items:
            self.player_items.append(self.available_items[name].__copy__())
            print(f"Added {name} to player's inventory.")
        else:
            print(f"Item {name} does not exist in available items.")

    def handle_event(self, event):
        # Handle button click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if self.button_rect.collidepoint(mouse_pos):
                self.show_inventory = not self.show_inventory
                return

            # Handle item clicks if inventory is open
            if self.show_inventory:
                self.handle_item_click(mouse_pos)

    def handle_item_click(self, mouse_pos):
        """Check if an item box is clicked and toggle selection."""
        start_x = (self.screen_width - (FRAME_SIZE * MAX_ITEMS)) // 2
        start_y = self.screen_height - FRAME_SIZE - 20

        for i in range(MAX_ITEMS):
            x = start_x + i * FRAME_SIZE
            y = start_y

            if i < len(self.player_items):
                item = self.player_items[i]
                if item.handle_click(mouse_pos, x, y, FRAME_SIZE):
                    # If clicked item is already selected, deselect it
                    if self.selected_item == item:
                        self.selected_item.is_selected = False
                        self.selected_item = None
                    else:
                        # Deselect previously selected item
                        if self.selected_item:
                            self.selected_item.is_selected = False

                        # Select the new item
                        self.selected_item = item
                        item.is_selected = True
                    break

    def draw_button(self, screen):
        # Change button color based on inventory state
        button_color = ACTIVE_COLOR if self.show_inventory else INACTIVE_COLOR

        # Draw the button background
        pygame.draw.rect(screen, button_color, self.button_rect)
        pygame.draw.rect(screen, BLACK, self.button_rect, 2)

        # Draw the button icon (centered within the button)
        scaled_icon = pygame.transform.scale(button_image, (BUTTON_HEIGHT - 10, BUTTON_HEIGHT - 10))
        icon_x = self.button_rect.x + (BUTTON_WIDTH - scaled_icon.get_width()) // 2
        icon_y = self.button_rect.y + (BUTTON_HEIGHT - scaled_icon.get_height()) // 2
        screen.blit(scaled_icon, (icon_x, icon_y))

    def display_inventory(self, screen):
        if not self.show_inventory:
            return

        # Calculate starting position for item frames
        start_x = (self.screen_width - (FRAME_SIZE * MAX_ITEMS)) // 2
        start_y = self.screen_height - FRAME_SIZE - 20

        for i in range(MAX_ITEMS):
            # Determine the position of the current frame
            x = start_x + i * FRAME_SIZE
            y = start_y

            # Draw either an item or an empty box
            if i < len(self.player_items):
                item = self.player_items[i]
                item.draw(screen, x, y, FRAME_SIZE)
            else:
                # Draw an empty box
                pygame.draw.rect(screen, BLACK, (x, y, FRAME_SIZE, FRAME_SIZE), 2)

    def draw(self, screen):
        # Draw the inventory button
        self.draw_button(screen)
        # Draw the inventory if toggled
        self.display_inventory(screen)