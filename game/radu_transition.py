import pygame
import sys
from time import sleep

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Load the background image
background = pygame.image.load("background2.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


# Transition function
def transition(screen, background, width, height, fps=60):
    black_surface = pygame.Surface((width, height))
    black_surface.fill((0, 0, 0))

    # Transition step size
    step = 20

    # Black screen enters from the right
    for x in range(width, -1, -step):
        # screen.fill((0, 0, 0))  # Clear screen to black
        screen.blit(black_surface, (x, 0))  # Draw black surface moving in
        pygame.display.flip()
        clock.tick(fps)

    sleep(1)
    # Background enters from the left
    for x in range(0, width + 1, step):
        screen.fill((0, 0, 0))  # Clear screen to black
        screen.blit(background, (0, 0), (0, 0, x, height))  # Draw part of the background
        pygame.display.flip()
        clock.tick(fps)


# Main loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill screen with the initial background
        screen.blit(background, (0, 0))
        pygame.display.flip()

        # Trigger transition (for demonstration)
        pygame.time.delay(2000)  # Wait 2 seconds
        transition(screen, background, WIDTH, HEIGHT)
        pygame.time.delay(2000)  # Wait 2 seconds after transition

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
