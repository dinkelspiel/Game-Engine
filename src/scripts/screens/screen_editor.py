from src.scripts.modules.renderer import Screen
from src.scripts.modules.gui import *
import os

class screen_editor(Screen):
    def __init__(self, game):
        self.game = game

        self.slider = gui_slider(game, 0, 100)

        self.slider.slider_body.set_x_constraint(center_constraint())
        self.slider.slider_body.set_y_constraint(percentage_constraint(0.96))
        self.slider.slider_body.set_width_constraint(percentage_constraint(0.9))
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

        self.song = self.game.sound_handler.load('song.mp3')

        self.slider.value_range = (0, int(self.song.get_length()))

        self.song_length = gui_text(game)
        self.song_length.parent = self.slider.slider_body
        time = str(self.song.get_length() / 60).split('.')[0] + ':' + str(int(str(self.song.get_length() / 60).split('.')[1]) / 1.6666666666)[0:2]
        self.song_length.text = str(time)
        self.song_length.set_y_constraint(pixel_constraint(-40))
        self.song_length.set_x_constraint(percentage_constraint(0.48))
        self.song_length.set_size_constraint(percentage_constraint(4))
        self.song_length.set_color(self.game.color_handler.get_rgb('main_menu.text'))
        
        self.song_length_current = gui_text(game)
        self.song_length_current.parent = self.slider.slider_body
        self.song_length_current.set_y_constraint(pixel_constraint(-40))
        self.song_length_current.set_x_constraint(percentage_constraint(0.52))
        self.song_length_current.set_size_constraint(percentage_constraint(4))
        self.song_length_current.set_color(self.game.color_handler.get_rgb('main_menu.text'))

    def update(self):
        current_time = self.slider.value
        self.song_length_current.text = str(max(current_time, 0.010) / 60).split('.')[0] + ':' + str(int(str(max(current_time, 0.010) / 60).split('.')[1]) / 1.6666666666)[0:2]

        self.slider.update()
        self.song_length.update()
        self.song_length_current.update()

    def render(self):
        self.game.renderer.screen.fill(self.game.color_handler.get_rgb('main_menu.background'))
        self.slider.render()
        self.song_length.render()
        self.song_length_current.render()