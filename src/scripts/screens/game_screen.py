from src.scripts.modules.renderer import Screen
from src.scripts.modules.gui import *
import os

from src.scripts.game.player import player

class game_screen(Screen):
    def __init__(self, game):
        self.game = game

        self.player = player(game)

    def update(self):
        self.player.update()

    def render(self):
        self.game.renderer.main_surface.fill((0, 0, 0))

        self.player.render()