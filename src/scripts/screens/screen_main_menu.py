from src.scripts.modules.renderer import Screen
from src.scripts.modules.gui import *
import os

class screen_main_menu(Screen):
    def __init__(self, game):
        self.game = game

        self.buttons_bg = gui_rect(game)
        self.buttons_bg.set_x_constraint(percentage_constraint(0.1))
        self.buttons_bg.set_y_constraint(center_constraint())
        self.buttons_bg.set_width_constraint(percentage_constraint(0.1))
        self.buttons_bg.set_height_constraint(percentage_constraint(0.8))
        self.buttons_bg.set_border_radius(10)
        self.buttons_bg.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg_2'))

        self.play_button = gui_press_button(game)
        self.play_button.rect.set_x_constraint(percentage_constraint(0.15))
        self.play_button.rect.set_y_constraint(percentage_constraint(0.15))
        self.play_button.rect.set_width_constraint(percentage_constraint(0.3))
        self.play_button.rect.set_height_constraint(percentage_constraint(0.15))
        self.play_button.rect.set_border_radius(10)
        self.play_button.rect.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg'))

        self.play_button_text = gui_text(game)
        self.play_button_text.parent = self.play_button.rect
        self.play_button_text.text = "Play"
        self.play_button_text.set_x_constraint(center_constraint())
        self.play_button_text.set_y_constraint(center_constraint())
        self.play_button_text.set_size_constraint(percentage_constraint(0.8))
        self.play_button_text.set_color(self.game.color_handler.get_rgb('main_menu.text'))

        self.play_button2 = gui_press_button(game)
        self.play_button2.rect.set_x_constraint(percentage_constraint(0.15))
        self.play_button2.rect.set_y_constraint(center_constraint())
        self.play_button2.rect.set_width_constraint(percentage_constraint(0.3))
        self.play_button2.rect.set_height_constraint(percentage_constraint(0.15))
        self.play_button2.rect.set_border_radius(10)
        self.play_button2.rect.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg'))

        self.play_button2_text = gui_text(game)
        self.play_button2_text.parent = self.play_button2.rect
        self.play_button2_text.text = "Settings"
        self.play_button2_text.set_x_constraint(center_constraint())
        self.play_button2_text.set_y_constraint(center_constraint())
        self.play_button2_text.set_size_constraint(percentage_constraint(0.8))
        self.play_button2_text.set_color(self.game.color_handler.get_rgb('main_menu.text'))

        self.play_button3 = gui_press_button(game)
        self.play_button3.rect.set_x_constraint(percentage_constraint(0.15))
        self.play_button3.rect.set_y_constraint(percentage_constraint(0.7))
        self.play_button3.rect.set_width_constraint(percentage_constraint(0.3))
        self.play_button3.rect.set_height_constraint(percentage_constraint(0.15))
        self.play_button3.rect.set_border_radius(10)
        self.play_button3.rect.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg'))

        self.play_button3_text = gui_text(game)
        self.play_button3_text.parent = self.play_button3.rect
        self.play_button3_text.text = "Exit"
        self.play_button3_text.set_x_constraint(center_constraint())
        self.play_button3_text.set_y_constraint(center_constraint())
        self.play_button3_text.set_size_constraint(percentage_constraint(0.8))
        self.play_button3_text.set_color(self.game.color_handler.get_rgb('main_menu.text'))

    def update(self):
        self.buttons_bg.update()
        self.play_button.update()
        self.play_button2.update()
        self.play_button3.update()
        self.play_button_text.update()
        self.play_button2_text.update()
        self.play_button3_text.update()
        self.play_button.rect.tween_to(percentage_constraint(0.15), percentage_constraint(0.15), 6)
        if self.play_button.hover:
            self.play_button.rect.tween_to(percentage_constraint(0.175), percentage_constraint(0.15), 6)

        if self.play_button.pressed:
            self.game.renderer.switch_screen('game')

        self.play_button2.rect.tween_to(percentage_constraint(0.15), center_constraint(), 6)
        if self.play_button2.hover:
            self.play_button2.rect.tween_to(percentage_constraint(0.175), center_constraint(), 6)

        if self.play_button2.pressed:
            self.game.renderer.switch_screen('settings')

        self.play_button3.rect.tween_to(percentage_constraint(0.15), percentage_constraint(0.7), 6)
        if self.play_button3.hover:
            self.play_button3.rect.tween_to(percentage_constraint(0.175), percentage_constraint(0.7), 6)
        
        if self.play_button3.pressed:
            self.game.stop()

    def render(self):
        self.game.renderer.screen.fill(self.game.color_handler.get_rgb('main_menu.background'))
        self.buttons_bg.render()
        self.play_button.render()
        self.play_button2.render()
        self.play_button3.render()
        self.play_button_text.render()
        self.play_button2_text.render()
        self.play_button3_text.render()