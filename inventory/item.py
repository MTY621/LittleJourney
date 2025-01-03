import pygame

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
ACTIVE_COLOR = (100, 150, 200)
INACTIVE_COLOR = GRAY
SELECTED_COLOR = (255, 255, 0)
BUTTON_COLOR = (0, 200, 0)
BUTTON_TEXT_COLOR = WHITE

class Item:
    def __init__(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image
        self.is_selected = False
    def __copy__(self):
        return Item(self.name, self.description, self.image.copy())

    def draw(self, screen, x, y, frame_size):
        """Draw the item at a given position."""
        # Draw selection outline if selected
        if self.is_selected:
            pygame.draw.rect(screen, SELECTED_COLOR, (x, y, frame_size, frame_size), 2)
            self.draw_item_buttons(screen, x, y - 50)
        else:
            pygame.draw.rect(screen, BLACK, (x, y, frame_size, frame_size), 2)

        # Draw the item image inside the box
        scaled_image = pygame.transform.scale(self.image, (frame_size - 10, frame_size - 10))
        screen.blit(scaled_image, (x + 5, y + 5))

    def draw_item_buttons(self, screen, x, y):
        """Draw 'Use' and 'Drop' buttons above the selected item."""
        # Use Button
        use_button_rect = pygame.Rect(x, y, FRAME_SIZE, 20)
        pygame.draw.rect(screen, BUTTON_COLOR, use_button_rect)
        pygame.draw.rect(screen, BLACK, use_button_rect, 2)
        self.draw_button_text(screen, "Use", use_button_rect)

        # Drop Button
        drop_button_rect = pygame.Rect(x, y + 25, FRAME_SIZE, 20)
        pygame.draw.rect(screen, BUTTON_COLOR, drop_button_rect)
        pygame.draw.rect(screen, BLACK, drop_button_rect, 2)
        self.draw_button_text(screen, "Drop", drop_button_rect)

    def draw_button_text(self, screen, text, rect):
        """Draw text centered inside a button."""
        font = pygame.font.SysFont(None, 20)
        text_surface = font.render(text, True, BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

    def handle_click(self, mouse_pos, x, y, frame_size, inventory):
        """Handle click to toggle selection."""
        if x <= mouse_pos[0] <= x + frame_size and y <= mouse_pos[1] <= y + frame_size:
            if inventory.selected_item:
                inventory.selected_item.is_selected = False
            inventory.selected_item = self
            self.is_selected = True
        if (self.is_selected and y - 25 <= mouse_pos[1] <= y - 5 and x <= mouse_pos[0] <= x + frame_size):
            print(f"Using {self.name}")
            for i in range(len(inventory.player_items)):
                if inventory.player_items[i] == self:
                    inventory.player_items[i] = None
                    break