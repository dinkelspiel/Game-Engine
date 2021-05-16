import pygame, math
from src.scripts.modules.entity import *

class player_movement_component:
    def __init__(self, game, parent) -> None:
        self.game = game
        self.parent = parent
    
    def update(self):
        if self.game.input.is_pressed("a"):
            self.parent.transform.x -= 1
        if self.game.input.is_pressed("d"):
            self.parent.transform.x += 1
        if self.game.input.is_pressed("w"):
            self.parent.transform.y-= 1
        if self.game.input.is_pressed("s"):
            self.parent.transform.y += 1

    def render(self):
        pass

class player_renderer_component:
    def __init__(self, game, parent) -> None:
        self.game = game
        self.parent = parent

        self.image = self.game.image.load("player.png")

    def update(self):
        pass
    
    def render(self):
        self.game.renderer.screen.blit(self.image, (self.parent.transform.x, self.parent.transform.y))

class Player(Entity):
    def __init__(self, game) -> None:
        self.game = game

        self.components = []

        self.transform = Transform()
        self.transform.y = 500

        self.add_component(player_movement_component(game, self))
        self.add_component(player_renderer_component(game, self))
