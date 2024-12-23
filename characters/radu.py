import pygame
from health import HealthBar

# Initialize Pygame
pygame.init()

# Initial display setup with RESIZABLE flag
screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Scrolling Background Example")

# Load the sprite sheet
sprite_sheet = pygame.image.load('character_images/main_character/Human/default.png').convert_alpha()

# Load and scale the background image
background = pygame.image.load('../background/castle/1_garden.png').convert()
background_height = screen_height
background_width = int(background.get_width() * (screen_height / background.get_height()))
background = pygame.transform.scale(background, (background_width, background_height))

# Frame dimensions
frame_width = 40
frame_height = 40

# Extract a specific frame (e.g., top-left frame)
frame = sprite_sheet.subsurface(pygame.Rect(0, 0, frame_width, frame_height))

# Scale the frame to make it larger (e.g., 8x size)
scale_factor = 8
scaled_width = frame_width * scale_factor
scaled_height = frame_height * scale_factor
scaled_frame = pygame.transform.scale(frame, (scaled_width, scaled_height))

# Character's relative position as a percentage of the screen
char_x_percent = 0.5  # Middle of the screen horizontally (50%)
char_y_percent = 0.75  # Near the bottom of the screen vertically (75%)

# Background scrolling variables
scroll_x = 0
scroll_speed = 2

# Fullscreen toggle state
is_fullscreen = False

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.VIDEORESIZE:
            # Adjust window size and rescale elements
            old_screen_width, old_screen_height = screen_width, screen_height
            screen_width, screen_height = event.w, event.h
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

            # Rescale the background image
            background_height = screen_height
            background_width = int(background.get_width() * (screen_height / background.get_height()))
            background = pygame.transform.scale(background, (background_width, background_height))

            # Adjust the scroll position proportionally
            scroll_x = scroll_x * (background_width / old_screen_width)

    # Update character's position based on screen dimensions
    x = int(screen_width * char_x_percent - scaled_width / 2)
    y = int(screen_height * char_y_percent - scaled_height / 2)

    # Character movement (affects the background scroll)
    scroll_x -= scroll_speed

    # Adjust scroll position to keep it looping
    scroll_x = scroll_x % background_width

    # Draw the scaled background twice to create a seamless loop
    screen.blit(background, (scroll_x, 0))
    screen.blit(background, (scroll_x - background_width, 0))

    # Draw the scaled sprite frame
    screen.blit(scaled_frame, (x, y))

    # Update and draw the health bar
    bar = HealthBar(100, 75, 200, 20, x + 40, y + 10)
    bar.update_health(-1)  # Simulating health decrease for testing
    bar.draw(screen)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()