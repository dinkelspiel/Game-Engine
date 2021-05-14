from src.scripts.modules.renderer import Screen
from src.scripts.modules.gui import *
import os

class screen_1(Screen):
    def __init__(self, game):
        self.game = game

        self.button = gui_toggle_button(game)

        self.button.rect.set_x_constraint(percentage_constraint(0.06))
        self.button.rect.set_y_constraint(percentage_constraint(0.07))
        self.button.rect.set_height_constraint(percentage_constraint(0.1))
        self.button.rect.set_width_constraint(aspect_constraint(3))
        self.button.rect.set_border_radius(5)
        self.button.rect.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg'))

        self.slider = gui_slider(game, 0, 100)

        self.slider.slider_body.set_x_constraint(percentage_constraint(0.06))
        self.slider.slider_body.set_y_constraint(percentage_constraint(0.25))
        self.slider.slider_body.set_width_constraint(pixel_constraint(200))
        self.slider.slider_body.set_height_constraint(pixel_constraint(5))
        self.slider.slider_body.set_border_radius(50)
        self.slider.slider_body.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg'))   

        self.slider.slider_head.parent = self.slider.slider_body
        self.slider.slider_head.set_x_constraint(pixel_constraint(0))
        self.slider.slider_head.set_y_constraint(center_constraint())
        self.slider.slider_head.set_width_constraint(pixel_constraint(20))
        self.slider.slider_head.set_height_constraint(pixel_constraint(20))
        self.slider.slider_head.set_border_radius(10)
        self.slider.slider_head.set_draw_color(self.game.color_handler.get_rgb('main_menu.text'))     

        self.button2 = gui_toggle_button(game)   

        self.button2.rect.set_x_constraint(percentage_constraint(0.06))
        self.button2.rect.set_y_constraint(percentage_constraint(0.32))
        self.button2.rect.set_width_constraint(percentage_constraint(0.12))
        self.button2.rect.set_height_constraint(percentage_constraint(0.1))
        self.button2.rect.set_outline_radius(5)
        self.button2.rect.set_border_radius(30)
        self.button2.rect.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg'))

        self.button_inside_rect = gui_rect(game)

        self.button_inside_rect.parent = self.button2.rect
        self.button_inside_rect.set_x_constraint(percentage_constraint(0.05))
        self.button_inside_rect.set_y_constraint(center_constraint())
        self.button_inside_rect.set_width_constraint(aspect_constraint(1))
        self.button_inside_rect.set_height_constraint(percentage_constraint(0.8))
        self.button_inside_rect.set_border_radius(30)
        self.button_inside_rect.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg')) 

    def update(self):
        self.button.update()
        self.slider.update()
        self.button2.update()
        self.button_inside_rect.update()

        self.button.rect.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg'))
        if self.button.hover:
            self.button.rect.tween_to(percentage_constraint(0.08), percentage_constraint(0.07), 24)
            self.button.rect.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg_2'))
        else:
            self.button.rect.tween_to(percentage_constraint(0.06), percentage_constraint(0.07), 24)

        if self.button.toggled:
            self.button.rect.set_draw_color(self.game.color_handler.get_rgb('main_menu.text'))
            self.button.rect.tween_to(percentage_constraint(0.08), percentage_constraint(0.07), 24)

        if self.button2.hover:
            self.button_inside_rect.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg_2'))
        else:
            self.button_inside_rect.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg'))
        
        self.button_inside_rect.tween_to(percentage_constraint(0.05), center_constraint(), 24)
        if self.button2.toggled:
            self.button_inside_rect.tween_to(percentage_constraint(0.57), center_constraint(), 24)

    def render(self):
        self.game.renderer.screen.fill(self.game.color_handler.get_rgb('main_menu.background'))
        self.button.render()
        self.slider.render()
        self.button2.render()
        self.button_inside_rect.render()
        self.game.renderer.screen.blit(self.game.font_handler.render(str(int(self.slider.value)), 'default', 32, self.game.color_handler.get_rgb('main_menu.text')), (300, 160))
        #value = int((self.slider_head.x - self.slider_body.x) / (self.slider_body.width / 100))
        #self.game.renderer.screen.blit(self.game.font_handler.render(str(value), 'default', 48, self.game.color_handler.get_rgb('main_menu.text')), (20, 20))