import pygame as pyg 

class Option:
    def __init__(self, text, x, y, width, height, on_click=None):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text_font = pyg.font.Font("assets/Noto_Sans_Mono/NotoSansMono-VariableFont_wdth,wght.ttf", 25)
        self.on_click = on_click
        self.on_hover = False
        self.selected = False
        return
    def select(self):
        self.selected = True
    def deselect(self):
        self.selected = False
    def draw(self, screen):
        # screen.fill((255, 255, 255), (self.x, self.y, self.width, self.height))
        if self.on_hover:
            pyg.draw.rect(screen, (200, 200, 200), (self.x, self.y, self.width, self.height))
        else:
            pyg.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
        if self.selected:
            pyg.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height), 2)
        text = self.text_font.render(self.text, True, (0, 0, 0))
        screen.blit(text, (self.x + self.width // 2 - text.get_width() // 2, self.y + self.height // 2 - text.get_height() // 2))
    def event_handler(self, event):
        if event.type == pyg.MOUSEMOTION:
            mouse_pos = event.pos
            mouse_pos = (mouse_pos[0] - 900, mouse_pos[1])
            if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height:
                self.on_hover = True
            else:
                self.on_hover = False
        if event.type == pyg.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            mouse_pos = (mouse_pos[0] - 900, mouse_pos[1])
            if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height:
                if self.on_click is not None:
                    self.on_click()
        return
class selectBox: 

    def __init__(self, rect):
        self.options = []
        self.option_buttons = []
        # self.addOption(["Level 1", 1])
        # self.addOption(["Level 2", 2])
        # self.addOption(["Level 3", 3])
        for i in range(10):
            self.addOption([f"Level {i + 1}", i + 1])
        self.current_option = 0
        self.option_buttons[0].select()
        self.rect = rect
        self.is_open = False
        
        
        self.fontpath = "assets/Noto_Sans_Mono/NotoSansMono-VariableFont_wdth,wght.ttf"
        self.title_size = 30
        self.title_font = pyg.font.Font(self.fontpath, self.title_size)
        
        self.value_size = 25
        self.value_font = pyg.font.Font(self.fontpath, self.value_size)
        
        # level field
        self.leveltitlerect = pyg.Rect(0, 0, 300, 60)
        surface_level = pyg.Surface((self.leveltitlerect.width, self.leveltitlerect.height)) 
        surface_level.fill((255, 255, 255))
        level_text = self.title_font.render("Level: ", True, (0, 0, 0)) 
        surface_level.blit(level_text, (10, self.leveltitlerect.height // 2 - level_text.get_height() // 2))
        self.levelTitle = surface_level
        
        # level value field
        self.update_level_value()
        
        # extend_off button 
        self.extend_off_rect = pyg.Rect(250, 15, 30, 30)
        surface_extend_off = pyg.Surface((30, 30))
        surface_extend_off.fill((0, 0, 0))
        surface_extend_off.fill((255, 255, 255), (3, 3, 24, 24))
        extend_off_text = self.value_font.render("-", True, (0, 0, 0))
        surface_extend_off.blit(extend_off_text, (15 - extend_off_text.get_width() // 2, 15 - extend_off_text.get_height() // 2))
        self.extend_off = surface_extend_off

        # extend_on button
        self.extend_on_rect = pyg.Rect(250, 15, 30, 30)
        surface_extend_on = pyg.Surface((30, 30))
        surface_extend_on.fill((0, 0, 0))
        surface_extend_on.fill((255, 255, 255), (3, 3, 24, 24))
        extend_on_text = self.value_font.render("+", True, (0, 0, 0))
        surface_extend_on.blit(extend_on_text, (15 - extend_on_text.get_width() // 2, 15 - extend_on_text.get_height() // 2))
        self.extend_on = surface_extend_on

        return

    def update_level_value(self):
        self.levelvaluerect = pyg.Rect(120, 5, 170, 50)
        surface_levelvalue = pyg.Surface((self.levelvaluerect.width, self.levelvaluerect.height))
        surface_levelvalue.fill((125, 125, 255))
        levelvalue_text = self.value_font.render(self.options[self.current_option][0], True, (0, 0, 0))
        surface_levelvalue.blit(levelvalue_text, (10, self.levelvaluerect.height // 2 - levelvalue_text.get_height() // 2))
        self.levelValue = surface_levelvalue

    def addOption(self, option):
        self.options.append(option)
        self.option_buttons.append(Option(option[0], 0, 0, 300, 50, lambda: self.changeOption(option[1])))
        return
    def changeOption(self, index):
        print(f'Change option to {index}')
        self.option_buttons[self.current_option].deselect()
        self.current_option = index - 1
        self.option_buttons[self.current_option].select()
        self.update_level_value()
    
    def event_handler(self, event):
        if event.type == pyg.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            mouse_pos = (mouse_pos[0] - 900, mouse_pos[1])
            if self.extend_off_rect.collidepoint(mouse_pos):
                self.is_open = not self.is_open
                return
        if self.is_open == True:
            for i, option in enumerate(self.option_buttons):
                option.y = self.rect.y + self.rect.height + i * 50
                option.event_handler(event)
        return

    def draw(self, screen):
        
        screen.blit(self.levelTitle, (self.leveltitlerect.x, self.leveltitlerect.y))
        screen.blit(self.levelValue, (self.levelvaluerect.x, self.levelvaluerect.y))
        if self.is_open == False: 
            screen.blit(self.extend_on, (self.extend_on_rect.x, self.extend_on_rect.y))
        else:
            screen.blit(self.extend_off, (self.extend_off_rect.x, self.extend_off_rect.y))
            for i, option in enumerate(self.option_buttons):
                option.y = self.rect.y + self.rect.height + i * 50
                option.draw(screen)
        return 
