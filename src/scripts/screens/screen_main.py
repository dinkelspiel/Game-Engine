from src.scripts.modules.renderer import Screen
from src.scripts.modules.gui import *
import os

class screen_main(Screen):
    def __init__(self, game):
        self.game = game

        self.rect1 = gui_rect(game)
        self.rect1.set_x_constraint(percentage_constraint(0.1))
        self.rect1.set_y_constraint(percentage_constraint(0.9))
        self.rect1.set_height_constraint(aspect_constraint(1))
        self.rect1.set_width_constraint(percentage_constraint(0.05))

        self.rect2 = gui_rect(game)
        self.rect2.set_x_constraint(percentage_constraint(0.17))
        self.rect2.set_y_constraint(percentage_constraint(0.9))
        self.rect2.set_height_constraint(aspect_constraint(1))
        self.rect2.set_width_constraint(percentage_constraint(0.05))

        self.rect3 = gui_rect(game)
        self.rect3.set_x_constraint(percentage_constraint(0.25))
        self.rect3.set_y_constraint(percentage_constraint(0.9))
        self.rect3.set_height_constraint(aspect_constraint(1))
        self.rect3.set_width_constraint(percentage_constraint(0.05))

        self.rect4 = gui_rect(game)
        self.rect4.set_x_constraint(percentage_constraint(0.32))
        self.rect4.set_y_constraint(percentage_constraint(0.9))
        self.rect4.set_height_constraint(aspect_constraint(1))
        self.rect4.set_width_constraint(percentage_constraint(0.05))

    def update(self):
        self.rect1.tween_color((20, 20, 20), 24)
        self.rect2.tween_color((20, 20, 20), 24)
        self.rect3.tween_color((20, 20, 20), 24)
        self.rect4.tween_color((20, 20, 20), 24)
        if self.game.input.is_pressed('d'):
            self.rect1.tween_color((255, 255, 255), 4)

        if self.game.input.is_pressed('f'):
            self.rect2.tween_color((255, 255, 255), 4)

        if self.game.input.is_pressed('j'):
            self.rect3.tween_color((255, 255, 255), 4)

        if self.game.input.is_pressed('k'):
            self.rect4.tween_color((255, 255, 255), 4)

        self.rect1.update()
        self.rect2.update()
        self.rect3.update()
        self.rect4.update()

    def render(self):
        self.game.renderer.screen.fill(self.game.color_handler.get_rgb('main_menu.background'))
        self.rect1.render()
        self.rect2.render()
        self.rect3.render()
        self.rect4.render()