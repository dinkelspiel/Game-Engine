from src.scripts.modules.renderer import Screen
from src.scripts.modules.gui import *
import os

from src.scripts.game.player import Player
from src.scripts.game.enemy import Enemy

class screen_settins(Screen):
    def __init__(self, game):
        self.game = game

        self.play_button = gui_press_button(game)
        self.play_button.rect.set_x_constraint(percentage_constraint(0.03))
        self.play_button.rect.set_y_constraint(percentage_constraint(0.8))
        self.play_button.rect.set_width_constraint(percentage_constraint(0.3))
        self.play_button.rect.set_height_constraint(percentage_constraint(0.15))
        self.play_button.rect.set_border_radius(10)
        self.play_button.rect.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg'))

        self.play_button_text = gui_text(game)
        self.play_button_text.parent = self.play_button.rect
        self.play_button_text.text = "Back"
        self.play_button_text.set_x_constraint(center_constraint())
        self.play_button_text.set_y_constraint(center_constraint())
        self.play_button_text.set_size_constraint(percentage_constraint(0.8))
        self.play_button_text.set_color(self.game.color_handler.get_rgb('main_menu.text'))

    def update(self):
        self.play_button.update()
        self.play_button_text.update()
        self.play_button.rect.tween_to(percentage_constraint(0.03), percentage_constraint(0.8), 6)
        if self.play_button.hover:
            self.play_button.rect.tween_to(percentage_constraint(0.05), percentage_constraint(0.8), 6)

        if self.play_button.pressed:
            self.game.renderer.switch_screen('main_menu')

    def render(self):
        self.game.renderer.screen.fill(self.game.color_handler.get_rgb('main_menu.background'))
        self.play_button.render()
        self.play_button_text.render()