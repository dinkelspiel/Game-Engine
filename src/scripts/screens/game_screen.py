from src.scripts.modules.renderer import Screen
from src.scripts.modules.gui import *
import os

from src.scripts.game.player import player
from src.scripts.game.world import world

class game_screen(Screen):
    def __init__(self, game):
        self.game = game

        self.player = player(game)
        self.world = world(game)

    def update(self):
        self.player.update()
        self.world.update()

    def render(self):
        self.game.renderer.main_surface.fill((0, 0, 0))

        self.player.render()
        self.player.render()