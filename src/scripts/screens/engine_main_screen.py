from src.scripts.modules.renderer import Screen
from src.scripts.modules.gui import *
import os

class engine_main_screen(Screen):
    def __init__(self, game):
        self.game = game
        
        self.right_panel = gui_rect(game)
        self.right_panel.set_pos(percentage_constraint(0.78), pixel_constraint(25), 1)
        self.right_panel.set_size(percentage_constraint(0.22), percentage_constraint(1), 1)
        self.right_panel.set_color(self.game.color_handler.get_rgb('engine.background'), 2)

        self.left_panel = gui_rect(game)
        self.left_panel.set_pos(percentage_constraint(0), pixel_constraint(25), 1)
        self.left_panel.set_size(percentage_constraint(0.22), percentage_constraint(1), 1)
        self.left_panel.set_color(self.game.color_handler.get_rgb('engine.background'), 2)

        self.top_panel = gui_rect(game)
        self.top_panel.set_pos(pixel_constraint(0), pixel_constraint(0), 1)
        self.top_panel.set_size(percentage_constraint(1), pixel_constraint(25), 1)
        self.top_panel.set_color(self.game.color_handler.get_rgb('engine.background_alt'), 2)

        self.bottom_panel = gui_rect(game)
        self.bottom_panel.set_pos(percentage_constraint(0.22), percentage_constraint(0.595), 1)
        self.bottom_panel.set_size(percentage_constraint(0.56), percentage_constraint(0.4375), 1)
        self.bottom_panel.set_color(self.game.color_handler.get_rgb('engine.background_alt'), 2)
        
        self.screen_panel = gui_rect(game)
        self.screen_panel.set_pos(percentage_constraint(0.22), pixel_constraint(26), 2)
        self.screen_panel.set_size(aspect_constraint(1.7777), percentage_constraint(0.56), 2)
        self.screen_panel.set_color((255, 0, 0), 2)

        self.add_asset_button = gui_toggle_button(game)
        self.add_asset_button.rect.parent = self.bottom_panel
        self.add_asset_button.rect.set_pos(pixel_constraint(5), pixel_constraint(5), 2)
        self.add_asset_button.rect.set_size(pixel_constraint(30), pixel_constraint(30), 5)
        self.add_asset_button.rect.visible = False
        self.add_asset_button.input_state = "general"

        self.add_asset_button_1 = gui_rect(game)
        self.add_asset_button_1.parent = self.add_asset_button.rect
        self.add_asset_button_1.set_pos(center_constraint(), center_constraint(), 2)
        self.add_asset_button_1.set_size(percentage_constraint(1), percentage_constraint(0.2), 2)
        self.add_asset_button_1.set_border_radius(10)
        self.add_asset_button_1.set_color((200, 200, 200), 1)

        self.add_asset_button_2 = gui_rect(game)
        self.add_asset_button_2.parent = self.add_asset_button.rect
        self.add_asset_button_2.set_pos(center_constraint(), center_constraint(), 2)
        self.add_asset_button_2.set_size(percentage_constraint(0.2), percentage_constraint(1), 2)
        self.add_asset_button_2.set_border_radius(10)
        self.add_asset_button_2.set_color((200, 200, 200), 1)

        self.add_asset = gui_rect(game)
        self.add_asset.set_pos(percentage_constraint(0.3), percentage_constraint(1), 1)
        self.add_asset.set_size(percentage_constraint(0.2), percentage_constraint(0.6), 1)
        self.add_asset.set_color(self.game.color_handler.get_rgb('engine.background'), 1)
        self.add_asset.set_border_radius(10)

    def update(self):
        self.add_asset.set_pos(percentage_constraint(0.3), (percentage_constraint(1)), 6)    
        self.add_asset_button_1.set_color((200, 200, 200), 12)
        self.add_asset_button_2.set_color((200, 200, 200), 12)
        if self.add_asset_button.hover:
            self.add_asset_button_1.set_color((100, 100, 100), 6)
            self.add_asset_button_2.set_color((100, 100, 100), 6)

        if self.add_asset_button.toggled:
            self.add_asset_button_1.set_color((100, 100, 100), 6)
            self.add_asset_button_2.set_color((100, 100, 100), 6)       
            self.add_asset.set_pos(percentage_constraint(0.3), (percentage_constraint(0.5)), 6)     
            self.game.input.set_input_state("asset_pack_change")
            if not self.add_asset.is_touching_mouse() and self.game.input.is_mouse_button_just_pressed():
                self.add_asset_button.toggled = False
                self.game.input.set_input_state("general")

        self.right_panel.update()
        self.left_panel.update()
        self.top_panel.update()
        self.bottom_panel.update()
        self.screen_panel.update()
        self.add_asset_button.update()
        self.add_asset_button_1.update()
        self.add_asset_button_2.update()
        self.add_asset.update()

    def render(self):
        self.game.renderer.main_surface.fill((0, 0, 0))
        self.right_panel.render()
        self.left_panel.render()
        self.top_panel.render()
        self.bottom_panel.render()
        self.screen_panel.render()
        self.add_asset_button.render()
        self.add_asset_button_1.render()
        self.add_asset_button_2.render()
        self.add_asset.render()