from src.scripts.modules.entity import *

class player(Entity):
    def __init__(self, game) -> None:
        
        self.game = game

        self.components = []
        self.transform = Transform()

        self.add_component(Camera_Relative_Component(game, self))
        self.add_component(Sprite_Renderer_Component(game, self))
        self.get_component(Sprite_Renderer_Component).sprite = self.game.image.load('error.png')
        self.get_component(Sprite_Renderer_Component).surface = self.game.renderer.main_surface