import pygame

#Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


class HealthBar:
    def __init__(self, max_health, bar_width, bar_height):
        self.max_health = max_health
        self.bar_width = bar_width
        self.bar_height = bar_height
        self.font = pygame.font.SysFont(None, 30)
    def draw(self, screen, current_health, x, y):
        # Calculate the filled portion of the bar
        fill_width = int((current_health / self.max_health) * self.bar_width)

        # Draw the red background (total health)
        pygame.draw.rect(screen, RED, (x, y, self.bar_width, self.bar_height))

        # Draw the green foreground (current health)
        pygame.draw.rect(screen, GREEN, (x, y, fill_width, self.bar_height))

        # Render and draw the health text
        health_text = self.font.render(f"Health: {current_health}/{self.max_health}", True, WHITE)
        text_rect = health_text.get_rect(center=(x + self.bar_width // 2, y + self.bar_height // 2))
        screen.blit(health_text, text_rect)