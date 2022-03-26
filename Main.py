import pygame
from tkinter import *
from tkinter import messagebox

With = 850
High = 200
Font1 = 'Lusida Console', 20
Label1 = 'YOU DOWNLOAD VIRUS', 1, (12, 140, 0)
screen1 = 50, 50


pygame.init()

screen = pygame.display.set_mode((With, High))

screen.fill(0, 0, 0)

pygame.display.set_caption("WARNING!!!")
font = pygame.font.SysFont(Font1)
label = font.render(Label)

screen.blit(label, (screen1))
pygame.display.update()

while True:
    pass