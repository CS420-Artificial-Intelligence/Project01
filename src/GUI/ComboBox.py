import pygame


class ComboBox:
    def __init__(self, x, y, width, height, font, options):
        self.rect = pygame.Rect(x,y,width,height)
        self.options = options
        self.font = font
        self.selected_index = 0
        self.is_extended = False

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

        selected_text = self.font.render(self.options[self.selected_index], True, (0, 0, 0))
        screen.blit(selected_text, (self.rect.x + 5, self.rect.y + 5))

        if self.is_extended:
            for i, option in enumerate(self.options):
                option_rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height, self.rect.width, self.rect.height)
                pygame.draw.rect(screen, (255, 255, 255), option_rect)
                pygame.draw.rect(screen, (0, 0, 0), option_rect, 2)

                option_text = self.font.render(option, True, (0, 0, 0))
                screen.blit(option_text, (option_rect.x + 5, option_rect.y + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                # Toggle expanded state when clicking the main box
                self.is_extended = not self.is_extended
            elif self.is_extended:
                # Check if any option is clicked
                for i in range(len(self.options)):
                    option_rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height, self.rect.width,
                                              self.rect.height)
                    if option_rect.collidepoint(event.pos):
                        self.selected_index = i
                        self.is_extended = False
                        break
            else:
                self.is_extended = False  # Collapse if clicked outside

    def get_selected(self):
        return self.options[self.selected_index]