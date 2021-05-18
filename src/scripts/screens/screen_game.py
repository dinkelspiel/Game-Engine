from src.scripts.modules.renderer import Screen
from src.scripts.modules.gui import *
import os

from src.scripts.game.player import Player
from src.scripts.game.enemy import Enemy

class screen_game(Screen):
    def __init__(self, game):
        self.game = game

        self.player = Player(game, self)
        self.enemy = Enemy(game, self)

        self.game_surface = pygame.Surface((1280, 720), pygame.SRCALPHA)

    def update(self):
        self.player.update()
        self.enemy.update()

        if self.player.health < 0:
            self.player.health = 10
            self.enemy.health = 50 
            self.game.renderer.switch_screen('lose')
        if self.enemy.health < 2:
            self.player.health = 10
            self.enemy.health = 50 
            self.game.renderer.switch_screen('win')

    def render(self):
        self.game_surface = pygame.Surface((1280, 720), pygame.SRCALPHA)
        self.game.renderer.screen.fill(self.game.color_handler.get_rgb('main_menu.background'))
        self.player.render()
        self.enemy.render() 
        width_diff = abs(self.game.renderer.screen.get_width() - self.game.renderer.original_size[0])
        height_diff = abs(self.game.renderer.screen.get_height() - self.game.renderer.original_size[1])
        if width_diff > height_diff:
            aspect_ratio = self.game.renderer.screen.get_width() / self.game.renderer.original_size[0]
            width = self.game.renderer.screen.get_width()
            height = self.game.renderer.original_size[1] * aspect_ratio
        else:
            aspect_ratio = self.game.renderer.screen.get_height() / self.game.renderer.original_size[1]
            width = self.game.renderer.original_size[0] * aspect_ratio
            height = self.game.renderer.screen.get_height()

        mx, my = pygame.mouse.get_pos()
        self.game.relative_mxmy = (mx / aspect_ratio, my / aspect_ratio)

        self.game.renderer.screen.blit(pygame.transform.scale(self.game_surface, (int(width), int(height))), (0, 0))