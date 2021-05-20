from src.scripts.modules.renderer import Screen
from src.scripts.modules.gui import *
from src.scripts.game.player import player
import os

class screen_main(Screen):
    def __init__(self, game):
        self.game = game

        self.Player = player(game, self)

    def update(self):
        self.Player.update()

    def render(self):
        self.game.renderer.screen.fill(self.game.color_handler.get_rgb('main_menu.background'))
        self.Player.render()