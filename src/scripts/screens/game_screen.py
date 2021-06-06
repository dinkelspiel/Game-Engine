from src.scripts.modules.renderer import Screen
from src.scripts.modules.gui import *
import os

from src.scripts.game.player import player

class game_screen(Screen):
    def __init__(self, game):
        self.game = game

        self.player = player(game)
        self.player2 = player(game)
        self.player2.fwd = 'UP'
        self.player2.color = (153, 229, 80)
        self.player2.color2 = (106, 190, 48)

    def update(self):
        self.player.update()
        self.player2.update()

    def render(self):
        self.game.renderer.main_surface.fill((0, 0, 0))

        self.player.render()
        self.player2.render()