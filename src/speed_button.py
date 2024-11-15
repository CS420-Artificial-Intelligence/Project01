import pygame as pyg 

from button import Button

class speedButton:
    def __init__(self, rect):
        
        # left right padding = 10% of the width 
        left_padding = int(rect.width * 0.1)
        right_padding = int(rect.width * 0.1)
        
        # 3 buttons slowdown, pause, speedup are align centered, there are spaces between them with is equal 5% of the width
        # button width = min(20% of the width, 80 % of the height) 
        
        self.button_size = min(int(rect.width * 0.2), int(rect.height * 0.8))
        
        total_button_width = 3 * self.button_size + 2 * int(rect.width * 0.05) 

        total_button_position = ((rect.width - total_button_width) / 2, (rect.height - self.button_size) / 2)
        
        total_button_position = (total_button_position[0] + rect[0], total_button_position[1] + rect[1])
        self.slowdown_rect = pyg.Rect(total_button_position[0], total_button_position[1], self.button_size, self.button_size)
        
        total_button_position = (total_button_position[0] + self.button_size + int(rect.width * 0.05), total_button_position[1])
        self.pause_rect = pyg.Rect(total_button_position[0], total_button_position[1], self.button_size, self.button_size)
        
        total_button_position = (total_button_position[0] + self.button_size + int(rect.width * 0.05), total_button_position[1])
        self.speedup_rect = pyg.Rect(total_button_position[0], total_button_position[1], self.button_size, self.button_size)

        self.slowndown = Button("assets/speed_button/slowdown.jpg", 
                           "assets/speed_button/slowdown_hover.jpg",
                           self.slowdown_rect)
        self.pause = Button("assets/speed_button/pause.jpg",
                       "assets/speed_button/continue.jpg",
                       self.pause_rect)
        self.speedup = Button("assets/speed_button/speedup.jpg",
                         "assets/speed_button/speedup_hover.jpg",
                         self.speedup_rect)


        self.rect = rect

        return 
    def event_handler(self, event):
        if event.type == pyg.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            mouse_pos = (mouse_pos[0] - 900, mouse_pos[1])
            if self.slowdown_rect.collidepoint(mouse_pos):
                return 0 
            if self.pause_rect.collidepoint(mouse_pos):
                return 1
            if self.speedup_rect.collidepoint(mouse_pos):
                return 3
        if event.type == pyg.MOUSEMOTION:
            mouse_pos = event.pos
            mouse_pos = (mouse_pos[0] - 900, mouse_pos[1])
            self.slowndown.mousemove(mouse_pos)
            self.pause.mousemove(mouse_pos)
            self.speedup.mousemove(mouse_pos)
        return
    def draw(self, screen):
        screen.fill((125, 125, 255), self.rect)
        self.slowndown.draw(screen)
        self.pause.draw(screen)
        self.speedup.draw(screen)
        return 
