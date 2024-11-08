import pygame as pyg 

class statusLine: 
    def __init__(self, rect, inf):
        self.inf = inf
        self.rect = rect 

        self.elementRect = self.rect.copy() 
        self.elementRect.width = self.rect[2] // len(self.inf)
        
        self.fontpath = "assets/Noto_Sans_Mono/NotoSansMono-VariableFont_wdth,wght.ttf"
        self.title_size = 30
        self.title_font = pyg.font.Font(self.fontpath, self.title_size)
        
        self.value_font = self.title_font
        
        self.elements = [] 
        
        # self.inf[i] = ["title", "value"]

        for i in range(len(self.inf)):
            # blit title and value 
            surface = pyg.Surface((self.elementRect.width, self.elementRect.height)) 
            if i % 2 == 0: 
                surface.fill((125, 125, 255))
            else: 
                surface.fill((150, 150, 255))
            title_text = self.title_font.render(self.inf[i][0], True, (0, 0, 0))
            value_text = self.value_font.render(self.inf[i][1], True, (0, 0, 0))
            surface.blit(title_text, (30, self.elementRect.height // 2 - title_text.get_height() // 2))
            surface.blit(value_text, (self.elementRect.width - 30 - value_text.get_width(), self.elementRect.height // 2 - value_text.get_height() // 2))
            self.elements.append(surface)
            
    def update(self, id, val): 
        self.inf[id] = val
    
    def draw(self, screen):
        
        self.elecmentRect = self.rect.copy() 
        self.elementRect.width = self.rect.width // len(self.inf)
        
        for i in range(len(self.inf)):
            screen.blit(self.elements[i], (self.elementRect.x + i * self.elementRect.width, self.elementRect.y))
            #self.elementRect.x += self.elementRect.width

        return 
