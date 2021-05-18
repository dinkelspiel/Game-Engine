import pygame, math
from src.scripts.modules.entity import *
from .bullet import *
from src.scripts.modules.gui import * 

class player_movement_component:
    def __init__(self, game, parent) -> None:
        self.game = game
        self.parent = parent

    def update(self):
        move_speed = 300 * self.game.delta_time
        if self.game.input.is_pressed("a") and self.parent.transform.x > 0 + 32 + move_speed:
            self.parent.transform.x -= move_speed
        if self.game.input.is_pressed("d") and self.parent.transform.x < self.parent.screen.game_surface.get_width() - move_speed - 32:
            self.parent.transform.x += move_speed
        if self.game.input.is_pressed("w") and self.parent.transform.y > 0 + 32 + move_speed:
            self.parent.transform.y-= move_speed
        if self.game.input.is_pressed("s") and self.parent.transform.y < self.parent.screen.game_surface.get_height() - move_speed - 32:
            self.parent.transform.y += move_speed

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
        image = pygame.transform.scale(self.image, (64, 64))
        img, rect = self.game.math.rotate_center(image, 0, self.parent.transform.x, self.parent.transform.y)
        self.parent.screen.game_surface.blit(img, rect)

class player_health_system:
    def __init__(self, game, parent) -> None:
        self.game = game
        self.parent = parent

        self.parent.health = 10
        self.cant_get_hit_by = []

        self.health_bar_rect = gui_rect(game)
        self.health_bar_rect.set_y_constraint(percentage_constraint(0.02))
        self.health_bar_rect.set_x_constraint(percentage_constraint(0.67))
        self.health_bar_rect.set_width_constraint(percentage_constraint(0.3))
        self.health_bar_rect.set_height_constraint(pixel_constraint(5))
        self.health_bar_rect.set_border_radius(10)
        self.health_bar_rect.set_draw_color(self.game.color_handler.get_rgb('player.health_bar'))

    def update(self):
        self.health_bar_rect.tween_size(percentage_constraint(0.3 - (0.03 * (10 - self.parent.health))), pixel_constraint(5), 24)
        self.health_bar_rect.update()

        for i, item in enumerate(self.parent.screen.enemy.bullets):
            if self.game.math.distance_between_points(self.parent.transform.x, self.parent.transform.y, item[0], item[1]) < 60:
                self.parent.screen.enemy.bullets.pop(i)
                self.parent.health -= 1
    
    def render(self):
        self.health_bar_rect.render()

class Player(Entity):
    def __init__(self, game, screen) -> None:
        self.game = game
        self.screen = screen

        self.game.player = self

        self.components = []

        self.transform = Transform()
        self.transform.y = 500

        self.add_component(bullet_shooty_thingy(game, self))
        self.add_component(player_health_system(game, self))
        self.add_component(player_movement_component(game, self))
        self.add_component(player_renderer_component(game, self))
