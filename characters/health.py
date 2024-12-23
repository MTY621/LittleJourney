import pygame

#Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


class HealthBar:
    def __init__(self, max_health, current_health, bar_width, bar_height, bar_x, bar_y):
        self.max_health = max_health
        self.current_health = current_health
        self.bar_width = bar_width
        self.bar_height = bar_height
        self.bar_x = bar_x
        self.bar_y = bar_y
        self.font = pygame.font.SysFont(None, 30)
    def update_pos(self, x, y):
        self.bar_x = x
        self.bar_y = y
    def draw(self, screen):
        # Calculate the filled portion of the bar
        fill_width = int((self.current_health / self.max_health) * self.bar_width)

        # Draw the red background (total health)
        pygame.draw.rect(screen, RED, (self.bar_x, self.bar_y, self.bar_width, self.bar_height))

        # Draw the green foreground (current health)
        pygame.draw.rect(screen, GREEN, (self.bar_x, self.bar_y, fill_width, self.bar_height))

        # Render and draw the health text
        health_text = self.font.render(f"Health: {self.current_health}/{self.max_health}", True, WHITE)
        text_rect = health_text.get_rect(center=(self.bar_x + self.bar_width // 2, self.bar_y + self.bar_height // 2))
        screen.blit(health_text, text_rect)

    def update_health(self, amount):
        self.current_health = max(0, min(self.max_health, self.current_health + amount))