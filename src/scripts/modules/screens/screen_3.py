from src.scripts.modules.renderer import Screen
from src.scripts.modules.gui import *
import os

class screen_3(Screen):
    def __init__(self, game):
        self.game = game

        self.rect = gui_rect(game)   

        self.rect.set_x_constraint(center_constraint())
        self.rect.set_y_constraint(pixel_constraint(20))
        self.rect.set_width_constraint(percentage_constraint(0.1))
        self.rect.set_height_constraint(aspect_constraint(1))
        self.rect.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg'))

    def update(self):
        self.rect.update()

    def render(self):
        self.game.renderer.screen.fill(self.game.color_handler.get_rgb('main_menu.background'))
        self.rect.render()