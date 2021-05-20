from src.scripts.modules.renderer import Screen
from src.scripts.modules.gui import *
import os

class screen_main(Screen):
    def __init__(self, game):
        self.game = game

    def update(self):
        pass

    def render(self):
        self.game.renderer.screen.fill(self.game.color_handler.get_rgb('main_menu.background'))