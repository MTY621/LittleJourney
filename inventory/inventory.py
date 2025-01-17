import pygame
from inventory.item import Item
import json


# Constants
BUTTON_WIDTH = 75
BUTTON_HEIGHT = 75
FRAME_SIZE = 64
MAX_ITEMS = 8

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
ACTIVE_COLOR = (100, 150, 200)
INACTIVE_COLOR = GRAY
BUTTON_COLOR = (0, 200, 0)
BUTTON_TEXT_COLOR = WHITE


# Load the sprite sheet
button_image = pygame.image.load("inventory/backpack.png")

# Define the dimensions of each sprite in the sheet
SPRITE_WIDTH = 16
SPRITE_HEIGHT = 16


class Inventory:
    def __init__(self, screen_width, screen_height, player):
        self.available_items = {}
        self.player_items = [None] * MAX_ITEMS
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.selected_item = None
        self.player = player

        # Inventory button setup
        self.button_rect = pygame.Rect(10, screen_height - BUTTON_HEIGHT - 10, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.font = pygame.font.Font(None, 36)
        self.show_inventory = False

        self.initialize_available_items()

    def initialize_available_items(self):
        try:
            # Open and parse the JSON file
            with open("items/available_items.json", "r") as file:
                items_data = json.load(file)

            for item_data in items_data:
                # Extract item properties from JSON
                name = item_data.get("name")
                file_name = item_data.get("file_name")
                item_type = item_data.get("item_type")
                price = item_data.get("price")
                is_edible = item_data.get("is_edible")
                stats = item_data.get("stats")

                if not file_name or not name:
                    continue  # Skip invalid entries

                # Load the sprite from the file
                sprite_path = f"items/{file_name}.png"


                # Create the Item object
                item = Item(name, file_name, item_type ,price, is_edible, stats)

                # Add the item to the available items dictionary
                self.available_items[name] = item

        except FileNotFoundError:
            print("Error: 'available_items.json' file not found.")
        except json.JSONDecodeError:
            print("Error: Failed to parse 'available_items.json'.")

    def add_item(self, name):

        if name in self.available_items:
            # Check if the inventory is full
            if self.player_items[MAX_ITEMS - 1] is not None:
                print("Inventory is full.")
                return 0

            # If the new item is a sword or shield, check if the player already has one
            if self.available_items[name].item_type == "sword":
                for i in range(len(self.player_items)):
                    if self.player_items[i] is not None and self.player_items[i].item_type == "sword":
                        self.player.atk += (self.available_items[name].stats[0] - self.player_items[i].stats[0])
                        self.player_items[i] = self.available_items[name].__copy__()
                        print(f"Added {name} to player's inventory.")
                        return 1
            if self.available_items[name].item_type == "shield":
                for i in range(len(self.player_items)):
                    if self.player_items[i] is not None and self.player_items[i].item_type == "shield":
                        self.player.defense += (self.available_items[name].stats[0] - self.player_items[i].stats[0])
                        self.player_items[i] = self.available_items[name].__copy__()
                        print(f"Added {name} to player's inventory.")
                        return 1

            # Add the item to the first available slot
            ok = 0
            for i in range(len(self.player_items)):
                if self.player_items[i] is None:
                    self.player_items[i] = self.available_items[name].__copy__()
                    print(f"Added {name} to player's inventory.")
                    ok = 1
                    break
            if self.available_items[name].item_type == "sword":
                self.player.atk += self.available_items[name].stats[0]
            elif self.available_items[name].item_type == "shield":
                self.player.defense += self.available_items[name].stats[0]
            return ok
        else:
            print(f"Item {name} does not exist in available items.")
            return 0

    def remove_item(self, name):
        for i in range(MAX_ITEMS):
            if self.player_items[i] and self.player_items[i].name == name:
                if self.player_items[i].item_type == "sword":
                    self.player.atk -= self.player_items[i].stats[0]
                elif self.player_items[i].item_type == "shield":
                    self.player.defense -= self.player_items[i].stats[0]
                self.player_items[i] = None
                print(f"Removed {name} from player's inventory.")
                return
    def has_item(self, name):
        for i in range(MAX_ITEMS):
            if self.player_items[i] and self.player_items[i].name == name:
                return True
        return False

    def handle_event(self, event):
        # Handle button click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if self.button_rect.collidepoint(mouse_pos):
                if self.show_inventory:
                    if self.selected_item:
                        self.selected_item.is_selected = False
                        self.selected_item = None
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
                if item:
                    item.handle_click(mouse_pos, x, y, FRAME_SIZE, self.player)

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

    def draw_button_text(self, screen, text, rect):
        """Draw text centered inside a button."""
        font = pygame.font.SysFont(None, 20)
        text_surface = font.render(text, True, BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

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
            if self.player_items[i]:
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