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
        else:
            pygame.draw.rect(screen, BLACK, (x, y, frame_size, frame_size), 2)

        # Draw the item image inside the box
        scaled_image = pygame.transform.scale(self.image, (frame_size - 10, frame_size - 10))
        screen.blit(scaled_image, (x + 5, y + 5))

    def handle_click(self, mouse_pos, x, y, frame_size):
        """Handle click to toggle selection."""
        if x <= mouse_pos[0] <= x + frame_size and y <= mouse_pos[1] <= y + frame_size:
            return True
        return False