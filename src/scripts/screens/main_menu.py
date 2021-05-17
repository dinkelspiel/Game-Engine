from src.scripts.modules.renderer import Screen
from src.scripts.modules.gui import *
import os

from src.scripts.game.player import Player
from src.scripts.game.enemy import Enemy

class main_menu(Screen):
    def __init__(self, game):
        self.game = game

        self.player = Player(game)
        self.enemy = Enemy(game)

    def update(self):
        self.player.update()
        self.enemy.update()

    def render(self):
        self.game.renderer.screen.fill(self.game.color_handler.get_rgb('main_menu.background'))
        self.player.render()
        self.enemy.render()