import pygame
import sys
from main import Button

pygame.init()

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 600, 550

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Button test")

green_button = Button(0,0,100,50,"hi","click me",None,10,(255,255,255),(0,0,0))

def main_menu():
    run = True
    while run:
        screen.fill((13, 242, 5))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
        green_button.draw(screen)
        pygame.display.update()
        
        

main_menu()