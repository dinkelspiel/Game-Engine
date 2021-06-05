from src.scripts.modules.entity import *
import pygame, math, numpy

class Player_Renderer_Component:
    def __init__(self, game, parent) -> None:
        self.game = game
        self.parent = parent

        self.walking_animation = []
        self.walking_animation_frame = 0
        self.walking_animation_frame_counter = 0
        for i in range(18):
            if i < 10:
                i = '0' + str(i)
            self.walking_animation.append(self.game.image.load('player/walking_' + str(i) + '.png'))

    def update(self):
        pass

    def render(self):
        self.walking_animation_frame_counter += 100 * self.game.delta_time
        if self.walking_animation_frame_counter >= 3:
            self.walking_animation_frame += 1
            self.walking_animation_frame_counter = 0
        if self.walking_animation_frame > 17:
            self.walking_animation_frame = 0

        mx, my = pygame.mouse.get_pos()
        self.parent.transform.direction = 180 - self.game.math.direction_between_points(self.parent.transform.x, self.parent.transform.y, mx, my) + 360

        image = self.walking_animation[self.walking_animation_frame]
        image = pygame.transform.scale(image, (64, 64))
        image, rect = self.game.math.rotate_center(image, self.parent.transform.direction, self.parent.camera_relative_x, self.parent.camera_relative_y)
        self.game.renderer.main_surface.blit(image, rect)

class Player_Movement_Component():
    def __init__(self, game, parent) -> None:
        self.game = game
        self.parent = parent
        
    def update(self):
        move_speed = 400 * self.game.delta_time
        mx, my = pygame.mouse.get_pos()
        angle = self.game.math.direction_between_points(self.parent.transform.x, self.parent.transform.y, mx, my)
        if self.game.input.is_pressed('w'):
            self.parent.transform.x += self.game.math.lengthdir_x(move_speed, angle)
            self.parent.transform.y += self.game.math.lengthdir_y(move_speed, angle)




    def render(self):
        pass

class player(Entity):
    def __init__(self, game) -> None:
        
        self.game = game

        self.components = []
        self.transform = Transform()

        self.add_component(Camera_Relative_Component(game, self))
        self.add_component(Player_Renderer_Component(game, self))
        self.add_component(Player_Movement_Component(game, self))