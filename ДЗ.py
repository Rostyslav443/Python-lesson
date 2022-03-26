import pygame
from tkinter import *
from tkinter import messagebox
import time



pygame.init()

screen = pygame.display.set_mode((850, 200))

screen.fill(0, 0, 0)

pygame.display.set_caption('WARNING')
font = pygame.font.SysFont("Lucida Console", 20)
label = font.render("YOU DOWNLOADED VIRUS", 1,
 (12, 140, 0, 1))

screen.blit(label, (50, 50))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            time.sleep(0,2)
          
            pygame.init()

        screen = pygame.display.set_mode((850, 200))

        screen.fill(0, 0, 0)

         pygame.display.set_caption("IMPORTANT MESSAGE")
         font = pygame.font.SysFont("Lucida Console")
         label = font.render(Label)

         screen.blit(label, (50, 50))
         pygame.display.update()

