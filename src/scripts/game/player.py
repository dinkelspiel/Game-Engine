import pygame
from src.scripts.modules.entity import *

class player_movement_component:
    def __init__(self, game, parent) -> None:
        self.game = game
        self.parent = parent


    def update(self):
        move_speed = 350 * self.game.delta_time
        if self.game.input.is_pressed('w'):
            self.parent.transform.y -= move_speed
        if self.game.input.is_pressed('s'):
            self.parent.transform.y += move_speed     
        if self.game.input.is_pressed('a'):
            self.parent.transform.x -= move_speed
        if self.game.input.is_pressed('d'):
            self.parent.transform.x += move_speed  

    def render(self):
        pass

class player_renderer_component:
    def __init__(self, game, parent) -> None:
        self.game = game
        self.parent = parent


    def update(self):
        pass

    def render(self):
        pygame.draw.rect(self.game.renderer.screen, (255, 255, 255), ((self.parent.transform.x, self.parent.transform.y), (50, 50)))

class player(Entity):
    def __init__(self, game, screen) -> None:
        self.game = game
        self.screen = screen

        self.components = []
        self.game.player = self

        self.transform = Transform()
        self.transform.y = 500

        self.add_component(player_movement_component(game, self))
        self.add_component(player_renderer_component(game, self))
        