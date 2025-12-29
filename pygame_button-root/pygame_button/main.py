import pygame
import threading

class Button:
    def __init__(self, x:int | float=0, y:int|float=0, width:int|float=80, height:int|float=40,text:str|bool=False, hover_text:str|bool=False, font:str|None =None, text_size:int = 20, text_color:tuple=(255,255,255),color:tuple=(0,0,0), hover_color:tuple=(50,50,50), image:str='',hover_image:str='', on_click=None, sound:str|bool=False) -> None:
        self.x =x
        self.y = y
        self.width = width
        self.height = height
        if image != '':
            self.image = pygame.transform.scale(pygame.image.load(image),(self.width, self.height))
            self.rect = self.image.get_rect()
            if hover_image != '':
                self.hover_image = pygame.transform.scale(pygame.image.load(hover_image),(self.width, self.height))
            else:
                self.hover_image = self.image
        else:
            self.image = False
            self.hover_image = False
            self.rect = pygame.Rect(x,y,width,height)
            
        self.font = font
        self.color = color
        self.text_color = text_color
        self.text=text
        self.hover_text = hover_text
        self.text_size = text_size
        self.hover_color = hover_color
        if sound:
            self.sound = pygame.mixer.Sound(sound)
        self.on_click = on_click
        self.is_hovered = False

        
        

    def draw(self, screen:pygame.Surface):
        if self.is_hovered:
            if self.hover_image != '':
                screen.blit(self.hover_image, self.rect.topleft) # type: ignore
            else:
                current_image = pygame.Surface((self.width,self.height))
                current_image.fill(self.hover_color)
                screen.blit(current_image, self.rect.topleft)

            if self.hover_text:
                font = pygame.font.Font(self.font, self.text_size)
                text_surface = font.render(self.hover_text, True, self.text_color) # type: ignore
                text_rect = text_surface.get_rect(center=self.rect.center)
                screen.blit(text_surface, text_rect)

            elif self.text:
                font = pygame.font.Font(self.font, self.text_size)
                text_surface = font.render(self.text, True, self.text_color) # type: ignore
                text_rect = text_surface.get_rect(center=self.rect.center)
                screen.blit(text_surface, text_rect)

        else:
            if self.image:
                screen.blit(self.image, self.rect.topleft) # type: ignore
            else:
                current_image = pygame.Surface((self.width,self.height))
                current_image.fill(self.color)
                screen.blit(current_image, self.rect.topleft)
            if self.text:
                font = pygame.font.Font(self.font, self.text_size)
                text_surface = font.render(self.text, True, self.text_color) # type: ignore
                text_rect = text_surface.get_rect(center=self.rect.center)
                screen.blit(text_surface, text_rect)
        

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))



        
