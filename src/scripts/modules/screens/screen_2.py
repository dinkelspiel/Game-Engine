from src.scripts.modules.renderer import Screen
from src.scripts.modules.gui import *
import os

class screen_2(Screen):
    def __init__(self, game):
        self.game = game

        self.slider = gui_slider(game, 0, 100)

        self.slider.slider_body.set_x_constraint(center_constraint())
        self.slider.slider_body.set_y_constraint(center_constraint())
        self.slider.slider_body.set_width_constraint(pixel_constraint(200))
        self.slider.slider_body.set_height_constraint(pixel_constraint(5))
        self.slider.slider_body.set_border_radius(10)
        self.slider.slider_body.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg'))   

        self.slider.slider_head.parent = self.slider.slider_body
        self.slider.slider_head.set_x_constraint(pixel_constraint(0))
        self.slider.slider_head.set_y_constraint(center_constraint())
        self.slider.slider_head.set_width_constraint(pixel_constraint(20))
        self.slider.slider_head.set_height_constraint(pixel_constraint(20))
        self.slider.slider_head.set_border_radius(10)
        self.slider.slider_head.set_draw_color(self.game.color_handler.get_rgb('main_menu.text'))      

    def update(self):
        self.slider.update()

    def render(self):
        self.game.renderer.screen.fill(self.game.color_handler.get_rgb('main_menu.background'))
        self.slider.render()
        #value = int((self.slider_head.x - self.slider_body.x) / (self.slider_body.width / 100))
        #self.game.renderer.screen.blit(self.game.font_handler.render(str(value), 'default', 48, self.game.color_handler.get_rgb('main_menu.text')), (20, 20))