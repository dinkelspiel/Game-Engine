import pygame, math
from src.scripts.modules.entity import *
from .bullet import bullet_shooty_thingy
from src.scripts.modules.gui import * 

class enemy_ai_component:
    def __init__(self, game, parent) -> None:
        self.game = game
        self.parent = parent

        self.state = "movement"

        self.parent.bullets = []
        self.bullet_firerate = 15
        self.bullet_firerate_counter = 0

        self.image = self.game.image.load("enemy_bullet.png")

    def update(self):
        if self.parent.health > 0:
            if self.state == "movement":
                move_speed = 200 * self.game.delta_time
                self.parent.transform.x += self.game.math.lengthdir_x(move_speed, self.game.math.direction_between_points(self.parent.transform.x, self.parent.transform.y, self.game.player.transform.x, self.game.player.transform.y))
                self.parent.transform.y += self.game.math.lengthdir_y(move_speed, self.game.math.direction_between_points(self.parent.transform.x, self.parent.transform.y, self.game.player.transform.x, self.game.player.transform.y))
                if self.game.math.distance_between_points(self.parent.transform.x, self.parent.transform.y, self.game.player.transform.x, self.game.player.transform.y) < 500:
                    self.state = "attack_start"
            elif self.state == "attack_start":
                self.target_x = self.game.player.transform.x
                self.target_y = self.game.player.transform.y
                self.state = "attack"
            elif self.state == "attack":
                if self.game.math.distance_between_points(self.parent.transform.x, self.parent.transform.y, self.game.player.transform.x, self.game.player.transform.y) > 500:
                    self.state = "movement"
                self.bullet_firerate_counter += 100 * self.game.delta_time
                if self.bullet_firerate_counter > self.bullet_firerate:
                    self.bullet_firerate_counter = 0
                    self.parent.bullets.append([self.parent.transform.x, self.parent.transform.y, self.game.math.direction_between_points(self.parent.transform.x, self.parent.transform.y, self.parent.screen.player.transform.x, self.parent.screen.player.transform.y), 300])
                    self.parent.bullets.append([self.parent.transform.x, self.parent.transform.y, self.game.math.direction_between_points(self.parent.transform.x, self.parent.transform.y, self.parent.screen.player.transform.x, self.parent.screen.player.transform.y) + 90, 300])
                    self.parent.bullets.append([self.parent.transform.x, self.parent.transform.y, self.game.math.direction_between_points(self.parent.transform.x, self.parent.transform.y, self.parent.screen.player.transform.x, self.parent.screen.player.transform.y) + 180, 300])
                    self.parent.bullets.append([self.parent.transform.x, self.parent.transform.y, self.game.math.direction_between_points(self.parent.transform.x, self.parent.transform.y, self.parent.screen.player.transform.x, self.parent.screen.player.transform.y) + 270, 300])

    def render(self):
        move_speed = 700 * self.game.delta_time
        new_bullets = self.parent.bullets
        for i, item in enumerate(self.parent.bullets):
            item[3] -= 1
            if item[3] < 0:
                new_bullets.pop(i)
            item[0] += self.game.math.lengthdir_x(move_speed, item[2])
            item[1] += self.game.math.lengthdir_y(move_speed, item[2])
            image = pygame.transform.scale(self.image, (60, 60))
            img, rect = self.game.math.rotate_center(image, item[2], item[0], item[1])
            self.parent.screen.game_surface.blit(img, rect)
        self.parent.bullets = new_bullets
class enemy_renderer_component:
    def __init__(self, game, parent) -> None:
        self.game = game
        self.parent = parent

        self.image = self.game.image.load("enemy.png")

    def update(self):
        pass
    
    def render(self):
        if self.parent.health > 0:
            image = pygame.transform.scale(self.image, (88, 88))
            img, rect = self.game.math.rotate_center(image, 0, self.parent.transform.x, self.parent.transform.y)
            self.parent.screen.game_surface.blit(img, rect)

class enemy_health_system:
    def __init__(self, game, parent) -> None:
        self.game = game
        self.parent = parent

        self.parent.health = 50
        self.cant_get_hit_by = []

        self.health_bar_rect = gui_rect(game)
        self.health_bar_rect.set_y_constraint(percentage_constraint(0.02))
        self.health_bar_rect.set_x_constraint(percentage_constraint(0.02))
        self.health_bar_rect.set_width_constraint(percentage_constraint(0.3))
        self.health_bar_rect.set_height_constraint(pixel_constraint(5))
        self.health_bar_rect.set_border_radius(10)
        self.health_bar_rect.set_draw_color(self.game.color_handler.get_rgb('enemy.health_bar'))

    def update(self):
        self.health_bar_rect.tween_size(percentage_constraint(0.3 - (0.03 * ((50 - self.parent.health) / 5))), pixel_constraint(5), 24)
        self.health_bar_rect.update()
        if self.parent.health > 0:
            new_bullets = self.game.player.bullets
            for i, item in enumerate(self.game.player.bullets):
                if self.game.math.distance_between_points(self.parent.transform.x, self.parent.transform.y, item[0], item[1]) < 80:
                    new_bullets.pop(i)
                    self.parent.health -= 1
                    self.cant_get_hit_by.append(item)
                self.game.player.bullets = new_bullets
    
    def render(self):
        self.health_bar_rect.render()

class Enemy(Entity):
    def __init__(self, game, screen) -> None:
        self.game = game
        self.screen = screen

        self.components = []

        self.transform = Transform()
        self.transform.y = 200
        self.add_component(enemy_health_system(game, self))
        self.add_component(enemy_renderer_component(game, self))
        self.add_component(enemy_ai_component(game, self))
