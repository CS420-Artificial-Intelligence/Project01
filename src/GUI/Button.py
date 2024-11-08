import pygame


class Button:
    def __init__(self, x, y, width, height, text, font, bg_color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color
        self.hover_color = (min(bg_color[0] + 30, 255), min(bg_color[1] + 30, 255), min(bg_color[2] + 30, 255))  # Lighter on hover
        self.is_hovered = False

    def draw(self, screen):
        # Draw background with hover effect
        color = self.hover_color if self.is_hovered else self.bg_color
        pygame.draw.rect(screen, color, self.rect)

        # Draw button border
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

        # Render and center the text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            # Check if the mouse is hovering over the button
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if button is clicked
            if self.is_hovered:
                return True  # Button clicked
        return False  # Button not clicked
