import pygame as pyg 

class selectBox: 
    def __init__(self, rect):
        self.options = [["Level 1", 1]]
        self.current_option = 0
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
        self.levelvaluerect = pyg.Rect(120, 5, 170, 50)
        surface_levelvalue = pyg.Surface((self.levelvaluerect.width, self.levelvaluerect.height))
        surface_levelvalue.fill((125, 125, 255))
        levelvalue_text = self.value_font.render(self.options[self.current_option][0], True, (0, 0, 0))
        surface_levelvalue.blit(levelvalue_text, (10, self.levelvaluerect.height // 2 - levelvalue_text.get_height() // 2))
        self.levelValue = surface_levelvalue
        
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
    def addOption(self, option):
        self.options.append(option)
        return
    
    def event_handler(self, event):
        if self.is_open == False: 
            if event.type == pyg.MOUSEBUTTONDOWN and self.extend_on_rect.collidepoint(event.pos): 
                    self.is_open = True
        else: 
            if event.type == pyg.MOUSEBUTTONDOWN and not self.extend_off_rect.collidepoint(event.pos): 
                self.is_open = False 
        return

    def draw(self, screen):
        
        screen.blit(self.levelTitle, (self.leveltitlerect.x, self.leveltitlerect.y))
        screen.blit(self.levelValue, (self.levelvaluerect.x, self.levelvaluerect.y))
        if self.is_open == False: 
            screen.blit(self.extend_on, (self.extend_on_rect.x, self.extend_on_rect.y))
        else:
            screen.blit(self.extend_off, (self.extend_off_rect.x, self.extend_off_rect.y))
        return 
