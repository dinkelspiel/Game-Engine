from src.scripts.modules.entity import *
import pygame, math, numpy, os

class World_Renderer_Component:
    def __init__(self, game, parent) -> None:
        self.game = game
        self.parent = parent

        self.level_data = open(os.path.join('src', 'resources', self.game.current_assetpack, 'data', 'levels', 'level'), 'r').read()
        exec('self.level_data = ' + self.level_data)
        print(self.level_data)

    def update(self):
        pass

    def render(self):
        pass

class world(Entity):
    def __init__(self, game) -> None:
        
        self.game = game

        self.components = []
        self.transform = Transform()

        self.add_component(Camera_Relative_Component(game, self))
        self.add_component(World_Renderer_Component(game, self))