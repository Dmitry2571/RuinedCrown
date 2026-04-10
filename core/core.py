#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:58:30 2026

@author: dmitrykhramov
"""
import pygame
from GUI.GUIMenu import SettingsMenu

class Core:
    
    def __init__(self):
        self.FPS = 60
        self.width = 1280
        self.height = 720
        self.p_width = 1280
        self.p_height = 720
        
        # Настройки с индексами текущего выбора
        self.resolutions = {
            (640,480): '640x480',
            (1280,720): '1280x720',
            (1920,1080): '1920x1080'
            }
        self._resolution_keys = list(self.resolutions.keys())
        self._resolution_idx = 1  # по умолчанию 1280x720
        
        self.framerate = [30, 60, 120]
        self._framerate_idx = 1 
        
    def init_gui(self, screen):
        self.menu = SettingsMenu((self.width, self.height), core=self)
        self.screen = screen
        
    def settings(self, screen):
        self.menu.draw(screen)
        return 'SettingsMenu'
    
    def update_settings(self, event, screen):
        return self.menu.update(event,screen)
        
    def get_FPS(self):
        return self.FPS
    
    def get_display_params(self):
        return self.width, self.height
    
    def get_resolution_display(self):
        """Возвращает строку для отображения текущего разрешения"""
        key = self._resolution_keys[self._resolution_idx]
        return self.resolutions[key]
    
    def get_framerate_display(self):
        """Возвращает строку для отображения текущего фреймрейта"""
        return str(self.framerate[self._framerate_idx])
    
    def change_resolution(self, direction: int) -> str:
        """
        Меняет разрешение: direction=1 (вправо/след), -1 (влево/пред)
        Возвращает новое значение для отображения
        """
        self._resolution_idx = (self._resolution_idx + direction) % len(self._resolution_keys)
        return self.get_resolution_display()
    
    def change_framerate(self, direction: int) -> str:
        """Меняет фреймрейт, возвращает новое значение для отображения"""
        self._framerate_idx = (self._framerate_idx + direction) % len(self.framerate)
        
        return self.get_framerate_display()
    
    def apply_changes(self):
       self.width, self.height = self._resolution_keys[self._resolution_idx]
       self.FPS = self.framerate[self._framerate_idx]
       self.screen = pygame.display.set_mode((self.width, self.height))
       self.menu.update_params(self.width, self.height,
                               self.p_width, self.p_height)
       
       
    