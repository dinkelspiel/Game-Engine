import pygame, math
from src.scripts.modules.entity import *

class bullet_shooty_thingy:
    def __init__(self, game, parent) -> None:
        self.game = game
        self.parent = parent

        self.parent.bullets = []
        self.image = self.game.image.load("bullet.png")
    
    def update(self):
        if self.game.input.is_mouse_button_just_pressed():
            mx, my = pygame.mouse.get_pos()
            self.parent.bullets.append([self.parent.transform.x, self.parent.transform.y, self.game.math.direction_between_points(self.parent.transform.x, self.parent.transform.y, mx, my), 400])

    def render(self):
        move_speed = 200 * self.game.delta_time
        new_bullets = self.parent.bullets
        for i, item in enumerate(self.parent.bullets):
            item[3] -= 1
            if item[3] == 0:
                new_bullets.pop(i)
            item[0] += self.game.math.lengthdir_x(3, item[2])
            item[1] += self.game.math.lengthdir_y(3, item[2])
            image = pygame.transform.scale(self.image, (50, 25))
            img, rect = self.game.math.rotate_center(image, 180 - item[2] + 180, item[0], item[1])
            self.game.renderer.screen.blit(img, rect)
        self.parent.bullets = new_bullets

class bullet_shooty_thingy2:
    def __init__(self, game, parent) -> None:
        self.game = game
        self.parent = parent

        self.parent.bullets = []
        self.image = self.game.image.load("bullet.png")
    
    def update(self):
        if self.game.input.is_mouse_button_just_pressed():
            mx, my = pygame.mouse.get_pos()
            self.parent.bullets.append([self.parent.transform.x, self.parent.transform.y, self.game.math.direction_between_points(self.parent.transform.x, self.parent.transform.y, mx, my), 400])

    def render(self):
        new_bullets = self.parent.bullets
        for i, item in enumerate(self.parent.bullets):
            item[3] -= 1
            if item[3] == 0:
                new_bullets.pop(i)
            item[0] += self.game.math.lengthdir_x(1, item[2])
            item[1] += self.game.math.lengthdir_y(1, item[2])
            img, rect = self.game.math.rotate_center(self.image, item[3], item[0], item[1])
            self.game.renderer.screen.blit(pygame.transform.scale(img, (50, 25)), rect)
        self.parent.bullets = new_bullets