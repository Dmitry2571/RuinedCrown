#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:04:33 2026

@author: dmitrykhramov
"""
import pygame
from pygame.color import THECOLORS

class MenuButton:
    def __init__(self, x, y, width, height, text, frame_normal, frame_hover):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.frame_normal = frame_normal
        self.frame_hover = frame_hover
        self.font = pygame.font.SysFont('couriernew', 40)
        self.is_hovered = False
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
            return self.is_hovered
        if event.type == pygame.MOUSEBUTTONDOWN and self.is_hovered:
            return True  # Кнопка нажата
        return False
    
    def draw(self, screen):
        # Выбор рамки
        frame = self.frame_hover if self.is_hovered else self.frame_normal
        
        # Масштабирование рамки
        scaled_frame = pygame.transform.scale(frame, 
                                               (self.rect.width, self.rect.height))
        screen.blit(scaled_frame, self.rect)
        
        # Отрисовка текста по центру
        text_color = (255, 120, 80) if self.is_hovered else (220, 220, 220)
        text_surface = self.font.render(self.text, True, text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


class Menu:
    
    def __init__(self):
        self.button_width = 330
        self.button_height = 85
        self.start_x = (1280 - self.button_width) // 2  # Центрирование
        self.bg_image = pygame.image.load(
                        'menu_background.png').convert_alpha()
        self.bg_image.set_colorkey((250, 251, 251))
        self.bg_image = pygame.transform.smoothscale(
                        self.bg_image, (1280, 720))
        self.button_label = pygame.image.load(
                        'buttons_label.png').convert_alpha()
        self.frame_normal = self.button_label.subsurface(
                        75,200,720,540)
        self.frame_normal = pygame.transform.smoothscale(
                        self.frame_normal, (330, 85))
        self.frame_hover = self.button_label.subsurface(
                        875,200,720,540)
        self.frame_hover = pygame.transform.smoothscale(
                        self.frame_hover, (330, 85))
        
        self.buttons = [
    MenuButton(self.start_x, 260, self.button_width, self.button_height, 
               "START", self.frame_normal, self.frame_hover),
    MenuButton(self.start_x, 350, self.button_width, self.button_height, 
               "SAVE", self.frame_normal, self.frame_hover),
    MenuButton(self.start_x, 440, self.button_width, self.button_height, 
              "LOAD", self.frame_normal, self.frame_hover),
    MenuButton(self.start_x, 530, self.button_width, self.button_height, 
              "SETTINGS", self.frame_normal, self.frame_hover),
    MenuButton(self.start_x, 620, self.button_width, self.button_height, 
              "EXIT", self.frame_normal, self.frame_hover),
        ]
        
        
    def draw(self, screen):
        screen.blit(self.bg_image, (0, 0))
        for button in self.buttons:
            button.draw(screen)
            
    def update(self, event, screen):
        for button in self.buttons:
            if button.handle_event(event):
                # Обработка нажатия кнопки
                print(f"Clicked: {button.text}")
        self.draw(screen)