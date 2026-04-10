#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 09:26:17 2026

@author: dmitrykhramov
"""
#Ruined Ccrown
# === Блок импортов===
import os
import pygame
from GUI.GUIMenu import Menu
from core.core import Core
# === Конец блока ===
# === Блок констант===
VERSION = '0.0.1a'
COLOR_BACKGROUND = (0, 0, 0)
EXIT_DELAY_MS = 100
# === Конец блока ===

def main():
    """Точка входа в приложение."""
    pygame.init()
    #Инициализация ядра
    core = Core()
    FPS = core.get_FPS()
    clock = pygame.time.Clock()
    
    # Настройка окна
    width, height = core.get_display_params()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(f"Ruined Crown v{VERSION}")
    core.init_gui(screen)
    
    # Инициализация главного меню
    menu = Menu((width, height))
    menu.draw(screen)
    
    #Состояния приложения
    status = 'Menu'
    running = True
    
    # === Игровой цикл ===
    while running:
        
        # Обработка событий
        for event in pygame.event.get():
            
            # Глобальные события
            if event.type == pygame.QUIT or status == 'Exit':
                running = False
            
            # Маршрутизация по состоянию
            if status == 'Menu':
                status = menu.update(event, screen)
                
            elif status == 'Settings':
                screen.fill(COLOR_BACKGROUND)
                status = core.settings(screen)
                
            elif status == 'SettingsMenu':
                FPS = core.get_FPS()
                status = core.update_settings(event, screen)

        # Отрисовка и синхронизация
        pygame.display.flip()
        clock.tick(FPS)
    # === Конец блока ===
    
    # Обработка выхода из любого состояния
    pygame.time.wait(EXIT_DELAY_MS)
    pygame.display.quit()
    pygame.quit()
    os._exit(0)

if __name__ == "__main__":
    main()