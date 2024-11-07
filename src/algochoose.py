import pygame as pyg 

class algoChoose: 
    def __init__(self, rect):
        self.rect = rect
        self.is_open = False
        self.options = [["UCS", 1], ["DFS", 2], ["BFS", 3], ["A*", 4]]
        self.current_option = 0
        
        self.fontpath = "assets/Noto_Sans_Mono/NotoSansMono-VariableFont_wdth,wght.ttf"
        self.title_size = 30
        self.title_font = pyg.font.Font(self.fontpath, self.title_size)
        
        self.value_size = 25
        self.value_font = pyg.font.Font(self.fontpath, self.value_size)
        
        # algo field
        self.algotitlerect = pyg.Rect(0, 80, 300, 60)
        surface_algo = pyg.Surface((self.algotitlerect.width, self.algotitlerect.height)) 
        surface_algo.fill((255, 255, 255))
        algo_text = self.title_font.render("Algo: ", True, (0, 0, 0)) 
        surface_algo.blit(algo_text, (10, self.algotitlerect.height // 2 - algo_text.get_height() // 2))
        self.algoTitle = surface_algo
        
        # level value field
        self.levelvaluerect = pyg.Rect(120, 85, 170, 50)
        surface_levelvalue = pyg.Surface((self.levelvaluerect.width, self.levelvaluerect.height))
        surface_levelvalue.fill((125, 125, 255))
        levelvalue_text = self.value_font.render(self.options[self.current_option][0], True, (0, 0, 0))
        surface_levelvalue.blit(levelvalue_text, (10, self.levelvaluerect.height // 2 - levelvalue_text.get_height() // 2))
        self.algoValue = surface_levelvalue
        
        # extend_off button 
        self.extend_off_rect = pyg.Rect(250, 95, 30, 30)
        surface_extend_off = pyg.Surface((30, 30))
        surface_extend_off.fill((0, 0, 0))
        surface_extend_off.fill((255, 255, 255), (3, 3, 24, 24))
        extend_off_text = self.value_font.render("-", True, (0, 0, 0))
        surface_extend_off.blit(extend_off_text, (15 - extend_off_text.get_width() // 2, 15 - extend_off_text.get_height() // 2))
        self.extend_off = surface_extend_off

        # extend_on button
        self.extend_on_rect = pyg.Rect(250, 95, 30, 30)
        surface_extend_on = pyg.Surface((30, 30))
        surface_extend_on.fill((0, 0, 0))
        surface_extend_on.fill((255, 255, 255), (3, 3, 24, 24))
        extend_on_text = self.value_font.render("+", True, (0, 0, 0))
        surface_extend_on.blit(extend_on_text, (15 - extend_on_text.get_width() // 2, 15 - extend_on_text.get_height() // 2))
        self.extend_on = surface_extend_on

        return 

    def draw(self, screen):
        # fill with white 
        screen.fill((255, 255, 255), self.rect)
        
        screen.blit(self.algoTitle, (self.algotitlerect.x, self.algotitlerect.y))
        screen.blit(self.algoValue, (self.levelvaluerect.x, self.levelvaluerect.y))

        if self.is_open:
            screen.blit(self.extend_off, (self.extend_off_rect.x, self.extend_off_rect.y))
        else:
            screen.blit(self.extend_on, (self.extend_on_rect.x, self.extend_on_rect.y))
        return 
