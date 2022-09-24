#Importando a parte Image da biblioteca Pillow
from ast import main
from PIL import Image

#Imports necessários do OpenCV
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from pathlib import Path
import argparse

#Imports necessários do Pygame
import pygame, sys
from PIL import Image
pygame.init()

def displayImage(screen, px, topleft, prior): 
    x, y = topleft
    #Obtem a posição do cursor do Mouse
    width =  pygame.mouse.get_pos()[0] - topleft[0]
    height = pygame.mouse.get_pos()[1] - topleft[1]
    #Garante que a largura da região selecionada seja positiva
    if width < 0:
        x += width
        width = abs(width)
    #Garante que a altura da região selecionada seja positiva
    if height < 0:
        y += height
        height = abs(height)

    #Elimina selecões redundantes (Quando o cursor do mouse está parado)
    current = x, y, width, height
    if not (width and height):
        return current
    if current == prior:
        return current

    #Exibi o retângulo para seleção da área
    screen.blit(px, px.get_rect())
    im = pygame.Surface((width, height))
    im.fill((128, 128, 128))
    pygame.draw.rect(im, (32, 32, 32), im.get_rect(), 1)
    im.set_alpha(128)
    screen.blit(im, (x, y))
    pygame.display.flip()

    #Retorna as dimensões da região selecionada
    return (x, y, width, height)

def setup(path):
    px = pygame.image.load(path)
    screen = pygame.display.set_mode( px.get_rect()[2:] )
    screen.blit(px, px.get_rect())
    pygame.display.flip()
    return screen, px

def mainLoop(screen, px):
    topleft = bottomright = prior = None
    n=0
    while n!=1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP: 
                if not topleft:
                    topleft = event.pos
                else:
                    bottomright = event.pos
                    n=1
        if topleft:
            prior = displayImage(screen, px, topleft, prior)
    return ( topleft + bottomright )