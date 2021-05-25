## Imports

import pygame, pyautogui
from src.scripts.modules.gui import *
import webbrowser

## Class for making you unable to register a non screen

class Screen:
    pass

## A Camera that pans around and moves object that has the Camera_Relative_Component component

class Camera:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

## Main Renderer Handler

class renderer:

    ## Functions

    # Getter for screen size to Vector2 Tuple

    def get_screen_size(self):
        return (self.screen.get_width(), self.screen.get_height())

    # Initializes a screen to be able to be used in renderer

    def load_screen(self, screen: Screen, screen_id):
        screen_add = screen
        self.screens[screen_id] = screen_add

    # Switches to a initialized screen

    def switch_screen(self, screen_id):
        self.current_screen = screen_id

    ## Initialize

    def __init__(self, game):

        self.game = game

        ## Initialize camera for renderer

        self.camera = Camera()

        ## Create variables

        self.screens = {}
        self.current_screen = ''

        ## Sizes

        self.original_size = (1280, 720)

        ## Start Surfaces

        self.screen_rect = gui_rect(game)
        self.screen_rect.set_x_constraint(center_constraint())
        self.screen_rect.set_y_constraint(center_constraint())
        self.screen_rect.set_width_constraint(percentage_constraint(1))
        self.screen_rect.set_height_constraint(percentage_constraint(1))
        self.screen_rect.visible = False
        self.screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
        self.main_surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)

        ## Load Fallback Screen

        self.load_screen(fallback_screen(game), 'fallback')

    ## Update Method

    def update(self):
        
        # Update Screen Rect

        self.screen_rect.update()
        self.screen_rect.x = 0
        self.screen_rect.y = 0
        self.screen_rect.width = self.get_screen_size()[0]
        self.screen_rect.height = self.get_screen_size()[1]

        # Clear main surface for drawing

        self.main_surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)

        # Update the currently selected screen or fallback if screen is invalid

        if self.current_screen in self.screens:
            self.screens[self.current_screen].update()
        else:
            self.screens['fallback'].update()


    ## Render Method

    def render(self):

        # Render the currently selected screen or fallback if screen is invalid

        if self.current_screen in self.screens:
            self.screens[self.current_screen].render()
        else:
            self.screens['fallback'].render()

        # Render the debug view

        self.screen_rect.render()

        self.game.debug.render()

        # Update the screen

        self.screen.blit(self.main_surface, (0, 0))
        pygame.display.update()

## Fallback screen

class fallback_screen(Screen):
    def __init__(self, game):
        self.game = game

        ## Define rect for text

        self.rect = gui_rect(game)
        self.rect.set_x_constraint(pixel_constraint(0))
        self.rect.set_y_constraint(pixel_constraint(0))
        self.rect.set_width_constraint(percentage_constraint(1))
        self.rect.set_height_constraint(percentage_constraint(1))
        self.rect.visible = False

        ## Define text 

        self.text = gui_text(game)
        self.text.parent = self.rect
        self.text.set_x_constraint(center_constraint())
        self.text.set_y_constraint(percentage_constraint(0.25))
        self.text.size = 62
        self.text.text = "Fallback Screen"

        self.text2 = gui_text(game)
        self.text2.parent = self.rect
        self.text2.set_x_constraint(center_constraint())
        self.text2.set_y_constraint(percentage_constraint(0.3))
        self.text2.size = 23
        self.text2.text = "This screen either appeared because you put in a \ninvalid name for a screen switch or you have no screen loaded.\nIf you think this is a bug create a issue on the Github page."

        ## Redirect button

        self.button = gui_press_button(game)
        self.button.rect.set_x_constraint(center_constraint())
        self.button.rect.set_y_constraint(percentage_constraint(0.65))
        self.button.rect.set_width_constraint(pixel_constraint(300))
        self.button.rect.set_height_constraint(pixel_constraint(100))
        self.button.rect.set_draw_color(self.game.color_handler.get_rgb('main_menu.bright_bg_2'))
        self.button.rect.set_border_radius(10)

        ## Redirect Button Image

        self.image = gui_rect(game, self.button.rect)
        self.image.image = self.game.image.load('github.png')
        self.image.set_x_constraint(center_constraint())
        self.image.set_y_constraint(center_constraint())
        self.image.set_width_constraint(aspect_constraint(1))
        self.image.set_height_constraint(percentage_constraint(0.8))
        self.image.show_rect = False

    ## Update

    def update(self):
        self.rect.update()
        self.text.update()
        self.text2.update()
        self.button.update()
        self.image.update()

        self.button.rect.tween_color(self.game.color_handler.get_rgb('main_menu.bright_bg_2'), 12)
        self.button.rect.tween_size(pixel_constraint(300), pixel_constraint(100), 12)
        if self.button.hover:
            self.button.rect.tween_color(self.game.color_handler.get_rgb('main_menu.bright_bg'), 3)
            self.button.rect.tween_size(pixel_constraint(305), pixel_constraint(105), 3)

        if self.button.pressed:
            webbrowser.open('https://github.com/willmexe/Game-Engine')

    ## Render

    def render(self):
        self.game.renderer.screen.fill(self.game.color_handler.get_rgb('main_menu.background'))
        self.rect.render()
        self.text.render()
        self.text2.render()
        self.button.render()
        self.image.render()