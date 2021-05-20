from .gui import *
import time

class Debug:
    def __init__(self, game) -> None:
        self.game = game

        self.debug_gui = gui_rect(game)
        self.debug_gui.set_x_constraint(percentage_constraint(0.55))
        self.debug_gui.set_y_constraint(percentage_constraint(0.6))
        self.debug_gui.set_width_constraint(percentage_constraint(0.44))
        self.debug_gui.set_height_constraint(percentage_constraint(0.38))
        self.debug_gui.set_border_radius(10)
        self.debug_gui.set_draw_color(self.game.color_handler.get_rgb('console.background'))

        self.update_time = 0
        self.render_time = 0

        self.frame_ms = 0

        self.fps_start_time = time.time()
        self.fps_end_time = 0

        self.latest_readings = 0

        self.fps = 0

        self.render_hud = False

    def send_stats(self, update_time, render_time):
        self.update_time = update_time * 1000
        self.render_time = render_time * 1000
        self.frame_ms = (self.update_time + self.render_time) * 1000

    def update(self):
        self.debug_gui.update()
        self.fps_end_time = time.time()
        self.latest_readings += self.frame_ms
        if self.fps_end_time - self.fps_start_time > 1:
            self.fps_start_time = time.time()
            self.latest_readings = 0

    def render(self):
        if self.render_hud:
            self.debug_gui.render()