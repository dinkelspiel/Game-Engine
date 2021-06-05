from src.scripts.modules.renderer import Screen
from src.scripts.modules.gui import *
import os

class level_editor_screen(Screen):
    def __init__(self, game):
        self.game = game

        self.surface = pygame.Surface((16, 16))
        self.surface.fill((0, 0, 0))

        self.save_button = gui_press_button(game)
        self.save_button.rect.set_pos(percentage_constraint(0.6), percentage_constraint(0.05), 1)
        self.save_button.rect.set_size(percentage_constraint(0.2), percentage_constraint(0.1), 1)
        self.save_button.rect.set_border_radius(5)

        self.save_button_text = gui_text(game)
        self.save_button_text.text = "Save"
        self.save_button_text.parent = self.save_button.rect
        self.save_button_text.set_size_constraint(percentage_constraint(0.8))
        self.save_button_text.set_x_constraint(center_constraint())
        self.save_button_text.set_y_constraint(center_constraint())

    def update(self):
        mx, my = pygame.mouse.get_pos()
        mx = mx / 45
        my = my / 45
        if self.game.input.is_mouse_button_pressed(0):
            pygame.draw.rect(self.surface, (255, 255, 255), ((mx, my), (1, 1)))

        if self.game.input.is_mouse_button_pressed(2):
            pygame.draw.rect(self.surface, (0, 0, 0), ((mx, my), (1, 1)))

        self.save_button.rect.set_color((47, 93, 98), 4)
        if self.save_button.hover:
            self.save_button.rect.set_color((94, 139, 126), 2)

        if self.save_button.pressed:
            self.save_button.rect.set_color((255, 255, 255), 2)
            with open(os.path.join('src', 'resources', 'main', 'data', 'levels', 'level'), 'w') as file:
                for i in range(16):
                    for j in range(16):
                        pass
                file.write(self.surface)

        self.save_button.update()
        self.save_button_text.update()

    def render(self):
        self.game.renderer.main_surface.fill((71, 89, 126))

        self.save_button.render()
        self.save_button_text.render()

        self.game.renderer.main_surface.blit(pygame.transform.scale(self.surface, (720, 720)), (0, 0))