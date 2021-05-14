from src.scripts.modules.renderer import Screen
from src.scripts.modules.gui import *
import os

class screen_4(Screen):
    def __init__(self, game):
        self.game = game

        self.button = gui_toggle_button(game)   

        self.button.rect.set_x_constraint(center_constraint())
        self.button.rect.set_y_constraint(center_constraint())
        self.button.rect.set_width_constraint(percentage_constraint(0.12))
        self.button.rect.set_height_constraint(percentage_constraint(0.1))
        self.button.rect.set_outline_radius(5)
        self.button.rect.set_border_radius(30)
        self.button.rect.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg'))

        self.button_inside_rect = gui_rect(game)

        self.button_inside_rect.parent = self.button.rect
        self.button_inside_rect.set_x_constraint(percentage_constraint(0.05))
        self.button_inside_rect.set_y_constraint(center_constraint())
        self.button_inside_rect.set_width_constraint(aspect_constraint(1))
        self.button_inside_rect.set_height_constraint(percentage_constraint(0.8))
        self.button_inside_rect.set_border_radius(30)
        self.button_inside_rect.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg'))


    def update(self):
        self.button.update()
        self.button_inside_rect.update()

        if self.button.hover:
            self.button_inside_rect.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg_2'))
        else:
            self.button_inside_rect.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg'))
        
        self.button_inside_rect.tween_to(percentage_constraint(0.05), center_constraint(), 24)
        if self.button.toggled:
            self.button_inside_rect.tween_to(percentage_constraint(0.57), center_constraint(), 24)

    def render(self):
        self.game.renderer.screen.fill(self.game.color_handler.get_rgb('main_menu.background'))
        self.button.render()
        self.button_inside_rect.render()