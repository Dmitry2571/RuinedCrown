#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:04:33 2026

@author: dmitrykhramov
"""
import pygame

class BaseElement:
    def __init__(self, x, y, width, height, text, frame_normal, font):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text = text
        self.frame_normal = frame_normal
        self.font = font
    
    def update_elem(self, x=None, y=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def get_x(self):
        return self.x
    
    
class MenuPanel(BaseElement):
        
    def draw(self, screen):
        # Масштабирование рамки
        scaled_frame = pygame.transform.scale(self.frame_normal, 
                                    (self.rect.width, self.rect.height))
        screen.blit(scaled_frame, self.rect)
        
        # Отрисовка текста по центру
        text_color = (220, 220, 220)
        text_surface = self.font.render(self.text, True, text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

class MenuButton(BaseElement):
    
    def __init__(self, x, y, width, height, text, frame_normal, frame_hover, font, label=None):
        super().__init__(x, y, width, height, text, frame_normal, font)
        self.frame_hover = frame_hover
        self.is_hovered = False
        self.label = label
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        return self.is_hovered
    
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
        
        
    def set_text(self, text):
        self.text = text


class Menu:
    
    def __init__(self, size):
        self.button_width = 330
        self.button_height = 85
        self.width = size[0]
        self.height = size[1]
        self.main_buttons = {
            'START': 'Start',
            'SAVE': 'Save',
            'LOAD': 'Load',
            'SETTINGS': 'Settings',
            'EXIT': 'Exit'
            }
        self.font = pygame.font.SysFont('couriernew', 40)
        self.start_x = (self.width - self.button_width) // 2  # Центрирование
        self.bg_image = pygame.image.load(
                        'menu_background.png').convert_alpha()
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
               "START", self.frame_normal, self.frame_hover, self.font),
    MenuButton(self.start_x, 350, self.button_width, self.button_height, 
               "SAVE", self.frame_normal, self.frame_hover, self.font),
    MenuButton(self.start_x, 440, self.button_width, self.button_height, 
              "LOAD", self.frame_normal, self.frame_hover, self.font),
    MenuButton(self.start_x, 530, self.button_width, self.button_height, 
              "SETTINGS", self.frame_normal, self.frame_hover, self.font),
    MenuButton(self.start_x, 620, self.button_width, self.button_height, 
              "EXIT", self.frame_normal, self.frame_hover, self.font)
        ]
        
    def draw(self, screen):
        screen.blit(self.bg_image, (0, 0))
        for button in self.buttons:
            button.draw(screen)
            
    def update(self, event, screen):
        for button in self.buttons:
            if button.handle_event(event):
                if event.type == pygame.MOUSEBUTTONDOWN \
                    and button.is_hovered:
                        return self.main_buttons[button.text]
        self.draw(screen)
        return 'Menu'
    
class SettingsMenu:
    
    def __init__(self, size, core):
        self.core = core
        #Сопоставление лейблов стрелок с методами core
        self.label_handlers = {
            'ReR': ('resolution', 1),   # Resolution Right
            'ReL': ('resolution', -1),  # Resolution Left
            'FrR': ('framerate', 1),    # Framerate Right
            'FrL': ('framerate', -1),   # Framerate Left
            }
        self.button_width = 330
        self.button_height = 85
        self.font = pygame.font.SysFont('couriernew', 40)
        self.width = size[0]
        self.height = size[1]
        self.start_x = (self.width - self.button_width) // 2
        self.main_buttons = {
            'BACK': 'Menu'
            }
        self.bg_image = pygame.image.load(
                        'menu_background2.png').convert_alpha()
        self.button_label = pygame.image.load(
                        'buttons_label.png').convert_alpha()
        self.arrow_right = pygame.image.load(
                        'arrows.png').convert_alpha()
        self.arrow_left = pygame.transform.flip(
            self.arrow_right, True, False)
        self.arrow_r_normal = self.arrow_right.subsurface(
            75,200,720,540)
        self.arrow_r_normal = pygame.transform.smoothscale(
                        self.arrow_r_normal, (100, 85))
        self.arrow_r_hover = self.arrow_right.subsurface(
            875,200,720,540)
        self.arrow_r_hover = pygame.transform.smoothscale(
                        self.arrow_r_hover, (100, 85))
        self.arrow_l_normal = self.arrow_left.subsurface(
            875,200,720,540)
        self.arrow_l_normal = pygame.transform.smoothscale(
                        self.arrow_l_normal, (100, 85))
        self.arrow_l_hover = self.arrow_left.subsurface(
            75,200,720,540)
        self.arrow_l_hover = pygame.transform.smoothscale(
                        self.arrow_l_hover, (100, 85))
        self.frame_normal = self.button_label.subsurface(
                        75,200,720,540)
        self.frame_normal = pygame.transform.smoothscale(
                        self.frame_normal, (330, 85))
        self.frame_hover = self.button_label.subsurface(
                        875,200,720,540)
        self.frame_hover = pygame.transform.smoothscale(
                        self.frame_hover, (330, 85))
        
        self.panels = [
    MenuPanel(self.start_x, 60, self.button_width, self.button_height,
            "RESOLUTION", self.frame_normal, self.font),
    MenuPanel(self.start_x, 240, self.button_width, self.button_height, 
            "FRAMERATE", self.frame_normal, self.font)
        ]
        self.buttons = [
    MenuButton(self.start_x + 330, 150, 100, 85, 
               "", self.arrow_r_normal, self.arrow_r_hover, self.font, label='ReR'),     
    MenuButton(self.start_x, 150, self.button_width, self.button_height, 
               "current resolution", self.frame_normal, self.frame_hover, self.font),
    MenuButton(self.start_x - 100, 150, 100, 85, 
               "", self.arrow_l_normal, self.arrow_l_hover, self.font, label='ReL'),
    MenuButton(self.start_x + 330, 330, 100, 85, 
               "", self.arrow_r_normal, self.arrow_r_hover, self.font, label='FrR'),     
    MenuButton(self.start_x, 330, self.button_width, self.button_height, 
              "current framerate", self.frame_normal, self.frame_hover, self.font),
    MenuButton(self.start_x - 100, 330, 100, 85, 
               "", self.arrow_l_normal, self.arrow_l_hover, self.font, label='FrL'),
    MenuButton(self.start_x, 530, self.button_width, self.button_height, 
              "APPLY", self.frame_normal, self.frame_hover, self.font),
    MenuButton(self.start_x, 620, self.button_width, self.button_height, 
              "BACK", self.frame_normal, self.frame_hover, self.font)
        ]
        # Сопоставление ключей с кнопками-значениями (для обновления текста)
        self.value_buttons = {
            'resolution': self.buttons[1],  # кнопка "current resolution"
            'framerate': self.buttons[4],   # кнопка "current framerate"
            }
        
        # Если core передан — сразу обновляем отображаемые значения
        if self.core:
            self._sync_display_values()
            
    def draw(self, screen):
        screen.blit(self.bg_image, (0, 0))
        for panel in self.panels:
            panel.draw(screen)
        for button in self.buttons:
            button.draw(screen)
            
    def update(self, event, screen):
        for button in self.buttons:
            if button.handle_event(event):
                if event.type == pygame.MOUSEBUTTONDOWN \
                    and button.is_hovered:
                        # === Обработка стрелок через core ===
                    if button.label and self.core:
                        setting_key, direction = self._parse_label(button.label)
                        if setting_key:
                            # Вызываем соответствующий метод core
                            method_name = f'change_{setting_key}'
                            if hasattr(self.core, method_name):
                                new_value = getattr(self.core, method_name)(direction)
                                # Обновляем отображение
                                if setting_key in self.value_buttons:
                                    self.value_buttons[setting_key].set_text(new_value)
                            return 'SettingsMenu'  # остаёмся в меню
                        
                        # === Обработка обычных кнопок ===
                    if button.text in self.main_buttons:
                        return self.main_buttons[button.text]
                    elif button.text == 'APPLY':
                        self.core.apply_changes()
                    
        self.draw(screen)
        return 'SettingsMenu'
        
    def _sync_display_values(self):
        """Обновляет текст кнопок-значений из данных core"""
        if not self.core:
            return
        self.value_buttons['resolution'].set_text(self.core.get_resolution_display())
        self.value_buttons['framerate'].set_text(self.core.get_framerate_display())
    
    def _parse_label(self, label):
        """Возвращает (setting_key, direction) или (None, None)"""
        if label in self.label_handlers:
            return self.label_handlers[label]
        return None, None
    
    def update_params(self, width, height, p_width, p_height):
        self.width = width
        self.height = height
        prev_start = self.start_x
        self.start_x = (self.width - self.button_width) // 2  # Центрирование
        betw = self.start_x - prev_start
        for button in self.buttons:
            pos = button.get_x()+betw
            button.update_elem(x=pos)
        for panel in self.panels:
            pos = panel.get_x()+betw
            panel.update_elem(x=pos)
        
    
    