import pygame

pygame.init()

font = pygame.font.Font(None, 32)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720

menu_background = pygame.image.load('assets/menu_background.webp')
menu_background = pygame.transform.scale(menu_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
menu_background_rect = menu_background.get_rect()
menu_background_rect = menu_background_rect.move((0, 0))

class Button:
    def __init__(self, x, y, width, height, color, selected_color, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.selected_color = selected_color
        self.text = text
        self.selected = False

    def draw(self, screen):
        # pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        if self.selected:
            pygame.draw.rect(screen, self.selected_color, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        if self.text is not None:
            text = font.render(self.text, True, BLACK)
            screen.blit(text, (self.x + self.width // 2 - text.get_width() // 2, self.y + self.height // 2 - text.get_height() // 2))

    def is_clicked(self, pos):
        x, y = pos
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height
    def is_selected(self):
        return self.selected
    def select(self):
        self.selected = True
    def deselect(self):
        self.selected = False

class ButtonContainer:
    def __init__(self):
        self.buttons = []
        self.selected = 0

    def select(self, index):
        self.buttons[self.selected].deselect()
        self.selected = index
        self.buttons[self.selected].select()

    def pack(self, button):
        self.buttons.append(button)
        self.select(0)
    def select_next(self):
        self.buttons[self.selected].deselect()
        self.selected = (self.selected + 1) % len(self.buttons)
        self.buttons[self.selected].select()
    def select_prev(self):
        self.buttons[self.selected].deselect()
        self.selected = (self.selected - 1) % len(self.buttons)
        self.buttons[self.selected].select()
    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen)



def run_menu(screen):
    top_margin = 100
    left_margin = 100
    number_of_maps = 10
    map_button = []
    button_container = ButtonContainer()
    for i in range(number_of_maps):
        map_button.append(Button(left_margin, top_margin + i * 50, 200, 40, BLUE, GREEN, f'Map {i + 1}'))
        button_container.pack(map_button[-1])
    quit_button = Button(left_margin, top_margin + number_of_maps * 50, 200, 40, BLUE, GREEN, 'Quit')
    button_container.pack(quit_button)

    print(SCREEN_WIDTH / menu_background.get_width(), SCREEN_HEIGHT / menu_background.get_height())

    while True:
        screen.fill(WHITE)
        screen.blit(menu_background, (0, 0))
        
        # Draw Buttons
        button_container.draw(screen)

        # Event Handling for Menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    button_container.select_next()
                if event.key == pygame.K_UP:
                    button_container.select_prev()
                if event.key == pygame.K_RETURN:
                    if button_container.selected == len(map_button):
                        print('Quitting')
                        return -1
                    if button_container.selected < len(map_button):
                        print(f'Starting Map {button_container.selected + 1}')
                        return button_container.selected
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.is_clicked(event.pos):
                    print('Quitting')
                    return -1
                for i, button in enumerate(map_button):
                    if button.is_clicked(event.pos):
                        print(f'Starting Map {i + 1}')
                        return i


        # Update the display
        pygame.display.flip()