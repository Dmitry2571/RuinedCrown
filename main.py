#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 09:26:17 2026

@author: dmitrykhramov
"""
#ruined crown
import pygame
from pygame.color import THECOLORS
import os
from GUI.GUIMenu import Menu
version = '0.0.0a'

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Ruined Crown")
    
    clock = pygame.time.Clock()
    FPS = 60
    screen.fill(THECOLORS['black'])
    menu = Menu()
    menu.draw(screen)
    status = 'Menu'
    
    running = True
    while running:
        pygame.event.pump()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if status == 'Menu':
                menu.update(event, screen)
        
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.time.wait(100)
    pygame.display.quit()
    pygame.quit()
    os._exit(0)

if __name__ == "__main__":
    main()