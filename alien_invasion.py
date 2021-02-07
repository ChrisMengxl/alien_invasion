# -*- coding: utf-8 -*-
# @Author: ChrisMengxl
# @Date:   2021-02-08 00:35:38
# @Last Modified by:   ChrisMengxl
# @Last Modified time: 2021-02-08 01:35:23

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen)

    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)


run_game()
