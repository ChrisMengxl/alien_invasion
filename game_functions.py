# -*- coding: utf-8 -*-
# @Author: ChrisMengxl
# @Date:   2021-02-08 01:25:41
# @Last Modified by:   ChrisMengxl
# @Last Modified time: 2021-02-08 01:35:48
import sys
import pygame

def check_events():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):

    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()
