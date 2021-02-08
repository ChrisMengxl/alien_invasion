# -*- coding: utf-8 -*-
# @Author: ChrisMengxl
# @Date:   2021-02-08 20:57:47
# @Last Modified by:   ChrisMengxl
# @Last Modified time: 2021-02-08 21:26:42
class GameStats():
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 让游戏一开始处于非活动状态
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
